# casimir1629: Pfalzgraf Johann Casimir to Ludwig Camerarius, 1629 (BSB Clm 10382), key of the two-digit letter cipher

Status: solved at the time (contemporary interlinear decipherment on the letters); key rebuilt from the glosses and validated on a held-out letter (Brice Dudout, 4 Nov 2026; 0.873 of characters vs 0.170 for the best shuffled key). The clear text of the letters is not transcribed here.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Lead no. 2187, found by WAINUT
(https://github.com/WAINUTAI) on 3 Nov 2026 while paging Clm 10382, and vetted in the leads review of 4 Nov 2026 (batch b71).
Not in the catalogue; no DECODE record.

## Documents

Munich, Bayerische Staatsbibliothek, Clm 10382 (Collectio Camerariana 32), letters of Pfalzgraf Johann Casimir
(Zweibrücken-Kleeburg) to Ludwig Camerarius, 1624-1629 (Johann Casimir series within n. 106-164). Digitised microfilm, MDZ
bsb00112117 (Public Domain Mark 1.0; images credited "München, Bayerische Staatsbibliothek"; none are included here).

| piece | date | MDZ scans | role here |
|---|---|---|---|
| n. 138 | Feb 1629 | 470 | training: the key was learned from its glosses |
| n. 140 | Calmar, 3 July 1629 | 476-477 | held out: transcribed after the key was frozen, measured once |

Other scans with cipher, not transcribed: 418 (about 1624), 447-448 (July 1626), 469, 471 (Feb 1629), 475, 482, 486 (Calmar, 10 Oct 1629).

The cipher passages carry a word-by-word decipherment written above the lines at the time. The content is therefore not new:
what this target adds is the key as a table that can be reused, with a held-out test.

## System and key (`key.tsv`)

A German letter cipher. Each letter has three homophones, in a block of three consecutive numbers:
14-16 a, 17-19 g, 20-22 n, 23-25 t, 26-28 b, 29-31 h, 32-34 o, 35-37 u/v, 38-40 c, 41-43 i, 44-46 p, 47-49 w, 50-52 d, 53-55 k,
59-61 x, 62-64 e, 65-67 l, 68-70 r, 71-73 y, 74-76 f, 77-79 m, 80-82 s, 83-85 z. Numbers 86 and up are nulls. 1-13 and 56-58 were
not seen. The numbers are written run together, without word division. Names (Radziwill, Schweden, Littaw, Grossfürsten) are
spelled; no nomenclator was seen on these leaves.

It is not the code of the neighbouring pieces: lead 2189 (Oxenstierna, 10 June 1625, same volume) is another letter cipher, in
Latin (t = 15, 46; u = 23, 26, 35, 38); lead 2190 (Clm 10380 n. 60-61, 1636) is a 3-4 digit nomenclator; `targets/camerarius1621`
is a 4-digit code.

## Validation (`validation.txt`)

The protocol was written and hashed before any measurement. The key was learned on scan 470 only (majority letter per number,
then extended by blocks of three), frozen by SHA-256, and measured once on scans 476-477, which were transcribed after the
freeze: 33 glossed words, 165 characters. Score 0.873 of characters (whole words 0.667), against 0.170 (0.030) for the best of
200 shuffled keys; margin 0.703. The thresholds, fixed in advance, were >= 0.85 and >= 0.30 above the best control.

After the measurement, two changes were made, and they are outside the test: 71-73 = y (learned as i from the gloss "bei",
written "bey" in cipher; the held-out part has freyheit, meyne, heyrath) and 44-46 = p (one word, "party"). The other errors are
the cipher clerk's spellings (heuraht, bunt, nemmen) or numbers hard to read on the microfilm (69/64, 23/24).

## Texts

`transcription.txt` lists each cipher group with the gloss written over it, and `decryption.txt` gives our decode with
`key.tsv` beside the gloss. They are a word list, not the letters: the clear German text around the groups was not
transcribed. 99 of the 127 glossed groups not cut by the binding decode exactly as glossed.

Unglossed groups on the scans read (Daniel's count): 4 non-null groups, 1 certain ("wie"), 1 probable ("daler", the end of
"Reichsthaler" cut at the binding), 0 restored, 2 unresolved.

## Prior work

- The glosses on the letters are the decipherment of the time (credited `contemporary`, prior solution).
- Halm 1874 p. 60 lists the letters (1622-1638) without a cipher note. No edition found. Not on DECODE. Nothing at Cryptiana
  (Tomokiyo) or in Lasry's lists (leads review of 4 Nov 2026).
- No target, PR or issue for Clm 10382, Johann Casimir or Kleeburg in this repository (GitHub API, origin/main c786648b,
  5 Nov 2026).
- Not opened: F. H. Schubert, *Ludwig Camerarius* (1955; 2nd ed. 2013), and Stålhane 1934 (the "Camerarius key" cited by
  Waldispühl and Kopal). If either prints this key, it should be credited and our role lowered.

## Limits

- One reader (an agent), on a microfilm 1334 px wide; 3/5, 4/9 and 23/24 are easy to confuse. No human palaeographic check.
- One training page; 44-46 rests on one word.
