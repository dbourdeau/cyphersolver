# Matignon's Cipher-3, BnF fr. 15571 f. 179: checked against Tomokiyo's decipherment

Catalogue item 12, the second Cipher-3 leaf. `../NOTES.md` listed it as "not-attempted; not transcribed". This
contribution is dated 6 Oct 2026.

**Result.** Method: read from an existing decipherment (Tomokiyo's interlinear), checked independently with his key.
Read in part: **473 of 509 signs (92.9%), measured**, against a shuffled-key floor of 3.5%.

**Leaf.** Gallica `btv1b90618802`, canvas 187, left page. The page is bound upside down and must be rotated 180°. It
has 21 cipher lines, all in cipher. Folio "179" is written at the top right; "191" (old foliation) is at the foot.

**Prior work.** S. Tomokiyo (cryptiana, *Henry III's Cipher with Ambassadors*) lists it as "undeciphered" but adds
"Uses Matignon's Cipher-3, which allows deciphering (see the image)". His image (`BnFfr15571f179.jpg` on cryptiana, 680 px)
carries an interlinear decipherment in magenta and margin notes on sign values: Z→o, ξ→e, n→e, t→r, X→j, L→p, ω→t.
- He never published it as text.
- The upstream `targets/matignon1586/NOTES.md` calls it "not yet transcribed or checked".
- So this leaf is in effect already read by Tomokiyo, and our work is an independent transcription and check.

**Method.**
1. Rotate, crop and deskew the page (−7.5°). The lines curve, so each was cut as a sheared strip between its
   left and right centres (`crops2/`, not included).
2. Two agents read the strips sign by sign, independently: `readA.txt`, `readB.txt`. Each had only the key
   table, Tomokiyo's margin values and the f. 276 conventions (`BRIEF_reader_f179.md`). Neither saw
   Tomokiyo's annotated image.
3. Reconcile them against the image and Tomokiyo's magenta, giving `read_final.txt`.

**Agreement and coverage.**
- **Two reads:** 472 of 516 signs agree (91.5%).
- **Coverage** (`python ../f276/scripts/measure.py read_final.txt 50`, the target's rule with the lexicon of the
  shared `lang` model `fr-1600-letters`):
  - reconciled reading after three passes: **473 of 509 signs (92.9%)** (earlier passes, with the bundled word list: 86.9%, 90.4%);
  - read A: 87.3%; read B: 89.1%;
  - shuffled keys (50): median 3.5%, max 23.8%.

**Reconciliation changes (read A → final):**
- **Line 2:** *la chose* (B; the o-shape is o here).
- **Line 3:** *[m]ande | depui[s]* (B's d; Tomokiyo).
- **Line 4:** *bruit* (B).
- **Line 6:** *resolu* (£ = o).
- **Line 7:** *ataquer* (Tomokiyo's magenta). The S-shaped sign is **q**; both readers had missed it.
- **Line 10:** *et que* (B).
- **Second pass:**
  - **Line 1:** *avec les enfans*. This is from Tomokiyo's magenta; the shapes alone are unclear.
  - **Line 14:** *grant* (B).
  - **Lines 16–17:** *escrira a Iehan* (B; the final ρ = a).
- **Third pass:**
  - **Line 1:** the final b = s (*enfans*). It was cut off by the first crop; the strips were re-cut from a wider crop
    (not included).
  - **Line 11:** *un ? long sejour*: q = l, small £ = o, y = n, 23 = g. One sign before *long* and one inside
    *sejour* are unread. This replaces the agents' *u n o l d n g*.
  - **Line 13:** *[ce]spendant que [code] ne*: the a-sign = t; the ω with an overbar is a code sign, unread.
  - **Line 18:** *employer **Lansac** en [blot] l'armée de mer*. Read B independently has *l a n s a c*. Guy de
    Saint-Gelais, seigneur de Lansac, was vice-admiral of Guyenne and governor of Brouage.
  - **Line 12:** *premier que remectre*. Read A's extra *e s* is not on the image; read B agrees.

## Clear text (16th-c. spelling; word division ours; […] unread, [?] doubtful)

> Frontin s'acomodera avec les enfans de la Rousiere, comme la chose lui a mandé. Depui[s] est dit resolu aller
> en [Q]uercy[?], mais le bruit qui a couru que c'estoit pour aller voir la Croix l'en a destourné. Il est
> maintenant resolu [d']ataquer Pons; il se poura prendre en ung mois. Je crains fort […] que la maladie qui est
> entre nos [g]ens de pied n'augmente, et que apres le siege il ne faille un […] long sejour premier que remectre
> l'armée en estat de servir, cependant que [code sign] ne gaigne grant pied en la Guascongne. La responce que nous
> fera o[n …] rendra tous sages. L'on escrira a Iehan Durant pour employer Lansac en […] l'armée de mer; il n'y est
> propre. Le commandeur de la D[…] y pourroit servir[?].

**English, loosely.**
- **Frontin and la Rousière:** Frontin will come to terms with La Rousière's children, as the matter has been sent
  to him.
- **The route:** he was said to have resolved on going into Quercy[?]. The rumour that it was to go and see la Croix
  turned him from it.
- **Pons:** he has now resolved to attack Pons, which could be taken within a month.
- **Sickness in the army:**
  - I much fear that the sickness among our foot will spread.
  - After the siege, a long rest would then be needed before the army could serve again.
  - Meanwhile [code: a person] would gain ground in Gascony.
- **The reply:** the answer we are given will make everyone wise.
- **The sea army:** Iehan Durant will be written to, to employ Lansac in … the sea army. He is not suited to it; the
  commandeur de la D… could serve there.

**Context (to verify).**
- **Names shared with f. 276:** Iehan Durant and La Rousière, so the two leaves belong together. Both concern
  Poitou and Saintonge in 1586.
- **A plausible fit, not established:**
  - the sickness and the siege fit the plague in Mayenne's and Matignon's army round the siege of Castillon
    (Aug–Sept 1586);
  - "ataquer Pons" (Saintonge) and Navarre gaining ground in Gascony fit the same campaign.

## Open

- **Line 8:** the sign after *fort*: a heavy C without n, maybe *que* or a null.
- **Line 11:** one sign before *long* and one inside *sejour*.
- **Line 13:** the ω-with-overbar code sign, probably a person (Navarre?).
- **Line 13:** *en esta[t]* and *[ce]spendant*: the sign shapes are uncertain.
- **Line 18:** the blot after *en*.
- **Line 20:** *de la D[…]use* and *po?urroiet*.
- **Not yet done:**
  - a line-by-line comparison with Tomokiyo's magenta at higher magnification (his image is only 680 px);
  - the historical check (Castillon, Pons, Frontin, the commandeur).
