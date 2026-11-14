# Siena, Concistoro 2308 fasc. 2, no. 8 (DECODE R4797): the Milan-Ferrara league slip, c. 1440-41, with its decipherment

Read at the time: the clear memorandum on the same sheet is the contemporary decipherment of the slip. Checked sign by
sign on 18 Oct 2026; the key rebuilt from the alignment reads all 166 cipher signs of the slip.

Part of the Concistoro 2308 collection index: [`research/siena2308/`](../../research/siena2308/README.md). Split out
of the former `targets/siena1421` entry on 18 Oct 2026 under the one-key rule.

## The disagreement, and how it was settled

- The project's inventory of 24 Sept 2026 (`targets/siena1421` NOTES) called no. 8 "read at the time": a ciphered slip
  pasted below its contemporary decipherment. That was a judgment from the contents; no sign was aligned.
- George Lasry's report of 17 Oct 2026 lists no. 8 as "c. 400 symbols — unsolved as of 17 October 2026 (no
  interlinear plaintext; a relation to the clear memorandum above the cipher is possible but speculative)"
  (`lasry_report.md`).
- 18 Oct 2026, this project: the slip transcribed sign by sign (`transcripts/no08.txt`, `no08.tok`) and aligned with
  the memorandum. The memorandum is written in paragraphs that open with an underlined catchword; the catchwords are
  the clear words of the ciphered text, and the words after each one decipher the cipher that follows it. Its fifth
  paragraph opens "Nel polizolo dicto segue" ("in the said slip there follows") and its last two catchwords, "Anchora
  disse" and "antiveduto questo", are the clear words of the slip (L3, L5). Aligned letter for letter, the slip's four
  cipher runs give the text of paragraphs 5-7, with one consistent key of 21 letter signs and two name signs
  (`decode.py`). The pattern words fix it beyond doubt: `5 9 T 9 5` = *aveva* (ABCBA), `F T W W 2 W 2` = *ferrara*,
  `L T Z PHI T L L Z` = *leonello*, and the same sign 7 is *d* in *dato*, *madonna*, *di*, *de*, *udirete*.
- So the project's statement stands, now verified, and George Lasry's "unsolved" is answered: the memorandum's last
  paragraph is the decipherment. George Lasry's count of c. 400 symbols is presumably the whole slip with its clear
  words; the cipher signs alone are 166.

## 20 Oct 2026: a second alignment, made independently

A parallel session (main branch, commit 883fa6f41, before this entry was merged in) fetched the image again with the
DECODE cookie and aligned the slip with the memorandum at 2x on the full-size photograph, without `transcripts/no08.txt`
or `decode.py`, in its own sign names (font look-alikes, not the names used above). Its three passages:

- slip l. 3-4, after the clear "Anchora d(iss)e": `÷ 59t95 75□ø I2 7øϕϕ2 9ff2ϕ +c5` = "[duca di Milano] aveva dato
  [ma]donna biancha" (*aveva* = 5 9 t 9 5, ABCBA; *dato* d = 7, a = 5, t = □, o = ø; *donna* 7 ø ϕ ϕ 2 with the same d
  and o and a doubled n), then `7t I2ɷ+ctɱt` = "de marchese";
- slip l. 2: `÷ tɷ I2ɷ+ctɱt 7ff o-tɷɷ2ɷ2 5 o-2|ot` = "[duca di Milano] el marchese di ferrara a fa|re" (*marchese*
  the same seven signs as in l. 4; *ferrara* f = o-, e = t, r = ɷ, a = 2);
- slip l. 5-6, after the clear "anti(ve)duto questo": `t ϕøϕ ff9ø I2ϕ+c2 ot +ct ...` = "e non può manchare che ...".

Its values (a = 5 or 2, c = +, h = c, d = 7, e = t, f = o-, n = ϕ, o = ø, r = ɷ, s = ɱ, t = □, v/b = 9) are the values
of the key above under other names (2 and 5 = a, 7 = d, T = e, W = r), and its three passages are runs 1, 3 and 4 of
the reading above: two alignments, made separately, give the same decipherment. It covered three passages, not the
166 signs.

The one doubt that session left, "la" and "manchare" both beginning with the sign it read I, is settled by the
reading above: the cipher has *madonna*, not the memorandum's *la donna*, so the sign is *m* in both words (and in
*marchese*), and there is no look-alike pair or encipherer's slip to explain.

## The sheet

- ASSi, Concistoro 2308, fasc. 2 "Lettere in cifra", pencil no. 8 (twice: on the memorandum and on the slip); DECODE
  R4797 (`Concistoro_2308_51`, 1 p., catalogued "1500-1599", no status). Image `IMG_R4797_I27940_P.jpg`.
- Upper two thirds: the memorandum, seven paragraphs. Paragraphs 1-4 decipher passages of a letter that is not on this
  sheet (the Duke of Milan, the Marquis of Ferrara "rimesso nel duca di Milano a fare guerra e pace", "di papa Felice",
  Niccolò Piccinino, "di buona voglia", Lucca); the last three ("Nel polizolo dicto segue ...", "Anchora disse ...", "antiveduto questo ...") decipher the slip.
- Lower third: the slip, six lines of clear cursive mixed with cipher. L1 is clear up to its last two signs.

## The reading

Memorandum, last three paragraphs (transcribed here 18 Oct 2026; underlined catchwords in italics):

> *Nel polizolo dicto segue*: [*modo?*] leggiere e capitagli e legha fral duca di Milano el marchese di Ferrara a fare
> guerra a Viniziani e sua legha. *Anchora disse* el duca di Milano aveva dato la donna Biancha a misser Leonello
> figlolo del marchese. *Antiveduto questo* e no puo manchare che questo udrete grandissimi facti.

The slip's cipher, deciphered with the rebuilt key (`python targets/siena8/decode.py`; spelling of the cipher):

1. (L1-L3) le|giere e chapitoli e legha fra [duca di Milano] el marchese di ferrara a fa|re
2. (L3) [guerra, faint clear] [Viniziani] e sua legha
3. (L3-L4) [duca di Milano] aveva dato madonna Biancha a missere Leonello filgliuolo de marchese
4. (L5-L6) e non puo manchare che questo udirete grandissimi fatti

Translation: "... to read the articles of the league between the Duke of Milan and the Marquis of Ferrara, to make war
on the Venetians and their league. He also said that the Duke of Milan had given Madonna Bianca to messer Leonello,
son of the Marquis. This foreseen, it cannot fail that you will hear of very great deeds."

Differences between cipher and memorandum: *chapitoli* / *capitagli*, *madonna* / *la donna*, *missere* / *misser*,
*filgliuolo de* / *figlolo del*, *non* / *no*, *udirete* / *udrete*, *fatti* / *facti*: spelling only.

## Dating (proposed)

The Marquis of Ferrara whose son is Leonello is Niccolò III d'Este (died 26 Dec 1441); "papa Felice" is the antipope
Felix V (elected Nov 1439); Bianca Maria Visconti married Francesco Sforza in Oct 1441, so the offer of her hand to
Leonello d'Este belongs before that. Between Nov 1439 and Oct 1441, most likely 1440-41. Not dated on the sheet.

## The key (rebuilt here from the decipherment)

Monoalphabetic with two signs for *a* (2, 5), one for *ss*/*s* (S), and two name signs: DM = *duca di Milano* (2x), VN
= *Viniziani* (1x). 9 serves for u, v and b (*aveva*, *Biancha*, *puo*). Full legend in `transcripts/no08.txt`, values
in `decode.py`. Not among the fasc. 1 keys compared by eye on 24 Sept 2026; the c. 1440 keys R4748 ("Cifra cum fratre
Bernardino") and R4749 name the same persons and were not compared sign by sign.

## Doubtful signs

- L3: a faint group after *fa|re*, lighter than the cipher, read as the clear word *guerra*; not counted as cipher.
- L3 *sua*: the S sign is followed by a small stroke, read as part of it.
- L4 *de marchese*: no *l* sign seen (the memorandum has *del*).
- L5 *puo*: the p sign there is a double stroke joined to a hook, counted as one sign.
- L6 *questo*: the q and u signs occur only here.
- L1 has "2 4 ffm(?)" in the clear text, read as an abbreviation, not counted.

## Verification v8, 23 Oct 2026

The translation wave flagged `texts/no08_reading.md` at 0.50: the two resolved name signs were written lower-case
(`[duca di Milano]`, counted as holes) and the run-edge `…` marks (clear text, not unread cipher) were counted too. With
the name signs capitalised and the marks dropped: **1.0** on explicit holes (4/4), 0.25 plain (1440 Sienese spelling),
hole rate 0. **A reading of fragments; keeps read** (grade A): each cipher run is a clause that holds, and every word is
confirmed letter for letter by the contemporary memorandum. Not 'not prose' (the runs are running sentences) and not
decoded-only (no hole).

## Independent verification by Brice Dudout (PR #565, 14 Nov 2026)

Brice Dudout (PR #565, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded `transcripts/no08.tok` from `key.json`
alone: 166 signs, 23 distinct, the four runs identical to `texts/no08_decryption.txt`. No key correction. Re-run here: same result;
the read share 1.0 stands. The DECODE image was not fetched.

## Remaining gaps

- the cipher behind paragraphs 1-4 of the memorandum - blocker: needs-physical-access; that cipher is in a covering letter not on this sheet and not among the DECODE photographs; its decipherment is on the memorandum.

## Escalation

- [x] siblings: every record of the busta opened (R4746-R4814, R1858); the covering letter is not among them.
- [x] clear-pages: the memorandum on the same sheet is the decipherment; aligned sign by sign.
- [n/a] known-keys: the decipherment gives the key; R4748/R4749 (c. 1440) could be compared to identify it but that would not change the reading.
- [n/a] print: not needed for the reading; no printed edition of the slip known.
- [x] key-rebuild: 21 letter signs and 2 name signs rebuilt from the alignment.
- [x] retry: the rebuilt key applied to the whole slip (`decode.py`): all four runs read.
- [x] retry (23 Oct 2026, v8): reading rescored with the name signs capitalised (1.0 explicit holes); keeps read

## Questions for George Lasry

- Does the alignment convince him (the four runs printed by `decode.py`, the pattern words above)?
- Is a key with these signs (the cross-topped b for *e*, the crossed 2 for *o*, the joined rings for *l*) among the
  c. 1440 keys he has seen (R4748, R4749)?
