# Source: the Danish chancery's key sheet for this cipher family

Tags: [sourced] read in the named record or file; [measured] computed or seen on the image here; [derived] inference; [unverified] not checked.

## The sheet

- Archive: Copenhagen, Rigsarkivet, TKUA Almindelig del 3 nr. 112 "Chiffer", Arkivalieronline unit 260610, image 150 of 309 (api image id 48691625). [sourced: unit listing and fetch log]
- Archive's own title and dates: the archive lists the series as "Chiffer", 1670-1709 (Tyske Kancelli, Udenrigske Afdeling; Daisy record heid 2132747, the record for unit 260610, seen 25 Nov 2026 21:52 UTC). [sourced: Daisy series list] The sheet itself looks earlier, about 1630-32, by its hand and by its names (Tilli, Papenheimb, Friedtlandt, Infantin); so it is older than the dates the archive gives the series. [derived]
- Image URL as fetched: `https://api.rigsarkivet.dk/ao/v1/images/48691625` (plain GET, no sign-in, HTTP 200, 1,107,691 bytes). [measured]
- Fetch date: 24 Nov 2026, 09:58:03 UTC. md5 5798d84da1170fc5cdb571e1cda4944d, sha256 1453a074be078cdeb30e4502f2522b88e8a9d45d257dba6ad9a1b118eb442097. [measured]
- Sister sheet: same unit, image 149 (api image id 48691624), `https://api.rigsarkivet.dk/ao/v1/images/48691624`, fetched 24 Nov 2026 09:58:01 UTC, 1,208,116 bytes, md5 b933d24a0eb75be778544006c10c874e, sha256 7b5605b994498018b4350aa5e7c46f9b83d79e1a1ff41402ff005c843fa24db7. [measured] Read at overview scale only: its table and rule lines were read, its name list was not transcribed. [unverified in detail]
- Link to this target: linked by Malcolm McBratney with Claude, 25 Nov 2026. The sheet was first seen in a sweep of the unit on 24 Nov 2026 and logged then as a key of the zobel1629 family without naming Pentz. [sourced: sweep log]
- The sheet names no user and no date. It was matched to Pentz by its letter values: all 38 values of key v1 (`../key.tsv`) stand on it. [measured] Its names (Tilli, Papenheimb, Friedtlandt, Infantin, Rubens, "Gesandten im Haag") point to about 1630-32 and a mission at The Hague. [derived] Whose mission is not known. [unverified]

## Files here

| file | what |
|---|---|
| `sheet150_transcription.tsv` | The sheet transcribed in full: 72 letter values, 9 index numbers, 3 rule lines, 174 names (258 rows; 72 + 9 + 3 + 174 = 258). Frozen 25 Nov 2026 08:00:22 UTC, md5 692d5950aeb7620500fd5a9b3924023b, sha256 9168da1820cd697537dddb662fa9ff365954d56e65082acb7965848fbb42d6c4; the file here is byte-identical to the frozen one. [measured] |
| `COMPARISON.tsv` | The sheet against key v1 (McBratney, `../key.tsv`) and key v3 (Brice Dudout, `../dudout/key.tsv`), value by value, with the index numbers, the nulls rule and the code numbers recorded in the nine letters. |
| `COMPARISON.md` | The same in short, with the counts. |
| `crops.tsv` | Seven reference crops, recorded as boxes, not filed as images: the nulls rule line; table 3 e = 33, g = 35 and r = 39 (each the column's letter heading stacked over its table-3 cell); index 63, 12 and 9. Per crop: the image id, the image URL as fetched, the fetch time (UTC), the source image sha256 (a local integrity check only), the box in source pixels, scale and resampler, the sha256 of the PNG as first filed in PR #974 and of its pixels. [measured] |
| `make_crops.py` | Re-cuts the seven crops from the archive's image (`python make_crops.py --fetch OUT_DIR`, or a downloaded copy) and checks each against `crops.tsv`. Re-fetched 25 Nov 2026 21:53 UTC, the archive's image was byte-identical to the 24 Nov fetch and all seven crops came out pixel-identical to those first filed. [measured] |

## About the transcription

- One reader (Claude), **not blind**: key v1 and both first-pass decodes were known. No second transcription.
- The file's header calls it "KEY v2 ... external key from the chancery sheet". That is the working name from the session that made it, and it is **not** key v2 of this target (`../key_history/KEY_pentz_v2_b110.txt`). The header also names local working paths. The header is left as frozen so that the hash still matches.
- The `crop` column names one reference crop per row (258 crops). Seven are recorded in `crops.tsv` and can be re-cut with `make_crops.py`; the rest can be re-cut from the image URL above. The crop images themselves are not filed in this repository: the image is Rigsarkivet's, and its reuse terms were not checked. [unverified]
- Doubts, as recorded in the file: table 3 r = 39 is written heavily over an earlier figure; the 4 of "64" in the rule line is written over; 7 "die Ens" (the Ems?); 171 Bever; 199 Brugk; 185 has a stroke through the first figure; 216 has a line through the number.
- The sheet has no syllable entries.
- The 24 Nov fetch time is from the fetch log; the freeze stamp is a local `date -u` beside the hashes, not an external timestamp.

## Not done

- Tomokiyo (Cryptiana) and Lasry were not searched for this sheet. [unverified]
- GitHub issues and pull requests opened after 24 Nov 2026 were not checked for an earlier link between this sheet and Pentz. [unverified]
- No repository script or checker was run for this addition.
