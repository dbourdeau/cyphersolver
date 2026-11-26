# PREREG — sal-stubbs, page (1) (box script) — written 2026-11-23 BEFORE any key is built or any decoding tried

Document: Society of Antiquaries of London, archives, THO/57/127, image « THO 57 127 a » (page numbered (1)).
Input (frozen): blind/P1_final.tsv = blind pass A + blind pass B + blind arbiter (Opus sub-agents), and P1_lines.json (reading order: 42 main lines top to bottom, left to right; rows L38 then L37 form one line split by a dash; margin columns M* excluded from both training and measure, read afterwards). SHA-256 of the inputs in PREREG_P1.sha256.
Known before this PREREG: sign inventory and frequencies only (34 shape codes, about 23 with frequency > 10; no word division) — compatible with a monoalphabetic substitution of a 23–24 letter alphabet.

## Hypothesis
H1: monoalphabetic simple substitution, one shape code (set of wedge positions) = one letter; possible nulls; language English (H1-en) or Latin (H1-la). Language is decided on the training portion only and written into the frozen key ("lang").
Not H1 (e.g. homophones, nomenclator, shorthand): reported as such, no forcing.

## Portions
- Training: lines 0–32 of P1_lines.json (rows L00–L32, 1,084 signs). The key is built ONLY from these lines (frequency analysis, hill-climbing and/or manual word reading).
- Held-out: lines 33–41 (rows L33–L42, 315 signs >= 300) = prereg/heldout_P1.json. Not looked at after decoding of any kind, not used to adjust the key. One single measure; afterwards the portion is burnt.

## Key freeze
The key (prereg/KEY_P1.json: {"lang", "map": sign -> letter or "" for null}) is frozen with SHA-256 (appended to PREREG_P1.sha256 via KEY_P1.sha256) BEFORE the measure.

## Measure (prereg/score.py, frozen here)
Decode the held-out sign sequence with the key ('?' flags stripped; unknown sign -> '?'). Normalise: lower case, j->i, v->u, letters only.
Lexicon: word forms of frequency >= 2 and length >= 3 from the corpora in lm/ for the key's language (en_*: Addison papers 1790 vol. 2, Defoe Robinson Crusoe, Sir Roger de Coverley/Spectator; la_*: Caesar, Commentarii) + a fixed list of 1–2-letter words (in score.py). SHA-256 of corpora in lm/SOURCES.sha256. No word added by hand.
Score S = share of decoded letters covered by a maximum-coverage segmentation of the continuous decoded string into lexicon words.
Controls: 200 keys obtained by permuting the VALUES of the frozen key among its signs (random.Random(1700+k), k = 0..199); same score.
Criterion (fixed now): PASS iff S >= 0.85 AND S >= max(controls) + 0.30. Fewer than 300 signs = « non mesurable » (not the case here: 315).

## Reading count (rule #728)
After the measure, all lines (incl. margin, if its reading order and orientation can be established) are decoded with the frozen key. Sure words only count, over the number of cipher words (words of the plaintext); probable (one sign corrected), restored (sense-based) and unresolved words are holes. < 40 words: « read » with <= 2 holes. One fiche per letter with clear text and justifications.
