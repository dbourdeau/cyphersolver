# Soviet radiograms Nr 451 (Krassin) and Nr 523 (Lutowinoff), 1921: system, table and reading

Two figure radiograms from Berlin to Moscow, intercepted in June 1921 by the US High Commission at Constantinople and filed in NARA RG 59, 861.00 (microfilm M316 roll 43, frames 0427-0428 and 0432). The cipher system and its table were recovered from the ciphertext alone, and both messages are read. The file is part of catalogue item 669 of the Cyphersolver ledger, "Soviet and German cipher radiograms of 1921".

**Relation to earlier work.** As of 10 November 2026 no decipherment and no plaintext of these two messages was found in the places listed in `docs/PRIOR_CHECK.en.md`. On the same file, Cyphersolver has deciphered two letter transpositions (Lejava Nr 1196, Voikov Nr 1883) and has published its work on the figure traffic as "no group value recovered" (targets/kopp1921 and neighbours). The two messages read here do not appear in those notes.

**State: full reading (both messages).** Pairs that read as sense: 750 of 764 in Nr 451 (98.2%), 279 of 288 in Nr 523 (96.9%). What is left is pairs outside the table (nine kinds, apparently numbers and abbreviations) and words with one wrong letter (`docs/OPEN.en.md`).

**No human has checked the transcription.** It was made by an AI from NARA's OCR and compared with an independent reading of the images by another AI. Agreement between AIs does not replace a human check.

## What the messages say

Nr 451 (dated 30 May 1921, repeat sent 14 June; Krassin to Chicherin):

> The work of the Berlin trade representation is developing quite normally. From all business circles I receive the most flattering comments. The Auswärtiges Amt also notes a favourable change in the general atmosphere around the trade representation. From conversations with Lutovinov and Stomonyakov I conclude that the auditing commission has produced rich material which characterises the preceding period of the Berlin representation very unfavourably. They work like horses, and this delays the conclusion. I most urgently ask you to send Comrade Kulyabko to Berlin as soon as possible; his help in the work of the auditing commission is absolutely necessary. Under the agreement the visa must be given by Stähler, and I ask you to insist on this. In no case take any decisions or measures without waiting for the report of the auditing commission; otherwise you will confuse all its work and make it easier to cover the traces. When the audit is finished Lutovinov and Stomonyakov will come to Moscow to report in person.

Nr 523 (dated 14 June 1921; Lutowinoff to Chicherin for Litvinov, copies to Chicherin, Molotov and Shlyapnikov):

> Received your letter of [...] June. I find the position you have defined for Kopp in Berlin absolutely inadmissible. Kopp has stated that the Narkomindel has already decided to leave him in Berlin as plenipotentiary. If this is so, I categorically protest against his appointment before the end of the audit, and I also demand urgent instructions to whom to hand over my duties. In [...] hours I hand over to Brodovsky.

The Russian text as deciphered is in `docs/READING.en.md`; the reading pair by pair is in `data/reading_451.tsv` and `data/reading_523.tsv`.

## System and table

1. Each letter of the plaintext (Russian in telegraphic style, prepositions dropped, й written и and ё written е) becomes a pair of digits from a 5 x 6 table. The first digit is 6, 7, 8, 9 or 0; the second is 0-5.
2. The pairs are written row by row into a square with a side of N digits, N/2 letters to a row. N is spelled out in Russian before the groups (SOROK = 40, DWADZAT TCHETYRE = 24). The rest of the square is filled with 00.
3. The square is sent column by column, top to bottom, starting from one edge (the columns are not permuted).

```
     0  1  2  3  4  5
6    е  в  ь  э  к  щ
7    а  ф  я  з  н  р
8    б  ы  г  л  ч  ю
9    ж  ·  ш  и  д  о
0    ·  т  п  х  у  м        06 = с   10 = full stop   33 = comma   00 = filler
```

In Nr 451 the digit columns run first digit, second digit, and the rows are read **right to left**. Nr 523 is the mirror image: second digit, first digit, rows read left to right. Cut the received digits into runs of N and the columns alternate between high digits (6-9) and low digits (1-5); that is how the system shows itself.

Decrypt: `python3 src/decrypt.py`. Tests: `python3 -m unittest discover -s tests`. Control: `python3 src/control.py` (needs `wordfreq`).

## Figures

| Item | Nr 451 (1,600 digits, 764 pairs) | Nr 523 (575 digits, 288 pairs) |
|---|---|---|
| Pairs that read as sense | 750 (98.2%) | 279 (96.9%) |
| Control (letter values of the table shuffled 1,000 times; mean 4-gram score) | 0 at or above the real key (real -11.127, best shuffled -14.686) | 0 at or above the real key (real -12.329, best shuffled -14.796) |
| Same table, rows read the other way | -13.889 | -14.282 |
| Used to build the table | yes (annealing on the ciphertext alone) | no (the table from Nr 451 was only applied) |
| Digit agreement with a second reader's transcription (OpenAI Codex) | 1,598/1,600 (99.88%) | 575/575 (100%) |
| Two-way choice on the image (80 sampled agreed digits + 10 control items; times Codex and Sonnet chose the transcribed digit) | 90, 90 | 90, 90 |
| Calibration (against a contemporary decipherment or an edition) | none found | none found |

How the figures are counted, and the caveats, are in `docs/METHOD.en.md`.

## Use of AI

Selection of the material, the system, the table, the reading and the documents: Claude Fable 5.2 (Anthropic). The transcription starts from the OCR served by the NARA catalogue. Second transcription: OpenAI Codex (codex-cli 0.163.0-alpha.10.2, gpt-6-astra, reasoning effort high). Two-way choices on the image: the same Codex and Claude Sonnet. Search for earlier work: Claude Fable 5.2 and a second reader who did not make the reading (Claude Sonnet). The human directed the work and decided on publication. No human compared the images with the transcription or the reading.

## Files

- `data/`: ciphertexts (`ciphertext_451.txt`, `ciphertext_523.txt`), table (`key.tsv`), reading pair by pair (`reading_*.tsv`)
- `src/`: decryption (`decrypt.py`), control (`control.py`)
- `second/`: prompt and output of the second transcription
- `docs/`: method (METHOD), reading (READING), open points (OPEN), search for earlier work (PRIOR_CHECK)
- `SOURCES.en.md`: sources and frame numbers. No images are in this repository

## Licence

Code: MIT. Own documents and data: CC BY 4.0 (`LICENSE`).
