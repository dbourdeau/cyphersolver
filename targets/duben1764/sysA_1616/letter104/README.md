# duben1764, system A: the letter on 104R-105L ("ce 15 de May 1764"), read in part with key_c02

Work of 17 Nov 2026 (Brice Dudout's session, Claude Opus 5.5, AI agents). Riksarkivet K 259 (IIIF A0073297), images 104 (right) and 105 (left).
Text files only; images on the Riksarkivet IIIF server (`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`).
No new measure was made; key_c02 is unchanged (SHA-256 `1813621c87e8...`).

| file | what it is |
|---|---|
| `passes/c104R-105L_passA.txt`, `passes/c104R-105L_passB.txt` | two blind transcriptions by two independent sub-agents (half-line crops / quarter-line crops); neither saw the other or any earlier file |
| `disagreements_104R-105L.txt` | the substantive differences and the reading kept (settled on full-size zooms) |
| `c104R-105L_merged.txt` | merged transcription: 104R 17 number lines, 105L 14 number lines; 597 groups, 558 of 100 or above; 26 lines still carry a `?` |
| `decode_104R-105L_key_c02.txt` | decode with key_c02 unchanged (key_c02 knows 531 of the 558 groups, 95.2 %) |
| `decode_104R-105L_key_c02_plus_conjectures.txt` | the same with the conjectured values of `../letter90/check_c02/conjectures_key_c02.json` in braces (not part of the key) |
| `reading_104R-105L_key_c02_tagged.txt` | strict tagged reading: sure / {probable} / ‹n› unresolved |

## Identity and prior state
- Chiffer n:o 1, system A: same hand, same "mon cher Comte" opening as the other St Petersburg letters of the file; key_c02 decodes French from the
  first line. Header in clear "ce 15 de May 1764" (faint). 105L ends the letter; a Swedish archival note follows. The contemporary decipherment
  106R-107L belongs to the other letter of the same date (105R-108L, tested in `../may1764/`); no decipherment of 104R-105L was found.
- Nobody had transcribed or read these pages: Bryan Payne's inventory (PR #185, `payne2026/inventory.csv`) lists image 104 from a thumbnail only;
  his May transcription covers 105R-108L. No other PR, issue or target mentions 104R (repository searched 17 Nov 2026).

## Strict count (Daniel's rule)
`python3 -I ../letter90/check_c02/count_words.py reading_104R-105L_key_c02_tagged.txt`:
**233 sure + 43 probable of about 291 words: sure 0.801, sure + probable 0.948.** Under the 95 % rule the letter is **read in part** (just under).
Most probable words rest on a group absent from key_c02 (e.g. 429 "même" three times, 539 "qua", 603 "sti") or on a doubtful group.

## What it says (English, from the reading; unresolved parts in brackets)
[Panin gave] the strongest assurances of the intention [...] of the Empress to concur with the King in everything that may make his situation more
favourable and put our affairs on a solid and lasting footing. I thanked him warmly for the confidence he had shown me, which he promised to
use, adding that, as the King had acted so frankly in communicating [his] true views, which the Empress herself had found as just as they were
moderate, he hoped that this Princess would on her side act with the same sincerity and without any detour, which could only have the worst
effect. Monsieur Panin protested that nothing was more real than the Empress's intention to restore the King's authority and to remedy the
drawbacks of our constitution, which he admitted was faulty in every way. Through these assurances, however, I made out some fear of a total
revolution among us, an apprehension I try to dispel as far as I can, saying even that the court is more and more losing the hope it had of
bringing round, little by little, [the] members [...] in the idea that the King seeks and expects no other support than that of Russia. With a
little patience we shall know where we stand, and I promise you not to let myself be amused for long by fine words. One must take [a course],
and the one in which the King finds his greatest security must be preferred even to the friendship of the Empress, which becomes useless if this
Princess is too slow to carry out her promises.

## Limits
Transcriptions by AI agents, not checked by a palaeographer; 105L05-105L07 are blotted and overwritten (struck groups uncertain). The reading of
the probable words depends on conjectured values that no period clear checks for this letter.

## 18 Nov 2026: blind digit-form check (Brice Dudout, sheet of 17 Nov evening; 4 of 4 controls right)
Applied in `reading_104R-105L_key_c02_tagged_plate1711.txt` (the tagged file above is kept): 104R01 g10 = 292 ("fortes") and 104R08 g7 = 668
("vues") become sure. 104R02 g19 = 233 is confirmed, but g18 reads 562 (absent from key_c02), so "rendre" stays probable; 105L07 g5 = 585 is
confirmed, but "soutien" also rests on the blotted 357/448, so it stays probable. Against the sense (words stay probable): 104R03 g9 534
("favorable"), 104R05 g12 557 ("qu'il"), 104R17 g14 201 ("crainte"), 105L03 g11 212 ("de"); 105L07 g9 582 sits in an unresolved span.
**Count: 235 sure + 41 probable of about 291 words: sure 0.808, sure + probable 0.948: read in part.**
