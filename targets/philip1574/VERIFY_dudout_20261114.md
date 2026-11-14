# philip1574: README recount of the clear version; scans no longer reachable (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Read bar (README)
`research/reading_audit/v10_relabel.share` on `clear_version.md` gives 433 words and 37 holes, i.e. **0.921**,
under the 0.95 bar, against the recorded `read_share` 1.0. The holes are not unread words: `v2_score.holes` turns
every bracketed abbreviation expansion into a hole (r[elaci]on, q[ue], cap[ita]n, v[uest]ra, nap[oles], ag[ost]o ...;
37 expansions in the Spanish text) and the file's English heading ("Abbreviations expanded in [brackets]") is counted too.

`verify_dudout_20261114.py` counts the Spanish body only, keeps the expansions as read words (the abbreviation is
written in the clear version, only its expansion is editorial) and drops the note "(cipher: ...)": **406 words, one hole
([?]oran = Hürrem Bey's name, given by the cipher), 0.998.** By the README rule the clear version is read; the
recorded 1.0 holds in substance (0.998). If `v10_relabel.py --apply` were run on this target as it stands, it would
move it to "read in part" on the expansions alone. Writing the expansions in another way (for instance italics, or
the abbreviation as written) would avoid that; not changed here.

## Image check
Not possible: the Koninklijke Verzamelingen rendition API named in NOTES.md now answers `410 Gone`
(`cms.koninklijkeverzamelingen.nl/api/images/rendition/11266/original/`, 14 Nov 2026), and the deepzoom paths of
`scans.json` answer 404. The ~16 cipher lines NOTES lists as not compared sign by sign with the key stay unchecked;
there is no sign-level transcription to re-run `key.md` on.

## Key correction
None (no transcription to test the key against).
