# Transcription brief (blind pass) — Mabeyn->Yemen telegrams, system B (Koc HPBK)

You are ONE of two independent transcribers. Do NOT open, list or read anything in the other pass folder
(transcription/passA or transcription/passB, whichever is not yours), HANDOFF.md, or any file other than
the images, this brief and your own output folder. Do not decode, do not guess letters from context or
from a key: record what is WRITTEN. No browser, no network, no rm.

Images (full resolution, Koc University, CC BY-NC-ND, never copy them elsewhere):
/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/mabeyn-yemen-1898/img/HPBK_<id>.jpg
Crop tool (coords in full-res pixels; writes to .../mabeyn-yemen-1898/v/<out>; then view the crop with Read):
  python3 "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/mabeyn-yemen-1898/scripts/crop.py" <id> x0 y0 x1 y1 <out.jpg> [maxdim]
Prefix your crop file names with your pass letter (e.g. A541_r1.jpg) to avoid clashes. Use crops of at most
~4 grid rows (or ~600 px tall) so the small glosses are legible; zoom tighter on doubtful cells.

Sheets, in this order: 541, 585, 575, 577, 587, 602. (If an image is not there yet, do the others first and
check again with ls; it is being downloaded.)

What is on the sheets: telegram forms (Ottoman, 1896-1900). The cipher is written in EASTERN ARABIC DIGITS
(٠١٢٣٤٥٦٧٨٩), mostly 2-digit numbers, some 3-digit numbers, and a few words in clear. A clerk wrote, above or
beside most numbers, an Arabic-script letter (for 2-digit numbers) or a word/syllable (for 3-digit numbers),
sometimes followed by a slash "/". Some cells hold a clear Ottoman word instead of a number.
Reading order: right to left within a row, rows top to bottom (on grid sheets the printed grid; on free
sheets follow the lines/columns as best you can and say in a comment line how you ordered them).
Do NOT transcribe the printed form or the header boxes (date, number of words, etc.); do transcribe the
address line above the cipher (e.g. "یمن ولایت جلیله سنه") and any clear signature lines as type=clear tokens.

Output: one TSV per sheet, <yourfolder>/<id>.tsv, UTF-8, with a header line, columns:
  seq  x  y  type  num  num_conf  gloss  gloss_conf  slash  note
- seq: 1,2,3... in reading order
- x, y: approximate centre of the NUMBER (or clear word) in full-res pixel coordinates (needed to align passes)
- type: num2 | num3 | num1 | clear | other
- num: the number in Western digits (e.g. 67, 221); empty for clear
- num_conf: s (sure) | p (probable) | u (unsure)
- gloss: the clerk's Arabic-script gloss for that number, in Unicode Arabic letters, exactly as written
  (one letter for most 2-digit numbers; a word for 3-digit numbers); "-" if no gloss; "?" if a gloss is there
  but illegible. Use isolated letter forms: ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ك گ ل م ن و ه ی ء ئ ۀ
  Write ك for kef whatever its form; distinguish ه (he) from ن (nun) as best you can and say so in note.
  For clear words, put the word in gloss.
- gloss_conf: s | p | u (dots are often missing: if the dotting is not visible, give the letter you see and
  mark p or u, and list alternatives in note, e.g. "ف or ق")
- slash: 1 if a "/" follows the gloss or number, else 0
- note: free text (alternatives, overwritten digits, struck-out numbers, etc.)

At the end, write <yourfolder>/SUMMARY.txt: per sheet, number of tokens, how many num2/num3/clear, how many
glosses marked u or ?, and the ordering you used. Then report briefly (paths + counts). Be careful and
literal; doubtful readings must be marked, never silently normalised.
