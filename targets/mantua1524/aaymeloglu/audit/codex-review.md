# Independent review of the Mantua 1524 decipherment

Reviewed by Codex, 15 November 2026. Only this report was written in the project folder. Existing transcriptions, keys, readings, and control results were not modified. Image crops and execution scratch files were kept outside the project.

**The central decipherment holds with corrections.** This is recognisable Italian produced by a substantially consistent alphabet, not merely sentences invented around isolated guesses. Carpi, heredi, investitura, Cremona, and the blood-tinted urine episode have substantial sign-level support. That does **not** establish every supplied word, a complete key, a blind predictive test, or historical novelty.

The strongest external finding is unusually specific: Gino Benzoni's biography of Federico II already describes Federico showing physicians blood-tinted urine and admitting the deception to Castiglione, including the phrase “sano et gagliardo.” This strongly supports the identification of the episode on 68r. It also means the episode is already known to scholarship. The biography's bibliography includes **Vat. lat. 8214**, so this is external published corroboration, not necessarily an independent archival witness. [Benzoni, *Dizionario Biografico degli Italiani* 45 (1995)](https://www.treccani.it/enciclopedia/federico-ii-gonzaga-duca-di-mantova-e-marchese-del-monferrato_%28Dizionario-Biografico%29/).

| Area | Verdict | Principal qualification |
|---|---|---|
| 1. Reproduction and strict readings | **Holds with corrections** | All 227 stored outputs reproduce after filtering null key entries; the documented decoder itself crashes. Strict labels pass the implemented guard, but the guard trusts confidence labels rather than checking independent support. |
| 2. Image transcription | **Holds with corrections** | Main passages survive. There are identifiable transcription errors on 298v and 68r, and several genuinely ambiguous signs. |
| 3. Key values and merges | **Holds with corrections** | Most frequent values are convincing. One-word values remain hypotheses; `mo`, `gr`, and `bu` have weaker support than an unqualified “strict” implies. No demonstrated single-valued resolution of `lo` = t/l. |
| 4. Reserved-line control | **Does not hold as an independent predictive validation** | Its numbers reproduce, and leakage is disclosed, but the starting key was trained on these lines and the solver had already seen their decode. |
| 5. Historical interpretation | **Holds with corrections** | The illness episode is specifically corroborated; Carpi's chronology needs distinctions; the exact day of Prospero's death is not settled by the cited evidence; 198r describes a conditional retreat, not a verified itinerary. |

Locations below use `leaf.line.seq`, where `seq` is the transcription/reading TSV segment number, not a newly inferred word number. A segment can contain several words or only part of one.

**1. Reproduction and the meaning of “strict”**

I ran `dec6.py key.json --all` using the requested checkout and `uv run --quiet --no-sync python`, with `UV_CACHE_DIR` redirected to temporary storage and `PYTHONDONTWRITEBYTECODE=1`. The script fails in `lib6.dec`:

```text
TypeError: sequence item 2: expected str instance, NoneType found
```

`load_key` retains explicit null values. `dict.get(symbol, fallback)` does not use its fallback when the symbol exists with value `None`. The first heading's unknown minim sign triggers the failure. The `_about` and `_merges` metadata are also loaded as if they were key entries, although they do not cause this particular failure.

For the audit only, I filtered metadata and null entries **in memory**, then ran the decoder and independently compared its units and outputs with the TSV. Result:

| Check | Result |
|---|---|
| Cipher/raised rows | 227 in both sources |
| Mismatching unit sequences | 0 |
| Mismatching `key_output` strings | 0 |
| Differing non-null values between `key.json` and `solve/key6.json` | 0 |
| Non-reserved tiers | 119 strict, 20 forced, 31 lenient, 11 doubt, 15 unread |
| Reserved tiers | 21 strict, 1 forced, 6 lenient, 3 doubt |
| Violations of the implemented strict guard | 0 |

All 140 currently strict rows have a single non-null value for each **declared merged unit**, no code sign, no confidence-C value, no transcriber alternative, and reading equal to output after the stated normalisation. That is a useful result. It is not equivalent to proving the unit boundaries or the confidence assignments.

In particular, `build_words.py` does not verify that a value is supported by more than one word. It checks whether the manually assigned confidence is C. `key6_src.py` even defines B as “2 words or one long word + sense,” whereas the public key describes B as two words. Under the user's stronger requirement, the support audit must be separate from the guard.

The main qualifications concern these strict rows:

| Rows | Value | Support problem |
|---|---|---|
| 298r.15.3 `summa`; 68r.23.3 `mai` | `mo` = m | Before reservation, `summa` is clean but the other intended support, 68r.16.6 `mandato`, has `m{n}?`. The reserved `mai` is welcome corroboration after the fact, not independent pre-reservation support. |
| 68r.19.4 `sangue` | `gr` = a | The other supporting word, 68r.11.2 `cavalcato`, has `r{c}?` in the compound. Two recognisable candidate words, but only one unqualified transcription. |
| 68r.03.1 `-deraria`; 68r.21.1 `mostrare` | `bu` = r | The other non-reserved support is the doubtful `b u{n}? cc` at 298r.18.1, completing `altra`. Reserved `mostrare` improved only after the post-hoc merge. |

I would either mark those five rows **conditional on the unit reading**, or demote them under a definition of strict requiring two independently secure supporting words. This is not evidence that their plaintext is wrong. It prevents the confidence labels from concealing the source of certainty. Other hand values, such as `i` = f and `I` = p, have ample independent lexical support despite the language model preferring alternatives.

There are also publication inconsistencies:

* **298r.H1.4, Victorie:** `reading.md` and `DECISIONS.md` call it **doubt**, correctly. `reading-words.tsv` still calls it **lenient** and says the cluster has four minims. Correct the TSV and its source override to doubt; the four-minim assertion should be withdrawn. This alone changes non-reserved counts to 30 lenient and 12 doubt, without changing strict coverage.
* **198r.18.8, Barbon:** the TSV correctly says **forced**, because `b` = b rests on this name. The prose claim “All strict except questo and exercito” is false. Add Barbon to the exceptions.
* **68r.23.5, tutto:** the note says “b read t,” but the stored unit is **`o`**, whose current value happens to be b. Keep sign labels distinct from plaintext values. The image correction below resolves this particular mismatch without changing the key.
* “Strict words” are really **strict segments**: `scr-`, `-sar`, and `inten-` count, and several rows contain multiple words. The present segment counts must not be presented as numbers of completely read words.

**2. Image checks and exact corrections**

I examined the four supplied JPEGs, each 1962 × 2773 pixels, in page overview and Pillow crops enlarged 2×, with selected difficult groups enlarged 3× or 4×. These were targeted checks, not a blind second transcription: I had read the proposed text. I compared actual strokes with the inventory and repeated instances rather than treating semantic fit as a visual observation.

The following 19 named groups alone contain **174 original sign labels**, before merges and excluding punctuation. Every group was checked on its image. Additional checks on 68r are logged immediately below; thus the requested 40-sign minimum is exceeded across all four leaves. “Agrees” means the inventory labels are defensible, not that every plaintext value is independently proven.

| Location and proposed word | Checked units in current transcription | Image finding |
|---|---|---|
| 298r.H1.2 Suardini | `a p# q 8 s mi no pa` | Agrees; `q` is a distinct descender-bearing sign. Its value a remains name-dependent. |
| 298r.H1.4 Victorie | `p# i n i 7 oo 9+ 8 mi 2` | `-ctorie` is well supported. The initial minim cluster does not establish the normal four-minim `mi` unit. Do not silently replace it with i. |
| 298r.H2.2 Februarii | `i dd 6 8 p# 9 8 mi pa` | Agrees, including paired d shapes and terminal `pa`. The adjacent day looks like clear 26. |
| 298r.08.2 Prosper(o) | `s 2 ss# a I 8 9+ a I= 2 8 ) )` | Stem of Prospero is convincing; the final two separate tall curved strokes really are anomalous. They are not a normal `9+`. |
| 298r.09.5 Carpi | `7 g1 8 I mi` | Agrees at the inventory level; compound `g1` remains a one-word unit/value hypothesis. |
| 298r.12.1 S. Prospero | `s I 8 9+ a I= 2 8 9+` | Prospero proper agrees. Initial `s` decodes d, so interpreting the title as S. is an abbreviation/context decision. |
| 298r.12.2 Carpi | `7 9 8 I mi` | Agrees; a strong clean occurrence. |
| 298r.12.5 heredi | `4 2 8 dd s mi` | Agrees. |
| 298r.13.4 la investitura | `ss# 9 mi x p# 2 a lo mi oo p# 8 9` | Agrees; this is the best direct occurrence of investitura. |
| 298r.17.4 heredi | `4 2 8 2 s mi` | Agrees; useful corroboration with a different e sign. |
| 298r.17.5 Prospe(r)o | `s 2 ss# a I 8 9+ a I= 2 9+` | The missing r is real in this transcription; the image does not warrant pretending that r was read. |
| 298v.02.5 Carpi | `7 9 8 I pa` | Agrees, with visibly distinct `pa` ending. |
| 298v.03.1 al S. Prospero | `cc ss# a I 8 9+ a b i 2 8 9+` | The anomalous `b i` cluster is present. It is not a clean second p occurrence. |
| 298v.03.3 heredi | `4 2 8 dd s pa` | Agrees. |
| 298v.04.6 first part of investitura | `mi x p# a` | **Correction:** last sign is a 2-shaped sign, not the hook labelled a. Read `mi x p# 2` = `inue`. |
| 298v.05.1 continuation | `a lo mi oo p# 8 9` | Agrees as `stitura`. Joined to corrected preceding line, gives `inue|stitura`, with no missing e or doubled s. |
| 298v.06.3 Carpi | `7 9 8 I mi` | Agrees. |
| 198r.18.4 Cremona | `7 8 2 e+ 9+ x 9` | Agrees sign for sign. Cremona is secure under the recurrent alphabet. Tortona is not supported. |
| 198r.18.8 Barbon | `b 9 8 b 9+ x` | Agrees, including repetition of b. This confirms the pattern, not the name-dependent b value. |

The principal Pillow crop rectangles, in original pixels `(left, top, right, bottom)`, were: 298r heading `(500,180,1550,385)`, lines 08–09 `(290,985,1740,1230)`, 11–13 `(280,1290,1730,1585)`, 15–18 `(290,1615,1740,1985)`; 298v lines 01–05 `(430,340,1845,820)`, 06–08 `(430,815,1830,1085)`; 198r lines 17–18 `(240,1520,1680,1740)`. The decisive 298v line-end crop was `(1650,640,1840,755)` at 4×.

For **68r**, I inspected the feigned-illness text at lines 03–05 and 10–19, all reserved lines 20–23, and additional crops of lines 02 and 07–09. In particular:

| Location | Sign-level finding and consequence |
|---|---|
| 03.1 `deraria` | The b/u-shaped group is visible. Whether it is one r unit is a decoding hypothesis; the image does not independently assign r. |
| 03.4 `caval(c)assimo` | Current output is `caualasssimo`, not cavalcassimo. The missing c and surplus s must remain explicit. |
| 03.5 `se ben`; 15.3 `indebilita` | The H-like cluster is unlike a normal keyed b. `H i` = b is a conjectural repair, not a recovered value. |
| 04.4 `infirmita`; 04.5 `potessimo`; 05.1 `valcare` | The recurrent `mi`, `no`, `lo`, `la`, and `dd` groups are defensible and the core clause survives. |
| 05.5 `Milano` | The difficult p-like sign remains ambiguous; stored output is `milauo`. Do not count this as another clean x/no = n occurrence. |
| 07.6 / 08.1 putative personal name | `cchilte` / `borronei` remain imperfect outputs. Neither Achille nor Borbone/Borrone is established by the signs. Withdrawal of Borbone here was appropriate. |
| 10.1 `dove venire` | The extra 7/c in `douecuenire` is visible. The prose and translation still omit it; this is not a literal reading. |
| 11.2 `cavalcato` | Compound a-shaped group present; its exact second component is less secure than the surrounding signs. Existing forced tier is appropriate. |
| 11.4 `l'altro`; 11.6 `cavallo`; 17.1 `alli` | The tall-stroke/loop unit is present where `lo` is recorded. Current outputs are `lattro`, `caualto`, `alti`. The l substitutions are contextual, not image-verified alternative values. |
| 12.1 `mostrando` | The transcription records two a-valued signs; current output `mostraando` should remain visible alongside the normalised word. |
| 12.7 `stancato`; 14.3–5 `mostrassimo haverne sinistrato`; 15.2 `schina` | Recurrent signs support these substantial portions of the riding/back-pain passage. |
| 13.6 `gian-`; 16.6 `mandato` | Minim count and `mo`/`no` distinctions need caution; current alternatives should not be erased because the words are plausible. |
| 16.3–5 `havemo questa matina` | Agrees; a useful independently readable lead-in. |
| 17.2 `medici` | The fifth unit has the angular top expected for 7. The earlier 9→7 correction is defensible. |
| 17.5–7 `orine fatte tingere` | Agrees, including `pa` in orine and both t units in fatte. This is strong direct cipher evidence. |
| 18.1–3 `a posta con sangue` | Agrees. The intentional dyeing of urine is supported without needing to perfect the rest of the sentence. |
| 18.5 `facendo` | The two problematic signs remain compatible with the recorded `7 7`; no clean image warrant for silently changing the first to 9. Output `fccendo`, reading facendo, lenient. |
| 18.6–8 `uscire voce che` | A single 7 occurs in uscire. The prior deletion of the duplicate 7 is defensible. |
| 19.2 `[9 9]` | **I cannot locate this separate segment between havemo and orinato.** The image goes from the terminal `bb` of havemo to `9+ 8 mi x ...`. Treat the segment as probably spurious and remove it if its claimed image position cannot be demonstrated. |
| 19.3 `orinato` | The suspect 7/9 is curved enough to merit rechecking, but I would not promote 9 to certain. Current `orincto` is not a strict reading of orinato. |
| 20.1 `fatto` | `bb` is visible; output fatto agrees with the proposed value, but this reserved occurrence cannot retrospectively supply training support. |
| 20.2 `scriver(e)` | The image is not a clean transcription of a regular scrivere under the current key. Raw `scruerbs` must be retained. |
| 21.1 `mostrare` | The `bu`-shaped group is visible. Its successful current decode is post-hoc, as disclosed. |
| 21.3 `[l]` | Heavily overwritten/crossed mark, possibly cancelled. Not a reliable independent word, even though the lexicon counts `l`. |
| 21.4–6 `Duca di Sessa` | Agrees sign for sign: `s p# 7 9 / s mi / a 2 a la 9`. This is a strong name/title sequence. |
| 21.9 + 22.1 `ve(r)ra?` | **No sign change required:** `p# 2 I cc / 8 mi 8 9` gives `uepa / rira`. Read **ve parirà**, “as you see fit,” in `et a chi ve parirà`. The proposed verrà discards real p, i, and r evidence. |
| 22.6 `sa(n)o`; 22.8 + 23.1 `ga(g)liardo` | The anomalous 8+ and H remain anomalous. The historical quotation confirms the likely intended words, not the values of these signs. |
| 23.4 `fossimo` | **Probable correction:** the large crossed-loop e+ seems to be followed directly by 9+, without an independent s. Suggested transcription `i 9+ a la mi e+ 9+`, giving fossimo. Less certain than the following correction; do not alter the frozen control on this basis. |
| 23.5 `tutto` | **Clear correction:** after `lo` there are two joined loops, `oo`, not a lone o. Suggested units `oo p# lo oo 9+` give tutto directly. No o = t exception is needed. |

68r crop rectangles: lines 03–05 `(320,605,1735,885)`, 10–12 `(320,1190,1740,1475)`, 13–16 `(320,1470,1740,1815)`, 17–19 `(320,1790,1735,2070)`, 20–23 `(320,2050,1740,2410)`. The absence of 19.2 was rechecked at `(260,1910,1750,2085)`; the end of 23.4 and 23.5 at `(760,2260,1320,2400)` enlarged 4×.

The most useful corrections are therefore **298v.04.6 a→2**, **68r.21.9–22.1 ve parirà**, and **68r.23.5 o→oo**. The last two are review-stage findings on reserved lines. They must never be folded into the old frozen score and called predictions.

**3. Values, contradictions, and unit merges**

The frequent alphabet has multiple mutually supporting words across leaves. Hand assignment is not itself a defect. What matters is whether a proposed value survives occurrences outside its generating word. I find adequate recurring support for `ss#` = l, `i` = f, `I`/`I=` = p, `la` = s, `6` = b, `pa` = i, `bo`/`d` = q, and the other frequent A values, with the specific exceptions below. The LM's disagreements do not overturn such evidence; conversely, its agreement cannot turn a guessed proper name into independent support.

| Weak or exceptional value | Assessment |
|---|---|
| `q` = a, Suardini at 298r.H1.2 | Plausible completion of a highly constrained name; only one occurrence. Keep forced. It cannot independently prove both the name and q's value. |
| `g1` = a, Carpi at 298r.09.5 | Strong contextual candidate because Carpi recurs with other a signs. Still only one example of this compound; keep forced and do not equate its shape with `gr` without qualification. |
| `o` = b, bene at 298r.04.2 | Plausible from bene servita, but most other lone-o contexts are unread. It does not generalise convincingly enough for A/B. The apparent contradiction in reserved tutto is likely a transcription error, not evidence for a second o value. |
| `bb` = o, havemo at 68r.19.1 | Better than a bare arbitrary guess: `etue[l]o` at 19.5 and reserved fatto at 20.1 fit too. However, these are contextual/reserved corroborations, not two clean pre-reservation word types establishing the value. Current forced tiers are conservative and acceptable. |
| `c` = e, exercito at 198r.17.3 | Weak: the same proposed word also needs x to stop reading n. Raw output is enercito. Other c occurrences are in doubtful/probably clear 68r.02 text. Keep conjectural. |
| `S` = d, denari at 298r.15.5 | Weakest kind of support: the generating word also requires i to read e instead of its well-established f. Raw dfnari is not independent evidence for denari. Keep lenient; S = d is a candidate, not a demonstrated key value. |
| `b` = b, Barbon at 198r.18.8 | The repeated b positions are compatible with Barbon and its historical identification. After rejecting Borbone on 68r, there is only one identifiable supporting name. `b i` in 298v.03.1 and b in 68r.20.2 do not provide clean confirmation. Keep forced. |
| `p+` = u | Sua, un, and qualche uno give plausible repeated support, though not all are clean standalone decipherments. At 298r.12.3, the same labelled sign must mean **per**, yielding current raw ului versus proposed per lui. Its shape is compatible with the ordinary clear-text abbreviation. Record a possible clear abbreviation or distinguish graphic uses; do not call p+ globally single-valued. |
| `p#` = u/v, exceptional per | The ordinary u/v value has abundant support. But 298v.04.2 gives raw `ulamorte`, rendered per la morte by assigning the initial p# the abbreviation value per. This is another explicit exception or clear/cipher classification problem, not a strict application of the alphabet. Its existing lenient tier is appropriate. |
| `C@` = q, questo at 198r.17.2 | Only a conjecture. The published JSON actually leaves it null, and the decoder produces `[C@]uesto`. This restraint is appropriate; statements that the key contains C@ = q are inaccurate. |
| `u` | Null in the final key, not an accepted one-word value. The frozen model used u = r before the bu merge. Keep the two states distinct. |
| `mo` = m; `gr` = a; `bu` = r | Plausible working values, but partly supported by uncertain unit transcriptions. See the five conditional-strict rows above. The final-key readability of reserved mai/mostrare corroborates them only after the earlier exposure and post-hoc changes. |
| `H`, `8+`, `) )`, BOX, IZ, CROSS | No stable recovered values. The intended words around them do not license adding g/n/o/person identities to the key. |

There are genuine tensions with a single substitution scheme: `lo` gives t where the reading wants l; `p+` and `p#` give u where particular readings want per; x gives n in the proposed exercito; i gives f in proposed denari; H would require incompatible treatments in se ben, indebilita, and maneggiassimo. These tensions are mostly disclosed. They should remain visible instead of being described collectively as merely “spelling.” Some may be transcription or copying errors, but that explanation is not established for each instance.

The merges themselves divide as follows:

| Merge | Verdict |
|---|---|
| `mi`, `oo`, `cc`, `dd` | **Defensible and strongly supported** as recurring decoding units. Their compound strokes recur in several lexical environments. This does not mean every difficult minim cluster is mi. |
| `no`, `la`, `pa`, `bo` | **Defensible**, supported by multiple environments and visible repeated shapes. The model's inconclusive split test for pa does not negate its repeated function in name/word endings, including orine. |
| `lo` | **Defensible as a unit; unresolved as a value distinction.** Frequent t is secure. No repeatable graphic rule separating t from l has been demonstrated. |
| `bb` | A plausible graphic unit with a provisional value. Repeated shape alone does not establish o. |
| `mo` | Plausible, but the m/n minim distinction in supporting examples needs care. Do not count giam→gian as confirmation of m. |
| `gr`, `g1` | Plausible compound units; gr has two proposed word contexts, one graphically uncertain, and g1 has one. Their common value does not prove that they are the same sign. |
| `bu` | Plausible **post-hoc** unit decision, not a demonstrated model result. The split/merged test is inconclusive, and two hand-selected words drive it. Retain that label even though it improves mostrare. |

For `lo`, the known l-demanding locations are 298r.01.1, 298v.01.1, 68r.11.4, 68r.11.6, and 68r.17.1; the conjectural Achille at 68r.07.6 would add another. None is strict in the TSV. That part is honestly handled. The prose notation `Cancel(l)ere`, however, suggests inserting a missing l; the actual operation substitutes l for decoded t. Show `canceltere → cancellere`, or otherwise mark substitution explicitly. A doubling-device explanation remains speculation, especially because l'altro does not put lo immediately after ss#.

Occurrence counts are not support counts. For example, the count for 6 includes the probably clear day 26, while some c/bo instances lie in probably clear words on 68r.02. Such entries should not be used as extra cipher evidence.

**4. Controls: reproducible arithmetic, contaminated validation**

I executed the body of `controls6.py` in memory, omitting its final file-writing statement. The final-key results reproduce the stored post-hoc figures:

| Measure | Observed | Null mean | Null sd | z | Empirical p |
|---|---:|---:|---:|---:|---:|
| Reserved all segments, final key | 20/31 | 4.815 | 1.615789 | 9.397884 | 1/201 |
| Reserved fully keyed segments of 4+ letters, final key | 11/20 | 0.060 | 0.237487 | 46.065710 | 1/201 |
| Non-reserved lexicon hits, final key | 81/191 | 18.995 | 5.935906 | 10.445752 | 1/201 |
| Non-reserved LM score, final key | -3256.097 | -4734.654 | 101.613 | 14.551 | 1/201 |

For the frozen reserved calculation, I removed bu from the merges and key, and restored u = r in memory, as indicated by the frozen output/LOO record. This reproduces its raw reserved strings and both headline results exactly: **19/31, z = 8.778991**, and **10/20, z = 41.854950**. The same reconstruction does not exactly reproduce the frozen whole-text result on today's transcription, which contains later image corrections; I do not claim it does. There is no complete immutable pre-refinement snapshot demonstrated here.

The implementation currently excludes reserved rows from round-6 annealing and context lookup, as claimed. `RESERVED.md` states the lexicon and scoring rules, and the files clearly distinguish the later bu improvement. These are good practices. They do not erase the explicitly admitted earlier fitting of anneal5 on **all** lines, the printed decode seen before reservation, or the possibility that line selection was informed by that exposure. A current Markdown assertion that rules were frozen is not itself independently timestamped proof of the chronology.

The correct interpretation is: **the fitted key produces much more Italian-like text than shuffled versions of its values, including on a previously exposed subset omitted from later refinement.** The stronger claim in `controls.md` that the reserved figure “tests prediction” is not justified as an independent validation. A random-key null does not model the process of fitting many keys/merges and inspecting their outputs. The non-reserved test's circularity is already acknowledged; the reserved test shares part of that problem.

Precise reporting corrections:

* The frozen units total **136**; the final bu-merged reserved text totals **135**. Specify which state is being counted.
* The 4+ denominator is **20 fully keyed segments**, not all long segments. There are **22** segments with at least four units: 68r.22.6 `sa[8+]o` and 22.8 `ga[H]li` are excluded by the complete-key condition. If the aim is coverage including unread long segments, report 10/22 frozen and 11/22 final. The observed hit counts and shuffled-score comparison do not change. The frozen rule's phrase “segments that decode to 4+ letters” allows the existing denominator, but it must be stated explicitly alongside the rule that unread material counts as a miss.
* The one-letter `l` at 68r.21.3 is a lexicon hit from a heavily overwritten, possibly cancelled sign. Excluding it gives 18/31 frozen and 19/31 final, as a sensitivity count, not a recomputed p-value. The existing caveat correctly identifies the lexical issue.
* Lexicon hits include fragments such as `inten` and strings such as `perla`, whose intended segmentation is per la. Call this a **lexicon-string score**, not a literal census of independently correct period-Italian words.
* `p = 1/201 = 0.004975...` means none of 200 shuffled keys scored as high. It is not the probability that the decipherment is wrong. The huge 4+ z values arise from a very low-variance discrete null and should not be read as Gaussian “42-sigma” or “46-sigma” validation.
* My image corrections to reserved lines, and the improved ve parirà interpretation, are **post-review** findings. Preserve both original scores unchanged. A future genuinely unseen passage, transcribed and frozen before decoding, would provide the missing predictive test.

**5. Historical claims, dating, and what the cipher actually establishes**

| Claim | Verdict and correction |
|---|---|
| Charles V at Vitoria, January–February 1524 | **Holds.** EFE's account, based on the local historical association's research, places his stay from 5 January to 6 March 1524. Thus 26 February fits. This supports the historical plausibility of Victorie; it does not repair the minim cluster or independently date an otherwise yearless heading. [EFE, 30 December 2023](https://efe.com/pais-vasco/2023-12-30/carlos-v-vitoria/). |
| Carpi promised/granted to Prospero before his death, investiture unissued | **Holds.** Franca Petrucci's biography explicitly reports the grant without investiture. The claim in `reading.md` that the cipher “adds” the non-investiture detail is therefore not a novelty claim that can stand. The heirs and proposed compensation are supported within the letter, but their novelty would require a further literature/edition check. [Petrucci, DBI 27 (1982)](https://www.treccani.it/enciclopedia/prospero-colonna_%28Dizionario-Biografico%29/). |
| Carpi taken from Alberto Pio | **Holds with chronological correction.** Fabio Forner dates an initial expulsion to **3 January 1523**, when Prospero commanded the imperial army, followed by recovery through Alberto's brother in August 1523. He separately dates renewed imperial occupation to **9 March 1525**, after Pavia. The Wikipedia passage cited in the reading discusses the latter phase and subsequent forfeiture. Do not carry that later felony/confiscation narrative backward as a completed legal settlement in February 1524. The cipher's `di ragione Carpi ... tolto` expressly raises the legal uncertainty. [Forner, DBI 84 (2015)](https://www.treccani.it/enciclopedia/alberto-pio_%28Dizionario-Biografico%29/); [the cited Alberto Pio account](https://en.wikipedia.org/wiki/Alberto_III_Pio). |
| Prospero died 30 December 1523 | **Holds only as late December 1523; exact day needs correction/qualification.** The requested 30 December differs from the 28 December cited in the existing reading, while Petrucci's DBI biography gives **31 December 1523**, at Milan. I would write “late December 1523” unless resolving that source discrepancy from contemporary records. All these dates fit news reaching Spain by February; none is supplied by the cipher. [Petrucci](https://www.treccani.it/enciclopedia/prospero-colonna_%28Dizionario-Biografico%29/). |
| Duke of Sessa as imperial ambassador in Rome in 1524 | **Holds.** The Royal Academy identifies Luis Fernández de Córdoba, second Duke of Sessa, as Charles V's Roman ambassador. The published state papers contain 1524 correspondence explicitly identifying Sessa in that office, including July entries 662–663. The reading of Duca di Sessa at 68r.21.4–6 is also directly supported by the key. [Real Academia de la Historia](https://historia-hispanica.rah.es/biografias/15460-luis-fernandez-de-cordoba); [*Calendar of State Papers, Spain*, July 1524](https://www.british-history.ac.uk/cal-state-papers/spain/vol2/pp647-650). |
| Federico feigning illness to avoid taking the field | **Holds strongly as identification of the episode.** Benzoni describes the very specific urine deception and identifies Castiglione as recipient of Federico's admission. The stated reason is lack of funds from Rome and Florence. That is firmer evidence than the reading's unverified explanation about avoiding service without the Pope's wish. It does not independently identify “salve,” resolve every cipher sign, or establish an exact January date. The supplied 68r face has no visible dated heading. [Benzoni](https://www.treccani.it/enciclopedia/federico-ii-gonzaga-duca-di-mantova-e-marchese-del-monferrato_%28Dizionario-Biografico%29/). |
| Bourbon, April 1524, rivers and Pavia/Cremona/Milan | **Holds with interpretation limits.** Bourbon's participation on the imperial side and the French retreat toward Novara fit the campaign; the broader French retreat culminated in the Sesia fighting later in April. But the cipher says `se retirera`, a prospective withdrawal, embedded in a condition about reinforcements and a truce. It does not report that Bourbon actually followed the listed itinerary. The places read Pavia, Cremona, Milano; their listing can describe fallback destinations, not necessarily a sequential march through all three. “Questo exercito” most naturally refers to the writer's own force, contrasting with the enemies in Novara, but that referent remains an interpretation. [Bourbon biography, imperial service](https://en.wikipedia.org/wiki/Charles_III,_Duke_of_Bourbon); [Sesia campaign overview](https://en.wikipedia.org/wiki/Battle_of_the_Sesia_%281524%29). |
| Archbishop of Capua negotiating a truce in spring 1524 | **Holds.** Contemporary dispatches record Nicholas Schönberg's mission, his arrival at Burgos on 14 April, and his negotiations with Charles V. This is specific support for the diplomatic setting of 198r.16, without proving the predicted retreat occurred. [*Calendar of State Papers, Venice*, April 1524, entries 818–822](https://www.british-history.ac.uk/cal-state-papers/venice/vol3/pp359-364). |

Two translations need substantive correction independently of historical identification:

* **68r.21.8–22.1:** `et a chi ve parirà` means “and to whomever you see fit [to show it],” not “and to whoever comes.” This preserves every current key value and the line division. Grade the joined reading as strict under the existing mechanical rule, while keeping the original frozen lexicon score unchanged.
* **68r.09 clear text + 10.1:** “il quale sapevamo dove venire” does not justify the supplied “[find]” in the English. Raw `douecuenire` is unresolved. A construction with dovea venire is plausible, but would require a justified treatment of the extra c and should remain a conjecture, not a completed translation.

The safe substantive conclusions are a negotiation over Carpi and Prospero's heirs, an admission of deliberately simulating illness, and a conditional military withdrawal toward named Lombard strongholds. The uncertain letterforms, proper-name completions, unidentified persons/codes, and historical motives should remain separate from those conclusions. No existing file was corrected as part of this review.
