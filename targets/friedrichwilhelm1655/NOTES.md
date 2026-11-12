# friedrichwilhelm1655: Elector Frederick William and Count Georg Friedrich of Waldeck, August-September 1655 (catalogue 2539)

Shelfmark: Gelders Archief (Arnhem), 0370 Heren en graven van Culemborg, inv. nr. 1257, "Register der acten, uitgegaan
van graaf Georg Friedrich, 1654, 1655". Viewer: https://proxy.archieven.nl/0/F424EF561CD74CA49720EAB1BD4F71C7 (856 scans).
Images: screenshots of the archieven.nl viewer in headless Chromium at device scale 2 (`scripts/anl_view.py`, a Python port
of `research/sweep_2026-11-11_dutch_2/anl_view2.js`), about 2490 x 3400 px a scan. Scans are not in git.

Contributed by WAINUT (https://github.com/WAINUTAI; PRs #470 and #471, 12 Nov 2026). The two PRs came as two folders
(`friedrichwilhelm1655`, the Elector's letters, and `waldeck1655`, Waldeck's letters to the Elector). Both use one key, so
at integration (12 Nov 2026) they were folded into this folder: one key, one entry.

## Documents

| doc | scans | what | state |
|---|---|---|---|
| c793 | 793-795 | signed letter, Cöslin 4 Sept 1655, Elector to Waldeck: 5 clear lines, then the body in cipher with clear words | read in part |
| ps797 | 797-798 | P.S. to it, clear and cipher alternating, signed, "Ut in lit: Cößlin 4 Sept" | read in part |
| ps717 | 717 (+715) | "Postscriptum" wholly in cipher, signed; the slip on scan 715 is its foot (same last three lines, same blot) | read |
| l819 | 819 | letter of September 1655: clear lines on Radziwill, then about 12 cipher lines, underlined, with a summary decipherment of the time in the left margin | read |
| w787 | 787-789 | Waldeck to the Elector, 7 Sept 1655: six cipher passages (42 groups) inside clear text | read in part |
| w813 | 813-814 | Waldeck to the Elector, Königsberg, 14 Sept 1655: three short runs and one block of 12 lines (57 groups) | read in part |

Scans 723-724 (letter of 17 Aug 1655) are in a different code (numbers up to four digits mixed with letters) and are not
treated. Of Waldeck's letters only the cipher passages and the clear words beside them are edited; the clear text between
them is not transcribed.

## System

A simple substitution of single letters by numbers, dot-separated, with clear words between the runs:
a 5, b 10, c 12, d 11, e 4, f 13, g 14, h 17, i 2, k 15, l 16, m 6, n 7, o 1, p 22, r 8, s 9, t 23, u/v 3, w 33 (also
written 3.3, "vv"), x 18, y 19, z 20 (`key.tsv`). A diaeresis over 3 or 1 gives ü or ö; a bar over a number doubles it.
No nulls or homophones. The Elector's pieces have no code words. Waldeck's w813 has one number that is not a letter,
51 (813.a and 814.12): from context a person, perhaps the Elector ("damit [51] an hand zu gehen", "ungeneigt [51]
beizustehen"). It is left as [51]; it is the one open code. The writer of the Elector's pieces slips now and then (11 for
10 in "bald", 15 for 16 in "also", 19 for 14 in "gestatten", 12 for 11 in "landtag", 12 for 11 in "würde"); each is marked.

## One target or two?

One. Waldeck's letters use the Elector's key unchanged (`key_frozen.tsv`: every number in w787 is in it; in w813 all but 18
and 51), they sit in the same volume (Waldeck's register of acts) and the same catalogue item, and the correspondence runs
in both directions. README Conventions and the writeup skill present results by key. The PR for Waldeck's letters called
its method "read with known key" because it applied the key recovered in the other folder; that is the same achievement,
so the method of the whole target is the one that found the key.

## How the key was found (no key filed, no decipherment used)

Ciphertext and the clear words of the same letter. During pass 1 of scan 795 the run after "den von", 15.8.1.12.15.1.3.3,
fits "Krockow" (a Krockow carries an instruction dated Cöslin 4/14 Sept 1655 in Urkunden und Actenstücke VII); with
e = 4 (the commonest number) and -en = 4.7, the common words (das, unsern, Völkern, durch, Stadt, Pferde) gave the rest
at once. The key was frozen from c793 alone (`key_frozen.tsv`); 18 = x was added later from Waldeck's "Weixel". The
clear words around the runs and the outside name are plaintext next to the cipher, so the method is key recovered based
on adjacent plaintext (`docs/_methods.py`), not ciphertext-only.

Candour on method: the key became evident during pass 1 of scans 795 and 793. Pass 1 of the other scans and all of
pass 2 were made with the key known, so the passes are not blind to the plaintext. Pass 2 used fresh half-width crops and
changed 12 lines (listed by `scripts/build_transcriptions.py`, which ran once in the working layout on the raw pass-1
notes kept in `work/raw_pass1/`). The independent review of 12 Nov 2026 (below) copied 15 cipher lines blind from the
scans and agrees number for number; the other lines still have no blind second reader.

## Held-out test (`scripts/heldout.py`, `heldout.txt`)

What is held out is the frozen key (22 values from c793), not the clear words or the name Krockow that gave it.

1. Scan 819 carries, in the left margin and in another hand of the time, a summary decipherment of its cipher
   (`gloss_819_margin.txt`, our reading of that note). The frozen key's mechanical decryption of the 40 cipher groups
   matches **196 of the note's 209 letters in order (0.938)** and 30 of its 37 words letter for letter. The misses are the
   note's own wording ("dero" where the cipher has "unsere", "dahin" for "dazu", "Rath" for "raht", "Bischoff"), the
   writer's two slips (lanctag, würce) and one clear "und".
2. Scan 797 has two interlinear glosses of the time: 9.1. 11.5.16.11 gives "so dald" (gloss "so bald", letter ratio
   0.83); 20.3.7.4.11.8.1 gives "zunedro" (gloss "zu dero", 0.77; the writer enciphered "ned" for "de").
3. In ps797, ps717, l819 and w787 every number is in the frozen key; in w813 every number is except 18 and 51.

How much this shows: little beyond the reading itself. The note is a summary of one cipher passage that follows the
cipher closely, and a 22-value substitution that reads as German on about 2,470 numbers needs no score to be credible.
The order of events (key frozen before the note and the glosses were looked at) rests on the contributor's record: one
commit per pull request, no external timestamp. The catalogue entry of 11 Nov 2026 already said that scan 819 "may be a
contemporary decipherment (not read)", so the note was known to exist before the work began.

## Statistical validation (`validation.tsv`, `scripts/validation_pairs.py`, integration step)

`docs/_validate.py` with `de-1640s`: 2,474 read tokens, 26 types, reading -2.245 per letter; random keys -6.617 (z 8.5);
a key annealed onto the shuffled ciphertext at best -4.169 (z 61.3); verdict pass.

## Reading (scripts/check_marks.py passes; counts by scripts/reading.py)

Word counts include the clear words copied from the page (c793 about 104 clear words beside 179 cipher groups; ps797
75 beside 84; ps717 2 beside 70; l819 20 beside 40 in the edited lines; w787 about 63; w813 about 12).

| doc | words | verbatim | marked repair | context fill / guess | with a hole | holes | Dan's checker clean share |
|---|---|---|---|---|---|---|---|
| c793 | 286 | 260 (90.9%) | 4 | 21 | 1 | 4 | 0.70 (264 words) |
| ps797 | 161 | 151 (93.8%) | 3 | 6 | 1 | 4 | 0.765 (160 words) |
| ps717 | 71 | 68 (95.8%) | 3 | 0 | 0 | 0 | 0.714 (68 words) |
| l819 | 64 | 62 (96.9%) | 2 | 0 | 0 | 0 | 1.00 (55 words) |
| w787 | 106 | 99 (93.4%) | 1 | 6 | 0 | 4 | 0.889 |
| w813 | 72 | 64 (88.9%) | 5 | 3 | 0 | 2 ([51]) | 0.833 |
| all six | 760 | 704 (92.6%) | 18 | 36 | 2 | 14 | |

The strict read share used for the headline is the "verbatim" column: a repair, a context fill, a guess or a hole is not
read (README read bar). The contributor counted the same way (the "verbatim" column is theirs). Counting the 18 marked repairs as read would give
722 of 760 (95.0%); that looser rule is not used. Counted on cipher words only (clear words out of the denominator) the shares are
lower (c793 about 87%, w787 about 84%). Words from a gloss only: 0. The context fills in c793 and ps797 are letters lost
in the binding of scans 794 and 798 (left-hand pages), and in w787 of scan 788.

Where the clean share comes from: the column above is `docs/_check_reading.py --file` run on the sentence text of each
reading, which is shipped as `work/text_<doc>.txt` (built with the reading by `scripts/make_reading.py` from
`work/marked/<doc>.txt`). Run in folder mode (`python docs/_check_reading.py friedrichwilhelm1655`), the checker scores
the reading files lower, because each `reading_<doc>.md` holds the sentence text and then the marked line-by-line block,
where every mark counts as a hole. The decryption files are unspaced decodes and score near 0.

`{[...]/abc}` in a marked line is a fill of letters lost in the binding; `{[...]/}` a line end in the binding where nothing
is lost; `[...]` is a hole. `scripts/reading.py` (run by `check_marks.py`) also fails when a `[...]` or `[nn]` of the
decryption is dropped from a reading line without a mark.

Content in short: from Cöslin the Elector tells Waldeck that the army will be on the Vistula within ten days and that
the ships must be ready in the Königsberg Haff. He gives the daily need of bread and beer and forage for 6,000 horses,
names Gerhard Roggen at Danzig and Christoph Melchior to help, and says that Danzig refuses passage and that he sends
von Krockow to treat with the city and the voivodes. The P.S. orders patrols of fifty and of five or six horsemen and an
entrenchment for 500 foot on this side of the Vistula. The August postscript: keep treaties with the local people,
"especially the Weihers", non-binding; deal with Ermland; Elbing subject to ratification; tell the Oberräte with caution.
Scan 819: Radziwill says they see no course but to put themselves under the Elector's protection; a general Prussian
diet should be called by the Bishop of Ermland. Waldeck, 7 Sept: the conditions with Sweden could hardly be worse; he has
written to Jacob Weiher, to Elbing and to Danzig and will speak to the Bishop of Ermland; Danzig offers ships; provisions
(vivres) against cartage money or security; news to General Sparr. 14 Sept: Weiher offers help; Vistula boats ordered at
Marienwerder; Magnus reports from Thorn that the town resolves to defend itself, plans a meeting with Danzig, Elbing and
the three voivodes on the Vistula, and is not unwilling to help [51].

## Prior art (checked 11-12 Nov 2026)

- One web search (12 Nov 2026; German terms: Kurfürst, Waldeck, Cöslin, September 1655, Woywoden, Krockow, Danzig,
  Weichsel): no edition, quotation or decipherment of these letters found.
- Catalogue vetting of 11 Nov 2026: Urkunden und Actenstücke VII does not print the Cöslin letter; DECODE and cryptiana
  have nothing on Waldeck or Culemborg.
- Erdmannsdörffer, Graf Georg Friedrich von Waldeck (1869), which the catalogue's verify field names: not opened by the
  contributor. At integration (12 Nov 2026) the two online copies on archive.org (`grafgeorgfriedri00erdmuoft` and the
  BSB scan `bub_gb_-E06AAAAcAAJ`) were fetched as text and searched with patterns that allow the long-s OCR errors for
  Krockow, Cöslin, Radziwill, Danzig, Marienwerder, Culemborg and Chiffre/Ziffer: no hit (Weichsel 6 times, Elbing and
  Thorn once). The OCR is too poor to exclude a quotation or a summary of these letters (it also finds no Radziwill and
  no Danzig); the book draws on Prussian archives and the Arolsen archive. This remains the main open prior-art point.
  The margin note on scan 819 shows that at least that letter was deciphered on the recipient's side in 1655.

## Independent review (12 Nov 2026, contributor's side)

An AI language-model agent that took no part in the solve reviewed both folders. Before opening any transcription it
cropped 15 cipher lines from the scans at full resolution and copied the numbers (793.05, 793.08, 793.11, 819.09, 819.12,
717.08, 717.12, 797.13, 797.18, and six lines of Waldeck's letters: 813.a, 813.b, 787.a, 787.b, 814.05, 814.07; about 190
numbers). All agree with the reconciled transcriptions number for number; two shape doubts (797.13 third sign 4 or 9;
819.09 last group 33 or 3.3, the same letter) were settled as the solver had settled them. It reproduced the mark check,
`heldout.txt` and the solver's clean shares, and found that `key_frozen.tsv` and `key.tsv` differ only at 18 = x. Grades
(reading_review in `profile.json`): ps717 A, l819 A, c793 B, ps797 B, w787 B, w813 B. It found that the hole at the end of
794.09 had moved in the reading, and that 814.05, 814.07, 814.08 and 814.10 dropped the binding hole without a mark; all
are marked now.

## Integration check (12 Nov 2026)

By a second AI language-model reader that is not the contributor, and with no human palaeographer.

- Re-run: `heldout.py`, `check_marks.py` (both groups of documents), the decryptions; an own decoder written from
  `key.tsv` agrees with ps717 and l819 letter for letter; German language model `de-1640s` per letter: real key -4.20,
  200 shuffled keys mean -9.23 (max -7.70).
- Images: scans 819, 717, 795 and 813 were fetched from the viewer by the research sweep's script (no bot check). Compared
  by eye: l819 lines 4-15 (40 groups, 206 numbers), ps717 lines 8-14 (29 groups, 142 numbers), c793 795.06-795.14 (33 groups,
  167 numbers), w813 813.a-c (9 groups, 43 numbers): 111 groups, 558 numbers in all. **Two errors found and corrected:** (1) 819.11, last group, is 16.5.7.12 (c), not 16.5.7.13 (f): the slip is
  "lanctag" (12 for 11), not "lanftag"; both pass files carried the same error, they are left as the record. (2) The clear
  word at 795.06 is "auß", not "auch" ("durch vorspan auß Pommern"; the translation now says "from Pomerania"). The
  held-out score is unchanged (196 of 209). Not compared: the rest of c793, ps797, w787, scan 814.
- Class: recomputed over the six documents with the strict rule: 704 of 760 words verbatim (92.6%), read in part. ps717
  and l819 reach 95% as documents.
- Method: key recovered based on adjacent plaintext (see above).
- Statistical validation added (`validation.tsv`).

## Remaining gaps

- Line ends of scans 794 and 798 - blocker: needs-physical-access; letters lost in the binding of the left-hand pages
  (21 context fills in c793, 6 in ps797; 798.06-798.08 have three holes, so the last two sentences of ps797 are thin).
  Only a new photograph of the opened volume could give them.
- 788.20-788.24 and the line ends of scan 788 - blocker: needs-physical-access; four holes, letters lost in the binding.
- The clear word before "etwa" on 797.20 - blocker: illegible; not read from the viewer image.
- 787.a "S{i/c}hweden" - blocker: illegible; 2 or 12 not settled on the image.
- Number 51 (813.a, 814.12) - blocker: open-codes; not a letter, from context a person, perhaps the Elector (a guess).
- Scans 723-724 (17 Aug 1655, another code) - blocker: no-key-material; numbers up to four digits mixed with letters, no
  key of that code is known; the catalogue item stays open for it.
- "Nebro" (793.11), the meeting place on the Vistula - blocker: too-short; one name with no context to identify it, read
  from the signs.
- "Magnus" (814.01) - blocker: too-short; one name in Waldeck's letter, not identified.
- Erdmannsdörffer 1869 - blocker: illegible; the only online copies are Fraktur OCR with long-s errors (see Prior art);
  a quotation of these letters cannot be excluded or found from them.

Scope, not gaps: the clear text of Waldeck's two letters, scan 819 lines 1-3 and the clear opening lines of 793 are not
cipher and were not transcribed in full; the read share counts the cipher passages and the clear words copied beside
them. The cipher was not read blind by a second reader outside the contributor's reviewer (15 lines) and the integration
check (111 groups); pass 2 was made with the key known.

## Escalation

- [x] siblings: all 856 scans of the volume are listed in the catalogue sweep; the cipher scans it names (715-819) were
  opened; Waldeck's own cipher passages are read here (w787, w813). Scans 723-724 are another code, not treated.
- [x] clear-pages: the margin note on scan 819 and the two glosses on scan 797 were found to be decipherments of the
  time and are used as the held-out check; Waldeck's register copies carry marginal summaries of the clear text only.
- [n/a] known-keys: no Brandenburg or Waldeck key of 1655 is known (catalogue vetting: known.py and DECODE, nothing);
  the key was recovered in full here.
- [x] print: Urkunden und Actenstücke VII opened (catalogue vetting); Erdmannsdörffer 1869 searched at integration in two
  online Fraktur OCR copies (see Prior art): no hit, but the OCR is too poor to exclude a quotation.
- [x] key-rebuild: the key is complete for letters (22 values and 18 = x); 51, a probable code word occurring twice, has
  no value and no context settles it.
- [x] retry: all documents decrypted with the final `key.tsv`; the remaining holes are binding losses and [51].
