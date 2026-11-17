# BnF fr. 15567 f. 24r (catalogue 2838): Matignon's Cipher-1, early 1584. Decoded, not read

Images: Source gallica.bnf.fr / BnF (ark:/12148/btv1b90639282, view 29, right half; folio label 30/24).
The leaf has a block of 12 cipher lines and then a clear paragraph in a cursive hand. The clear paragraph has not been
transcribed. The facing leaf (view 29, left) is an address leaf, "A Monsieur / Monsieur de Villeroy Con[seill]er et
premier sec[retai]re d'estat du Roy". It is not certain that the address belongs to f. 24.

Tomokiyo (cryptiana, henryiii.htm) reconstructs Matignon's Cipher-1 from this leaf and f. 54, without a reading.

## Interlinear glosses (period hand)

Short glosses are written in letters over line 1 and a few other signs. They agree with the key wherever they can be
compared:
- Over l. 1 (from left to right): "court", "ung", "bru…", "L", "beaucoup de gens". The decode gives
  *…court ici un abpuit dont beaucoup ideae?s…*.
- Over ll. 3-8, short letter groups. These were not transcribed letter by letter.

## Transcription and test

- `transcription.txt`. Ll. 2-10 are the held-out portion D (387 labels). They were transcribed in two blind passes
  (`test_D/f24_pass1.txt`, `test_D/f24_pass2.txt`), and the passes agreed on 85.2% of signs after convention
  normalisation. The portion was then arbitrated on the image without a key (`test_D/f24_portion_final.txt`). Ll. 1,
  11 and 12 are pass 2 only and were not arbitrated.
- Pre-registered single test (`test_D/PREREG-D.md`, frozen before transcription; `test_D/PREREG-D2.md`, frozen before
  decoding). The key is `key.tsv` of this target, unchanged (sha256 eb00fd85…3404). The rule and the controls are the
  same as for tests 1 and 2.
- **Result: 294/385 signs = 76.4% in sense runs; 200 shuffled keys median 2.6%, max 27.8%. The 0.85 bar is NOT met**
  (max + 0.30 = 0.578 is met). The portion is now used up (`test_D/RESULTAT.txt`).

## Marked reading (`reading_marked.txt`)

Marking: plain = sure; {probable}; [restored]; ‹unresolved, letters as decoded›.

```
L01: ‹?hohillbp› {court} ‹ici› {un} {bruit} {dont} beaucoup {de} {gens} ‹debi›
L02: ‹eas› ‹elont› ‹eocandalisez› ‹o› est que le roy veult faire ‹??ler› ‹lerea›
L03: ‹imen?do?lison› ‹ala?lr› que les ocasions ‹olz› m'en {ont} dict
L04: sont ‹ulest› {prevenu} de faire ‹uober?es› et d'avoir {voulu}
L05: ‹u› faire surprendre le {chasteau} du ‹hlieo› ‹eai› bien ‹voupu›
L06: ‹luertirceo› {il} {importe} ‹ilesepuice› du roy ‹ctoln?eaultp?›
L07: ‹a› employer ‹da?pses› {provinces} que ‹aen?aient› ‹bo›
L08: ‹nrmoenu› ‹serez› ‹???› prudence acoustumee ‹?o?et› ‹paslnt›
L09: c'est ‹ouil?alseue› beaucoup ‹aeu› meschans bruictz
L10: contre {l'honneur} du roy que l'on ‹slrapomtez› ‹a?debe?ieu›
L11: ‹r?etmoyopiieneu?eeste› ‹aducerti› {premier} ‹ulbeuust›
L12: ‹t?ieleu?e› fait ‹arrester› ‹aoci›
```

| | ll. 2-10 (portion D) | whole block |
|---|---|---|
| sure | 36 | 38 |
| {probable} | 8 | 15 |
| ‹unresolved› | 31 | 40 |
| words | 75 | 93 |
| strict share (sure only) | 0.480 | 0.409 |
| sure + probable | 0.587 | 0.570 |

**State: decoded, not read.** The phrases hold, but the sentences do not.

## English (phrases only)

"… a rumour [is going about], of which many people … is that the King wants to do … the occasions … they told me of
it … are … prevented from doing … and of having wished … to have the castle of … surprised … well … it matters … of
the King … to employ … [in his?] provinces … [your] accustomed prudence … it is … many wicked rumours against the
honour of the King, which one … had … arrested …"

## Open

- Ll. 1, 11 and 12 need an arbitrated second pass. The clear paragraph below the block and the address on the facing
  leaf need transcribing: they may give the writer and the date.
- The glosses over ll. 3-8 need transcribing letter by letter.
- No person has checked this work. Transcription, arbitration and reading were done by Claude Opus 5.5 for Brice
  Dudout, 17 Nov 2026.
