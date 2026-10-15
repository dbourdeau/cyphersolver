# BnF Espagnol 318 no. 92: the Great Captain to Lorenzo Suárez, 17 Aug 1500, in the Cifra general (catalogue no. 9)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This folder used to be the whole volume:
five ciphered letters in at least four ciphers. It now keeps **no. 92** (ff. 116r–v), in the *Cifra general de los
Reyes Católicos*. The other letters are different ciphers, each with its own entry and page:

- [`targets/federico1497/`](../federico1497/NOTES.md), no. 5 (ff. 5–6v, 11 Jan 1497): Escrivà's cipher no. 1,
  deciphered in print by Ivan Parisi (2020);
- [`targets/esp318no95/`](../esp318no95/NOTES.md), no. 95 (f. 122r–v, 8 Jan 1497): George Lasry's 2022 alphabet,
  applied here in stretches;
- [`targets/esp318no93/`](../esp318no93/NOTES.md), nos. 93 and 94 (ff. 118–121v, 1503–04): not solved; key not
  identified, and whether the two share a key is not established.

The volume's shared material stays here: the IIIF manifest, notice and folio map, the full-size scans of all
thirteen cipher folios (`full/`), the literature (`lit/`), the key transcription (`keys/`) and the segmentation
pipeline built for no. 95 (`seg.py`, `glyphs.py`, `cluster.py`, `montage.py`, `localseg*.py`, `*95*.py`, `lm.py`,
the `f122r_*` outputs and the git-ignored intermediates). The no. 95 and no. 93 entries refer to them by path.

**Outcome: read with known key, read in part.** Session of 17 Sept 2026 (identification), 21 Sept 2026 (both pages
transcribed and read in part).

## The volume

Ark `btv1b52503046q`, 486 canvases, 127 folios, ex-Ruffo Scilla collection, bought by the BnF in 1857; Morel-Fatio
no. 172. Folio → canvas from the IIIF manifest (`lab2canvas.json`); the volume's own foliation, not the canvas count.

| no. | ff. | canvases | letter | cipher | entry |
|---|---|---|---|---|---|
| 5 | 5–6v | 32–35 | Federico III of Naples to the Catholic Monarchs, San Germano, 11 Jan 1497 | Escrivà's cipher no. 1 | federico1497 |
| 92 | 116–116v | 440–441 | Gonzalo Fernández de Córdoba to Lorenzo Suárez, 17 Aug 1500 | Cifra general de los RRCC | **this entry** |
| 93 | 118–118v | 446–447 | Lorenzo Suárez (de Figueroa) to the Catholic Monarchs, Venice, 24 Feb 1504 | not identified | esp318no93 |
| 94 | 120–121v | 452–455 | The viceroy of Sicily to Ferdinand, Messina, 27 Apr 1503 | not identified | esp318no93 |
| 95 | 122–122v | 458–459 | Unaddressed cipher, 8 Jan 1497 | Lasry's 2022 alphabet | esp318no95 |

## No. 92 — the cipher identified and proved

The leaf is headed, in the sender's hand, "la respuesta q[ue] enbio a los s[eño]res en xbij de ag[osto] 1500", and
opens in clear: *"Muy mag[nifico] Señor: a los xiiij d[e]l presente recebi v[uest]ra letra con hun breve d[e]l papa y
otras dos cartas del embax[ad]or veneçiano con uno suyo, dando priesa en my yda a la resistençia del turco…"* — then
alternates clear and cipher for two pages.

Tomokiyo notes that the Great Captain "used this cipher" (Ferdinand/Isabella's cipher of c. 1500–1502) in this letter,
but marks the letter undeciphered. The identification can be proved rather than assumed, because a later hand wrote a
**partial decipherment between the lines** of f. 116r. Reading those interlinear words against the printed key gives
eight independent hits and no misses:

| gloss on the leaf | cipher | *Cifra general* |
|---|---|---|
| lo | `yuy` | Lo |
| y tpo | `h` `boy` | (E =) y · Tiempo |
| por | `zez` | Por |
| estar | `xiz` + `7` | Esta + r |
| en | `xuy` | En |
| tanto | `baz` | Tanto |
| el negoçio | `xix` `zol` | El · Negocio |
| de | `xup` | De |
| puede | `zuy` | Puede |
| no | `zik` | No |
| — | `bob` | Que |

`7` = R and `h` = E come from the key's own symbol alphabet, and the glossator's "y" for `h` is the ordinary *e*/*y*
alternation of the conjunction, so it confirms rather than contradicts. A gloss-anchored line decodes straight
through:

```
ct   h  boy      zez    xiz  7  xuy  baz      ff k …
pt   y  tiempo   por    esta r  en   tanto    p  g …
```

that is, *"…y tiempo, por estar en tanto…"* — exactly the words the glossator wrote above it. f. 116v ends half in
clear — *"…no desconfio que mucho se pudiera aprovechar … se ha ofreçido … yo me desnudo y descargo y me satisfago en
que n[uest]r[o]…"* — with `zin` = Nápoles, `xar` = después, `biz` = toda, `xuy` = en among the codes, and below it the
inventory mark "Inventº 11 Ottº 53".

The key is transcribed here as `keys/cifra_general.txt` / `.json`: 683 code groups from Galende Díaz's plates
(pp. 167–173), plus the twenty-one personal symbols (Papa = A, Emperador = B, Rey de Françia = F, Rey de Spanya = G,
Rey de Napoles = □, Don Fadrique prinçipe de Altamira = S†, …). `decode.py` applies it to a transcription.

## No. 92 — both pages transcribed and read in part (21 Sept 2026)

Both pages were transcribed line by line (36 lines on f. 116r, 11 on f. 116v) with the sign alphabet Galende prints on
p. 167 (`lit/gal/p09.png`) and the code list; the transcription and a line-by-line reading are in `f116_reading.md`.
Three things the specimen line had not shown: the fifth form of A (`⊃#`) and the fifth form of E (q with k below) are
the commonest vowel signs; the crossed T is the key's *duplicate* LL (*vituallas*, *Pulla*, *llamó*); and the clear
hand's *con-* abbreviation (ꝯ) is used inside the cipher (*contenté con el*, *con color de*).

The letter is the Great Captain's answer to Suárez's request, on the Pope's and Venice's behalf, that he take the
fleet against the Turk (the Cephalonia campaign of autumn 1500). He will go, but at a price: *no deve pasar … si no
grande remuneración*; the business is *en tanto peligro … e a tanto lexos*; Venice holds *Brindizi y Otranto* in
*Pulla*, and he asks for *puertos de Italia donde esta armada se pueda recoger quando el tiempo lo requiriese, por no
aver de bolver tan lexos*, to land *nuestros dolientes y heridos y ropa e vituallas* and refit the ships *sin los
ynconvenientes de estar en casas agenas*. He had asked the same through Garcilaso when the Pope called him, and got it,
the castellans being *españoles y criados del Rey*. Suárez is to raise it *con color de nuestro descanso y reparo*.
Verso: *segund su necesidad no creo que nada desto les sea ynposible*; the ambassador of Venice at Naples has offered
it; *yo me desnudo y descargo*.

Second pass the same day: Tomokiyo's unpublished partial reading of the opening (commented out in cryptiana's
`spanish.htm`) settles `zap` = `zag` *me*, `bac` = `vac` *armada*, `xie` = *cargo*; Sanuto (*Diarii* III cols. ~708–709,
~982–983) reports the same demand from the Venetian side (*aver qualli porto li piace a li bisogni … vituarie*; a port
*seperato* from the Venetian fleet). RAH 9/15 is not online and no printed clear copy was found. Third pass (Sanuto's
cribs on recto ll. 8–11): the cribs are not in those lines, but `zie` = *parescer* (*pareceria tener*, l. 11; fits all
five places), and ll. 8–11 now read *si empresa a propósito de sus altezas … no hablo en ello … segun la necesidad
dellos ay … en semejante acatamiento pareceria tener mas respeto a …*.

Open: the codes `bog` (×3), `zeb`, `zems`, `xob`, `bue` do not fit Galende's printed values in context, so either his
plates carry misprints there or the hand uses a variant; about ten letter-sign stretches are unresolved (list in
`f116_reading.md`, Open points). About three quarters of the words read (estimate by line; no token count was kept).

## What is in this directory

* `full/` — IIIF `full/full` images of all thirteen cipher folios of the volume (4100–4200 px wide). Gallica returns
  HTTP 429 after about six full-size requests in a row — pause 20 s between them.
* `manifest.json`, `lab2canvas.json`, `notice.html` — the ark's manifest, the folio→canvas map, and the BnF notice.
* `keys/cifra_general.txt|.json` — the *Cifra general de los Reyes Católicos*, 683 codes + 21 personal symbols.
* `ct92_glosses.txt`, `ct92_specimen.txt`, `f116_reading.md` — no. 92's glosses, specimen line and full reading.
* `decode.py` — applies the key to a whitespace-separated transcription; `crop.py`, `strip.py`, `lines.py` — the image
  tools. Line pitch comes from the autocorrelation of the ink profile (f. 116r 113 px, f. 118r 128 px, f. 120r 100 px,
  f. 122r 114 px).
* Shared with the other entries: the no. 95 pipeline (`seg.py`, `glyphs.py`, `cluster.py`, `montage.py`,
  `assign95.py`, `localseg*.py`, `viterbi95.py`, `hybrid95.py`, `linedp95.py`, `band95.py`, `reseg.py`, `solve95*.py`,
  `lm.py`, the `f122r_*` outputs; see `targets/esp318no95/`), and `lit/` (Parisi 2020, Galende Díaz 1994, Tomokiyo's
  pages, the Bergenroth Gran Capitán key photographs).

## References

* J.C. Galende Díaz, *La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V*, Cuadernos de Estudios
  Medievales y CC.TT.HH. XVIII–XIX (1993–94), 159–178 — https://digibug.ugr.es/handle/10481/30410
* S. Tomokiyo, *Spanish Ciphers during the Reign of Ferdinand and Isabella*, cryptiana.
* M. Sanuto, *I Diarii*, vol. III.

## Remaining gaps

- five code groups (bog ×3, zeb, zems, xob, bue) - blocker: needs-physical-access; they contradict Galende's printed values in context; his plates misprint others, and the manuscript BRAH 9/15 ff. 7-9, not digitised, would settle them
- about ten stretches of letter signs (grade I) - blocker: illegible; the q-shaped N and the reversed-9 S cannot be told apart at Gallica's 4155-px resolution

## Escalation

- [x] siblings: all thirteen cipher folios of the volume opened; no other letter in the Cifra general; no decipherment of no. 92 elsewhere in the volume
- [x] clear-pages: the interlinear glosses of f. 116r used as cribs and as the proof of the key; the clear passages give the context of every cipher stretch
- [x] known-keys: the Cifra general is the key (eight glosses, no misses); Escrivà no. 1 and the Gran cifra do not fit its code initials
- [x] print: Galende Díaz 1994, Tomokiyo (including his commented-out partial reading), Sanuto's Diarii III, CODOIN, Zurita, BRAH Noticias, archive.org: no clear copy
- [x] key-rebuild: zap=zag, bac=vac, xie=cargo, zie=parescer, vog=acatamiento, zer=zec fixed from context and Tomokiyo; the five codes left contradict the plates in every place
- [x] retry: second and third passes (21 Sept 2026) re-read every doubtful stretch with the corrected values; recto ll. 8-11 now read in sense

## Assumptions for George's review

- The volume's entry is split per key: no. 92 (Cifra general) here; no. 5 (Escrivà no. 1), no. 95 (your 2022
  alphabet) and nos. 93-94 (key not identified) in their own entries. Your credit is on no. 95 only.
- Nos. 93 and 94 are kept together in one attempted entry only because both are unread and their keys are unknown;
  no shared key is claimed for them.
