# Held-out test on Ridolfi doc. 114, and what its gloss taught

14 November 2026. Ridolfi's letter of 22 October 1494 (ASF MAP LXXIV doc. 114, cc. 258v and 259v) is in the same cipher as 112, 113 and 115 and carries a contemporary interlinear decipherment. It was not used in building the readings: its images were downloaded on 13 November with the rest of docs 97 to 115, and the working notes record no use of them (a statement about the record; the hashes below fix what the files are, not when each was written or seen). Brice Dudout tested our key on it first ([cyphersolver #589](https://github.com/dbourdeau/cyphersolver/issues/589)); Daniel Bourdeau asked us to run it as our own held-out test. This folder is that test, and then the use of 114's gloss as an exemplar set.

## The measurement

Protocol and hashes: [PREREGISTRATION.md](PREREGISTRATION.md), written before the cipher leaves or the printed text were opened by the session that scored.

- One agent located the cipher lines and painted out the gloss ([blocks.md](blocks.md)); it saw the gloss and it set the block boundaries. A second agent, given only the masked crops, the label and shape inventory without values, and letters 112, 113, 115 with their label sequences as exemplars, transcribed 865 signs in 27 lines ([transcription-frozen.tsv](transcription-frozen.tsv), [its notes](transcription-blind-notes.md)). The file was hashed before the decoder ran.
- How blind this was. The transcriber did not see the gloss, the key values or the printed text. The label names it was given are shape names for most signs but mnemonic for a few (BB, CC, NN, ET, TH), so it was not blind to those values, and the exemplar label sequences carry the earlier transcribers' sign divisions. It was told to leave out a small raised two-sign mark that occurs three times on c. 259v (lines 4, 13, 16) and that the masker could not classify; the gloss later showed it is cipher, the raised *ta* of *M[aes]tà*. The session that wrote the protocol and ran the scorer had seen c. 258r (clear text) and the two plaintext fragments quoted in issue #589.
- Key: `key.json` at commit 46dec7b, unchanged ([key-46dec7b.json](key-46dec7b.json)).
- Reference: the printed text in Desjardins and Canestrini, *Négociations diplomatiques de la France avec la Toscane*, t. I (1859), pp. 585-586 ([reference-desjardins.tsv](reference-desjardins.tsv)), fetched after the freeze.

| | Agreement | Best of 1,000 shuffled keys | Mean shuffle |
|---|---|---|---|
| **Pre-registered: any listed value of a sign counts** | **0.838** | 0.379 | 0.286 |
| First listed value only | 0.775 | | |

The bar was 0.85 and the result is under it by 0.012: the pre-registered criterion was not met. The score is character agreement after alignment, with word division discarded and any listed value of a two-valued sign allowed; it is not the share of words or signs read correctly. The protocol also promised a count of words that come out exact; that count was not made. Dudout's independent figure on the same letter was 0.774 against 0.397. `python3 score.py transcription-frozen.tsv reference-desjardins.tsv` reproduces [result-desjardins.txt](result-desjardins.txt).

What costs agreement: Desjardins prints a modernised text (*elezione* for the gloss's *electione*, *dilezione* for *dilectione*, *gli disse* for *li dixe*) and writes out what the cipher abbreviates or gives as one sign (*il Re*, *il duca*, *Sua Maestà*, *prefata*); the transcriber's own errors; and the boundaries of block 5.

Block 5 was delimited wrongly at both ends. Its first three marks on c. 259v line 3 are probably the clear abbreviation *ch[e] q[ua]n[do]*; the transcriber flagged them and counted them as cipher because the boundary list said so. Its last reference word, *si*, is clear text in the margin before the clear *trovava*. The last group of line 5 (*el quale*) also looks like clear script and is not adjudicated. The frozen figure stands as measured. As a diagnostic made afterwards, with no new shuffles: dropping *si* from the reference gives 0.839, and dropping *che quando* and the three marks as well gives 0.844, still under the bar.

**After the fact, not pre-registered:** against the gloss as read from the leaf ([gloss/](gloss/), [reference-gloss.tsv](reference-gloss.tsv)) the same frozen transcription scores 0.886 (best shuffle 0.378). The gloss letters are 4 to 6 px tall and about a dozen spellings were settled by counting the cipher signs beneath them, so this is a comparison with a partly cipher-assisted reading of the gloss. It is not independent validation, and the difference from 0.838 mixes modernised spelling, abbreviation and different block boundaries, so it does not measure any one of them.

## What the gloss gave

From here on 114 is no longer held out.

1. **÷ separates into n and c by its dots, as the key sheet itself has it.** Enlarged, the sheet's cell for c shows the dash with a dot below only, and its two cells for n show a dot above, one with a second dot below. We had recorded ÷ as one sign with two values. A third agent sorted every ÷ of 114 by what the ink shows, without values ([shapes/doc114-A.tsv](shapes/doc114-A.tsv)). Joined to the reference afterwards through the scorer's alignment, not sign by sign by hand ([aligned-signs.tsv](aligned-signs.tsv)): a tick or dot above the dash is *n* in 32 of 34; a dot below only is *c* in 14 of 21. The mask had painted out much of the space around the signs in 114, so the same sort was repeated on the unmasked letters, by agents who had the labels but not the values: in 112, 113 and 115 a mark above (with or without a dot below) is *n* in 73 of 73 and a dot below only is *c* in 34 of 34, 34 and 20 of them in words where the word alone decides; in Alamanni's letter 12 of 12 and 6 of 6 in such words ([shapes/ridolfi-A.tsv](shapes/ridolfi-A.tsv), [shapes/alamanni-A.tsv](shapes/alamanni-A.tsv)).
2. **Ridolfi's d and l are different signs.** Both are a tall stem ending in an open hook. With a horizontal arm to the right at the baseline it is *l* (32 of 33 in 114; 32 of 32 in the three letters); without the arm, with or without a bar across the stem, it is *d* (38 of 43; 57 of 57).
3. **A sign for ll.** A d-shape with a long bar across its ascender stands in 114 where the gloss has *quella*, *alla*, *quello*, *fanciullo*, *Isabella*, *quelli*; the two l's can be seen in the gloss ink at *q[ue]lla* and *alla* on c. 258v. In 112, 113 and 115 the same form gives *castello*, *a lla camera*, *ne lletto*, *della*, *quelli*, *quello*, *quella*, *Isabella*, *non volle*, *cavallaro*, *ne lla città*, *a lla corte*: fourteen uses, all words. In Alamanni's letter it is the sign we could not place in *mante[?]o*, which becomes *mantello*.
4. **bb** (cross with dots): *gioverebbe*, *harebbe*, *passerebbe*, *sarebbe*, 4 of 4, with both b's visible in the gloss at *giouerebbe* and *passerebbe*.
5. **Person signs.** The long-tailed 2 with a raised c is glossed *Re* five times. The same base with another raised letter is glossed *Duca* twice ([gloss/signs.md](gloss/signs.md)); once with a raised 3-like letter and once with a raised h-like letter that may be the hook of letter 112. The 9-shaped null stands after the first of them and before the second; in 112 it follows the sign twice out of three. That is a good match but not a certain one at 1272 px, so the sign of 112 stays inferred, now as [il Duca].

The sorts on 112, 113, 115 and on Alamanni's letter were made by agents that used the existing label sequences to find the signs, so their agreement with the values the words had already forced (54 of 54 and 32 of 32 in Ridolfi, 18 of 18 in Alamanni) is a consistency check and not an independent blind confirmation. What is independent of our readings is the key sheet's own c and n cells and the gloss of 114.

`apply_shapes.py` is the script that relabelled the two transcriptions as published at 46dec7b from the shape tables (`Na`, `Nb`, `/a`, `/b` for the ÷ forms; `Zh`, `Za`, `LL` for Ridolfi's stem signs). Only signs sorted with high confidence were relabelled; the rest keep the two-valued label or their recorded alternative, and their word keeps its tier. The spellings that changed with the ll sign and the person-sign rows were then edited by hand.

## Gabbrielli's copy book

Dudout pointed to Gabbrielli's nineteenth-century *Chiavi delle cifre delle lettere ai Dieci di Balìa dal 1424 al 1530*, vol. 1, on Vincent Ilardi's microfilm reel 58 ([Yale Dataverse, doi:10.60600/YU/XKVOWE](https://doi.org/10.60600/YU/XKVOWE)). Read from frames 58-29 and 58-38:

- **No. 25, "Alamannis (de) Petrus", 1492, Dieci filza 39,** is the alphabet of MAP LXXII 183, as far as Gabbrielli recovered it (he has no b, g or z, and one sign for d). His "doppie" are ll (the barred d-shape), nn (the large e-loop), rr (the barred circle) and tt, and the ÷ forms he draws under C and under N look different, though the dots are hard to make out on the film. That corroborates the nn and rr we had only fitted, and it is where the ll sign was first seen. It is a reconstruction made from deciphered letters, three and a half centuries later, so it is corroboration and not a second key sheet.
- **No. 34, "Johannes Batta de Rydolphis", 1495, Dieci filze 40-42,** is a different alphabet, with its own doppie and name numbers. It is not the alphabet of the October 1494 letters.

Not tested here: no. 25 against Alamanni's doc. 96 as a separate key (as far as it goes it is the alphabet of 183), and nos. 13, 26 and 30.

The frames and the ASF images are not redistributed. The shape sorters' cut-outs are image crops and are not in the repository either; the tables give each sign's position.
