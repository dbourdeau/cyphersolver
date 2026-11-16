# Hautefort to Bellièvre, Grenoble, March 1584 — BnF fr. 15567 ff. 158-161 (catalogue 2839) and fr. 15568 ff. 207-209 (2841)

Status: **read in part** (16 Nov 2026, contributor's own review, preliminary; not yet second-read). **Not validated at the
programme's standard bar** (f. 160v: 0.787 < 0.85): partial submission by documented exception, decided by Brice Dudout on
16 Nov 2026 (DEROGATION.md). Images: Source gallica.bnf.fr / BnF.

## Catalogue corrections
* 2839 is in **fr. 15567** (Gallica btv1b90639282), not fr. 15568: f. 158r = view 164 (right), f. 160r = view 166, f. 161r = view 167 (right).
* Tomokiyo assigns f. 162 and f. 194 to another cipher ("Maygnieulx's Cipher"): the Hautefort letter is ff. 158-161.
* 2841 runs beyond f. 208: view 215 = f. 207r, view 216 = f. 207v + f. 208r, view 217 = f. 208v + f. 209r, all cipher.
* ff. 207-209 are in **another hand** with different usage (+ = e there, = g on f. 158; small ʌ for both i and g; nomenclator
  signs at the head). Tomokiyo's table does not decode it as it stands; see "Second hand" below.

## Prior art
Tomokiyo (cryptiana, *French ciphers during the Reigns of Charles IX and Henry III*, henryiii.htm) reconstructs a partial
"Hautefort's Cipher" from the interlined decipherment of ff. 158, 160 and from f. 207, and gives no reading. Not in GL.htm,
the DECODE dumps, known.py, issues or PRs (searched 16 Nov 2026).

## Method (preregistered)
1. Key: Tomokiyo's table, corrected on f. 158r (lines 1-20 transcribed) and f. 160r: ∂ with curved head = m, with flat head = s;
   barred q = e, plain q = t; ɷ = o; dotted ſ = n; ꝭ, A = s; 2 = n; ɼ = u; small ʌ = i; Ձ = y. Codes 14, 15, 17 open.
2. Blind portion chosen by position before the leaf was looked at (f. 159r, blank, so f. 161r), PREREG and key frozen by SHA-256,
   leaf transcribed in two passes (f161/read1.txt, read2.txt; 7 differences, all decided on the image, f161/read_final.txt).
3. One measurement (measure.py): share of letters covered by dictionary words of 4+ letters: **0.519** against the best of 200
   shuffled keys 0.246 (mean 0.098); thresholds fixed beforehand 0.40 and +0.20. A first metric (2+-letter words) was dropped on
   training data before any look at the portion, because shuffled keys scored as high as the real one (PREREG.md).

## Blind tests (all reported, failures included)
| Portion | PREREG | Score | Best / mean of 200 shuffled keys | Verdict |
|---|---|---|---|---|
| f. 161r ll. 1-14, 325 signs | PREREG.md (v2; thresholds 0.40 and +0.20 set by the contributor) | 0.519 | 0.246 / 0.098 | passes those thresholds, not the standard bar |
| f. 160v ll. 1-15, 330 signs | PREREG-v3.md (standard bar >= 0.85 and >= best + 0.30) | 0.787 | 0.505 / 0.268 | **fails** |
| f. 161v, 287 measurable signs | PREREG-v4.md (∂ = m\|s resolved by the lexicon, controls alike) | not run | — | not measurable (< 300 signs) |

No fresh portion of 300 signs is left in this hand (f. 159 is the blank address leaf).

## Reading
f. 158r opens "Mõsieur de Maugiron se porte bien … la si grant peur de la venue de Monsieur de Montpensier … s'est desia retiré en
intention de n'y retourner plus". f. 161r ll. 1-14: Lesdiguières "monstra en estre fort aliené", "on se doubta des huguenots",
"occasion de se doubter de l'Espaignol et du duc de Savoie" (f161/reading_en.md). Read as sense on the measured portion: 0.81.
f. 160v ll. 1-15: "il n'avoit poinct de responce du duc de Savoye … ne tasche qu'a me retirer donnant esperance d'estre bientost
de retour" (f160/reading_en.md); sure 0.65, sure + probable 0.88. Most probables are ∂ read m where sense wants s.

## Remaining
Second reader; a rule for the two ∂ forms (m/s); values of codes 15, 17, 14 and of the signs C2, f2; second hand: the cross
shapes (+ = g/e/m), signs &, *, 14, 16, 7o and the head-of-letter nomenclator, and a checked transcription of ff. 207r, 208r-209r.

## Second hand (fr. 15568 ff. 207-209, catalogue 2841) — blind test passed at the standard bar
* Opus failed on this hand (18 lines, degenerate annealing). One run of Claude Fable 5.2 (API, 16 Nov 2026) received the Gallica
  crops of ff. 207r, 208r, 208v, 209r — **never f. 207v** — and returned a sign-by-sign transcription (≈ 3,000 signs,
  f207-209/transcription_fable.txt), sign codes (f207-209/GLYPHS-hand2.md), a sign map to the first hand (f207-209/SIGN-MAP.tsv)
  and a key with a confidence per value (key_hand2.json, f207-209/KEY-JUSTIFICATION.tsv).
* Finding: **same cipher as the first hand**, not a second alphabet: about 40 signs keep their value; this hand (or the first-hand
  key) differs on c = l, G = a, th = i, v = qui; + is mostly g (some e/m by sense); new signs ^! = g, O2 = m.
* PREREG-main2.md froze key_hand2.json, the sign codes and measure_main2.py (measure_v4 generalised to x|y values) by SHA-256
  before f. 207v (chosen by position on 16 Nov, CHOIX-PORTION) was cropped. The leaf was then transcribed in two passes
  (f207v/read1.txt, read2.txt; 4 doubtful shapes decided on enlarged crops; clear "Je vous diray …" excluded).
* One measurement, ll. 1-11, 318 signs: **0.879 vs best of 200 shuffled keys 0.536 (mean 0.362) → passes** (≥ 0.85 and ≥ +0.30).
  Calibration on the training pages: 0.922 vs 0.497.
* Reading (f207v/reading_en.md): an envoy of "son Altesse" (Savoy), the sieur Alexandre (governor of Villeneuve d'Asti on f. 207r),
  spends a day with Lesdiguières and, "apres plusieurs promesses et adiurations", delivers a charge from the Duke. Sure 53,
  probable 9, supplied 3, unread 8 (73 words): sure + probable 0.85 → **read in part**. Fable's reading of the training pages
  (Calignon, Ségur's journey to Germany, the Infanta of Spain) is unvalidated and not claimed here.
