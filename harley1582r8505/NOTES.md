# "L'Estat du Roy de Navarre et de son party en France" (BL Harley MS 1582 ff. 263-264; DECODE R8505)

Catalogue entry "Unknown sender to unknown recipient, 2 ciphertexts, BL Harley MS 1582 (R8501, R8505)".
Worked 22 September 2026.

**Outcome: attempted, open.** The two records split cleanly:

- **R8501** (Harley 1582 ff. 71-72) is *not* an open problem: it is one of Sir Edward Stafford's 1586 despatches
  and it carries its own contemporary decipherment on f. 72r. That decipherment was transcribed, and the letter
  key rebuilt from it, in the sibling target `harley1582r8500/` (see its NOTES; `f72r_clear.txt`, `key.tsv`).
  Nothing is left unread there.
- **R8505** (ff. 263-264, 4 images) is a different document in a different cipher, and is the real target. It is
  **identified here** and **transcribed here in full for the first time** (about 3,600 sign tokens), but **not read**.

## What R8505 is

A French political memoir, headed on f. 263r:

> *L'Estat du Roy de Navarre & de son party en France*

Four sides of small secretary hand, clear French throughout with long runs of graphic-sign cipher written inline in
the same hand, in mid-sentence, exactly as in the Stafford letters of the same volume. Internal dates: the peace
"de l'an 1577", Brouage "l'an 1580", "l'an 1576", so it was written after 1580; the tone (Navarre as a possible
heir, the Religion's places de sûreté, Monsieur still a factor, the "party" being surveyed for an outside reader)
places it with the mid-1580s Navarre embassies to England. Contents of the clear passages: Navarre's two
"qualitez" (first prince of the blood, chief of the reformed churches); the places he holds in Guyenne, Languedoc,
Dauphiné, Provence; named gentlemen and governors (Turenne, Châtillon, Laval, Montgomery, Rohan, Lesdiguières,
Ségur, La Rochefoucauld…); garrison and harquebus numbers; the Catholic and German alliances; the marriage
question. The ciphered runs carry the sensitive parts of exactly those paragraphs.

DECODE's record is thin and partly wrong: no title, no date, no author, language given as "English?", and the
whole is filed under "unknown". The corrections are queued for DECODE (`decode_updates/queue.json`).

## The cipher

- **Graphic signs**, about 50 distinct shapes (Greek-like and geometric: L, Γ, Π, Ш, β, ε, ω with a bar, ψ, φ, χ,
  η, ∂, ⧗, crossed and looped verticals), written spaced out sign by sign, with no word division. Sign chart with
  shape descriptions: `signs.md`.
- **Dot groups** (`:`), one to four dots, punctuate the runs; they do not behave like letters here.
- **Nomenclator numbers** written between dots: 6, 21, 26, 36, 51, 57, 72, 81, 99, 721 - almost certainly names
  (Navarre, the King, the Religion, Spain, Monsieur…).
- Statistics of the transcription (3,630 tokens, 56 names incl. aliases): index of coincidence **0.040**, far below
  a plain substitution (~0.078) and consistent with a **homophonic** alphabet; Sukhotin's vowel test splits the
  signs into ~20 "vowel" signs carrying 51% of the text and the rest consonantal, which is the profile of letters
  with several homophones each, not of a syllabary.

## What was done

1. Fetched the four full-resolution images with the DECODE session cookie (`img/`, git-ignored, BL material).
2. Identified the document from the clear text (title, date bracket, contents) - new; DECODE has none of this.
3. Transcribed every cipher run on all four sides: `ct_p1.txt` (f. 263r, by hand here), `ct_p2.txt` (f. 264r),
   `ct_p3.txt`, `ct_p4.txt` (versos). Format and sign names in `signs.md`. ~3,630 sign tokens.
4. Cryptanalysis (`solve.py`, `solve2.py`, `solve3.py`, shared `lang/` models):
   - homophonic letter annealing, order-4/5 French LM, unigram-frequency penalty, up to 20 restarts x 400k moves,
     whole text and page by page (to guard against sign-name drift between transcribers);
   - syllabic variant (each sign = letter, syllable, double or null): collapses to degenerate keys;
   - language control: the same anneal under English, Spanish, Italian and 17th-c. French models scores the same
     as the 1530-1600 French model (about -2.9/char against -1.9 for real text), i.e. no language fits.
   No key was recovered; nothing reads.

## Why it did not come out

Three candidate causes, in order of likelihood:

1. **Transcription noise.** The signs are small, faint and closely similar in several families (b/T/Tu, ω/ϖ/ωʃ,
   ε/Ɛ-crossed, Π/Π-with-hook, ψ/y/cy). Three readers (one of them me) produced the four files and flagged those
   splits as uncertain; a 10-15% sign error rate is enough to defeat homophonic annealing at this text length.
2. **More than a homophonic alphabet.** The 1583 letter at BnF 500 Colbert 401 f. 143, written to Ségur in the
   same milieu, describes the Navarre ciphers of these years as having "toutes choses tellement dispersées en
   lettres, syllabes, doubles, nulles… Les noms sont en lettres et syllabes" (see `../segur/NOTES.md`). If this
   key mixes letters with syllables, doubles and nulls, a pure letter anneal cannot converge.
3. **Length.** Homophonic keys of ~50 signs over ~3,600 tokens are near the practical limit for ciphertext-only
   annealing without a crib.

## Remaining gaps

- open-key: the whole of R8505 (~3,630 sign tokens) is unread; no key material for it has been found on the
  DECODE record, in the volume's other records (R8498-R8506 were checked) or in print.
- needs-second-transcription: the sign chart needs one reader to re-read all four sides in one pass against a
  fixed chart, resolving the b/T, ω-family, ε-family and Π-family splits, before another attack is worth running.

## Escalation

- [x] siblings: all DECODE records of Harley 1582 (R8498, R8499, R8500, R8501, R8502, R8504) and R8506 checked;
      none is a key, none is in this cipher. R8501 is Stafford's, already read in `harley1582r8500/`.
- [x] clear-pages: the memoir's own clear text was read and used for context; there is no interlinear or marginal
      decipherment anywhere on ff. 263-264.
- [x] known-keys: the Ségur/Navarre key recovered in `../segur/` is numeric (1-123), not graphic, and does not
      apply; no graphic-sign Navarre key of the 1580s is on DECODE or in Tomokiyo's published tables.
- [x] print: searched for the memoir in print ("L'Estat du Roy de Navarre et de son party en France") and in the
      Calendars of State Papers Foreign for 1583-86; not found calendared with a decipherment.
- [x] key-rebuild: attempted, see above; failed.
- [ ] retry: worth one more session after a single-reader re-transcription, and after a search for another copy of
      the memoir (BnF Dupuy/Fonds français, Mémoires de la Ligue) whose ciphered passages might be in clear - a
      clear copy would be a complete crib.

## Files

`img/` (git-ignored BL images), `signs.md` (sign chart), `ct_p1..p4.txt` (transcription), `solve*.py` (attacks),
`run*.txt`/`r3*.txt` (best keys and their decrypts), `profile.json`.
