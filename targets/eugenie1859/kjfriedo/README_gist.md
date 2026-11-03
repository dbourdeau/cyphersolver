# NAF 11355 – Prince Napoléon dispatches, token streams (f7r, f10r, f11r, f12r)

Companion to the addendum issue (follow-up to #39 / #74). Same layout as `lasry_tokens_f9_f15_f17_f18.tsv`, with two
extra columns. 215 groups: f7r 13, f10r 9, f11r 58 (ancien 31 + nouveau 27), f12r 135.

Source: Gallica `btv1b52517729k` (pdf_page = page of the Gallica PDF: f7r 21, f10r 27, f11r 29, f12r 31).
Transcribed by hand from the scan; f10r, f11r, f12r rechecked at 400 dpi (23 Oct 2026).

Columns
- `line` – line of the message text on the sheet, counted from the first line of the body (after address and date);
  f7r: body lines 1–3 are clear text, groups on lines 4–5; f10r: groups on lines 3–4 inside the clear text;
  f12r: lines 1–2 and the start of line 3 are clear text, groups on lines 3–24, clear text resumes after 1727.
  f11r has no clear body: `line` counts the group lines, 1–4 *ancien chiffre*, 5–8 *nouveau chiffre*.
- `ordinal` – position of the group within the folio (f11r: ancien 1–31, nouveau 32–58).
- `value` / `value_status` – only the word-model anchors from the addendum (§4); everything else `?` / `unknown`.
  `anchor_word_model_dHauterive_witness`: 1299 = division holds under d'Hauterive's text of f11; with Comandini's
  "la Division", 1682 = la and 1299 = la division are also admissible. f11 ancien values (616, 2774) are not
  transferable to the nouveau key.
- `reading` – `high` or `uncertain`; the `note` gives the alternative reading.

Open points: the f12r header reads "55 parole, 133 gro."; 135 groups are read, so two groups are probably
wrong or extra. f10r: 1828 (not 1898). f12r: 2101 is one group (not 1210 1); 466 (not 1646); 1861 (not 1841).

Licence: the transcription and annotations in this TSV are released under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/). Attribution: Jozef Krajčovič, transcription of BnF NAF 11355
(Gallica btv1b52517729k). The manuscript images are not included; source gallica.bnf.fr / BnF.

Jozef Krajčovič (`kjfriedo`)
