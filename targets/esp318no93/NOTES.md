# BnF Espagnol 318 nos. 93 and 94: Lorenzo Suárez (Venice, 1504) and the viceroy of Sicily (Messina, 1503) — keys not identified

Split on 14 Oct 2026 from `esp318` (the whole volume, catalogue no. 9) under the one-key rule (George Lasry,
14 Oct 2026). **Attempted, not solved.** The two letters are kept together in one entry only because both are unread
and neither key is identified: **no shared key is claimed for them**, and their code-initial bands differ. The other
ciphered letters of Espagnol 318 are different ciphers, each with its own entry and page:
[`targets/esp318/`](../esp318/NOTES.md) (no. 92, the *Cifra general*), [`targets/federico1497/`](../federico1497/NOTES.md)
(no. 5, Escrivà's cipher), [`targets/esp318no95/`](../esp318no95/NOTES.md) (no. 95, Lasry's alphabet).

`ct93_eye.txt` and `solve93.py` moved here (the script now reads the Spanish model `lm.py` / `lm_tabs.pkl` from
`targets/esp318/`). The scans (`full/f118r.jpg` … `full/f121v.jpg`), the segmentation of f. 118r
(`f118r_glyphs.pkl`, `ov/m93a.png`) and the literature (`lit/`, with Quirantes's photographs of the Gran Capitán key
sheets in `lit/crypt/img/`) stay in `targets/esp318/`. Session of 17 Sept 2026.

## The two letters

| no. | ff. | canvases | letter | code initials |
|---|---|---|---|---|
| 93 | 118–118v | 446–447 | Lorenzo Suárez (de Figueroa), ambassador at Venice, to the Catholic Monarchs, Venice, 24 Feb 1504. Wholly in cipher | c/g/h/l/m/n/p/q/r/t/z |
| 94 | 120–121v | 452–455 | The viceroy of Sicily to Ferdinand, Messina, 27 Apr 1503. Spanish, clear and cipher mixed, four pages | g/l/m/n/p/r/v/z |

f. 121v carries the superscription "Alto y muy poderoso prinçipe Rey y Señor", the wax seal, and a later Spanish
endorsement written sideways in the left margin: **"Del virrey de Siçilia en çifra"**. There is no decipherment
anywhere in the volume for either letter.

## What they are

Both are written the way the secretariat's ciphers are written: single invented symbols for letters, with homophones,
interleaved with groups of two to four Latin letters that are nomenclator entries. In no. 93 the groups read
`gto pie roe hug heg mat gnd gab zoe mae cpm lnq hoe hac zup qup gre zen gne` …; in no. 94 `gag rah mnb mms nob gik
luy mei nen mok pol pat par paq vaz mal nyb nyl gob gib lob moe nak rag lue` …. The standalone symbols are
`+ ÷ ʒ ff ıı :/ ⧻ 7`.

The initial range of the code groups is the discriminator. Three keys of this office are in print or reconstructed:

* **Escrivà no. 1** (the key of no. 5, `federico1497`): initials p-, q-, r-, s-, t-, v-, x-.
* **Cifra general de los RRCC** (the key of no. 92, `esp318`): initials v-, x-, y-, z-, b-, c-.
* **Gran cifra of the Gran Capitán, 1501–1504** — Bergenroth's reconstruction, BNE MSS 20.211/52, re-found by the
  CNI in 2018: initials h-, l-, m-, p-, q-, r-, s-, u-/v-.

Nos. 93 and 94 fall outside the first two and inside the third. One concrete hook: Bergenroth reads **LUQ = capitán**,
and no. 93 has the group `lnq` — *u* and *n* being the same two minims in this hand. Bergenroth also has `muy` = de,
and `muy` occurs in no. 93. That is a lead, not a demonstration: both Bergenroth's list and the CNI's are partial
(Bergenroth's own sheet counts 89 unidentified symbols), and most groups in nos. 93–94 are in neither. Testing it
needs a full transcription of one of the two. A second candidate, untested because unpublished: Galende Díaz's file
BRAH 9/15 opens with **"Cifra del visorrey" (ff. 1–6)**, which he describes but does not reproduce. No. 94 is a
viceroy's letter.

The segmentation run over f. 118r (910 glyphs on 33 lines) makes the architecture measurable. The clean clusters
split into two kinds. Single signs with letter-like frequencies: the p-with-loop sign in three drawings (81 tokens,
9 % — a vowel), the `oo` ligature (24), the heavy double bar (22), the `ʒ`/h-like sign (21), the `re` ligature (15),
`ꝺ` (14), the triple stroke (13), and `+ ÷ :/`. And letter groups that recur as units: `gto` alone occurs 15 times on
the page, `zoc`, `zen`, `hac`, `mae`, `maq`, `muy`, `zup`, `gne`, `mat`, `zel` several times each.

## The attempt that failed

If the letter groups were not code units but runs of letter-shaped signs (as the *Cifra general*'s alphabet is), a
plain homophonic solver on the character stream would break the leaf. Lines 1–21 of f. 118r were transcribed sign by
sign (`ct93_eye.txt`, 1,016 tokens, 40 distinct signs; `python docs/_check_profile.py --measure
targets/esp318no93/ct93_eye.txt`) and annealed against the Spanish 5-gram model from eight starts (`solve93.py`): the
best key scores −3.5 nats a token where real Spanish scores −1.8, and the output is vowel soup. The token statistics
say why: 66 % of all `p` signs occur inside `pie`, 28 % of `g` inside `gto`, and the top trigrams (`gto` ×21, `pie`
×19, `gnꝺ` ×15, `heg` ×13) are far too concentrated for letter runs. The groups are atomic. No. 93 is a nomenclator
problem and needs the key.

## Why it stops here

The *Gran cifra* survives only as Bergenroth's nineteenth-century reconstruction in BNE MSS 20.211/52; the Biblioteca
Nacional returns a bot-check page on its viewer, search and image endpoints; the manuscript is absent from Europeana
and Hispana; Bergenroth's Simancas transcripts on the Internet Archive are handwritten and their OCR yields almost
nothing. Quirantes's two photographs are one the first-campaign alphabet of 1494–98 and the other a partial list of the
second. BRAH 9/15 is not digitised.

The dates, for whoever continues: no. 94 is Messina, 27 April 1503 — the day before Cerignola — and no. 93 is Venice,
24 February 1504, in the weeks after the Garigliano.

## Remaining gaps

- No. 93 (f. 118r-v), whole letter - blocker: no-key-material; CVC nomenclator with atomic groups; the suspected Gran cifra key survives only as Bergenroth's partial list (BNE MSS 20.211/52), not online
- No. 94 (ff. 120r-121v), whole letter - blocker: not-attempted; never transcribed; Bergenroth's Gran-cifra list not tested against it

## Escalation

- [x] siblings: all thirteen cipher folios of the volume opened; no decipherment of nos. 93-94 anywhere in it
- [x] clear-pages: none for no. 93; the clear islands of no. 94 give context but no crib has been placed
- [x] known-keys: Escrivà no. 1 and the Cifra general excluded by code-initial range; Bergenroth's Gran-cifra list and the 'Cifra del visorrey' not obtained or not tested
- [x] print: Parisi 2004 and 2020, Galende Díaz 1994, Tomokiyo's Spanish-cipher and Lasry pages, Quirantes 2018
- [ ] key-rebuild: not done — a solver that treats the CVC groups as unknown words while annealing the sign alphabet against Spanish was not built
- [ ] retry: not done — no. 94 to be transcribed first

## Next step, in order

1. Transcribe no. 94, ff. 120r–121v. It keeps dropping into clear (*"para poder passar esta nao la galea de allá …
   donde llegó don Fernando de Andrada y Benavides y Carvajal y bolvióse de los aquí …"*, *"commo esto passamos en
   anocheçiendo"*, *"En lo de la hazienda luego …"*), so every ciphered stretch has context on both sides.
2. Test Bergenroth's Gran-cifra list against that transcription before attempting a cold break.

## Assumptions for George's review

- Nos. 93 and 94 are one entry only as "attempted, open, key relationship not established"; the earlier "four keys"
  count for the volume is not a verified count, and no shared key is claimed for these two.
