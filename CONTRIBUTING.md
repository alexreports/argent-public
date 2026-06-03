# Contributing & Editorial Standards — Argent Public

Argent Public exists to make Quebec's **public spending** legible — energy, the
green transition, and public administration — using only the public record.
These standards are not optional. They are what makes the publication credible
and legally defensible.

---

## 1. The core rule: publish only the public record

We publish what is **documented and public**: decrees, contracts, budgets,
financial statements, audits, official reports, registries, and on-the-record
statements. If it is not in the public record, it does not go on the site.

- **No rumour. No leaks. No anonymous tips presented as fact.**
- **No speculation.** We document what *is*. Where the record is silent or
  incomplete, we say so plainly rather than infer, imply, or fill gaps.
- **No partisan framing.** We do not endorse parties, candidates, or causes.

---

## 2. Sourcing discipline

Every factual claim must be traceable to a public document.

- **One claim → one source.** Numbers, dates, names, and quotations each link to
  the document that supports them.
- **Quote precisely.** Use exact figures and wording. Do not paraphrase a number.
- **Cite the primary source**, not a secondary report about it, wherever possible
  (e.g. the decree itself, not an article describing the decree).
- **Mark context clearly.** Facts and analysis must be visibly separate. Any
  interpretation is labelled as such and stays minimal.

---

## 3. Archiving: every source gets a dual link

Links rot and pages change. Every source therefore carries **two** links:

1. **Live link** — the original URL.
2. **Archived copy** — a snapshot on the Wayback Machine and/or archive.today.

Use the helper before publishing:

```bash
python3 archive_sources.py --yaml <URL>
```

Paste the resulting block into the item's `sources:` front matter. Confirm the
archived copy actually renders the relevant content before relying on it.

---

## 4. The four-part dossier structure

Every dossier answers the same four questions, in order:

1. **The question** — a precise, verifiable question we set out to answer.
2. **The evidence** — the public documents that answer it, each cited.
3. **The cost** — what it means for public funds, with sourced figures.
4. **The change sought** — the decision, disclosure, or accountability expected.

Keep the question neutral. Where the facts raise a question, ask it — never
presume the answer.

---

## 5. Explainers

- Plain language first. Define every technical term on first use.
- Still fully sourced — an explainer is not an opinion piece.
- Aim to make a non-specialist able to read a dossier afterwards.

---

## 6. The Record

The Record is our archive of primary documents. Each entry includes:

- **Title**, **Date** of the document, **Issuer**;
- **Live link** and **Archived link**;
- A short, factual **description** of what the document is.

Add documents to the Record even before a dossier cites them — it is the
evidentiary backbone of the site.

---

## 7. Tone

Calm, neutral, evidence-first. We do not editorialize, sensationalize, or use
loaded language. The strength of the work is the documentation, not the adjectives.

- Prefer "the contract commits $X" over "a staggering $X".
- Attribute every characterization to a document or an official.
- Let readers draw conclusions from sourced facts.

---

## 8. Corrections

Accuracy is the product. When we get something wrong:

1. Fix the content.
2. Log the correction in `_data/corrections.yml` (in **both** languages), with a
   date, the item affected, and what changed.
3. Never silently edit a substantive factual error — the correction log is public.

---

## 9. Bilingual parity

French is primary; **everything** must also exist in English (and vice-versa).

- Create both language files with a shared slug and matching `alt_lang_url`.
- Translate faithfully — no extra claims in one language that aren't in the other.
- Translate UI strings in `_data/i18n.yml`, not inside templates.

---

## 10. Legal care

This publication is built to withstand scrutiny.

- Stick to the public record and exact quotation; that is the first line of
  defence.
- Distinguish fact from any commentary.
- Where a claim is sensitive, ensure the archived primary source clearly supports
  it before publishing, and route it through editorial/clearance review per your
  internal process.
- When in doubt, leave it out and keep reporting.

---

## 11. Privacy (non-negotiable)

The site collects nothing: no analytics, no cookies, no tracking, no email
capture. Do not add scripts, embeds, pixels, or third-party widgets that would
change that. Following is RSS-only, by design.

---

## Pre-publish checklist

- [ ] Every factual claim is linked to a public document.
- [ ] Every source has both a live link and a working archived copy.
- [ ] Figures and quotations are exact.
- [ ] Facts are kept separate from any analysis.
- [ ] Dossier follows Question → Evidence → Cost → Change.
- [ ] French **and** English versions exist, with matching `alt_lang_url`.
- [ ] Tone is calm, neutral, non-partisan.
- [ ] No tracking/analytics/embeds were introduced.
- [ ] Builds cleanly (`bundle exec jekyll build`) with no errors.
