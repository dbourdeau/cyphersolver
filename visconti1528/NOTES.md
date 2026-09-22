# Galeazzo Visconti to Anne de Montmorency, Campo a Landriano, 30 Aug 1528 (catalogue 177)

Read in part (92.7% of cipher glyphs read with confidence, measured by glyph count in final.md). Key: partial
(the letters are recovered; the numbered nomenclator is not). Written up 22 Sept 2026 as
https://dbourdeau.github.io/cyphersolver/visconti1528.html.

BnF fr. 3034 f. 154r-v, no. 68 (DECODE R4223). Gallica btv1b90600370, view 243 = f. 154r (clear opening, 30 cipher
lines), view 244 = f. 154v (9 cipher lines, then the clear close and date). View 242 = f. 153, a separate clear
item. Italian, Lombard spelling (single consonants: tuto, tuti, andase, fuse). Work of 22 Sept 2026.

## Sender and recipient

- Catalogue 177 and DECODE R4223 say "Unknown sender". The letter is unsigned in clear, but the cipher is Galeazzo
  Visconti's: Tomokiyo (cryptiana GL.htm, "Galeaz Vesconte's Cipher (1528-1529)") lists this leaf with fr. 3045 f.28
  and fr. 3096 f.91, both signed by Visconti, and Lasry's key table is headed "BNF Francais 3045f28 and 3034f154 -
  Italian". The same sign set and hand run through all three (siblings.md).
- Recipient: "mons. le grant maestre", Anne de Montmorency (Tomokiyo's description of the address).
- Date line in clear: "Da al Campo a Landriano ali XXX d'aust" [1528].

## Prior work

- DECODE R4223: "Non-decrypted".
- George Lasry's key table (05/11/2023) on Tomokiyo's GL.htm (saved copy gramont1529/GL.htm; image here
  key_fr3045_f28.png). Key only, no plaintext of this letter published. A web search found no edition.
- So the key was known before the attempt; the text was not.

## Files

- KEY.md: the working key (Lasry's table plus what this letter added).
- cipher.txt: first rough token transcription (1344 tokens; superseded by the reading files' glyph-level passes).
- decode.py: applies the rough key to cipher.txt.
- reading_r01-15.md, reading_r16-30.md: recto, glyph by glyph from deskewed Gallica natives, with corrections.
- reading_verso.md, final.md: verso, redone glyph by glyph in the second pass; the retry of every open recto spot;
  the full text; glyph totals; English summary.
- siblings.md: fr. 3045 f.28 and fr. 3096 f.91r opened (escalation step "siblings").

## Key (what this letter added to Lasry's table)

ne-sign = S, me-sign = L, small y = N (a bent-arm y = B), theta = G, plain p = M, the sign written like the word
"far" = CHE, "fu" = FU, q = H (F in "Francesco" by shape), three forms of E, tau and the "2" form = A, hooked tau =
Q, + = O. The long thin diagonal strokes under the lines are word dividers added later by a decipherer, not parts of
signs; they had produced false "hooked p", "crossed q" and "crossed y" readings. The crossed sign is the figure 4
(proved on the siblings, where 42 and 48 appear as numeral pairs): so 48, 4θ and 4r are numbered nomenclator codes,
and rr, qq are recurring code groups. No list of these codes survives in Lasry, Tomokiyo or the siblings.

## Reading (final.md)

Recto: "Poco scritti le lre. Il consiglio de heri fu per tirare queli capitanei che erano lì a la opinione che no
fuse andase a Milano, perché era la mia(?) tuto causato comtagio. Scrito questo, s'è chiarito questa mane, ha esendo
venuto il duca d'Urbino a casa de [48], per deliberare o a Milano o a Pavia. [...] E questa fu inventione de
Francesco, dita in secreto ha queli de la Signoria, [...] aciò che se vincese la opinione de andare a Milano. Rex. Il
che [...] è parso al duca d'Urbino providitore et maiore parte de loro dal canto nostro. Io era solito sempre esere
chiamato il primo per aprire il camino ali altri, et questa volta ha comenciato a Francisco [...] [4θ] dise che ere
da andare a Pavia. Io comenciai a dire quelo agio scrito de andare a Milano. Pensate che Francesco il primo a
interompere, poi qualche uno altro che mi vergogno dirlo, [4r] sapendolo dissimulare. [...] Si va a questo modo se
harà uno pastone de mala digestione. Io vedo asai cose, ma che è in mia posa [..] a provederli; e sapiate che tuti li"

Verso: "nostri, dico tuti, comenciando al capori [...] Dio ch'io scriva al [peu] et a vostra S. provedase [...]
però mai de dire il servicio dil [peu], e vaglia quanto potrà. Tuta volta certifico [...] dito il duca d'Urbino
providitore, et a io che se andarà [...] a traversat[..] il camino tra Milano e Pavia [...] poi il resto," then in
clear "che ca fin de questa ma[teria], pregando n[ost]ro S[ign]or Dio dona a V. S. bona e longa vitta. Da al Campo a
Landriano ali XXX d'aust."

Substance: a council of war at Landriano, held at the lodging of [48], on whether the League army should march on
Milan or Pavia. Visconti argued for Milan. A scheme of Francesco's (Francesco Maria Sforza?), whispered to the
Venetian officers, swung the vote; the Duke of Urbino and the Venetian proveditor chose Pavia. Visconti, usually
called to speak first, was called after the others and interrupted. "A stew of bad digestion" if this goes on. The
army will go to cut the road between Milan and Pavia.

Glyph totals (final.md): 1338 cipher glyphs; 1240 read with confidence (92.7%); 45 read with the sense open or
tentative; 53 without a value.

## Remaining gaps
- nomenclator codes 48 (x2), 4θ, 4r, rr, qq, peu (x2), the rex context - blocker: no-key-material; numbered code, no key in Lasry's or Tomokiyo's tables or in the two sibling letters
- the final sign pair of so../lo../do.. (r10-12) and the one-off signs [Y r] r12, [mur·][ω] r16, [v b] r30, Π v08-09 - blocker: too-short; they occur only here, the siblings show no occurrence to test a value on
- v03 middle and v06 small signs - blocker: illegible; two zoom passes on the Gallica native gave no stable shape

## Escalation
- [x] siblings: fr. 3045 f.28 (Visconti to Angelo Bolano, Alessandria 15 Oct 1528, btv1b9060156p view 54) and fr. 3096 f.91r (Visconti to Francis I, pieve de Locate 15 June 1529, btv1b9060015d view 94) opened; key confirmed on both ("mal tratamento", "che disperat-"); the crossed sign is the figure 4, so 48/4θ/4r are numbered codes; rr and qq recur as groups; peu and the one-off signs do not occur
- [x] clear-pages: the verso and address leaf carry no decipherment; f.153 (view 242) is a separate clear item
- [x] known-keys: Lasry's Visconti table (the base key); the Bizozola key of fr. 3034 f.156 is a different cipher
- [x] print: Tomokiyo GL.htm (key only), web search: no edition of the letter
- [x] key-rebuild: key extended on this letter (ne=S, me=L, y=N/B, crossed psi read with y, theta=G, p=M, far=CHE, fu=FU, q=H/F by shape, three E forms, word-divider strokes identified)
- [x] retry: second pass over every open spot and the whole verso glyph by glyph (final.md)
