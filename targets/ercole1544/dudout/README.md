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
