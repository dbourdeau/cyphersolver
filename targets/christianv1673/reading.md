# christianv1673 - reading of the closing cipher block (Danish, spelling of the order)

Order of Christian V to Jens Juel and Christoffer Lindenov, Copenhagen, 25 May 1673, closing block (image 10 foot and image 11,
lines T01-T15 of `transcription.txt`). Read by sense from `decryption.txt` with `key.tsv`, after the key was validated
(`validation.txt`). The block itself was never used for any measurement.

Marks: CAPITALS = words written in clear in the order (not counted); plain lower case = certain (every group read with the key,
the word is regular Danish of the time); {x} = probable (one value inferred or one sign doubtful, see the list); [x] = restored
(a group with no value, word supplied from the sense; the groups are given in brackets); <...> = unresolved. Word division and
punctuation are ours. Spelling of the time kept (w for v, ff, haffuer, woris).

## Text

SKULDE DA UDI DEN MATERIE <e·384·r·o·i·jo·ce·ri·s> LIGESOM wi [befalt] (320·a·l·t) haffuer <384> <co·n·r·e·348·r·t>
UDEN {strygen}/strygen woris [Slotte] (s·lo·t·906) at PASSERE med deris <646> krigskibe, SAA haffuer J at swaare
AT DET ICKUN ER en {Indulgencien}, tid som med <la·g·ge·n·s> {udstirkelse} {saaledes} til SIDES som ellers ANDRE
ved SAMMEN{tegn} permitteris, OG AT DET ENDDA ICKE SKEER paa {aldre} wilkaar END PAA DET foresatte {Fundament},
AT DE af andre {Kronede} Hoveder OG I SAER Kron Sverig SELF, {huis} [Exempel] (e·29·e·m·pe·l) de ATSKILLIGE GANGE
allegeret haffuer, <32·re> bewises, AT AF DEM ingen {strygen} begieren, OG ER langt fra AT WI NOGEN
tid den ret DE HAFDE wilde frasige som WI OG woris HØY{loflige} forfædre i saa MANGE aar {u}PAA{kieret} HAFFT HAFDE.

(In line T02 the first "strygen" is certain; the one in T12 is probable. "HØYloflige" and "uPAAkieret" mix clear syllables of
the original with cipher: høy- and paa- are written in clear, -loflige and u-/-kieret are cipher. "SAMMENtegn": sammen in clear,
-tegn in cipher.)

## Words

68 words come from cipher groups (words written in clear in the order are not counted).

| class | n | words |
|---|---|---|
| certain | 49 | wi (T01); haffuer, strygen (T02, q barred = i), woris (T02); at, med, deris, krigskibe, haffuer, J (T03, q barred); at, swaare, en (T04); tid, som, med, til (T05); som, ellers, ved, permitteris (T06); paa, wilkaar (T07); foresatte (T08); af, andre, Hoveder (T09); Kron, Sverig, de (T10); allegeret, haffuer, bewises (T11); ingen, begieren, langt, fra (T12); tid, den, ret, wilde, frasige, som, woris (T13); høyloflige, forfædre, i, saa, aar (T14) |
| probable | 10 | Indulgencien (486 = du inferred from the syllable block; ending -sien doubtful); udstirkelse; saaledes (847, one gloss in 1674); Sammentegn; aldre (or andre); Kronede (Kro·ni·de); strygen (T12, q doubtful); upaakieret; huis = hvis (590: gloss "huis" in 1674 and the h block 580-596, KEY-v2 has "sind"); Fundament (534 = fu inferred from the syllable block) |
| restored | 3 | befalt (320; doubt: the verb befale has its own group 425 in 1674); Slotte (906); Exempel (29 = x not attested in 1673) |
| unresolved | 6 | e·384·r·o·i·jo·ce·ri·s (T01); 384 (T02); co·n·r·e·348·r·t (T02); 646 (a word in k-, before "krigskibe"); la·g·ge·n·s (T05; "Flaggens" is tempting but needs an f); 32·re (T11) |

**Certain + probable = 59/68 = 86.8%**; with the restored words 62/68 = 91.2%. Under the 95% bar: read in part.

Note on the count. The fiche of our working folder (11 Nov 2026) gave 46 certain, 10 probable, 3 restored, 6 unresolved of 65
words = 86.2%. Re-counted word by word for this PR, three certain words were missing from its list (wi in T01, haffuer at the head
of T02, woris in T13); no word changed class. Both counts are under 95%; the class "read in part" does not change.

## Why the holes

The six unresolved words and the three restored ones come from seven code groups: 32, 320, 348, 384 (twice), 646 and 906.
None of them is glossed anywhere in the volume: not in the two glossed orders used for the key (images 32-41, searched before the
measurement) and not in the held-out order (images 42-43, searched after it). The syllable blocks of the code give the initial
of two of them only (384 = a word in a-, 646 = a word in k-). The loose decipherment leaf of image 9 stops before this block; its
verso was not filmed.

## Sense

The block deals with the salute at sea in the Sound (Øresund): whether Swedish warships must strike (stryge) when they pass
the Danish castles. The king tells his envoys that if, in
this matter, [the Swedes argue that] their ships should pass "our castles" with their warships without striking, they are to
answer that any such exemption is only an indulgence for a time, as others are allowed elsewhere by an agreed signal
(Sammentegn), and on no other footing than the one already laid down: that other crowned heads, and above all the Crown of
Sweden itself, whose example they have alleged several times, show that none of them claims the salute [of Denmark]; and that
Denmark is far from ever giving up a right that the king and his most praiseworthy ancestors have held unchallenged for so many
years. The next paragraph, in clear, turns to the coinage ("Hvad mynternes reglement mellem begge ...").
