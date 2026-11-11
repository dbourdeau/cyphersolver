# Zeschau → Seebach, Dresden → St Petersburg, 1841–1843

Status: in progress (attempted, open: R5005 is segmented into groups of 2, 3 and 4 digits, Brice Dudout, 11 Nov 2026,
and a few values are proposed from the erased decipherment, but there is no key and the letters are not read; next
steps in `dudout/README.md`).

## The target

Heinrich Anton von Zeschau (Saxon foreign minister) to Albin Leo von Seebach, Saxon minister resident in
St Petersburg. HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12. DECODE R5005–R5008 ("Partially decrypted";
note: "interlinear decrypted, but unfortunately rubbed out"). Unpublished catalogue entry (rule-scored).

| DECODE | Date | Language | Cipher |
|---|---|---|---|
| R5005 | 18 Jan 1841 | French | 70 lines, 3,764 digits (the 3,969 written here until 11 Nov 2026 was a miscount): the whole despatch body (6 images, 5 written spreads) |
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

**Superseded in part on 11 Nov 2026** (see "Segmentation" and "Integration check" below): the groups are not pairs
but 2, 3 or 4 digits long, so the pair counts, the per-line pair phases of `offsets.json` and the seven pair values
below are kept as the record of the September attempt, not as the present description. On whole groups the glosses
fall as 711 la, 708 pre, 234 mi, 294 er (or re / ere), 746 que (proposals, not tested).

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

## Integration check (11 Nov 2026)

On integration of PR #401 (Brice Dudout), after reading `dudout/segment.py` (it only reads `ct_R5005.txt` and prints):

- `python3 dudout/segment.py ct_R5005.txt` reproduces `dudout/R5005_groups.txt` byte for byte: 1,309 groups, 190 types
  (337 of 2 digits, 795 of 3, 176 of 4, one stray final digit), 15 outside the forms (1.1%). `ct_R5005.txt` has the
  SHA-256 given in `dudout/validation.md` and was not changed by the PR.
- Held-out measure recomputed here with an independent script (the rule's regex and form test, a3 and a7 as two
  streams, offset 0): 291 of 296 groups in the forms = 0.983 (a3 60/60, a7 231/236), 859 digits; lengths 68 / 186 / 41
  and one single digit; 3-digit groups ending in 1/3/4/6/8 0.984 (183/186); [3468] pairs 32/33; no immediate repetition;
  0.956 of the a3+a7 tokens are of a type seen in the other blocks. All as stated.
- Controls re-drawn here (1,000 each, best of offsets 0-3, another seed): digits shuffled within lines mean 0.641,
  max 0.712; pairs shuffled mean 0.619, max 0.687. The PR gives maxima of 0.703 and 0.700; the maximum of 1,000 draws
  moves with the seed, so "at most 70%" is better said "about 0.70 at most (0.71 in our re-draw)". The synthetic
  true-pair control was not re-run (its generator is not in the PR). The real figure is far above all of them.
- In-sample blocks (the ones the rule was built on): 0.977 to 1.000 per block, as stated. The segmentation also
  re-synchronises: started one, two or three digits late, a block scores within about 0.01 of offset 0 (a4 excepted).
- Not checkable here: that the rule was written without sight of a3 and a7, and the pre-registration hashes (the
  hashed files are the contributor's local files, "available on request"). `validation.md` itself says a3 and a7 had
  been seen as raw digits on 5 Nov. We take the protocol on the contributor's word; the measure itself reproduces.
- Corrections made on integration: R5005 is **3,764 digits** in 70 lines (sum of the lines of `ct_R5005.txt`;
  2,905 + 859 in the PR agrees), not 3,969 as these notes, the page and the ledgers said. Repeat counts on the raw
  digit string: `7778948206` 4 times (not 5), `2437784` 3 times, `06777818` 5 times of which `06777818711001` once
  (not 3), `00866` never as written (0086 is a frequent 4-digit group, 17 times). "Immediate repetition never occurs"
  holds within each stream.
- Consequences recorded: the two-digit description is withdrawn in `profile.json`, catalogue entry 53, the README row,
  the page `docs/zeschau1841.html` and the DECODE queue entry (cipher type: a table of 2-, 3- and 4-digit groups for
  letters and syllables). The September solvers all worked on pairs or on the 1/2/3 prefix code, so none of them
  tested this segmentation: a solver on the 1,309 groups is the next untried step, with the 15 off-form groups to
  check on the images first.
