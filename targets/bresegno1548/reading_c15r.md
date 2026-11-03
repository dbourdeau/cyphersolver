# Bernardo Bresegno to Ferrante Gonzaga, Rome, 5 Oct 1548: reading of the cipher on c. 15r

Biblioteca Estense Universitaria, Autografoteca Campori, Brezeno (abate), cc. 15-16, 22. Cipher on c. 15r, lines L01-L24.
**Status: read in part.** A transcription job, not a break: the contemporary decipherment bound in as c. 22r covers the whole cipher.

The Spanish text is that of c. 22r (`clear_c22r.txt`, checked at full size), which the signs carry. The marked text
below gives every departure of the signs from it. `scripts/reading.py check` rebuilds the decryption from
`transcription_c15r.txt` and `key.tsv`, walks the marked text unit by unit and exits 1 on any unmarked departure.
English: `translation_c15r.md`.

## Clear opening (c. 15r, not cipher)

Ill.mo y Ex.mo señor. A [...] deste escriui a V. E. y le di auiso de quanto se offrecia: lo q agora se offrece es que

## Cipher (Spanish, as c. 22r)

el Cardenal Moron me ha dicho que antier confrontaron a Fierrauante con su cuñado en el castillo y que huuo entre ellos
gran contradicion, y despues a la noche sacaron a su cuñado del castillo y con vna barca le passaron a Torre de nona, y
alli, segun el Papa le ha dicho, le pusieron a la cuerda sin al calle ni otra cosa ninguna, y que confesso que era
uerdad que hauia muchos dias que el de suyo hauia pensado de hazer este tractado, y que hauia muchas uezes dicho a este
q siruiesse a V. Ex., que ternia mejor condicion que la que alli tenia, sin dezille cosa ninguna del Tractato, y que
despues hauia ydo a V. Ex. y comunicadole este su pensamiento, y que V. Ex. le hauia respondido que no podia darle
comission ninguna sin auisar primero a su Mag. y uer lo que mandaua, que el entretuuiesse y lleuasse adelante la
platica y que le auisaria lo que hauia de hazer luego que supiesse la uoluntad de su Mag.; que el entonces vino a
Boloña, no estando alli Moron, y hablo al Fierrauante claramente y hizo promissiones de parte de V. Ex.; y preguntado
como pensaua effectuar esta cosa, dixo que pensaua poner en el Palacio Trezientos hombres, losquales le sostuuiessen
hasta que el señor Duque de Florencia embiasse gente a soccorrerle. Esto es lo que hasta ahora ha confessado, y V. Ex.
sera seruido de tenello en si, porque recibiria daño Moron por hauerselo dicho en confession a el Papa.

"al calle" as written on c. 22r and given by the signs (al-ca-lle); the sense is "alzalle" (without hoisting him).

## Marked text (machine-checked)

Marks: `{a/e}` the text reads a where the signs give e; `{+s}` no sign gives s; `{-e}` a sign gives e that the text
does not have; `[V. Ex.]` etc. code group. A word with no mark is verbatim from the signs. ñ and ç are written n and z.

<!-- marked -->
{-b}{-u}el {-t}[Cardenal] {M/c}or{+o}n m{+e} ha di{c/e}ho que anti{e/q}r confrontaron a Fierrau{+a}nte con su cunado en el castillo y que huuo entre ell{o/u}s g{-u}ran contradicion y despues a la no{c/e}he sacaron a su cun{a/e}do del cast{+i}llo y con {v/u}na barca le passaron a Torre de n{+o}na y alli segun {e/?}{+l} [Papa] le h{+a} di{c/e}h{o/u} le pusieron a la {c/e}{+u}erda s{+i}n al calle ni {o/m}tra cosa ninguna y que confess{o/d} que era uerdad que hauia mu{c/e}h{o/u}s dias que el de suyo hauia pensado de hazer este t{r/o}{+a}{+c}tado y que hauia mu{c/e}has uezes di{c/e}h{o/u} a este q {-u}{-e}siruie{+s}se a [V. Ex.] que ternia mejor condicion que la que alli tenia sin dezille cosa ninguna del Tr{+a}{+c}ta{t/d}o y que despues hauia ydo a [V. Ex.] y comu{n/f}{+i}cadole este su pensa{m/c}iento y que [V. Ex.] le hauia {-r}respondido que no podia darle comiss{i/r}on ninguna sin auisar primero a su [Mag.] y uer lo que mandaua que el {e/?}ntretu{+u}ie{+s}se y lleua{+s}se adelante la platica y que le auisaria lo que hau{+i}a de hazer luego que s{+u}pie{+s}se la uoluntad de su [Mag.] que el entonces {v/u}ino a [Bolona] no estando alli Moron y hablo al Fierrauante {c/e}lar{+a}mente y {+h}{+i}z{-i}{-h}o promissiones de parte de [V. Ex.] y preguntado como pensaua e{f/s}{+f}e{+c}tuar esta cosa di{x/d}o que pensaua poner en el Palacio Trezientos hombres losquales le sostuuies{+s}en hasta que el senor [Duque de Florencia] embias{+s}e gente a so{+c}correrle Esto es lo que hasta ahora ha confessado y [V. Ex.] sera seruido de tenello en si porque r{-r}ecibiria dano Moron por hauerselo di{c/e}ho en confession a el {-e}{-l}[Papa]{-a}
<!-- /marked -->

## Word count against the 95% rule

250 words (a code group counts as one word). **204 of 250 (81.6%) come verbatim from the signs; 46 carry at least one
mark.** All 250 read as sense only because c. 22r gives them. The status is therefore **read in part**: a transcription
job whose full text is the contemporary decipherment, not a reading of the signs at the 95% bar.

The count was 196 (78.4%) before the independent check. Two sign fixes the check settled (L02 `d^5`, L19 `#^2 7^2`)
give 198 (79.2%). Six more words (confrontaron, a, contradicion, passaron, a, Fierrauante) come from four digit
placements settled on crops after the check (L02 twice, L03, L05, L17; see the foot of `transcription_c15r.txt`). Those
placements were looked for where this text had marks, so they are not independent of c. 22r.
