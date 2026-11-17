# Notes on the interlinear gloss, ASF MAP LXXIV doc. 114

Files: gloss.tsv (per line), gloss-by-block.tsv (generated from gloss.tsv), signs.md (glossed signs and crops), sign_*.png and context_*.png (crops from raw/).

## Conventions in gloss.tsv

- `[..]` expands an abbreviation that is written abbreviated in the ink: ch[e] (ch with a 3-shaped stroke), no[n], co[n], i[n], ca[m]pare, q[ue]llo, p[re]se, p[er], v[ost]ri.
- `&` is the gloss's et-sign (a small tironian/ampersand-like mark). It is never written out as "et" or "e".
- `(?)` follows the uncertain letter or, at the end of a word, marks the whole word. `[…]` is illegible ink.
- S. M.ta, S.ri, D. are written abbreviated with raised letters, as shown.
- Word division follows sense; the ink often runs article and noun together (elRe, dlDuca, laltre, daffectione, dorliens).

## Resolution limit (read this first)

The source images are 1272 px wide and that is the largest size the archive's image server returns. Gloss letters are 4-6 px tall and sit on JPEG block edges, so upscaling adds nothing. Whole words are almost all recognisable; individual letters often are not. In particular the image CANNOT decide:

- **e vs i** in short words: every "el" may be "il" and the reverse. I give "el" throughout except L5 where "il" looked better. Do not use this file as evidence for el/il.
- **single vs double consonants** inside a word where the letters are minims or small bowls (pezo, careze, racomandava, glene, amicitia are single as far as I can see, but each is one pixel-column from the double form).
- **c vs ch** before a/o (careze/chareze, picolo/picholo, racomandava/rachomandava).
- **-e vs -i** endings (dimostrazione/-i, havere/haver).

Where I could, I checked a doubtful spelling against the number and identity of the cipher signs underneath (same sign recurring for the same letter elsewhere in this document). That is internal evidence from the cipher line, not from the key: key-46dec7b.json, the transcription-*.tsv files, aligned-signs.tsv and result-desjardins.txt were not opened. The spellings that lean on the cipher count rather than on gloss ink alone are: ristrignetevi (g before n), partita, careze, dimostrazione (z, and final -e), daffectione, glene, figlo, lharebbe, tenessi, amicitia, Sampolo, dorliens, mandorono. For those, the gloss ink is compatible with the form given but would not by itself exclude the neighbouring form; each carries (?) in gloss.tsv for that reason. Anyone scoring a decipherment against gloss.tsv should treat agreement on these words as circular.

## Legibility by line

| leaf | line | grade | remark |
|---|---|---|---|
| c258v | 14 | good | |
| c258v | 15 | good | "ristrignetevi" long word, middle letters blurred |
| c258v | 16 | fair | "importantia" is a row of minims |
| c258v | 17 | good | one word |
| c258v | 19 | good | "co" before p[re]fati: cannot see whether it carries a nasal stroke |
| c258v | 20 | good | two short glosses, one per block |
| c258v | 21 | fair | a small crossed mark between "quanto" and "uno"; last word begins with a wide x- or z-like letter |
| c258v | 23 | good | |
| c259v | 3 | good | |
| c259v | 4 | good | "el D." has a small mark over the D, not read |
| c259v | 5 | fair | picholo / figluolo / el quale are squeezed |
| c259v | 6 | fair | "intendendo" blurred |
| c259v | 7 | fair | glene, racomandava doubtful in detail |
| c259v | 8 | fair | first word (tenessi) poor |
| c259v | 9 | fair | lharebbe, figlo |
| c259v | 10 | fair | careze, dimostrazione |
| c259v | 11 | good | |
| c259v | 12 | poor in one place | one word after "sera" illegible, see below |
| c259v | 13 | fair | pezo, partita |
| c259v | 14 | good | |
| c259v | 15 | good | |
| c259v | 16 | good | |
| c259v | 17 | good | one word struck out |
| c259v | 18 | fair | "cose" small |
| c259v | 19 | good | |
| c259v | 20 | good | |
| c259v | 21 | fair | |

## Coverage

- Every cipher line carries gloss: c258v L14-17, 19, 20 (two separate glosses, one for each block), 21, 23; c259v L3-21.
- Each gloss run ends in a long horizontal rule drawn out to the right, EXCEPT c259v L21 (the last cipher line), where the gloss simply ends after "confortare" with no rule that I can see.
- The gloss occupies only the left part of the interlinear space because it is written much smaller than the cipher. It still accounts for the whole cipher line beneath: line by line the gloss stops at the word where the cipher line stops, except that the gloss never splits a word. Where the cipher breaks a word across lines the gloss writes the whole word on one line (for example offerirli complete on c259v L4 while its last signs are at the start of L5; tanto on c258v L16 while its signs open L17; malato on L3 while its last two signs open L4; duchessa on L13 and L16 while its last signs open L14 and L17).
- Signs with no gloss equivalent: a recurring tall sign with a raised circle (with a 9-shaped companion) at sense breaks, and the 9-shaped sign beside some Re/Duca signs. Details and positions in signs.md section 4. They look like nulls or punctuation. No other un-glossed cipher was found.
- **c259v L3: the cipher probably starts later than masked/blocks.md says.** The marks at x~420-495 that follow "E m'ha affirmato" look like clear text in abbreviation, not cipher: "ch[e]" (slanting first stroke, small c/r, then a tall crossed 3-like stroke) and "q[ua]n[do]" (q, n, with a stroke above). Evidence: (1) they carry no gloss, and the gloss starts with "Re" directly over the Re sign at x~520; (2) the letter-writer's own clear-text "che" elsewhere has the same build (compare context_c259v_L03_che_quando_clear.png with context_c258v_L17_clear_che.png, the "che" of "le cose che corrono"); (3) the print has "che, quando" at exactly this point. The comparison is between two blurred 15-px words, so this is probable, not proven. If it holds, block 5 opens "Re fu a visitare..." and the first four or five marks of the block are not cipher signs.
- The undecided marks in masked/manifest.tsv: the L3 smudge at x 890-925 is the raised 3 of the Duca sign; the L20 kept patch at x 936-956 is the raised c of the Re sign; the raised two-sign marks on L4, L13, L16 are the superscript "ta" (see signs.md).
- c259v L3 has an interlinear "ha" with a caret above the clear words "E m [ha] affirmato". It is a correction to the clear text, not gloss.

## Unresolved places

- **c259v L12, after "la sera"**: a word of about six or seven letters, crossed by a cipher descender from the line above, illegible (it could be a first attempt at "di nocte" or something like "dipoi"). It is followed by "di nocte" in visibly paler, browner ink than the rest of the gloss. The cipher underneath has nothing between the signs for "sera" and those for "di nocte". Likeliest explanation: the glossator's "di nocte" was spoiled and rewritten, but I cannot prove it.
- **c259v L17, after "mandorono"**: one short word heavily struck out, illegible. The cipher has nothing corresponding.
- **c258v L21, between "quanto" and "uno"**: a small crossed stroke. Possibly a cancelled false start, possibly the tail of a cipher sign from the line above. The cipher has nothing between "quanto" and "un(o)".
- **c259v L4 "el D."**: the mark over the D may be a raised "ca" (D[u]ca); not legible.

## Differences from the Desjardins print that matter

Block 1
- Gloss "ristrignetevi" (g before n; the cipher has the same order); print "ristringetevi".
- Gloss "co[n] v[ost]ri"; print "co' vostri".
- "piero" is spelled out letter by letter in the cipher; there is no name-sign for him.

Block 2
- Gloss "i[n] dilectione & amore co(?) p[re]fati cittadini"; print "in dilezione e amore coi prefatti cittadini". Single t in prefati (cipher agrees). I see "co", not "coi"; the cipher has two signs (c, o) there.
- "voi" is a single sign (upright H).

Block 3
- Seen in the gloss ink: the last word begins with a wide x- or ss-like letter (exercito / essercito); print "esercito". Inferred from the cipher: a single sign stands there which elsewhere stands for "ss" (passerebbe, tenessi, duchessa), which favours "essercito" for the cipher.
- Seen in the gloss ink: "uno". Inferred from the cipher (tentative): only two signs, u-n.

Block 5
- The print's "che, quando" is clear text, not cipher (see Coverage).
- Gloss "Re" with no article at the start; print "il Re".
- Second duke: gloss "el D."; print "il duca".
- Gloss "S. M.ta"; print "Sua Maestà". The cipher itself is abbreviated: sua + M with raised "ta".
- Gloss "haver ch[e] offerirli"; print "avere che offerirgli".
- Gloss "se no[n] il suo picholo figluolo el quale"; the print continues "il quale si", but "si" is the clear word in the margin at the start of L6 ("si trovava"), not part of the cipher or gloss. reference-desjardins.tsv block 5 therefore ends one word too late ("si").

Block 6
- Gloss "glene racomandava" (as far as legible; cipher spells g-l-e-n-e and r-a-c-o-m-); print "gliene raccomandava".
- Seen in the gloss ink: "& p[re]gavalo" ends L7 and L8 opens with one word of six or seven letters ending -ssi, then "p[er] suo"; there is no room for a separate "lo" before it. So the gloss has ONE "lo" where the print has "pregavalo lo tenessi". The cipher agrees (a single l-o between the signs for pregava and tenessi). The first letters of "tenessi" themselves are poor.
- Gloss "li dixe lharebbe"; print "gli disse lo arebbe".
- Gloss "figlo" (twice: L9 and L14; cipher f-i-g-l-o both times); print "figliuolo".
- Gloss "molte careze & dimostrazione daffectione". Seen in the ink: a letter with a descender (z) after "dimostra-", and "daffectione" as one word. Inferred from the cipher, not readable in the ink: singular "dimostrazione" by the cipher's final sign (the same sign that ends "electione", "dilectione"); print plural "dimostrazioni". The z of dimostrazione and careze is a z in the cipher (same sign in both, different from the t-signs), whereas affectione, electione, dilectione are spelled c-t-i.
- "partita" is INFERRED FROM THE CIPHER (p-a-r-t-i-t-a, the same t-sign twice); in the gloss ink the word is "parti?a" and I cannot tell t from v. Print "partiva". If right it changes the sense slightly ("once His Majesty had left").
- Gloss "p[er] buono pezo"; print "per buono pezzo".
- Gloss "del Duca dorliens": here Duca is SPELLED OUT in letter-signs (d-u-c-a), not written with the Duca sign; that sign is evidently reserved for the Duke of Milan. Print "duca d'Orléans".
- Gloss "Sampolo"; print "San Polo".
- Gloss "mandorono"; print "mandarono".
- Gloss "q[ue]lli S.ri"; print "quelli signori". Abbreviated in the cipher too.
- Gloss "infra laltre cose li dixono"; print "in fra le altre cose, gli dissono".
- Gloss "ch[e] el Re suo padre": this Re is a different sign (slanted H with two bars) from the Re of the rest of the passage (2 + raised c), which fits the sense: the first is the duchess Isabella's father, the second the French king.
- Gloss "amicitia col Re"; print "amicizia col Re".
- Gloss "pero esser parole"; print "però essere parole".
- Extra ink the print does not have: the illegible word on L12 and the struck-out word on L17 (both probably the glossator's own slips).

Spelling pattern overall: the gloss (and the cipher) keep -ctione/-tia, h- in haver/harebbe, x in dixe/dixono, single consonants where the print doubles, and "&" for the conjunction.

## Confidence

- Wording (which words stand in the gloss, in what order): high for every line except the three unresolved places above.
- Letter-for-letter spelling: moderate. Roughly four words in five I would stand behind as spelled; the rest are flagged with (?) or fall under the e/i, single/double and c/ch limits stated at the top.
- Sign identifications in signs.md: Re (2 + raised c), Duca on L3 (2 + raised 3), che (B), non (arch with dot), et (curl), voi (upright H) are secure. The raised letter of the Duca sign on L4 and the exact form of the second "Re" sign on L19 are not.
- This was a single reading made with the print open as a guide to sense. It has not had an independent blind re-read.
