# Second reading, Brienne 13 copies (target maisse1593)

11 Nov 2026. Independent second reading of the clear copies in Brienne 13 (BnF NAF 6984, Gallica btv1b100904592), made blind from the full-size images in `sources/raw/repo_help_2026-11-11/maisse1593/brienne/`, then collated with the first readings.

## What was read

- `brienne_172r_173v_r2.txt`: Henri IV to Maisse, Chartres, 8 Feb 1593, from the line containing "Le surplus de voz lettres" (fol. 172r, b177 right) to "priant Dieu" (fol. 173v, b179 left). 86 lines.
- `brienne_193v_196r_r2.txt`: Mantes, 28 Apr 1593, from the line containing "L'experience" (fol. 193v, b199 left) to "priant Dieu etc." (fol. 196r, b201 right). 145 lines.
- Folio numbers 172, 173, 194, 195 and 196 checked on the rectos.
- Both files were hashed into `SHA256SUMS` before any first reading was opened. They have not been changed since.
- Correction to their headers: the excerpt on fol. 172r starts on line 21 of 28, not line 15. The excerpt on fol. 193v starts on page line 23 (counting the three heading lines), not line 19. In `collation.tsv`, line numbers count from the top of each folio on that basis.

## Collation

The collation compares with WAINUT's `f406_brienne_copy.txt` (fol. 172r–172v part), `f410_brienne_copy.txt` (fol. 193v–194r part), and `brienne_173r_173v.txt` and `brienne_194v_196r.txt`. Line counts match folio by folio. There are no line-break disagreements.

`collation.tsv` lists 66 disagreements, one row each:

| kind | rows | settled on the image [V] | open |
|---|---|---|---|
| word | 35 | 33 | 2 |
| spelling | 27 | 27 | 0 |
| abbreviation | 4 | 3 | 1 |
| line break | 0 | – | – |
| **total** | **66** | **63** | **3** |

The first readings and the second reading follow different conventions, and those differences are not listed word by word. They are counted on five summary rows at the end of the TSV: accents (37 tokens), u/v (100) and i/j (1), capitals (46), apostrophes (32) and punctuation (12). The first readings print the copy's acute marks and modern v/j. The second reading drops all accents, as the brief asked, and keeps the copy's u/v.

Of the 35 word rows:
- 20 go against the first reading (wrong word, or a word left as [?], left out, or normalised to the expected sense).
- 10 go against the second reading.
- 3 go against both readings ("Aiant neantm.", "Au moings", "viuement").
- 2 are open or only partly settled.

Most spelling rows favour the second reading. The exceptions are "touttes/Touttesfois", where the copy has double t and the second reading had single t, and "Chaous", "cogneu", "guieres", "toucheroit" and "L'asseu-", where the first reading's letters were right.

## Still open

1. Fol. 172v, line 24: "i'ay besoin d'en fe.[?] / vn a tours". "fe" carries a superscript, probably "faire" ("d'en faire vn [voyage] a Tours"). The first reading has [?] here.
2. Fol. 193v, line 24: "vous ne vous estes este[?] en rien trompe". It is a copyist slip either way, and the second word may be "este" or "estre".
3. Fol. 194v, line 24: "agrandir[...] merite". The image shows no "le" before "merite". The verb ending (-ent / -oient / -ont) is unclear.

## Errors in the first readings that matter for sense (settled on the image)

- Fol. 195r, line 28: "aux presens de Leuant", not "aux pensions de Pisani". The 20,000 escus were for the Levant presents.
- Fol. 194r, line 17: "s'aduancent ou recullent" (the first reading is right here; the second had "ouuertement").
- Fol. 194r, lines 16 and 18–20: "luy veullent persuader" (not "voudront"); "le grand duc luy enuoiera" (not "leur"); "Au moings quilz n'ayent" (not "A[insi?]"); "de moy de laffection", where the "de" is interlined above the line.
- Fol. 194v, lines 11–12: "Je croy que la resolution a este bonne d'en faire enleuer Lancosme" (not "Je voy ... retirer").
- Fol. 195r, line 26: "le secours qui vous auoit este enuoye" (not "le service").
- Fol. 195v, lines 5–6: "pour Gien-/ne pour vne fois seulement" (not "bien-/tost [?]"). The initial is the same G as in "Gondy". Which place is meant is not settled here.
- Fol. 195v, line 23: "tres aise" (not "bien aise").
- Fol. 196r, line 10: "viuement ambrasse par le Commung" (the first reading is right on "viuement").
- Fol. 173r, line 4: "J'ay donne le terme a ma noblesse" (not "le temps").
- Fol. 173r, line 11: "Comme ont volontairement offert ceux qui sont pres de moy" (not "Comme ilz m'ont").
- Fol. 173r, line 28: "Orez que ie n'eusse" (not "Or ce que").
- Fol. 173v, lines 2 and 11: "Apres l'ouuerture de laq.lle" (not "et pour l'ouverture"); "Et y a ce pendant" (not "Il y a").
- Fol. 172v, line 10: "Aiant neantm. faict entendre" (the first reading has "et i'ay neantmoins[?]"; the second had "Neant neantm.").

The second reading's own word errors were all corrected by the first readings: "pourroit" for "pouuez", "nomme au" for "nouueau", "aurez" for "auez", "seruice" for "secours" (172v), "que" for "queux", "ouuertement" for "ou recullent", "&" for "de", "de vous ouurir" for "et vous ouure", "touchoit" for "toucheroit" and "vniuersellement" for "viuement". In the TSV, each of these has the image reading as its settled reading.

One reading stands as written although the sense wants something else: fol. 194r, line 27 has "tout ce qui pour seruir", where the sense wants "peut".

Nothing was posted, pushed, emailed or committed. No other file in the maisse1593 folders was opened.
