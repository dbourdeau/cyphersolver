# Catalogue 1565 and 1570: independent verification, 3 Nov 2026

Verdict: confirmed with corrections. Both keys are real, and both documents stay "read in part". The percentages are too
high, and the 1565 reading has wrong words and unmarked repairs that must be fixed before it goes anywhere.

| document | status claimed | honest status now |
|---|---|---|
| 1565, cc. 15-16, 8 May 1545 | read in part, 77% of cipher words (89% with clear) | read in part, key confirmed. About 204 of about 301 cipher words (68%). Fails the 95% bar |
| 1565, cc. 48, 49r | not read | not read. Not tested here. "Too short" has no matched control yet |
| 1564 | sampled only | not attempted, as claimed |
| 1570, Vittoria Gonzaga | read in part, 105 of 132 number words (80%) | read in part, key confirmed. 80% holds only for the words transcribed. At most about 55% of the number words on the pages seen, because most of c. 21r was never transcribed |

Nothing here reaches the bar. Under the project rules, "read in part" is a stopping point only when every unread piece has an
outside blocker. c. 21r and c. 22v of 1570 have none, so that work should continue.

## 1. Blind test

Before opening NOTES.md, any transcription, key or reading file, I read signs from the scans and saved them to the
scratchpad. For 1565 I used the full-resolution scans. For 1570 I fetched tiles at native size (about 5000 px page width).
My sign names were my own. They were mapped to the solver's names only afterwards.

| sample | signs | disagreements | rate |
|---|---|---|---|
| 1565, c. 15v lines v01-v08 (held-out page) | 184 | 10 | 5.4% |
| 1570, cc. 20r and 21r, lines both of us read (20r.1, 21r.1) | 57 groups | 5 | 8.8% |

The 1565 differences:

- 6 are q against g. I used one label for both, so I did not separate them independently.
- 1 is P against Fq, the same kind of failure. On zoom the shapes do differ (ring on a post against a q with a lead-in), so
  the split is more than sense alone, but I did not make it blind.
- 1 is i against l, inside a nulled sign at v02.
- 1 is the last crossed sign of v08. The solver has V (4 with raised 5). The scan shows a 4 with no raised 5.
- 1 is a real solver error at v05, in section 6.

Excluding my two label failures, the rate is 3 of 184 (1.6%). A spot check by eye of r01-r02 on c. 16r also showed no difference.

Decrypting my own reading with the solver's key gives the same text. v01 is identical to the solver's raw output
("risolutohaueeiadattomgliodirema"). v03 differs only where my q stands for his g.

The 1570 differences all resolved on zoom, none against the solver:

- carico: third-from-last group is 50, not my 10.
- grano: 10 and 55, not my 20 and 15.
- tratte: first group is a faint-topped 85, not my 65. This one is shape plus sense.
- il: 45, not my 85.

carico and grano were the groups the solver changed after his first reading. My blind misreads match his first reads, and
the tiles support his corrections. 45 and 85 are hard to separate at a glance, so a lone l or t rests partly on sense.

## 2. Rerun of the decryption

My own scorer gives the same result on a different scale.

| test, on cc. 15v-16r | real | shuffled table, mean / best | scrambled sign order, mean / best |
|---|---|---|---|
| Frozen key, pass 1b | -10.229 | -13.967 / -12.893 | -12.824 / -12.283 |
| Frozen key, raw pass 1, no code list, no merges | -10.718 | -13.964 / -12.855 | -13.045 / -12.677 |
| Final key, all pages | -9.988 | -14.898 / -13.916 | -13.400 / -13.017 |

On the solver's own scoring function, the frozen table gives -7.435 exactly, as claimed. My 200 shuffles there gave mean
-10.181, best -9.510 (claimed -10.168, -9.326).

1570: I read 224 groups blind. Injective quadgram annealing on them, with no key, recovered 11 of the 18 letter values and
already produced "disturbare", "stata", "dinteresse", "fatta soriuere", "hauere". The swapped-pair table checks through all
18 letters. With the table, 213 of the 224 groups are keyed.

## 3. Held-out and freezing

**1565: pass, with one limit.**

- The file order supports the claim. The corpus was built at 00:14, before any key, and does not contain this letter.
- Four new seeds on c. 15r reproduced the frozen table 44 of 44, so it was not hand-steered.
- c. 15v-16r were not used to fit it. The frozen key matches the final key on 33 of 43 signs and 87.7% of held-out tokens.
- Limit: it was run at 00:35, after the solver had read all pages. The two pass 1b rules and the code list came from that
  work. Removing them (second row above) still passes, so this leak is small.
- Stricter control: four annealer runs on c. 15r with its sign order scrambled scored -12.24 to -12.63 on the held-out
  pages, against -10.229 for the real training. The shuffled-table test alone flatters the result, because it also breaks
  letter frequency. The scrambled-order control does not, and it still passes.

**1570: now clean for cc. 20r and 21r.** The solver's test was not clean. Mine is, because my digits were read before I saw
the table. Result: -10.452 against shuffled mean -15.147, best -13.197 (500 tables). I did not re-read cc. 3v, 4r, 11r, 22r
or 23r, and those transcriptions are still only at 1400 px.

## 4. Language, events, English, repairs

The Italian is real period language and fits May 1545, as far as general history goes. Solid independent ties:

- The docket on c. 16v is in the clear and reads "Del matrimonio con Ottavio", "Del p[ri]orato di Barletta" and "Il Car.
  d'Agosta desidera ... contra li protestanti".
- The cipher gives "priorato", "domar Luterani" and, as section 6 shows, "agorta desidera".
- The docket gap in NOTES.md, "Del [...] di Napoli", looks like "Del vicere di Napoli", to be confirmed on a clearer crop.
- The ordered strings hold. L01 gives e then d h i l m n o r s t u, and 10 of those 11 signs have values that do not depend
  on the string (L = n does). L11, L24 and v06 are vowel runs.

The English follows the Italian, but it inherits the wrong words listed in section 6.

**Unmarked repairs.** The reading header promises that repairs carry `[?word]`. About 19 cipher words differ from the raw
decryption and carry no mark: errare (raw erraq-e), fatto (hatto), visitata (luisitata), signor (sieno), ha (uina), sole
(soe), dato (datto), viene (oiene, though NOTES.md says K words are marked), desiderar, a, senza (raw za, one use of Gs),
essortar (essnortar), Luterani (luterapi), il s. (is), di (d), Farnese (farnes), hora (hra), imperadore (imperadoe), qui
(ooqui). Context-only values are marked for the code words, but not for the signs L, n, k and Gs, each with one use outside code words.

**Unproved nulls.** NOTES.md shows order in L01, L11, L24 and v06 only. It says the L01 tail, r04 and r07 are null by position
alone. L26, v12 and v20 are also called null strings and carry `<null>` in the reading, with no proof given. Five unordered
strings (L26, v12, v20, r04, r07; 48 letters, about 10 words) were left out of the denominator. v12 is the clearest problem, since "redeuto aer conto di cui
deve" looks like text ("aver conto di cui deve"), not a null string.

## 5. Word count under the 95% rule

The rule counts cipher tokens, so 89% is the wrong headline. It includes clear words.

| measure | 1565 cc. 15-16 |
|---|---|
| Solver: plain sense in cipher | 223 of 291 = 77% |
| Less about 19 unmarked repairs, plus about 10 words of unproved null strings | about 204 of about 301 = 68% |
| Whole letter, words in runs of 8+ between holes (mostly clear text) | 449 of 632 = 71%, a ceiling |

1570: my own chunk-by-chunk count gives about 102 of 132 transcribed words, so the claim is fair for what was transcribed.
But 132 is not the extent of the text. The second number line on c. 20r and about seven of the eight number lines on c. 21r
are missing, and c. 22v is unseen. That adds at least about 60 words, which gives about 100-105 of at least 190, or at most
about 55%. This is an estimate, since the full block has not been counted.

## 6. Corrections

These are from the scans and tokens, and are proposals until the solver checks them.

**v05, solver's transcription is wrong.** After g the scan has a small E (with raised 4) that the solver lacks, and there is
a 9 under the q. The line should run `g E p q _9 e r l F K`, which gives r i m o n i o. "matrmeonio" then becomes "matrimonio"
with no repair, and the reading's silent fix turns out right for a reason the solver did not have.

**r04-r05, words dropped.** Raw output is `{QUAN}agortadesideraqui{IMA}`. The reading has "{QUAN} [...] a desiderar qui", and
the English "to wish {IMA} here". With the docket's "Il Car. d'Agosta desidera", this should read about "{QUAN} [?d']Agosta
desidera qui {IMA}", with one clerk's slip (r for s). That makes Quan very likely the Cardinal, or Cardinal of Augsburg, at
L01, r05 and the closing line. Context only, so still doubtful.

**L20, wrong word.** Raw "frneseuinalacort". The reading has "vi ha la corte", translated "has the court for it". "vien a la
corte" keeps the signs and makes better sense: Farnese comes to court with words alone.

**v17-v18, probably wrong.** Raw "impresadiuerraquestoaoo". The reading has "impresa diverra questo [...]", translated "this
will come". Better: "impresa di [g]uerra questo a[nn]o", whether or not a war is undertaken this year. Both repairs are
unproved.

**v02-v03, clear text.** The reading prints "si tratta". The scan has "si trat" then a line start the solver gives as "ra".
Compare "trattara" at v24 and "si dara" in the same sentence. A future tense is likely.

**v11, clear word dropped.** The clear "mi" at the end of v11 is gone from the reading.

**1570, c. 21r and c. 20r.** My first-pass digits, decrypted with the table, are unrepaired except for 45/85:

- c. 20r: "[?per] non disturbare il carico che ... sarebbe stato il maggior danno d'interesse da ..."
- c. 21r: "... di Torre Maggiore mi ha fatto scrivere da Pompeo ... facci havere ... tratte di grano t'ho risposto con cerim. e
  che ... erano aperte le tratte ... porte di ferro ..."

The groups 109 and 18 2 are unexplained. Treat all of this as a lead for a proper pass, not as a reading.

NOTES.md says 1400 px is the most the server gives for a whole page. That is true but not a blocker: region requests return
native resolution, and `tiles.py` already does this for 1565.

## 7. Not tested

- The misfit of the 1556 and 1560 tables.
- The digit statistics on cc. 48 and 49r. README requires a matched synthetic control for a negative result, and "too short"
  has none.
- Line-by-line blind reading of c. 15r or of cc. 15v lines after v08.

## 8. Print

Two searches (Capilupi cipher letters to Ferrante Gonzaga 1545; Vittoria Gonzaga 1691 with Ruffo, San Paolo, Bisceglia) found
no edition of either. That does not clear them. The Chiesi essay remains unseen, and one calendar entry for "Camillo Capilupo,
Mantuan Envoy with the Emperor" could not be opened and has no year in the snippet. The 1570 entry had no earlier search.

Collision: origin/main is now 3c777efd5, not 9a126ccc0. A local look shows no target for these letters. `catalogue.json` has
no Capilupi, and the mention in `gonzaga1590` is a different man (Giulio). Recheck before any PR. The folder is untracked and
nothing is committed.
