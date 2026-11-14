# mirabel1622 - the ciphered letters of BNE MSS/18428 that were deciphered at the time (verification, 14 Nov 2026)

BNE MSS/18428 holds seven 1622 letters of the Marquis of Mirabel in this cipher. Six carry a contemporary decipherment by Gondomar's
secretary; only the letter of images 13 right - 15 left (this target's reading) has none. The six are **already read by their
contemporaries**: nothing is claimed here as a new decipherment of them. They were used as cribs ("rosettes") to extend the
coloma1622 key C04 into CLE_M02 (key.tsv, column source), and are listed so that the reader can check where each value comes from.

| viewer images | letter | contemporary decipherment | used for |
|---|---|---|---|
| 5 right - 7 right | Paris, early 1622 (Valtelline, Feria, Grisons) | margin clears (5 r, 6 l, 6 r, 7 r), interlinear on 7 r | 4‡ = g, y = g, _113_ DUQUE DE FERIA, 60 = i, 221 FUERZA, _71_ COMO, _89_ |
| 31 right - 32 left | Paris, 1622 (Jülich, Valtelline capitulations, Don Manuel de Portugal) | full clear copy on a separate leaf, fol. 31 (image 32 right) | 267 INDIAS, 202 ESPAÑA, _89_ CUYDADO, _180_ AVISA, 257 HIJO, _97_ CARTA, _21_ MAURICIO, ar = ma, σ = mo, 141 ELLO, 318 OFICIO |
| 34 right | Paris, March 1622 (Feria, "lo capitulado en Madrid") | clear copy image 33 left (attached 13 Nov 2026: same text) | 308 34ʳ NUESTRO SEÑOR, _0_ REBELDE, 319 OTRO, 280 ITALIA, 221, 260 |
| 38 right - 40 right | Paris, 17 March 1622 | full clear copy on a separate leaf, images 39 right - 40 left | 308 NUESTRO, 141 ELLO, _49_ BUEN, _56_ CAPITULA, 225 FUERTE, _39_ BIEN, _80_ CONDE, _100_ DIOS, 86 os, ō = t, fiz = que, zon = yo, sa = al, g = p |
| 41 right - 42 left | Paris, 30 April 1622 | margin clears of image 41 right | nothing new (_140_ era, _31_ ALGUN-, 246 GENTE confirmed) |
| 44 right | Paris, 1622 | margin clear (coloma1622 held-out test H5) | ō = t (same word "ministros"; noted Ð in the H5 transcription of coloma1622) |

The inventory of 9 Nov 2026 (issue #367) counted five letters with a contemporary clear and one (image 34 right) "possibly covered";
the attachment of image 33 left to image 34 right was checked on 13 Nov 2026, so six of seven are covered.

## Decoding the aligned passages with CLE_M02

Learning data, not a test (the values were read on these same clears). Normalisation: lower case, no accents, v = u, j = i, y = i,
h dropped, ll = l; character agreement = 2 x matched / (decoded + clear). Clear words standing inside the cipher (para, vn, creencia)
are kept as written. Labels: v32 g = viewer image 32, left page; d = right page.

| letter (cipher / contemporary clear) | cipher | key CLE_M02 decodes | contemporary clear | char. agreement |
|---|---|---|---|---|
| v32 g / fol. 31 (v32 d) | `para 58‡ 81 f _136_ Δ` | para ? lo s ENEMIGO s | para los enemigos | 1.00 |
| v32 g / fol. 31 (v32 d) | `fe xe σ Δ` | te ne mo s | tenemos | 1.00 |
| v32 g / fol. 31 (v32 d) | `75 _31_ Δ 214` | i ALGUNA s FRANCES | y algunos franceses | 0.88 |
| v32 g / fol. 31 (v32 d) | `83 267 62 cir 55 x fa 79 Δ` | as INDIAS o ri e l ta le s | as indias orientales | 0.94 |
| v32 g / fol. 31 (v32 d) | `98 91 m _141_ Δ` | ca bo d ELLO s | cabo dellos | 1.00 |
| v32 g / fol. 31 (v32 d) | `202 93 _89_` | ESPAÑA da CUYDADO | españa da cuydado | 1.00 |
| v32 g / fol. 31 (v32 d) | `_180_ 7 71 81 Δ 318 Δ` | AVISA r i lo s OFICIO s | avisar y los oficios | 1.00 |
| v32 g / fol. 31 (v32 d) | `sor x 84 fe tu` | co l es te REY | con este rey | 0.90 |
| v32 g / fol. 31 (v32 d) | `vn 257 93 f fe` | vn HIJO da s te | un hijo deste | 0.90 |
| v32 g / fol. 31 (v32 d) | `_97_ f fur creencia` | CARTA s de creencia | cartas de creencia | 1.00 |
| v32 g / fol. 31 (v32 d) | `fer 94 67 57 σ f fe xe 8 fur fo 93 84 fa 246` | fer de u e mo s te ne r de to da es ta GENTE | que devemos tener de toda esta gente | 0.93 |
| v32 g / fol. 31 (v32 d) | `20 son 98 7 78 σ xa 82 V 58‡ fur 202` | a po ca r la mo na lu h ? de ESPAÑA | a apocar la monarquia de españa | 0.88 |
| v38 d - v40 d / v39 d - v40 g | `fi 308 Δ _136_` | ti NUESTRO s ENEMIGO | porque nuestros enemigos | 0.77 |
| v38 d - v40 d / v39 d - v40 g | `chu _140_ 94 202` | fu era de ESPAÑA | fuera de españa | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `71 xar 80 f os Δ sor x̣ _141_ 75` | i sa li s mo s co ? ELLO i | y saliamos con ello y | 0.90 |
| v38 d - v40 d / v39 d - v40 g | `246 71 xir` | GENTE i si | gente y si | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `_49_ 30 sor fri 93` | BUEN a co gi da | buena acogida | 0.96 |
| v38 d - v40 d / v39 d - v40 g | `78 f _56_ sir 62 x Δ` | la s CAPITULA ci o l s | las capitulaciones | 0.91 |
| v38 d - v40 d / v39 d - v40 g | `81 94 66 sa fo 80 xa` | lo de u al to li na | lo de valtolina | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `94 fo 96 f 308 f` | de to do s NUESTRO s | de todos nuestros | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `78 98 69 xar as f 225 san car 78` | la ca u sa ma s FUERTE pa ra la | la causa mas fuerte para la | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `xo chu _140_` | no fu era | no fuera | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `_39_ fi Δ fo xo Δ` | BIEN ti s to no s | bien que esto nos | 0.77 |
| v38 d - v40 d / v39 d - v40 g | `faz ō car 56` | que t ra e | que trae | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `is xi f ō cor Δ` | mi ni s t ro s | ministros | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `75 fiz xir ss tt 96` | i que si e n do | y que siendo | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `71 g cor fe Δ fa tt fe f` | i p ro te s ta n te s | y protestantes | 1.00 |
| v38 d - v40 d / v39 d - v40 g | `_100_ 81 V ŧ fra` | DIOS lo h ? ga | dios lo haga | 0.94 |
| v6 g (margin) | `xo sun 55 94 sa 98 8 98 89 98 san car 93 8 xo f _89_` | no pu e de al ca r ca ve ca pa ra da r no s CUYDADO | no puede alzar cabeza para darnos cuidado | 0.91 |
| v6 d (margin) | `sor tt 81 f 4‡ c̣ir xor xe Δ` | co n lo s g ? so ne s | con los grisones | 0.92 |
| v5 d (margin) | `fon se _113_` | por el DUQUE DE FERIA | por el duque de feria | 1.00 |
| v7 d (margin) | `x̣ xer 66 60 40` | ? se u i a | se veia | 0.91 |
| v7 d (margin) | `sa _136_` | al ENEMIGO | al enemigo | 1.00 |
| v34 d / v33 g | `62 g cer xir 96 se tu 308 34ʳ` | o p re si do el REY NUESTRO SR | ofrecido el rey nuestro señor | 0.85 |
| v34 d / v33 g | `78 f 221 Δ 94 f fe tu` | la s FUERZA s de s te REY | las fuerzas deste rey | 1.00 |
| v34 d / v33 g | `xur f _0_ f` | su s REBELDE s | de sus rebeldes | 0.92 |
| v34 d / v33 g | `71 319 Δ` | i OTRO s | y otras | 0.83 |
| v34 d / v33 g | `san car 280` | pa ra ITALIA | para italia | 1.00 |
| v44 d (margin, H5) | `is xi Δ ō cor f` | mi ni s t ro s | ministros | 1.00 |

39 segments, 243 tokens (6 without value in CLE_M02); characters of the clear matched 515/559 = 0.921
