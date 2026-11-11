# Viewer: Lee's letters of 1, 2 and 6 February 1813

`index.html` shows each manuscript frame beside the reading of William Lee's three letters to James Monroe. It is a
plain static page with no external scripts: open `index.html` directly from disk, or serve the folder from any static
host (GitHub Pages included).

- **Tabs:** one per letter, plus "Key and citation" (where the keyword WINCHESTER comes from, how Lee's slips garble the
  text, how *The Papers of James Monroe* is used).
- **Views:** "The letter" (context, the whole letter with the cipher marked, and the cipher figure by figure: figure, key
  letter, the letter it gives), "Passage by passage" (figures, the key's output, the reading, the 1813 clerk's reading
  and a note; filters for proposals and differences and for text first read now), and "Full text".
- **Marks:** † the 1813 reader failed, ‡ he never reached the passage, ≠ he read it differently, § proposal (the
  reading assumes a particular slip of Lee's); `[x]` letters are supplied for Lee's wrong figures.

## Images

No images are stored here. The page loads each frame from the National Archives catalog:

    https://catalog.archives.gov/medialz/dc-metro/rg-059/302031/T164/T164-03/T164-03-<NNNN>.jpg

(RG 59, microfilm T164 roll 3, frames 0099-0110; 0103 is not used). The "original at NARA" link opens the same file.

## Files

| file | what |
|---|---|
| `index.html` | the viewer (layout, image pan and zoom, rendering) |
| `data.js` | the readings, passage by passage, generated (below) |
| `reveal_lee1813.json` | draft for the site's "watch it decipher" widget (`docs/reveal/<slug>.json` format): the opening of the 6 Feb letter, figure/key letter to letter |

## Regenerating `data.js`

`data.js` is generated from the reading, decryption and transcription files of this folder (and the 1813 clerk's
readings of 2 Feb) by the contributor's build script, which is not part of this repository:

    python3 scripts/build_viewer_data_2026_11_11.py lee1813
    python3 scripts/build_viewer_data_2026_11_11.py --docs lee01,lee02,lee06 --out targets/lee1813/viewer
    python3 scripts/build_viewer_data_2026_11_11.py --docs lee01,lee02,lee06 --check   # compare, write nothing

It writes `window.READINGS = {docs, frameLabels}`; each document carries its passages (`numerals`, `keyrow`, `mech`,
`read_as`, `clerk`, `marks`, notes) and the letter, reading and context as HTML.

## The reveal draft

`reveal_lee1813.json` follows the schema of `docs/reveal/*.json` (`slug`, `anchor`, `title`, `caption`, `unit`,
`key_note`, `tokens` with `g`, `p`, `cls`, `w`). Each tile's `g` is the figure as Lee wrote it over the key letter used
(`24/C`), so a tile always gives the same letter. Lee's mistakes are marked, never repaired silently. A wrong figure
keeps the letter it actually gives as `p` (so the key grid stays true) and shows "wrong → meant" through the widget's `show`
field, with `cls: "inf"`, which `docs/style.css` already colours red (`.tile.inf`); amber `unc` was too close to the normal
letter colour in the dark theme. Slips that read correctly once followed (a key letter used twice, a stray dot in 1.2, two
figures run together as 11) are `unc` and named in `g` ("16/T again", "1.2→12/T", "11→1/H"). The caption lists each one. Word starts were set with `docs/_reveal_words.py`. To use it, copy it to
`docs/reveal/lee1813.json`.
