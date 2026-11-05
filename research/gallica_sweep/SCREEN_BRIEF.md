# Screening brief: Bellièvre volumes (BnF fr. 15906, 15900 (1), 15891), Nov 2026

You are screening contact sheets of a digitised 16th-century French letter-book for **cipher**. Each sheet is a JPEG
grid of canvases (pages, or two-page openings for fr. 15906), each labelled `cNNN` at its top-left. The canvases
are in `<dir>/cNNN.jpg` at 800 px wide.

What counts as cipher (flag it):
- runs of Arabic figures inside running text or in blocks (e.g. `24 17 30 4 12`, `·45·`), not dates, sums or folio numbers;
- strings of invented signs, Greek-like or barred letters, dotted letters, nonsense letter strings that are not words;
- whole letters or paragraphs written in such signs; a clear letter with a few cipher words or names;
- key tables or nomenclators (alphabet rows with signs under them, lists of names with numbers/signs);
- cipher with an interlinear or marginal decipherment (note it: the decipherment matters).

Do NOT flag: dates, folio numbers, money columns and accounts, signatures and paraphs, Latin abbreviations, Italian or
Spanish or German clear text, printed pages.

Method:
1. Read every sheet in your list with the Read tool, in order.
2. For any canvas that might hold cipher, open `<dir>/cNNN.jpg` itself (800 px) and look again. If still unsure, say
   "unsure" rather than dropping it.
3. After each sheet, append one line per flagged canvas to your output file (create it if missing), in this form:
   `cNNN | yes/unsure | what is there (system: figures/signs/letters; how many lines; whole page or a few words) | decipherment on or beside it? (interlinear/marginal/none) | sender/addressee/date if legible`
   and, when a sheet has nothing, the line `sheet sNNN_NNN: none`. Append as you go; do not save it all for the end.
4. Finish with a short summary of the flagged canvases. Do not fetch anything from the web; do not edit any other file.
