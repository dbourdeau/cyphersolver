# Test plan, catalogue 2857 (Juan Manuel, Genoa, 14 April 1497): does George Lasry's key for BnF Espagnol 318 no. 95 read it?

Written Mon 16 Nov 2026, 23:13 EST (time from the `date` command), by the AI agent working item 2857, BEFORE any
decoding of 2857. No sign value has been applied to the 2857 transcription before this file was hashed; the test
script was dry-run only on a dummy file of made-up ids. One run.

## Inputs (sha256)

| file | sha256 |
|---|---|
| `i2857/transcription_reconciled.txt` (224 positions, 2 holes) | f19fa0e263954c0df22c55e0f4ac9677454fdb888f88eb121fc3f3a8681af478 |
| `i2857/transcription_A.txt` (agent; knows the key) | 3d516ae6823043e4e7aa7c3a56593ba4030e031ca5ad30920af3952739098466 |
| `i2857/helper_blind/transcription_B.txt` (blind helper, Opus, medium effort) | f6aa040273cfcd28dc6a07386297374b66592036ad506bbb21f45a203f2a1e92 |
| `i2857/adjudications.tsv` (8 settled disagreements) | 1ff8ed40c09bcd817914dbd5b1031c4a3a9b5fedc3d3f67d2fd00345284d2de6 |
| `i2857/private/signsheet_K_private_map.json` (tile id -> Lasry column/row) | bd647c137befa770e9d396e04b87e0bd59601fa2b5c655df1d9b45757c4f5f3b |
| `i2857/private/signsheet_K_blind.png` (value-free sheet the helper used) | ed229f36bf8cafdf9c88ba3eb492b9fecfe807f6c94955eb4dcb385a6d853a56 |
| `upstream_files/esp318no95/lasry2021/cryptiana/images/esp318_1497_key.png` (Lasry's key image, "key updated October 2026", repository origin/main) | b3a4e5a4b3122a946931e054522d3acc47a6eb248c9470eed11cbad770924372 |
| `upstream_files/esp318no95/lasry2021/ctts/key.txt` (same key in CTTS labels) | 5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06 |
| `output/claver1497_2026-11-16/wordlist_claver_es.tsv` (3,665 forms) | 9b4e5b16a0f16656d2c7a4a3677331deab55fb40c54976babb4c8468002f091b |
| `output/claver1497_verify_2026-11-16/raw/pulgar1780_bub_gb_RB9nAr9N5AkC_djvu.txt` (Pulgar, Crónica, Valencia 1780) | b265e4c7d071a0d83cb903565948a954dd0603cc1ab2d875c150fda6cf22ec29 |
| `scripts/test2857.py` | 463cde34bceee7336ebb0c48776d6d857afaccd5205eca397862f86af2fe34bf |
| `scripts/wl2857.py` | 2e7c269cbc70a8f171a607a565c80e044db6da31958d8002f8c74cae5c64e6fb |
| `scripts/reconcile2857.py` | be6b3550d7e487ac99251fd06da2041dc4a183939efac98e27d620a2a207b88d |
| `sources/raw/claver1497_2026-11-16/pages_0039/p001_0_Im0.jpg` (recto, 1550 x 2233) | 4090aae4bd486db2063a402f002a54d7795b0300cf327d092d6fee3ac677a36c |

## Key, applied unchanged by script

Each sign tile was cut by script (`signsheet2857.py`) from Lasry's key image; an alphabet tile's value is the letter
of the column it came from (21 letters, 44 signs: A2 B1 C2 D3 E2 F1 G1 H1 I2 L3 M3 N2 O3 P2 Q2 R4 S2 T2 U2 Y2 Z2).
Specials: 9-with-dot = y (Lasry "[y?]"), D-like sign = null, "aunque" sign = code. Code groups take Lasry's labels:
bac ciudad, bcd cardenal, bnh rey, bon gente, dae papa, dif "rey de romanos?", and boo, dah, dal, dcl, dnl unidentified
names. No value is changed, added or refitted. Signs not in his table have NO value: N03 (u/v with a bar at upper
left, 2 occurrences), the Latin group [bnm] (1; not one of his groups; it may be his bnh, but it is not changed), and
the holes # (2).

## Measure (fixed now; calibrated only on Lasry's own letter, see below)

1. Decode the reconciled transcription sign by sign; code groups split the text into segments; unvalued signs give "?".
2. Normalise each segment letter by letter with the rules of `output/claver1497_2026-11-16/scripts/spnorm.py`
   (z=c, y=i, v=u, j=i, doubled letters other than l single).
3. Word list: every form of `wordlist_claver_es.tsv` plus every form of Pulgar's Crónica (1780 OCR) of at least 4
   letters seen at least 5 times, normalised the same way (`wl2857.build_claver_pulgar_long(..., 4, 5)`). The
   Pulgar-based list of the 16 Nov verification run was never saved as a file, so it is rebuilt by this rule.
4. Segment each segment by a Viterbi search (word cost -ln(count/N); an unknown letter costs 10).
5. **Score = share of letters (holes included in the denominator) that lie inside dictionary words of at least 3
   letters, or inside shorter dictionary words standing directly between two such words** (`sandwich_measure`).
   Because 2857 is written without reliable word spaces, "share of cipher words that are Spanish words" is measured
   over letters of the segmented text; this is the nearest fixed equivalent.

## Marks (one run)

- **Pass (read under Lasry's key): score at least 70%** and the control valid.
- **Same family, different key: 30% to under 70%.** Then report the per-sign agreement (share of each sign's
  occurrences inside counted words) and STOP: no refitting in this session.
- **Miss: under 30%.**
- **Control:** 1,000 tables with Lasry's letter values permuted among his 44 alphabet signs (code groups fixed),
  seed 2857; the test is valid only if the control's 95th percentile is under 20%. If it is not, the result is
  "test not valid", whatever the score.

## Calibration done before this plan (on Lasry's own letter only; logs in `i2857/calibration_no95*.log`)

Lasry's key on his own CTTS transcription of no. 95 (first 225 signs, about the length of 2857), 1,000 permutations:
plain coverage with the full Pulgar list gave true 74.5% but control 95th percentile 33% (rejected); Claver list only,
sandwich measure: true 66.4%, control 17.5%; **chosen list (Claver + Pulgar 4+ letters seen 5+ times), sandwich
measure: true 72.7%, control mean 9.6%, 95th percentile 19.3%** (450 signs: 80.9% / 17.6%; whole letter 86.0% /
17.0%). So a correct key on a text of this length scores only a little above the 70% mark: a genuine reading of
2857 could land just under it. This is stated now so that a result of 60-70% is not over- or under-read later.

## After a pass (only then)

Diplomatic text with holes, normalised text, English translation marked as an AI agent's, read share by the
repository's rule (cipher words only; a word is read only if every sign has a value from the key and no letter is
supplied or changed by sense; holes by words), and what the letter says.
