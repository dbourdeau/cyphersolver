# f. 25v, third pass (BnF fr. 3091, Selve to Francis I, Venice, 14 Sept 1535; DECODE R3697)

Image `img/native_f28.jpg`, left half, native pixel coordinates as in pass 2. DECODE's P5/P6 were checked as
well. They are the same photograph at lower resolution (3393 px for the whole page against about 4500 native),
so they add nothing. Crop scripts are in the session scratchpad:
- `c.py`: autocontrast + Lanczos upscale.
- `s.py`: Gaussian blur, then autocontrast. This worked best for the faint margin hand.
- `k.py`: non-local-means denoise + CLAHE.
- `dk.py`/`th.py`: dark-ink windowing.

The best magnification was 1.4-2.2x. Beyond that the file is only blur.

**Imaging observation (new).** The horizontal strike through T1-T3 is *lighter* than the cipher ink. At a
threshold of about 85-105 (8-bit, after sigma 1 blur) most of the strike drops out and the sign cores survive
(`th.py`). The same window also removes the thin parts of the signs, though, so it only helps with heavy signs.
A colour or multispectral image would probably separate the two inks cleanly. This is the concrete request to
make to the BnF.

Notation as in pass 2. "Agrees" means the visible part of the sign (top, bottom, descender, cross, loop) matches
the key sign for the crib letter.

---

## Gap 1: struck lines T1-T3 and the margin note

### Step 1: the margin note re-read

Crops were made at 1.3-2.5x with three processings (plain autocontrast, blur + autocontrast, denoise + CLAHE).
The hand is lighter and more cursive than the letter's clear hand. Lines 1-2 end in filler dashes, so each ends
a unit.

| line | pass 2 | pass 3 best reading | confidence |
|---|---|---|---|
| 1 | en Hongrie(?) —— | **en(?) Hongrie ——** | Hongrie: medium-high. The first word is 2-3 letters (en/de). |
| 2 | Hiero[nimo](?) A[?]c[o]ne(?) —— | **Hiero[nimo] [?]——**. The second word starts with a looped letter that can be a secretary *d* or *e*, followed by about 5 minim/round letters. Candidates: *demeure* (shape), *entretenu* (sense, see T1). It is not *Lasco*. | Hiero: high. Second word: unread. |
| 3 | ambassadeur po[ur] | **amiablement —— po^r** (pour, with a superscript r) | high. It matches the first cipher word of T2 exactly, so "ambassadeur" is withdrawn. |
| 4 | la charge qu'il a de | **la charge qu'il a de** | high |
| 5 | l'evesch[é](?) de Wespre[m](?) | **Vesprym(?) de la guerre(?)**. The first word has a tall looped initial (a secretary V that looks like b), a long descender (p) and ends *-ym*. The last word has a descender pair that reads as secretary *rr*: *gu-e-rr-e* (pass 1's "ladusse"). | Vesprym: medium. "de la": high. guerre: low-medium. |
| 6 | [?]ing(?) on fait sus fond(?) | **en luy(?) on fait s[..] fond[..]** | "on fait": high. The first group has a y-descender, so *en luy* is plausible. The end is unread. |
| 7 | contre ses ad…(?) | **contre ses ad[..]** (adversaires? adherens?). The word is cut by the flourish of the next paragraph's initial. | contre ses: medium-high |

The note is a **contemporary decipherment, not a summary**. Its line 3, "amiablement", is the first cipher word
of T2. Line 4 is the next 17 cipher signs. Lines 6-7 match "on fait" at the start of T3 and "contre ses" in mid-T3.

### Step 2: crib alignment against the struck signs

**T2 (y 1262)**. This is the only line where the crib runs continuously.

| crib | signs seen | agrees? |
|---|---|---|
| amiablement | ʒ x ʒ z ƀ / ω x ‡ ▽ 7 | 11/11. The crossed long ƀ is clear above and below the strike. |
| pour | ʃ(long, descends) ɵ x°(dark cross) ꝏ | 4/4 |
| la | / z | 2/2 |
| charge | [c not seen] £(tall ‡ with curled top) z ꝏ ∽(blotted) ‡ | 5/6. The c is lost in the strike. |
| qu'il | 6 x° q(long descender) / | 4/4, plus the trailing z-hook of *qu'ilz*. This is doubtful: it may belong to the next sign. |
| a | ● (blot) | 0/1 visible. The crib requires it. |
| de | L ‡ | 2/2 |
| Vesprim | ɯ/W ʃ(looped top, long) ꝏ [z] ʒ x | W, ʃ, ꝏ, ʒ, x agree (V p r i m). One z-like sign is unexplained. There is no separate sign for *es*: either the W carries it or it is lost in the strike. |
| de la | L ω / z | 4/4 |
| guerre(?) | ●(big blot with descender) ‡/x° ω ꝏ [ω] | Only the u-cross, e and r agree. The g is a blot, and the doubled r with its null is not seen. Low confidence. |
| en | ω ▽ (▽ drawn 7-shaped) | 2/2 |
| luy | / x ʒ | 3/3 |

T2 reads: **amiablement pour la charge qu'il a de Vesprim de la guerre(?) en luy**. About 50 of about 62 signs
are read as sense (12 doubtful: c, a, the Vesprim extras, guerre). About 12 signs are not assigned. Most are
between "qu'il" and "de" and inside "Vesprim".

**T1 (y 1150)**. The struck text starts at "Quand depu[is]". Whether "de pu" is clear or cipher cannot be told,
because the cipher L ω ʃ x° would look the same. After that come about 35 signs.
- Tail (x 3330-4100) at 2.4x: `/ ω [x?] ▽ | 7 ꝏ ω 7 q ‡ ▽ ω ▽ 7`. This reads *l'e[?]n-tretienent*, that is
  **l'entretiennent(?)**, "they treat him", which runs on into T2's "amiablement". The 10 signs of *-tretienent*
  agree (7 bar-and-stem, dark ꝏ, ω, 7, long q, ‡, ▽, ω, ▽, 7). The 4 signs before them fit only in part.
  Confidence: medium-low. The margin's line 2 second word (*entretenu*?) would echo it, but the shape does not
  confirm that.
- Middle (x 2850-3330): `... ot ‡ | ω' q ● ꝏ ▽ x° x ꝏ ω ot ‡`. The crib *Hieron[imo]/Hieronymus* would need
  h i e r o n [y] m. The q(i) ●(e) ꝏ(r) ▽(n) x(m) sequence is suggestive, but the h and o are not confirmed.
  Not counted. *Hongrie* (£ R ▽ ∽ ꝏ q ω) cannot be placed: no £ is visible anywhere in T1. The margin's line 1
  may be a heading rather than a line-by-line gloss.
- Head (x 2850-3000): `ʃ ℓ ℓ ω ot ‡ ʃ ɵ ω ω`. Unread.
- T1 total: about 35 signs, about 10 read as sense (all doubtful), about 25 unread.

**T3 (y 1376)**
- Start: `R ‡ ▽ [▽] S z q [/|7] z ...`. The crib *on fait* gives R = o (as in "bon" and "en ont"), ▽ = n,
  S = f (short, as in failloient), z = a, q = i, and the stroke under the strike = 7 (its top bar is where the
  strike runs). **"on fait"** is read with medium confidence. The ‡ between R and ▽ and the second ▽ are
  unexplained.
- Middle: `/ z | ‡ z / ω / S | / R ω / ʒ p / z` (la ...). This does not align with the margin's "s[..] fond[..]"
  on any value set tried (‡ as e, o or h; / as l or c). Unread.
- `/ R ● 7 ꝏ ω | ot ‡ ot`: **contre ses**. / = c, R = o, blot = n, 7, ꝏ, ω, then ot ‡ ot. 8 of 9 signs agree.
  Medium-high.
- After it: `L ꝏ [ꝏ] ω x° ‡ ʃ q | z ʒ x x ω | ot R | ...`. The crib *ad[versaires]* does not fit (no z before
  the L, no ot). Unread.
- Clear after (x 3850-4150): "... de pro[pos](?) S[ire] ..." then a new paragraph.
- T3 total: about 55 signs, about 16 read as sense (on fait, la, contre ses), about 39 unread.

### Clear words of the struck block
T1 in clear: "me semble que est bonne sorte. Quand depu[is]". The line is struck from "Quand" on. The earlier words
are overwritten by the strike's start but legible. Nothing clear can be seen between T1 and T3 except the T3 end,
"de pro[pos](?) S[ire]". The sentence after the block begins a new paragraph with a flourished initial:
"[S]ire, ... temporiser ... qu'il vous a pleu me commander par vos ...". Pass 2 already had this.

### Why the rest of T1-T3 stays open
- **Physical: resolution.** The native Gallica file is the largest available. The signs have an x-height of
  about 30 px, and the strike covers the middle third of each. Denoising, CLAHE, gamma, blurring and ink-density
  windowing were all tried. The windowing removes the strike but also the thin sign strokes. Only signs with a
  distinctive top or bottom can be confirmed.
- **The crib is only partial.** The margin is legible for about 60% of its letters. Where it is legible and
  aligns (T2, "on fait", "contre ses"), the signs agree. Where it is not legible (line 2's second word, line 6's
  end, line 7's end), there is no crib.
- Remedy: a colour or multispectral image of fr. 3091 f. 25v, or autopsy of the original. The strike ink is
  lighter than the cipher ink, so a colour image should separate them.

---

## Gap 2: end of lower line L5 (y 4165)

Re-read at 1.6x, 2.3x and 3x (c.py). The long diagonal cancellation crosses at x ≈ 2420 (the "d'eux" group),
x ≈ 2980 (between "vous" and "sçaur-") and x ≈ 3560 (the final group).

- `7 ω ▽ x°`: tenu. `ʃ ● R ʃ R ot`: propos. Both unchanged, high.
- `ℓ ‡(hooked top) x x ω`: **comme**. The hooked ‡ = o, as on f. 25r ("seroit") and in "marchant". The pass-2
  "4ℏ" group is ω. Upgraded to high.
- `L ω ✗(x° under the diagonal) ʒ(closed 3 with tail)`. This is "d'eu-" plus a sign read as x (a lying-8/3
  shape), giving **d'eux(?)**. The diagonal passes through the u. Medium-low.
- `Ꜿ(C-hook with long top and inner loop, dot above) ‡(small cross, dot) x°(looped x) ot`. The value depends on
  the hook: as d it gives **deus**, and as v it gives **vous**. The hook is the same shape as the d in "quand"
  (L4), so *deus* ("deux") is preferred. Low-medium. *d'eux deux* is still an odd phrase. *comme de vous* would
  need L ω alone before it, leaving ✗ ʒ unexplained.
- `ot / z ʒ' ꝏ ω W ot`: the diagonal crosses between ot and /, and the pass-2 "ɤ" was part of that stroke.
  Reading: s ç a [ʒ with a superscript mark: u] r e [W] s. W is a null here, as on f. 25r ("France", "umbre",
  "entre"). This gives **sçaurés** (= sçaurez). Medium.
- `6 ‡ ʃ ɵ [stroke]`: q, cross (u or e), long ʃ (descends, so p), ɵ (o), then a short stroke crossed by the
  diagonal (7 or / or nothing). This gives **qu(e) po-** / **que p[our](?)**. It is unfinished: the next words,
  "Quan[..] ... de", are clear text struck by the writer, and "pour continuer le propos dudict Duc" follows. The
  cipherer seems to have dropped into clear text here. Low.
- Struck clear after the cipher: "Qu[a]n[t](?) i'ay(?) de" (struck), then "pour / continuer le propos dudict Duc
  [que](?) cy dessus ...". The struck words are too blotted for more.

Reading: **tenu propos comme d'eux deux(?), [vous] sçaurés que p[our](?) ...**. The last 5 signs are not secured.
Still open: the final group (5 signs, physical: the diagonal and a blot, and the text breaks into clear), and
the value of the Ꜿ hook (unresolved, not blocked).

## Gap 3: the lone a-sign before "quand" (L4, x ≈ 2520)

At 2x the sign is a large open **3** whose lower bowl closes into a tail. It sits well apart from "susdict"
(`ot x° ot L q / 7`, where the slash = c is confirmed) and from "quand". It is not the tailed ʒ = y: its tail is
a closing flourish, not a descender. "quand" = `6 x° ʒ(tailed = a) [v] ▽(T with bowl) Ꞇ(long-topped d-hook,
crossed by the diagonal)`. There is also a small `v` stroke between a and ▽. It may be a pen-lift of the ▽ or an
l-sign (`<`).

Readings tested:
- *a qu'ilz* ("to whom they"): gives good sense ("par le marchant susdict, a qui ilz en ont quelquefois tenu
  propos"). But it needs ʒ = i (it is the tailed a-form here), v = l and the hook = z. The ▽ is left over.
  Rejected on the shapes.
- *a quand*: fits every sign but does not parse.
- *susdicta* / *le marchant susdict a*: does not continue.

Result: the 3 = **a** is certain as a sign. Its role is unresolved: most likely a cipherer's slip (a false start of
"quand", whose third sign is also an a) or a null. It is counted as unread (1). It is not externally blocked.

---

## Updated counts

Sign totals are hand counts per strip (± 3 per line, as in pass 2).

| run | signs | read as sense | of which doubtful | unread |
|---|---|---|---|---|
| L1-L3 | 152 | 152 | 4 | 0 |
| L4 | 44 | 43 | 2 (marchant extra o, quand hook) | 1 ([a]) |
| L5 | 38 | 31 | 12 (d'eux deus, sçaurés) | 7 (final group 5, 2 stroke fragments at the diagonals) |
| **lower block** | **234** | **226 (96.6%)** | **18** | **8** |
| T1 | ~35 | ~10 (-tretienent) | ~10 | ~25 |
| T2 | ~62 | ~50 | ~12 | ~12 |
| T3 | ~55 | ~16 (on fait, la, contre ses) | ~6 | ~39 |
| **struck top** | **~152** | **~76 (50%)** | **~28** | **~76** |
| **page** | **~386** | **~302 (78%)** | | **~84** |

Pass 2 had the struck top at about 31/150 (20%). The gain comes entirely from using the margin as a crib.

## Margin note, best reading

> en(?) Hongrie —— / Hiero[nimo] [?] —— / amiablement po[u]r / la charge qu'il a de / Vesprym(?) de la
> guerre(?) / en luy(?) on fait s[..] fond[..] / contre ses ad[..]

## Continuous reading of f. 25v (clear in roman, cipher in bold, [?] = unread, (?) = doubtful)

... me semble que est bonne sorte. [struck from here:] Quand depu[is] **[? … ] l'entretiennent(?) amiablement pour
la charge qu'il a de Vesprim de la guerre(?), en luy [?] … on fait [? … ] contre ses [? … ]** de pro[pos](?).
[margin, contemporary decipherment: "en Hongrie — Hiero[nimo] … — amiablement pour la charge qu'il a de Vesprym
de la guerre, en luy on fait … contre ses ad…"]

Sire, … [clear paragraphs as in pass 2] … Et pour[tant] leur fust … chargé de parler avecques … entreprinse cy
dessus, **ne failloient pas d'adviser et faire adviser par d'aultres des occurrances de ça, sans especifier
aultrement; entendre, et les advis qu'ilz donnent au Turc, et qu'ilz luy font donner par le marchant susdict,
[a] quand en ont quelquefois tenu propos comme d'eux deux(?), [vous] sçaurés(?) que p[our](?) [...]**
[struck clear: Quan[t](?) i'ay(?) de] pour continuer le propos dudict Duc … cy dessus davantaige, sinon que de
ladicte paix aussy …

English gist of the struck passage: *[When since] … [they] treat him amiably regarding the charge he holds of
Veszprém in the war(?); in him … they do … against his [adversaries?]*. The margin places it in Hungary and
names "Hiero[nimo]". Identifying him with Hieronim Łaski remains open, as in pass 2.

## Remaining gaps and blockers

1. **T1-T3, about 76 signs.** Physical blocker: the strike covers the x-height at the native resolution. The
   margin crib is illegible for exactly the unread stretches (line 2's second word, the ends of lines 6-7).
   Needs a colour or multispectral image or the original. The finding that the strike ink is lighter makes a
   colour image likely to work.
2. **L5 final group `6 ‡ ʃ ɵ [.]`, 5 signs.** Partly physical (the diagonal cancellation, a blot) and partly
   textual: the cipher breaks off into struck clear text.
3. **L5 `Ꜿ` hook (deus vs vous) and the "d'eux" group under the diagonal.** Unresolved, not blocked. Next step:
   compare every C-hook on ff. 24-25 and in the 1536 letter to decide d vs v.
4. **L4 lone "3" before quand.** The sign is certain. Its role (slip or null) is unresolved.
