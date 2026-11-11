# lilienthal1665: Resident Johan von Lilienthal in Moscow, 1665-1667 (Riksarkivet, Diplomatica Muscovitica 1/36/82), key of the homophonic letter code

Status: solved at the time (contemporary German decipherment written over every code run); key rebuilt from the glosses and validated on a held-out page (Brice Dudout, 10 Nov 2026; 0.887 of characters vs 0.047 for the best shuffled key). The clear text of the letters is not transcribed here.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2316, found in Daniel Bourdeau's Riksarkivet
western sweep and vetted in leads review n09 (6 Nov 2026), which marked it "read": the decipherment of the time is between the
lines, "only the key is of further use". This target supplies that key. Our role is the key and its verification, not a solution.
Sibling target: `ebers1664` (lead 2315, PR #383), the other Swedish agent in Moscow, a different code.

## Documents

Stockholm, Riksarkivet, Diplomatica Muscovitica, SE/RA/2113/2113.1/1/36/82, *Residenten Johan von Lilienthal, brev till Kungl.
Maj:t, 1665-1667* (137 images, IIIF series R0000814, public viewer sok.riksarkivet.se, no login). Letters of the Swedish resident
in Moscow to Charles XI (the Regency), in German. No images are included here: the IIIF manifest carries no rights statement.
Credit for the images: "Riksarkivet, SE/RA/2113/2113.1/1/36/82, bildid R0000814_000nn".

| image | role here |
|---|---|
| 42, left and right | training: the key was learned from its glosses |
| 47, left | training |
| 45, left page, lines 1-10 | held out: first 160 cipher groups, transcribed after the key was frozen, measured once |

Code runs fill nearly every image from 28 to 49; they were not transcribed beyond the three images above. Images 11, 65, 74 and 83,
listed by the sweep, are mostly clear text on the thumbnails we saw.

## System and key (`key.tsv`, CC BY 4.0)

Not a nomenclator (our own first notes said so; that was wrong, from low-resolution views). It is a German letter substitution
with homophones, with numbers also for ch, sch, st, ss, ll, ff and tz; u, v and w share their numbers. Groups of 2-3 digits,
separated by dots, mixed with clear German. There are six code series: 23-59, 63-100, 103-150, 153-190, 293-349 and 353-390;
numbers ending in 1 or 2 do not occur. Each series runs through the alphabet (23 a, 24 b, 25 c, 26 ch, ... 59 y); series 293-349
repeats the order of 23-59 (+270, then +290) and series 353-390 that of 63-100 (+290). 107-120 and 303-320 were never seen: they
may hold words or names, or simply be unused.

The frozen key has 158 codes, learned without a conflict from 1116 aligned groups. After the measurement, from the order of the
table and the sense of image 45: 89 = st (feste), 27 = ff (auff; also "difficultas" on 38 right), 64 = c (instruction),
54 = tz (Danielewitz), 348 = z (zusammen); from structure alone 379 st, 344 tz, 75/365 k, 378 sch and 68/358 ff (uncertain).
These rows are derived, marked "post" in `key.tsv`, and were not tested.

## Validation (`validation.txt`, `frozen/`)

The first protocol (`frozen/PREREG.md`, in French, SHA-256 0d67cc26...) treated the code as a nomenclator and held out image 42.
Before any measurement it was amended (`frozen/PREREG-L2.md`, a3199fb6...): image 42, already seen in part, moved to training,
and image 45, not yet looked at, became the held-out page. The key was learned on images 42 and 47 only (`frozen/PAIRES-LILIENTHAL.tsv`)
and frozen (`frozen/KEY-LILIENTHAL.tsv`, 81f56ea7...). On image 45 the first 160 cipher groups were transcribed and frozen first
(`frozen/H_L-CHIFFRE.txt`, e769ed16...), then the gloss above them was read and frozen (`frozen/G_L-GLOSE.txt`, 27f32f15...).
One measurement (`frozen/scripts/measure.py`, output `frozen/MESURE-L.txt`): 0.887 of characters against 0.047 for the best of
200 shuffled keys (mean 0.024), margin 0.840. Thresholds fixed in advance: >= 0.85 and margin >= 0.30. Verdict: validated.
The 5 groups outside the frozen key (89, 27, 64, 54, 348) counted as wrong in the measurement.

Declared bias: the gloss is on the same image and was visible while the numbers were transcribed.

## Texts

`transcription.txt` gives lines 1-10 of image 45 left (185 groups; the first 160 measured) and the gloss; `decryption.txt` our
decode with `key.tsv` beside the gloss; `translation.md` an English rendering. The passage is a run of cipher with two short
clear insertions, not the whole letter. Content: someone holds firmly to his instruction and propositions, and some of the great
boyars (Dolgoruka, Ilia Danielewitz, Almasi) talked it over together after yesterday's conference.

Daniel's count on the measured portion: 160 groups; 155 in the frozen key; 5 outside it (now read by sense and structure); 0 cut;
0 restored.

The gloss is not always word for word. On image 45 the cipher has "haten auch etliche von den grossen boiaren" where the gloss
writes "und welche von den grossen boiaren", and "feste auff" where the gloss has "hatte auf". A full reading from the cipher
rather than from the gloss would show these differences across the volume; we did not do it.

## Gloss inventory

At 3000 px, a band through the middle of each page 28-49 (38, 42, 45 and 47 seen more fully, 38 right in full): a gloss over every
run seen, including the Latin words of 38 ("difficultas", "foedus", "baptismi"), which are Latin enciphered letter by letter and
glossed. 49 right "348.186.379.70.375.295.129.106.327" = "zu stercken", glossed on the line above. No bare passage found; this
agrees with leads review n09 (31, 42, 45 at 2600 px).

## Prior work

- The glosses are the decipherment of the time (credited `contemporary`, prior solution).
- Leads review n09: nothing on DECODE, at Cryptiana (Tomokiyo) or in Lasry's lists; no edition found.
- No target, branch or PR for Lilienthal, R0000814 or Diplomatica Muscovitica 1/36/82 in this repository (GitHub API, 10 Nov 2026).

## Limits

- One reader (an agent), on 3000 px images; no human palaeographic check.
- Two training images, one held-out page; the "post" rows untested; 107-120 and 303-320 unknown.
- Not checked: the tops and bottoms of the pages 28-49 other than 38, 42, 45 and 47, so a short bare run there is not excluded.

## Integration check (11 Nov 2026)

On integration (PR #384): `frozen/scripts/measure.py` re-run on the frozen files gives the same output (0.887, best control
0.047, mean 0.024, margin 0.840); the SHA-256 files in `frozen/` check out; decoding `transcription.txt` with `key.tsv`
reproduces `decryption.txt` line for line. The page crop of image 45 was fetched from the Riksarkivet IIIF image service,
whose `info.json` carries the Public Domain Mark (the manifest itself has no rights field).

## Remaining gaps
- the "post" rows of key.tsv (89 st, 27 ff, 64 c, 54 tz, 348 z; from structure alone 379 st, 344 tz, 75/365 k, 378 sch, 68/358 ff) - blocker: too-short; each rests on one or two words of image 45 or on the order of the table, and the one held-out page is spent, so no blind test is left for them in the parts read
- codes 107-120 and 303-320 - blocker: no-key-material; not one occurrence in the runs read, so nothing to learn them from
- a held-out test with the gloss out of view - blocker: no-key-material; every code run seen carries its gloss on the same leaf (gloss inventory above, leads review n09), so no unglossed page is known to test on (declared bias)

Not gaps of the reading: the other code runs of images 28-49 and the clear German between the runs were not transcribed,
but the contemporary gloss over every run is their reading. Not checked, and workable (no outside blocker): the tops and
bottoms of pages 28-49 other than 38, 42, 45 and 47 at full resolution, so a short bare run there is not excluded. The dates
of the letters on images 42, 45 and 47 are in their clear text, which was not transcribed.

## Escalation
- [x] siblings: bands through every page 28-49 at 3000 px for the gloss inventory; lead 2315 (Ebers) opened: a different code, own target ebers1664
- [x] clear-pages: images 11, 65, 74 and 83 are mostly clear text on the thumbnails; the Latin words of 38 are enciphered and glossed
- [x] known-keys: no key of this series on DECODE, at Cryptiana or in Lasry's lists (leads review n09); Ebers's key is a different series
- [x] print: no edition of Lilienthal's despatches found (leads review n09)
- [x] key-rebuild: 158 codes from 1116 aligned groups of 42 and 47, then the post rows from the order of the six series and the sense of 45
- [x] retry: the held-out lines decoded again with the post rows (decryption.txt); all 185 groups of lines 1-10 give letters
