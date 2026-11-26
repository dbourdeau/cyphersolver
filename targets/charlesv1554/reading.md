# Reading: Bibliothèque municipale de Besançon, Ms 1582, f. 2r-v

Cipher passage of Charles V's letter to his ambassadors in England (Lalaing, Egmont, Courrières, Simon Renard),
Brussels, 24 January 1554. The text is **already in print** from the minute: Gachard, *Collection des voyages des
souverains des Pays-Bas* IV (1882), appendix CLV, pp. 311-314 (this passage pp. 313-314); English calendar in Tyler,
*CSP Spain* XII (1949), pp. 44-49 (this passage pp. 46-47). This reading is made from the cipher, decoded with the key
in `key.tsv` (an independent re-derivation of the cipher published by Pich-Ponce 2024), and is given so that the
cipher, the contemporary decipherment on the page and the printed minute can be compared.

Marks: sure (no mark: the decode spells the word) / {probable} (the decode is off by a sign or a key value but the
word is clear and agrees with the minute) / [restored] (not in the decode, supplied from the minute) / `[... n]` a
line not transcribed, its size estimated from the minute. Spelling of the cipher kept. Line numbers are the cipher
lines of the blind transcription (`transcription/cipher_reconciled_AB.tsv`); a hyphen marks a word split over two lines.

## Text (French)

```
r1   [no]stre part que {nous} avons {tousjours} eu et
r2   avons encores la mesme volenté de desirer la {pai-
r3   -x} union et {repos} publicque de la {chrestien-
r4   -té} et {pour} euiter d'entrer en rompture {nous}
r5   {avons} souvent {comporté} et {dissimulé} {beau-
r6   -cop} de {choses} {aux} françois et que ceste {der-
r7   -nière} rompture {ilz} l'ont faicte comme {tou-
r8   -t} le monde scait {voluntairement} et par {leur}
r9   {libre} election sans cause {quelconque} que {tou-
r10  -tesfois} et {nonobstant} toutes les {choses}
r11  {notoirement} si {mal} passées {nous} {n'avo-
r12  -ns} {jamais} {rebouté} {d'entrer} en negociation
r13  de {paix} si avant que l'on [mit] en {avant}
r14  conditions {raisonnables} et que {nous} {te-
r15  -nons} que si {sans} passion l'on {estime} {et}
r16  {juge} {celle} que a la requisition du {cardinal} d'Imola
r17  {nous} {mismes} en {avant} {au} mois de {sep-
r18  -tembre} dernier que l'on la {tiendra} {accom-
r19  -paigné} {de} toute raison {combien} que sur {icel-
r20  -le} [le] roy {n'a} {jamais} {donné} responce {quelle} {quelle}
r21  soit ny {declairé} plus avant a quoy
r22  {il} {vouldroit} {pour} {retourner} {a} {paix}
r23  {ce} {puisque} {nous} sumes et {continuons} en la
r24  mesme volenté que dessus de {facillement} {condescen-
v1   -dre} a negociation de {paix} si avant que
v2   l'on offre conditions {convenables} vous
v3   {pourrez} en certiffier de {nostre} {part} [ladi-
v4   -cte] {dame} afin {qu'elle} le face entendre ou
v5   que {bon} luy semblera que {tant} plus y encli-
v6   -nerons {nous} {pour} estre {chose} qui se {negocie}
v7   par {elle} et {où} {elle} mect la {main}
v8   {mais} {qu'il} {fauldroit} prealablement en-
v9   -tendre {ce} que les {françois} {vouldront} di-
v10  -re {non} seulement en ce de la {paix} {mais}
v11  {aussi} de la tresve {puisque} selon les conditions
v12  {qu'ilz} y {vouldroient} mectre
v13  {nous} {pourrons} {juger} de {quel} pied {ilz}
v14  {cheminent} et l'apparence {qu'il} y aura
v15  de {pouvoir} {tirer} {quelque} fruit de ce {qu'ilz}
v16  mectront en avant {pour} le {repos} {public-
v17  -que} {et} sera {bien} que vous le {lieutenant} {d'Amont}
v18  assentez dudit {Paget} si {l'ambassadeur}
v19  de France ne luy aura depuis parlé plus
v20  avant {des} partiz de mariage {dont} ses {let-
v21  -tres} a vous faisoient mention de
v22  ce que l'on vous respondra cy dessus et que
v23  avec le temps entendrez plus avant
v24  de ce que l'on {vouldra} dire du {costel} de France
v25  {il} sera {bien} que de temps {a} autre
v26  {nous} {donnez} {advertissement} {pour} [regarder] [a] [quoy] [nous] [vouldrons] [resouldre] [selonc] [ce]
```

## Count (repository rule: sure words only)

358 words: **215 sure (60.1 %)**, 131 probable, 12 restored. With probable words, 346 of 358 = 96.6 %. **Read in
part.** (Until 19 Nov 2026 the last line of each page, r24 and v26, was cut off in the transcription crops and counted
as not read: 210 sure. Both lines were then transcribed from the full scans in two new blind passes and arbitrated,
`transcription/cut_lines_r24_v26.tsv`: r24 adds 5 sure and 2 probable words; v26 adds 4 probable words, and its
last 8 words, *regarder à quoi nous vouldrons resouldre selonc ce*, are restored from the minute: the line ends with
three signs (r, n?, va) that do not spell them, and whether the cipher went on elsewhere is not known. *condescendre*
runs from r24 (*conde*, then a sign cut by the paper edge) to v1 (*ndre*).)

Most probable words are probable for one of three recurring reasons, all key-side: (1) the sign read `nus` for *nous*
(and `pur` for *pour*), i.e. a syllable value for *no/po* missing from the re-derived key; (2) the two forms `nz` (d/i)
and `w` (a/l) that the transcribers did not separate; (3) the a/n/p confusion of `mt`/`nt` (*cardipaa* = *cardinal*,
*raisonpables*). Pich-Ponce's published table (2024), compared on 19 Nov 2026 (NOTES.md), explains (1) for *no*
(`m'.`, her o-syllable mark) and (2) and (3) for `w` (her 20 a and 10 l), `nz` (17 d and 12 i) and `mt` (na); her values
are not transferred into `key.tsv` or this reading, which stay an independent re-derivation.

Unresolved / open: r13 the cipher reads `c^ n u` (*deit*), the minute and the contemporary decipherment *mit*; the
words at r23 *ce* (minute *Et*); in v26 the sign after *advertisse-* (c or t) and the last three signs.

## Translation (English, by the contributor; not the CSP calendar text)

... our part, that we have always had and still have the same will to desire the peace, union and public repose of
Christendom; and to avoid coming to a breach we have often borne and overlooked many things from the French; and this
last breach they made, as all the world knows, of their own will and free choice, without any cause whatever. That
nevertheless, and notwithstanding all the things so notoriously ill done, we have never refused to enter into
negotiation of peace, provided reasonable conditions were put forward; and we hold that if one weighs and judges
without passion the proposal that we put forward at the request of the Cardinal of Imola in the month of September
last, it will be found to carry every reason, although the King has never given any answer whatever upon it, nor
declared further on what terms he would return to peace. And since we are and continue in the same will as above, readily to
come to negotiation of peace provided suitable conditions are offered, you may assure the said Lady [Queen Mary] of it
on our part, so that she may make it understood wherever she pleases: that we shall be the more inclined to it because
it is a thing negotiated by her and to which she sets her hand; but that it would first be necessary to hear what the
French will say, not only on the peace but also on the truce, since by the conditions they will wish to put to it we
shall be able to judge on what foot they walk, and what likelihood there is of drawing some fruit from what they put
forward for the public repose. And it will be well that you, the Lieutenant of Amont, find out from the said Paget
whether the ambassador of France has since spoken to him further of the marriage matches that his letters to you
mentioned; and of what you are answered on the above, and of what in time you learn further of what is said on the
French side, it will be well that from time to time you give us notice, so that we may consider what we shall
resolve accordingly (the last eight words restored from the minute).

## Summary

Charles V tells his ambassadors in London how to answer the French peace overtures made to Wotton in France and, in
England, by the French ambassador to Lord Paget: the Emperor has always wanted peace, the French broke the last truce
of their own will, his proposal of September 1553 made at the request of the legate Girolamo Dandino (Cardinal of
Imola) was never answered; he will negotiate peace, or first hear French terms for a truce, the more readily because
Mary Tudor is the go-between. Renard is to learn from Paget whether the French ambassador has said more about the
marriage matches he had raised.
