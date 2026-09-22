# Guise? to the duc de Mercœur, 27 May and 20 June 1587 (BnF fr. 15564 ff. 119, 142)

Catalogue entry "Unknown sender to Philippe-Emmanuel, duke of Mercoeur ?", DECODE R4162 (f. 119) and R4165 (f. 142).
Session 2026-09-22.

Status: read (95.1% of letter signs, measured; key: Lasry 2022, extended)

## Prior art

- DECODE lists both records as "Non-decrypted" (records created 20 Feb 2023, BnF images, login).
- George Lasry solved the cipher of the letters to Mercœur in fr. 15564 ff. 27, 78, 119, 142 (and fr. 15565
  ff. 105, 122) and published the **key table** only (cryptiana `code/GL.htm`, "Duke of Guise? in BnF fr.15564 and
  fr.15565", image `GL/GL_BnFfr15564.png`, dated 29/05/2022), plus a decipherment overlay of f. 27 alone
  (`GL/GL_BnFfr15564f27decipher.png`). No plaintext of ff. 119 or 142 is published there or on DECODE, as far as
  I found. So the key existed; the texts had not been read out in public.
- A peer session is working on the neighbouring folios (ff. 27, 30, 78, 151) in `mercoeur1587/`; this folder holds
  only ff. 119 and 142.

## Sources

- Gallica fr. 15564 = `ark:/12148/btv1b9064027v`. **f. 119 = view 132, right half** (a full page wholly in cipher,
  44 lines, dated below "Ce xxvij^e May 1587"). **f. 142 = view 155, right half** (a slip: seven clear lines, then
  16 lines of cipher, dated "Ce xx^e Juing 1587").
- Crops (git-ignored, in `img/`): re-fetch with
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9064027v/f155/4400,4150,4535,1750/full/0/native.jpg` (f. 142 cipher)
  and `.../f132/4800,650,4135,4400/full/0/native.jpg` (f. 119).

## System

Lasry's key: homophonic substitution, 2–7 signs per letter (cursive letter-forms, digits, Greek-like shapes), a
small nomenclator of ff-ligature groups for common words (DE AU LA ET DES QUE LES MON LE QUI POUR PAR VOUS NOUS
LEUR SON), and digit groups for names (his "Unknown" row: 21, 71, 73, 89 …). No word division.
Several signs are near-identical shapes with different values (loop = A or S; C-shape = L, R or F; slash = A, C or P);
the reading resolves them word by word.

## f. 142, 20 June 1587

Clear part (my reading): the writer has been assured of what passed at the interview of the Queen Mother with the
King (?), and gives news "que nous avons d'Allemagne: que le duc de Lunebourg avec neuf mil chevaulx sera sans
faulte sur le bord du Rhin le xx^e de juillet ou le douziesme, … xy Suisses et xy lansquenets pour …", then cipher.

Reading of the cipher: `f142_reading.txt`. In outline: the writer's party says a levy (of the King?) is well
advanced, that within six weeks there will be [a] levy of a thousand lances and four thousand reiters, "qui est ung
instable secours"; that because of hasty resolutions "nous sommes maintenant contraincts de donner ordre a nos
affaires, qui ne peuvent estre avec telles seuretez que si nos premiers desseings eussent esté effectuez avec ordre et
mesure"; that "dans cinq ou six jours j'espere avoir resolu … la chose … avec [73]", with "les forces qui seront
necessaires allant la trouver a Meaux"; closing "ne faudrons de vous mander toutes nouvelles et vous baise tres
humblement les mains".

## Result

**Read.** Both letters read with Lasry's key, applied sign by sign over a transcription pinned against the images:
f. 119 1,861 signs, 84 unread (95.5%); f. 142 623 signs, 44 unread, 7 of them name/code groups (92.9%; 93.9% of
letter signs). Together 2,477 letter signs, 121 unread: **95.1%**, measured from `f119_reading.txt` and
`f142_pinned.txt` (the `|| total unread` column). Open codes: [21] (twice), [43], [71], [73] (twice), [N], [&],
[9b], [ffv], [ffσ], [ffx], [ffou] - Lasry's "Unknown" row, names not identified.

Method: first-pass sign labels -> beam search over the key's homophone candidates with the fr-1600-letters 5-gram
(`beam.py`, `bl.py`, `bl2.py`) -> line-by-line relabelling at 2x zoom with pinned letters (`'x` in the label files;
`merge_pins.py`, `merge142.py`), about twenty agent passes of three lines each, then a wordlist/phrase search over
candidate classes for the last runs. Key extensions over Lasry's table (same hand): y = D / "de"; ✝ = Q; ɤ = D, T or
X; x-shape = Y or N; 3/ʒ = C or D; 8 = M, B, N or T; 6 = E or R (dotted Є = R); k/ℓ = A; "=ʃ" = P.

## f. 119, 27 May 1587 (DECODE R4162)

Reading: `f119_reading.txt` (per line: reading || signs unread). In substance: the writer has Mercœur's letter and
the report of his army; "comme nous avons resolu de nous y gouverner"; the levy of reiters is assured, and by
August "nous avrons sans doubte deux mil lances italiennes ou albanoises et quatre mil reistres, soubs la levee [de]
ce [que] [21]"; "il a envoyé son secretaire vers … le colonel Fifer [Pfyffer] avec douze mil escus pour arrester et
traicter d'une levee de neuf mil suisses, auquel nous n'avons eu encore response et l'attendons a toutes heures";
the said duke [21] "s'est aussi resolu" to raise a thousand five hundred men; Flanders(?), "ses parans et amys";
"l'armée des heretiques … composée d'huict mil reistres, douze mil suisses, deux regimens de lansquenets, quatre
mil harquebusiers pour Chastillon", who is to bring French cavalry; "si nous ne nous resolvons a nous en defaire,
ce qu'est tant utile pour la gloire de Dieu et la cause que nous poursuivons de mon costé, il ne fault espargner
rien, soing ny diligence"; the general and particular reputation, "la conservation particuliere de nos amys"; "c'est
un grand malheur … eschauffé davantage, et que sur luy l'on ne peult prendre plus ferme fondement"; the towns "des
partisans" and [71] "et son frere"; "je vous ay desia mandé"; "vous baise bien humblement les mains".

## f. 142, 20 June 1587 (DECODE R4165)

Reading: `f142_reading.txt`. After the clear news (Lunebourg with nine thousand horse on the Rhine by 20 July,
Swiss and lansquenets) the cipher says someone "iusques icy a esté tousiours se monstre incredule"; the levy that
was to be so far advanced is not, "il n'a plus de six semaines"; "la levée de mil lances et quatre mil reistres,
qui est ung instable secours"; "nous sommes maintenant contraincts de donner ordre a nos affaires, qui ne peuvent
estre avec telles seuretez que si nos premiers desseings eussent esté effectuez avec ordre et mesure"; "dans cinq ou
six jours j'espere avoir resolu la chose … avec [73], les forces qui seront necessaires allant la trouver a Meaux, ou
il m'a donné … aller veoir"; "je ne faudray a vous en mander toutes nouvelles".

## Remaining gaps
- scattered unread letter signs, 121 of 2,477 (4.9%), no run longer than 8 - blocker: open-codes; each tried in three or more zoomed passes plus a candidate-class phrase search over the French corpora; several look like code pairs (98, 89, z3) rather than letters
- name codes [21] [43] [71] [73] [N] [&] [9b] [ffv] [ffσ] [ffx] [ffou] - blocker: open-codes; Lasry's key leaves them unidentified and they occur once or twice

## Escalation
- [x] siblings: the other fr. 15564 records (ff. 27, 30, 78, 151) worked by a peer session in `mercoeur1587/`; neighbouring leaves looked at, no decipherment
- [x] clear-pages: f. 142's clear part is the letter's own opening, not a decipherment; f. 119 has none
- [x] known-keys: Lasry's fr. 15564 key is the key and fits both letters
- [x] print: cryptiana GL.htm gives the key and an f. 27 decipherment only; no printed text of ff. 119/142 found
- [x] key-rebuild: key extended from what reads (beam over widened candidates, per-sign relabelling, 13 new sign values listed above)
- [x] retry: every unread run retried with the extended key in three rounds, with a wordlist phrase search
