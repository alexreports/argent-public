# Argent Public

A bilingual (French-primary / English) static **Jekyll** site documenting public
spending in Quebec — energy, the green transition, and public administration —
using only the public record. Every claim is sourced, linked, and archived.

- **No analytics, no tracking, no cookies.** Following is RSS-only.
- **Bilingual** with `/fr/` and `/en/` paths and a language toggle on every page.
- **Dual citations** (live + archived) for every source.
- Built for **GitHub Pages**.

---

## Table of contents

1. [Quick start](#quick-start)
2. [Project structure](#project-structure)
3. [How to add content](#how-to-add-content)
4. [Bilingual workflow](#bilingual-workflow)
5. [The archive helper script](#the-archive-helper-script)
6. [RSS feeds](#rss-feeds)
7. [Deploying to GitHub Pages](#deploying-to-github-pages)
8. [Connecting the argentpublic.org domain (Namecheap)](#connecting-the-argentpublicorg-domain-namecheap)
9. [Design system](#design-system)
10. [Privacy by design](#privacy-by-design)

---

## Quick start

You need **Ruby** (2.7+), **RubyGems**, and **Bundler**.

```bash
# 1. Install dependencies
gem install bundler
bundle install

# 2. Run the site locally (http://localhost:4000)
bundle exec jekyll serve

# 3. Or just build the static site into _site/
bundle exec jekyll build
```

If you prefer not to use Bundler, you can run with a global Jekyll install:

```bash
gem install jekyll jekyll-sitemap jekyll-seo-tag
jekyll serve
```

> The site visits `/` and immediately redirects to `/fr/` (French is primary).

---

## Project structure

```
argent_public/
├── _config.yml              # Site config: metadata, collections, languages
├── Gemfile                  # Ruby dependencies (github-pages gem)
├── index.html               # Root → redirects to /fr/
├── 404.html                 # Bilingual not-found page
├── robots.txt               # Crawler hints + sitemap link
├── archive_sources.py       # Helper: archive URLs → dual citation links
│
├── _data/
│   ├── nav.yml              # Navigation (FR/EN labels + URLs, linked by `key`)
│   ├── i18n.yml             # UI strings per language
│   └── corrections.yml      # Corrections log (empty by default)
│
├── _includes/
│   ├── head.html            # <head>: meta, fonts, RSS autodiscovery
│   ├── header.html          # Logo + nav + language toggle
│   ├── lang-toggle.html     # FR/EN switch (links to page counterpart)
│   ├── footer.html          # Footer + privacy note
│   ├── sources.html         # Renders dual citation links
│   └── localized-date.html  # FR/EN date formatting
│
├── _layouts/
│   ├── default.html         # Base HTML shell
│   ├── page.html            # Static pages (methodology, about, follow)
│   ├── dossier.html         # Dossier: Question→Evidence→Cost→Change
│   ├── explainer.html       # Explainer
│   └── record_entry.html    # Record entry (issuer/date/live/archived)
│
├── _dossiers/               # Dossiers collection (one file per language)
├── _explainers/             # Explainers collection
├── _record/                 # The Record collection
│
├── templates/               # Blank copy-paste templates (NOT published)
│   ├── dossier.md
│   ├── explainer.md
│   └── record-entry.md
│
├── fr/                      # French pages
│   ├── index.html           # Accueil
│   ├── dossiers.html        # Listing
│   ├── explications.html
│   ├── registre.html
│   ├── methodologie.md
│   ├── a-propos.md
│   ├── corrections.html
│   ├── suivre.md
│   └── feed.xml             # French RSS/Atom feed
│
├── en/                      # English pages (mirror of /fr/)
│   └── … + feed.xml         # English RSS/Atom feed
│
└── assets/
    ├── css/style.scss       # Design system (compiled to style.css)
    └── images/              # Logo + favicon
```

---

## How to add content

All content lives in the three **collections**: `_dossiers`, `_explainers`,
`_record`. Each piece exists as **two files** — one per language — that share a
slug so the language toggle can link them.

### 1. Dossier (Question → Evidence → Cost → Change)

Copy `templates/dossier.md` into `_dossiers/`:

```bash
cp templates/dossier.md _dossiers/2026-02-mon-sujet.fr.md
cp templates/dossier.md _dossiers/2026-02-mon-sujet.en.md
```

Edit the front matter. The four parts are front-matter fields (`question`,
`evidence`, `cost`, `change`) and accept Markdown. Sources go in the `sources:`
list with both a `live:` and an `archived:` URL.

### 2. Explainer

```bash
cp templates/explainer.md _explainers/mon-concept.fr.md
cp templates/explainer.md _explainers/mon-concept.en.md
```

The body is plain Markdown. Keep it in plain language; cite every claim.

### 3. Record entry

```bash
cp templates/record-entry.md _record/2026-02-decret-123.fr.md
cp templates/record-entry.md _record/2026-02-decret-123.en.md
```

Fill in `doc_date`, `issuer`, `live_link`, `archived_link`, and `description`.

> **Listing & sorting** happens automatically: each listing page filters its
> collection by `lang` and sorts newest-first. New items also appear in the
> matching-language RSS feed.

---

## Bilingual workflow

Every page declares two front-matter keys that make the bilingual system work:

```yaml
lang: fr                              # fr | en
alt_lang_url: /en/dossiers/mon-sujet/ # URL of the SAME content in the other language
```

- `lang` tells layouts, feeds, and listings which language a file belongs to.
- `alt_lang_url` is what the **FR/EN toggle** links to. Set it on both files so
  the toggle jumps directly between counterparts. If omitted, the toggle falls
  back to the other language's home page.
- For collection items, keep the **same slug** in both `permalink`s (only the
  `/fr/…` vs `/en/…` prefix and translated segment differ).

UI labels (nav, buttons, field names) are translated centrally in
`_data/i18n.yml` and `_data/nav.yml` — you rarely need to touch templates.

---

## The archive helper script

`archive_sources.py` submits source URLs to the **Wayback Machine** and
**archive.today**, then prints ready-to-paste dual citation links. Standard
library only — no `pip install` needed.

```bash
# Archive one or more URLs and print Markdown citations
python3 archive_sources.py https://www.legisquebec.gouv.qc.ca/…

# Emit a YAML block ready for a dossier's `sources:` front matter
python3 archive_sources.py --yaml https://example.gouv.qc.ca/decret-123

# Read URLs from a file (one per line)
python3 archive_sources.py --file urls.txt --yaml

# Only look up existing snapshots (don't submit new captures)
python3 archive_sources.py --no-save https://example.gouv.qc.ca/x
```

Example YAML output to paste under `sources:`:

```yaml
sources:
  - title: "REPLACE WITH SOURCE TITLE"
    live: "https://example.gouv.qc.ca/decret-123"
    archived: "https://web.archive.org/web/2026…/https://example.gouv.qc.ca/decret-123"
```

> archive.today sometimes rate-limits automated requests. When it does, the
> script still returns the Wayback link plus an `archive.ph/newest/…` URL you can
> open by hand to confirm or create the copy.

---

## RSS feeds

Two independent Atom feeds are generated (no third-party plugin):

- French — `/fr/feed.xml`
- English — `/en/feed.xml`

Each feed merges that language's dossiers, explainers, and record entries,
newest first. The correct feed is auto-discoverable from every page's `<head>`,
and both are linked from the **Follow / Suivre** page.

---

## Deploying to GitHub Pages

There are two common setups. **A custom domain (argentpublic.org) is the
recommended path** and is described below.

### Option A — User/Org or custom-domain site (recommended)

1. Create a GitHub repository (e.g. `argent-public`).
2. Push this project:
   ```bash
   git init
   git add .
   git commit -m "Initial Argent Public site"
   git branch -M main
   git remote add origin git@github.com:<you>/argent-public.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Build and deployment**
   - **Source:** *Deploy from a branch*
   - **Branch:** `main` / `/ (root)`
4. Because we serve from a custom domain, keep `baseurl: ""` in `_config.yml`
   (already set).
5. Add your domain (see next section). GitHub writes a `CNAME` file for you;
   commit it if prompted.

### Option B — Project site at `username.github.io/argent-public`

If you deploy WITHOUT a custom domain, set the base path so links resolve:

```yaml
# _config.yml
baseurl: "/argent-public"   # must match the repo name
url: "https://<username>.github.io"
```

Then rebuild. (Switch `baseurl` back to `""` when you move to the custom domain.)

> **Plugins:** this site uses only `jekyll-sitemap` and `jekyll-seo-tag`, both on
> the GitHub Pages allow-list, so the default Pages builder works out of the box.
> If you later add unsupported plugins, switch to a GitHub Actions build.

---

## Connecting the argentpublic.org domain (Namecheap)

You'll point the apex domain `argentpublic.org` (and `www`) at GitHub Pages.

### Step 1 — Tell GitHub about the domain

1. Repo → **Settings → Pages → Custom domain** → enter `argentpublic.org` → **Save**.
   This creates a `CNAME` file in the repo (commit it if it isn't auto-committed).
2. Leave **Enforce HTTPS** unchecked until DNS has propagated, then enable it.

### Step 2 — Configure DNS in Namecheap

Log in to Namecheap → **Domain List** → **Manage** next to `argentpublic.org` →
**Advanced DNS**. Remove any default "parking" records, then add:

**Apex (`argentpublic.org`) — four A records to GitHub Pages:**

| Type     | Host | Value           | TTL       |
|----------|------|-----------------|-----------|
| A Record | `@`  | `185.199.108.153` | Automatic |
| A Record | `@`  | `185.199.109.153` | Automatic |
| A Record | `@`  | `185.199.110.153` | Automatic |
| A Record | `@`  | `185.199.111.153` | Automatic |

**(Optional but recommended) IPv6 — four AAAA records:**

| Type        | Host | Value                  |
|-------------|------|------------------------|
| AAAA Record | `@`  | `2606:50c0:8000::153`  |
| AAAA Record | `@`  | `2606:50c0:8001::153`  |
| AAAA Record | `@`  | `2606:50c0:8002::153`  |
| AAAA Record | `@`  | `2606:50c0:8003::153`  |

**`www` subdomain — one CNAME:**

| Type        | Host  | Value                    | TTL       |
|-------------|-------|--------------------------|-----------|
| CNAME Record| `www` | `<username>.github.io.`  | Automatic |

> Replace `<username>` with your GitHub username/org. Note the trailing dot is
> how Namecheap stores it; the UI may add it for you.

### Step 3 — Set `url` and verify

1. In `_config.yml` set:
   ```yaml
   url: "https://argentpublic.org"
   baseurl: ""
   ```
2. Wait for DNS to propagate (minutes to a few hours). Check with:
   ```bash
   dig +short argentpublic.org
   dig +short www.argentpublic.org
   ```
3. Back in **Settings → Pages**, confirm the domain shows a green check, then
   tick **Enforce HTTPS**.

> **Namecheap tip:** if you use Namecheap's *URL Redirect Record* for the apex,
> remove it — GitHub Pages needs real A/AAAA records, not a redirect.

---

## Design system

- **Colours:** dark green `#125b38`, blue `#0057b7`, black body text `#111`,
  wordmark navy `#2e3a47` (from the logo).
- **Type:** **Lexend** (Google Fonts) for headlines; **Times New Roman** (serif)
  for body. Body text is large — 19px desktop, 18px on small screens.
- **Look:** clean, newspaper-like, generous reading width, hairline rules.
- **Accessibility:** semantic HTML, skip link, visible focus styles, strong
  contrast, responsive down to mobile, print stylesheet.

Edit `assets/css/style.scss`; Jekyll compiles it to `style.css` on build.

---

## Privacy by design

- No analytics scripts, no tag managers, no cookies, no fonts that profile users
  beyond Google Fonts' CSS delivery (you can self-host the font if you prefer).
- `<meta name="referrer" content="no-referrer">` is set.
- The only way to follow the site is RSS — no email capture, no accounts.

---

## License & editorial

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for editorial standards (sourcing
discipline, archiving, corrections, tone). Content is published from the public
record; sources are linked and archived.
