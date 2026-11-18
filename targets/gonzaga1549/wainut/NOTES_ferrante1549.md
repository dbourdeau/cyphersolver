> Folded into `targets/gonzaga1549/` on 14 Nov 2026 (owner's decision on issue #618; one key, one entry). This file is WAINUT's NOTES.md of `targets/ferrante1549/` as it stood, with the sections the project added on 14 Nov; paths in it are relative to this folder (`wainut/`), and `targets/gonzaga1549/` is now the parent folder. Current state, gaps and escalation: `../NOTES.md`.

# Ferrante Gonzaga 1549: letters of Charles V (catalogue 1560) and Prince Philip (catalogue 1561), Biblioteca Estense, Autografoteca Campori

Status: in progress. Not yet written up: no site page or README row. Read in part, or not read, with escalation steps still open (see its status below, Remaining gaps and Escalation). The status below is the contributor's.

Status, 3 Nov 2026: read in part. One long break, Charles V of 14 Nov 1549 (cc. 60r-62r): 811 of 910 words verbatim from the signs, 864 with marked repairs. No document of either entry is read in full. Prior art is open: see below. Nothing here is claimed as new.

Catalogue 1560 and 1561 are one target because the letters use one key. Contributed by WAINUT. The work was done with AI language-model agents. Reading was done sign first: shapes were copied, then decoded, and only then checked for sense. Separate agents made the blind passes and the independent check named below.

## Status per document

Breaks (no contemporary decipherment):

| document | status | words | verbatim | with repairs | proposals, holes | transcription |
|---|---|---|---|---|---|---|
| Charles 14 Nov 1549, cc. 60r-62r | **read in part** | 910 | 811 (89.1%) | 864 (94.9%) | 43, 3 | see "Blind checks" |
| Philip 4 Aug 1548, c. 10r | **read in part** | 80 | 75 (93.8%) | 78 (97.5%) | 2, 0 | one pass; a half-scale check differs on 20.3% of signs |
| Philip 24 Nov 1551, c. 28r, D and E | **read in part** | 66 | 56 (84.8%) | 62 (93.9%) | 4, 0 | one pass, no second reader |
| Philip 24 Nov 1551, c. 26r | **read in part** | 91 | 75 (82.4%) | 82 (90.1%) | 8, 1 | one pass, no second reader; vicariate passage unsafe |
| Philip 25 Jun 1546, cc. 5r-5v | **decoded, not read** | none claimed | | | | one rough blind pass |
| Philip 14 Mar 1553, cc. 35-40 | **decoded, not read** | none claimed | | | | one rough blind pass |
| Philip, catalogued 16 Jun 1563, cc. 24-25 | **decoded, not read** | none claimed | | | | one rough blind pass, bleed-through, group C unreliable |

Counts come from `scripts/check_marks.py`, which aligns each reading with its decryption letter by letter and fails if a departure from the signs is left unmarked. "Verbatim" means the letters the signs give. "With repairs" adds the words marked `°`, where the sense is firm but letters differ; the repairs are listed in `editorial_ch1549_1114.md` and `editorial_philip_1548_1551.md`. A `[...]` counts as one word and may hide more. Some verbatim words rest on values taken from this same letter (`m`, `R^`, the `nov14` rows of `key.tsv`). c. 10r stays read in part: the verbatim share is under 95%, and it has one primary pass with a high disagreement rate. On 14 Nov the rule is missed even with the repairs, by one word.

Transcription jobs (a contemporary decipherment covers them; not breaks):

| document | what covers it | transcription |
|---|---|---|
| Philip 8 Mar 1549, c. 12r | c. 14r | two passes |
| Philip 23 May 1547, cc. 9r-9v | cc. 11r-11v | one pass |
| Philip 24 Nov 1551, c. 28r, C | marginal decipherment | one pass |
| Charles 13 May 1549, c. 30r | c. 29r | one pass |
| Charles 30 Sep 1549, all cipher | six marginal decipherments | one blind pass, not yet an edition; `reading_ch1549_0930_1120.md` |
| Charles 20 Nov 1549, all cipher | marginal decipherments, including c. 64v | one blind pass, not yet an edition; same file; the test on it fails on runs of 4+ |

Not started: Charles 15 Jul and 23 Dec 1549, 1 Jul 1552, 11 Aug 1542 (looks like a different sign set on a contact sheet, not tested). cc. 131-132 were not located. (14 Nov 2026: cc. 131-132 are `targets/renard1549/`, 11 Aug 1542 is `targets/gonzaga1542/`, 23 Dec and 15 Jul 1549 are described in `targets/gonzaga1549/`; two more Philip letters, cc. 15-17 and cc. 32-34, are not started. See the section of 14 Nov 2026 below.)

Corrections to the catalogue:

- Marginal decipherments exist for c. 28r and c. 64v. The entries list these letters as undeciphered. The 30 Sep and 20 Nov letters are covered in full, so of the five Charles letters called undeciphered, these two are transcription jobs. 14 Nov is the real break.
- c. 14r begins "De Su Mt.", not "De su Al.".
- c. 12r has about 230 signs, against about 428 letters on c. 14r. The copy is not abridged.
- The letter catalogued 16 Jun 1563 cannot be 1563. It opens "El Principe" and is addressed to Ferrante, who died in 1557. Philip stopped being prince in January 1556. The pencil note on the leaf has a question mark. Its clear text speaks of letters of 21 March and 13 April, of Piedmont, and of a report by the Duke of Alba. That suggests the early 1550s; the year is not shown.

## The system

A syllabary with homophones and a small code. It has word-like tokens but no word division.

A consonant base takes a vowel mark: one dot a, bar e, two dots i, raised o o, raised s u. So base `T` gives ta, te, ti, to. Bare signs give single letters, with homophones. Dots written under a sign cancel it. Code words are disguised as ordinary words: `dide` Su Magestad, `quod` Embaxador, `gaces` Rey de Francia, `em` franceses, `gien` vuestra, `mus` para, and on 14 Nov `Pollo`, `vela`, `inta`, `nep`.

`key.tsv` is the working table, 160 rows; sign names are mine. Each row says whether the value is frozen, later, changed, or doubtful. `key_frozen_1547.tsv` is the frozen table. Context-only values: `Pollo` Papa (holds at every occurrence on 14 Nov, no contemporary text), and, doubtful, `vela` Roma, `inta` la Yglesia, `nep` Francia. Doubtful for two values: `9` (d, and u in ciudad, usar), `c` (rr, and c in occasion, acordio, sucesso). `D3` is du (duque, many) but do on c. 28r (Mirandola). Values changed for Charles 1549 after the freeze: `8` c, `D3` du, `o:` ri, `x+` pre.

Added 3 Nov: `m` b (2, both sobre), `R^` gra (1), and, doubtful and from one occurrence each, `3+:` zi, `os2` gu, `7T` su. `&` has no value. `os3` and `xs` were dropped: at zoom they are `g+` (creer, B25) and `ys.` (nueuo, C29). `J^` went with the D27 correction. `b_` (value ua) was renamed `bu`, because a trailing `_` means cancelled. `8'` occurs once, at the end of c. 12r L02, and looks like `Q` there; it is not `8s`. `xp` has only C04, and its hook differs from `xu`, so "fruto" is a proposal. `v` (do) stands for bare d in santidad, opportunidad, ciudad, podria, aduertencia, qualidad; these are marked as repairs. On the image `9` and the sign in ciudad and usar cannot be separated by shape.

The 1556 key was not run. It is a letter table with numbers, and it has no way to express these syllable signs.

## How the key was obtained

1. Philip 8 Mar 1549: c. 12r transcribed twice. The passes differ on 20 of 235 signs. Pass 2 was not blind, and I cannot show pass 1 came before the table, so the two are dependent.
2. Table derived by aligning against c. 14r.
3. Extended with 9r and 9v lines 1-10, then frozen (`key_frozen_1547.tsv`). 1547 and 1549 are the same table.
4. Extended on 14 Nov by the iteration in CONTRIBUTING: decode, find where the sense breaks, go back to the image.

Method for the profile: key recovered from adjacent plaintext.

## Held-out tests

| test | letters in order shared with clear | letters in runs of 4+ | 200 shuffled tables (max) |
|---|---|---|---|
| 1547, 9v lines 11-16, frozen table, not blind | 0.888 | 0.857 | 0.418 / 0.239 |
| Charles 13 May 1549, frozen table, not blind | 0.978 | 0.932 | 0.431 / 0.374 |
| **30 Sep 1549, 408 signs, blind reader, frozen table** | **0.728** | **0.595** | 0.420 / 0.532 |
| **20 Nov 1549, 140 signs, blind reader, frozen table** | **0.652** | 0.323 | 0.519 / 0.355 |

The bold rows are the honest test, rerun with `scripts/score_blind.py key_frozen_1547.tsv`. The reader had no table, no clear text and no sense in view, and copied shapes from crops cut to leave out the margins, though stray margin letters show at the edges. The table never saw these letters. Sign names were mapped to mine automatically, from the alignment of 14 Nov; removing the hand-added part of that map gives 0.726/0.596 and 0.640/0.289, so it did not create the result. On 30 Sep the result beats every shuffled table on both measures. On 20 Nov it beats them on order, but fails on runs of 4+.

These tests show the table works on other letters with a noisy blind reader. They do not measure the reading of 14 Nov.

## Blind checks of the readings

- 14 Nov, A08-D23: a separate reader with no table made `transcription_kn14_pass2.txt`. 2,132 aligned signs, 80.8% the same after mapping names. The differences were not all settled.
- 14 Nov, D14-E03: an independent verifier read 425 signs from full-resolution crops before opening the transcription. **Raw differences 39 of 425, 9.2%**; 7.1% after naming equivalents. That reader had `key.tsv` open, so this is blind to the transcription but not to the table: a strong second reader, not a shape-only reader. D24-F04 therefore has a reader with the table in view, not a shape-blind one.
- 4 Aug 1548, c. 10r, half-scale strips, same verifier: **43 of 212 signs differ, 20.3%**.
- With 30 shuffled frozen tables, pass 2 finds 2 of 255 words of 6+ letters on average, against 52 with the frozen table. So the sense is not expectation. But pass 1 alone carries the 14 Nov count: pass 2 with the full key finds 37% of the long words of the reading verbatim, pass 1 83%.
- A00-A07 have one pass only. D24-D27 have only partial blind support from group T of the blind file.
- Blind reads of 200 signs were not done for 30 Sep, 20 Nov, Philip 1546, 1553, "1563", c. 26r, c. 28r. Their status rests on rerunning files, not on the image.

Corrected at zoom after that check, each on the image:

| line | was | now | effect |
|---|---|---|---|
| B25 | `os3` | `g+` | creer |
| C19 | `X l+ Q X X y+s`, `3:` | `X l^ Q x X y+s`, `3^` | "en lo demas no deueys en ninguna manera": the negative is on the page |
| C29 | `xs` | `ys.` | nueuo |
| D15 | `a+ x a+ J_` | `a+ X a+ J:` | "o de otra" |
| D16 | `l: Q g^ E g^ 8: a+ as L^ - 5` | `l^ 3+ g^ E g^ 8: a+ 5 as J: - 5` | "manera Horacio entrasse" |
| D19 | `v` | `v^` | obseruada, agreeing with tregua |
| D21 | `y:` | `7:` | tambien, no repair |
| D27 | `l^ Q g:`, `cp 5_ Q J^` | `l^ 3+ g^`, `xu 5 Q J:` | "de manera que", "nuestra" |
| E02 | `Z+`, `v`, ends `Lb` | `x+`, `v^`, ends `Lb n` | "emprenda", "contra ella" |
| F04 | `n as J g+` | `n a+ fh g+` | ofrecer |

Where I differ from the verifier, on the image:

- F04: the verifier left the sign before `g+` open. It is `fh`, the same as C22, so "ofrecer" needs no repair.
- D21: the verifier wrote that "tambien" needs a repair of `y:`. The sign is thin and straight like `7:` at B26, and the verifier's own blind line has `7:`. No repair.
- E02: the verifier's note gives `Tp`; the sign has flat bars and is `Jo`, as in that reader's blind line. "[?inoue]" stays a proposal either way.

The verifier counted 76 firm words with an unmarked departure, 773 of 908 verbatim. All are now handled: 53 words are marked `°`; the rest went verbatim through the sign corrections above, the new key values, or by keeping the spelling of the signs (dissymulacion, ueemos, remictimos, dubdando, debra). The word total moved from 908 to 910 because six holes became words.

`dissymulacion` is 8 signs, `v: - Y lp 6^ 8: a+ as`. The two readers agree on all 8. Seven are frozen. `lp` = mu is later, but it also gives "muriendo" at B13.

## Reading of 14 Nov 1549

`reading_ch1549_1114.md` (Spanish), `translation_ch1549_1114.md` (English), `editorial_ch1549_1114.md` (word count, every repair, notes, contents, context).

Charles forbids Ferrante's plan to conclude terms with Ottavio Farnese over Parma. "Capitular" here means to conclude terms, and the signs at A01-A02 make it Ferrante's own determination, not an offer by Ottavio. A private settlement between the two is approved. The authority Ferrante gets is conditional on two cases: Camillo Orsini plays a trick and Parma is evidently out of the Church's hands; or Orazio or another enters Parma by a deal with France or otherwise. In the second case he is to try to make himself master of the city with dexterity and dissimulation. The letter's last word is that nothing else is to be started. It still treats Paul III's death as a future event, though he had died four days earlier; the clear text of c. 64r shows the news reached Brussels about 18 Nov. The clear text of the letter covers none of this.

## Other letters

- 23 May 1547: after the death of Francis I, on Ferrante's visit to the Piedmont frontier; Siena's refusal of the garrison; the exchange of Piacenza, not named in the cipher.
- 4 Aug 1548: Genoa; Henry II's descent into Italy. `reading_1548_c10r.md`.
- 8 Mar 1549, Heidelberg: the Emperor orders Philip to write to Figueroa on Genoa; Ferrante is asked to act with temperance.
- 13 May 1549: Ferrante is to work out secretly where money and materials for "la obra" can come from, with no sign of the intention. That the work is a fortress at Siena is a proposal.
- 30 Sep and 20 Nov 1549: `reading_ch1549_0930_1120.md`.
- 24 Nov 1551: `reading_1551_c28r.md`, `reading_1551_c26r.md`. Parma war, Nice, Siena, the bishop of Arras, Don Diego de Mendoza.
- 25 Jun 1546, Madrid: the clear text congratulates Ferrante on his election to the place of the Marquis del Vasto. The blind decoding has runs such as `delartill..ri`, `conintencion`, `lleuar`, and `Su Magestad`.
- 14 Mar 1553, Madrid, about 70 lines: `Su Magestad` recurs. c. 36 is a contemporary Italian summary of topics: Don Antonio de Bivero and the needs there, light horse, costs, what the French have taken, Siena, the men lacking in the Spanish infantry, pikes and powder, the monthly pay, the men-at-arms of the Kingdom. That list is a crib for the next pass.
- Catalogued 1563: `Embaxador figu..` decodes at C-03. The second half of the blind pass is unreliable.

No sense should be drawn from the three decoded letters yet.

## Prior art (3 Nov 2026)

Repo at 8b48b6cdd: no target folder for these letters. `charles1536`, `philip1574`, `gonzaga1590` are other letters.

Opened: Calendar of State Papers, Spain, IX, Nov 1549, pp. 465-481; Calendar of State Papers, Venice, V, Nov 1549; Treccani, Dizionario Biografico degli Italiani, "Gonzaga, Ferrante". None prints this letter or this authorisation. The DBI records Gonzaga's Siena exchange proposal of Nov 1549 and earlier instructions for a surprise "dopo la morte di Paolo III", so the idea of seizing Parma is known, and Gonzaga's threat to Parma is common knowledge. Do not read the dissimulation clause as unknown.

Not opened: Corpus documental de Carlos V, ed. Fernández Álvarez, vol. III (1548-1554; catalogue records only, no full text found); Pastor vol. XII; Robertson; Rodríguez-Salgado; Brandi; Motta; Gosellini; Solmi; Druffel; the Simancas minutes (Estado 1196 is the lead). Whether the 14 Nov letter or its minute is printed is **unknown**. If it is, it is a crib, and the reading becomes a check against it.

Related: *Documenti ispano-genovesi dell'Archivio di Simancas* (1868) lists a cipher letter of the prince to Figueroa of 8 Mar 1549 (https://digi.econbiz.de/viewer/image/176352146X/20/).

## Images

Lodovico Media Library (CC BY-NC-SA), `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`. Links only, no scans in this folder. Source regions over about 1 megapixel return 422. `scripts/fullpage.py` fetches a whole page in tiles, one request a second, with the User-Agent WAINUT-research.

Philip: 8 Mar 1549 `fa08c81b-4cf3-4914-878e-98059ad124b8`; 23 May 1547 `9c67dac4-f213-4484-9e5e-fb5c1408ea76`; 4 Aug 1548 `96578a9c-2963-4448-8786-5fa35a3c44e7`; 24 Nov 1551 `3f4f51da-b3b0-4159-9824-f22958c248dd` (c. 26) and `9ad3b749-cbac-4adc-94cd-b080227c220f` (c. 28); 25 Jun 1546 `68f59b4c-c5e3-431f-9226-00927538c698`; 14 Mar 1553 `6990ecfe-8ee7-4994-b2d6-3ccc332ee9e2`; catalogued 16 Jun 1563 `499ee545-fcd1-4afe-9776-a21cdbf0efb4`.

Charles: 13 May 1549 `0dbb01cc-7d7a-4aac-b3a8-0b6713c56416`; 14 Nov 1549 `bf3cf88e-72bf-4608-8e75-a0390e17284b`; 20 Nov 1549 `2c329985-47ac-4687-8356-ee2a90f24b0f`; 30 Sep 1549 `656346d0-d012-4621-9973-fca518e5126e`; 11 Aug 1542 `c710a32c-42a7-4159-8abc-472aed58f7c9`; 15 Jul 1549 `9b292209-d8f4-4d64-b714-dd50af780c54`; 1 Jul 1552 `006d60a7-5e7e-4c4b-bbbc-68760577ce88`; 23 Dec 1549 `d824fd53-2d20-4daf-b854-7b654a8d0248`.

## Files

`transcription_*`, `decryption_*`, `reading_*`, `translation_*`, one set per document; `editorial_*`, the notes to the readings; `clear_*`, the contemporary decipherments as I read them; `key.tsv`, `key_frozen_1547.tsv`. Scripts: `python scripts/decrypt.py` rebuilds every decryption; `python scripts/check_marks.py <doc> [--table]` checks and counts a reading; `python scripts/score_blind.py key_frozen_1547.tsv` runs the blind tests; `scripts/score.py` runs the tests against the clear; `scripts/fullpage.py` fetches pages.

The two blind decryption files are unrepaired decodings of a rough shape pass and keep that reader's errors.

## Session of 6 Nov 2026 (no status change)

Catalogue 1561 was reopened with the aim of reaching the read bar. Nothing moved. c. 10r lines A1-A4, B1-B2, B4-B5 and c. 28r D1-D4 were viewed again at 0.55-0.62 scale (tiled IIIF crops, left and right halves). On c. 10r every line compared with `transcription_1548_c10r.txt` agrees to the eye; that look came after the transcription, so it is not an independent pass and does not lift the status. A fresh sign-by-sign pass of the 1546 letter (cc. 5r-5v, about 23 cipher lines of about 28 signs) was started and stopped after line 1: several signs there are not in `key.tsv` (a barred pi-like sign, a cross with a loop), and the blind pass names do not map to them. The unread letters (1546, 1553, "1563") still need a named sign set built on the images before any decryption is worth reading.

## 14 Nov 2026: issue #615 (Brice Dudout), cc. 131-132, letters held elsewhere, two more Philip letters

Four points from Brice Dudout's own work on the Campori letters, each checked here against the repository or the
Lodovico images (plain requests, no bot check, one every two seconds).

1. **cc. 131-132 are located and have their own target.** Karl V, sfasc. IV, cc. 131-132 is Lodovico record
   e7e65c38-4c54-48b1-8003-6da1c5c2ba1b: `targets/renard1549/` (Ivan Sourvillo, issue #373, read in part, 10 Nov 2026;
   the imperial ambassador in France to Charles V, a copy sent to Ferrante). Its notes say c. 132 is blank or address
   only; Brice Dudout has 132r blank and 132v without an address. Another key: not part of this target.
2. **Three "not started" letters are worked in other folders.** 11 Aug 1542 (cc. 109-110) is `targets/gonzaga1542/`
   (Prabal Gupta, issue #318; a consonant sign with a vowel digit above, another cipher). Charles 23 Dec 1549
   (cc. 76-78, with its decipherment on c. 77) and 15 Jul 1549 (cc. 40-42, a numeric cipher with its decipherment on
   c. 41) are in `targets/gonzaga1549/` (23 Dec read there against c. 77, 15 Jul described), which also holds this project's own reading of the
   14 Nov 1549 letter and of the 13 May, 30 Sep and 20 Nov passages: the same letters and the same cipher as the
   Charles letters of this folder. The two tables (`key.tsv` here, the sign table of `targets/gonzaga1549/`)
   have not been compared value by value; that comparison, and the one-key question, are taken up under issue #618.
   1 Jul 1552 (sfasc. I cc. 81-84) is described there as another sign set with a decipherment on cc. 82-83; not started
   anywhere.
3. **Two Philip letters that the list above does not have.** Both records exist and were opened here:
   - Felipe II, sfasc. I, **cc. 15-17**, record 50aa71f4-d965-41be-a5b9-b9bd4c31efb3 (18 Mar 1549 by his dating;
     the date line was not looked for here). c. 15r: "El Principe", four clear lines, then ten lines of cipher in
     this target's sign set (`dide`, `quod`, `tac` are written as on the other letters), then clear. c. 17r is a clear
     slip of eight lines in another hand, "lo que despues ay que dezir es que oy ha llegado correo del emperador mi
     señor con los despachos … sobre de la empresa contra Dergut arraez, en lo qual Su Magestad avisa al Ambaxador
     Figueroa …": by its form the decipherment of the cipher of c. 15r, as c. 14r is for c. 12r ten days earlier.
     He holds a frozen transcription of 242 tokens (not sent). A third cipher and clear pair for the key, and,
     if kept out of the key, a second held-out test.
   - Felipe II, sfasc. I, **cc. 32-34**, record 897e61b7-4957-4f07-b4d2-debae54659a1. c. 34r ends "De Monçon a vj de
     octubre 1552", signed "Yo el Principe". Cipher on c. 32r (three passages, about twelve lines) and c. 34r (eleven
     lines), same sign set; cc. 32v-33v not opened here. No decipherment seen on the two pages opened. He counts
     about 50 lines, cipher only. A break candidate longer than c. 10r, c. 26r or c. 28r.
4. He agrees that the letter catalogued 16 Jun 1563 is in the same table (his earlier sorting by eye had put it
   under another cipher). No new evidence; the letter stays "decoded, not read".

Neither new letter is transcribed here. They are added to the gaps and to the escalation list.

## 14 Nov 2026: issue #618 (Brice Dudout), the Simancas sheet of 1866 and this target's code words

The sheet is described in `targets/gonzaga1549/NOTES.md` (section of the same date): AGS, Biblioteca, D/00203 no. 243, a
reconstruction made at Simancas in 1866 from deciphered letters of 1545, not a table of the period; public PDF,
reproduction prohibited. Read here from the PDF and set against `key.tsv`:

| `key.tsv` | status there | sheet of 1866 | result |
|---|---|---|---|
| dide Su Magestad | frozen | Su Magestad dide | same |
| quod Embaxador | frozen | Embajador quod | same |
| gien vuestra | frozen | Vuestra gien | same |
| em franceses | frozen | Franceses em | same |
| gaces Rey de Francia | frozen | Rey de Francia gacez | same |
| mus para | frozen | para mus | same |
| Pollo [Papa] | context, firm | Papa pollo | same |
| inta [?la Yglesia] | context, doubtful | Su Santidad inta (Iglesia is sor) | corrected to Su Santidad |
| nep [?Francia] | context, doubtful | Francia nec, with an end mark | sense confirmed; the letters want a look at the image |
| vela [?Roma] | context, doubtful | not on the sheet | open |

Six of six frozen code values, which came from the contemporary decipherments of Philip's letters, agree with a list
drawn in 1866 from other letters: the two are independent, so this is a check of both. The hole at A16 (`et ud y tu`)
is not cured: the sheet has "Embajador de Inglaterra et ud" and "lea tu", and its nulls note names `et`; none gives
sense there.

Brice Dudout reran `scripts/check_marks.py` on a copy of the 14 Nov reading with inta = Su Santidad, nec/nep = Francia,
pollo = Papa and et = null and reports 867 of 908 words (95.5%) against 864 of 910 (94.9%) "with repairs". That figure
is his and his file was not sent. By the strict rule of this project (sure words only; a marked repair is not a read
word) the letter stands at 811 of 910 verbatim (89.1%), and at most six words move, so it stays read in part.
`key.tsv` and the reading are not changed in this round.

**The same letters are in `targets/gonzaga1549/`** (the project's own reading of 3 Nov 2026, on the site): Charles V
of 14 Nov 1549 and the passages of 13 May, 30 Sep and 20 Nov. The two were made apart, from separate transcriptions and
separate tables, and neither cited the other. That makes a second reading of one letter, to be compared line by line,
and one key in two folders. The recommendation to the owner is in the round's report (R14_ib.md); nothing is merged here.

## Remaining gaps

- 14 Nov, code words: inta is Su Santidad and nep is Francia by the Simancas sheet of 1866 (issue #618); not yet written into `key.tsv` and the reading; a line-by-line comparison with the reading in `targets/gonzaga1549/` is not done - blocker: not-attempted; waits for the decision on one entry for this key.
- 14 Nov, three holes (A03 `5 a a`, A14 `lalgunte`, A16 `et ud y tu`) and 43 proposals, among them `[?inoue]` (E02) and the words touched by `9`, `c`, `vela`, `inta`, `nep` - blocker: open-codes; no key sheet found, context alone does not settle them.
- 14 Nov, sign differences of pass 2 (19.2% of A08-D23) not all settled; A00-A07 one pass - blocker: not-attempted; a zoom reading of A00-D13 would likely cure more of the 53 repairs.
- c. 10r, c. 26r, c. 28r: one primary pass each; the vicariate passage on c. 26r needs a second pass before anyone relies on it - blocker: not-attempted; budget.
- Philip 1546, 1553, "1563": need a proper pass in a named sign set - blocker: not-attempted; budget.
- 30 Sep and 20 Nov: not yet editions; they need the line-by-line pass given to 14 Nov - blocker: not-attempted; budget.
- Charles 15 Jul, 23 Dec 1549, 1 Jul 1552: not started here (23 Dec and 15 Jul are described in `targets/gonzaga1549/`); 11 Aug 1542 and cc. 131-132 are other ciphers with their own targets (`gonzaga1542`, `renard1549`); catalogue 1563 (Juan Manrique 1554, Brezeno 1548) not tested - blocker: not-attempted; budget.
- Philip, sfasc. I cc. 15-17 (cipher c. 15r, clear slip c. 17r; 18 Mar 1549 by Brice Dudout's dating) and cc. 32-34 (Monzón, 6 Oct 1552, cipher on cc. 32r and 34r, no decipherment seen): not transcribed (issue #615) - blocker: not-attempted; the first is a third pair for the key or a second held-out test, the second a break of about 50 lines.
- Prior art: Corpus documental vol. III, Druffel and the Simancas minutes, before anyone calls any of this new - blocker: needs-physical-access; no full text found online.

## Escalation

- [ ] siblings, 14 Nov 2026 (issue #615, Brice Dudout): two Philip letters were not in the list, sfasc. I cc. 15-17 (cipher with a clear slip) and cc. 32-34 (6 Oct 1552, cipher only); both opened, neither transcribed. The other Felipe II records of the search (39 in all) have not been opened one by one for more cipher
- [x] siblings: all listed letters of both entries were fetched; the key was built on the siblings with a decipherment (c. 12r, cc. 9r-9v) and tested on c. 30r, 30 Sep and 20 Nov
- [x] clear-pages: clear pages checked; marginal decipherments found on c. 28r and c. 64v that the catalogue does not list
- [x] known-keys (6 Nov 2026): the repo keys were checked for a same-family key. `mendoza1548/key_1548.md` is the same Spanish chancery syllabary (Bucuré 2025, reconstructed from Neapolitan letters of 1547; Bertomeu Masiá 2009 places it in the correspondence of Granvela, Mendoza and Ferrante Gonzaga). Two code groups agree with `key.tsv`: `dide` = Su Majestad, and `nego:` = franceses, against our `em` franceses and doubtful `nep` Francia. Not done: a value-by-value comparison of the two tables, which could settle the doubtful `9`, `c`, `vela`, `inta`, `nep`, and Bucuré 2025 and Masiá 2009 themselves, which are not opened. The 1556 key cannot express these signs; `charles1536` is a different syllable system; `philip1574` and `gonzaga1590` are other letters. `gonzaga1549/` holds separate work on catalogue 1560 (its own tables of 13 May, 14 Nov, 20 Nov 1549).
- [ ] known-keys, 14 Nov 2026 (issue #618): the Simancas reconstruction of 1866 (AGS D/00203 no. 243) agrees with the six frozen code words and Pollo, and corrects inta; its syllable rows not compared with `key.tsv`; `targets/gonzaga1549/sign_table.tsv` not compared either
- [ ] print: CSP Spain IX, CSP Venice V and the DBI opened; Corpus documental III, Druffel and the Simancas minutes not
- [x] key-rebuild: table extended on 14 Nov from what reads, by context and on the images; each value marked
- [ ] retry: done for the lines listed under "Blind checks of the readings"; not yet for A00-D13 as a whole
