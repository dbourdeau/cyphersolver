# ebers1664: Commissary Adolf Ebers (Eberschildt) in Moscow, 1662-1666 (Riksarkivet, Diplomatica Muscovitica 3/b/602), key of the two-digit letter code

Status: solved at the time (contemporary German decipherment written over every code run); key rebuilt from the glosses and validated on a held-out page (Brice Dudout, 10 Nov 2026; 0.909 of characters vs 0.047 for the best shuffled key). The clear text of the letters is not transcribed here.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2315, found in Daniel Bourdeau's Riksarkivet
western sweep and vetted in leads review n09 (6 Nov 2026), which marked it "read": the decipherment of the time is on the leaves,
"only the key is of further use". This target supplies that key. Our role is the key and its verification, not a solution.

## Documents

Stockholm, Riksarkivet, Diplomatica Muscovitica, SE/RA/2113/2113.1/3/b/602, *Kommissarien Adolf Ehbers (Eberschildt), Moskva,
1662-1666* (172 images, IIIF series R0003225, public viewer sok.riksarkivet.se, no login). Letters of the Swedish commissary in
Moscow to Charles XI (the Regency), in German. No images are included here: the IIIF manifest carries no rights statement.
Credit for the images: "Riksarkivet, SE/RA/2113/2113.1/3/b/602, bildid R0003225_000nn".

| image | role here |
|---|---|
| 106 (Moscow, 17 July 1664) | training: the key was learned from its glosses |
| 108 | training (second copy of the letter of 106) |
| 138, left page | held out: first 160 cipher groups, transcribed after the key was frozen, measured once |

Code runs appear on nearly every image from about 98 to 145, and at 81 and 160; they were not transcribed beyond the three images above.

## System and key (`key.tsv`, CC BY 4.0)

A German letter substitution with homophones. Two-digit groups 15-95, separated by dots, mixed with clear German; Arabic numerals
(3, 12, 2000, 2500) are written in clear. The order is roughly alphabetical (15 a, 16 b, 18 c, 20 d, 22 e, 24 f, 36 g, 38 h, 39 i,
40 k, 41 l, 43 m, 45 n, 47 o, 48 p, 51 r, 94 s, 95 t, 67 u, 68 v, 69 w, 72 z), with second numbers for frequent letters
(77 a, 81 e, 25 f, 89 n, 90 o) and numbers for doubled letters (42 ll, 44 mm, 54 ss). 74 = ä rests on one word.

After the measurement, from the glosses of images 101, 103 and 138: 53 = s (nichts, etwas, smolinsko, naschokin) and 55 = t
(tractiren). These two rows are derived, marked "post" in `key.tsv`, and were not tested. 46 (image 106, "51.43.15.46") is unresolved.

## Validation (`validation.txt`, `frozen/`)

The protocol (`frozen/PREREG.md`, in French, SHA-256 0d67cc26...) was written after reading a few pairs on image 106 and before
any transcription of the held-out part. The key was learned on images 106 and 108 only (53 glossed words, `frozen/PAIRES-EBERS.tsv`)
and frozen (`frozen/KEY-EBERS.tsv`, 15a63f9b...). On image 138 the first 160 cipher groups were transcribed and frozen first
(`frozen/H_E-CHIFFRE.txt`, 53d9f22a...), then the gloss above them was read and frozen (`frozen/G_E-GLOSE.txt`, 341b8d3f...).
One measurement (`frozen/scripts/measure.py`, output `frozen/MESURE-E.txt`): 0.909 of characters against 0.047 for the best of
200 shuffled keys (mean 0.021), margin 0.862. Thresholds fixed in advance: >= 0.85 and margin >= 0.30. Verdict: validated.
The 9 groups outside the frozen key (53, 55) counted as wrong in the measurement.

Declared bias: the gloss is on the same image and was visible while the numbers were transcribed.

## Texts

`transcription.txt` gives the 160 held-out groups and the gloss; `decryption.txt` our decode with `key.tsv` beside the gloss;
`translation.md` an English rendering. They are phrases (the code runs), not the letter: the clear German between the runs was
not transcribed. Content: envoys to go to Poland for the boundary commission, the voivodes at Smolensk, treating with the Poles;
Marselis and Nashchokin are named.

Daniel's count on the measured portion: 160 groups; 151 in the frozen key; 9 outside it (53, 55, now s and t); 5 cut in the
binding; 0 restored. The decode matches the gloss except for spellings (kluch/klug, gesanten/gesandten, naschokin/naskokin).

## Gloss inventory

A gloss over every run on images 81, 98R, 101, 102R, 103, 106, 108, 124, 133, 138 and 143, and no bare passage found, which agrees
with leads review n09 (106, 108, 112, 114, 119, 121, 138, 140, 145, 160). 143 repeats the letter of 138; the foot of 103/104 holds copies.

## Prior work

- The glosses are the decipherment of the time (credited `contemporary`, prior solution).
- Leads review n09: nothing on DECODE, at Cryptiana (Tomokiyo) or in Lasry's lists; no edition found.
- No target, branch or PR for Ebers, Eberschildt, R0003225 or Diplomatica Muscovitica 3/b/602 in this repository (GitHub API, 10 Nov 2026).

## Related

Lead 2316 (Johan von Lilienthal, Diplomatica Muscovitica 1/36/82) is a different system (a nomenclator of about 390 values); work
in progress, not part of this target.

## Limits

- One reader (an agent), on 3000 px images; no human palaeographic check.
- Two training images, one held-out page; 53 and 55 untested; 46 unresolved; the few 4-digit groups not seen in the parts read.
