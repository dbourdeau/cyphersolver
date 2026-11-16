# Vetting, Daniel Bourdeau (2026-11-15)

Run by a Claude Code session (Claude Opus 5.5) for Daniel Bourdeau, 15 Nov 2026, following `research/VET.md`.
Leads 2895-2898 from the Arabic sweep of 15 Nov 2026 (`research/sweep_2026-11-15_arabic/part_C.md`, `part_D.md`).
No open issue or pull request names any of them (gh search on the ids, Browne, Hamdani, Ismaili).

## Verdicts

- **2895, open.** Cambridge, Browne F. 43 and F. 16: Subh-i Azal's "cyphers" turn out to be short groups of Eastern
  Arabic digits. Browne printed them in JRAS 1892: p. 489 (F. 43: 5331685 and 3125311376) and p. 651 (F. 16 colophon:
  51092). He says Azal refused to explain them, and he prints no reading. Nicholson 1932 has nothing more, and the
  literature searches found no explanation. Seen as Browne's typeset transcription on the archive.org scan. The
  manuscripts themselves are not on CUDL as far as could be found. A related convention is in print: Rosen reads
  Baha'u'llah's 152 as the abjad letters of Baha (same JRAS volume, p. 273), recorded as `key_held` and not tested.
  The text is very short, about 22 digits.
- **2896, unvetted.** IIS MS 1662: the de Blois entry on the IIS site shows that cipher survives on fols 29a-b and
  83b and gives no reading. But Verena Klemm, Die Welt des Islams 65/4 (2025) 381-414, an open-access study of this
  notebook, could not be opened: brill.com answered 403, and her blog post is behind a bot check. No images.
- **2897, unvetted.** IIS MS 1291 (b): the only description is "part of the text in cryptic alphabet", and there is
  no image. It may be the standard Tayyibi secret script, whose key is in print (Strothmann 1943, cited by Gacek
  1984, which is full text on archive.org).
- **2898, unvetted.** IIS MS 1313: the only description is "cryptograms on p.23", which could be text or diagrams.
  There is no image, and Poonawala 1977 was not opened.

## Routes

| Host | Result |
|---|---|
| special-collections.iis.ac.uk/Details/manuscripts/{154,45,832,587} | 200 with curl. The entries are full catalogue text, each marked "No image available for this record". The gallery tiles load by script. |
| raw.githubusercontent.com (fihristorg/fihrist-mss) | 200 for the TEI of F. 43, F. 16, F. 41, F. 42 and F. 44. codeload zip 403, not retried. |
| archive.org | 200. Used for the JRAS 1892 djvu text, the inside.php full-text search and the `page/nNNN_w2000.jpg` page images (iiif.archive.org `$n` gave 404). Also Nicholson 1932 (`b31361596`) and Gacek 1984 (`GacekCatalogueOfMSInIISLibrary1984FT`) full text. |
| cudl.lib.cam.ac.uk | `/iiif/MS-ADD-03996` 200, `/iiif/MS-BROWNE-F-00043` 500, `/search` 403 (stopped there). images.lib.cam.ac.uk IIIF guesses 404. |
| brill.com | 403 on the Klemm PDF; stopped. |
| globalcommentary.utoronto.ca | JavaScript cookie challenge (bot check), not passed. |

## What is left

- 2896: read Klemm 2025 in a browser for fols 29a-b and 83b, then ask the IIS for images. de Blois 2011's
  introduction and plates in print may hold the MS 1499 cipher table.
- 2897, 2898: ask the IIS (Ismaili Special Collections Unit, Aga Khan Centre) for images of MS 1291 ff. 71r-86v and
  MS 1313 p. 23.
- 2895: ask Cambridge UL (near_eastern@lib.cam.ac.uk) for images of F. 43 ff. 101b and 203a, F. 16 f. 261a and the
  end of F. 39, to check Browne's typesetting of the digits.
