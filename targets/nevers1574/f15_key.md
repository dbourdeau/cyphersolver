# Henriette de Clèves to Nevers, Lyon 16 Sept [1574]: the substitution alphabet as recovered

BnF fr. 3315 ff. 15r, 15v, 16r. Recovered 22 Oct 2026 (Claude Opus 5.5) by aligning the large cipher signs with
the contemporary interlinear French gloss, word by word. A value is entered only when it holds in several words.
ASCII notation as in `f15_signs.tsv`.

| plain | sign(s) (notation) | evidence words (cipher -> gloss) |
|---|---|---|
| a | `1` | `1` a; `167FZ` aviez; `4124` tant; `+1T7` mary |
| b | `±` | `±82` bon; `±7F2` bien; `±F16` beau |
| c | `C` (open c-shape) | `CF` ce; `C824F24F+F24` contentement; `C729` cinq |
| d | `b` (b-shape) | `bF` de; `b6` du; `+1b74` m'a dict; `b822FT` donner |
| e | `F` (also `E`) | everywhere: `7F` je, `2F` ne, `96F` que |
| f | `+` crossed long form; on f.16r also `q̶` (crossed q) | `+174` faict; `+17ʒ7T` faillir; `1q̶q̶72` affin (16r) |
| g | `0` | `082bFT2F+F24` gouvernement; `3706` ligue; `0F247ʒh8++F` gentilhomme |
| h | `h` | `h67C4` huict; `hF6TF9` heures; `Ch89` chose |
| i / j | `7` | `7F` je; `97` si; `b74` dict; `786Tb6y` jourdhuy |
| l | `3` | `31` la; `367` luy; `3F` le |
| m | `+` plain cross | `+F` me; `+1b1+F` madame; `+8297F6T` monsieur |
| n | `2` | `2F` ne; `F2` en; `982` son |
| o | `8` | `82` on; `8TbTF` ordre; `G86T` pour |
| p | `G` / `(9` (looped p) | `G1T` par; `(98724` point; `(9679` puis; `G9678` puis |
| q | `9` | `96F` que; `9673` qu'il; `9614TF` quatre |
| r | `T` | `TF2b6` rendu; `G86T` pour; `8TbTF` ordre |
| s | `9` (same sign as q; often with a long descender) | `9F6` sceu; `F94F` esté; `9168yF` Savoye |
| t | `4` | `F4` et; `4F+G9` temps; `F94874` estoit |
| u / v | `6` | `6F6oZ` veulx; `686` vou(s); `bF+F6T124` demeurant |
| x / z | `Z` | `6F6oZ` veulx; `167FZ` aviez; `4T66FTFZ` trouverez |
| y | `y` | `9168yF` Savoye; `786Tb6y` jourdhuy; `y` y |
| doubled consonant | `ʒ` (one sign for ss / ll) and `b̶` (crossed d, ll) | `+7ʒF` fisse; `FʒF` elle; `(91ʒF` passé; `+7bFb̶F+F24` fidellement; `96Fb̶F` qu'elle |

Name and number signs (not letters):

| sign | gloss | where |
|---|---|---|
| `SS` | Roy | 15r l.25 (l'interest du Roy), 15v ll.8, 10, 17 (au Roy, du Roy, le Roy) |
| `[RM]` boxed group | Royne mere | 15r l.4 |
| `[-d-]` boxed group | Royne | 15r l.5 |
| `XX` + digits | a number | 15v l.1 `XX15..` glossed "25"; 15v l.7 `XXm` glossed "24" |
| `XX` before `62F 3706` | unread (perhaps "et" or a name) | 15v l.10 |

## Homophones and traps

* `9` serves both q and s; context and the descender separate them only loosely. `(9`/`G` is p, not s.
* `+` covers two letters: a plain cross is m, a crossed long stroke is f. They are not kept apart in the tsv
  (both written `+`); the gloss decides (`+F` me, `+174` faict).
* `6` is u and v; `b` is d. Read `6` as d nowhere: the 1584 table's d=6 does not hold here.
* `8` occasionally stands where the gloss has a (`+178` mais, 15v l.18) - probably a slip.
* *gouvernement* is written `0 8 2 …` in all five places (15r ll. 8, 10-11, 15; 15v l. 23; 16r l. 12): the n sign `2`
  stands where the gloss has u, and the v is `6` (or `b` on 15r l. 8). Elsewhere u is `6` (`686` vous, `G86T` pour).
* `b`, the d sign, stands for u/v three times: 15r l. 2 `9bE` que, l. 8 `082bFT2F+F24` gouvernement, l. 26
  `9b1PTF9` qu'apres. Both usages found by Brice Dudout's check of 14 Nov 2026 (PR #572), who saw 15r ll. 2 and 8 on
  the image as transcribed: the encipherer's habit or slips, not transcription errors. They are not table values.

## Difference from Nevers no. 2 (1584, BnF fr. 3995 f. 16)

Same family (a=1, i=7, l=3, m=4/+ shapes, n=2, o=8, r=T, t=crossed 4, g=o-shape, x=Z), but:
e is `F` here (1584: ð/♀); q is `9` here (1584: ∂); d is the b-shape here (1584 also 6); s shares `9` with q;
p is a looped G/(9 here; m is a plain `+` and t a `4` (in 1584 m=4); a doubling sign `ʒ` is used for ss/ll.
Applying the 1584 table unchanged produces false text, as the earlier session found.
