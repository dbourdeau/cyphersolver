# Vetting, Daniel Bourdeau (2026-11-25)

Run by a Claude Code session (Claude Sonnet 5.5) for Daniel Bourdeau, following `research/VET.md`. Leads: the 9 new leads
merged from the sweeps of 24-25 Nov 2026 (ids 3851-3859) and five older leads from `research/leads.json`. The file is
`vetting.json` (`python research/vet.py --check` passes; applied with `--apply`). Result: 1 promoted, 1 held for its
owner, 1 closed, 11 unvetted.

## Merge

Branches merged: `worktree-agent-ad884b8b47d2b32f1` (with its parent `a44b47e5cc055d447`, both contained in
`worktree-agent-a2f3c7a19f4f0515d`), `a2f3c7a19f4f0515d`, `a6ec34871d6d1b6f5`, `geniza-literature-2026-11-25`. Conflicts in
`research/COVERAGE.md` (kept both sides' new sections) and `research/README.md` (took main's copy, re-ran
`research/_index.py`). `merge.py` did not know the two new sweep folders: both were added to its `SWEEPS` list. The
Arabic-treatises rows lacked `region`, `seen`, `score_note` and had an invalid `period`, and the Geniza rows had
`seen: "image viewed"`, no `score_note` and periods like `1101-1300`; those fields were fixed in the two `candidates.json`
files (periods set to `unknown`). 9 rows merged as 3851-3859. The YEK massive sweep produced a shortlist
(`research/sweep_2026-11-25_yek_massive/shortlist.tsv`), no candidate rows, so nothing from it was merged.

## Leads

- **3849 Butler, Mexico, 30 Oct 1830: open, promoted** (catalogue 3849). Frame 233 of NARA M97 roll 6 seen at 4024 px: a
  numeric nomenclator (55 numbers, 4 signs) among plain English, endorsed "my private Cypher". Bosch Garcia's edition
  (UNAM PDFs, vol. II) was opened: no item of 30 Oct 1830, so it is not printed. DECODE, Cryptiana unsolved.htm and GL.htm,
  Weber 1979, Narvaez 2019: no reading. The State Department code was tested by the sweep and does not fit.
- **3855 T-S K24.37: open block written, not promoted** (the owner catalogues K24.24 and K24.37; `targets/tsk2437`).
  Eight lines of dash-divided angular signs, about 200, seen at 1800 px, not mirror Hebrew as the literature survey
  guessed. PGP 32699: description only.
- **3856 CUL Or.1080 6.12: unvetted.** Four lines of cursive strokes on parchment; script not identified, not shown to be a
  cipher.
- **3857 T-S Ar.39.472: unvetted.** Letter-and-number table; reads as a divination table.
- **3858 CUL Or.1080 14.13 + 14.25: unvetted.** Amulet; stroke-and-numeral lines read as abjad number series.
- **3859 T-S K12.60 verso: closed, not_cipher.** Charakteres each glossed with a Hebrew letter: key-type material for the
  Bohak ring-letter family, no ciphertext.
- **ENA 3207.17 (PGP 10130) and ENA 3682.7 (PGP 6744): not leads, no row.** The thorough sweep saw both. ENA 3207.17 was
  viewed on 15 Nov 2026 (`sweep_2026-11-15_arabic/part_A.md`: an amulet formula in charakteres, not a cipher). ENA 3682.7 was
  re-viewed in a crop here: a ring-ended charakteres amulet inside an ouroboros ending in Greek-like capitals ("NIBH"),
  magical names and not shown to be a cipher. Both stay in the Bohak-family notes for a key comparison once K5.7 and
  K12.60 are compared with Bohak 2010; neither goes to the catalogue.
- **T-S K24.24, T-S AS 187.240, ENA 4100.7b:** already targets or owner's items (`targets/tsas187240`, `targets/ena4100`;
  K24.24 is the owner's); not touched. Lead 2884 (K24.24) stays unvetted from 15 Nov.
- **3851-3854 (Syriac and Arabic secret-script catalogue rows): unvetted.** No leaf seen: BL digitisation of Add. 21580 and
  14471 not found (the BL record for 14471 conflicts with the lead's shelfmark); vHMML USJ 2/980 needs the owner's sign-in;
  ONB N.F. 303 images 5-72 not screened and Elmore 1999 not opened.
- **2903 Jain colophon (CUL Add. 2255 f. 19v): unvetted.** Seen: a run of Devanagari digits and a cross, so numerals, not an
  unidentified script; about twelve signs.
- **2958 Alcort D/0004: unvetted.** The margin decipherment is on the sheet and issue #779 is working it.
- **2529 Oxenstierna 1634: unvetted.** HSH del 30 p. 91 still not found online.
- **2901 Sudan telegrams (Durham): unvetted.** A printed code-book system; needs the code book.
- **2387 ASF MAP LXXIII doc. 3: not touched.** It already carries an `open` block of 16 Nov and counts as ready to promote,
  but its host fails TLS from curl and did not load in Chrome today, so the leaf could not be re-seen; the block says
  only that a letter substitution "fits better" than a hard hand. Left for the owner to decide.
- **2832 P.Vindob. A.P. 11016:** ready by the gate but kept off the website at the owner's request (memory note of 15 Nov);
  not promoted.

## Routes

| Host | Result |
|---|---|
| geniza.princeton.edu (`/en/documents/<id>/`, `/scholarship/`) | plain curl; scholarship 404 for all six records |
| images.lib.cam.ac.uk IIIF | plain curl; cudl.lib.cam.ac.uk pages give 403 |
| catalog.archives.gov `medialz` frame images | plain curl, no login |
| historicas.unam.mx Bosch Garcia PDFs (about 22 MB each, OCR text) | plain urllib with a browser User-Agent |
| cryptiana.web.fc2.com `unsolved.htm`, `GL.htm` | work (Shift_JIS) |
| archiviodistatofirenze.cultura.gov.it | curl exit 35 (TLS), Chrome did not load the image URL |
| decode_search.py | works |

## Next vetting pass

Take (1) 3856-3858 with a palaeographer or the Bohak/Zinger group; (2) the older online leads still waiting for an edition:
2529 (HSH 30 or AOSB I:12), 2222/2221 (Teleki volumes); (3) 3644 Laurens (a maintainer must open the three images named in
its next step); (4) re-view 2387 when the ASF host answers; (5) the YEK shortlist after its Arabic-script terms are swept.
Of the "up to 40 older leads" only five were worked: most online leads left are blocked by an edition or an archive host.
