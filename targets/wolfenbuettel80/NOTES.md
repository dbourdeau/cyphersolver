# The cipher on folio 103v

Herzog August Bibliothek, Cod. Guelf. 80.4 Aug. 8°, catalogue 3897 (lead 3656 before it passed the gate; removed from the catalogue at this write-up). A reader added a German judgment below an alchemical recipe. The host volume dates to the fifteenth century. The cipher addition is undated. [Library catalogue](https://diglib.hab.de/?catalog=Heinemann&db=mss&id=80-4-aug-8f&list=ms)

## Reading

**Status: read in part (26 Nov 2026).** By the README word rule (sure words only), 8 of the 11 cipher words come out of the key with nothing supplied (72.7%). Three words carry supplied letters: *da[s]*, *wec[gk]* and *philo[s]ophei*. The short-text floor allows at most two holes in a text under 40 words, so it does not apply and the note is read in part, not read. By signs, 48 of 52 take a value from the key (92.3%).

> Mich dunct also, da[?s] dises der rechte wec[?gk] ist der philo[?s]ophei.

“It seems to me, then, that this is the true way of philosophy.” The word for “way” begins *wec-* and has two further signs. Their proposed values yield *wecgk*. The evidence for the word is stronger than the evidence for the precise order and values of the final consonants. The writer splits *philo-sophei* between manuscript lines. Punctuation and capitalization are editorial. [Full-resolution manuscript page](https://diglib.hab.de/mss/80-4-aug-8f/max/00218.jpg)

| Line | Signs, grouped as written | Literal substitution |
|---|---|---|
| 1 | `7T25 3KL2D 96yV` | mich dunct also |
| 2 | `39J 3Ty4y 34B B425D4` | da? dises der rechte |
| 3 | `O42FE TyD 34B 85T6V` | wec?? ist der philo |
| 4 | `jV854T` | ?ophei |

## How the key was recovered

Codex (GPT-6) transcribed the manuscript images and used the Python programs in this folder to test the key. A word-boundary four-letter frequency search tried substitution keys against the repository's Dutch, German, Latin, Danish and French lexicons. The German run on a preliminary transcription gave *mihr ducht also dam dises den nehrte gehey ist den brilo mobrei* and *distil* below. The German syntax suggested *mich*, *der rechte* and *philosophei*. The corrected values also gave *aceto* in the text below and Latin words on the closing leaves. The mixed lines and scanned pages had been inspected before the search. These cross-checks should not be counted as a blind trial. The adjacent alphabet on 104r assigns the 3-like form to i, whereas the 3-like form repeatedly gives d here. [Facing alphabet](https://diglib.hab.de/mss/80-4-aug-8f/00219.jpg)

The sign labels 2, 3, 4, 5, 6, 7 and 8 resemble the corresponding digits. The 9 label denotes an open loop descending into a tail. T is a crossed 5, B a marked 6, K a crossed 2, D a small triangle, L a right angle, V an upturned or check-shaped stroke, and y a fork with a descender. The letter names in the transcript are arbitrary. Run `python targets/wolfenbuettel80/decipher.py` from the repository root to print the key output, including unresolved signs.

## Checks elsewhere on the leaves

- **HAB image 00030.** The annotation starts `3T4 O4Tyy4 3T4 T25`, giving *die weisse die ich*. The dotted circle supplies w. [Image 00030](https://diglib.hab.de/mss/80-4-aug-8f/max/00030.jpg)
- **HAB image 00155, f. 74r.** The same circle gives *worden* in `OVB34L` after *der do rot ist*, and *wol* in `OV6`. Further down, the clear words *unnd ein* introduce a coin that is to be rubbed with the mixture. The numeral-like p, apparent f and `4LLTF2E` give *pfenni?c?*. Reading this as *pfennigck* gives g for the footed 4 and k for the marked 2. The two uncertain signs occur on either side of c here, but both follow c on 103v. The decoder preserves those orders. [Image 00155](https://diglib.hab.de/mss/80-4-aug-8f/max/00155.jpg)
- **Historical spelling.** The Hessian place-name register transcribes *Walterlebacher weckg* in 1432. This supports the identification of *Weg* from *wec-* plus two consonants. Its final two letters are in the opposite order from the proposed *wecgk* on 103v. [Hessian register, Haingrund](https://www.lagis-hessen.de/de/subjects/rsrec/chapter/merged/sn/shfb/register/ort/rsq/437010020/entry/haingrund)
- **HAB images 00036 and 00074.** The first inscription mixes large initials, the mercury sign and cipher letters to give *Oleum ☿ est fermentum* (“the oil of mercury is the ferment”). The second ends in *uitriolum* (“vitriol”). Both readings use the same letter values as the closing leaves. [Image 00036](https://diglib.hab.de/mss/80-4-aug-8f/max/00036.jpg) · [Image 00074](https://diglib.hab.de/mss/80-4-aug-8f/max/00074.jpg)

- **103v, below the sentence.** `924DV` gives *aceto* (“with vinegar”) and `3TyDT6` gives *distil*. A further group after the clear word *den* begins *essi-* and runs into the binding. German *Essig* (“vinegar”) supports the Latin reading *aceto*. [Folio 103v](https://diglib.hab.de/mss/80-4-aug-8f/max/00218.jpg)
- **104v, three labels.** The first gives *spirtus*, evidently *spiritus* (“spirit”), with one i supplied in expansion. The large C and following *orpus* give *corpus* (“body”). The third reads *anima* (“soul”), with the library stamp overlapping its beginning. [Folio 104v](https://diglib.hab.de/mss/80-4-aug-8f/max/00220.jpg)
- **105r, mixed Latin.** The first two groups give *mercuricm* and *sulphurem*. The intended first word is very likely *mercurium* (“mercury”), with a plain or weakly marked 2 where a crossed 2 would give u. A third group between the clear *Et* and *in aquam* gives *salem*. Thus the first three lines name mercury, sulphur and salt. [Folio 105r](https://diglib.hab.de/mss/80-4-aug-8f/max/00221.jpg)

The remaining cipher groups on 105r are less distinct. After *in aquam*, an apparent f and `T?D` suggest *fiat*, while `yV6K7` gives *solum*. The next line has clear *sepe*, then `9ByV` (*arso*), an apparent footed 4 beside a smudge, and a longer group giving *s?lui?t*. The lower line has clear *fiat* and `yK68KB` (*sulpur*, “sulphur”). The clear conclusion *et habebis quod optas* means “and you will have what you desire.” These fragments do not yet yield a continuous translation of this separate recipe. [Full-resolution image 00221](https://diglib.hab.de/mss/80-4-aug-8f/max/00221.jpg)

## Transcription doubts

- **J and j, 103v.** - read: both s values provisional; checked: image, decode; These descended, 7-like signs differ from the short 7 of *mich* and from the forked sign in *dises*. The contexts *da[s]* and *philo[s]ophei* suggest s. The key leaves both shapes open.
- **O42FE, 103v.** - read: wec with provisional g and k; checked: image, decode; The five apparent signs are a dotted circle, a 4, an angular 2, a footed 4-like form and a barred 2. Comparison with images 00030 and 00155 resolves O as w. The proposed F and E values depend on the coin name on 00155. Direct substitution then gives *wecgk*. The transcribed *weckg* in the historical register makes an alternate order worth recording. The strict decoder retains *wec??*. Images 00222–00224 show blank leaves or binding material.
- **Last sign at the fold, 103v.** - read: essi followed by an unresolved sign; checked: image, decode; The visible beginning suggests *essi[g]*. Too little of the last glyph survives in the photograph to use it as a key for g.
- **Third label, 104v.** - read: anima, initial a partly obscured; checked: image, decode; The left edge is obscured by the stamp. The surviving loop and the readable *nima* support the initial a.
- **First group, 105r.** - read: mercuricm, likely mercurium; checked: image, decode; The penultimate sign lacks the clear cross-stroke visible earlier in the word. Both the literal output and the proposed expansion are retained above.

## Remaining gaps
- the two descended 7-like signs J and j, s in da[s] and philo[s]ophei - blocker: too-short; each occurs once in the four lines and no annotation read elsewhere in the volume gives either shape a value, so s is supplied from the sense
- the last two signs of wec?? (F and E, read g and k) - blocker: too-short; their values rest on one coin name on image 00155 (pfenni?c?), where they stand on either side of c, while the 1432 spelling weckg has the opposite order; no other occurrence fixes them

## Escalation
- [x] siblings: the other cipher annotations of the volume read for comparison (images 00030, 00036, 00074, 00155; 103v below the note; 104v; 105r); none gives J, j, F or E a value beyond the proposed g and k from 00155
- [x] clear-pages: the facing alphabet on 104r (image 00219) checked; it gives the 3-like form as i where the note needs d, and has no value for the open signs
- [x] known-keys: the alphabets on 104r and 00220 compared sign by sign; neither supplies the four open signs
- [x] print: Heinemann (1903) pp. 151-152 and Lang, Zotov and Piorko (2024) searched; no reading of the note or of the alphabets
- [x] key-rebuild: g and k proposed for F and E from the coin name on 00155; kept out of the strict decoder because the order is unconfirmed
- [x] retry: decipher.py re-run with the strict key on all four lines (26 Nov 2026); the same four signs stay open
