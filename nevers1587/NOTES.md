# A correspondent at Randan (Auvergne) to the duc de Nevers, 27 March and 4 April 1587 — BnF fr. 3975 ff. 28, 30 (DECODE R4285, R4286)

Catalogue item 185, "Unknown sender (Rome) to Louis Gonzaga, duke of Nevers, 2 ciphertexts" (class C, scored by
rule). Session of 22 September 2026.

Status: read. Both letters are in clear French with a few cipher items; every item is read with the key
**BnF fr. 3995 no. 11** (the Nevers key book), used unchanged. 26 of 27 cipher units accounted for (0.963, measured
from `reading.tsv`): 22 letters, words and codes, 3 nulls, and 2 signs of a struck-out false start; one sign (ƥ in
the f. 30 run) is taken as a null against its key value. DECODE's "Rome" is wrong: the first letter is dated
**"De Randan, ce XXVII mars"** in cipher.

## The documents

* BnF fr. 3975 = Gallica `btv1b90605473` (396 canvases, *Collection Mémoires de la Ligue*, anc. 8931(3), de Mesmes
  277). f. 28r = canvas 52, f. 28v = 53, f. 29 (blank) = 54, f. 29v (address) = 55, f. 30r = 56, f. 31v (address) = 58.
  IIIF `full/full` gives 4949 × 6545 px. Images in `img/` (git-ignored).
* BnF notice (cc504266, cached `gallica_sweep/notice_cc504266_cd0e37708.html`): piece 7, f. 28, *"Lettre avec
  chiffrement et déchiffrement adressée à M. le duc de Nevers pour lui rendre compte d'un voyage à Lyon. Ce XXVII
  mars 1587"*; piece 8, f. 30, *"Lettre adressée par le même correspondant et sur le même sujet … Ce IIII apvril
  1587"*. The "déchiffrement" is two interlinear glosses on f. 30 only ("Le duc d'Espernon" over 45, "Lyon" under the
  first four signs of the run). Nothing is glossed on f. 28.
* **R4285 = f. 28r–v**, 27 March 1587 (the year from the docket "27 de Mars 1587"). Two pages of clear French. Cipher:
  code numbers 94, 6, 23 (each with the key's virgule, "94," "6,") and the place in the dateline, ten signs
  `C ∞ 6 ƥ z ι ◊ é ι ⊕` before the clear "ce xxvij Mars".
* **R4286 = f. 30r**, 4 April 1587 ("Ce iiij apvril 1587"). One page of clear French. Cipher: code 45 and one run of
  13 signs `π ^ ꭓ é ∞ ƥ F ƨ h Ŧ ◊ 7 o`.
* Both are signed with the same monogram (an M-like cipher mark between two ʃ), and the hand fills line ends with a ʃ.

## The key

Tomokiyo's catalogue of fr. 3995 lists **no. 11 (f. 23, "1586")**: substitution by letters, figures and symbols,
figures or letters with a virgule for names and words, capitals for small words. Read from Gallica `btv1b525085665`
canvas 52 and tabulated in `key.md`. It fits at once: 45 = "D: d'Espernon" (the gloss), 94 = "Marquis",
6 = "Mr d'Antragues", 23 = "Rne de Navarre", and π ^ ꭓ é = l y o n. The name list is southern and Auvergnat (St Vidal,
Mandelot, Maugiron, Randan, the grand prieur, the comte de Sault, the bishop of Clermont).

Instructions on the sheet: *"L'on pourra se servir de toutes sortes de caractaires que l'on voudra faire a plaisir avec
ceulx qui sont dans ce chiffre, lesquelz serviront de nulles."* So a sign absent from the table is a null. ∞ is absent.

## The sibling that calibrated the hand: BnF fr. 3413 f. 102

Tomokiyo notes that no. 11 "is used in a letter of Cardinal of Guise to the Duke of Nevers, Clairmont, 25 February
(BnF fr. 3413, no. 49 (f. 102))". fr. 3413 = Gallica `btv1b52510705j`, f. 102r = canvas 213. It is **not** the
cardinal de Guise: it is the same hand, the same ʃ line-fillers and the same monogram signature as fr. 3975 ff. 28/30,
dated in clear "De Clairmont ce xxv feb[vrier]". It reports the Gévaudan Huguenots' raids, the King's order to St Vidal
to prepare the sieges of Marvejols and Le Malzieu (so 1586: Joyeuse took both in August 1586), and five cipher lines
with an interlinear decipherment in another hand: *"Mr du Mayne m'a mandé qu'il desire que je l'aille trouver avec ma
compagnie, deux mille hommes de pied et bon nombre de ma cavalerie … si je l'abandonnois"*.

Aligned with its gloss it gives this writer's forms of the key signs (key.md, third column):

| gloss | cipher | note |
|---|---|---|
| m'a mandé | t 9 ʃ ƥ é 1 0 | 1 = d (the key's i), 0 = e |
| qu'il desire que | z 4 7 m · 5 ⊕ 3 r 6 h · g + b | 5 = d (ʃ), ⊕ = e (♀), 3 = s |
| trouver | a c n 4 + b 6 | + = v |
| avec | ƥ 4 h ƨ | |
| ma compagnie | t 9 · 74, | 74 = Compagnie |
| deux mille | 1 6 4 φ · t r m π h | his 6 and b (e) look alike |
| hommes | ∂ 4 t s b 0 | ∂ = h, 0 = s here |
| de pied | 1 ⊕ Ŧ 7 6 5 | **Ŧ = p** (the key's script F) |
| et bon | F x n 2 | **F = et** (capital F), 2 = n |
| si je l'abandonn[ois] | 0 7 · r b · m 9 x ƥ 2 1 n 2 é … | 0 = s |

## The reading

`dec.py` decodes `ciphertext.txt` with the table and writes `reading.tsv`.

**f. 30 run** `π ^ ꭓ é | ∞ ƥ | F | ƨ h | Ŧ ◊ 7 o` = **Lyon · [null null] · et · ce · pais**:
*"45 [le duc d'Espernon] a esté en tres grande alarme, passant pres Lyon et ce pais, et sans aucun subject, car je
vous puis asseurer qu'on n'a jamais songé de luy faire desplaisir."* Ŧ = p and F = et are this writer's usage (see the
sibling); ∞ is a null by the key's own rule. ƥ is the key's a, but "Lyon a et ce pais" is not French, so it is taken as
a null with ∞ (grade M).

**f. 28v dateline** `C | ∞ | 6 ƥ z ι ◊ é | ι ⊕` = **de · [null] · Randan · (de)**: *"De Randan, ce xxvij Mars"*.
C = de (capital), 6 = r, ƥ = a, z = n (the writer's 2 and z are one shape: "2 4 7" = qui and "x n 2" = bon in the
sibling), ι = d (his dotted-i form of the d-sign), ◊ = a, é = n (looped, ∂-like). The last two signs read d, e and are
a false start: at full resolution (canvas 53, 3× crop) the ⊕ is a pale blot struck through with a double "="
stroke, and the ι stands just before it. The writer began "de" in cipher, cancelled it, and wrote "ce xxvij Mars" in
clear. Read as cancelled (grade C).

**Codes (f. 28r)**: *"en ce temps mesme 94 [le marquis] y arriva, qui vendit une terre a 6 [M. d'Entragues], dont ils
s'estoient remis a mons. de Lyon pour le marché"*; *"pour ce qui est de 23 [la reine de Navarre], je ne m'en suis voulu
jamais mesler"*. Grade H for all four codes (the key's list; 45 is also glossed).

The full clear text of both letters, with the cipher items resolved, is in `reading.md`.

## Who wrote

Not named. What the three letters (fr. 3413 f. 102, fr. 3975 ff. 28, 30) show: he writes from Clermont (Feb. [1586])
and Randan (27 Mar 1587), in Auvergne; he keeps a company, foot and cavalry of his own; Mayenne asks him to join him
with two thousand foot; he asked the King for leave to maintain cavalry against the Gévaudan Huguenots; he went to Lyon
on private business while Tournon, St Vidal and the bishop of Le Puy met Mandelot about the war in Vivarais; he keeps
clear of the reine de Navarre (then held at Usson, in Auvergne); he hopes to wait on Nevers at Nevers. Randan was the
seat of Jean-Louis de La Rochefoucauld, **comte de Randan**, governor of Auvergne (killed at Issoire, 1590), and he is
the obvious candidate, but the key lists "Mr de Randan — 8", and nothing on the leaves names him. The write-up says
"a correspondent at Randan, probably the comte de Randan", no more.

"94, le marquis" in Auvergne in March 1587 is probably the marquis de Canillac, who had custody of Marguerite at Usson
and changed sides in her favour that winter. Context only, not proven.

## Prior work

DECODE R4285/R4286: "Non-decrypted", sender unknown, R4286 origin "Rome" (wrong), no transcription. Tomokiyo: fr. 3975
"Information on BnF does not mention 'chiffre'" (league.htm); the fr. 3413 sibling is listed under the cardinal de
Guise. Not in *Les Mémoires de M. le duc de Nevers* (1665; Gallica `bpt6k6435941k`, `bpt6k8717151d`, full-text search
for Randan, Chenonceau, Espernon: no hit on these letters). No reading anywhere before this session.

## Remaining gaps
- f. 30 run, sign 6 (ƥ, after the null ∞) - blocker: too-short; key value a gives no sense, taken as a null; one occurrence, nothing to test it against

(The dateline's last two signs, first listed here as unexplained, were re-examined at full resolution on
22 Sept 2026 and are a struck-out false start; see The reading.)

## Escalation
- [x] siblings: fr. 3975 ff. 29-31 (addresses, docket, a credence note in another hand) and fr. 3974-3978 notices searched for the same correspondent; fr. 3413 f. 102 found (same hand, glossed) and used to calibrate the glyph forms
- [x] clear-pages: the "déchiffrement" of the notice is the two glosses on f. 30; nothing on f. 28
- [x] known-keys: Tomokiyo's fr. 3995 keys nos. 9-16 viewed; no. 10 ruled out (45 = Picardie); no. 11 fits and reads everything
- [x] print: Tomokiyo nevers.htm and league.htm; Mémoires de Nevers (1665) full text on Gallica: nothing
- [x] key-rebuild: n/a for the key (no. 11 is complete); the writer's glyph forms rebuilt from the glossed sibling (Ŧ = p, F = et, 1 = d, 0/⊕ = e, 2/z)
- [x] retry: both items re-decoded with the calibrated forms (enum_readings.py, edits.py list the blind attempts that failed before calibration); the three doubtful signs re-examined at full resolution, the dateline pair found struck out

## Files

* `key.md` — key no. 11 with this writer's forms.
* `ciphertext.txt` — the cipher items, one sign per token (27 units).
* `dec.py` → `reading.tsv` — the decode.
* `reading.md` — both letters in full, cipher items resolved.
* `enum_readings.py`, `edits.py` — the language-model enumerations tried before the sibling was found (no result).
* `src/manifest.json`, `src/manifest_3413.json` — Gallica manifests.
