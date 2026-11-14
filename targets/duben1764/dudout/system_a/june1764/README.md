# 15 June 1764 letter (Chiffer n:o 1, system A): pre-registered test of key_c01 and reading

| file | what |
|---|---|
| `PREREG.md`, `SHA256SUMS-PREREG` | plan, key hash, single measure, thresholds; hashed before transcription (04:15 CET) |
| `SHA256SUMS-AMEND1` | amendment 1 + transcription, clear, script hashes; before the decode (04:33 CET) |
| `transcr/c1764-06-15.txt` | cipher 108R.01-15 + 109L.01-17 (frozen) |
| `transcr/passes/` | pass 1, blind pass 2 (sub-agent), list of the 55 differing places, two clear passes |
| `clears/p1764-06-15_clear_contemporary.txt` | contemporary decipherment 109R + 110L (frozen) |
| `scripts/measure_june.py` | the one measure (check2.py metric, seed 1764) |
| `outputs/measure_result.txt` | its output and the raw decode |
| `reading_1764-06-15_en.md` | strict count (341/342), where the cipher is (110R), English translation |

Re-run from `targets/duben1764/dudout/system_a/`:
```
python3 -I june1764/scripts/measure_june.py key_c01.json june1764/transcr/c1764-06-15.txt june1764/clears/p1764-06-15_clear_contemporary.txt
-> groups 511, key coverage 0.761, clear letters 1465, M 0.3829, controls max 0.0573, mean 0.0347: PASS (M >= 0.15 and >= max + 0.10)
```
Order of events is by the contributor's record (file hashes and times in the two SHA256SUMS files; no outside timestamp).
Transcriptions by AI agents (one reader + one blind reader), not checked by a palaeographer. Images not included
(Riksarkivet, Public Domain Mark per the IIIF manifest; `https://lbiiif.riksarkivet.se/arkis!A0073297_00108/full/max/0/default.jpg`).

Hash check: `SHA256SUMS-PREREG` holds the hash of PREREG.md before amendment 1 was appended; it is the file's lines above
"## Amendment 1" minus the blank line before it: `n=$(grep -n "^## Amendment 1" PREREG.md | cut -d: -f1); head -n $((n-2)) PREREG.md | shasum -a 256`
gives c941c974... `shasum -a 256 -c SHA256SUMS-AMEND1` checks the rest.
