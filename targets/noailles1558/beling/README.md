# Noailles 1558: Brackx's transcription checked on the images, a print check, and the f. 60v gaps

Contributed by Andrew Beling, with AI agents, 11 November 2026.
This folder adds to `targets/noailles1558/`. It changes nothing in Daniel Bourdeau's files or in Michael Brackx's
`brackx/`. The edits that go with it are in the same pull request: a dated section and two gap lines in `../NOTES.md`,
and in `../profile.json` three solution steps, the same gap changes and a verification credit. `docs/` is not touched.

[V] = checked on the image or in the source. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `transcription_check.tsv` | every one of Brackx's 272 sign tokens (`brackx/transcription_f60r_f60v.txt`) checked on the image: agree / unclear / possible extra sign, with notes |
| `charriere_check.md` | the search of Charrière, *Négociations de la France dans le Levant* II, for this letter |
| `CHECKS.txt` | checker output |

No images are included. The regions are Gallica btv1b9059865k views 61 and 62 (IIIF), at native resolution.

## 2. Brackx's transcription holds on the images [V]

Each sign was located with his `positions_*.txt` and judged on shape alone against his `legend.md`, without reference
to the key. One reader.

- **270 agree, 2 unclear, 0 differ.** Unclear: B2 #11 `s5` (pale, more like a small 5 than an s); C4 #3 `w` (a v-like
  stroke with a curl, not the usual double loop).
- **Two possible extra signs**, both pale and possibly show-through: a cross over a blot in C4 between `Zo` and `w`, and a
  hook in A3 between `zB` and `O`.
- No decoded letter changes under key r5.
- On the open signs: `al 5` at the end of C2 is clear, so the stray "u l" there is in the cipher. `ag` (C2) is written in
  ordinary cursive letters, underlined, not in a cipher shape: perhaps a correction in clear ("ay"), as his notes allow.
  `Ob` (C2) is a dark oval inside a stain and may be a blot. `+o` (C4) is close in shape to `4o` (o) in C6.

## 3. No printed text (Charrière II) [V on the OCR]

Charrière prints Noailles's Venice letters of 7 and 15 Nov 1558 but not this letter of 13 Nov; none of the block C gloss
phrases occurs in his November letters. So there is still no outside plaintext to test key r5. One correction to
`../NOTES.md`: the parallel cited as "II 505, letter of 7 Nov 1558" is on p. 505 but belongs to the letter headed
"Venise, 7 et 20 octobre 1558", where it is said of the emperor Ferdinand I ("se faict fort vieulx et donne encore mauvais
ordre à ses affaires"). Block A is probably about him too [I]. Details in `charriere_check.md`.

## 4. Why there is no held-out test

Key r5 was built from all three glosses (A and B inner margin, C outer margin), so no glossed text is left to hold out.
A shuffled-key score against the same gloss would measure fit, not prediction, so none was run.

## 5. The f. 60v gaps (C2, C4, C5): all tentative, one context each

Outer-margin gloss, re-read at native resolution [V reading, low to medium confidence]:
line 4 **"ilz ont d'autruy les"** (NOTES: "d? commun…"; the minims after "autr" could also be "autru y u les");
line 6 **"[vi]ennent p[ou]r a hazard"**; line 8 **"[?2 letters] ravitailles qu'ilz"** (NOTES: "ravitaillez").

| sign | candidate | basis |
|---|---|---|
| `+o` (C4) | z | C4 "e r o **+o** a r d" against "hazard" |
| `Ob` (C2) | r | C2 "d a t **Ob** u ag" against "d'autruy"; may be a blot |
| `ag` (C2) | y, written in clear | see section 2 |
| `lp` (C5) | "ost" | C5 "o n t **lp** e a u x" against "ont osté aux" |

None conflicts with a firm value of key r5. What they do not fix: C2 still ends in "u l"; C4's "e r o" does not give
"pour a ha-"; C5's "t h ?" does not give "ravi-". A sharper image of the f. 60v outer margin, which only the BnF can
supply, is what would settle gloss lines 4-8. The gain is two or three values; the letter stays read in part.
