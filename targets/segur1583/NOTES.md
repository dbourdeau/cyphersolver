# A correspondent at Beaupréau to Ségur, July 1583 (BnF 500 de Colbert 401 f. 143): a third key of the Navarre design

Transcribed on 16 Sept 2026 in `targets/segur/`. Gallica ark:/12148/btv1b10035574w, f. 143 = canvas 154.

**Split on 14 Oct 2026 from `segur`** under the one-key rule (George Lasry): f. 143 is in a different key from the
three Navarre letters of 1585-86 (key A, `segur`) and from Tomokiyo's f. 321 key (`navarre1586`); each is a different
cipher with its own page. `ct_143.txt` moved here. Attempted, not solved.

## The letter

Tomokiyo's cryptiana page lists it among four letters "of Henry III to Segur" in figures. It is not from the king: it is
*to* Ségur from a correspondent at Beaupréau, July 1583, signing "vostre tres humble et tres … serviteur". Its clear text
is about the cipher itself: *"Il me semble qu'il n'est point besoin d'autre alphabet, vous y avez toutes choses tellement
dispersées en lettres, syllabes, doubles, nulles et tout le reste qu'il est impossible de le descouvrir … Les noms sont en
lettres et syllabes."* That is the design found in key A (letters, syllables, doubles, nulls; names written with
letter-signs), here with different values. The clear text also speaks of someone of "grand faute" and of 156, 134 and
136 (name numbers) to be sent.

## The cipher

`ct_143.txt`: 58 numeric tokens, 42 distinct (measured 14 Oct 2026 with `_check_profile.py --measure --digits`), with
letter-written signs Pa, a, H, L, I, and the name numbers 156, 134, 136 in the clear passages. Figures run 2-133 in the
cipher lines. Key A (`targets/segur/key_v4.json`) gives only scattered French-looking fragments, and the f. 321 key nothing (checked 14 Oct 2026). At this length
the structured annealers cannot work: matched controls fail at f. 333's size (~100 tokens) for the free annealer, and the
design-constrained one was tested only down to that size.

George Lasry reports (Oct 2026) that his saved decryptions of 15 Oct 2024 include f. 143. They are unpublished and were
not seen here.

## Remaining gaps
- the whole cipher of f. 143 (58 numeric tokens) - blocker: too-short; below the floor of the annealers for this design, no other letter in this key in the volume (swept), no gloss; Lasry's 2024 decryption is unpublished

## Escalation
- [x] siblings: all 440 canvases of 500 Colbert 401 swept (in segur): no other letter in this key; 500 Colbert 402 not digitised
- [x] clear-pages: none; the clear text describes the system but gives no values
- [x] known-keys: key A (key_v4.json) and Tomokiyo's f. 321 key applied 14 Oct 2026: the f. 321 key gives nothing; key A gives a few French-looking fragments (*…ande efeire…*, *…faisi…*) inside non-French runs (*hfurtsitumailaco*, *vuvvislisexecuvopns*), so if the key is related it is not the same; not pursued further
- [x] print: Tomokiyo's cryptiana pages (listed unsolved, as Henry III)
- [n/a] key-rebuild: 58 tokens is below the tested floor of both annealers, and a design-constrained run would also need the table offsets (letter range, syllabary start), which 58 tokens cannot fix
- [n/a] retry: nothing deciphered to regrade

## Assumptions for George's review
- His prior-solution credit is placed here because his saved decryptions of 15 Oct 2024 cover f. 143; the key is taken to
  differ from ff. 233/239/288v as the NOTES record, not checked against his decryption.
