# AGS Estado leg. 1394 no. 247 — García de Toledo to Philip II, 16 July 1565 (Great Siege of Malta)

Solved 2026-09-18. The cipher is a **homophonic substitution on two-digit figures 12–43**, laid out in
plain alphabetical order, used inline inside otherwise-clear Spanish. 1,930 figure groups; the whole
letter reads. No nomenclator groups (no word or name codes) occur anywhere in it: names like *Çaragoça*,
*Augusta*, *Cabo Bono*, *Argel*, *Maltta*, *Mecina* and *Mosiur de Lenni* are spelt out letter by letter.

## The key

| letter | figures | letter | figures | letter | figures |
|---|---|---|---|---|---|
| a | 12 13 14 | i | 24 25 26 | r | 35 |
| b | 15 | l | 27 | s | 36 |
| c | 16 | m | 28 | t | 37 |
| d | 17 | n | 29 | u / v | 38 39 40 |
| e | 18 19 20 | o | 30 31 32 | x | 41 |
| f | 21 | p | 33 | y | 42 |
| g | 22 | q | 34 | z | 43 |
| h | 23 | | | | |

Machine-readable in `key.json`. Structure: the five vowels plus *u/v* get three figures each, every
consonant one; the sequence runs straight through the alphabet with no j, k or w, so the whole table is
recoverable from any two or three cribbed words. 12–43 is exactly 32 values with nothing to spare, which
is why no nulls or code groups exist. Usage over the letter: s 178, r 153, a 143+95+50 = 288, e 132+67+36
= 235, o 100+40+13 = 153, i 110, u/v 97 — ordinary Spanish letter frequencies, and the homophones are
used unevenly (13 twice as often as 14, 19 twice as often as 18), i.e. the clerk had favourites.

Scribal habits worth knowing before transcribing: **ñ is written nn** (*sennales*, *Espanna*,
*campanna*); *u* and *v* are one letter; doubled letters are sometimes written once (*en tiera*) and
sometimes doubled where modern Spanish has one (*spantaado*, *quinta[a]les*). This is the *duplicado* —
a clerk's copy — and it carries copying slips: *quesido* for *querido*, *puddo* for *puedo*, *entras*
for *entrar*, *hazes* for *hazer*, *sennalda* for *señalada*, *lonze* for *onze*.

## How it fell

1. **Access.** PARES serves plain JPEGs with no IIIF. With a cookie jar: GET
   `.../ParesBusquedas20/catalogo/show/3576569`, read `dbCode=` out of the page, then
   `.../ViewImage.do?accion=42&txt_descarga=1&dbCode=27138924&txt_id_imagen=<n>&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0`
   for n = 1..6. `txt_zoom` other than 10 returns a *smaller* 355×484 thumbnail, so ~915×1250 is the
   maximum available; that is legible for figures when cropped and upscaled ~2.5–5×.
2. **Cribs from the clear text.** The first break came from two runs standing next to clear words:
   `36 18 24 36 16 24 18 29 37 30 36` after "los" gave *seiscientos*, and the run after "puso" gave
   *en tiera*. Those two fix a, c, d, e, i, l, n, o, r, s, t at once.
3. **The alphabet closes itself.** Because the assignments came out in alphabetical order (12–14 = a,
   15 = b, 16 = c…), the gaps could be predicted rather than solved: 21 = f, 41 = x, 42 = y, 43 = z were
   filled by prediction and then confirmed on *effetos*, *baxeles*, *plazer*, *yban*.
4. **Transcribe, decode, iterate.** `transcription.txt` keeps the figures digit-for-digit with the clear
   text around them; `decode.py` prints the decode, `render.py` writes the reading. Nonsense in the
   output localises misread digits: the confusable pairs in this hand are **17/19**, **35/36**, **35/38**
   (a long-tailed 3 vs a dotted 8) and **13/14**. Every correction in this repo's history of the file was
   found that way, not by re-reading at random.
5. **Audit.** All 1,930 groups fall inside 12–43, all 32 codes occur, and no run has odd length. An
   out-of-range value or an odd run is the signature of a transcription error, not of a second cipher.

## Independent confirmation

*Mosiur de Lenni*, deciphered from figures, is **Andrea Provana di Leinì**, the Savoyard commander whose
galleys sailed in the relief squadron — exactly the man who would be reporting whether the galleys were
signalled off. Don Juan de Cardona's 600 soldiers, *Çanoguera* as pilot, the Conde de Modica serving at
his own cost, Gian Andrea Doria's claim on the treasury, and the fortification of Syracuse and Augusta
are all consistent with the Sicilian record for July 1565. None of these names is in the clear text.

## Historical value

The letter is the viceroy's own account, written from Messina one week after the *Piccolo Soccorso* got
into Birgu, of **a second relief run that failed**: the galleys came within four miles of the harbour
mouth, the *barqueta* sent ahead got in and arranged fire-signals, and La Valette signalled
*clarissimas* that they should **not** enter — twice, within the appointed hour — so they slipped back
out to sea undetected. García adds the Grand Master's tears, the forbidden sortie that killed 200 Turks,
the siege lines "seven, eight and ten palms high" around the Turkish batteries, only 1,500 Turks at the
water, sickness killing men in the Ottoman camp, and the Algiers squadron sighted off Cape Bon by a wine
ship bound for La Goleta. The financial paragraphs are blunt: 40,000 escudos a month for the ships, two
months' pay owed, half the 48,000 ducados already spent, "in this kingdom there is nothing but infinite
debts", and *El estar sin galeras me destruye*.

## Status of prior work

Tomokiyo's cryptiana pages call the 1565 Malta cipher letters undeciphered and do not list this one;
PARES carries no decipherment for it, and the address leaf (image 6, *En manos del señor Franco de
Erasso*, sealed) shows no office annotation of a decipherment. Web searches for the document and for
editions of the AGS Malta correspondence turned up no published text (checked 2026-09-18). The
non-duplicate original in the same legajo, which this letter says "yra con esta" alongside the governor
of Mdina's own letter, would be the natural place for a contemporary Spanish decipherment to align
against; that check is still open.

## PARES search route (worked out here)

The results table is server-rendered, so no browser is needed: with a cookie jar,
`GET /ParesBusquedas20/catalogo/find?nm=&texto=<words>&anio1=<y>&anio2=<y>` returns the hits
(`catalogo/show/<id>` links in the HTML), and `signatura=EST%2CLEG%2C1394%2C247` finds one record by
shelfmark. A *partial* signature such as `EST,LEG,1394` returns "No se han encontrado datos" — the field
matches whole shelfmarks only, which is why the legajo cannot be listed that way. `catalogo/description/<id>`
gives the record's text; neighbouring ids are unrelated documents, not neighbouring folios.
Searching *carta cifrada Toledo* limited to 1565 returns exactly one García de Toledo item: this one.

## Open questions

- `yaretas` (f. 2v, line 2) — figures are unambiguous (42 12 35 20 37 14 36). Read as *jaretas*, the
  netting rigged over a galley's deck; with 41/42 confusion it could be *xaretas*, the same word.
- `secanos` (f. 2r) — "çierto es secanos donde podria ser assaltada", read as shoals/dry ground that
  would let the sea-facing cavalier be stormed.
- "salio del burgo el mismo lunes a los diez y nueue" — hours, not the day of the month, on the reading
  adopted here.
- The original (non-duplicate) despatch and the Mdina governor's enclosure have not been located in
  PARES yet.

## Files

- `img/p1.jpg` … `p6.jpg` — the six PARES images (ff. 1r, 1v, 2r, 2v, address leaf, seal side).
- `transcription.txt` — figures digit-for-digit + clear text, line by line, page markers `== pN`.
- `key.json` — the cipher table.
- `decode.py` — prints the decode with figure runs in angle brackets.
- `render.py` → `reading_raw.md` — the running text with decoded runs in italics.
- `reading.md` — the edited reading, with word division and an English summary.

## Reproducing

`python decode.py` prints the decode of `transcription.txt`; `python render.py` rewrites `reading_raw.md`.
The working crops are not kept in the repo: regenerate them from `img/` with a crop-and-upscale of the
region you want (2.5–5× LANCZOS on a grayscale conversion is what the figures were read at).

## Companion letter no. 249 uses the same key (19 Sept 2026)

PARES search `texto=Garcia de Toledo Malta`, 1565, lists EST,LEG,1394,249 (record 3576586, dbCode 27138937, four
images): "Duplicado de carta de García de Toledo … a Felipe II", Messina 16 July 1565, one page with thirteen lines
of figures in clear Spanish. The figures decode with this key: *Sauiendo le entrado el socorro* · *la llegada de
los* (navios) · *Cabo Bono* · *Argel* · *las galeras … con la gente a la Goleta* · *a mal tiempo* · *(r)espuesta
del Maestre* · *forma de ponelle mas gente* · *falta* · *pide mas de la que yo agora le puedo dar* · *partiran las
galeras mañana* (ñ = *nn*). New sign: a barred θ for *ll* (in *llegada*, *ponelle*); the *r* of *respuesta* is
written as an M-like sign. Not transcribed in full. No. 248 (same day, to Eraso) is in clear on its first page.
Estado leg. 1395 not checked.
