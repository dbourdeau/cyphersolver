# Plan, frozen before any decoding: Guaras to Don John, London, 15 Feb 1577 (TNA SP 70/143 f. 93)

Written 27 Nov 2026, about 23:20-23:27 EST, by the AI agent working register lead `guaras1577-donjohn` (Claude Opus 5.5).
No person has checked it. Its SHA-256 and the time of freezing are in `PLAN.sha256`. Nothing below has been run when
this file is frozen. Up to now I have seen the page images, the two blind transcriptions (as files, plus the first
lines of each) and the 1574 key file; I have not applied any key or looked at Kervyn de Lettenhove's printed text.

## Inputs (SHA-256)

- `transcription_A.txt` 44d182f1f39af8a7ffeceb801fd2d00f1c57395f11cd190efe2c6fe59f54b506 (helper A, Opus, blind)
- `transcription_B.txt` a53c7a0f44d2df45005f60b4faf36db9deb49c591c4c0e4ad20865330e46b978 (helper B, Opus, blind,
  worked from the last line back)
- `key_guaras1574_from_main_c09aa9ed7d.json` 0aa283dc99c7963e994b3b61628e5dd729af5df881c877cdddf3efb6ac08e681:
  Andrew's 1574 key exactly as on dbourdeau/cyphersolver main c09aa9ed7d,
  `research/vetting_2026-11-17_ajbeling/1001/key.json` (merged with #743; wording of sign 8 from #892).
- Language model text: Zurita, *Historia del rey don Hernando*, 1580 (`output/claver1497_verify_2026-11-16/raw/
  zurita1580_bub_gb_XgWt5lHz3_MC_djvu.txt`, 75979b15...). Real-Spanish yardstick: Pulgar, *Cronica*, 1780
  (`.../pulgar1780_bub_gb_RB9nAr9N5AkC_djvu.txt`, b265e4c7..., first 5% skipped).

## Step 1. Compare the two transcriptions (no values used)

1.1 Notation bridge, fixed from the two readers' own sign notes only: A `u T t` = B `u S T`; A `u T P` = B `u S P`;
A `u T 6` = B `u y 6`; A `h` = B `t` when B's `t` stands alone (the H-like sign). Gap marks, underlines, commas,
points and slashes are dropped; dotted numbers stay as single tokens (`#35`). Everything else is compared as written.
1.2 Each line is aligned token by token (difflib SequenceMatcher). Agreement = tokens in matching blocks / aligned
positions (matches + max of the two sides of each non-matching block). Reported per line and overall.
1.3 A reconciled stream keeps agreed tokens and writes `?` for every disagreement. It is hashed before step 2.

## Step 2. Apply the 1574 key unchanged

2.1 Each cipher token that is a sign of the 1574 key (`d e f g h i m n o p q r s t z c 6 k x 8 l`, lower case)
gets its 1574 plain letter; every other token (capitals, other digits, dotted numbers, `?`) is a hole `#`. Applied
separately to A, to B and to the reconciled stream.
2.2 Measures, each computed once:
- coverage = tokens with a value / all tokens;
- letter-trigram score: mean log-probability per letter of the decoded letters (holes break the stream into runs;
  only trigrams inside runs count), model = Zurita 1580, add-one smoothing, normalisation lower case, accents
  stripped, v->u, j->i, y->i, f and s merged;
- 200 controls: the same tokens with the key's plain values shuffled among its signs (Python `random.Random(1577)`);
- yardstick: the same score on 200 windows of Pulgar text cut into runs of the same lengths.
2.3 Verdict rule. "Reads" only if coverage >= 0.80, the score beats all 200 controls, and it is at or above the 5th
percentile of the Pulgar windows. Then, and only then, a strict word count is made: a word counts as read only if
every letter of it comes from the key with no letter supplied and no doubtful token. "Partly fits" if the score
beats all 200 controls but coverage or the yardstick fails. Otherwise "does not read".
2.4 If it does not read or only partly fits, I do not extend the 1574 key. Any value added would be a new key build;
for that I only write a held-out protocol and manifest (passage chosen before any key work, at least 300 cipher
tokens) and do not measure it in this session.

## Step 3. Structure (after step 2)

Token inventory and frequencies, repeated runs (both readers saw lines 11-13 repeat a passage), dotted numbers.

## Step 4. Kervyn de Lettenhove, only after steps 2-3 are recorded

*Relations politiques des Pays-Bas et de l'Angleterre* IX no. 3359 pp. 200-201 (Spanish text with gaps) and X
no. 3640 pp. 69-70 (French translation of the time): used only to compare length, the place of gaps against the dotted
numbers, and whether the printed text could fit a cipher of this length. Cited, not copied beyond a few words.
