# BnF fr. 3022 nos. 6, 10, 20: del Vasto and Ranzo ciphers, 1527–28 (catalogue item 7)

Gallica ark `btv1b90601558` (view = canvas; ink folio ≈ (view+1)/2; the BnF notice's folio numbers run about
3 higher than the ink foliation). Work done 2026-09-18; no. 6 measured and extended 2026-09-22.

## Verdict per item

| no. | ink ff. / views | what it is | status |
|---|---|---|---|
| 10 | ff. 26–28 (views 51–55) + loose f. 39 (views 76–77) | del Vasto to Charles V, "De Ysola" (Ischia), 27 Sept 1527 | **read in part by others, not measured here.** George Lasry (2023) with Satoshi Tomokiyo's edited text (2026), cryptiana GL.htm §"Gasto–Charles V Cipher 1"; copy in `prior/BnF_fr3022_f26_decryption.txt`. That file is an edited plaintext, not a sign transcription, so no cipher-token fraction can be taken from it. Of its 1,146 words, 47 carry a `?` (19 of them a bare `?` for an unread group), and some stretches are garbled ("como sin qve prometio", "esaique?s"). Tomokiyo still asks for someone to complete it. Not reworked here. |
| 6 | ff. 16v–17v (views 32–34) | catalogued as "Rapport … à l'empereur", no author; actually del Vasto to Charles V, [Rome, early Dec 1527]: it cites his letters of 6 Nov and 27 Sept, reports the Pope's release agreement, and awaits Orange "de aqui a tres dias" | **read, 98.0% measured** (1,646 of 1,680 cipher tokens, `n6_signs.tsv` / `n6_measure.py`, 22 Sept 2026). Lasry's key alone gives 92.6% and the 18 Sept identifications 94.9%. The 18 Sept verdict "read" was unmeasured. Open: 10 code group types (11 tokens) and nine short stretches (23 tokens); see Remaining gaps. |
| 20 | ff. 44r–46v (views 86–91) | Italian letter, Madrid 11 April 1528, **to "Garbino"** (endorsement, f. 47v); the writer is almost certainly **Hieronimo Ranzo**, Gattinara's man (same code as Ranzo's signed letters, below) | **not solved.** Code structure established, full transcription made, function-word skeleton only. See below. |

Also in the volume:
- **f. 16r–v** is clear text.
- **ff. 40–43 (no. 19, 6 Nov 1527)** is Cipher 2. Its content is summarised in CSP Spain III.2 no. 233 (from RAH Salazar A-41 f. 329).
- **ff. 48–50v (nos. 20bis–21)** is Garbino's espionage kit:
  - A jargon sheet: cover letters are signed "Antonio de Cosenza" and addressed to "Andrea Romano in Valencia", and news is disguised as grain prices.
  - A code-name list, e.g. Imperatore = "Joan Jacobo", Marchese del Guasto = "portolano de Gergenti", Garbino = "antonio petra".
  - The **"Aditione nel zifra"** (`additione.json`).

## No. 6 / Cipher 2 (del Vasto, Dec 1527)

Caesar +1 over a 21-letter alphabet with homophones, plus b-/c-/d- three-letter codes. Lasry's key also has a
row of two-per-syllable code signs (al, con, de, el, es, la, lo, no, para, por, qve, sin). Tomokiyo (GL.htm)
already doubted those pairings.

**Measurement (22 Sept 2026).** `n6_signs.tsv` is the reading file. It keeps Lasry's decryption of ff. 16v–17v as
a sign-level token list, one token per cipher sign in his labels. Each run of tokens gets a reading and a status:
- r: Lasry's value as it stands;
- i: a value inferred on 18 Sept;
- n: a value inferred or glyph-checked on 22 Sept;
- u: not read;
- x/w: signs seen on the image that Lasry left out.

`python vasto1527/n6_measure.py [--text]` checks that the tokens reproduce Lasry's stream exactly and counts them.

| state | tokens read | fraction |
|---|---|---|
| Lasry's key alone | 1,555 / 1,680 | 92.6% |
| with the 18 Sept code readings | 1,595 / 1,680 | 94.9% |
| now | 1,646 / 1,680 | **98.0%** |

Nomenclator group tokens (titles excluded): 27 read, 11 open.

**Code values**, all grade I (inferred from context). The 18 Sept list is in `n6_reading.md`.
- In no. 6 from that list: di mandado, coy Italia, baf primero, biq duque, der poca, raq mi, dnd qual,
  bim empresa, cip mil, dod quando, cac Florencia, bog buelta, bag rica, boq estado, deh Marca, dnb dinero,
  det he, bad basta(ra), bas deve (or puede).

Added or corrected on 22 Sept, with glyphs checked on views 32–34:
- **bet = dello**: "no quedando en Lombardia exercito [dellos] tan pujante"; no. 19 f. 41v "el poco cuidado que
  [dello] he". It was open.
- **da = otro**, not liga: "no[da]s" = nosotros and "no hiziesen [otro] fruto" in no. 19.
- **dop = tiempo**, not invierno: "si el [tiempo] que ya entra fuerte no lo estorva"; "en estos [tiempo]s".
- **dab = tiene(n)**, as das: "porque ellos no [tiene]n gente".
- **<37> = final(mente)**: "y [final]mente no podrian …", and "y [finalmente] yo veo" / "el exercito esta" in no. 19.
  At 17va.11 the glyph is ſ (r), not <37>: "si persevera[r]a".
- **Syllable signs**, which Lasry pairs wrongly:
  - boz = esto, not fin: "y por esto pienso", "a estos enemigos", "en estos tiempos".
  - bab = mas: "y demas pasaren", "y mas se podra ver".
  - bar = tan: "tan adelante", "tan cerca".
  - bop = como: "como si", "como por otras", "como ay", "como sus fieles".
  - bopt = ellos: "hallandose ellos pasados", "porque ellos no tienen gente". Lasry reads it "con s".
  - bie = el: Lasry "al".
  - bis = de: "banda de alemanes".
  - bep = es in "es poca gente", "es ganar", but en in "y o en alguna manera … o en hazelles la guerra",
    "que en tantas faltas", "y en todo".
- **at and quia** are clear/cipher switch markers, not text. "at" stands at every boundary in nos. 6 and 19, both
  entering and leaving the cipher (after "Mylan.", after "socorrido.", at the ends of cipher runs on ff. 41r and
  41v). "quia" (Lasry "p l <33>") stands before the cipher on f. 17r (twice) and f. 41r.
- The barred sign ≡ (Lasry "?") is a stop.

The content is del Vasto's plan to take the army out of Rome toward Tuscany: secure Siena, threaten Florence,
take Perugia and the state of Urbino, and pass into the Marche. He also warns that the army cannot be sustained
"desta manera" without money. `n6_reading.md` has the 18 Sept edited text; `n6_measure.py --text` prints the
current one.

## No. 20 / the Garbino–Ranzo code

**System.** Each group is a base letter with a superscript number: c170, i100, p149 and so on. The addition
sheet (f. 50) shows that the base letter is the initial of the word or syllable (a327 apresso, c327 Cartagenia,
g215 Garbino, h106 havendo, s395 soa santita). It also shows that entries continue each letter's base list
(a1–326, b1–156, c1–326, …, z1–35).

**The numbering within a letter is not alphabetical.** Tested in `n20/alphatest.py`:
- no. 20 scores z = −0.5 against a shuffled-order null.
- The test's power check, a genuinely alphabetical code applied to Castiglione's letters, scores z ≈ +6.5.

So a number carries no positional information. Other bases:
- **z** (z6–z9, z15): behaves as nulls or punctuation.
- **y** (y2–y53, ~130 tokens): a genuine list of unknown initial. Its glyph resembles the addition sheet's x.
- **Q** and **D**: rare extra lists.

**Ciphertext in the same code.**

| source | groups | notes |
|---|---|---|
| no. 20 (`n20/f44r.txt` … `f46v.txt`) | 1,315 (546 types) | transcribed from full-resolution scans |
| Ranzo's signed letters, BnF fr. 2988 ff. 2r–v, 9r–10v (ark btv1b9059908w, views 6, 7, 17–20) | ~2,600 | `n20/ranzo_c0*.txt`, transcribed by six subagents. f. 2v is marked "dup.ª" (duplicate). |
| **Total** | ~3,900 | 316 group types shared between the two sources |

fr. 2988's other "pièces en chiffre" (views 43–87, alternating with clear copies of Doria letters, July–Aug 1528) are a dense symbol cipher of the French side, not this code; checked views 56 and 60. Ranzo in fr. 3019 no. 27 (f. 73) is views 114–116 of btv1b9059994n: signed 'Hieronimo Ranzo', all in cipher, no interlinear or separate decipherment (view 118 is an unrelated 1559 docket); not transcribed. No duplicate or crib either: the no. 20 and Ranzo transcriptions share nothing longer than stock three- and four-group phrases. Cipherbrain (17 May 2016, comments by Norbert Biermann and Thomas, 2017) found no known nomenclator for Ranzo's code. Also and
possibly fr. 3019 no. 36 (f. 94, "Reporto de homo … venuto da Genova", chiffré).

**Clair. 327 ff. 279–280** (btv1b9000764n views 263–264) is an 18th-century copy of no. 20. It is headed
"Vol. 86 fol. 44 … Lettre non signée écrite au seigneur Garbino du 11 d'avril 1528 … partie en chiffre, partie
non", and has no decipherment. **Clair. 314 f. 337** (btv1b90007741 view 252) copies the addition and jargon
sheets. No French decipherment and no base key was found.

**Attack (`n20/solve2.py`).** A word-substitution annealer:
- each group type maps injectively to a word with the right initial
- z-groups are optional nulls
- scoring is a Kneser–Ney word-bigram model on Castiglione's *Lettere* (1769–71 ed., long-s OCR repaired) plus Guicciardini/Machiavelli from Wikisource

It was validated on a held-out 3,900-word Castiglione control encoded the same way: **token accuracy ~46%,
type accuracy ~9%**. So on the real text it can deliver only the function-word skeleton. That skeleton is
stable across six restarts:
- che (c170), il (i100), per (p149), la/le (L10/L47), re (r41), non (n38), si (s8), sua (s233)
- tanto (t89), tempo (t10), ma (m8), ne (n8), mi (m170), più (p246), molto (m7), nel (n90)
- ha/ho (h57/h30), in (i29), perché (p150), con (c227), a (a127), o (o113), io (i286), al (a137)

Content words are not recovered. **A reading needs the base key or real cribs.** The most promising crib
sources are:
- Garbino's side of the correspondence;
- Ranzo's letters in Spanish or Italian archives with contemporary decipherments;
- Gattinara's papers.

## Remaining gaps

- No. 20 (Madrid, 11 Apr 1528, to Garbino), whole letter - blocker: no-key-material; Ranzo's code is non-alphabetical, the annealer recovers only function words on a matched control; needs Ranzo's table or a clear copy.
- No. 6 code groups dnh, bnq, rar (x2), car, cny, bny, beb, bnc, ge+, and der at 17va.2 (11 tokens; 10 group types) - blocker: open-codes; one or two contexts each, and none fits a single value. rar is Florencia or Luca ("ganar en el camino a [rar] y ponella debaxo el mando de V. M."). ge+ may be a stop. dnh ("segun la [dnh]") does not fit Roma. Further contexts are in no. 19 ff. 41–43, which have not been transcribed.
- No. 6 stretches "y y por [mq]" at the head of f. 16v, "es [en de las los] que mas se ha de trabajar", "el duque de Urbino [es de] otro exercito", "servira [que de con] mil [cny]", "ira [que l] camino", "la principal de [der de] pais" (der = poca does not fit here), "en [cnt] parte" (ninguna or otra), "esperar [es] mas ventaja", "apuntamiento [es] [bnc]" (23 tokens besides the codes) - blocker: open-codes; the signs are transcribed, but the syllable-code values that make sense elsewhere do not make sense here. Probably Lasry's labels merge different glyphs, as they do for es/en and con/tan/ellos. Needs a glyph-level retranscription of these words.
- No. 10, the queried words of Lasry and Tomokiyo's edited text (47 of 1,146 words carry a ?, 19 of them bare) - blocker: open-codes; found read by others and not reworked here (it is outside this target's measured fraction); no sign transcription of it exists, so it is not measured.

## Escalation

- [x] siblings: no. 19 (ff. 40–43, same key). Lasry's decryption of f. 40 was used for contexts. ff. 41r and 41v were scanned on the images for the open groups, which gave bet = dello and the at/quia markers. ff. 41–43 were not transcribed in full.
- [x] clear-pages: the clear passages of no. 6 (ff. 16r–17r) frame the cipher and fixed its date and the at/quia markers. No clear duplicate of the cipher exists; CSP Spain III.2 no. 233 summarises only no. 19.
- [x] known-keys: Lasry's Cipher 2 key (prior/BnF_fr3022_f16.png). Its syllable-sign row was corrected against the glyphs (boz, bab, bar, bop, bopt, bie, bis, bep).
- [n/a] print: no. 6 is not calendared. CSP Spain III.2 covers no. 19 only.
- [x] key-rebuild: code values were inferred from context across nos. 6 and 19 (grade I).
- [x] retry: the 22 Sept pass re-read no. 6 against the images wherever a reading turned on a glyph (views 32–34), and measured it. Still to do: a full glyph-level transcription of no. 6 and of no. 19 ff. 41–43. That would settle the merged syllable signs and give more contexts for the 10 open groups.

## Files

- `n6_signs.tsv`, `n6_measure.py`: no. 6 sign-level reading file and its measure (22 Sept 2026)
- `n6_reading.md`: no. 6 edited reading and code table (18 Sept 2026)
- `n6_codes.json`, `n6_subst.txt`, `n6_lasry_joined.txt`: working files
- `n20/`: transcriptions (no. 20 and Ranzo), `load.py`, solvers (`solve.py` and `anchor.py` assume
  alphabetical order, now refuted; `free.py`, `solve2.py`), `alphatest.py`, `calib.py`
- `additione.json`: the addition sheet (f. 50–50v)
- `prior/`: Lasry/Tomokiyo decryption files and key images
- `bho/`: CSP Spain III.2 pages (BHO)
- `ita/prep.py`: corpus preparation. The corpus texts themselves are not committed.

**DECODE R1894 (catalogue entry 170), 21 Sept 2026.** The record "BNdF AncienFonds invnr.2988 ff9-11" (Ranzo, Italian, 4 pp.,
dated 1520 by BnF's 1520-29 range) is the fr. 2988 Ranzo letter already transcribed above. The record has no key, decipherment or
transcription. Nothing new was attempted, and the entry is marked "attempted, open" in the same state as no. 20.
