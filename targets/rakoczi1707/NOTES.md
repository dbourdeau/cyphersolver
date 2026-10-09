# Philippe Groffey (?) to Ferenc Rákóczi II, 15 October 1707 — DECODE R902

Status: read (deciphered with the preserved key R639). Both cipher pages were retranscribed group by group from the
images (30 Sept and 5 Oct 2026); 982 of 1,017 counted groups (96.6%) read as sense (`measure_tr.py`,
`R902_reading.md`).

MNL OL, G15 Caps. C. Fasc. 39, pp. 277–279. DECODE R902,
`NAH_G15_CAPS_C_FASC_39_277`. The archive images are not in the public domain and are deliberately not reproduced
here. Research copies were viewed through the account supplied for this project.

## Correction to the catalogue

DECODE calls Pompeio Cesoni (Ferenc Rákóczi II) the author. The address leaf says, in clear,
`A Monsieur / Monsieur Pompeio Cesoni`. Rákóczi is therefore the **recipient**, not the sender.

The sender is very probably **Philippe Groffey** (also Grophey/Graffei in the literature):

- the matching key is headed `De Monsieur de Bonac et Graffei`;
- the writer handles intelligence from the Swedish and Polish courts and discusses letters from Pál Ráday to
  Field Marshal Carl Gustaf Rehnskiöld;
- Groffey was the French-speaking agent used by Rákóczi at those two courts, and the 1707–08 accounts print his
  salary by name.

There is no open signature on the photographed leaves, so the name is an attribution, not a palaeographic reading.

## The key

The letter uses the preserved table in **DECODE R639**, MNL OL G15 Caps. C. Fasc. 44/08. Its transcription is
`DOC_R639_D2752_2752.txt`; the heading is `De Monsieur de Bonac et Graffei`.

It is a one-part numerical nomenclator:

- 10–120: homophonic letters and common endings;
- 121–460: syllables and common words;
- 461–560: titles, peoples, countries, places, names, months, and numbers;
- 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119: nulls.

Rare, diagnostic values include 489 = *Monsieur*, 491 = *Monseigneur*, 497 = *les Svedois*, 506 = *Svede*,
507 = *Pologne*, 526 = *le Prince Constantin*, and 533 = *Dantzig*. The same table reads the known-plaintext
comparators R852 and R912. On R902 it recognizes 1,020 of 1,108 parsed groups (92.1%). The residue is overwhelmingly
made of impossible numbers, joined groups, and one-digit slips in DECODE's manual transcription.

`decode.py` applies the table. `R902_key08_read.txt` is the conservative token-level result: bracketed numbers are
not silently guessed. The raised leading `1` used in this hand is represented by DECODE as `1^.` and must be joined
to the following one or two digits; treating that period as an ordinary separator destroys the reading.

## What the letter says

The document is an intelligence and lobbying report from the Polish–Swedish theatre. The first part surveys military
and diplomatic news involving the Tartars, Saxony, the Swedes, the Emperor, Vienna, and the English and Dutch. The
writer then turns to his own work for Rákóczi. Secure or nearly secure stretches read:

> J'ay aussi eu l'honneur de vous [représenter], Monseigneur, ... les lettres de Monsieur Ráday au général
> Rehnskiöld ...

> ... à la Cour de Suède ... réparer le tort ... à Votre Altesse ... vos intérêts ...

> ... sur mon zèle à Votre Altesse ... je me suis donné tous les mouvements ... tant à la chancellerie suédoise
> qu'à la Cour de Pologne ...

The second leaf discusses the King of Poland, Prince Konstanty, and the King of Sweden, then the disposition of
Polish grandees and troops. Its clearest political sentence says that someone taking Poland's interests to heart was
resolved to sacrifice himself, if necessary,

> ... pour affranchir la liberté ... opprimée par les Suédois en faveur du roi Stanislas ...

This is not a private letter by Rákóczi. It is a report **to** him about attempts to advance his interests at the
Swedish and Polish courts, including the fate of Ráday's approach to Rehnskiöld and Polish resistance to Swedish
management under Stanisław Leszczyński.

## Limits of the reading

(Superseded on 5 Oct 2026 by the full image retranscription below; kept as the record of the DECODE-based stage.)

The key is certain; the exact prose is not yet publishable as a continuous quotation. The DECODE transcription often
confuses a single digit (for example 142 gives *bo* where 192 must give *eu*, and 143 gives *bu* where 173 gives
*de* in `J'ay aussi eu l'honneur de vous`). Because the code mixes letters, syllables, and complete words, one wrong
digit can turn a normal word into several plausible-looking fragments. Contextual repairs were used only to
identify phrases and are **not** accepted as a continuous diplomatic reading.

A final edition requires retranscribing the 2 cipher leaves directly, group by group, then rerunning `decode.py`.
The result above is enough to identify the system, reverse the catalogue's sender/recipient direction, attribute the
writer with high probability, and establish the subject of the hidden text.

## 30 Sept 2026: closing lines of p. 278 transcribed afresh and read continuously

For Lasry's list of quotations (the old quotation was four M fragments), lines 10-18 of p. 278 (DECODE image 4844,
`R902_p2.png` in the main checkout) were transcribed group by group from the image (`tr/R902_p278_l10-18.txt`,
196 groups) and decoded with the corrected R639 table of targets/rakoczi1704 (`decode_tr.py`). Every group that is
not a filler has a value. Reading and translation: `R902_p278_reading.md`. The passage:

> On se borne présentement à se plaindre de la conduite de Vostre Altesse à l'égard des affaires de la Pologne, et
> de certains discours qu'elle doit avoir tenus en présence de gens qui en ont rendu compte, asseurant qu'elle
> avoit dit que, prenant les intérêts de la Pologne autant à cœur que ceux de la Hongrie, elle estoit résolue de se
> sacrifier elle-mesme s'il le falloit pour affranchir la liberté polonoise opprimée par les Suédois en faveur du
> Roy Stanislas. Je suis avec un très profond respect …

So the 'someone taking Poland's interests to heart' above is Rákóczi himself, as reported to the Swedes; the
'Hongrie' is 517 (DECODE's 527 would be Tekeli). Findings:

- DECODE's '3^' is this hand's 5 and its '1^.' the raised 1. Read that way its digits are mostly right; the old
  `decode.py` took 3^ as 3. Its real slips here are the curled 1 before 7/0 read as 2 (273 for 173 de, 276 for
  176 di, 278 for 178 du, 204 for 104 U), a few single figures (325/315, 404/407, 200/100, 527/517) and groups run
  together without the point.
- 212 = Fa (C: the F row is the syllable series; faveur, falloit); 93 = st (C: Stanislas; 'obstacle' in R912).
- An underlined number keeps only its first syllable (C, eight cases): 342_ pren-ant, 123_ af-franchir,
  507_ Polo-noise, 343_ pres-ence, 124_ Al-tesse, 160_ Com-pte, 424_ tre, 344_ pro-fond.
- Line-opening 125, 127 and 670 are fillers here, like the 5xx groups at line ends.

## 5 Oct 2026: p. 277 and p. 278 lines 1-9 retranscribed from the images; 96.6% read

The rest of the letter was transcribed afresh group by group from the images (`tr/R902_p277.txt`, 31 lines;
`tr/R902_p278_l01-09.txt`), from line strips at 1.5-1.8x with contrast enhancement (p. 278 deskewed -3.3 deg).
The decisive palaeographic point: the curled 'c' figure in this hand is **1**, not 2 (DECODE gives 274/275/273
for 174/175/173 throughout), and DECODE's '1 o? 4' is often 109 (the hand's 9 is a q-shape). With that, the
DECODE-based 92% "has a value" figure became a continuous text: the report is dated **Słupca, 15 October**
(1707), follows two earlier letters from Görlitz and Lübben, and covers the Swedish settlement with the
Emperor, the Swedish army waiting 8 leagues from Poznań for recruits landed at Stettin, Ráday's letters to
Rehnskiöld, the writer's advice to send a new agent to the Swedish court, the suspicion he lies under, and the
rumour that Rákóczi had arrested the Palatine of Ruthenia's children and a Polish royal envoy returning from
Constantinople with a Turkish deputy. Reading: `R902_reading.md`.

`measure_tr.py` counts every group except line-initial fillers (97-127 odd, 125, 127, 563, 566, 670, 689) and
line-final 5xx/6xx groups: p. 277 617/643 (96.0%), p. 278 l. 1-9 185/190 (97.4%), p. 278 l. 10-18 180/184
(97.8%); **R902 982/1,017 = 96.6%**. Twelve groups are counted read only after a context-forced one-figure
correction (grade C, listed in CORR: e.g. 118 es for 128 in *dernieres*/*recrues*, 298 ni for 248 in
*maniere*/*opinion*), and 89 = Et is added (C, three places). Line-initial 121 and 129 are counted as unread, not
as fillers.

## Sources checked

- DECODE R902 (ciphertext and address leaf), R639 (key), R852 and R912 (same-key comparators).
- Kálmán Thaly, ed., *II. Rákóczi Ferencz fejedelem leveleskönyvei*, vol. 2 (1873). The printed accounts name
  Groffey and record salary paid through December 1707; the target letter itself is not printed there.
- Kálmán Benda, *Le projet d'alliance hungaro-suédo-prussienne de 1704* (1960), on Philippe Grophey and Ráday.
- *Études sur François II Rákóczi, prince de Transylvanie*, identifying Philippe Groffey as Rákóczi's representative
  especially at the Swedish and Polish courts.

## Remaining gaps
- R902 p. 277 l. 13-14, the end of the first paragraph (10 groups: 224 264 174 226 37 / 324 125 104 589 4) - blocker: open-codes; the groups are clearly written and decode to letters that make no word (gi les de gu O pe avec U); possibly a name or a null run; no sibling or print to check against
- R902 scattered single groups (~25: 85, 8, 120 x2, 297, 363, 129, 436, 860, 95, 92, 9, 194, 589, 121, 129, 264, 89, 27, closing 4/5/567/609) - blocker: open-codes; each was re-read on the image and the reading stands, but the value gives no sense in context
- Grade-C corrections (12) rest on context, not on the image - blocker: needs-physical-access; image resolution (2448 px for the page); a higher-resolution scan from MNL OL would settle them

## Escalation
- [x] siblings: same-key comparators R852 and R912 read; DOC files R633-R646 fetched
- [x] clear-pages: R902's two leaves carry only cipher plus the clear address; a first-line interlinear gloss on p. 277 ('a s lu p u le t mars') is a contemporary attempt and agrees with 66 45 262 94 ... 258 (A S lu P ... le)
- [x] known-keys: score_keys.py tested NAH G15 keys; R639 (Bonac et Graffei) fits
- [x] print: Thaly, Rákóczi leveleskönyvei II (1873), Benda 1960, Études sur François II Rákóczi: letter not printed
- [n/a] key-rebuild: key table R639 is complete; only 89 (= Et) added from this letter
- [x] retry: whole letter retranscribed from the images (30 Sept, 5 Oct 2026) and remeasured with the extended table: 96.6%
