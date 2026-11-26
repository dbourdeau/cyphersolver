Status: read in part (Brice Dudout, 12 Nov 2026; catalogue 1554, letter 2, c. 114r only: 96 of 117 words read, 50 sure + 46 probable; 42.7% sure, 82.1% sure + probable; the other six letters of catalogue 1554 unchanged, decoded, not read).

# ercole1544 / dudout: catalogue 1554, letter 2 (c. 114r), second transcription and reading

Brice Dudout, with Claude Opus 5.5, 12 Nov 2026. Builds on WAINUT's (LcCompany) work in this folder: the key
(`../key_frozen.tsv`, from the c. 103r / c. 104r pair) and the first transcription and decode of c. 114r
(`../transcription_0114r.txt`, `../decryption_0114r.txt`). Nothing in WAINUT's files is changed.

## What was done

1. **A second, independent transcription** of c. 114r (`transcription_0114r_dudout.txt`) from the Estense IIIF
   tiles at full resolution, made without opening WAINUT's transcription or decryption. Like WAINUT's transcribers,
   ours knew the table. Frozen by SHA-256 (89ed7126...64fa) before any decode by program.
2. **One pre-registered measure** (`PREREG_0114r.md`, frozen b6ecd81a...2659 before the key was applied): the key
   is applied unchanged to the new transcription, and c. 114r was never used to build the key, so the whole page
   (about 420 signs) is held out. Measure: share of decoded letters covered by Italian words of 3+ letters.
   Result (`measure_0114r.txt`): **0.605 against 200 shuffled letter tables, max 0.416, mean 0.266; PASS**
   (thresholds set in advance: above the control maximum and at least 0.50). The key holds on new text and on a
   transcription made by someone else.
3. **Agreement of the two transcriptions** (`compare_0114r.txt`, `compare_0114r.py`): 342 of 470 aligned positions
   (72.8%) before settling. Most differences are look-alike pairs named in NOTES (c/e, g/q/z, n/r/u) plus a/n,
   f/s, x/r and numbers read as letters (19 as t9, 5 as s, 55 as SS). This is the first measure of the
   transcription error on a whole 1554 page: a single pass of this hand should be expected to be wrong on
   roughly one sign in seven.
4. **A reading** (`reading_0114r.md`, `translation_0114r.md`) from both transcriptions. A word is sure when both
   give its signs; probable when they differ, or when a look-alike sign had to be chosen by sense and only one
   Italian word fits. Probable words were not settled on crops one by one. Count: `count_0114r.py` ->
   `count_0114r.txt`: 117 words, 50 sure, 46 probable, 21 unread. Below 95%: **read in part**.

## What the letter says (summary)

The count of Mirandola reports that count Giovan Tommaso (Pico), having learnt something, is working through
don Diego (probably Diego Hurtado de Mendoza) to be taken into favour, so as to make the count yield to his
claims in Mirandola; he is resolved to come to court and disturb "this negotiation". The writer tells the
recipient ("Vostra Excellentia", so probably Ferrante Gonzaga) so that he knows in what spirit count Giovan
Tommaso comes. No sender, date or address on the leaf.

## Open

- B09, eight words between "accioche" and "attende"; B05 two pairs of words; B07 "elaoi" and "tereso"; codes 44,
  55, 28. Settling the 128 differences on 3x crops is the next step and should raise the sure share.
- The other six letters of catalogue 1554 (cc. 113r, 115r-120v) were not re-transcribed.
- Scripts were run in our working folder: `measure_0114r.py` expects `work/key_frozen.tsv` (a copy of
  `../key_frozen.tsv`) and an Italian corpus `work/it_nunz_clean.txt` (16th-century nunciature letters, 1.5 MB, not
  included); the lexicon is its words of frequency >= 3.

No images are included (Estense, CC BY-NC-SA; IIIF ids in `../NOTES.md`).

## Shape plate of 25 Nov 2026, cc. 78r-79r and 174r-175v (proposal: a correction of signs, no gain in reading)

Brice Dudout, with Claude Opus 5.5, 25 Nov 2026. The transcription, table, decryption and reading of these two
letters are LcCompany/WAINUT's (PR #221). This section and its files record one check on their work and a patch that
applies it. None of their files is changed by this folder; the owners decide whether to take it, change it or
decline it.

**How.** The plate was built and scored by AI agents (Claude). Brice Dudout (human reviewer) answered it. It asked
about ten signs from the NOTES list "Not settled on the image". Each question showed the boxed sign next to real
examples of each candidate shape from sure places of the same hand, with no value or word shown. Three hidden
controls of known answer were mixed in, and all 3 passed. The selection rule and the integration rule were written
and hashed before the plate was built; one amendment, made before any answer, only re-cropped boxes. The Estense
images (CC BY-NC-SA) were used privately: no image, crop or derivative is included. AI analysis was not raised with
the archive; the project's method was not presented to it at the time.

**Result.**
- Settled by shape: A05 `3` (a lone 3 is not in the table: open code `[#3]`), B01 `h` (confirmed), B02 `n` (the
  signs give "sa io"; `[?Se]` kept), B21 3rd sign `n` (`h ? n b`), E21 `g`, F03 `q`, F08 `2 q` (open code `[#2]`),
  G06 `z` (confirmed).
- *intertener* (E21) becomes sure: verbatim, the repair goes. *gratissime* (F03) goes from sure to probable: the
  signs give "gratissi-d-e", so it becomes the repair `gratissime°`, from the sense only.
- G06: with z confirmed, the signs give "masca" (*si cavara la masca*, take off the mask) against the repair
  `tasca°`. Flagged; `tasca°` is kept.
- Still open: B21 2nd sign (none of the shapes offered; close to a), C07.

**Plate defects.** C07 is not counted: the examples of 9 and of z showed the same sign in this hand (the "tailed 9"
z). In the control x/a/n, one example of the decoy a was badly framed (about 5 px to the left, it held the arm of the
x); the control was answered right and is kept as valid.

**Count** (folder's `scripts/count_words.py`, unchanged): the same before and after (cc. 78r-79r plain 718, clean 184,
verbatim 148; cc. 174r-175v plain 1240, clean 260, verbatim 216, repairs 15). One word moves each way. Status: still
read in part.

**Applying the patch.** From the repository root:
`git apply -p1 --directory=targets targets/ercole1544/dudout/ercole1544-planche-2511.patch`.
It applies cleanly to `main` at db211162a9 (the folder's files are unchanged since b13dd55072). After it,
`scripts/decode.py` regenerates both decryptions as patched, and `scripts/check_repairs.py` passes.

**Files** (in this folder): `PROPOSAL.md` (the proposal, table of answers and changes), `ercole1544-planche-2511.patch`,
`RECOMPTE.md` (word-by-word recount, in French), `sign_check_2511/` (selection rule with its amendment, in French;
`REGLE-SELECTION.sha256` checks the final version; the initial version is its first 4656 bytes,
`head -c 4656 REGLE-SELECTION.md | shasum -a 256` gives 762d8bf4…6959; the answers `answers-2511-ercole.json`; their
meaning in English, `results.tsv`), `SHA256SUMS` (hashes of these files and of this README).
