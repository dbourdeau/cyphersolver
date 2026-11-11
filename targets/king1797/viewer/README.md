# Viewer: King, No. 29 (13 April 1797)

`index.html` shows the manuscript frames of Rufus King's despatch No. 29 to Timothy Pickering beside its reading. It is
a plain static page with no external scripts: open `index.html` directly from disk, or serve the folder from any static
host (GitHub Pages included).

- **Tabs:** the despatch, plus "About the code" (how the key was rebuilt and how firm the reading of No. 29 is).
- **Views:** "The letter" (context, the whole despatch with the code marked, and each coded line group by group with the
  value underneath), "Line by line" (the groups as written, the key's output and the reading), and "Full text" (the whole
  despatch, frames 0092-0096, with a summary).
- **Marks:** yellow words rest on the context of this letter alone (grade I values in `key.tsv`).

## Images

No images are stored here. The page loads each frame from the National Archives catalog:

    https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-004/M30-004-<NNNN>.jpg

(RG 59, microfilm M30 roll 4, frames 0092-0096). The "original at NARA" link opens the same file.

## Files

| file | what |
|---|---|
| `index.html` | the viewer (layout, image pan and zoom, rendering) |
| `data.js` | the reading, line by line, generated (below) |
| `reveal_king1797.json` | draft for the site's "watch it decipher" widget (`docs/reveal/<slug>.json` format): lines 7-13 of the paragraph on Sweden, code group to word |

## Regenerating `data.js`

`data.js` is generated from `reading_no29.md` and `no29_decryption.txt` of this folder by the contributor's build
script, which is not part of this repository:

    python3 scripts/build_viewer_data_2026_11_11.py king1797
    python3 scripts/build_viewer_data_2026_11_11.py --docs king29 --out targets/king1797/viewer
    python3 scripts/build_viewer_data_2026_11_11.py --docs king29 --check   # compare, write nothing

It writes `window.READINGS = {docs, frameLabels}`; the document carries its coded lines (groups as written, values,
reading) and the letter, reading and context as HTML.

## The reveal draft

`reveal_king1797.json` follows the schema of `docs/reveal/*.json` (`slug`, `anchor`, `title`, `caption`, `unit`,
`key_note`, `tokens` with `g`, `p`, `cls`, `w`). Values are those of `key.tsv` as applied in `no29_decryption.txt`;
the five grade I values in these lines are marked `unc`, and the clerk's + in line 8 is a `null`. Word starts were set
with `docs/_reveal_words.py`. To use it, copy it to `docs/reveal/king1797.json`.
