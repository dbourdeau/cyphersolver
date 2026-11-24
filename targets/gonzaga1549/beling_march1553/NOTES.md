# The Spanish enclosure to Philip’s letter of 14 March 1553

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera F, Felipe II, sfasc. I, cc. 35–40. Three pages in the same file give continuous Spanish corresponding to six passages of Philip’s cipher letter to Ferrante Gonzaga. The Italian list of topics is on 36r. The Spanish is on 37r, 37v and 38r. The archive displays the wrapper, 39r, before the final written leaf. Its twelve canvases include the original dateline on 40v. The role of the Spanish sheets as a draft, extract or decipherment remains unknown. [Library manifest](https://edl-jarvis.cultura.gov.it/meta/iiif/6990ecfe-8ee7-4994-b2d6-3ccc332ee9e2/manifest) · [37r](https://edl-jarvis.cultura.gov.it/images/iiif/db/f063418c-a5c0-49e0-9cdb-4c5c76bda4d9/full/1200,/0/default.jpg) · [37v](https://edl-jarvis.cultura.gov.it/images/iiif/db/5e882715-411a-44fa-a585-f0f2f2369da8/full/1200,/0/default.jpg) · [38r](https://edl-jarvis.cultura.gov.it/images/iiif/db/28117cb9-ce4f-4904-a1a7-7d77fa71905f/full/1000,/0/default.jpg)

WAINUT transcribed 64 cipher lines and produced the rough output in the adjacent wainut directory. Issue 220 and the target notes identify the Italian slip. Issues 615 and 618 discuss other comparisons and the shared Imperial Cipher. We did not find these three Spanish pages identified in those discussions or target notes. The Spanish opening continues the original’s “principalmente” with a clause about paying the troops in Piedmont. The six passages cover pay, the shortfall in light horse, expenses and the French occupation, Siena, the Spanish infantry, and the supply of pikes and powder. [WAINUT’s work](https://github.com/dbourdeau/cyphersolver/tree/57bd42d0f82b73a8452db0472792caf49e0aefef/targets/gonzaga1549/wainut) · [Issue 220](https://github.com/dbourdeau/cyphersolver/issues/220) · [Issue 615](https://github.com/dbourdeau/cyphersolver/issues/615) · [Issue 618](https://github.com/dbourdeau/cyphersolver/issues/618)

## Which passages correspond?

The working transcription in spanish_enclosure.txt records the three Spanish pages, expands abbreviations and flags uncertainties. This is a single reading of clear manuscript prose. All six consecutive blocks of WAINUT’s output match their assigned paragraph more closely than the other five by normalized edit similarity after removing “su Magestad”. The boundaries were chosen after reading the witnesses. The weakest pair, B56–64, scores .298 against .265 for the closest alternative. Run `python3 -I -B check_correspondence.py` here to recompute all 36 scores from the two transcriptions and check the published table. These matches establish the order and subject of the six passages.

Two independent readers agreed on 20 of 32 signs at the opening of the March cipher. Applying Brice’s published table gave the uninterrupted letters “lapagadela” in the expected place on 37r. Whole-prefix similarity reached .433 against a preset .75. The best of 1,000 shuffled keys scored .340. This test missed. The two rows have 6/10 and 14/22 agreed positions. The planned October 1552 transfer therefore stopped before testing. The original two reader files, plan, 1,000 control scores and result are included in opening/. From this directory, `python3 -I opening/check.py` independently reconstructs the two alignments and checks all 1,000 scores against the repository's existing Imperial table. Its frozen plan has SHA-256 8bd0177c9d8a50e805fde53f94e826d1f82cb11151cb4430e2654d4ac6c66ad3.

## What the Spanish sheets can predict

We fitted ten changes in how WAINUT’s March sign labels are interpreted, using B01–40 and the first three Spanish paragraphs. On the last three paragraphs, B41–64, the inherited decoder required 621 edits for 865 Spanish letters. The fitted decoder required 487. Each paragraph improved. The best scores in 1,000 full-key shuffles and 1,000 shuffles redistributing just the changed values were 677 and 528 edits. Both checks passed. For example, B42 tokens 9–15 give “de ser por ver” and B50 tokens 12–16 give “ya su Magestad os” after normalizing historical letter forms. These examples were selected after scoring. Cipher words credited as newly read under the two-reader rule: zero.

The frozen changes performed worse on two further transcripts of Charles V’s letters from 1549. The combined edit distance increased from 356 to 380 over 928 letters. Thirteen correction shuffles did at least as well. This test missed. The comparison letters are 30 September and **20 November** 1549. The separately discussed 14 November letter supplied a retrospective sign-label diagnostic. Of 172 candidate positions in that 14 November file, 65 met the frozen positional restrictions. The inherited emission matched 56, the March change matched three and neither matched six. The inherited map used this very letter in its development. The 107 exclusions remain visible in paired_positions.tsv and the line alignment in paired_lines.tsv. The document-transfer miss and the paired-label comparison measure different things.

## A second reading of the Spanish pages

Another reader transcribed the three Spanish pages directly from the photographs without seeing the first transcript, the cipher or the fitted table. The readings differ over tense and spelling. On 37r the first reader gives “Sinifica[n?]os nos” and the second “Significays nos”. On 38r the second reader records a canceled “gente” before “infanteria” and a correction above the line for the first mention of pikes. At the later mention the first reader gives “pignas [?]” and the second “picas”. Both readings are provided for checking against the image. Neither replaces the frozen reference.

The same ten changes, tested without refitting on the second reader’s last three paragraphs, reduced edits from 621 to 489 over 865 letters. Both control sets again had zero ties or wins out of 1,000. Their best distances were 676 and 526. This supports the March result under an independently transcribed reference. It supplies no additional cipher words or evidence for transferring the table to another document.

## Reproduction

From this directory in a disposable copy of the repository, run the commands below with Python 3. The scripts use the existing source files in the adjacent wainut directory and regenerate their output tables. PLAN.md and PLAN_transfer.md preserve the original calibration and cross-letter plans. The independent enclosure reading has a separate plan in second_witness/. Their SHA-256 digests are 3ba51eaf7cf89a840392e1e4def72d366d45b1c75e05be45168f3c2fabff2e9b and a0bcff2ffcef89a942d9d0aa5b1d80fc199fff9b0a2f139aa2431922fa04d268 respectively. The frozen fitted table hashes to 96194a7090753441209671470f582981def06ea0617e34feceee3b1675adb5bc.

```sh
python3 -I -B calibrate.py validate
python3 -I -B calibrate.py fit
python3 -I -B calibrate.py test
python3 -I -B transfer.py
python3 -I -B examples.py
python3 -I -B second_witness/score_reference.py
```

Source tracing and collation by Andrew Beling with AI agents. Cipher transcriptions and original rough readings by WAINUT. Historical key and sign atlas in the associated Imperial Cipher work by Brice Dudout.

AI agents did this work; no person has checked it.
