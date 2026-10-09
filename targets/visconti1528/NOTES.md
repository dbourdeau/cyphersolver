# Galeazzo Visconti to Anne de Montmorency, Campo a Landriano, 30 Aug 1528 (catalogue 177)

Read in part (1248 of 1337 cipher glyphs read as sense, 93.3%, measured by count_tokens.py over tokens.txt, re-read 5 Oct 2026; third
pass 22 Sept 2026). Key: partial
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
- George Lasry's key table (05/11/2023) on Tomokiyo's GL.htm (saved copy targets/gramont1529/GL.htm; image here
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

## Code identifications from the full sibling readings (22 Sept 2026, second session pass)

fr3045_f28_reading.md and fr3096_f91_reading.md (both read in part):
- [48] = probably Saint-Pol: fr. 3096 l.8 "cum l'andata di [48]" (June 1529, when Saint-Pol left the camp for Genoa); fits "a casa de [48]" here (the council at the French commander's lodging, attended by the Duke of Urbino). Probable, no clear-text match.
- [peu] = probably the King: fr. 3045 l.19 "per servicio di [ep]", the same formula as v04-05 "il servicio dil [peu]". Probable.
- [rr] = a French agent acting for the King, not the King (fr. 3096 l.3 "[rr] heri ... fece l'oficio de vostro bono servitore"); name not found. The r21 "[r r ᵽ]" here is rr plus one sign.
- [4θ], [4r], [qq] and the so../lo../do.. final pair do not occur in either sibling. qq recurs in fr. 3045 as an overbarred name-like group, not identified.
- fr. 3096 also shows q = F (facio, fece, farà) and a b-shaped H / h-shaped B pair; no change to the readings here.
Crediting the two probable identifications (48 x2, peu x2) moves the measured figure from 1240 to about 1246 of 1338 (93.1%). The rest stays blocked as listed below; the read bar (95%) is not reached.

## Lead from the siblings (visconti1529)

22 Sept 2026. Two rules were found on the siblings (targets/visconti1529/, fr. 3096 f.91 and fr. 3045 f.28) after this
letter was read: a bare Λ is a doubling mark (que[Λ]la = quella, a[Λ]sai = assai), and the 'far' sign stands for NTO
as well as CHE (altrotanto, mancamento, quanto). They have not been re-applied to this letter's open stretches
(so../lo../do.., asciilati, ascicsai pui, acuvante, the v03 and v07 runs). The counts above are unchanged.

## Third pass (22 Sept 2026)

final.md "## Third pass (sibling rules)" and its addendum; token file tokens.txt, counted by count_tokens.py.
- "fuo" (r01, r12) = Lombard *fu*, as in fr. 3096 "che fuo", "fuose"; blotted retouches in r05, r10, r12 read.
- r09 overlined `q q` = code [qq] (fr. 3045 l.2, l.16), followed by "volse": "[qq] volse [48] che il duca d'Urbino tirase".
- r21 `r r` is overbarred: code [rr], the French agent of fr. 3096 ("poi a me [rr] [ᵽ] acuvante se").
- v07 has no A between "et" and "io": "et io che se andarà" (1 token removed, total 1337).
- v03 middle, enhanced on the Gallica native (autocontrast, unsharp mask, threshold, 2x): the signs are sharp and
  legible, "m ı t ǂ ï r"; the ǂ-r pair is the numbered code 4r seen in r25. The v03 gap is a code, not illegible.
- 'far' is CHE at every place here (NTO fits none); several readings tested and not adopted (final.md).

Counts: 1337 glyphs; 1247 read as sense (93.3%); 53 sense open; 21 unread; 16 code. Below the 95% bar (1271 needed).

## Remaining gaps
- nomenclator codes 48 (x2), 4θ, 4r (r25 and v03), rr (r21), qq (r09), peu (x2) (48 probably Saint-Pol and peu probably the King, from the siblings, not proved) - blocker: no-key-material; numbered code, no key list survives, both siblings read in full without resolving them
- the final sign pair of so../lo../do.. (r10-12, values I-I, "soi/doi" Lombard, "loi" not secure), the one-off signs [Y r] r12, [mur·][ω] r16, ᵽ and "acuvante" r21, + r27, [v b] r30, Π v08, the v07 "sfu[m]o" and v09 "spire[Λ]rà" stretches, r07 "asciilati", r09 "cicsai pui" - blocker: too-short; they occur only here, the siblings show no occurrence to test a value on, readings tested in the third pass need two or more slips
- v01 blotted ψ̄ and the ſt ligature - blocker: illegible; a solid ink blot and a flourished ligature, unchanged after enhancement

## Escalation
- [x] siblings: both siblings then read in full (fr3045_f28_reading.md, fr3096_f91_reading.md): 48 = Saint-Pol and peu = King probable, rr a French agent; fr. 3045 f.28 (Visconti to Angelo Bolano, Alessandria 15 Oct 1528, btv1b9060156p view 54) and fr. 3096 f.91r (Visconti to Francis I, pieve de Locate 15 June 1529, btv1b9060015d view 94) opened; key confirmed on both ("mal tratamento", "che disperat-"); the crossed sign is the figure 4, so 48/4θ/4r are numbered codes; rr and qq recur as groups; peu and the one-off signs do not occur
- [x] clear-pages: the verso and address leaf carry no decipherment; f.153 (view 242) is a separate clear item
- [x] known-keys: Lasry's Visconti table (the base key); the Bizozola key of fr. 3034 f.156 is a different cipher
- [x] print: Tomokiyo GL.htm (key only), web search: no edition of the letter
- [x] key-rebuild: key extended on this letter (ne=S, me=L, y=N/B, crossed psi read with y, theta=G, p=M, far=CHE, fu=FU, q=H/F by shape, three E forms, word-divider strokes identified)
- [x] retry: second pass over every open spot and the whole verso glyph by glyph (final.md)
- [x] retry (third pass, 22 Sept 2026): sibling rules from visconti1529 re-applied to every open stretch (doubling Λ, far = NTO, ρ = F, fuo = fu); r09 qq and r21 rr identified as codes; 1240 (by eye) / 1235 (token file) -> 1247 of 1337
- [x] enhancement: autocontrast, unsharp mask, threshold and 2x zoom on the Gallica native crops of r21, v01, v03, v06, v07, v09: r21 rr overbarred; v03 signs legible and the ǂ-r pair is code 4r; only the v01 blot stays illegible
- [x] retry (push to 95%, 5 Oct 2026): every open stretch rechecked; r10-12 pair tested as RO (soro/loro/doro: only loro fits) and as I (soi/loi/doi: loi not secure), left open; r07, r09, v03 still give no word with at most one slip; the 16 code glyphs stay unkeyed. No change, 1247/1337 = 93.3%. 95% needs 24 more glyphs; 16 of the 90 unread are codes with no key, the rest one-offs and blotted spots.
- [x] full push (5 Oct 2026, coordinator request): the natives in full/ (c243 4153x6087, Gallica full/max) were already on disk; the deskewed page desk243.png was re-cut at full resolution on measured line centres (push/r*.png, zoom push/z07.png). Tested with Lasry's own table, which this letter's key had diverged from:
  - Lasry gives an L-shaped sign as a third A, and the siblings use L=A 32 times (fr. 3045). Here the footed L reads C in 26 secure words (duca, scrito, capitanei), so it is a different sign. Taken as A it gives r07 "asaiilati" and r09 "as|aiasai pui": no word either way.
  - r07 at 4x: the second sign of the ψψ pair carries a long thin stroke running left under the L. That is a later word divider, so the pair is not the crossed N of Lasry's table. "asciilati" stays.
  - Lasry gives the m-shaped sign as L. That yields v03 "...dlcuspaeonlit...", v07 "o sfulo" and r16 "il che lur e[ω] parsa" (Lombard lur = loro?). Only r16 reads, and only with an unknown ω, so nothing is counted.
  - 48 = Saint-Pol and peu = the King, against every sibling occurrence: [48] occurs twice, both in fr. 3096 ("cum l'andata di [48]", "[48] ne crede"); [ep]/[peu] once in fr. 3045 ("servicio di [ep]"). Every context fits, but none forces the value, and no clear text names the person. Not counted.
  Result: no change, 1247/1337 = 93.3%.
- [x] sign-by-sign re-read on the new crops (5 Oct 2026; verso cut on measured centres, push/v*.png). Signs as seen:
  - r03 end `me 7 p̶ ψ 7 | a s a n`: the stroke through p is a divider. "la mia" stands, sense open.
  - r16 `rex ψ me l q d Λ m u r · d ω 7 k ne`: a bare Λ (the doubling mark) stands before "mur". The ω may be one sign with the following 7. Unresolved.
  - r30 start `ne a ψ n y d | ψ n s Λ ∂ n 7 ne`: the [v b] pair looks like Λ∂. Unresolved.
  - v01 end `... o n k ψ ▮ d θ 7 ſt`: the blot is solid. Unchanged.
  - v03 middle `Λ m l s ne ρ 7 d n m ı t ǂ ı̈ r`: the sign read as o (P) is a ρ with a long left tail (F by the sibling rule). The token file now has ρ=F?. Sense still open. The line ends "...[4r] cel|aro" (celarò, v04), already read.
  - v06 `em far q 7 s d p w ne ψ y d ψ ∂ ψ`: w = O gives "che havemo" (that we have). Counted (+1). The following "si ne[?]di" stays open.
  - v07 `o d k + ne ρ s m n 7 a k 7 s d`: the "neρ" of v03 recurs, possibly one sign. "a per o sfu[m]o" stays open.
  - Recto 10-12, 21 and 27 and verso 2, 8 and 9 were rechecked on the crops; no sign differs from tokens.txt.
  Re-measured with count_tokens.py: 1247 -> 1248 of 1337 (93.3%).
