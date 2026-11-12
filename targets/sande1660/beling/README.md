# Sande 1660: cipher A transcribed in full and tested against the frozen key; a start on cipher B from its glosses

Contributed by Andrew Beling, with AI agents, 11-12 November 2026.
This folder adds to `targets/sande1660/`. It changes nothing in WAINUT's files (`key.txt`, `transcription.txt`,
`decrypt.py`, `reading.md`, `translation.md`). The NOTES.md and profile.json edits that go with it are in the same pull
request; `docs/` is not touched.

[V] = checked on the image or in output. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `PREREG.md` | round 1: the test of key.txt on m0271, written before any transcription or script |
| `PREREG_round2.md` | round 2: the rest of cipher A as new held-out material, written before any of it was transcribed |
| `key/key.txt`, `key/transcription_build.txt` | `../key.txt` and `../transcription.txt` copied unchanged (sha256 `f4974639…`, `3e9999ca…`) |
| `lexicon/pt.json.gz` | `lang/lexicons/pt.json.gz` copied unchanged (sha256 `a1127215…`) |
| `transcription/m0271.txt` | m0271, all 37 lines, first reading (round 1; reader knew the key table) |
| `transcription/m0271_r2.txt` | m0271, second reading, blind to the first reading, the key and any decryption |
| `transcription/m0272.txt`, `m0265_rest.txt`, `m0266_rest.txt`, `m0267.txt`, `m0269_rest.txt`, `m0273_top.txt` | round 2: every cipher A line not transcribed before (168 lines, 5,094 tokens), one blind reader per page |
| `scripts/test_m0271.py`, `scripts/test_round2.py` | the two pre-registered tests (standard library) |
| `scripts/posthoc_round2.py` | a post-hoc re-score of round 2 (section 3; not pre-registered) |
| `scripts/collate_m0271.py`, `scripts/decode_all.py`, `scripts/cipherB_glosses.py` | collation, reading decrypt, cipher B table |
| `results/test_m0271_*`, `results/test_round2_*`, `results/posthoc_round2*` | test results and line-by-line decrypts with their lexicon parse |
| `results/collation_m0271.txt`, `collation_m0271_settled.md` | the two m0271 readings collated, each disagreement looked at on the image |
| `results/unkeyed_numbers.md` | numbers below 60 that key.txt lacks: second look |
| `results/code_groups_round2.md` | every code group with its places, and which values hold in more than one |
| `results/m0271_reading.md`, `results/round2_reading.md`, `results/decode_all.txt` | the reading (not part of any test) |
| `cipherB/m0063_runs.txt`, `cipherB/m0062_runs.txt`, `results/cipherB_m0063.txt` | cipher B runs and glosses, the table built from them, and its check |
| `results/frozen_inputs.sha256`, `frozen_inputs_round2.sha256`, `prereg_round2_written.sha256` | hashes taken before each scoring script existed |
| `images.txt`, `CHECKS.txt` | the scans used (ids, hashes); order of work, hash checks and re-runs |

Scripts run from this folder with `python3 -I scripts/<name>.py`.

## 2. Round 1: m0271 held out [V]

Unchanged from the first version: S_held 0.782 against S_build 0.739 (threshold 0.628); 200 shuffled keys mean 0.158,
best 0.366; margin 0.416; pass. Details in `PREREG.md` and `results/test_m0271_result.json`.

**Second reading (new).** An AI agent in a separate context, given only the scan and the glyph notes of NOTES.md,
re-read m0271 without the first transcription, the key or any decryption. Both readings have 1,225 tokens; 1,202 are
identical and aligned (0.981). The 21 disagreements were looked at on the image (`collation_m0271_settled.md`):
6 settled on the image, 11 by the word the decrypt must make, 4 still open. The first reading had one clear error
(l. 10, "61" for 6.1, "se de|pende") and one probable one (l. 3, 7 for 17 or 1.7). Under the round-1 rule the blind
reading scores 0.765. The second reader is the same model family as the first, so this is two independent readings by
machine, not by a person.

## 3. Round 2: the rest of cipher A held out [V]

`PREREG_round2.md` (hashed at 2026-11-11T23:46:45Z, before any transcription) fixed the material, the transcribers'
blindness and the score (the round-1 rule, unchanged). Five agents, each in its own context and given only its scans
(one did both m0267 and m0273, where PREREG_round2 said one agent per file),
transcribed every line not transcribed before; none saw key.txt, transcription.txt, NOTES.md or any decryption. The
files were copied unchanged, hashed (2026-11-12T00:16:35Z) and scored once.

**Pre-registered result: S_new 0.709 on 96 lines (2,706 letters), against S_build 0.739 (threshold 0.628);
200 shuffled keys mean 0.157, best 0.392; margin 0.317. Pass**, but only just on the margin.

**A flaw in the pre-registration.** The exclusion rule (leave out a new line that shares 6 tokens in a row with a
build line) was meant to catch lines physically the same as build lines. It caught 72 of 168, almost all because the
letters repeat phrases (que, porque, Sua [72], Vossa Excelência). Only one is a physical overlap (m0269.12). The rule
removed the lines with the commonest words, which lowers the score. A post-hoc re-score (`posthoc_round2.py`, not
pre-registered, same key, rule and null) on all 167 lines but m0269.12 gives **S 0.728 (4,726 letters), shuffled
best 0.387, margin 0.341**; the 71 lines the rule left out score 0.753 alone. The pre-registered figure stands as the
test; the post-hoc one is reported for what it is.

Per page (pre-registered subset): m0272 0.688, m0265 0.693, m0266 0.670, m0267 0.802, m0269 0.698, m0273 0.784.
The blind transcriptions carry 180 doubtful (`*`) and 76 unread signs; most `?` are at the binding edge of m0266 and
m0272. They count against the key, so the score is conservative.

**Coverage.** Cipher A has 250 cipher lines (the transcribers' counts: m0265 43, m0266 42, m0267 22, m0268 1, m0269
39, m0271 37, m0272 37, m0273 29), not ~290. All are now transcribed at least once: 7,630 tokens, of which 7,374
(0.966) take a letter from key.txt; 134 are code groups, 40 are numbers below 60 the key lacks, 82 not read.
The round-2 pages have one reader each.

## 4. Numbers the key does not cover [V shape, I values] (`unkeyed_numbers.md`)

- **31 = o**: a homophone. Both m0271 readers saw 31 in two places (com-o, no m-o-do); the blind readers of m0265,
  m0266 and m0272 found six more, each needing o (acomodar, meios, todo o povo, os ofícios, deseja o bem).
- **38 = m**: probably a homophone (6 places, all need m); the new places have one reader each.
- 23 (2.3, "pessoa"), 26 (20), and on the new pages 28 (18/20), 17 (13), 34 (30): misreadings or dropped dots.
- 25 (twice in "deferirão": a variant 27 or a third e) and 42 (h? twice, once doubtful): open.
- The "22" the blind m0271 reader saw five times is a 27 with a closed foot; every place needs e.

## 5. Code groups (`code_groups_round2.md`)

With more than one fitting place: **132 embaixador** (11), **72 Majestade** after "Sua" (13; group 72 or "7.2" not
settled), **79** the Dutch / the States (9), **102 Brasil** (3), **115 paz** (3), **137 ministros** (3).
Fair (2-3 places, a rival value fits too): 117 Inglaterra, 122 armada, 131 naus; 73 is a country (France or England).
61, 62, 69 (probably 63, 66) are separators or nulls; 65 is often 6.5 ("di"). Open: 128, 64, 134, one-place groups.

## 6. What the letters say [I] (`round2_reading.md`)

Three letters from an agent near The Hague to "Vossa Excelência". The Dutch, inflamed by the arrival of the [128],
keep up the war; France (de Thou, Cominges) offers mediation; the writer urges that an ambassador with powers be sent,
and that "o senhor Protector" be moved "dessa banda", "essa república" being "a manilha deste jogo". His letters are
opened, he is held suspect and fears expulsion, and the Dutch, he says, "têm cifras que andam decifrando". He asks
Vossa Excelência to write to him in cipher and to forward his letters to the King. The addressee is in England
(Bordeaux, the Protector, "essa república"): Francisco de Melo, Portugal's envoy in London, fits. A Dutch armada on the
Portuguese coast that should not "return in the spring" puts the letters in autumn-winter 1657 (m0268 "30 Nov 165[7]").
Names in clear or cipher: Francisco Mendes, Jacob Aba[?], António Correia Br[avo?], Duarte da Silva.

**The m0268 line [V].** The line "Vossa [62] Excelência não firme [61] suas cartas" with the date "…30 Nov 165?" is
written down the left margin of m0269; the m0268 scan shows it only because the edge of the m0269 leaf is in that
photograph. It is a marginal note to the m0269 letter.

## 7. Cipher B from the m0063 glosses [V runs, I table] (`results/cipherB_m0063.txt`)

Every cipher run on m0063 (10 runs) was read with its gloss. Aligned one group to one letter, the glosses give a
consistent table, **a homophonic letter substitution** (not syllabic as NOTES supposed): 26 groups for 18 letters
(a 12 204; e 80 325 330; i 30 120; o 14 400 405; u 25 28 570; b 20, c 40, d 70, f 15, g 18, h 24, l 35, m 37, n 45,
p 10, q 90, r 95, s 13), with 9xx groups closing each run. No group gets two letters.
- Leave-one-out on the 7 aligned runs: 47 of 57 groups are known from the other runs, and all 47 are right.
- The unglossed run R1 reads "minis?ros" (ministros, giving 60 = t); "ninguem" is written "ninguens" (or a trailing 13).
- **Check on another page:** six glossed runs on m0062, read after the table was built: 48 of 53 groups are in the
  table and all 48 agree with the glosses (perdiçam, de penetrar, Vanicheli, protector, se vendem, mercancia).
So the m0063 glosses give a working key for cipher B; it reads about 0.9 of the glossed runs on a second page.
Limits: one reader for the runs; only m0063 and six runs of m0062 are transcribed; the other cipher B pages
(m0055-m0062, m0065 and the others NOTES lists) are not; unknown groups remain (3, 33, 60, 65, 200, 9xx).

## 8. Open

- A second reading of the six round-2 pages (one blind reader each), starting with the 180 `*` signs.
- The 4 open m0271 disagreements; 25 and 42; a second look at 38 on the image.
- Code groups 128, 64, 134, 73 (France or England) and the one-place groups; 72 as a group or "7.2".
- The writer (Teles de Faro is one candidate the NOTES name; the text points to an unaccredited agent) and the
  addressee (Francisco de Melo in London fits). Unchecked leads found on the web: J.A.K. Haas on the Hague embassy of
  Fernando Telles de Faro, 1658-59 (BMGN), and a translation of a Teles de Faro memorial to the States General (Bodleian,
  MS. Rawl. A. 61/2). No printed text or clear copy of any of these letters was found.
- Cipher B: transcribe the other pages and decode them with the m0063 table.
