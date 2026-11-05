# Henri III to Bellièvre and Villeroy, 21 Oct 1580: key test on the cipher postscript (5 Nov 2026)

BnF fr. 15906 (2), ff. 520r-522v (Gallica btv1b9064322t, canvases 92-95). Purpose: decide whether the edition's
analysis (*Lettres de Henri III* t. V, no. 4006, p. 110) covers the 17-line cipher postscript on f. 522v, which has
no decipherment on the leaf. Done by a subagent from the full-resolution openings; transcriptions `ct_521r.txt`,
`ct_ps.txt`, aligned plaintext `pt_521r.txt`, key `key.json`, crop scripts `crop.py`, `qcrop.py`, `rows.py`,
`pscrop.py` (crops are git-ignored).

## Key

Anchor: above line 7 of the f. 521r block the decipherer wrote "escripte" letter by letter over the signs. The block
was then aligned to the complete marginal decipherment on its clear runs (empescheray, sieur, Rochepot, puisse, loger,
troupes, Cambray, advisera, que ce soit, mes terres, demoure, ferme, Flandres, resolution que j'ay dernierement,
escripte en vostre instruction, vouloir, adjouster, ny diminuer, bien pourrez). The margin's first words read "que je
n'empescheray pas". The f. 521v blocks were not needed.

System: homophonic letter substitution, mostly one sign per letter, with word signs (que, vous, luy, de, la, le, du,
rien), number codes (10 a person; 12, 14, 7; 18 = sieur after "mon"/"le"), and groups of null signs framing each
block. High-confidence letters: a c e f h i/j l n o p r s t u/v y z and ss; medium: m, d, two look-alike r/t signs;
eight signs unidentified.

## Postscript, read in part (? = unread)

1. (De)puis ceste lettre escripte, le s(ieu)r (de) Marchaumont ? ? ? ...
2. ... sentir que mon(sieur) frere veult envoyer devers Cambray ... se peussent
3. saisir le Castelet [7] ? ... ilz ... ilz
4. eussent ... ilz craignent ... ilz
5. vouloient avoir ma permission ? ... seulement ...
6. ...ration ... ilz s'en feussent saisyz ... Marchau-
7. -mont, que je seroy(s) ... que je ne le voulois nullement ... aussy ...
8. ... une ... je veulz y penser avant que d'entrer
9. en aucune choze, il y ... [12] ... J'ay aussy receu une despesche du [?]
10. de laquelle je vous envoye ... ?mention? de la paix ...
11. ... que les aultresfois que ?j'ay traicté de la paiz, ce ... de la
12. ? et le [Roy] catholicque ?n'a point ? que luy que j'ay employé aulx aultres paix
13. ?les premiers et principaulz ... [10]
14. Je suis d'advis que vous Villeroy luy en escripviez ... que [10], et luy mandiez
15. que je le vous ay commandé ... (quel)que opinion il vouldroit s'en mesler
16. ou il a envye d'y traverser. / a Dolinville ...

## Verdict

The postscript is the source of the last part of the edition's analysis of no. 4006: "... je veulz y penser avant que
d'entrer en aucune choze" (line 8) is the edition's quotation "... a quoy je veulx bien penser avant que d'entrer en
aucune chose qui me puisse nuire", and lines 10-16 (the peace; Villeroy to write to the man "que j'ay employé aulx
aultres paix", code 10, to learn whether he wants to take part or to obstruct) are its closing sentence "Enfin le
maréchal de Biron veut se mêler du rétablissement de la paix en France. Des consignes sont données ici à Villeroy pour
qu'il écrive au maréchal." Code 10 = Biron, who negotiated the peaces of 1570 and 1577, on the edition's word; it is
not spelled out in the cipher. So the editors had the postscript deciphered (by themselves or from a decipherment not
on the leaf), and the item is not an open cipher. Lead closed as read (edition).
