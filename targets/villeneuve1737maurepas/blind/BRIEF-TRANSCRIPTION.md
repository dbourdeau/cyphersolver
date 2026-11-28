# Blind transcription brief — Villeneuve 1737 (Archives nationales, AE/B/I/414)

You transcribe numeric cipher groups from 18th-century French diplomatic letters. You do NOT decipher. You have no key and must not try to build one or guess meanings of numbers. Images are PRIVATE: do not copy, crop, upload or describe them outside this task; only write the text files requested.

Images: band crops in /Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/villeneuve-1737/crops/
Name = <frame><side>_b<band>.jpg, side S = single page, L = left page of spread, R = right page. Each page is cut into 3 horizontal bands (b1 top, b2 middle, b3 bottom) that OVERLAP by ~4 %: a line may appear at the bottom of b1 and the top of b2 — transcribe it once. For orientation, whole-spread overviews are in .../villeneuve-1737/thumb/<frame>.jpg and medium-size in .../small/. Read every image with the Read tool; zoom by reading the band again if needed. If a line is unclear, look at it in the larger 'small' image too.

Output: ONE plain text file (path given in your task). For each page, a header line `# <frame><side>` then one record per manuscript line, numbered from the top of the page (L01, L02 ...), counting only lines that carry cipher numbers or text of the letter (skip archive stamps, folio numbers, marginal headers like "Commerce", reflection/bleed-through from the other side of the paper which appears faint and mirrored).

Records:
- `L07 C: 304 199 168 87 171 164 102 469 78 17 10 82 303` — cipher line, groups separated by single spaces, left to right, exactly as written.
- `L07 G: Pour le féliciter sur son avènement` — ONLY on pages with an interlinear decipherment written above the numbers (frames 0197-0202, 0230-0231): the gloss text written above that cipher line, in modern letters, original spelling, as read. Give the G record before its C record, same line number. If the gloss is illegible write ‹…› for the illegible part.
- Clear (non-cipher) words of the letter itself inside or between cipher lines: write them in the C record between « », e.g. `L09 C: 441 205 44 215 148 198 «ne puisse» ` ; a line that is wholly clear text: `L10 T: pas être préjudiciable à notre` (T = clear text line; for long clear passages a short summary like `L10-L18 T: (clear text, 9 lines)` is enough after the first line).

Notation inside C records:
- Uncertain digit(s): give your best reading followed by ? , e.g. `187?`; if two readings are equally possible, `187|107`.
- Illegible group: `?`
- Group(s) lost in the binding/gutter or off the edge of the image (a line visibly continues into the fold): end the line with `[G]` (one [G] whatever the number of lost groups). A group only partly visible at the gutter: read what you can and add `?`, or `[G]` if nothing readable.
- A small mark written above or below a group (small numeral, dot, accent, comma, apostrophe-like stroke): write group then `^` and the mark, e.g. `318^2`, `318^'` ; underlined group: `2_` ; overlined: `2^-`.
- Punctuation between groups other than the normal dot separator (semicolon, comma, colon, double dot ".."): attach it to the preceding group: `130;` `118,` `44..`
- Struck-through group: `~318~`.
- Do NOT normalise or "correct" numbers to make them consistent across lines. Write what you see.

Be complete: every cipher group on every listed page. Finish with a line `# END` and a short line `# notes:` with any general remarks (e.g. lines you were unsure belonged to the letter).
