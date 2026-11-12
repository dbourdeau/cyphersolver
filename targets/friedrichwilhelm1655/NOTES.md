# friedrichwilhelm1655: Elector Frederick William to Count Georg Friedrich of Waldeck, August-September 1655 (catalogue 2539)

Shelfmark: Gelders Archief (Arnhem), 0370 Heren en graven van Culemborg, inv. nr. 1257, "Register der acten, uitgegaan
van graaf Georg Friedrich, 1654, 1655". Viewer: https://proxy.archieven.nl/0/F424EF561CD74CA49720EAB1BD4F71C7 (856 scans).
Images: screenshots of the archieven.nl viewer in headless Chromium at device scale 2 (`scripts/anl_view.py`, a Python port
of `research/sweep_2026-11-11_dutch_2/anl_view2.js`), about 2490 x 3400 px a scan. Scans are not in git.

## Documents

| doc | scans | what | state proposed |
|---|---|---|---|
| c793 | 793-795 | signed letter, Cöslin 4 Sept 1655: 5 clear lines, then the body in cipher with clear words | read in part |
| ps797 | 797-798 | P.S. to it, clear and cipher alternating, signed, "Ut in lit: Cößlin 4 Sept" | read in part |
| ps717 | 717 (+715) | "Postscriptum" wholly in cipher, signed; the slip on scan 715 is its foot (same last three lines, same blot) | read |
| l819 | 819 | letter of September 1655: clear lines on Radziwill, then about 12 cipher lines, underlined, with a summary decipherment of the time in the left margin | read |

Scans 723-724 (letter of 17 Aug 1655) are in a different code (numbers up to four digits mixed with letters) and are not
treated. Waldeck's own letters in the same system are in `../waldeck1655/`.

## System

A simple substitution of single letters by numbers, dot-separated, with clear words between the runs:
a 5, b 10, c 12, d 11, e 4, f 13, g 14, h 17, i 2, k 15, l 16, m 6, n 7, o 1, p 22, r 8, s 9, t 23, u/v 3, w 33 (also
written 3.3, "vv"), x 18, y 19, z 20 (`key.tsv`). A diaeresis over 3 or 1 gives ü or ö; a bar over a number doubles it.
No nulls, homophones or code words were found in the Elector's pieces. The writer slips now and then (11 for 10 in
"bald", 15 for 16 in "also", 19 for 14 in "gestatten", 13 for 11 in "landtag", 12 for 11 in "würde"); each is marked.

## How the key was found (no key filed, no decipherment used)

Ciphertext only, with the clear words as context. During pass 1 of scan 795 the run after "den von", 15.8.1.12.15.1.3.3,
fits "Krockow" (a Krockow carries an instruction dated Cöslin 4/14 Sept 1655 in Urkunden und Actenstücke VII); with
e = 4 (the commonest number) and -en = 4.7, the common words (das, unsern, Völkern, durch, Stadt, Pferde) gave the rest
at once. The key was frozen from c793 alone (`key_frozen.tsv`); 18 = x was added later from Waldeck's "Weixel".

Candour on method: the key became evident during pass 1 of scans 795 and 793. Pass 1 of the other scans and all of
pass 2 were made with the key known, so the passes are not blind to the plaintext. Pass 2 used fresh half-width crops and
changed 12 lines (listed by `scripts/build_transcriptions.py`, which ran once in the working layout on the raw pass-1
notes kept in `work/raw_pass1/`). The independent review of 12 Nov 2026 (below) copied 15 cipher lines blind from the
scans and agrees number for number; the other lines still have no blind second reader.

## Held-out test (`scripts/heldout.py`, `heldout.txt`)

1. Scan 819 carries, in the left margin and in another hand of the time, a summary decipherment of its cipher
   (`gloss_819_margin.txt`, our reading of that note). The frozen key's mechanical decryption of the 40 cipher groups
   matches **196 of the note's 209 letters in order (0.938)** and 30 of its 37 words letter for letter. The misses are
   the note's own wording ("dero" where the cipher has "unsere", "dahin" for "dazu", "Rath" for "raht", "Bischoff"), the
   writer's two slips (lanftag, würce) and one clear "und".
2. Scan 797 has two interlinear glosses of the time: 9.1. 11.5.16.11 gives "so dald" (gloss "so bald", letter ratio
   0.83); 20.3.7.4.11.8.1 gives "zunedro" (gloss "zu dero", 0.77; the writer enciphered "ned" for "de").
3. In ps797, ps717, l819 and Waldeck's two letters every number is in the frozen key except 18 and 51.

## Reading (scripts/check_marks.py passes; counts by scripts/reading.py)

Word counts include the clear words copied from the page (c793 about 104 clear words beside 179 cipher groups; ps797
75 beside 84; ps717 2 beside 70; l819 20 beside 40 in the edited lines).

| doc | words | verbatim | marked repair | context fill / guess | with a hole | holes | Dan's checker clean share |
|---|---|---|---|---|---|---|---|
| c793 | 286 | 260 (90.9%) | 4 | 21 | 1 | 4 | 0.70 (264 words) |
| ps797 | 161 | 151 (93.8%) | 3 | 6 | 1 | 4 | 0.765 (160 words) |
| ps717 | 71 | 68 (95.8%) | 3 | 0 | 0 | 0 | 0.714 (68 words) |
| l819 | 64 | 62 (96.9%) | 2 | 0 | 0 | 0 | 1.00 (55 words) |

Words from a gloss only: 0. The context fills in c793 and ps797 are letters lost in the binding of scans 794 and 798
(left-hand pages). The checker's holes are mostly these and period spellings its word list lacks.

Where the clean share comes from: the column above is `docs/_check_reading.py --file` run on the sentence text of each
reading, which is shipped as `work/text_<doc>.txt` (built with the reading by `scripts/make_reading.py` from
`work/marked/<doc>.txt`). Run in folder mode on the shipped files (`python docs/_check_reading.py friedrichwilhelm1655`),
the checker scores the reading files lower: c793 0.443, ps797 0.50, ps717 0.448, l819 0.615. Each `reading_<doc>.md`
holds the sentence text and then the marked line-by-line block, where every mark counts as a hole; the merged
griffoli1555 shows the same pattern. The decryption files are unspaced decodes and score near 0.

`{[...]/abc}` in a marked line is a fill of letters lost in the binding; `[...]` is a hole. `scripts/reading.py` (run by
`check_marks.py`) also fails when a `[...]` or `[nn]` of the decryption is dropped from a reading line without a mark.

Content in short: from Cöslin the Elector tells Waldeck that the army will be on the Vistula within ten days and that
the ships must be ready in the Königsberg Haff. He gives the daily need of bread and beer and forage for 6,000 horses,
names Gerhard Roggen at Danzig and Christoph Melchior to help, and says that Danzig refuses passage and that he sends
von Krockow to treat with the city and the voivodes. The P.S. orders patrols of fifty and of five or six horsemen and an
entrenchment for 500 foot on this side of the Vistula. The August postscript: keep treaties with the local people,
"especially the Weihers", non-binding; deal with Ermland; Elbing subject to ratification; tell the Oberräte with caution.
Scan 819: Radziwill says they see no course but to put themselves under the Elector's protection; a general Prussian
diet should be called by the Bishop of Ermland.

## Prior art (checked 11-12 Nov 2026)

- One web search (12 Nov 2026; German terms: Kurfürst, Waldeck, Cöslin, September 1655, Woywoden, Krockow, Danzig,
  Weichsel): no edition, quotation or decipherment of these letters found.
- Catalogue vetting of 11 Nov 2026: Urkunden und Actenstücke VII does not print the Cöslin letter; DECODE and cryptiana
  have nothing on Waldeck or Culemborg.
- Not checked: Erdmannsdörffer, Graf Georg Friedrich von Waldeck (1869), which the catalogue's verify field names. Its
  online OCR is not usable, and a second web search by the reviewer (12 Nov 2026) found no full text or quotation. A
  review of the book says it draws on Prussian archives and especially the Arolsen archive, so it may quote or summarize
  these letters or the Waldeck side of the correspondence. This is the main open prior-art point. The margin note on
  scan 819 shows that at least that letter was deciphered on the recipient's side in 1655.

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve reviewed both folders (this one and `../waldeck1655/`).
Before opening any transcription it cropped 15 cipher lines from the scans at full resolution and copied the numbers
(793.05, 793.08, 793.11, 819.09, 819.12, 717.08, 717.12, 797.13, 797.18, and six lines of Waldeck's letters; about 190
numbers). All 15 agree with the reconciled transcriptions number for number; two shape doubts (797.13 third sign 4 or
9; 819.09 last group 33 or 3.3, the same letter) were settled as the solver had settled them. It reproduced the mark
check, `heldout.txt` and the solver's clean shares, and found that `key_frozen.tsv` and `key.tsv` differ only at 18 = x.
Grades (reading_review in `profile.json`): ps717 A, l819 A, c793 B, ps797 B. No state changed.

Fixes made after the review: the hole at the end of 794.09 had moved to the start of 794.10 in the reading
(`{[...]/ü}ber`); it is now marked on its own line (`dr{[...]/ü}-` / `ber`), with no change to any count. The reading
checker was hardened as described above. The sentence texts are shipped in `work/`, and the folder-mode scores are given.

## Remaining gaps

- Line ends of scans 794 and 798 - blocker: needs-physical-access; letters lost in the binding of the left-hand pages
  (21 context fills in c793, 6 in ps797; 798.06-798.08 have three holes, so the last two sentences of ps797 are thin).
  Only a new photograph of the opened volume could give them.
- The clear word before "etwa" on 797.20 - blocker: illegible; not read from the viewer image.
- "Nebro" (793.11), the meeting place on the Vistula - blocker: not-attempted; read from the signs, not identified.
- Clear words "durch vorspan auch Pommern" (795.06) - blocker: not-attempted; the reviewer suggests "auch" may be "aus"
  (or "durch"); it is clear text and should be checked on the scan.
- Scan 819 lines 1-3 and the clear opening lines of 793 - blocker: not-attempted; not transcribed in full.
- Blind second reading of the cipher - blocker: not-attempted; pass 2 was made with the key known. The reviewer's
  15-line blind spot-check agrees fully, which reduces the concern but does not remove it.
- Erdmannsdörffer 1869 - blocker: not-attempted; not opened (see Prior art).

## Escalation

- [x] siblings: all 856 scans of the volume are listed in the catalogue sweep; the cipher scans it names (715-819) were
  opened; Waldeck's own cipher passages are read in `../waldeck1655/`. Scans 723-724 are another code, not treated.
- [x] clear-pages: the margin note on scan 819 and the two glosses on scan 797 were found to be decipherments of the
  time and are used as the held-out test.
- [n/a] known-keys: no Brandenburg or Waldeck key of 1655 is known (catalogue vetting: known.py and DECODE, nothing);
  the key was recovered in full from the ciphertext.
- [ ] print: Urkunden und Actenstücke VII opened (catalogue vetting); Erdmannsdörffer 1869 not opened.
- [n/a] key-rebuild: the key is complete; every number in the four letters is a letter of the frozen key.
- [x] retry: all documents decrypted with the final `key.tsv`; the remaining holes are binding losses.
