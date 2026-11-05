# The Dieppe shipping clause

Henri IV to Pierre Jeannin, Buzanval and Russy, Paris, 8 July 1607. BnF, Français 3516, f. 116v, cipher lines 4 (last group) to 6.

**French, spaced reading.** « Si tost que nous scaurons que leurs [nauire]s seront partiz pour les venir charger. »

**English.** “As soon as we learn that their ships have set out to come and load the funds.”

The square brackets isolate the proposed expansion of barred `90`. The final `s` is a separate cipher sign. The script represents the key’s shared u/v value as `u`, hence raw `uenir` becomes *venir* here. Capitalization, word spacing, and the full stop are editorial. “The funds” renders the object pronoun *les*, which refers back to the 375,000 livres specified immediately before this clause. The printed edition confirms the Dieppe shipment and the amount. [1875 edition, p. 88, left column](https://archive.org/details/negociationsdiplomatiquesetpoli/page/n113/mode/1up)

## Ciphertext and output

Each output item corresponds to one sign directly above it. Angle brackets identify the one proposed expansion. The last word on line 5 runs into line 6.

```text
4 cipher    u4
  value     si

5 cipher    dd Xlow U3 longS x^  84^  U3 fCurl eps U2 ba 96^ eq x^  56^  eq 90^      U3 fStraight ro
  value     t  o    s  t     que nous s  c     a   u  r  on  s  que leur s  <nauire> s  se        r

6 cipher    94^ c^  longS cross no hook^ 54^ eq U2 dots3 zLoop cross ba fCurl tallLoop eps ba hook uf ro
  value     ont par t     i     z  pour  le  s  u  e     n     i     r  c     h        a   r  g    e  r
```

| Reading | Evidence | Assessment |
| --- | --- | --- |
| *leurs* | Barred `56` plus `=` on line 5. The same pair reads *leurs* before *partisans* on f. 86r. | Supported by the cipher. The 1656 and 1875 editions have *les* here. |
| *nauire* | Barred `90` aligns with the interlinear word for ships, followed in cipher by the same `s` sign used in *sont* elsewhere. The edition independently identifies the noun as *navires*. | Strong local inference. Singular expansion and spelling are editorial conventions. A second occurrence of the code would test its value outside this clause. |
| *seront* | `fStraight ro` at the end of line 5 plus barred `94` at the head of line 6 gives `se + r + ont`. | Supported by the cipher. The same straight f begins *secourir* on line 3. |

[Gallica manuscript scan](https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f201/full/3400,/0/default.jpg) · [Lasry’s System A chart](https://dbourdeau.github.io/cyphersolver/lasry/jeannin1607/key_1.jpg)

## Villeroy’s instruction on discretion

Villeroy to Jeannin, 15 June 1607. BnF, Français 3516, f. 87r, the end of cipher line 5 and start of line 6.

**French.** « Qu’ilz n’ayent occasion de s’en cacher. »

**English.** “[So] that they have no reason to conceal it.”

“It” is their possible decision to take the truce. The following line continues with *du tout de vous et de nous*. Villeroy wants the envoys to be discreet enough that the States have no reason to hide their decision from the envoys or the French court. The affirmative reading in the checked editions reverses that part of the instruction. [Manuscript scan](https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f150/full/1700,/0/default.jpg) · [1656, p. 72](https://books.google.com/books?id=yahDAAAAcAAJ&pg=PA72) · [1819, vol. 1, p. 222](https://books.google.com/books?id=10cUAAAAYAAJ&pg=PA222) · [1875, p. 64](https://archive.org/download/negociationsdiplomatiquesetpoli/page/n89/mode/1up)

```text
5 cipher   3^     zLoop eps oDash ff  97^      rComma U3 rr fCurl eps
  value    quilz  n     a   y     ent occasion de     s  en c     a

6 cipher   fCurl tallLoop dots3 ro
  value    c     h        e     r
```

The French inserts apostrophes and spaces. The `n` of *n’ayent* is a separate, plainly visible cipher sign, and the interlinear reads *nayent*. Neither of the two added code values in the clause supplies the negative.

| Added value | Manuscript comparisons |
| --- | --- |
| Barred `3` → *qu’ilz* | f. 87r *qu’ilz n’ayent*, f. 112v *qu’ilz ont*, f. 116v *qu’ilz sont*. |
| Barred `50` → *j’ay* | f. 113v *car j’ay sceu*, f. 114v *que j’ay*, and f. 116v *j’ay trouvé*. |
| Barred `97` → *occasion* | f. 87r *n’ayent occasion*, f. 115v *quelque occasion*, and f. 116r *donneront occasion*. |

[Lasry’s System A chart](https://dbourdeau.github.io/cyphersolver/lasry/jeannin1607/key_1.jpg) · [Manuscript locations](SOURCES.md)

## Dotted groups for diplomatic parties

The same hand writes two small dots over each of these numbers. They are separate from the barred groups above. The readings below are the contemporary glosses, with light spelling normalization. The script uses `<ESPAGNE>` as a semantic label for dotted `11` so it can replay both contexts without guessing the expansion.

| Group | Cipher samples and readings | English |
| --- | --- | --- |
| Dotted `15` | f. 112v `95^ 74.. 54^ 15..`, *ou avec le Roy d’Angleterre*. F. 113v `u4 54^ 15..`, *si le Roy d’Angleterre*. | “or with the King of England” and “if the King of England” |
| Dotted `20` | f. 112v `x^ 20.. 94^`, *que les archiducz ont*. F. 115v `54^ eq 20..`, *les archiducz*. The first gloss supplies the article within the group, while the second cipher spells out the article. | “that the archdukes have” and “the archdukes” |
| Dotted `11`, the king | f. 88r `11.. hook^`, *le Roy d’Espagne pour*. F. 116r `23^ 74.. 11..`, *guerre avec le Roy d’Espagne*. | “the King of Spain, to” and “war with the King of Spain” |
| Dotted `11`, the Spaniards | f. 112v `54^ eq 11.. 95^`, *les Espagnolz, ou*. F. 115v `74.. 54^ eq 11.. 95^`, *avec les Espagnolz, ou*. | “the Spaniards, or” and “with the Spaniards, or” |

[Manuscript locations](SOURCES.md)

## Control on a separate royal dispatch

In Henri IV’s 16 June 1607 letter, f. 91r, the first cipher line includes *de leurs nauires*, “of their ships,” in a sentence about the recall of the Dutch fleet. The known key accounts for the full nine-sign segment. The s after barred `56` is a different homophone of the one used on f. 116v. Here *nauires* is spelled using six signs, including one for the syllable *re*. [Manuscript detail](https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f157/2495,665,690,245/690,/0/default.jpg) · [1875 edition, p. 62](https://archive.org/details/negociationsdiplomatiquesetpoli/page/n87/mode/1up)

```text
cipher   rComma 56^  U3 zLoop eps U2 cross hCurl eq
value    de     leur s  n     a   u  i     re    s
```

## F. 113r, the long truce

**French** — *[…] années, en laquelle je vous repeteray que je suys content […].*

**English** — “[…] years, in which I will tell you again that I am willing […].” The preceding text refers to a long truce. The printed continuation says Henri IV is willing to intervene on the terms his envoys reported if a definitive peace cannot be reached. [Manuscript, view 194](https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059630p/f194/full/1700,/0/default.jpg) · [1875, p. 86](https://archive.org/details/negociationsdiplomatiquesetpoli/page/n111/mode/1up)

```text
penultimate tail
cipher   oval zLoop loopCross dots3 loopCross eq rr 53^ x^
value    a    n     n         e     e         s  en la  que

last line
cipher   dots4 loopCross dots3 51^ nn   hCurl qStem dots3 longS uf ro eps oDash x^  51^ U3 U2 oDash eq pComma longS rr longS
value    l     l         e     je  vous re    p     e     t     e  r  a   y     que je  s  u  y     s  con    t     en t
```

The cipher splits *laquelle* between `que` at the end of the first line and `lle` at the beginning of the second. The three repetition signs duplicate `n`, `e` and `l` within their respective lines. The 32 signs resolve with the public chart. The printed text matches the sampled words with regularized spelling. A faint contemporary interlinear reading is also visible on the scan.
