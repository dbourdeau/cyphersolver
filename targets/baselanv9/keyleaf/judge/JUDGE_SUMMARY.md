utc 2026-11-25T03:43:24Z | model claude-opus-5-5 | effort not exposed | session https://claude.ai/code/session_01P5UF3myhVjFtgU9vTMj1qn | sha256 BRIEF.txt af20815f4a928f7af259ae3a9a76d371528ab093899f20d3022cc0a55dd06a8a | sha256 decode.txt 41b28e8be72dfc162d2c6c8d9a17822f4a2a9c350555eac6a43d56d6fe078dc6

# Judge summary: baselanv9 pass 2 (key leaf), strict

Inputs read: BRIEF.txt and decode.txt only. 144 lines scored, every a-z letter. Per-word tags and per-line counts in JUDGE_OUT.tsv.

## Totals (letters; % read = S/(S+E+N))
| Section | S | E | N | [?] | Arithmetic | % |
|---|---|---|---|---|---|---|
| TRAIN f4r | 600 | 17 | 86 | 16 | 600/(600+17+86)=600/703 | 85.35 |
| TRAIN f4v | 732 | 19 | 102 | 12 | 732/(732+19+102)=732/853 | 85.81 |
| H1 | 237 | 15 | 130 | 5 | 237/(237+15+130)=237/382 | 62.04 (UNDER 65) |
| H2 | 510 | 25 | 182 | 7 | 510/(510+25+182)=510/717 | 71.13 |
| H3 | 51 | 2 | 16 | 1 | 51/(51+2+16)=51/69 | 73.91 |
| PENT | 2221 | 48 | 251 | 26 | 2221/(2221+48+251)=2221/2520 | 88.13 |
| ALL | 4351 | 126 | 767 | 67 | 4351/(4351+126+767)=4351/5244 | 82.97 |

H3 pentacles: P3 19/(19+1+16)=19/36=52.8% UNDER 65; P4 32/33=97.0% over.

## Pentacles (PENT): 62 scored, 57 at/over 65%, 5 under
Under: S1-025 11/26=42.3%; S1-039 27/44=61.4%; S1-070 25/42=59.5%; S1-071 23/37=62.2%; S1-096 23/40=57.5%.
All others at/over (per-line % in JUDGE_OUT.tsv).

## Judging rules applied
- Transposed letters (surgesn, ruebatn, obedietn, uenietn, treumnt, habesn ...) = two slips = N. This recurring pattern costs much of the N.
- One slip (wrong/missing/added letter) = E, 1 letter E, rest S. For a missing letter, one existing letter is counted E.
- A real Latin word that misfits the grammar by one letter is E (quem for quae, amore for amorem, morte for mortem); otherwise a Latin word is S.
- [?] words: S if recognisable with at most one further slip, else N. ~ not scored; i~ri scored E (i for x in xri).
- Words broken at a line end WITHOUT "=" were not joined (brief allows only "=" joins): cogno|scu, po|tui, omni|um, opu|sculo scored N (27 letters). If joined: f4r 612/703=87.06%, f4v 746/853=87.46%, overall 4377/5244=83.47%.
