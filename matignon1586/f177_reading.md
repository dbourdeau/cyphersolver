# fr. 15571 f. 177 — Forget, 31 December 1585: Mayenne's plan for Gascony, in the solved cipher

Canvas 185 right of fr. 15571 (ark `btv1b90618802`). An archivist's hand heads the leaf
*"31 decemb. 1585"* and summarises it: *"Lettre de Mr Forget … Pons ou Taillebourg, mais le Vicomte
de Turenne ayant paru en campagne avec gens et canons, on a changé d'advis, et résolu d'aller en
Gascogne où Mrs du Mayne et de Matignon devoient [commander]"*, with a second note at the foot:
**"Dessein de Mr du Mayne pour la conduitte de son armée en Gascogne et les difficultez qui s'y
rencontrent."** Four clear lines, then 29 lines of cipher (counted on the image 22 Sept; "28" earlier), of which 24
are transcribed. Measured coverage (`measure.py`): 24% of transcribed tokens, 20% of the leaf.
Transcription in `f177_cipher.txt`, decoder output in `reading_f177.txt`.

## This leaf is in the solved cipher

That was not obvious — the catalogue lists fr. 15571 ff. 177, 179 separately from the fr. 15572
leaves, and two of the fr. 15572 leaves turned out to use other keys. The test that settled it:
line 3 decodes as *"…que **indubitablement** l'on…"*, and of the fifteen figures spelling that word
**twelve are keyed**, giving `in?ubita?l?ment` before the model contributes anything. The code
`14` = **que** fires twice in the same three lines. A wrong key does not produce a fifteen-letter
French adverb out of keyed figures.

## The reading

Fragments, not continuous text — about a third of the words:

> … que **indubitablement l'on** … **advertir** … **vostre** … **en grand** … **de nostre** …
> **il y va de tout cela** … **l'on dist** … **nous** … **descen[dre]** … **des commun[s]** …
> **M[onsieu]r de Matignon** … **qui seroit** … **recourir … ce qu'il veut** … **dit que nous** …
> **le dit sieur de M**… … **estoit** … **forcer** … **l'amitié des** …

The subject matches the archivist's note: Mayenne's design for the conduct of his army into
Gascony, and the difficulties in the way of it.

## Coverage, honestly

Lower than on the fr. 15572 leaves — this hand is smaller and I read its figures less reliably, so
the transcription carries more noise. What is established is the *key*, and two proper names
(Matignon, and a "sieur de M—"). A careful re-transcription would raise the yield; the cipher is
not the obstacle.
