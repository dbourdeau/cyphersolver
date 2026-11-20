# Richelieu → M. de Rancé, cipher letters of July 1629 (BnF Français 3829, ff. 87 & 89)

**Outcome:** alphabet fully recovered by ciphertext-only cryptanalysis from Tomokiyo's transcription, then
found to agree word-for-word with a decipherment already printed in 1858 by D.-L.-M. Avenel, *Lettres,
instructions diplomatiques et papiers d'État du cardinal de Richelieu*, t. III, nos. CXCIX (p. 368, f. 87) and
CCV (p. 381, f. 89). Avenel had "recomposé" the key from deciphered documents in the Archives des Affaires
étrangères (his note 2, p. 262). So the cipher is **not** unsolved — it was solved 168 years ago and the
fact was missed by the modern lists. Our independent result is a verification of Avenel, not a first.

Status before this work: listed as unsolved by S. Tomokiyo (cryptiana, "Unsolved Historical Ciphers",
updated 6 Sep 2026) and DECODE R9461/R9462 ("Non-decrypted"). Worked from Tomokiyo's transcription
only (manuscript images not publicly available: BnF fr.3829 is not on Gallica; DECODE images need login).

## Cipher system

Homophonic substitution, two-digit figures, with a small nomenclature.

| Symbol | Letter | Symbol | Letter | Symbol | Letter |
|---|---|---|---|---|---|
| 10 | c | 17 | f | 24 | m |
| 11 | b | 18 | t | 25 | s |
| 12 | g | 19 | a | 26 | u/v |
| 13 | p | 20 | d | 27 | e |
| 14 | l | 21 | i/j | 28 | q |
| 15 | o | 22 | n | | |
| 16 | r | 23 | h | | |

- 10–28 = the 19 letters a b c d e f g h i l m n o p q r s t u in a scrambled order (no x y z observed).
- 29 30 31 32 33 = a e i o u and 34 35 36 37 38 = a e i o u — two extra homophone sets for the vowels
  (33 = u confirmed by Avenel's "ne piquer" = 22 37 13 21 28 33 30 16).
- **Tilde/diacritic = doubled letter**: ~14 = ll, ~22 = nn, ~25 = ss, ~30 = ee (d'e**ll**e, bo**nn**e, do**nn**er, Bra**ss**ac, amba**ss**ade, maitre**ss**e, men**ee**).
- 39 = "et" (corrected 23 Oct 2026 from Avenel: *frontière et menée*, *Chevreuse et autres*; earlier read as a in "amenée"); 40 = "de", 42 = "la" (word codes).
- ≥41 = nomenclature. Identified (this work + Avenel's footnotes across vol. III):

| Code | Meaning | Code | Meaning |
|---|---|---|---|
| 51 | le Roi | 60 | Mme de Longueville |
| 52 | la Reine mère (Marie de Médicis) | 66 | le cardinal de La Valette |
| 54 | Monsieur (Gaston d'Orléans) | 83 | l'Espagne / le roi d'Espagne |
| 58 | la duchesse de Chevreuse | 84 | l'Angleterre |
| 59 | la princesse Marie (de Mantoue) | 92 | la Lorraine |

  Cleartext jargon also used: *Castor* = le Roi, *Lysandre* = la Reine mère (Avenel).

  The full key, with its Nov 2026 extension (41 = *que* and nine more names from Avenel's notes on the sibling letters
  of Feb-May 1629), is `texts/key.md`; that file, not this table, is the key of record.

## Cribs that broke it (in order)

1. `14 19` before/after *de, pour, bien que* → **la**.
2. `20 19 26 18 16 30 25` → **d'autres** (fixed d a u t r e s and showed 30 = second e).
3. `20 27 ~14 35 … 30 ~14 35` after *tousjours pour l'amour* → **d'elle … elle** (tilde = doubling).
4. `11 16 19 ~25 29 10` after *Mr de* → **Brassac**; `14 19 24 11 29 ~25 34 20 27` after *pour* → **l'ambassade**.
   → "j'ay proposé au Roy Mr de Brassac pour l'ambassade de Rome". Jean de Galard de Béarn, comte de
   Brassac, in fact became French ambassador in Rome in 1630 — independent historical confirmation.
5. Remaining letters from *huit cens, la paix, esprits, secrete, se face, Vincennes, frontiere, Bonneuil*.

## Reading (Avenel's fuller transcription, with the codes resolved; our reading agrees everywhere)

**f. 87 — À M. de Rancé, Saint-Privat, 7 juillet 1629 (Avenel CXCIX)**

> [Le Roi] est fort en colère de l'action *de Boneuil*. Il remet à [la Reine mère] *de le chasser* comme elle
> l'estimera à propos; si l'affaire est certaine, il mériteroit *pis*. Castor [le Roi] voudroit bien que
> la [duchesse de Chevreuse] peust estre *attrapée près de la frontière et amenée au bois de Vincennes*,
> auquel cas il faudroit que personne *de dehors ne la vist*. *Les cabales de* [la Lorraine] avec
> [l'Espagne] par le moyen de la [Chevreuse] et autres sont insupportables. La paix aura surpris
> *ces esprits malins*. … J'eusse volontiers servy Mr *Vautier*, mais l'abbaye estoit de longtemps promise
> à [La Valette]. … J'ay parlé à *Marcheville* de ce que *Andreni* [d'Andemy] a dit; il le nye tout à
> fait … contre le service de [le Roi]. … Et si [l'Espagne] s'en plaint …

**f. 89 — Pour M. de Rancé, mi-juillet 1629 (Avenel CCV)**

> Nous sommes en peine de quoy *la paix de* [l'Angleterre] ne s'achève point … [Le Roi] est d'advis que
> [la Reine mère] prépare une armée pour *la Champagne de dix mil hommes et huit cens chevaux* …
> [La Reine mère] doibt, renvoiant ce gentilhomme de [l'Angleterre], luy escrire des lettres obligeantes et
> pleines *d'amour*, et qui disent … que [la Reine mère] *se portera* tousjours, pour l'amour *d'elle ainsy
> qu'elle* l'en a prié, à *une bonne union entre* [le Roi] *et* [l'Angleterre]. [La Reine mère] peut passer
> jusques là de dire qu'elle peut l'asseurer qu'outre *l'évesque et les prestres* qui doivent estre *près
> d'elle*, il ne voit pas qu'on ait dessein de luy *donner d'autres François que* ceux qui sont *près
> d'elle*; mais il faut que ce soit *une lettre secrète*, ou bien le dire en grande confiance à *Vantelet*
> qui aura créance par *la lettre de* [la Reine mère] … luy recommandant de *ne le dire qu'à sa
> maistresse*; et cependant il *le dira aux* autres, qui est ce qu'on *doit désirer*. Il est *à souhaiter
> que cette paix se face et* promptement.
> J'ay proposé au roy Mr de *Brassac pour l'ambassade de Rome*. Vous sçaurez de [la Reine mère] si elle
> aura agréable cette proposition … vous irez trouver ledit Sr de *Brassac* … la proposition que j'ai
> faite *au roy* de luy … s'asseurer *des meubles* qui luy sont nécessaires pour cet *ambassade*.

"Elle" / "sa maistresse" = Henrietta Maria, Queen of England (Louis XIII's sister), whose French bishop
and priests had been expelled by Charles I — the peace of Susa (24 Apr 1629) was being finalised.

## 23 Oct 2026: re-reading (REREAD_BRIEF, batch b33)

The reading audit of 22 Oct had left the key decode of Tomokiyo's partial transcription *decoded, not read* and
Avenel's text only as an excerpt. Avenel nos. CXCIX and CCV were transcribed in full from the Google Books page images,
with his printed figures (`texts/ff87-89_avenel_figures.txt`); every figure run decoded with the key gives his footnote
decipherment (`research/reading_audit/b33_rl_decode.py`). Figure 39 is *et* (both occurrences), not *a*. Three places
were checked on the DECODE scans (R9461, R9462): the clerk left out the *a* of *au bois* (Avenel's `16` there is a
misprint), and f. 89v reads *la proposition que j'ay faite a 51 30 18 52* (*au roy et à la reyne mère*), where Avenel
printed only `51`. Running reading `texts/ff87-89_reading.md` (English `texts/ff87-89_en.md`, log
`texts/ff87-89_reread_log.md`): 0.83 clean sentences (b17, fr), 0.97 counting explicit holes only, one hole ([?au]).
Both outcome entries read; nothing open in the cipher. Avenel's clear text was not collated word by word with the
manuscript (his accents and punctuation kept).

## Transcription slips in the cryptiana text (all confirmed by Avenel's independent transcription)

- `38` for `28` in *l'évesque*; `25` for `28` in *souhaiter que*; `35` for `25` in *près d'elle*.
- `25` for `26` in *Vautier*; `16` for `26` in *Vantelet*; `14` for `24` in *de Rome*.
- `22` for `23`, `11` for `13` in *Champagne*; `47` for `17` in *frontière*; missing `19` in *au bois*.
None affects the recovered alphabet.

## 19-20 Nov 2026: the nine sibling letters (BnF fr. 3828, 3825, 3835)

Avenel t. III prints nine more letters of Feb-May 1629 to Rancé and the Queen Mother with their figures in place
(nos. CXIX, CXXXV, CXLVI, CXLVII, CLIII, CLIV, CLV, CLVIII, CLXVII). Under a pre-registered held-out test the fr. 3829
key reproduces his decipherment of CLIV + CLV (0.940 against a best shuffled control of 0.456): a verification of
Avenel and of the key, "read from existing decipherment". Strict count 337/374 cipher words (values taken from his
notes to these letters are holes, the base codes 54, 59, 60 included): three letters read, six read in part. Method and count: `texts/fr3828_method.md`; reading
`texts/fr3828_reading.md`; key `texts/key.md` (Extension). The manuscripts were not seen.

## What remains

- Nothing cryptanalytic. The alphabet, homophones, doubling mark, word codes and the main nomenclature are
  all recovered and independently confirmed.
- Housekeeping: tell S. Tomokiyo (cryptiana) and the DECODE maintainers that BnF fr.3829 ff. 87/89 were
  deciphered in Avenel III (1858) pp. 368–369, 381–383, with the key table above, so the entries can be
  marked solved.
