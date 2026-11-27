# IMAGE_ACCESS: JSTOR community.38709311 (Fenian Brotherhood Collection, Catholic University of America)

## Where the images are
- Viewer: https://www.jstor.org/stable/community.38709311 (image seq=1 and seq=2). Each image shows one opened side of the
  folded sheet (two pages side by side). Rights statement shown on the item: "No Copyright - United States". Free to view.
- Viewed 2026-11-25, about 23:22-23:30 UTC, in Malcolm McBratney's Mac Chrome through Claude in Chrome, without a JSTOR
  login (the page showed "Log in" buttons).
- Page order by sense, and where each page sits in the viewer:

| page | viewer image | half | first words | number groups |
|---|---|---|---|---|
| P1 | seq=1 | right | "Letter No. II. London June 24th 1885. My Dear Friend" (top margin upside down: "When Madame H— returns ...") | none |
| P2 | seq=2 | left | "From the notes I gave him" | G01 (line 8), G02 (line 21) |
| P3 | seq=2 | right | "We found him a polished gentleman" | G03 (line 15) |
| P4 | seq=1 | left | "other firms." | G04-G13 (lines 4-23) |

- A IIIF image URL was seen in the page (https://www.jstor.org/iiif/2021/05/25/20/15c73f1b-a920-49bc-ab79-939afb379a2c_de...,
  truncated in the DOM listing). It was not fetched, so no IIIF region boxes can be given.

## What could not be fetched
- Plain GET from the sandbox of https://www.jstor.org/stable/pdf/community.38709311.pdf at 2026-11-25T23:21:14Z: HTTP 200
  but text/html, 3,038 bytes (a refusal page, not the PDF). No other scripted route was tried.
- A login test by a person in a private window: not done.

## Working crops (not filed)
No images are filed in this pull request (as asked on #974). JSTOR's terms for re-publishing Community collection
images were not checked here. The transcription was made from 39 working screen zooms of the viewer (38 PNG, 1 JPG),
taken with Claude in Chrome at 3x zoom; they are about 1,176-1,188 x 410-420 px each (some smaller cut-outs), are
screen captures and not archive files, and are kept locally. Their scroll offsets in the viewer were not recorded, so
the viewer positions are given by page, half and line (table above). To rebuild any crop: open the viewer, choose the
image and half from the table, zoom in three steps, and scroll to the line.

Which local crop shows which group (from the blind reader's table, blind2/BLIND2.tsv; file names are Chrome capture ids):

| group | page.line | crop file(s) |
|---|---|---|
| G01 | P2.8 | ...1795649014157-7rhrbf, ...1795649294103-99leqq |
| G02 | P2.21 | ...1795649027015-352t5w |
| G03 | P3.15 | ...1795648995475-0kenz3, ...1795648976442-a71vi0 |
| G04 | P4.4 | ...1795649040520-fdntb8 (cut at the bottom edge) |
| G05 | P4.6 | ...1795649040521-7fhmj8 |
| G06 | P4.11 | ...1795649040522-rfbwec, ...1795649258404-9khao7 |
| G07 | P4.14 | ...1795649040522-dgsoc6, ...1795649258404-0eetb5 |
| G08 | P4.16-17 | ...1795649074535-kb5zfb, ...1795649040522-dgsoc6 |
| G09 | P4.18 | ...1795649074535-kb5zfb, ...1795649271167-7ki79y |
| G10 | P4.19-20 | ...1795649074535-kb5zfb, ...1795649106823-jlkqho |
| G11 | P4.20 | ...1795649106823-jlkqho, ...1795649258405-21zfj8, ...1795649106823-1641ui |
| G12 | P4.21 | ...1795649106823-jlkqho, ...1795649074535-zbpgud |
| G13 | P4.23 | ...1795649271166-fiyjb9, ...1795649074535-zbpgud (digit bottoms clipped at the page edge in both) |

The blind reader's enlargements (blind2/zoom/, 22 PNG cut from these crops) are also kept locally and not filed.
