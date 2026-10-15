# BnF fr. 3022 no. 6: del Vasto to Charles V, Rome, early December 1527 (Cipher 2; catalogue item 7)

Status: read (22 Sept 2026, 98.0% measured). Split 14 Oct 2026: no. 20 and the Ranzo letters (a different code) are now `targets/ranzo1528/`; no. 10 (Cipher 1) is a third cipher with its own key, recovered by Lasry (2023) from no. 10 itself, and read in part by Lasry and Tomokiyo; it is a separate cipher from no. 6's Cipher 2 and is a cross-reference only (one key per entry: this entry presents Cipher 2, nos. 6 and 19).

Gallica ark `btv1b90601558` (view = canvas; ink folio ≈ (view+1)/2; the BnF notice's folio numbers run about
3 higher than the ink foliation). Work done 2026-09-18; no. 6 measured and extended 2026-09-22.

## Verdict per item

| no. | ink ff. / views | what it is | status |
|---|---|---|---|
| 10 | ff. 26–28 (views 51–55) + loose f. 39 (views 76–77) | del Vasto to Charles V, "De Ysola" (Ischia), 27 Sept 1527 | **a different cipher (Cipher 1), cross-reference only since 14 Oct 2026: read in part by others, not measured here.** George Lasry (2023) with Satoshi Tomokiyo's edited text (2026), cryptiana GL.htm §"Gasto–Charles V Cipher 1"; copy in `prior/BnF_fr3022_f26_decryption.txt`. That file is an edited plaintext, not a sign transcription, so no cipher-token fraction can be taken from it. Of its 1,146 words, 47 carry a `?` (19 of them a bare `?` for an unread group), and some stretches are garbled ("como sin qve prometio", "esaique?s"). Tomokiyo still asks for someone to complete it. Not reworked here. |
| 6 | ff. 16v–17v (views 32–34) | catalogued as "Rapport … à l'empereur", no author; actually del Vasto to Charles V, [Rome, early Dec 1527]: it cites his letters of 6 Nov and 27 Sept, reports the Pope's release agreement, and awaits Orange "de aqui a tres dias" | **read, 98.0% measured** (1,646 of 1,680 cipher tokens, `n6_signs.tsv` / `n6_measure.py`, 22 Sept 2026). Lasry's key alone gives 92.6% and the 18 Sept identifications 94.9%. The 18 Sept verdict "read" was unmeasured. Open: 10 code group types (11 tokens) and nine short stretches (23 tokens); see Remaining gaps. |
| 20 | ff. 44r–46v (views 86–91) | Italian letter, Madrid 11 April 1528, to "Garbino", in Ranzo's code | **a different code: moved to `targets/ranzo1528/` on 14 Oct 2026.** |


Also in the volume:
- **f. 16r–v** is clear text.
- **ff. 48–50v (nos. 20bis–21)**: Garbino's espionage kit, which belongs with no. 20 (`targets/ranzo1528/`).

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

`python targets/vasto1527/n6_measure.py [--text]` checks that the tokens reproduce Lasry's stream exactly and counts them.

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

## Remaining gaps

- No. 6 code groups dnh, bnq, rar (x2), car, cny, bny, beb, bnc, ge+, and der at 17va.2 (11 tokens; 10 group types) - blocker: open-codes; one or two contexts each, and none fits a single value. rar is Florencia or Luca ("ganar en el camino a [rar] y ponella debaxo el mando de V. M."). ge+ may be a stop. dnh ("segun la [dnh]") does not fit Roma. Further contexts are in no. 19 ff. 41–43, which have not been transcribed.
- No. 6 stretches "y y por [mq]" at the head of f. 16v, "es [en de las los] que mas se ha de trabajar", "el duque de Urbino [es de] otro exercito", "servira [que de con] mil [cny]", "ira [que l] camino", "la principal de [der de] pais" (der = poca does not fit here), "en [cnt] parte" (ninguna or otra), "esperar [es] mas ventaja", "apuntamiento [es] [bnc]" (23 tokens besides the codes) - blocker: open-codes; the signs are transcribed, but the syllable-code values that make sense elsewhere do not make sense here. Probably Lasry's labels merge different glyphs, as they do for es/en and con/tan/ellos. Needs a glyph-level retranscription of these words.

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
- `prior/`: Lasry/Tomokiyo decryption files and key images
- `bho/`: CSP Spain III.2 pages (BHO)
- `mk_validation.py`, `validation.tsv`: statistical check of the no. 6 reading
- image tools for the fr. 3022 scans (`blocks*.py`, `grid*.py`, `crop20.py`, `halves.py`, `lines.py`, `seg.py`, `sheet.py`, `slowfetch.py`); `lm.py` Spanish letter model from the Memorias

## 14 Oct 2026: split from Ranzo's code

Until 14 Oct 2026 this folder also held no. 20 (the letter to Garbino) and Ranzo's letters, which are in a
different system altogether: an initial-letter code with numbered word lists, where nos. 6 and 19 are a shifted
letter cipher with three-letter code groups. George Lasry pointed out that entries combining different ciphers
are confusing, and the page had been titled "Del Vasto to Charles V, and a letter to Garbino". No. 20, the Ranzo
letters, the addition sheet, Rosson's measure and George Lasry's contributed Ranzo edition moved to
`targets/ranzo1528/` (`n20/`, `lasry/`, `additione.json`, `measure_rosson.py`, `clairfetch.py`, `ita/`) with their
own page (`docs/ranzo1528.html`). No. 10 (Cipher 1, Lasry 2023 / Tomokiyo 2026) is a third cipher, not reworked
here; it is kept as a cross-reference only and no longer counted as part of this target. What remains is no. 6,
del Vasto's December letter in Cipher 2, with no. 19 as its sibling: read, 98.0% measured. The image tools
(`blocks*.py`, `grid*.py`, `crop20.py`, `halves.py`, `lines.py`, `seg.py`, `sheet.py`, `slowfetch.py`) work on the
fr. 3022 scans and stay here.
