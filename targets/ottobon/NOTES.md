# Marco Ottobon to Giovanni Mocenigo, 27 April 1589 (BNE Mss/994 ff. 34–38) — NOTES

Status: read in part — key identified (Council of Ten's Zifra Prima, DECODE R1789 + two homophones); letter
deciphered in part, 62.7 % of tokens measured (981/1,565, measure_rd.py, 9 Oct 2026, after the dec.py/fit.py
re-reading; 46 % before). Open: ff.35v-36v and gaps of ff.37r-38r, blocked by the image resolution / register copy.
See §9-§11, Remaining gaps, Escalation.

**Verdict (2026-10-09, fourth session): the letter is enciphered in the Zifra Prima of 1577-78 (ASVe CX, Cifre, b.4
reg.16 ff.64-65 = DECODE R1789), with two extra homophones (d83 = a, c86 = o). The first-pass transcription's digit
errors are systematic (7 read as 2, 8 as 0, 3/5/8 confused); corrected against the key and the DECODE images, 721 of
1,566 tokens read as Italian (46 %), the second piece (ff.37r-38r) best (56-72 %), ff.35v-36v worst (12-17 %). It is the
Senate's answer to a French request for help to Henry III: Venice will intercede with Sixtus V on the King's behalf.**

**Verdict (updated 2026-09-16, third session): all seven cipher pages transcribed at first pass (1,528 tokens, 196 distinct) from the BNE images, which are the same ~130 dpi as the PDF; the design is a Venetian letter-plus-figure nomenclator of the 1577-78 *Zifra Prima* type (base letters a c d f g h, figures 1-99, letters, syllables and words mixed), not N.11; ciphertext-only solving in progress, see §8. Two archival keys are the short route: DECODE R1789 (b. 4 r. 16 f. 64) and R1790 (f. 79).** Earlier verdicts follow.

**Verdict (first session): blocked at the images, not attempted cryptanalytically.** The manuscript is digitised in full by the
Biblioteca Nacional de España (BDH record bdh0000174344, now BNE Digital oid 0000174344) and the letter is also
DECODE record R2252, nine openings. Neither image set can be reached by a script from this network: every bne.es host
that serves images sits behind a Cloudflare Turnstile check that curl, WebFetch and Playwright-driven Chromium, Chrome
and Edge (headless and headful) all fail, and the DECODE files need a login. A browser session by a person gets either
in minutes ([GET_IMAGES.md](GET_IMAGES.md)). What was established without the images is below, and the attack is
prepared so that the transcription can start the day the folios are in hand.

Session 2026-09-16.

## 1. What the item is

Tomokiyo, *Unsolved Historical Ciphers*, "Venetian Letter in Spanish Archives (ca.1589)": "Ms. 994 of National
Library, Madrid, contains an undeciphered letter from Venetian secretary Marco Otthobon to ambassador Juan Mocenigo,
dated 27 April 1589. Valle de la Cerda appears to have solved it, but his solution is lost. … The cipher symbols
consist of an alphabetical letter followed by Arabic figures." His Valle de la Cerda article adds that Catalina, Duchess
of Savoy, gave the letter to Valle at Turin on the Duke's orders, and cites Carnicer and Marcos p. 245 and Navarro
Bonilla et al. (2015) p. 115.

The printed catalogue (*Inventario general de manuscritos de la Biblioteca Nacional*, III (897–1100), Madrid 1957,
pp. 214–216; PDF at bne.es, `invgenmss03.pdf`) describes Mss/994, *Cartas orij. en cifra*, 191 folios, as Valle de la
Cerda's own dossier of his services as *Secretario de la Cifra*, and gives item 5 as:

> Carta en cifra de Venecia que dio en Turin la Señora Infanta Doña Catalina por orden del Duque de Saboya a Luis
> Valle de la Cerda que declaro y no tiene contracifra ni declaración por hauerse perdido. [La carta es del secretario
> Marco Otthobon al Embajador Juan Mocenigo, 27 abril 1589. Firma autógrafa] (fol. 34).

Item 6 begins at fol. 64 and fol. 39 is listed blank, so the letter is ff. 34–38; the volume's foliation runs ahead of
the image count because fols. 10–12, 14–21, 40–57, 61–63, 73–82 and 160–176 are missing (torn out by Tiran in 1842 for
the Affaires étrangères, or lost). The same volume holds Valle's other trophies: Alençon's letters with the
reconstructed alphabet (fol. 5), Rogers to Nicles 1585 (fol. 26), Longlée's letters (fol. 64), Sertori's cipher
(fol. 83), the Princess of Ascoli's booklet (fol. 92), Philip III's test cipher of 1599 (fol. 103), the *cifra de los
secretos de las minas* (fol. 113) and a hundred-year-old cipher (fol. 186).

The record on Europeana (`/2022717/bnesearch_detalle_bdh0000174344`) carries the BDH metadata: *Memorial de los
servicios prestados a los Reyes Felipe II y Felipe III por D. Luis Valle de la Zerda, correspondencia y documentos del
mismo*, "Originales y copias", "Varias h. en blanco", olim Mss/18724/5/1.

### The people

- **Giovanni Mocenigo** was the Republic's ambassador to Henry III, at Tours with the King in March–April 1589 (his
  dispatches of 14 March and 6 April 1589 are calendared in *CSP Venice* viii, nos. 823 and 825, both "Italian;
  deciphered"), and stayed on with Henry IV; Bonavoglia (2019, n. 22) records that in June 1595 the Council of Ten
  recommended Partenio's cipher after learning from Mocenigo, "the previous ambassador in France", that François Viète
  boasted he could read Venetian ciphers. Not the doge of that name (DBI 75).
- **Marco Ottobon** (Venice 1554 – 1649), *cittadino originario*, secretary of the Senate from 1584, on missions
  1588–97, later secretary of the Ten and *cancellier grande* in 1639 (A. Menniti Ippolito, DBI 79, 2013). Venetian
  Senate letters to ambassadors were subscribed by a secretary of the Senate, so a letter "from the secretary Marco
  Otthobon to the ambassador" with Ottobon's autograph signature is most likely a **Senate dispatch to the embassy in
  France**, whose register copy would be in ASVe, Senato, Deliberazioni Secreta, for April 1589.* The alternative is a
  private letter from a secretary on mission. The Venice–Paris courier road crossed Savoy, which is how it came to
  Turin and to Valle.

\* Inference from chancery practice, not verified against the register; the register, if it holds the letter, is a
complete crib and turns the problem into key reconstruction.

## 2. What the pages look like

DECODE R2252, "BNE_ms.994_LuisValledelaZerda_5_34r_63v", symbol sets *Alphabet, Numerical*, origin Venice, 9 images,
status N/A, cleartext language given as Latin (probably an error for Italian). The nine 200-px thumbnails are public
([decode/](decode/), montage in `decode/montage.png`):

| image | left page | right page |
|---|---|---|
| 1 | f. 33v blank | f. 34r: Valle's cartouche heading and a ten-line description in clear |
| 2 | f. 34v blank | f. 35r: cipher, full page, ~25 lines |
| 3 | f. 35v: cipher, full | f. 36r: cipher, full |
| 4 | f. 36v: cipher, full | f. 37r: cipher, full |
| 5 | f. 37v: cipher, full | f. 38r: cipher, half page, signature block, seal |
| 6 | f. 38v: address side (a few lines) | f. 39r blank |
| 7–9 | blank openings | |

So the ciphertext is about six and a half pages of dense script, on the order of 150 lines. At the density of
Bonavoglia's specimens (15–25 letter-plus-figure groups per line) that is 2,500–4,000 tokens, more than five times the
Ségur letters and the longest Venetian text on any of the lists. Length is what decided Ségur, Lucca and Warsaw.

## 3. Access: everything tried

| route | result |
|---|---|
| `bdh.bne.es/bnesearch/…`, `bdh-rd.bne.es/viewer.vm`, `pdf.raw`, `high.raw`, `low.raw` | all 308 to `bnedigital.bne.es/bd/card?oid=0000174344&site=bdh` (server: cloudflare) |
| `bnedigital.bne.es/bd/card`, `/bd/medium`, `/bd/viewer`, `/iiif/…` with Chrome headers, es-ES | HTTP 403, 1.3 MB Cloudflare "Un momento…" page with a Turnstile widget |
| WebFetch of the same | 403 |
| Playwright: bundled Chromium headless; Edge headless; Edge headful | Turnstile never clears in 60 s, title stays "Un momento…" |
| Wayback Machine CDX for object 174344 | captures exist only of page 1 (`pdf.raw … page=1`, 2024 and 2025, the binding) and `low.raw` pages 1–5 (2025-07-28); nothing of ff. 34–38 |
| Europeana record | metadata only; `edmIsShownBy` absent |
| Hispana, datos.bne.es, catalogo.bne.es, archive.org search | metadata or nothing |
| DECODE R2252 | RecordsView public; `IMG_R2252_I160NN_PM.png` without login returns a 986×568 "Insufficient permissions to see the full image" placeholder; thumbnails `TH_IMG_…` 200 px |
| Google Books / print | the letter is not reproduced in Carnicer and Marcos (2005) or Navarro Bonilla (2015) as far as their online descriptions show; Lohmann Villena 1954 concerns item 11 |

Not tried, by policy: registering a DECODE account, or any method that pretends the client is not a script. Daniel's
browser session is the way in, and it is quick.

## 4. What the cipher family is, and what to expect

Tomokiyo files the letter with the **Venetian ciphers with superscripts**: a base letter followed by one or two
figures, often written as exponents, for letters, syllables and words. The Council of Ten's cipher book of 1578–87
(ASVe, CX, Cifre, chiavi e scontri di cifra, b. 4, r. 16) holds the *zifra granda* used by ambassadors in European
capitals, described by Bonavoglia (HistoCrypt 2019, §4, Figs. 1–2):

- an alphabet with three homophones per letter (a polywog sign, a turned-T sign and *u* with a figure; his example for
  A is o18 t8 u15);
- an abacus for the ten digits;
- a **syllabary of 27 consonant rows × 5 vowels** whose figures end in 1 2 3 4 5 for -a -e -i -o -u, the base letters
  being f, r and a: ba–bu = f1–f5, ca–cu = f11–f15, da–du = r1–r5, pa–pu = a1–a5, ta–tu = a41–a45 and so on
  (transcribed from his Fig. 2 into [refs/zifra_granda_syllabary.json](refs/zifra_granda_syllabary.json));
- a dictionary of some 500 words (L54 = *Guerra*).

Two years before the letter, on 26 August 1587, the Ten approved Franceschi's ciphers; the *Ziffra N.11* of 1587 (same
book, c. 74) encodes single letters as base letter a/c/d/f/g/h plus 1–20 with a modulo-20 structure (Bonavoglia 2022,
Fig. 7–8; Tomokiyo's table). Bonavoglia's overview (Cryptologia 46, 2021) says the letter-plus-two-figure design was in
use for almost a century, so the 1589 letter may use the zifra granda itself, a re-keyed table on the same plan, or the
1587 generation. Tomokiyo notes there is no evidence either way. Valle read it in 1589 without a key.

Consequences for the attack:

1. **The vowel-slot test decides the design in a minute.** If the figures' last digit is confined to 1–5 within a
   base letter and the mod-5 histogram is far from flat, the syllabary is on the zifra granda plan, and the annealer
   from `targets/segur/` (structured syllabary with vowel slots, clear-text context) applies directly; that solver read a
   97 % control at 460 tokens and here there would be 2,500+.
2. **A direct key-reuse test** against the 1578–87 syllabary: fraction of tokens that are table entries, and the
   Italian 5-gram score of the resulting syllable string against random relabellings ([structure.py](structure.py)).
   If the key is the zifra granda, the letter reads at once, apart from the word list, which the text's own repeats
   will gloss.
3. If neither, it is a homophonic nomenclator with letters, syllables and words mixed; at 2,500–4,000 tokens the
   Lucca/Warsaw 5-gram-plus-dictionary annealer has more than ten times the text it needed, and the Ségur mod-5
   machinery covers any regular syllabary. Repeated formulae (*Serenissimo Principe*, *Vostra Serenità*, *Illustrissimo
   Signor Ambasciatore*, the dateline) are cribs. The crib to look for first: the Senate register copy in ASVe, or
   the calendared substance of Mocenigo's April–May 1589 dispatches (*CSP Venice* viii, nos. 823–828) for the
   subject matter (Henry III at Tours, the treaty with Navarre of 3 April, the levy in Germany, England's fleet).

## 5. Plan once the images are in hand

1. `python render.py ms994_full.pdf` (or `--decode`), then `--crop` each page into strips at 2×.
2. Glyph-level transcription into `ct.txt` with the grammar in [parse.py](parse.py): base letter, figure, whether the
   figure is superscript or inline, one- vs two-digit figures written where two would fit, capitals, the polywog and
   turned-T signs, clear-text words, line ends. Record divergences and doubtful glyphs in `ct2.txt`, as the Birago
   experience requires (his transcriptions normalise marks; here there is none to trust, which is better).
3. `python structure.py ct.txt`: profiles, IC, vowel-slot test per base letter, zifra granda key-reuse test, repeats.
4. Branch on the result as in §4; controls first (a matched synthetic text enciphered with the zifra granda plan and
   with a random nomenclator of the same size), then the target; write up only when the control reads and the target
   either reads or provably does not.

## 6. Files

- `GET_IMAGES.md` — the browser step, both routes, with the file names to save under.
- `parse.py`, `structure.py`, `render.py` — token grammar, structural tests, page rendering and cropping.
- `refs/zifra_granda_syllabary.json` — Bonavoglia 2019 Fig. 2 transcribed; `refs/zifra_granda_fig2.png` — the figure
  (ASVe b. 4 r. 16, reproduced by Bonavoglia "for no profit use only").
- `decode/th_R2252_P1-9.png`, `decode/montage.png` — the public DECODE thumbnails.
- `refs/` does not keep the Bonavoglia PDFs: HistoCrypt 2019 (ep.liu.se/ecp/158/001/ecp19158001.pdf) and 2022
  (ecp.ep.liu.se/index.php/histocrypt/article/download/410/369/312) are open access.

## Sources

- S. Tomokiyo, *Unsolved Historical Ciphers* (cryptiana.web.fc2.com/code/unsolved.htm), *Luis Valle de la Cerda*
  (valle.htm), *Venetian Ciphers with Superscripts* (venetian.htm, last modified 23 Oct 2025).
- *Inventario general de manuscritos de la Biblioteca Nacional*, III, 1957, pp. 214–216 (Mss/994).
- Europeana record 2022717/bnesearch_detalle_bdh0000174344; BNE Digital oid 0000174344.
- DECODE R1940 (biography of Valle, 7 pp.), R2248–R2262 (Mss/994 items 1–15), R2252 (this letter).
- P. Bonavoglia, "Hieronimo di Franceschi and Pietro Partenio: Two Unknown Venetian Cryptologists", HistoCrypt 2019,
  pp. 3–11; "The Enigma of Franceschi's Falso Scontro", HistoCrypt 2022; "The ciphers of the Republic of Venice: an
  overview", Cryptologia 46 (2022) 4.
- *CSP Venice* viii (1581–1591), ed. H. F. Brown, 1894, nos. 823–827 (British History Online).
- A. Menniti Ippolito, "Ottoboni, Marco", DBI 79 (2013).
- D. Navarro Bonilla et al., "Cryptanalysis Skills and Secret Information Practices under Two Monarchs: Secretary Luis
  Valle de la Cerda", in *Geheime Post* (2015); C. Carnicer and J. Marcos, *Espías de Felipe II* (2005) — cited through
  Tomokiyo, not seen.

Checked: catalogue entry, DECODE record and thumbnails, Europeana metadata, all listed access routes, Bonavoglia's
figures. Not checked: the page images themselves, the ASVe register, the 2005 and 2015 monographs. User must verify:
nothing here is a reading; the item stays open.


## 7. Second session, 2026-09-16: the folios

Daniel downloaded the whole manuscript as PDF from BNE Digital (`ms994_full.pdf`, 151 openings, embedded JPEGs of
about 2200 x 1800 px per opening, i.e. ~130 dpi per page). `python -c` extraction into `img/pNNN.jpeg`; contact
sheets `img/sheet0-4.png`. **Page map:** PDF page 29 right = f. 34r (Valle's cartouche heading, as the thumbnail
predicted); 30 right = f. 35r (Latin protocol + 17 cipher lines); 31 = ff. 35v-36r; 32 = ff. 36v-37r; 33 = f. 37v
full + f. 38r (10 lines, signature flourish); 34 left = f. 38v address; 34 right onward blank until item 6.

### What the page says in clear

f. 35r opens with the ducal protocol in Latin, in a chancery hand:

> Pascalis Ciconia Dei gratia Dux Venetiarum etc. Nobili et sapienti viro Ioanni Mocenigo oratori nostro apud
> Serenissimum Regem Christianissimum fideli dilecto salutem et dilectionis affectum.

and the address on f. 38v reads *Nobili et Sap. Viro Ioanni Mocenigo oratori nostro apud Ser.mum Regem
Christianiss.mum*. So the document is a **letter of the Doge and Senate (Pasquale Cicogna, doge 1585-95) to the
ambassador in France**, subscribed by the secretary of the Senate Marco Ottobon, as inferred in §1. Consequences:
the register copy exists in principle (ASVe, Senato, Deliberazioni Secreta, reg. for 1589, under 27 April), and the
plaintext is Italian chancery prose to the ambassador at Henry III's court in the weeks after the treaty with Navarre.

### What the cipher looks like

Base letter followed by one or two figures, inline (not raised), no separators, ~17-22 tokens a line, 17 cipher
lines on f. 35r, full pages on ff. 35v-37v, 10 lines on f. 38r: **roughly 120 lines, 2,000-2,500 tokens**. The base
letters visible are **a, c, d, f, g and a tall looped h** (which reads as a long s at first sight). That is exactly
the alphabet base-letter set of Franceschi's **Ziffra N.11**, approved by the Council of Ten on 26/31 August 1587,
twenty months before this letter: an alphabet of six homophones per letter on a, c, d, f, g, h with figures 1-20
(rows related by shifts mod 20: c = a - 5, d = a + 1, f = a - 8, g = a - 3, h = a - 4), and syllables, numbers and
words on the other base letters, mostly 1-20 with a few 21-99 (Bonavoglia 2022 §9.1, Figs. 7-8; Tomokiyo,
venetian.htm). The alphabet is transcribed into [refs/n11_alphabet.json](refs/n11_alphabet.json) (checked: each
row a permutation of 1-20, and it reproduces Franceschi's own example L15 d8 a20 q8 c10 ... = *quanto io*).
Franceschi's photograph of the table (`refs/n11_alphabet_asve_c74.jpeg`) shows the same numeral forms as the
letter: 6 with a tall stem like a *b*, 9 like a *g*, 5 like a *ç*, looped 4, 7 like a *1* with a foot.

The other candidate, the 1578-87 *zifra granda* (§4), is **excluded on the base letters**: its alphabet sits on
polywog/turned-T/u and its syllabary on f, r, a; here f and a carry figures up to 99 and there is no polywog.

### Why the transcription stopped

Line cutting (`cutlines.py`), bleed-through suppression (background normalisation + gamma; `img/*_clean.png`) and
3x-5x crops (`img/lines/`) make the token shape clear but not the digits: at ~15 px x-height, 1/7, 2/9, 6/b, 5/s
and 0/o are not separable, and the first cipher line lies under the stain. A first pass over f. 35r
(`ct_draft_f35r.txt`, 205 tokens, kept as a draft only) reads 119 tokens inside the N.11 alphabet but with a letter
profile (p, z, f among the most frequent) that no Italian text has, which measures the misreading rate rather than
the key. **Not a transcription of record; nothing was decoded.**

### Next step (Daniel): five high-resolution images

BNE Digital serves each opening at full resolution in the viewer. Needed: viewer images **30, 31, 32, 33, 34**
(the openings f. 34v/35r to f. 38v/39r) downloaded at the highest size offered, saved as `img/hi_p030.jpg` ...
`img/hi_p034.jpg`. At 300 dpi or better the digits separate and the N.11 alphabet can be tested directly with
`python decode_n11.py ct.txt`: if the letter tokens come out as Italian (e a i o n r l t s c on top) the alphabet is
Franceschi's and only the nomenclator remains, glossed from context and the Senate register; if not, the
structured annealer from `targets/segur/` runs on the six-homophone design with the mod-20 row structure as a constraint.

Files added this session: `ms994_full.pdf` (not committed, 33 MB), `img/` (page JPEGs, cleaned pages, line
crops), `cutlines.py`, `decode_n11.py`, `ct_draft_f35r.txt`, `refs/bonavoglia2022.pdf` + `.txt`,
`refs/n11_alphabet.json`, `refs/n11_alphabet_asve_c74.jpeg`, `refs/n11_alphabet_square_fig8.png`.

Checked this session: page map against the thumbnails; the protocol and address in clear; base-letter inventory on
ff. 35r, 38r; the N.11 table's internal consistency and Franceschi's worked example. Not checked: any digit
reading; the ASVe register; whether N.11 was actually issued to the France embassy (Bonavoglia gives no
attribution). User must verify: the ducal-letter identification rests on my reading of the Latin protocol from
the image, which is legible but not collated with a second witness.


## 8. Third session, 2026-09-16: the BNE viewer images and the first-pass transcription

Daniel downloaded the ten viewer images 25-34 (`img/hi00-hi09.jpg`, 2,200-2,600 px per opening: the viewer's largest
size is the PDF's resolution, so no gain in pixels, only in JPEG quality). hi04 = f. 34r heading; hi05 = f. 35r;
hi06 = ff. 35v-36r; hi07 = ff. 36v-37r; hi08 = ff. 37v-38r; hi09 is a later item (a Spanish code list), not ours.

### The letter is partly in clear, and it is two pieces

- **f. 36r, last six lines, clear Italian:** *Il m.ro delle poste di Francia che sta in questa città, ne ha mostrato
  un capitolo di l[ette]ra scrittegli da quello di Lione, che coll'occasione d'inviargli lettere sue gli manda anco le
  4? sole altre? righe delle l[ette]re di 28. del passato, dicendo[gli]* — and **f. 36v, first four lines:** *che il
  rimanente con tutte le altre [lettere] tre sono state intercette in quelle [parti], onde continuamo scriver ...*,
  then one mixed line (*notitia,* + cipher) and five cipher lines, then **Dat. in nostro Ducali Palatio die xxvii
  Aprilis, Ind. [..] MDLXXXIX** and **Marco Ottobon Secr.** So the Senate tells the ambassador that the postmaster of
  France in Venice showed it a passage of a letter from the Lyon postmaster, who forwarded only a few lines of the
  dispatch of 28 [March], the rest and three other letters having been intercepted; hence the cipher. The subject
  matter of the cipher part is therefore what the Senate wanted to keep from the interceptors in April 1589: the
  Tours court, the treaty with Navarre, the levy, England (CSP Venice viii nos. 823-828 give Mocenigo's side).
- **ff. 37r-38r are a second piece** (no protocol, a small cipher header at the top right of f. 37r, 24 + 25 + 9
  lines, ends with a flourish). Either a separate enclosure or the continuation on a fresh sheet; both hands are the
  same chancery hand.

### Transcription (first pass, `ct_f35r.txt` ... `ct_f38r.txt`, merged in `ct_all.txt`)

| page | lines | tokens | notes |
|---|---|---|---|
| f. 35r | 17 | 212 | P1 under the stain |
| f. 35v | 21 | 249 | line ends lost in the gutter |
| f. 36r | 18 | 224 | lines slope; line 17 read twice with 3/5 tokens different |
| f. 36v | 6 | 57 | mixed clear/cipher, crops overlap |
| f. 37r | 24 | 341 | cleanest page after f. 38r |
| f. 37v | 25 | 363 | line ends lost in the gutter |
| f. 38r | 9 | 116 | pilot page |

Method: `cutpage.py` (background normalisation, gamma to drop the bleed-through, periodic line grid) and
`cutmanual.py`; one labelled full-width crop per line at ~2.2x (`img/lines/`). Numeral forms fixed from f. 38r at 5x
and from Franceschi's own sheets: **1 = dotted i, 0 = o, 4 = looped (reads as *a* inside a figure), 5 = long s,
6 = b-shape, 9 = g-shape, 7 = 1 with a foot (rare or misread), 2 sometimes r-shaped**; the base letter h is a tall
looped ascender, at first taken for a long s. **Reliability:** about 70 % per token (one line read in two overlapping
crops disagreed in 3 of 5 tokens); the pairs h20/h50/h52/h22, 1/7, 2/9 and 3/5 carry most of the doubt. `?` marks
the tokens I could not read; the files are a draft, not a transcription of record.

### What the statistics say (python on `ct_all.txt`)

- 1,528 well-formed tokens, 196 distinct, 55 singletons; IC of the token stream 0.0135 (Italian letters 0.075:
  consistent with 5-6 homophones per letter plus a nomenclator).
- Base letters c 324, h 288, d 254, a 246, g 213, f 203. Figures 1-99 on every base letter; only 37 % are <= 20,
  so this is **not** N.11 (letters confined to 1-20 on these six bases). It matches Tomokiyo's description of the
  **Zifra Prima** of 1577-78 (ASVe b. 4 r. 16 f. 64; DECODE R1789): "a letter (a-h) with a superscript figure (1-99)",
  letters, syllables and words "without distinction", two-part (per scriver / per trazer), with d96 = a and f1 Accio,
  f2 Accordo, f3 Ad, i.e. the word list alphabetical on f. Our text has no d96 and its f1-f3 are rare, so the 1589
  key is a sibling, not that sheet itself; f. 79 of the same register (DECODE R1790) is a second two-part code of the
  type.
- Most frequent: d83 66, g99 48, c99 47, a20 39, h52 37, a64 36, h51 35, c86 35, c29 33, g15 30, f20 29, f61 27.
  d83 at 4.3 % is the *e*/*a* level of a heavily homophonic letter or a very common word; the *99* tokens on c and g
  look like a null or a separator. Repeated trigrams (h51 c99 h4; a96 d10 h52; g16 a96 d10, three each) are spelled
  words.
- Digit table: no figure ends in 7 and only 17 end in 8, no figure begins with 7: partly real (a nomenclator need
  not use every number) and partly my 7 -> 1 misreading.

### Ciphertext-only attacks: all fail their controls (nothing decoded)

| solver | target | control | verdict |
|---|---|---|---|
| `solve_letters.py`: every token one letter, 5-gram Italian LM, 150k steps, 4 seeds | -2.75 to -2.81 nats per 5-gram, vowel soup | 3 shuffled texts -2.80 to -2.85 | no separation |
| `solve_units.py` v1: token -> letter, CV syllable or wildcard, score = LM + 2.0/char - 5/wildcard | -2.08/char, syllable soup | matched synthetic (62 % letters x 6 homophones, 23 % syllables, 15 % word symbols, 190 symbols, 1,528 tokens): **0 % letters recovered** at 0 % noise | objective invalid: the LM rewards *nonosicono* strings |
| `solve_units.py` v2: token -> letter or wildcard (-3), 120k steps | -2.33 to -2.47/char, no Italian | same control: **4-9 % letters** at 0 % noise, 3-9 % at 15 % noise | below any useful level |

So a letter-level annealer does not read a 190-symbol nomenclator of this composition even from a perfect
transcription of this length, which is the Joyeuse/Birago result again at larger size; with the ~30 % transcription
noise on top the target is out of reach ciphertext-only. Not tried, and the only things that could change this:
(a) a second, independent transcription pass from better images (BNE has no larger size; the DECODE files or a
scan order from the BNE reproduction service at 300-400 dpi), (b) a structural prior from the key layout (one-part
alphabetical order as in the Zifra Prima sheet f. 64, which would make the initial letter of each plaintext unit
monotone in the a1..h99 order and turn the problem into the Ségur alphabetical-boundary search), which needs a look
at DECODE R1789/R1790, (c) the plaintext itself from ASVe Senato Secreta reg. 87 or Dispacci Francia filza 11, which
turns this into key reconstruction and a check of Valle de la Cerda's lost solution.

### Short route (Daniel)

DECODE R1789 and R1790 are the two keys of this type in Franceschi's register; the 1589 France key would be a
re-keyed copy of the same layout, and either sheet would show the layout (which bases carry the alphabet, where the
syllables sit, how the word list runs) and possibly the key itself. Also worth asking: the register copy of the
dispatch in ASVe, Senato, Deliberazioni Secreta, reg. 87 (1589), under 27 April; and Mocenigo's dispatches of April-
May 1589 in Senato, Dispacci Francia, filza 11, which would carry the same cipher and Venice's own decipherments.

Checked: every cipher line read once from the images (f. 36r lines 16-17 twice, at 4x); the clear passages; the
statistics; both solvers against matched controls before the target. Not checked: the other 118 lines against a
second reading; the DECODE key sheets; the ASVe registers. User must verify: the transcription is a first pass at
about 70 % reliability; nothing has been decoded; the Zifra-Prima identification rests on Tomokiyo's description of
f. 64, not on the sheet itself.


## 9. Fourth session, 2026-10-09: DECODE images, the Zifra Prima key, and key trials

With the DECODE login cookie working, the full-size files were fetched into `img/decode/` (git-ignored):
R2252 (nine openings, 2,930-3,270 px wide, i.e. the same BNE scans, watermarked "© Biblioteca Nacional de España",
about 1.4x the pixels of the BNE viewer images, still JPEG-softened and with heavy bleed-through), and the candidate
keys and siblings R1788, R1789, R1790, R1843, R1870 (3,500-4,450 px). No record has a DOC transcription file.

### What the candidate keys are

| record | what it is | fit to this letter |
|---|---|---|
| R1789, b.4 r.16 ff.64-65 | **Zifra Prima** per scriver (2 pp.) and per trazer (2 pp.): six bases a c d f g h, figures 1-99, words, syllables (in runs of five, often in reversed vowel order), single letters (homophones), doubled letters, numerals, nulls, all mixed | same design and same code space; **transcribed in full from the per trazer pages** into [keys/zifra_prima_R1789.tsv](keys/zifra_prima_R1789.tsv) (527 codes) |
| R1790, b.4 r.16 f.79 | small cipher on bases c/f/m/r (1-20), a dozen words on h; note at foot: *serve la sopradetta ziffra col capitano in Golfo, à quello della Guardia contra Uscocchi, et con li Rettori de Zara* | different bases; not this letter's key |
| R1788, b.4 r.8 | "N.° 8 Germania per trazer": a cardboard grille (caselle) | not relevant |
| R1870, Busta 30 ff.177-181 | Piero Duodo, ambassador in France, 2 Aug 1595, cipher passages with their decipherments | bases o (polywog), a, f, r, c, h: the zifra-granda family, not this one |
| R1843, Busta 6 ff.105-106 | Hieronimo Lippomano, bailo, Pera 20 July 1590 | bases r, a, f, u ...: zifra-granda family |

### Trial of the Zifra Prima on the existing transcription (`trykey.py`)

1,448 of the 1,528 tokens (94.8 %) are codes defined in the Zifra Prima, but the decode is not Italian
(*vestre Illustr a Capi di X va Cardinal tt ... Maone ... Capi di X ...*): a20 = *Capi di X* would occur 39 times and
c86 = *Maone* 35 times. Undefined in it: d83 (66, the commonest token here), g90 (7), g95 (3), d86 (2), g83, f82.
So **the 1589 key is a sibling with the same code space but a different allocation**, as the third session
predicted from Tomokiyo's description.

Usage by code (the counts per base 1-99 are in the session log): this letter concentrates on c20-c29 (all ten
used, 15-33 each), h1-h4, h50-h52, d10-d15, d20-d23, a49-a52, a80-a85, f61-f66, g14-g16, g20-g22, and the high
singletons d83, c86, c99, g99, a64. These are runs, i.e. the 1589 key, like the Zifra Prima, assigns its frequent
units (letters and syllables) in contiguous runs.

`shift_test.py`: the Zifra Prima with base letters permuted and a constant offset per base (6! x 99^6 space, coordinate
ascent on the it-cinquecento 5-gram per character) reaches -2.91/char only by stringing long nomenclator words
(*Sua Serenità, Re d'Inghilterra ...*), not text. **Not a shifted or re-lettered copy of the Zifra Prima.**

### Print / crib

CSP Venice viii (BHO) has nothing for 27 April 1589: the April 1589 section holds only nos. 825-827 (Mocenigo 6 April;
Lippomano and Contarini 29 April), and Brown calendared Senate letters only when they touched England. No crib in print.

### Correction, same session: the Zifra Prima IS the key; the first-pass transcription misreads digits systematically

The Zifra Prima decode looked like nonsense because of the transcription, not the key. Digit statistics of the
first pass: no tens digit 7 at all and only 27 tens 3s, against 427 tens 2s; no units 7, only 8 units 8, against 311
units 0. In this hand the **7 is a z-shape read as 2, the 8 a small closed loop read as 0, and 3/5/8 are confused**.
With those re-readings the frequent tokens fall onto the commonest units of the Zifra Prima: d83 -> d53 *a* (66),
a20 -> a28 *che* (39), c20-c29 -> c70-c79 *lla lu lo li le la ma me mi mo*, g20 -> g70 *da*, d20 -> d70 *Del*, f10
-> f18 *ne*, h52 -> h32 *ti*; the unchanged ones already were (g99 *di*, c99 *r*, a64 *et*, g15 *re*, f20 *no*, f61 *e*,
d10 *po*, d15 *pro*, h4 *so*, h1 *sa*, h20 *Sua Santità*, h22 *Sua M.tà Christianissima*, g22 *Re di Francia*).
Passages then read as Italian, e.g. f.35r ll.16-17 *alcun soccorso per proveder ... al pericolo di quella corona et*
(f6 h4 a4[9] c99 h4 d23 d15 h51 g[7]2 c99 ... d15 h51 d8 g16 a49 ... g99 g10 c[7]5 a49 g[1]7 f1[7] a64), and the
statistical test agrees (Spearman of usage against corpus frequency for the 183 syllable/short-word codes 0.286,
structured null 99th percentile 0.231, p = 0.0008). `beam.py` (per-token Viterbi over digit-confusion variants with
the it-cinquecento 5-gram) gives a first machine draft (`beam_all.txt`); it still prefers long nomenclator words, so
the reading is being done by hand, line by line, from the candidates (`cands.py`) and the DECODE images (line crops
by `cut_decode.py` into `img/dl/`).

**So: the letter is enciphered in the Council of Ten's Zifra Prima of 1577-78 (ASVe CX, Cifre, b.4 reg.16 f.64,
DECODE R1789), unchanged as far as tested.** Valle de la Cerda's "lost" solution is reproducible from the key.

### Machine draft (beam v1)

`beam.py` with optional word spaces between units (it-cinquecento 5-gram with spaces), length credit 1.45/char,
penalty 5 per nomenclator word, digit-confusion costs re-estimated twice by EM (`em_conf.py` -> `conf_em.json`)
re-reads 758 of 1,528 tokens and gives a draft that is Italian in long stretches (`draft_beam_v1.txt`), e.g.
*... sua Cesarea Maestà di sovenir Sua Maestà Christianissima in tanta necessità et soministrarle alcun soccorso per
proveder ... quella corona et assicurar ...*, *... copia che vi mandar ...*, *... informato [di] qualche mutatione ...*,
*... accioche possiate ...*, *... darci lume ...*, *... che facemo della particolar persona [di] Sua Maestà
Christianissima ...*, *... di quel Regno et delli travagli della Maestà Sua ...*. It still over-uses some nomenclator
entries (*Sua Santità* for h30 *ta*, *questa Maestà* for g15 *re*); the hand-checked reading follows.

Print search, same session: no edition of the Senate's letters to Mocenigo or of his 1589 despatches was found
(web search; CSP Venice viii and ix calendar only English-relevant despatches). The register copy (ASVe, Senato,
Deliberazioni Secreta, 1589) is not online. So no crib: the reading rests on the key.

### Hand reading (in progress)

`READING_GUIDE.md` is the working guide; readings go into `rd_<page>.txt` (codes as corrected, unit values, Italian,
confidence per line); `measure_rd.py` measures them. f.35r first pass by hand: the Senate reports a request (by the
French ambassador in Venice, presumably) *... che quel Serenissimo Re porta alla Republica Nostra, et quanto
confid[a] nella cordiale corrispond[enza] ... ne ricercò che [questa Republica] ... con Sua Cesarea Maestà di sovenir
Sua Maestà Christianissima in tanta necessità et soministrarle alcun soccorso per proveder al iminente pericolo di
quella corona et ...*. f.37r (helper agent): *... la molta affettione che in tutti li tempi passati è [stata] da [noi]
portata, et tuttavia porta la Republica Nostra alla Serenissima corona di Francia, e come ben nota ad ogniuno ...
che portamo et la grande stima che facemo della particolar persona di S.M.C.*


## 10. Fourth session, results of the hand reading (2026-10-09)

Three readers worked line by line from `READING_GUIDE.md` (this session on f.35r; two helper agents on ff.35v-36v and
ff.37r-38r), choosing for each token the Zifra Prima code that is compatible with the image and the confusion classes
and makes Italian with its neighbours. Files: `rd_f35r.txt` ... `rd_f38r.txt` (corrected codes, unit values, Italian,
confidence per line), `reading.txt` (the Italian, one paragraph per page), `measure_rd.py` -> `measure_rd.out`.

| page | tokens | high | medium | low | read (high+medium lines, no '?') |
|---|---|---|---|---|---|
| f.35r | 212 | 66 | 85 | 61 | 134 (63 %) |
| f.35v | 249 | 0 | 34 | 215 | 29 (12 %) |
| f.36r | 224 | 0 | 42 | 182 | 33 (15 %) |
| f.36v | 58 | 0 | 11 | 47 | 10 (17 %) |
| f.37r | 342 | 73 | 160 | 109 | 193 (56 %) |
| f.37v | 364 | 57 | 252 | 55 | 238 (65 %) |
| f.38r | 117 | 57 | 50 | 10 | 84 (72 %) |
| **all** | **1,566** | 253 | 634 | 679 | **721 (46 %)** |

(Token counts are those of the corrected lines, slightly above the 1,528 of `ct_all.txt` where tokens were split.)

### What the letter says (as far as read)

**First piece (ff.35r-36v), the Senate to Mocenigo.** [The French ambassador in Venice] *esposti delli travagli et
bisogni ... di Sua Maestà Christianissima ... nella sua prima audientia ... l'amor et afetione grande che quel
Serenissimo Re porta alla Republica Nostra, et quanto confidi[a]mo nella cordiale corrispondenza ... ne ricercò che
[questa Republica] ... con Sua Cesarea Maestà di sovenir Sua Maestà Christianissima in tanta necessità et
soministrarle alcun soccorso per proveder al iminente pericolo di quella corona et assicurarsi dalli nemici ...*;
f.35v, mostly unread, ends *... risposto quello che vederete della copia che vi mandamo col ... et perche informato di
qualche mutatione* (f.36r) *et poi lascia[ta] ... da alcun degli ministri possiate sa[pere] ... et alla ottima
dispositione ...*; f.36v *notitia, accioche possiate con[...] ... lettere et darci lume delle cose*. Then the clear
passage about the intercepted letters of 28 March and the dateline.

**Second piece (ff.37r-38r), the text of the Senate's answer (the "copia" sent with the letter).** *... la molta
afetione che in tutti li tempi passati è [stata] da [noi] portata, et tuttavia porta la Republica Nostra alla
Serenissima corona di Francia, è come ben nota ad ogniuno ... che portamo et la grande stima che facemo della
particolar persona di Sua Maestà Christianissima, per[ciò] sentimo quel dispiacere molto delle [...]tione di quel
Regno et delli travagli della Maestà Sua ... l'ottima dispositione et osservanza ... verso di lei ... con la nostra
pronta volontà verso il servitio di lei ... per dare a Sua Maestà Christianissima quel maggior [...] che per noi si
può al presente ... desiderare et procurare il bene, la grandezza di quella Serenissima corona et particolar commodo
et servitio della sua persona ... habbiamo deliberato ... interponer al presente ... presso lo Sommo Pontifice la
intercessione della Republica Nostra, perche Sua Santità si mova a dovere con la sua somma autorità favorire, ove farà
bisogno, la causa giustissima della Maestà Sua nell'acquetare le sollevationi di quel Regno et ammorzar l'incendio di
guerra, il qual vedemo con gravissimo danno et maggiori pericoli di tutta la Christianità si va accendendo ... per
prudentia et pietà della Santità Sua veder partorir alcun frutto ... potrà Sua Maestà Christianissima conoscere ...
dell'animo nostro verso la grandezza et ogni prosperità di lei, et verso lo beneficio et la quiete della
Christianità ... [na]sce da una pronta et disposta volontà ...*

So the Senate answered the request for help (or for an approach to the Emperor) with an intercession at Rome, in the
weeks before Sixtus V's monitorium against Henry III (24 May 1589). This is the content Valle de la Cerda would have
extracted for Philip II at Turin.

### Key notes from the reading

- The 1589 key is the R1789 sheet plus at least two homophones the sheet lacks: **d83 = a** (66 tokens) and **c86 = o**
  (35 tokens; some c86 tokens of the first pass are c56 *in*, e.g. *in-fo-r-ma-to*). R1789 has c86 = *Maone* and no
  d83. `keys/ottobon_overrides.tsv`.
- Recurrent misreadings besides the digit classes: d15/d11 for d55 *n*; h1 for h4 *so*; g20 for g38 *sta*; h51 for f61
  *e* (f.35r l.9); c64 for f64 *l* (f.35r l.8); h2x for h3x.
- No nomenclator word seen so far falls outside the R1789 vocabulary.

## 11. Fifth session (2026-10-09, later): constrained decoder `dec.py`

A proper noisy-channel decoder replaces `beam.py`: for every first-pass token, P(read | true code) from a base-letter and
per-position digit confusion model **estimated from the 721 hand-read tokens** (first-pass token aligned to the hand
code by DP, `dec.page_pairs`), a code prior from the same tokens (smoothed by unit class), and a 5-gram character LM
with spaces built with the shared `lang` engine on the it-cinquecento sources plus Albèri's *Relazioni degli
ambasciatori veneti* (9 vols, archive.org djvu text, double weight; `build_venlm.py`, corpus in `corpus/`,
git-ignored; 47 M chars). Vectorised Viterbi beam (400 states) over whole pieces, optional word space before every
unit, a "skip" option for garbage tokens; per-token margin = score lost when the token's value is forbidden and a
±6-token window re-decoded (`dec.margins`).

Calibration (`python -I dec.py calib`, leave-one-page-out: channel + prior trained on the other six pages, the page
decoded blind, compared with the hand codes of its high/medium lines, by value):
- identity baseline (first-pass token = hand token): 475/721 = 65.9 %;
- old weights (ALPHA 1, CLEN 1.3, as beam.py): 73.8 %; tuned (ALPHA 0.4, BETA 0.4, CLEN 0.3): **644/721 = 89.3 %**
  (f.37r 92 %, f.37v 91 %, f.35r 87 %, f.38r 86 %).
- synthetic test (`dec.py sim`: the hand-read runs re-corrupted by sampling the channel; 627 tokens): at 55 %
  identity the decoder recovers 82.6 %; at 40 % identity only 61 %. Venetian LM vs it-cinquecento: 82.6 vs 82.0 %.
- word-level lexicon bonus/OOV penalty (corpus word list): no gain (75-82 %); self-training EM of channel/prior on
  the decoder's own output: no gain (89.2 / 88.8 %). Both left off.
- margin calibration on hand-read tokens (`mcal.py`): margin < 1: 56 % agree, 1-2: 78 %, 2-3: 98 %, >= 3: 97-100 %.

The decoder changes 40-48 % of first-pass tokens on every page, the hard pages ff.35v-36v included, so their
first-pass transcription is not obviously noisier than the read pages'; what the hand readers lacked there was
anchoring sense. Output: `dec_out/<page>.txt` (codes, values, Italian, margins, alternatives), `view.py <page>` prints
it with low-margin units in brackets.

### Crib-fit re-reading (`fit.py`, `refit.py`, `texts_reread.txt`)

The decoder alone does not give sense on ff.35v-36v (`view.py f35v`), so the reading is done the other way round:
an Italian text is proposed for a line (from the hand reading, the decoder's draft and the context; `lineview.py`
shows both and each token's candidates), and `fit.py` finds the best code sequence of the line's first-pass tokens
whose values spell it exactly (gaps '...' allowed; channel + prior cost per token). A token counts as read only
when it lies outside a gap and its channel log-prob is >= -8 (the hand readers' own accepted tokens: 98.2 % >= -6,
99.2 % >= -8, none below -10). `refit.py --texts texts_reread.txt --write` rewrites the rd blocks of the lines in
the texts file and keeps the earlier block wherever the fit reads fewer tokens than the hand pass (hand pass kept in
`rd_hand1/`). Parallel print found by a search agent (Hübner, *Sixte-Quint* iii no. 36, Doge to Badoer 13 May 1589:
"la grandezza del pericolo iminente", "questo incendio universale"; ii p. 236, Doge to Badoer 29 April 1589,
French paraphrase) confirms the subject but gives no verbatim crib for the letter.

New readings this pass (first round, 9 Oct): f.35v ll.7-9 *... [giudi]cassimo bene a collegarsi et stringersi
maggiormente in qualche unione di lega, assicu[rar] ...*; l.13 *... iscusandosi*; l.14 *[peri]coli ai movimenti et
per noi*; l.16 *sodisfare come vole[...]*; f.36r l.1 *mutatione, et poi lascia[ta] intentione*; l.2 *evento che ve
ne sia ... da Sua Maestà Christianissima*; f.37r ll.15-16 *quanto alle richieste fateci da Vostra [...] in nome di
quel Serenissimo Re, le dicemo che* (so the second piece is addressed to the French ambassador: it is the Senate's
answer to him); l.2 *[co]pia della risposta fata al Signor ...* (heading of the second piece; kept as low, see the control
below); f.37v l.6 *et
continuata volontà*; f.37v l.20 *incendio di guera*; f.38r l.6 *faciamo ... nasce da un[a]*.

### Control of the crib fit and the result (`fitcontrol.py`)

A crib fit can always place some letters, so each line's text was also fitted onto 15 wrong lines (shifts of 3-59
lines through the letter). Share of tokens "read" by chance: 22 % at channel threshold -8, **10 % at -5**, 5 % at -3;
on the true lines 82 / 80 / 70 %. The re-reading uses **-5**; the five lines whose true fit did not beat the best
wrong-line fit by 3 tokens (f.37r l.2, f.35r l.3, f.36r ll.8, 12, 14) stay low (f.36r l.12 keeps its earlier medium
hand block). Re-measured with `measure_rd.py` (`measure_rd.out`):

| page | tokens | read before | read now |
|---|---|---|---|
| f.35r | 212 | 134 (63 %) | 143 (67 %) |
| f.35v | 249 | 29 (12 %) | 120 (48 %) |
| f.36r | 224 | 33 (15 %) | 78 (35 %) |
| f.36v | 58 | 10 (17 %) | 17 (29 %) |
| f.37r | 342 | 193 (56 %) | 240 (70 %) |
| f.37v | 363 | 238 (65 %) | 285 (79 %) |
| f.38r | 117 | 84 (72 %) | 98 (84 %) |
| **all** | **1,565** | **721 (46.0 %)** | **981 (62.7 %)** |

The read bar (95 %) is not reached. What blocks the rest is the first-pass transcription of the digits on lines
without an anchoring phrase: neither the decoder nor a proposed text can be confirmed there at chance level 10 %.

## 12. Write-up and shared language model (2026-10-09, sixth session)

- **Language model registered in `lang/`.** Source `it-relazioni` (Albèri's *Relazioni*, the nine Internet Archive ids
  of `corpus/`, local glob `targets/ottobon/corpus/*alb*.txt`, new recipe flag `"dehyphenate": true` in
  `lang/corpora.py`) and model `it-venezia` (it-renaissance + it-nunziature + it-relazioni twice = double weight,
  `early` norm, order 5, spaces). Same 47,007,119 characters as the local `corpus/venlm.o5.sp`; 1.3 % of 5-gram cells
  differ (rare ones; file order and separators). `dec.py` now loads `it-venezia` (`LOCAL_VENLM=1` for the old table);
  `build_venlm.py` builds the registered model and writes `corpus/venwords.json`. Check: `dec.py calib` at the tuned
  weights (ALPHA 0.4, BETA 0.4, CLEN 0.3) against the current rd files gives **870/981 = 88.7 % with both models**,
  identical per page. (That reference set includes the crib-fit re-reading, so it is not independent of the decoder's
  channel model; the independent figure stays 644/721 = 89.3 % against the hand reading.) beam.py, confuse.py,
  shift_test.py and zp_repair.py keep it-cinquecento so their recorded results reproduce.
- **Write-up**: docs/ottobon.html (method: read after matching with key from external sources; extent partial,
  981/1,565 = 62.7 %). Crops from the DECODE R2252 images (f. 35r head and foot, f. 38r) and the R1789 per trazer
  sheet. Portraits skipped (nothing trustworthy on Commons/Wikidata for Marco Ottobon or the ambassador Giovanni
  Mocenigo; recorded in docs/_explore_skip.json). DECODE queue: R2252 (Partially decrypted, Italian, sender/receiver/
  date, reading decode_updates/decryptions/R2252.txt with low lines as gaps), R1789 (dates 1577-78, transcription
  offered), R1790 (dates, sheet note).

## Remaining gaps

Measured 9 Oct 2026 (measure_rd.py): 981 of 1,565 tokens read (62.7 %); f.35r 68 %, f.35v 48 %, f.36r 35 %, f.36v
29 %, f.37r 70 %, f.37v 79 %, f.38r 84 %. The unread tokens are where the first-pass digits are too corrupt for the
calibrated decoder (dec.py) or a crib fit (fit.py) to fix them and no anchoring sense exists; an image pass at 2x on
the DECODE scans (previous pass) did not resolve them.
- ff.35v-36v, 316 tokens (f.35v ll.3-6, 10-11, 15, 20; f.36r ll.4, 6, 8-11, 14-16; f.36v ll.2-3, 5-6, and gaps in the read lines) - blocker: needs-physical-access; the only images (BNE scan, ~130 dpi in the PDF, ~1.4x on DECODE) do not separate 2/7, 3/5/8, 0/8 and the bleed-through is heavy; a 400-dpi BNE reproduction of ff.35-38 or the register copy (ASVe, Senato Secreta, Deliberazioni Francia 1589, 27 April) is needed.
- f.35r, 69 tokens (ll.1-3 and 12, about 50, plus gaps in read lines) - blocker: illegible; ll.1-3 under the stain at the head of f.35r, l.12 too faint; no better image than the BNE scan exists online.
- ff.37r-38r, 199 tokens (f.37r ll.1-2, 7, 10, 22, 24; f.37v ll.1, 3; gaps in read lines) - blocker: needs-physical-access; unresolved digits and gutter losses; the text of this second piece (the Senate's answer to the French ambassador) should be in de Maisse's letter-book "avec les responses", BL Add MS 30635 (not digitised), and in the ASVe register.
- f.37r top-right header (four small groups) - blocker: illegible; too small to transcribe at this resolution.

## Escalation

Section 0a of the writeup skill:
- [x] siblings: DECODE R2248-R2262 (Mss/994 items 1-15) opened 9 Oct 2026: the other items are Spanish, French and
  graphic-sign ciphers (Alençon, Rogers, Longlée, Sertori, Philip III ...), none Venetian, no decipherment of this
  letter; ff.38v-63v inside R2252 are the address leaf and blanks. Venetian siblings R1790 (Gulf/Zara cipher), R1788
  (grille), R1870 (Duodo 1595), R1843 (Lippomano 1590): different systems.
- [x] clear-pages: Valle's clear heading on f.34r, the clear passage of ff.36r-36v (postmaster of Lyon, intercepted
  letters of 28 March), the protocol and the address on f.38v read; none is a decipherment. No clear copy of the
  letter in the volume or on DECODE.
- [x] known-keys: R1789 (Zifra Prima, CX b.4 reg.16) is the key, adopted with d83 = a and c86 = o (fourth
  session; 89 % decoder agreement shows no second key is mixed in); R1790 (same register) and R1788 checked and not
  this system; the 1590/1595 Venetian ciphers R1843/R1870 are of the zifra-granda family.
- [x] print: CSP Venice viii (Mar-June 1589), Hübner *Sixte-Quint* ii-iii (Doge to Badoer 29 April and 13 May 1589:
  parallel wording only), Desjardins *Négociations* v, A. Morosini *Historia Veneta* XIII, De Thou XCV: no text of the
  letter or of the answer to de Maisse. Manuscript copies: ASVe Senato Secreta register; BL Add MS 30635-30637.
- [n/a] key-rebuild: the key is the archival sheet R1789 and covers every code read; the two homophones the sheet
  lacks were found from context; no code among the 981 tokens read needs a value the sheet does not give.
- [x] retry: 9 Oct 2026, every unread line retried computationally: calibrated noisy-channel decoder (dec.py, 89 %
  agreement with the hand reading on held-out pages) and crib fits of proposed texts (fit.py, chance level 10 % per
  token vs 80 % on the true lines, fitcontrol.py); 260 tokens gained (46.0 -> 62.7 %). The rest needs a better image
  or a register copy (above).

## DECODE queue

- R2252 (9 Oct 2026 addition): offer the re-read rd_*.txt (62.7 % of tokens) and the decoder; correct the item: the
  second piece (ff.37r-38r) is the Senate's answer to the French ambassador in Venice (de Maisse), headed *[co]pia
  della risposta fata al Signor ...*; f.35v reports his proposal of a closer union (*collegarsi et stringersi
  maggiormente in qualche unione di lega*).

- R2252: cleartext language Italian (record says Latin); plaintext Italian; a ducal letter (Pasquale Cicogna, Doge,
  and Senate) to Giovanni Mocenigo, ambassador in France, 27 April 1589, subscribed Marco Ottobon, secretary of the
  Senate; key = R1789 (Zifra Prima) with d83 = a and c86 = o added; status partially deciphered; two pieces (ff.35r-36v
  letter, ff.37r-38r copy of the Senate's answer to the French request). Offer the corrected transcription and
  reading (`rd_*.txt`, `reading.txt`).
- R1789: date 1577-1578 (Franceschi's register b.4 reg.16; Bonavoglia), not 1500-1799; name "Zifra prima per scriver /
  per trazer"; used Venice -> France (Mocenigo) in 1589 (R2252). Offer the transcription of the per trazer table
  (`keys/zifra_prima_R1789.tsv`, 527 codes).
- R1790: date 1577-1587 (same register); the sheet's note: serves for the Captain in the Gulf, the Guardia against the
  Uskoks and the Rettori of Zara.
