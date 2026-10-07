# Aerssen cipher - transcription conventions (shared by all workers)

System (established so far): syllabic nomenclator. Tokens = numbers 1-109 (plain or barred),
Latin letters (plain or barred), a few Greek-like signs; dots are separators (ignore for values).
Values are mostly CV syllables (de, la, ne, mo...), single letters (n, s, t, r, l, z, e, a, i, u, b, p, c, x)
and code words (10+ = (le) Roy, 109 = Monsieur, 25+ = Mr de Villeroy, 42 = la Royne d'Angleterre,
94 = lettres, 95 = (l')ambassadeur [Buzanval], 85 = Breda, eps^ = quat(re)).
u/v and i/j are interchangeable in values (40 = ue/ve). Decipherers sometimes write b for v (bi = vi).

## Token notation (ASCII, space separated; omit the dots)
- number as written: `28`; any bar on it (over, under or through) -> `28^`; cross above -> `10+`
  (keep `+`; it marks names). Both bar and cross: `25^+`.
- Latin letters: `d f k p y z b c e h q v w x m g t s` etc. Barred / struck: `k^`, `y^`, `w^`, `m^`, `v^`, `T^`, `e^`, `h^` (=ħ).
  Script tall-loop l (ℓ, looks like a tall e): `l`.  Capital-looking letters keep case: `T^`, `J` (Ʒ-like sign = bo).
- Greek-like signs: `eps` (ε), `eps^`, `eta` (η), `eta^`, `lam` (λ), `alpha` (α), `alpha^`, `pi` (π), `beta` (β),
  `psi` (ψ), `inf` (∞, horizontal 8), `apar` (Ⱥ, a-like with cross stroke = pa/par).
- In this hand the digit 8 looks like ∂ / δ (round body, ascender curving left): standalone it is `8`.
  4 looks like q with straight descender (sometimes a cross); 9 like g with curved descender. Distinguish 14 vs 19 carefully.
  2 looks like z; the LETTER z (= le) is a separate sign with a hook - mark `z` vs `2` carefully.
- Unreadable / uncertain: append `?` (e.g. `14?`); illegible token: `??`.

## Output block format (one per cipher passage)
```
## P <file-unique id> | src=<inv>_<scan> | y=<approx fraction> | gloss=interlinear|sheet:<letter>|slip|none
TOK: <tokens>
GLOSS: <contemporary decipherment as written (French), or '-' if none>
ALIGN: <token>=<value> ... (same order as TOK; value '?' if not determinable from the gloss)
CONTEXT: <a few words of clear text before/after>
NOTE: <doubts>
```
Only align values that the gloss supports; never invent. If gloss and cipher disagree, say so in NOTE.

## Key values seen so far (1598, slip on 2016 scan 31 = contemporary sign-by-sign worksheet)
28^=de 29^=de 38^=fo 12=n 21=z 3=a 7=e 24=e inf=e 38=te 20=r 18=t p=ro 17=u 27=u 40=ue/ve eps^=quat c=re
52=vi(bi) 10^=g eta^=mi 6=l 19=s 14=o 2^=cu 1^=pa(?)/ga(?) m^=pi 64=su 94=lettres 44=za f=me(and/or re: two f-like signs?)
7^=co J=bo apar=pa 14^=ce eps=le 109=Monsieur 26^=di 26=i z=le e=re 5=i lam=mo 9^=po 10+=Roy 15=p alpha^=lu
16=x 36=se k=ri k^=pe h^=no 8=la 1=c 57=he(che?) y^=me T^=ne h=qui 4=b 4^=bu 32=va(1598 Buzanval)/do(1601 doibt?)
42=la Royne d'Angleterre 85=Breda 95=ambassadeur 25+=Mr de Villeroy 50=ti 51=ti 30=fa 28=sa 9=em/en 55=ge 58=vo
e^=nu 23=a 48=ri? 33=do?

## UPDATE (after first 1601 work) - IMPORTANT
- Bar POSITION matters: write `^` for a bar ABOVE, `_` for a bar BELOW / through the descender (e.g. `9_` = po
  in 1598/1601, `9^` = mi in 1601). If unsure of position write `^?`.
- A grave-accent tick or small stroke above a number (`47\``) often marks a code word (name); write it as `47'`.
- Key differs between 1598 and 1601: 1598 32=va; 1601 32=do, 33=va, 33^=do, 36=du/se, b=que, b^=ni, psi=ie,
  q^=no, h^=no, h=qui, t^=pa, 13=q, 15=p, 5=i, a^=lu, beta^=lu, y=la, y^=me, w^=na (pi-like w), eps^=ma, g=que,
  21+=Mr de Bouillon, 25+=Mr de Villeroy, 95=l'ambassadeur, 10+=(le) Roy, 109=Monsieur.
- Do NOT use the 30 Apr / 5 May 1601 lists (2019 scans 46-47) unless told.

## Final 1601 labels and repository grades (4 October 2026)
Historical updates above record the research sequence; the old instruction to withhold list A no longer applies.
Use qF for the foot-barred po-sign in 25 May and 30 April A10/A16; qT for the through-stroked qui-sign in 11 May.
Keep q^ (po) distinct: no general merger of q glyphs. The corrected 25 May Queen code is plain 42, not 42'.
The supplied visual corrections are accepted from recount_listA.md; no fresh image inspection is claimed here.
Repository H = primary key, C = known-plaintext letter, M = uncertain, I = inferred.
There is no primary key sheet here: attested values are C; theta and minority alternatives remain M.
The supplied key used H/C/M for >=3/2/1 attestations. Preserve that obsolete frequency scale only in
key.tsv's legacy_support column, so the historical validation's H denominator remains reproducible.
List A is a contemporary decipherment, not a cipher-key sheet. Its reuse contaminates the holdout.
