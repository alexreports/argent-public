---
# ============================================================
#  DOSSIER TEMPLATE
#  Copy to _dossiers/ and rename, e.g.:
#    _dossiers/2026-01-mon-dossier.fr.md   (lang: fr)
#    _dossiers/2026-01-mon-dossier.en.md   (lang: en)
#  Keep the SAME slug part so the language toggle links match.
# ============================================================
layout: dossier
lang: fr                       # fr | en
title: "Titre du dossier"
slug: mon-dossier              # shared slug; used for alt_lang_url
permalink: /fr/dossiers/mon-dossier/
alt_lang_url: /en/dossiers/mon-dossier/
date: 2026-01-15
updated:                       # optional: YYYY-MM-DD
theme: "Énergie"               # e.g. Énergie / Transition verte / Administration
summary: "Résumé d’une phrase, neutre et factuel."

# ---- The four-part structure (Markdown allowed in each) ----
question: |
  Posez ici la question factuelle, précise et vérifiable que le dossier examine.

evidence: |
  Présentez les preuves issues du registre public. Citez chaque chiffre.
  Renvoyez aux sources numérotées ci-dessous, p. ex. [1], [2].

cost: |
  Chiffrez ce que cela représente pour les fonds publics, avec sources.

change: |
  Décrivez la décision, la correction ou la reddition de comptes attendue.

# ---- Sources: dual citation links (live + archived) --------
sources:
  - title: "Décret 0000-2026, Gazette officielle du Québec"
    live: "https://www.example.gouv.qc.ca/document"
    archived: "https://web.archive.org/web/2026/https://www.example.gouv.qc.ca/document"
    note: "Note facultative."
  - title: "Rapport annuel, Société d’État"
    live: "https://www.example.gouv.qc.ca/rapport.pdf"
    archived: "https://archive.ph/abcde"
---

<!-- Optional free-form context below the four-part structure.
     Keep it factual; mark any analysis clearly. Leave empty if not needed. -->
