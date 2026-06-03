#!/usr/bin/env python3
"""
archive_sources.py — Argent Public source-archiving helper
===========================================================

Submit one or more source URLs to BOTH the Wayback Machine
(web.archive.org) and archive.today, then print Markdown- and
YAML-ready *dual* citation links (live + archived) for pasting
straight into a dossier, explainer, or record entry.

Why: every claim on Argent Public must carry a live link AND an
archived copy, so the evidence survives even if the original page
is changed or removed.

--------------------------------------------------------------------
USAGE
--------------------------------------------------------------------
  # One or more URLs on the command line:
  python3 archive_sources.py https://example.gouv.qc.ca/decret-123

  # Several at once:
  python3 archive_sources.py URL1 URL2 URL3

  # From a file (one URL per line):
  python3 archive_sources.py --file urls.txt

  # Emit YAML ready for a `sources:` front-matter block:
  python3 archive_sources.py --yaml https://example.gouv.qc.ca/x

  # Only fetch the LATEST existing Wayback snapshot (do not submit):
  python3 archive_sources.py --no-save https://example.gouv.qc.ca/x

--------------------------------------------------------------------
NOTES
--------------------------------------------------------------------
* Standard library only — no pip install required.
* archive.today is best-effort: it sometimes rate-limits or blocks
  automated submissions. When it does, the script still returns the
  Wayback link and an archive.today *search* URL you can open by hand.
* Be polite: the script pauses a few seconds between submissions.
* Nothing here tracks anyone; it only talks to the two archives.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "ArgentPublic-ArchiveHelper/1.0 (+https://argentpublic.org)"
TIMEOUT = 60  # seconds


# --------------------------------------------------------------------
# HTTP helper
# --------------------------------------------------------------------
def _request(url: str, method: str = "GET") -> tuple[int, str, dict]:
    """Perform a request, returning (status_code, final_url, headers)."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.geturl(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, url, dict(e.headers or {})
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"  ! network error: {e}", file=sys.stderr)
        return 0, url, {}


# --------------------------------------------------------------------
# Wayback Machine
# --------------------------------------------------------------------
def wayback_latest(url: str) -> str | None:
    """Return the most recent existing Wayback snapshot URL, if any."""
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8", "replace"))
        snap = data.get("archived_snapshots", {}).get("closest", {})
        if snap.get("available") and snap.get("url"):
            # Normalise to https
            return snap["url"].replace("http://", "https://", 1)
    except Exception as e:  # noqa: BLE001 - best effort
        print(f"  ! wayback lookup failed: {e}", file=sys.stderr)
    return None


def wayback_save(url: str) -> str | None:
    """Ask the Wayback Machine to capture `url` now; return snapshot URL."""
    save_url = "https://web.archive.org/save/" + url
    status, final_url, headers = _request(save_url, method="GET")
    # The save endpoint usually redirects to the snapshot, or exposes it
    # via the Content-Location header.
    if "web.archive.org/web/" in final_url:
        return final_url
    loc = headers.get("Content-Location") or headers.get("content-location")
    if loc:
        return "https://web.archive.org" + loc
    # Fall back to whatever snapshot now exists.
    return wayback_latest(url)


# --------------------------------------------------------------------
# archive.today
# --------------------------------------------------------------------
def archive_today_save(url: str) -> str | None:
    """Best-effort submission to archive.today (archive.ph)."""
    submit = "https://archive.ph/submit/"
    data = urllib.parse.urlencode({"url": url}).encode()
    req = urllib.request.Request(
        submit, data=data, method="POST", headers={"User-Agent": USER_AGENT}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            final = resp.geturl()
            refresh = resp.headers.get("Refresh", "")
        if "archive." in final and "/submit" not in final:
            return final
        # Some responses carry the location in a Refresh header: "0; url=..."
        if "url=" in refresh:
            return refresh.split("url=", 1)[1].strip()
    except urllib.error.HTTPError as e:
        # 429/403 are common when rate-limited.
        print(f"  ! archive.today returned HTTP {e.code} (rate-limited/blocked)",
              file=sys.stderr)
    except Exception as e:  # noqa: BLE001
        print(f"  ! archive.today submission failed: {e}", file=sys.stderr)
    return None


def archive_today_search(url: str) -> str:
    """A URL a human can open to find/create an archive.today copy."""
    return "https://archive.ph/newest/" + url


# --------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------
def process(url: str, do_save: bool) -> dict:
    """Archive one URL and return a result dict."""
    print(f"\n→ {url}")
    result = {"live": url, "wayback": None, "archive_today": None}

    # Wayback ----------------------------------------------------------
    if do_save:
        print("  · submitting to Wayback Machine …")
        result["wayback"] = wayback_save(url)
        time.sleep(2)
    if not result["wayback"]:
        result["wayback"] = wayback_latest(url)
    print(f"  · wayback: {result['wayback'] or 'not available'}")

    # archive.today ----------------------------------------------------
    if do_save:
        print("  · submitting to archive.today …")
        result["archive_today"] = archive_today_save(url)
        time.sleep(3)
    if not result["archive_today"]:
        result["archive_today"] = archive_today_search(url)
        print(f"  · archive.today: open to confirm → {result['archive_today']}")
    else:
        print(f"  · archive.today: {result['archive_today']}")

    return result


# --------------------------------------------------------------------
# Output formatters
# --------------------------------------------------------------------
def fmt_markdown(r: dict) -> str:
    archived = r["wayback"] or r["archive_today"]
    parts = [f"[Live link]({r['live']})"]
    if r["wayback"]:
        parts.append(f"[Archived (Wayback)]({r['wayback']})")
    if r["archive_today"]:
        parts.append(f"[Archived (archive.today)]({r['archive_today']})")
    return f"- {r['live']}  \n  " + " · ".join(parts)


def fmt_yaml(r: dict) -> str:
    archived = r["wayback"] or r["archive_today"] or ""
    return (
        "  - title: \"REPLACE WITH SOURCE TITLE\"\n"
        f"    live: \"{r['live']}\"\n"
        f"    archived: \"{archived}\""
    )


# --------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Archive source URLs to Wayback Machine + archive.today "
                    "and print dual citation links.")
    ap.add_argument("urls", nargs="*", help="One or more URLs to archive.")
    ap.add_argument("--file", "-f", help="Read URLs from a file (one per line).")
    ap.add_argument("--yaml", action="store_true",
                    help="Emit a YAML `sources:` block instead of Markdown.")
    ap.add_argument("--no-save", action="store_true",
                    help="Do not submit new captures; only look up existing ones.")
    args = ap.parse_args()

    urls: list[str] = list(args.urls)
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as fh:
                urls += [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
        except OSError as e:
            print(f"Cannot read {args.file}: {e}", file=sys.stderr)
            return 2

    if not urls:
        ap.print_help()
        return 1

    results = [process(u, do_save=not args.no_save) for u in urls]

    print("\n" + "=" * 60)
    print("YAML front-matter block:" if args.yaml else "Markdown citations:")
    print("=" * 60)
    if args.yaml:
        print("sources:")
        for r in results:
            print(fmt_yaml(r))
    else:
        for r in results:
            print(fmt_markdown(r))
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
