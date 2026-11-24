# Readings, one file per letter

Written by the two reading agents on 14 Nov 2026 from the two transcription passes and the images; corrections from the
independent second agent are applied and recorded at the end of the files concerned (1776-04-30, 1776-09-01, 1777-08-02,
1778-06-14, 1779-05, 1779-09-20, 1781-09-02).

Paths in these files to `print/...` and `web/...` (extracts and OCR of the printed editions) and to `readings/auto/`
refer to the working folder and are not committed: the edition texts are under their publishers' terms. The editions are
listed in `../sources.md`; the passage-by-passage result is `../print_check.tsv`.

Marks: in the number blocks `*` = a number kept as written but emended in the text, `{...}` = plain words or signs written
inside a run, `[x..]` = struck out, `#` = lost or blotted; in raw decodes `{x}` = an emended letter; in normalized text
cipher passages are in [brackets].

Since 24 Nov 2026 the texts in `../letters/*_text.txt` use the project's marks instead of the ones above (the maintainers'
integration review, an AI agent): cipher passages between ⟦ and ⟧, `[x]` for a letter corrected or supplied by sense (a hole on
the read bar), `{+x}` for a letter given by another cipher copy or by the decipherer's letter over the number, `{-x}` for a
letter or sign the numbers give and the reading drops. Each file lists its marked letters under "Notes". The files in this
folder were not changed: their "Normalized text" sections keep the first marks. Three places differ from them in substance: the
cipher repeats the plain word before it on 2 Aug 1777 (le), 14 Aug 1777 (à) and 24 Feb 1778 (des); "Pensionaire" is printed with
one n, as the numbers spell it; and "mérit(ent)" of May 1779 is now "mérit[e]". The key replay (`../replay.py`) checks the
`_text` files against the key output.
