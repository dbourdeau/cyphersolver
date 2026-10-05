# R9634 — Lope Hurtado de Mendoza (Genoa) to Charles V, 13 September 1522

RAH Salazar 9/26 (A-26), ff. 14–16. DECODE R9634 (3 openings, `img/IMG_R9634_I45360_P1-3.jpg`), first worked
2026-10-02. Status: **read in part, 71% of cipher tokens read as sense (measured)**.

- **f. 14r** (P1 right): *S. C. C. Mt*, clear opening (the sack of Genoa, Lope's illness), then cipher from l. 14.
- **f. 14v, f. 15r** (P2): cipher with clear words between the runs, 24 + 25 lines.
- **f. 15v** (P3 left): 13 cipher lines, then clear (*pareceme que era razon de escrevir a V. Mt. esto que aqui he
  oydo, especial siendo de tan buen servidor de V. Mt. como es Geronimo Adorno ...*).
- **f. 16r** (P3 right): clear only — Cesarino's illness, don Juan Manuel in Rome; dated *de Genoba xiij de
  setiembre 1522*, autograph signature. DECODE has the month (9) but not the day or the place.
- **No clear version** of the cipher in the record, and none in print: Bergenroth CSP Spain ii calendars no
  Hurtado letter of Sept 1522 (searched 2026-09-21, NOTES "Escalation"). The reading below rests on the key alone.

Files: transcription `r9634_cipher.txt` (one line per manuscript line, 1191 cipher tokens), line-by-line reading
with unread counts `r9634_reading.tsv`, values specific to this hand `key_1522_r9634.tsv`, decoder
`python decode.py --letter r9634` (confirmed / probable coverage, unvalued tokens).

## What the letter says

Written from Genoa four months after the imperial sack of the city (30 May 1522), it reports a plan that
"honourable and sensible men" and Geronimo Adorno (the new imperial doge) put to Lope Hurtado: the Emperor and the
King of England, *queriendo destruir al Rey de Francia*, should make war on him through **Provence**,

> que es la tierra mas flaca que el tiene, y donde el exercito de V. Mt. puede entrar seguro, una tierra fertil
> ... [para proveer con las galeras de Genova] ... donde pueden entrar bien ... los de la mar y los de la tierra

The French are *muertos de miedo* after the sack. Taking Provence and Lyon (*y Leon y parte del ...*) would
cost the King of France the rest; *tomarle lo otro que le queda y cercarle en Paris* — something not to be done
*por Flandes ni por España*. Lope asked Adorno what force would be needed: **six hundred men-at-arms, [...] light
horse and [x thousand] soldiers, and for their pay 70,000 ducats a month** (*lxx U yob z*), if the Emperor and
the King of England agreed on it; the [lansquenets and Italians] in the duchy of Milan, *el exercito de [...]
soldados y mil hombres darmas*, would serve. Adorno added that the Pope would be glad to see the troops go on
*por no los tener alojados en sus tierras*, that the light horse should be paid and given their arrears, *con que
pagar su sueldo y sobrados dineros*; that it must be kept secret *por que no toviesen aviso*, and settled now for
**the month of March**; *es cosa segura, de poca costa e provechosa*; the King of France would only garrison the
fortresses, and with the great armies that the Emperor and the King of England keep at excessive cost the
whole could be paid for. The clear close commends Adorno as *tan buen servidor de V. Mt.*

This is an early form of the Provence invasion that Charles V and Henry VIII did launch in 1524 (Bourbon and
Pescara before Marseille), here proposed from Genoa in September 1522.

## Coverage (measured)

Token counts: `decode.py --letter r9634` counts 1191 tokens (it keeps the five `·` marks and a few
punctuation tokens); `python docs/_check_profile.py --measure r9634_tokens.txt` counts 1174 symbols. The shares
below use the 1191 count.

`r9634_reading.tsv` gives, for each manuscript line, the number of cipher tokens that are not part of a word read
with sense; totals computed against `r9634_cipher.txt`:

| page | tokens | read as sense | share |
|---|---|---|---|
| f. 14r | 227 | 167 | 74% |
| f. 14v | 325 | 204 | 63% |
| f. 15r | 435 | 336 | 77% |
| f. 15v | 204 | 135 | 66% |
| **total** | **1191** | **842** | **71%** |

Valued by the key (`decode.py --letter r9634`): 949/1191 confirmed (80%), 1119/1191 with probable values (94%). The
gap between 94% valued and 71% read is the spelled words whose letters all have values but which do not yet give
a word (`∂7ɣ8ϑɣα4`, `y&Ɛʇʇα47`, `xɩ4ε∠7x&` ...), plus about 45 code groups that occur once. A language check on
the read text (`lm.best_language`) returns es-modern first (-1.69/char, next ca-modern -2.04).

## Key findings

- **The 1524 alphabet holds for this 1522 hand** with the R9649/R9646 sign names: a (7, ß, Ho), e (8, H, oo), r
  (ʇʇ, ɣ̊), t (ϑ, b), u/v (∠), i (α), n (4), o (&), d (x, 9), s (c, ∂), c (ɣ, f), m (ϯ, ʇ), p (ɭb, ⊃), f (#).
- **New sign**: `ɋ` (looped rho-like) = **r** — *tierra* three times, *una tierra fertil* exact.
- **`z` after a code is the plural s**: `xul z` los, `xug z` las, `xud z` hombres, `yob z` ducados, `xob z yal z`
  *grandes exercitos* (15v11). This is not the 1524 standing-alone `z` = n.
- **Codes**: `yob` = **ducado** (`lxx U yob z` = 70,000 ducats, after *serian menester ... cada mes*); `xep` = mar
  (*los de la xep y los de la tierra*); `xu` = **gente** (*aver la xu; dixome que la xu darmas*, 15r13 — conflicts with
  the 1524 `xu` = ha- and the 1522 probable `xu` = hara); `zar∂` = des- (*destruir*); `ʃil` toma, `ʃal` esta,
  `ʃop` bi, `xud` hombre each re-confirmed in three or more contexts.
- **Null groups after the run opener `Ꮒ`**: `ʃta`, `ɡʇo` (with `ɣ̊ʇ`/`ʑto`), `ʆ∂`, `yt`, `yω`. The clerk's clear of
  R9649 (f. 268) has nothing for `Ꮒ yω ʃta`; in R9634 the sentence closes over `Ꮒ ʃta` (14r13), `Ꮒ ɣ̊ʇ ɡʇo` (14v07,
  *con lo que a el le quitasen*), `Ꮒ ʆ∂` (14v14, 15v07), `Ꮒ ∂ yt` (14v17); in R9646 `Ꮒ ʃta avia miedo` and `bien Ꮒ ʑto
  ɡto ofrecer`. `ʃta` is confirmed (four letters), the others probable.
- **The e/t confusion recurs**: in *muertos*, *acordasen*, *faltasen*, *gastara* the sign read 8 (e) stands in a t
  slot; the closed `8` and open-topped `ϑ` are not separated at DECODE's resolution (`read_r9649.md`). These words
  are marked ~ (probable) in the reading.

## Unread and why

- About 45 code groups seen once (`ʃe`, `xer`, `zud`, `zac`, `ʃum`, `ʇudd`, `yat`, `ʌʃ`, `zub`, `ʃof`, `zif yin`,
  `xen`, `zε`, `zer`, `ʃi`, `ʃq`, `xin`, `car ʒa`, `xas zɣ`, `yul` ...) and `yel` (4×), `ɣ̊e` (4×), `ʃun` (2×), `ʃud` (2×):
  no crib and no second context that forces a value. Left open.
- Spelled words whose letters have values but give no word: `ʇʇ&48ʇʇ8∂` and `∂7ɣ8ϑɣα4` (14r12), `y&Ɛʇʇα47`,
  `xɩ4ε∠7x&` (14v03, probably place names: *lo mas de ...*), `8&ɣʇʇα8ʇʇ7` (14v16), `zα∂ɷ8∂Hɣϑ&∂` (15r11),
  `x838ɋHoɣ̊` (15v05), `z&∂ϑ8ɣHɣ̊` (15v12). Each has one or two signs at the limit of the scan (8/ϑ, ∂ as s/p/t, ε as
  l/g). Blocker: illegible at DECODE's 1700 px per folio.
- Numerals in 15r05/15r09/15r10 (`·9·`, `x b U`, `ɷɩ U`): the force sizes other than 600 men-at-arms and 70,000
  ducats are not fixed.

## Retry, 2026-10-02 (after R9645 and R9656)

Every unread group was retried against the values won on R9645's glosses and the R9656 regrade. Two words gained:
`xug xu` = *la gente* (14v23; `xu` = gente is confirmed on R9645's gloss *la gente de v. mgd*) and `yɩ ɣ̊` = `yiL` + r =
*hazer* (15r20, probable; R9645 r16 *no puede yiL*). **846 / 1191 = 71%.** The rest (about 45 codes and the spelled words
listed above) occur once and recur in no sibling with a crib.

## 2026-10-03

**872 / 1191 = 73.2%** (from 71.0%). Gained: *sostener* (15v12), *tenia* (15r14), *ser* (15r25), *vio* (14r10), and 14v22 *si el gran ~capitan ~fue(ra) ~vivo* (zif, yin pooled; ɸα∠& by `wordmatch.py`). No better image (DECODE has none; RAH behind a bot check), no crib in Sanuto XXXIII or CSP ii; see NOTES "Push toward a full reading".
