# T-S AS 187.240: Geniza bifolio with Hebrew-letter and glyph cipher blocks (Cambridge University Library)

Status: in progress

Lead from the Hebrew-script sweep of 6 Nov 2026 (`research/sweep_2026-11_hebrew/`). Cambridge University Library,
Taylor-Schechter Additional Series 187.240, Princeton Geniza Project id 42435 (tagged `cipher`, added 2026: "merits
examination, might be solvable based on the surrounding formulae"). Undated, paper, probably 12th-14th c. (unassessed).
No edition, no published reading found. Not in DECODE, Tomokiyo or Lasry (sweep check).

## Access

Images by plain curl, no bot check: `https://images.lib.cam.ac.uk/iiif/MS-TS-AS-00187-00240-000-0000N.jp2/full/full/0/default.jpg`,
N = 1 and 2 (2000 px wide; N = 3 is a 404). Saved under `img/` (not committed; re-fetch with the URL).
Note: the sweep called N=1 the recto. The first image (`p1.jpg`) is the **less informative side**; `p2.jpg` is the side with the
glyph block. Which is recto and which verso is not settled (the CUDL labels were not read).

## What the page shows (6 Nov 2026, looked at on the crops of `p2.jpg`)

The sheet is torn and stained; text survives in several ruled-off blocks (a rule is drawn under each).

- **Hebrew-letter lines** (upper left): word-divided by dots, words of 2-4 letters that are not Hebrew words. A string
  *kk mas nun m'k nk* (כך מס נן מעכ נך) recurs on at least two lines, and *lk 'b qw ...* (לכ עב קו ...) opens two more.
  Between them are lines in the same hand that look like plain Hebrew (*lomar lkn 'sy lh ...*, "to say: therefore make ...").
- **Plain Hebrew lines** (lower left and upper right): two or three lines under each rule that read as ordinary words; the
  letters are legible but the hand and the stains stopped a certain reading at this resolution. Their content is the
  surrounding formula the Geniza Project note points to.
- **Glyph block** (lower right, two ruled units): about 120 invented signs in lines that open with the same sign group and
  repeat nearly in full (the second unit repeats the first). One sign is a stemmed goblet shape that stands at the start of
  lines. The lines look like the same formula written twice, which gives a repeat to align.
- Reading of the whole as a type: a practical text (charm or amulet instructions) in which the strings that look like divine
  or angelic names are written in a code. This is a hypothesis from the layout, not tested.

## Size, honestly

The usable ciphertext is small: about 100 Hebrew letters and about 120 glyphs, with holes and stains, and the two blocks are
probably one formula in two codes. That is below what a ciphertext-only break needs (a few hundred signs in one system). The
only realistic route is a crib: the plain Hebrew lines around the blocks, plus the repeat between the two glyph units.

## Moves so far

1. First-pass transcription of the Hebrew-letter block (`transcription_hebrew_block.txt`), from the downsized crop, with `?`
   for doubtful letters. Not verified at native resolution.
2. Nothing tested yet. Standard permutations (atbash, albam, ayak-bekar) are to be run on a checked transcription, not this one.
3. **Native-resolution images** fetched (IIIF region tiles, `img/n1.jpg`, `img/n2.jpg`, 5286 x 4628 px; the 2000-px `full/full`
   copy is a quarter of the detail). Side 1 (`n1`) carries the most Hebrew-letter lines (ruled blocks at right and left); side 2
   (`n2`) carries the glyph block. At this size the lines are legible, but the hand is cursive and ם/ס, כ/ב, ך/ן, ל/ר are
   ambiguous on a crop, so a line-by-line transcription is not safe to base a solve on.
4. What the clearer lines of side 1 look like (lower right block, read right to left, not verified): runs of two- and
   three-letter groups, several ending in final forms (נך, פך, נן), such as *שלם נן ... פך נך קר שב* and *כך מס נן מעכ נך*,
   alternating with lines of ordinary Hebrew words (*שרי חזק*, *עקיר*, *לומר ... עשי*) and rows of dots used as fillers. The same
   groups recur from block to block, so the blocks are probably one formula written several times.
5. **Hypothesis, untested:** the three-letter groups (*לכב*, *ושר*, *יחו*, *חבו*, *ראה*, *ע"ב*) resemble the 72 trigrams of the
   Shem ha-Meforash (Exodus 14:19-21), the usual material of Geniza magical texts. If the Hebrew-letter lines are that sequence,
   written in a letter-substitution or a two-letter shorthand, the sequence is a known plaintext of about 216 letters and the page
   is solvable by alignment. This needs a checked transcription; the groups that recur here (*כך מס נן מעכ נך*) are not
   trigrams of the standard list, so a transformation would have to be found first.

6. **Second pass at native size** (`transcription_side1_clear_lines.txt`, ten lines, every one with doubtful letters). The
   lines mix three kinds of material: runs of 2-3-letter groups with a frame that repeats (`... נן ... פך נך קר שב`,
   `כך ... נן מעכ נך`: slot 3 and slot 5 begin with נ, and the same final forms close the groups), lines of plain Hebrew
   epithets (`שרי חזק`, `מלכי`, `עקיר`, `לומר לכן עשי`), and dot fillers. The frame suggests a fixed formula whose second and
   fourth words vary from line to line.
7. Eyeball checks against two candidate plaintexts, neither confirmed: the 72 trigrams (Exodus 14:19-21) and the 42-letter name
   (*Ana bekoach*, six groups of seven letters, its pairs *קר עש טנ ... חק בט נע*). A few pairs resemble (`קר`, `חק`, `עב`), but no
   run of three consecutive groups matches, and with doubtful letters that is no evidence either way.

8. **Enhanced grayscale at native size** (autocontrast crops of `n2.jpg`) makes the upper-left block of side 2 legible. The
   frame of the repeated formula is now clear, three times in a row: `[לכב? עב קו וח] כך לס נן מעט נך` (the second word is לס
   or לם, not מס as first read). Dot-words close in a final form whenever the last letter is כ, מ, נ, פ or צ, so the scribe
   treats each dot-group as a word; `כך` is then kaf-kaf, `נן` is nun-nun, `נך` is nun-kaf, `פך` is pe-kaf. Several groups are
   also real Hebrew words (`כך` thus, `פך` flask, `קר` cold, `שב`, `קו`, `עב`, `מעט`), so the text may be a word code (each
   Hebrew word standing for a letter or a name) rather than a letter cipher.
9. **Computed test** (6 Nov 2026, post hoc, tokens read from the images with final forms collapsed): of 15 groups
   (`כך לס נן מעט נך פך קר שב עב קו וח עי לכב כנש`) five occur as substrings of the 42-letter name's letter string
   (`ננ`, `קר`, `שב`, `קו`, `עי`); in 2000 shuffles of those 42 letters the mean is 1.06 and the maximum 5, so P(>= 5) = 0.002.
   The 72 trigrams give 3 hits against a baseline of 3.1 (no signal). A weak hint for the 42-letter name (Ana bekoach), not a
   reading: the tokens were chosen after looking, some readings are doubtful, and the groups do not follow the name's order.

10. **Three-agent transcription** (files `transcription_side1_AB.txt`, `transcription_side1_CD.txt`, `transcription_side2.txt`,
    `glyphs.txt`; all low to medium confidence, block D of side 1 is mostly stain and bleed-through). Results that hold:
    - The Hebrew frame is nine groups, `לכ עב קו וח כך לס נן מעט נך` (19 letters), seen on three lines of side 2 and once on side 1;
      a second frame, `שלם נן ?? פך נך קר שב`, closes side 1.
    - The plain lines recur: `לומר לכן עשי/מעשי` three times, `מלכי עתוד?`, `.. מבני ..` over `עמרם`, and a torn
      `ופרצו עתולי? קרו? ערוצים?`. They point to an Exodus/Amram setting, nothing more.
    - The glyph formula (a goblet sign, then 7 glyph-words, 15 signs, 14 distinct) is written three times identically, so the
      repeats add no information. It does not line up with the Hebrew frame (7 words against 9; 15 signs against 19 letters;
      repeat pattern differs), so the two are different texts or different codes, not a parallel pair.
11. **Isomorph test** (computed): no window of the 72 trigrams (216 letters) or of the 42-letter name has the same letter-repeat
    pattern as the 19-letter frame, or as its halves of 9 and 11 letters. So neither is the plaintext under a letter substitution
    (with final forms collapsed). The weak hint in move 9 does not survive this test.

**Status after this round: not broken, and not breakable by ciphertext alone.** The usable ciphertext is one 19-letter frame
(a few variants) and one 15-sign glyph line, each repeated; repetition gives no new equations. A break needs a plaintext for
the frame: from the plain lines around it, from the Geniza formulary this fragment belongs to, or from Elbaum's and Bohak's
work on the same group of ciphers. Next: identify the formulary (Amram, ערוצים, עשי: search Geniza magic texts for the same
plain lines), then ask Elbaum and Bohak.

12. **PGP record** (geniza.princeton.edu/documents/42435, read 6 Nov 2026): "Bifolio of pen trials including a section written in a
    cipher; merits examination (might be solvable based on the surrounding formulae)", tag `cipher`, Hebrew, no transcription,
    no translation, no related documents or bibliography. Images there are labelled 1r and 1v; n1 here is 1r. "Pen trials" means
    a scribe's practice sheet, so the formula may be a stock phrase written through a cipher, and the repeats are practice, not
    meaning.
13. **Classical Hebrew ciphers on the 9-group frame** (computed): all 21 alphabet shifts, atbash, albam, ayak-bekar and
    reversal. None gives running Hebrew. Atbash gives `כל זש דפ פס לל כח טט יזנ טל` (three real words, `כל`, `כח`, `טל`, as
    chance would give); reversal gives `כל בע וק חו ככ סל ננ טעם כנ` (`טעם` from `מעט`, `כל`, `סל`). Neither is a reading.

Not broken. The blocker is now the missing plaintext as much as the transcription: cursive Geniza letters that I cannot tell apart from crops
(ם/ס, כ/ב, ך/ן, ל/ר) make every candidate test unreliable. What would move it: a checked transcription by a reader of Geniza
cursive (Elbaum or Bohak, or a palaeographer), then the two candidate plaintexts tested as isomorphs.

## Remaining gaps

- Clean transcription of all blocks at native resolution, both sides: not done.
- The plain Hebrew lines are unread: image quality and a need for a Hebrew palaeographer, to be tried first.
- The glyph block has no transcription alphabet yet.

## Escalation

Not yet reached (section 0a of the writeup skill): sibling fragments in the same Taylor-Schechter group, other Geniza
glyph ciphers (T-S NS J479 and Elbaum's annotated alphabet, T-S K5.7, K24.24), and contact with Alan Elbaum (Princeton Geniza Project)
and Gideon Bohak, who work on the Geniza cipher material. Coordinate with them before anything is published or sent.
