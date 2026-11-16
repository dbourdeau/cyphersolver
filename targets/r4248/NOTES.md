# Unsigned letter to Montmorency, 1536, in the second fr. 3053 cipher (BnF fr. 3053 ff. 85-87; DECODE R4248)

Read in the session of 21 Sept 2026 under `targets/rome1536/` (catalogue item 180).

**Split on 14 Oct 2026 from `rome1536`** under the one-key rule (George Lasry): R4248 is not in Mascon's cipher,
the key of the cardinal de Mâcon's other letters in fr. 3053, but in a second, unrelated cipher, and it was read from
the contemporary decipherment bound with it, not with any key. The cardinal's letters are a different cipher, with
their own page (`docs/rome1536.html`). `R4248.md` (the reading) and Tomokiyo's second fr. 3053 table
(`img/francisMacon2.png`) moved here; the DECODE page crops are git-ignored in the main checkout
(`targets/rome1536/img/IMG_R4248_*`).

## The record

DECODE R4248, catalogued with the eight fr. 3053 letters "Unknown sender (Rome) to Anne de Montmorency". Images: P2-P3 =
f. 85r/v (clear + cipher), P5-P6 = continuation (clear), P8-P9 = f. 86 (clear decipherment). No date, place or
signature on the crops; the letter ends "Hors deux jours je seray a Rome …" (folio 87). 1536 by its place in the
volume. Writer not identified.

## The cipher

The glyph set (ǂ, W, ~, α, ∞, Ɛ, ꝗ, looped ʃ, φ, #, 11, z, k, 30) is not Mâcon's; with Mâcon's key it decodes to
nonsense. It matches **Tomokiyo's second fr. 3053 table** (nulls 30, ǂ, 22; I/J = ~; L = 7/11; R = W; O = 3; U = α;
P = ʃ), and Tomokiyo notes that the f. 85 fragment is "deciphered on f. 86". After *et partant* the cipher
"ꭓ m Ɛ 3 30 11 ǂ" starts JE LE CO[NSEILLOIS], as in the decipherment. The table was not rebuilt.

## Reading (from the f. 86 decipherment)

About 20 cipher lines. f. 86 is a full clear copy of the ciphered part, transcribed in `R4248.md` (~85 % of words
secure in the secretary hand). It agrees with every clear connecting phrase left on f. 85 (*et partant*, *fumee et
vent*, *Je luy dys davantaige*, *car en fin il falloit*, *Et seroit chose trop longue …*). The writer, after a day in
the country with "monsieur le cardinal Carafe(?)", urged him that everything, above all the conduct of the war,
should pass through Montmorency's hands and that anything else was "fumee et vent"; the cardinal seemed persuaded,
and added that the cardinal of Lorraine, in his capitulation with the pope, had conceded things "never thought of
before", which they meant to undo, leaving the whole matter to Montmorency.

Doubtful words of the decipherment: *Carafe*, *[pouvoir?]*, *[Roy?]*, *partir [?]*, *rompre [?]*.

## Open

- The key could be tabulated by aligning f. 85 against f. 86 (the plaintext is complete); not needed for the reading.
  (14 Nov 2026: the values used to check the transcription are listed in `R4248_decode.md`.)
- f. 86 (Gallica view 159) should be re-read against the cipher decode: nine differences, see the 14 Nov 2026 block.
- The writer and the cardinal ("Carafe"?) are not identified.

## Assumptions for George's review

- No Lasry credit on this entry: his Mascon's-cipher table does not apply to R4248, and no file of his covers it.

## 14 Nov 2026: the cipher transcribed and decoded (audit section I, "no transcription file")

- No transcription was in the folder and DECODE R4248 has none (nine images, no text; full-size images need a login).
- Gallica has the volume: BnF Français 3053, ark `btv1b90601432`, 162 views. **f. 85r = view 157, f. 85v = view 158,
  f. 86 (the decipherment) = view 159**, f. 87 = view 160. Fetched at full size through
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90601432/f157/full/max/0/default.jpg`. openapi.bnf.fr answered
  HTTP 500 for view numbers that do not exist (169-173, my first guess) and dropped some connections; retries worked.
- The cipher is longer than the September estimate: **26 lines** (12 on f. 85r, 14 on f. 85v), **712 signs** (measured
  with `_check_profile.py --measure` on the sign labels), broken by clear words. `R4248_transcription.txt` gives every
  sign with a shape label; 8 signs are marked doubtful. A single AI transcription, not checked by a person.
- Check by decoding: `R4248_decode.md`. One value per label, taken from Tomokiyo's second table where the sign matches
  it and from the f. 86 decipherment otherwise. All 26 lines come out as French and follow the decipherment, clear
  links included. Nulls: 30, 22, 19, the three-barred cross, the 3 in a curve.
- Not resolved: one word in line 16 (decoded "aaiette", where R4248.md has "partir [?]"); the ringed x, which is i/j
  but also stands where x ("mieulx") and "pape" are expected (probably more than one sign typed alike); the barred oval
  (r and h) and the reversed c (c and o), look-alike pairs not told apart; one sign with no letter value where the
  decipherment names the cardinal de Lorraine (labelled CL).
- **The decode differs from the transcription of f. 86 in R4248.md in nine places** (table in `R4248_decode.md`). The
  ones that change the sense: "faire fondement dessus vous, qu'est et le scavoir et le pouvoir" (R4248.md: "de vous
  seul, car c'est a scavoir le premier [pouvoir?]"); "qu'il debveroient totallement se remettre en vostre jugement"
  (R4248.md: "qu'il cognoistroit totallement le [Roy?] en ce jugement"); "par vostre moien reordonner les conditions"
  (R4248.md: "par leurs moyens [de] rompre [?]"); "toute capitulation de qui ilz vouloient entierement dependre"
  (R4248.md: "toute l'application de qui vouldroient entierement se rendre"); "ung seur fondement" (R4248.md: "ung
  seul fondement"). f. 86 was not re-read on the Gallica scan in this session, so R4248.md is left as it is and the
  differences are recorded, not settled; `R4248_en.md` has a note pointing here.
- The key is not written as a file: the values are Tomokiyo's table and the contemporary decipherment. Method and
  class unchanged.
