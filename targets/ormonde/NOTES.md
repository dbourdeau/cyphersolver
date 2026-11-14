# Ormonde–Maltravers Cipher (1634–1635) — NOTES

**Verdict: SOLVED (alphabet recovered; every spelled word read; the nomenclator confirmed against Wentworth's own
dispatches in Knowler's *Strafforde's Letters*, 1739 — seven of nine codes fixed, two person-codes in one clause
(185, 149) still unidentified).**

Target: S. Tomokiyo, *Unsolved Historical Ciphers* → "Ormonde-Maltravers Cipher (1634-1635)"
(https://cryptiana.web.fc2.com/code/unsolved.htm).

Two sessions on 2026-09-15: alphabet and first reading; then the nomenclator checked against Knowler (§4a).

## 1. Sources

| Source | What it gives | Where |
|---|---|---|
| HMC, *Calendar of the manuscripts of the Marquess of Ormonde, K.P., preserved at Kilkenny Castle*, vol. I (1895), pp. 28–29 | The two letters (Maltravers → Ormond, 13 Sept 1634 Dorking; 22 Jan 1634/5 Whitehall), cipher figures printed in the text | IA `calmarqormonde01greauoft`; OCR in [ormonde1_djvu.txt](ormonde1_djvu.txt) lines 2101–2156; page scans [p28.jpg](p28.jpg), [p29.jpg](p29.jpg) (IA `page/n43`, `page/n44`) |
| Same volume, index "Cypher, letters in. 28, 75, 118, 209, 214" | Other cipher letters in the volume: p.75 Sir Edward Nicholas → Ormond 18 Apr 1644 (with interlinear decipher, a *different* key, figures 4–211); pp.209–214 letters of the 1650s (another key, figures up to 523). **Nothing else from 1634–36, no key, no decipherment of the Maltravers letters.** | [cipher_runs.txt](cipher_runs.txt) (output of [find_cipher_runs.py](find_cipher_runs.py)) |
| HMC Ormonde New Series vols. 1–3 (1902–04; bundled in the same IA djvu file) | No Maltravers letters, no 1630s cipher | grep of the same file |
| **W. Knowler (ed.), *The Earl of Strafforde's Letters and Dispatches*, vol. I (1739)** | Wentworth's own account of every event the cipher passages refer to: Kildare's flight and the King's refusal to see him (p. 309); the dispatch praising Ormonde's conduct in the Lords and moving that he be sworn a Councillor "in exchange" for Crosby, with Coke's marginal answer that the warrant is enclosed (pp. 352–3); Crosby in England, Jan 1635 | IA `bim_eighteenth-century_the-earl-of-straffordes_strafford-thomas-wentwo_1739_1`; excerpts in [knowler_excerpts.txt](knowler_excerpts.txt) |
| Tomokiyo, "Ciphers in Early Stuart England before the Civil War" (strafford.htm) | Wentworth–Charles I, Wentworth–Laud (nulls < 30, codes 85–202), Wentworth–Windebank ciphers (images only); Scudamore 1636 and Cave 1638 ciphers "assign three (or six) figures to each letter in regular arrangement"; Ormonde–Clanricarde 1643 also regular. None is the Maltravers key (different null/code ranges), but they show the *type*: regular alphabet blocks + nulls + numbered nomenclator. | fetched 2026-09-15 |
| Wedgwood, *Thomas Wentworth* (1961) p.159; Wikipedia "James Butler, 1st Duke of Ormond" | "In January 1635 Ormonde was sworn of the Council" — confirms the reading of letter 2 | — |

The printed figures were checked against the page scans: **every figure below is exactly as printed** (in particular
"26" in the first run is printed, not an OCR slip).

## 2. Ciphertext (as printed; full letters in [ciphertext.txt](ciphertext.txt))

Letter 1, 13 Sept 1634:
> My lord of Kildare is long ago in England though I have not seen him, it is said he came over because he was
> **65, 35, 21, 26, 59, 98, 113, 186, 108, 143,** refused to see him because he brought no
> **28, 69, 49, 50, 70, 44, 89,** from **186, 99.**

Letter 2, 22 Jan 1634/5:
> You desire to know what **93, 185, 95,** hath written unto **99, 149,** concerning **98, 10, 44, 79, 47, 8, 59,** for whom
> **270** thus hereafter of which I can give you no account of at all, only by what I hear it is like to go worser with
> him, rather than better, **95, 186, 98** hath written unto **98, 218, 97** much in praise of **100, 174, 103** in general,
> and particularly for his good carriage in **111, 95, 221,** and upon his motion **93, 31, 174 99** is to be
> **64, 99, 11, 79, 85, 35, 12, 69, 28, 29, 79, 44,** in which courses **174** shall do well to continue.

59 figures, 39 distinct, max 270. Repeated: 98 ×4, 99 ×4, 44/79/95/186 ×3, 28/35/59/69/93/174 ×2.

## 3. Structure (from [analyze.py](analyze.py), output in [analyze_out.txt](analyze_out.txt))

* **91–111 are nulls.** Nine distinct values (93 95 97 98 99 100 103 108 111), each used 1–4 times, and 17 of 18
  occurrences sit at the edge of a cipher run or immediately beside a ≥112 code (`93 185 95`, `99 149`, `95 186 98`,
  `98 218 97`, `100 174 103`, `111 95 221`, `186 99`). Tomokiyo's guess is confirmed.
* **≥112 are nomenclator codes** (113 143 149 174 185 186 218 221 270): each stands alone between nulls or clear
  text, and 270 is explicitly *introduced* ("for whom 270 thus hereafter").
* **< 91 are letters**, and the letters are the key to the whole thing: the four spelled runs contain doubled letters
  written with *consecutive* figures — `49 50`, `69 70`, `28 29`, `11 12` — i.e. each letter owns a block of
  consecutive figures. Cribs:

  | figures | reading | context |
  |---|---|---|
  | 28 69 49 50 70 44 (89) | l e t t e r (s) | "brought no letters from [the Lord Deputy]" |
  | 11 79 85 35 12 69 28 29 79 44 | c o u n c e l l o r | "upon his motion [Ormonde] is to be a councellor" (Ormonde sworn PC Jan 1635) |
  | 10 44 79 47 8 59 | C r o s b y | Sir Piers Crosby, who fell out with Wentworth in the 1634 Parliament and was put out of the Irish Council early in 1635 ("like to go worser with him") |
  | 64 | a | "is to be **a** [null] councellor" |
  | 65 35 21 26 59 | a n g [k] y | "he was angry [with] the Lord Deputy" — see §5 |

  All of these are consistent with **one regular key**: the 19 consonants of the 24-letter alphabet
  (b c d f g h k l m n p q r s t w x y z; i=j, u=v) in alphabetical order, **three figures each, starting at 7**,
  followed by the vowels from 64:

  ```
  b 7-9   c 10-12  d 13-15  f 16-18  g 19-21  h 22-24  k 25-27  l 28-30  m 31-33  n 34-36
  p 37-39 q 40-42  r 43-45  s 46-48  t 49-51  w 52-54  x 55-57  y 58-60  z 61-63
  a 64-..  e ..69,70..  i ..  o 79-..  u 85-..      (vowel block sizes not fixable: 5 each = 64-88, or a=3/others 6 = 64-90)
  91-111 nulls        112+ nomenclator (names/words)      1-6 unknown (nulls or "&"/"the"?)
  ```
  Every letter-figure in the text falls where this grid predicts (b8 c10-12 g21 l28-29 m31 n35 r44 s47 t49-50 y59
  a64-65 e69-70 o79 u85); the only misfit is 26 (see §5). An exhaustive scan of regular grids (start 1–11, block
  2–4, uniform vowel blocks 2–6; 42 grids) ranks start=7/size=3 first by English quadgram score.
* Tomokiyo's "44 79" / "79 44" are simply **r-o** (C**ro**sby) and **o-r** (councell**or**).

## 4. Reading

Letter 1 (13 Sept 1634):
> ...it is said he [Kildare] came over because he was **ANGRY** [null] **113**=*with* **186**=*the Lord Deputy* [null]
> **143**=*the King* refused to see him because he brought no **LETTER[S]** from **186**=*the Lord Deputy* [null].

Letter 2 (22 Jan 1634/5):
> You desire to know what [null] **185** [null] hath written unto [null] **149**, concerning [null] **CROSBY**, for whom
> **270** thus hereafter, of which I can give you no account... it is like to go worser with him rather than better.
> [null] **186**=*the Lord Deputy* [null] hath written unto [null] **218**=*Secretary Coke* [null] much in praise of [null]
> **174**=*Ormonde* [null] in general, and particularly for his good carriage in [null][null] **221**=*Parliament*, and upon
> his motion [null] **31**=m(?) **174**=*Ormonde* [null] is to be **A** [null] **COUNCELLOR**, in which courses
> **174**=*Ormonde* shall do well to continue.

## 4a. The nomenclator checked against Knowler (second session)

The events behind both cipher passages are described by Wentworth himself in dispatches printed in Knowler's
*Strafforde's Letters* (1739), vol. I (OCR downloaded from the Internet Archive and searched; the passages are copied
with OCR line numbers in [knowler_excerpts.txt](knowler_excerpts.txt)):

* **Kildare (letter 1).** Wentworth to Secretary Coke, [October] 1634, p. 309: "The Earl of Kildare went away from
  hence without the privity of this State, and in seeming displeasure against me ... within an hour after, he put to
  sea for England. Indeed I should not have mentioned thus much, but that I hear **his Majesty refuseth to admit him
  to kiss his hand**, which I acknowledge as a respect to me". Coke's marginal answer: "The Earl of Kildare shall be
  sent back as is advised." This is exactly Maltravers's sentence: *he was angry with the Lord Deputy; the King
  refused to see him because he brought no letters from the Lord Deputy.* So **143 = the King** and **113** is the
  connective between "angry" and "the Lord Deputy" ("with"/"against"; Wentworth's own word is "against").
* **Ormonde and Crosby (letter 2).** Wentworth to Coke, Dublin 16 Dec. 1634 ("22 Dec." until 14 Nov 2026; see the last section), pp. 352–3, reporting who had served well
  in the Parliament: "In the Higher House, there is my Lord of Ormond, that hath as much advantage of the rest in
  judgment and parts, as he hath in estate and blood; and one, who upon my observation since I came hither,
  expresseth very good affections to the Crown and Government; so as I hold him a person of consequence, and fit to
  receive some mark of his Majesty's favour, and humbly offer it to his Majesty's wisdom, **whether it were not
  seasonable to make him a Counsellor** ... so as I should think we had got much the better by the **exchange of the
  Earl of Ormond for Sir Piers Crosby**." Coke's marginal answer: "for the Earl of Ormond, your Lordship shall receive
  herewith **his Majesty's warrant to swear him Counsellor**, according to your advice." Maltravers, a month later:
  *the Lord Deputy hath written unto [218] much in praise of [Ormonde] in general, and particularly for his good
  carriage in [Parliament], and upon his motion [Ormonde] is to be a councellor.* The match is clause for clause:
  **186 = the Lord Deputy, 174 = Ormonde, 221 = Parliament, 218 = the addressee of the dispatch, Mr Secretary Coke**
  (the dispatch was for the King and Coke's marginalia are the King's answers, so "the King" is the alternative for
  218; but the King already has 143, so Coke is preferred). **270** is the code Maltravers assigns to Crosby after
  spelling the name once.
* **Crosby's fall.** James Howell to Wentworth, Westminster 1 Jan. 1635: the fall of Mountnorris "hath quailed the
  spirits of some [Sir Piers Crosby] who thought to have come off well, and in a bravery resolved never to see Ireland
  while your Lordship governs" — Crosby was in England, and "like to go worser with him" (Maltravers, 22 Jan) is the
  court gossip of that month.
* **Maltravers's standing.** Wentworth to Windebank, [summer 1634]: "His Lordship [Arundel] and my Lord Maltravers were
  yesterday both sworn of this Council" — Maltravers was himself an Irish Privy Councillor when he wrote, which is why
  he had, and coded, this kind of news.

Nomenclator, as it now stands:

| code | value | evidence |
|---|---|---|
| 186 | the Lord Deputy (Wentworth) | three consistent uses; Knowler p. 309 and pp. 352–3 |
| 174 | the Earl of Ormonde ("your lordship") | three uses; Knowler pp. 352–3 and Coke's marginal |
| 221 | the Parliament (Irish, 1634) | "good carriage in" ↔ "in the Higher House" |
| 143 | the King | "refused to see him" ↔ "his Majesty refuseth to admit him to kiss his hand" |
| 218 | Mr Secretary Coke (or the King, through Coke) | addressee of the 22 Dec. dispatch |
| 270 | Sir Piers Crosby | assigned in the text ("for whom 270 thus hereafter") |
| 113 | with / against (connective) | "angry 113 the Lord Deputy" ↔ "in seeming displeasure against me" |
| 185 | a person or body, not the Lord Deputy | "what 185 hath written unto 149 concerning Crosby"; see §5 |
| 149 | a person or body, not the King or Lord Deputy | same clause |

## 5. Residual problems (honest list)

1. **185 and 149.** "You desire to know what [185] hath written unto [149] concerning Crosby ... of which I can give
   you no account at all." Since 186 (Lord Deputy) and 143 (King) are used in the same letters, 185 and 149 are other
   parties unless the key carried homophones. Adjacent numbering (185/186) suggests a grouped list of officers
   ("Lord Treasurer"/"Lord Deputy" is the obvious pair); 149 near 143 suggests the royal or Council group ("the
   Council", "the Queen"). Candidates from the Crosby affair: the Lord Treasurer (Portland), the Earl of Holland,
   Secretary Coke, the Lords of the Council. Not decidable from the text; Maltravers himself says he cannot answer
   the question, so no further letter of his will settle it either. Only the key sheet or an Ormonde letter *asking*
   the question would.
2. **26 in "angry".** The grid gives 26 = k, so the printed run reads a-n-g-k-y; r is 43–45. Since "angry" is the
   only sensible word, either Maltravers mis-enciphered or the HMC transcriber misread the MS (44/45 → 26). The
   figure is printed as 26 (scan checked), so this cannot be resolved without the manuscript.
3. **89 at the end of "letter".** Either u (if vowels are a=64-66, e=67-72, i=73-78, o=79-84, u=85-90 — then a slip
   for s) or a null/plural sign (if vowels are 5 each, 64–88, and 89–111 are nulls). Sense is unaffected.
4. Exact vowel block sizes and the meaning of 1–6 cannot be fixed from 59 figures. **31** (= m) before 174 is
   unexplained (perhaps "m[y lord]" begun and abandoned, or an error).

## 6. What was tried

* Downloaded OCR of HMC Ormonde vol. I; extracted both letters; regex scan of the whole bundled file for figure runs
  ([find_cipher_runs.py](find_cipher_runs.py)) — no other 1630s cipher, no key, no interlinear decipher.
* archive.org advancedsearch for all "manuscripts of the Marquess of Ormonde" volumes (17 items; old series I–II,
  new series I–VIII) — the 1634–35 letters appear only in old-series vol. I.
* Compared with the Wentworth-circle ciphers described on cryptiana (Wentworth–Laud: nulls < 30, codes 85–202;
  Scudamore/Cave/Ormonde–Clanricarde regular-block alphabets): same *design family*, different key.
* [analyze.py](analyze.py): frequencies, range distribution, null-position test, bigrams, crib-derived regular grid,
  exhaustive regular-grid scan with quadgram scoring, and an unconstrained homophonic hill-climb (simulated annealing,
  quadgram score, 40 restarts) on the 28 letter-figures. **The hill-climb yields nothing** ("thath erethet hereth
  erthereare", q=-76 vs. -137 for the true key) — with 28 symbols and 28 letters it just fits common quadgrams; the
  solution comes from the consecutive-doubled-letter structure plus historical cribs, not from statistics.
* Second session: Knowler vol. I OCR (2.5 MB) downloaded and searched for Kildare, Crosby, Ormond, Maltravers, Arundel;
  letter headers, closings and running heads located for each hit (results in §4a). Vol. II not needed (1636 on).
* Bodleian **Carte Calendar** (Edwards, 1877–83): the HTML calendar online at bodley.ox.ac.uk begins at volume 30
  (1660); volumes 1–29 are not online, so the 1630s Carte letters to Ormonde cannot be checked for further ciphers
  from here.

## 7. Where the rest is

* The originals (Kilkenny Castle Ormonde papers) are now in the **National Library of Ireland, Ormonde Papers**
  (MSS 2300 ff.); a key sheet, if it survives, would be there or among Maltravers/Arundel papers (Arundel Castle).
  Not online.
* Bodleian **Carte MSS** (vol. 1, 1630s letters to Ormonde) may hold copies; the early Carte volumes are not
  calendared online (see §6).

## 8. Files

`ciphertext.txt`, `analyze.py`, `analyze_out.txt`, `find_cipher_runs.py`, `cipher_runs.txt`, `knowler_excerpts.txt`,
`ormonde1_djvu.txt` (OCR, 4.4 MB, not committed), `p28.jpg`, `p29.jpg`, `NOTES.md`.

## Verification 3, 23 Oct 2026

The v3 sweep flagged the reading at 0.29 on the explicit-hole measure: `texts/letters_decryption.md` (copied from §4)
leaves the code numbers and `[null]` marks in the running text, and each counts as a hole. A reading is now
`texts/letters_reading.md`: the HMC clear text with the cipher words in place, nulls dropped, codes written as their
values, the doubtful ones as `[?word]` (*angry* on the misprinted or mis-enciphered 26, 113 *with*/*against*, 218
Coke) and 185, 149, 31 left unread. **0.75 on explicit holes**, 0.667 plain, hole rate 0.073. The sentences hold, the
clear text carrying them around short cipher runs. Kept read, grade B. It rests on the alphabet recovered from the
adjacent clear text and the nomenclator matched against Knowler 1739; there is no manuscript, key sheet or
contemporary decipherment.

## Verification, 14 Nov 2026

Brice Dudout (*L'Europe chiffrée*), with Claude Opus 5.5. Details in
[texts/verification_20261114.md](texts/verification_20261114.md).

* **The print checked again.** All 59 figures were compared with the HMC page images (IA n43, n44) and agree; 26 and
  31 are clearly printed so. This check is not blind. The same pages hold two other Maltravers letters, 30 Sept 1634
  and 10 July 1635, and neither has any figures.
* **185 = the Lord Deputy (probable).** Three points support it. The clause "185 hath written unto 149 concerning
  Crosby" is built like "186 hath written unto 218". In Knowler vol. I, Wentworth wrote on Crosby before 22 Jan 1635
  only in the dispatch to Coke of 16 Dec 1634, and that dispatch also praises Ormond and proposes him for the Council.
  And 185 sits next to 186, which fits the key's blocks of consecutive figures. **149** stays open: it could be Coke
  under a second figure, or Laud (Wentworth sent him duplicates of the dispatch the same day), or the King.
* **Date.** The Ormond dispatch is signed 16 Dec 1634 in Knowler. The letter of 22 Dec 1634 is to Cottington.
* The vowel blocks are still not fixed: 5 each, or a = 3 and the others 6, the second making 89 = u. No measurement
  is possible, since the text has 59 figures in all.
* **Strict count:** 17 of 19 cipher units read as sense (12 sure, 5 probable, 2 unresolved: 149 and 31), 89.5%,
  against 84.2% before. Still **read in part**.

