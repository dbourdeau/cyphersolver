# Zeschau → Seebach, Dresden → St Petersburg, 1841–1843

Status: attempted, open. The system is identified and a few code values are recovered from the erased decipherment,
but the letters are not read.

## The target

Heinrich Anton von Zeschau (Saxon foreign minister) to Albin Leo von Seebach, Saxon minister resident in
St Petersburg. HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12. DECODE R5005–R5008 ("Partially decrypted";
note: "interlinear decrypted, but unfortunately rubbed out"). Unpublished catalogue entry (rule-scored).

| DECODE | Date | Language | Cipher |
|---|---|---|---|
| R5005 | 18 Jan 1841 | French | about 70 lines, 3,969 digits: the whole despatch body (6 images, 5 written spreads) |
| R5006 | 6 Apr 1842, No. 13 | French | clear opening ("J'accuse la réception de vos rapports inclus le nº 17 du 22 Mars"), then 8 + 3 cipher lines; clear section about the Kühnel succession |
| R5007 | 13 June 1842, No. 18 | German | clear, cipher block of about 10 lines, clear close (Gütschow named) |
| R5008 | 26 Oct 1843, No. 17 | German | clear, cipher of 5 lines inside a sentence ("Indem ich nach dem Eingang Ihrer Berichte NN. 21 und 22 … bekenne, [cipher] habe ich die Ehre …") |

DECODE's R5007 title says 13.06.1846; the letter is dated 13 Juni 1842.

## Verify first (done)

- DECODE key records: every Dresden key (record_type 2, HStAD) was listed from `research/catalogue_harvest/decode/list.json`.
  The latest is R2334 (1799–1806). There is no key for the 1840s, and none filed with 10731.
- No printed edition of the Zeschau–Seebach correspondence was found. Nothing in Tomokiyo.

## Transcription

`ct_R5005.txt`: R5005 in full, one row per written line, tagged `a<block>_<line>` by page region (not in reading
order). Hand-read from 2400-px line strips (`seglines.py`, `pitch.py`). R5006–R5008 are not transcribed yet.

## What the cipher is

- Unseparated digits, clean hand. Two-digit groups: 96 of the 100 pairs occur.
- About a third of the lines have an odd length, so a group can be split across lines. `offsets.json` records each
  line's pair phase, chosen by EM on pair frequency.
- The table is a **syllabary**, not a letter substitution. The erased pencil decipherment is still faintly
  visible over R5005 p. 5 (right), line a5_03: `11 70 82 34 29 40` has "la pre m i er e" over it (*la première*).
- Values from glosses: **11 = la, 70 = pre, 82 = m, 34 = i, 29 = er, 40 = e, 46 = que** (46 is at the end of a8_05).
  Other traces ("pour", "a", "ex", "ce", "ne") could not be tied to a group with confidence.
- Long repeats that should be names or formulae: `7778948206` (5×), `06777818711001` (3×), `2437784` (3×), `00866`.

## What failed

| Step | Result |
|---|---|
| Null digits (every set of 1–3 digits) + pairs | no gain in pair IC (best 1.42 vs 1.31 raw) |
| Prefix code (first digit sets group length 1/2/3) | no clear winner |
| Homophonic letters on pairs, phase 0 / 1, and two prefix codes (`hsolve.py`, French 4-gram model + letter-frequency penalty; the same code solves a synthetic 1,800-letter French homophonic control at −2.18/char) | −3.05 to −3.17/char, no French |
| Syllabary annealer, free syllables (`syll.py`) | degenerates to "ment/vous/ait" |
| Syllabary with one-cell-per-syllable and length-neutral scoring, gloss seeds fixed (`syll2.py`, `syll3.py`) | still no French |

Gloss harvest: enhanced crops (`gl.py`, background-subtracted grey) on R5005 p. 5 give about one faint word per line.
Show-through from the reverse side mixes in, so glosses alone will not rebuild the table.

## What would move it

1. The Seebach-side key or the St Petersburg legation's decipherments (HStAD 10731, other Nrs.; Seebach papers).
2. Multispectral or UV imaging of R5005: the pencil decipherment was complete once.
3. Transcribe R5006–R5008. The German letters use the same code; the cipher in R5008 sits inside a known sentence
   frame, and R5006's cipher follows a clear acknowledgement of Seebach's reports.
4. A syllabary annealer with a proper French/German syllable model, seeded with the seven values above.


## Segmentation (Brice Dudout, 11 Nov 2026)

R5005 is not in pairs: groups are 2, 3 or 4 digits long, the length set by the first digit(s), and run on across lines. The rule was proposed by Fable 5.2 on R5005 without blocks a3 and a7, then measured once on a3+a7: 98.3% of groups in form, against at most 70% for controls. Structure only, no reading. Details in `dudout/`.
