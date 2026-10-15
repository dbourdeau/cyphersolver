Transcription brief: Vienna -> Schenck letters, 1706 (DECODE R7486-R7500)

Folder: C:/Users/dbour/cypher/.worktrees/sieniawski1708/targets/sieniawski1708/
Images (full resolution, git-ignored): img/IMG_R<rec>_I<id>_P<n>.jpg ; reduced copies in img/small/.
Each record is one letter (2-6 images; the last image of a record is often a two-page spread, and some
images are blank address leaves / backs with only a docket).

The letters: German (Kurrent hand, with French/Latin loanwords), from an agent in Vienna ("Wien 7 marty 1706"
in a later hand at the top of the address leaf), to "Monsieur" (Schenck, chamberlain of Augustus II), signed
"Votre tres humble et tres obeiss. ...". Each letter is numbered at top left ("N. 18", "N. 32") and has a
docket ("Rec. 12 aprilis 1706" etc.).

The cipher, as far as seen: mixed into the clear text are
 - 3-digit code numbers (100-599, e.g. 150, 181, 187, 189, 190, 208, 258, 413, 452) for names/words;
 - runs of 2-digit numbers (about 10-79) written closely together that spell words letter by letter
   (e.g. "34 30 32 43 25 64 61 62 21 59 40 40 19 43"); "19 43" and "19 45" often end a run.
   Digits are often run together with little spacing; split into 2-digit groups only where the hand
   makes it clear, otherwise write the digit string exactly as written and mark it {?split}.
 - isolated small letters with a dot inside cipher runs ("o.", "f.", "g.", "c.", "e", "d.", "b."), and a
   sign like "L" or "£"; transcribe them as they appear, in lower case, keeping the dot.
 - superscript letters/marks written above some cipher numbers (e.g. small "a", "ä", "e", "r", "p", "t", "f",
   "c"), and occasional interlinear clear words above or below code numbers in another ink ("der", "der Kayser")
   which are the recipient's partial decipherment. These are important: record each one, attached to the
   number it stands over, as 64^a or 208^[der Kayser]. Marginal notes: transcribe too, saying where they are.
 - struck-through numbers: write them as ~~187~~.

What to produce: ONE file per letter, transcr/R<rec>.txt, in this format:

  # R7486  N. 18  Wien 7 March 1706   docket: "Rec. 12 aprilis 1706"   images: P1 (text p.1), P2 (address/back), P3 (pp.2-3)
  [P1 l.1] Mit dieser Post habe von 189 der 187 ...
  [P1 l.2] ...
  (every line of the letter, in reading order: clear text in German as best you can read it, with [?] for
  unreadable words, and the cipher exactly in place; keep line numbers per page and per column of a spread
  as [P3a l.5], [P3b l.5])
  ## margin P1 left (vertical): ...

Rules:
 - The cipher numbers matter most. Read every digit at full resolution: crop the full-resolution image with
   PIL (python; e.g. Image.open(f).crop((x0,y0,x1,y1)) then save to img/crop/ and view it) into strips of
   2-4 lines at native resolution (do not downscale below ~1000 px for a half-width strip). Re-check every
   cipher run twice. Where a digit is uncertain write it with a ? after it (e.g. 5?8) and give alternatives
   if you can (5?8|38).
 - Clear text: best effort, but do try; it gives the context needed later. Normalise nothing; keep spelling.
 - Write the file for each letter as soon as that letter is done (append page by page), so nothing is lost
   if you are stopped. Do not write anything else in the repository.
 - At the end, report: per letter, the number of 2-digit cipher numbers, the 3-digit codes seen, any
   interlinear glosses (with the number each stands over), the date and number of the letter, and anything
   that looks like a key or decipherment.
