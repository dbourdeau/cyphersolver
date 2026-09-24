# Galeotto Fibindacci da Ricasoli's cipher, 1424/25: Gabbrielli's key, extended from the glossed sibling letters

Work of 24 Sept 2026. Base: P. D. Gabbrielli's table "Cifra di Galeotto Fibindacci da Ricasoli ... 1424" (ASF, Chiavi
delle cifre ... Dieci di Balìa, vol. 1, no. 1, October 1863; Yale Ilardi reel 58, frame `58-3.pdf`; printed by Meister
1902 p. 50), re-read this session from the film at full size (`keys/k_alpha.png`). Extension: Gabbrielli's own
interlinear glosses over the cipher runs of the four letters DECODE holds (R3754 = Responsive 2 no. 171, R3755 = no. 21,
R3756 = no. 91, R3757 = no. 92), aligned sign by sign in `TRANSCRIPTION.md` (sibling section) and `cipher171.tsv`.

## Was a fuller key already available? (checked 24 Sept 2026)

| where | what is there | result |
|---|---|---|
| Gabbrielli vol. 1, frame 58-3 (key no. 1) | alphabet of 45 signs, 18 nulls, 30 nomenclator entries, 6 clear cover-words; note "tolto da poche parole trovate in sole quattro lettere" | the base key; re-read, see corrections below |
| Gabbrielli vol. 1, frame 58-4 (key no. 2, "Fibindacci (de) Karolus commissarius", an. 1424, filza 1 nos. 128, 157; filza 2 no. 156) | alphabet of two signs per letter and 9 word signs (che, con, del, et, fanti, non, Orsolo?, per, se); note "tolta da poche parole di tre sole lettere" | a different sender (Carlo Fibindacci) and a different system: shared shapes carry other values (+o = B, 6 = S, π = I, ∧ = H, ∃ = non), which the glossed pairs of nos. 21, 91, 92, 171 contradict (+o = O, 6 = M, π = F, ∧ = R, ∃ = Malatesta). Not this cipher |
| Gabbrielli vol. 1, frames 58-5, 58-6 (keys nos. 3, 4) | "Johannes" and "Zaninus et Conradinus", 1424, filza 7: Latin syllabic nomenclators | not this cipher; later frames (58-7 to 58-9, per the 23 Sept scan) are keys of 1430 |
| Gabbrielli vol. 1 indexes (58-index1..3) | sender index | checked 24 Sept: the three fetched frames are the title leaf and the start of the "A" names (Acciaioli, Alamanni, Albizzi); the F (Fibindacci) and R (Ricasoli) pages were not fetched. Fetch them from reel 58 before any DECODE upload |
| Meister 1902, pp. 43-50 | prints key no. 1 as Gabbrielli made it, footnote "only from a few words in four letters" | same key, no additions |
| Somogyi 2016 (Verbum 17, pp. 195-217), Allegato 3 "Fi2" | reproduces Meister's table (45 signs) and analyses it | same key; no ciphertexts (project scan of 23 Sept 2026, `oldest/scan_2026-09-23/italy.md`) |
| DECODE keys | records R5687-R5698 are Gabbrielli's volume ("ASFi_SIVol1_1" ... "_12", "Alfabeti che servono a spiegare le lettere in cifra ... dal 1424 al 1530", uploaded 2023, authentication required); R5687 (5 pages), R5688-R5690 dated 1424 | the Gabbrielli volume is already on DECODE as key records; no key record is linked to R3754-R3757, and none holds more than Gabbrielli's table (the 1424 records are frames of the same volume). DECODE has no other Florentine key of 1424-25 |
| DECODE ciphertexts | R3753-R3758 (Dieci di Balìa Responsive 2, 3, 7): R3755-R3757 are the three siblings, all "Non-decrypted", language given as Latin | no transcription or decryption attached |

So no fuller key exists in print or on DECODE. The extension below is new. Before any upload the DECODE key records
R5687-R5690 should be linked to R3754-R3757 (they are the published key), and the extended table can go up as a
derived key that cites them.

## Corrections to the tabulation in NOTES.md (from the film, not new values)
- ▽ is under **E** in Gabbrielli's table, not D. ⊓ with a stem (⊓̍) is his second **I**; 8 with a ring below (8̊, a
  key-shape) is his first **S**; the cross over a small circle (ô) is his first **T**; the "star with tail" (⋉) his
  second T; two crosses side by side (#, ‡‡) his second **L**; the plain 9 his first **B**.
- His O "4 with a cross-bar" (q‡) is the closed 4; the open 4 with a long bar (⊀) is a different sign (T below).

## Grades
H = the value is fixed by a Gabbrielli gloss over the run where it occurs (or by his table and at least one glossed
run). M = probable: the value fits every run where the sign occurs, but rests on position in a word the context
gives, or on one gloss only with a competing value. I = inferred from context only.
Evidence notation: `21-12` = run 12 of no. 21 in TRANSCRIPTION.md; `171 L7f` = run in `cipher171.tsv`.

## The alphabet (Gabbrielli's signs, then the values recovered here)

| letter | Gabbrielli 1863 | recovered here (grade; evidence) |
|---|---|---|
| A | ∵ (:·), Ħ (H with bar), ℘ (looped p) | ɤ (℘ lying on its side; Gabbrielli filed it as a null) = A (H; 91-2 MANDATO, 171 L12b) |
| B | 9, -·- | none. 9 is N in every glossed run (below) |
| C | φ (9 with loop), ⊢, E | ᴗ (small u) = C beside its D value (M; 171 L3b and L12b CITADINI, both under the gloss "cintadini"); ɣ (y-shape) = C (M; 21-6 CONTENTERÀ) |
| D | ᴗ (small u/o), ⊐ | confirmed: ᴗ in 21-4, 21-10, 21-12, 21-15, 91-2, 171 L3a, L7a, L11c (H) |
| E | ς (5), ⊔, ▽ | Ꜧ (H with a hook) = E (M; 21-6) |
| F | π, o— | o— confirmed (H; 21-20 FILIPPO) |
| G | ═, ⁝ | ═ confirmed (H; 21-10, 21-15 MODIGLANA); ⁝ (M; 92-2 MINGARDO) |
| H | ‖ | none new |
| I | ·:' (dots with tick), ⊓̍, ‡ | ÷' (bar with dots and tick) = I (M; 92-4 HIERI); ɦ = I (M; 21-8 IMOLA); !: = I (M; 21-20 FILIPPO); # = I (M; 171 L12b, by position; # is also L) |
| L | ·÷· (÷), #/‡‡, ● | + (single cross) = L (M; 21-2 NOVELLA, one occurrence; + alone is also Gabbrielli's word sign "castello") |
| M | ●, 6, ɧ | ʃ (5-shape with a cross-stroke) = M (H; 91-2 MANDATO) |
| N | 7, E | **9 = N** (H; 21-4 NE ANDARONO, 21-6 NON, 171 L12a PARENTI); ϙ (9 with straight tail) = N (M; 171 L3b CINTADINI) |
| O | ∂, q‡ (4 with bar), ✱ | **+o (cross beside a circle) = O** (H; 21-4, 21-6, 21-12, 92-1, 171 ×5; distinct from Gabbrielli's null o+ and his word sign +o– "Dieci", which has a tail); **ʒπ (π with a hooked leg) = O** (H; 21-10, 21-15 MODIGLANA ×2); 3 = O (M; 21-6) |
| P | Ч/ψ, ♀ | confirmed ψ (H; 21-19 PROMETTERE, 171 L12a) |
| Q | -]-, 4o | none new; 4o also stands alone for Carlo (nomenclator) |
| R | Γ°, ∧ | ∧ confirmed (H; 21-4, 21-12, 21-19 ×2, 92-4) |
| S | 8̊, ⊼ | π = S (M; 171 L7f SOSPETOSA; π is F in the same clause); ʓ (3 with loop) = S (M; 171 L7f; Gabbrielli has a similar null) |
| T | ô, ⋉ | **⊀ (open 4 with long bar) = T** (H; 21-19 PROMETTERE, 92-1 CONDOTTO, 91-1 PARTENDO); Ƭ = T (M; 21-6); ll (two light strokes) = T (M; 171 L12a PARENTI) |
| U/V | ÷̈ (dots over bar), 99, ♀ | confirmed ÷̈ (H; 21-8 VENUTA, 21-12 ORIUOLO), 99 (H; 21-2, 92-1 SALVO), ♀ = V (H; 92-4 VENNE, 171 L2a PAVOLO) |

## Nulls
Gabbrielli's 18: ∵̇ (:·:), ɤ, 8, ⁝⁝, ⊕ on a stem, ////, ʓ-like S, H in a box, ƙ, ∞, ʒ over 6, A with loop, ß, q, ✱, "ay",
2 (?), o+. Corrections and additions:
- ɤ is not a null: it is A (above).
- q (9 with a long tail) is a null (H; 171 L4b ACOMANDINO, where the gloss has no letter for it).
- **▼ (heavy filled triangle or block) = null** (M; 21-2 ROTTA, 21-4 ANDARO▼NO, 171 L11c MADON▼NA, 171 L4a before ⊡).
- ϡ (feathered sign) = null (M; 171 L7b P[ϡ]URE).
- plain 4 without a bar = null (I; 171 L2a P[4]AVOLO).

## Nomenclator (Gabbrielli's 30 entries; the ones seen here)
Confirmed by glosses in the siblings (H): ∃ Malatesta (21-23 ×2, 91-4), M Duca di Milano (21-3, 21-6, 21-17 ×3), ff che
(21-3, 21-6), β con (21-3 "guerra col duca": β stands for the cover-word con = guerra; 92-1 SALVO[β]DOTTO: β is also
the syllable *con* inside a word, which Gabbrielli did not note), o7 Galeotto (21-16, 91-5), oto Pandolfo (21-21,
21-24), 4o Carlo (21-21, 21-22, 91-1b), ooo fiorini (21-18, 92-6), ·+· castello (21-11), +o– Dieci (21-7, 21-13,
171 L11b), 8 Faenza (21-9), ⊥̇ città (21-9), oɣ / ɣρ / ɣ Conte d'Urbino (21-26, 92-4, 171 L3c, L9a, L13a), oTo gente
d'arme (21-8), ↑ fanti (171 L11a).
Added: ſſſ = pace (H; 21-7, gloss "pace"; Gabbrielli's entry beside "Per" may be this sign, the film is unclear there).
Proposed, not proved: ⊡ (box with a bar, after the null ▼) = il Papa (I; 171 L4a, Gabbrielli's mark ṗp̄ above it; the
sign resembles his "H in a box", which he lists as a null and, with a bar, as "Mille").

## Count of recovered values (not in Gabbrielli's table, or changing his value)
- H (6): ɤ = A, ʃ = M, 9 = N, +o = O, ʒπ = O, ⊀ = T; plus the nomenclator entry ſſſ = pace (7 in all).
- M (18): ᴗ = C, ɣ = C, Ꜧ = E, ÷' = I, ɦ = I, !: = I, # = I, + = L, ϙ = N, 3 = O, π = S, ʓ = S, Ƭ = T, ll = T;
  nulls ▼, ϡ, q confirmed; β as the syllable *con*.
- I (3): plain 4 = null, ⊡ = il Papa, the single E before "dicesse" in no. 171 = ella (word sign).

## What the key still lacks
- Values for B, H, Q beyond Gabbrielli's, and for the signs in the unaligned runs (21-1, 21-14, 21-28, 91-1b, 91-3,
  91-6, 91-7, 92-2/3 middle, 92-4 first six signs, 92-5, 92-6). The sign ⊀ followed by ψ in no. 171 L7e is unread.
- Polyphones to settle: ᴗ (D and C), # (L and I), π (F and S). Each rests on one letter so far.
- The rest of no. 92 (about fifteen glossed runs) is not yet transcribed. It is the next source of pairs.
