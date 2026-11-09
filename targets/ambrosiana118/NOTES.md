# Ambrosiana A 118 inf., f. 154r: vowel-shifted heading over a plain Latin poem (catalogue #1347)

Status: attempted, not solved. The one enciphered word was not turned into a name.

Source: Biblioteca Ambrosiana, A 118 inf., unit 1, n. 6, f. 154r (guard-leaf insert). OPAC `ambro:catalog:25605`:
"Carme cifrato, inc. Carmina edita per mfnpflrfp. Altisono similis credit regnare tirampnus..." (bot check: the OPAC
record opens in the built-in browser, not curl). Images: IIIF manifest
`digitallibrary.unicatt.it/veneranda/data/public/manifests/0b/02/da/82/80/14/a1/a6/0b02da828014a1a6.json`, canvas 319
(`319_A118inf._c.154r`, 1513 x 2000 px at `full/max`). The route works with curl.

## What the leaf holds
- Top left: a framed Latin poem of 16 lines on a tyrant and his wars ("Altisono similis credit regnare tirannus"),
  under the heading `Carmina edita p mfnpflrfp`. The body is plain Latin with ordinary abbreviations, not enciphered
  (`poem.txt`). The catalogue's "carme cifrato" refers to the heading only.
- Below and to the right: Italian verse, the right-hand column headed "Petracca" (Petrarch's *Pace non trovo*,
  *Benedetto sia 'l giorno*) in a second hand. Not enciphered.

## The cipher
- `mfnpflrfp` (9 letters; `heading_cipher.txt`) has no a, i or u and only f, p, l where e, o, i would stand. A vowel
  shift fits: each vowel written as the next letter, a>b, e>f, i>l (j and k skipped), o>p, u>x.
- Undone, the word reads ?-e-n-o-e-i-?-e-o with the seventh glyph r or x (x = u). No Latin or Italian name or word
  results from either reading. The first glyph is a ligature (OPAC: "m") and minim letters (m, n, u, i) are
  ambiguous in this hand, so the transcription of the ciphertext itself is not secure.
- Also tried: the full-alphabet Caesar shift of one (gives "lemoekqeo", no word).

## Prior art
OPAC lists no decipherment. Web searches on the incipit and on lines of the poem found nothing (9 Nov 2026).

## Remaining gaps
- first and seventh glyph of the heading word, reading of the whole word - blocker: illegible; the 1513-px IIIF image is the only copy, the glyphs are minim-ambiguous
- identification of the poem and its author in other manuscripts - blocker: no-key-material; no edition or incipit database found, none searchable online

## Escalation
- [n/a] siblings: no sibling cipher leaves on this folio; the rest of the codex is plain
- [n/a] clear-pages: the poem itself is the clear text
- [x] known-keys: vowel shift read off the heading; full Caesar +1 tried and rejected
- [x] print: OPAC and web searches on the incipit and lines of the poem, nothing; Walther and Mirabile not yet consulted
- [n/a] key-rebuild: the key (five vowels) is not in doubt; the 9-letter ciphertext is
- [n/a] retry: nothing to retry with a longer text

## Next step
Compare the heading against attributions of the poem in other witnesses (Poetae latini aevi / Walther, *Initia
carminum*, Mirabile) and against the glyph shapes of the codex's other headings.
