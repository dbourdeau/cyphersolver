# Fra Guglielmo Vizani to the Comte de Césy, Prinkipo 8 Oct 1637 (BnF Français 16158 ff. 292-294). READ (outside key, 1 Oct 2026)

TARGETS.md listed "Fra Guglielmo Vizani (1637) - no transcriptions" (from Cryptiana's unsolved list). On 1 Oct 2026 Satoru (satoru.net, with Claude Opus 5.5
under his direction) emailed a transcription, key and reading and published them at https://satoru.net/crypt/vizani/. Nothing here predates it: the first
work on this target is the verification below.

## What the letter is

A letter of 8 October 1637 from Fra Guglielmo Vizani, Prinkipo (Isola di S. Principe), to the French ambassador at Constantinople, Philippe de Harlay, comte de
Césy (the address leaf f. 293v reads "All'Ill.mo ... Sig. Conte di Cesy in Constantinopoli"). BnF Français 16158, ff. 292-294; Gallica ark btv1b9061541x,
view 295 for f. 292r. Clear Italian with eight cipher lines (54 cipher words, 190 signs). A second letter of the same date, f. 294, has one cipher line.

## The reading (Satoru; checked here)

"Il signor [231] m'ha mandato a domandare se li quattro mila scuti [?] a [31] di monsignor Beria d'ordine di V.E. furono promessi a d(ett)o Sig.r, il quale ... e
vicino all'ottenere il patiarchato per se. ... [64?] Monsignor Beria spera che tra due mesi sia per esser mutato; il [36] e dattone? un suo partiale, e per su(a) [198]
havere l'intento a [227] e incertissimo." The clear passages say that orders changed on 30 May and that nothing can be said by letter while the plague lasts.
His identification (Beria = Cyril Kontaris of Veroia, "close to obtaining the Patriarchate"; Kontaris took office 20 June 1638, Lucaris was strangled 27 June) is his and fits.

The cipher: homophonic symbol cipher with word dividers (|), signs for tt and ss, word signs for il and che, numeric name codes. Key: `key.json`; transcription:
`cipher_words.tsv` (copied from his page with credit; glyph shapes approximated with look-alike characters).

## What was checked here (1 Oct 2026)

- `dec.py` re-decodes all 54 words from his transcription with his key: 46 agree with the plain he gives, 2 differ (both "monsignor": his glyph strings omit an s and an n,
  an abbreviation), the rest are name codes or his own query marks.
- Italian per-letter score of the decode: -1.78 (`it-cinquecento`; -1.99 `it-modern`), against a best of -4.30 (mean -5.30) over 200 keys of the same shape with the letters
  shuffled among the sign classes (-6.66 / -8.49 under `it-modern`).
- Compared with the Gallica image (IIIF crop of f. 292r, git-ignored): the first nine words of line 1 agree sign by sign (the stroke, 231 and the word divider included), and the
  code "64" before the second "Monsignor Beria" is two digits, as he has it. (Brice Dudout, 14 Nov 2026, finds it undecided: see below.) The whole transcription was not re-checked by eye; his is a first transcription.
- His own controls (on his page, not re-run): 16 synthetic ciphers of the same size solved in 15 cases (97-100% of letters); 24 shuffled versions of the text scored -1294 to -1236 against -1073.7 for the real one; 5 of 8
  seeds gave the identical reading. The same key reads the cipher line of f. 294 (claimed; not checked here).
- Small points for him: the page says 53 words and lists 54; the viewer's last line range stops before "incertissimo".

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: the letter is Italian of 1637 (not Spanish). Satoru's reading: plain 0.333, explicit 0.667 on six sentences; the holes are the five name codes (no key material), one unread sign and 'dattone?'. Each sentence builds around the codes: only scattered codes open. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## Independent verification by Brice Dudout (PR #565, 14 Nov 2026)

Brice Dudout (PR #565, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded `cipher_words.tsv` from `key.json` alone (47
of 54 words as published; the other 7 are the known abbreviations, query marks and open signs) and re-read the doubtful signs on the
Gallica image of f. 292r: 231 and 31 are digits, though the writer's 1 has the shape of the e homophone; "li?" is a crossed 3, distinct
from the 3 of 31, with no value; the second sign of "64" is written exactly like ꝗ, so the group could be two key signs (a, m) as well as the code 64: undecided, "[64?]" stays a guess; dattone as transcribed. No key correction. His
decoder re-run here gives the same figures; the image re-reading is his (not repeated). The read share 0.926 (read in part) stands.

## Remaining gaps

- name codes 31, 36, 64?, 198, 227, 231 - blocker: no-key-material; Césy's minutes for 1637-38 (BnF fr. 16154-16155) are microfilm only, no code list known
- two signs (the "li?" word and one after "scuti") unread, and "dattone?" - blocker: illegible; single words, no second context

## Escalation

- [x] siblings: the companion letter f. 294 reads with the same key (his claim); no other Vizani cipher known
- [x] clear-pages: none; the clear text around each cipher line is the context he used
- [x] known-keys: no Vizani or Césy code list known
- [x] print: Halphen 1904 (Louis XIII to Césy) for context, not for the cipher
- [n/a] key-rebuild: key complete for the letters; only name codes open
- [n/a] retry: nothing new to retry

Contamination: the reading came from outside before any work here (email 1 Oct 2026); none existed before that.
