# Catalogue 2533: the cipher opening in Johan van Ewsum's register (Groninger Archieven 696 inv. 595)

Contributor: lccompany (WAINUT), 12 Nov 2026. Work by AI language-model agents under WAINUT's rules; no human
palaeographer has checked the text.

## Document

- Groninger Archieven, 696 Familie van Ewsum, inv. nr. 595 (old order 136II): register of land rents and debts of
  Johan van Ewsum, 1533-1557. One opening in cipher, scan 193 of 199; the same opening is photographed again as scan 1
  (a different photograph; full sizes 2615 x 3525 px for scan 1 and 3130 x 3540 px for scan 193; see Images for the
  size of the copies used).
- Left page: the key (two lines, clear letters over signs), a three-line note in clear Dutch, then 23 lines of cipher.
  Right page: 6 lines of cipher, a 3-line block set off by a vertical stroke, a rule, one line of cipher words between
  colons, and the clear Latin caption "ad perforandum caput gallinae".
- The note under the key, in clear: *Vm dat woert tho breke mach men dese caracter [venus sign] int midde offt vpt
  ende sette* ("to break up the word one may set this character in the middle or at the end"): a null.
- Not dated on the page; the text gives only "decima Ivly" (10 July). The cipher names "Hacfort", "Meynert van Ham",
  "Iorien Schenck", "Wedde" and a truce with "den Stichschen steden". Identified by the contributor (inferred, not
  given by the text) as Berend van Hackfort, who held the house of Wedde from 1530; Meinert van Ham, the Guelders
  commander in the Ommelanden in 1536 until Heiligerlee; and probably Georg Schenck van Toutenburg. On those
  identifications the opening falls in the Guelders years of Groningen, probably 1533-1536; this range has not been
  checked against Meinert van Ham's dated career or against the dated truces with the Sticht (see Remaining gaps).
  The slug `ewsum1535` is a placeholder for that range.

## System

Simple substitution with word division kept. `key.tsv` and `key_frozen.tsv` hold the same 23 entries (22 letter
signs and the null; the files have 26 and 25 lines with their comment and header lines). 22 signs for a-y (no j, u, x, z; `v` serves for u, `w` once for u in
*terstwnt*), plus the venus sign as a null (9 times in the text, inside or at the end of words, as the note says).
The writer marks a word carried over to the next line with `//`. A few groups are struck out under ink blots.

## Key source and held-out test

The key is the writer's own, on the same page: each of the 23 entries in `key.tsv` is read from the key lines, none was set from
the cipher text, and the file was frozen (`key_frozen.tsv`) before the first decryption run. The whole cipher text is
therefore held out from the key. Result with the frozen key, unchanged: 120 of 123 cipher words (97.6%) decrypt
mechanically to words of the period language; the other three are one omitted letter (*knech{+t}en*, where L13 spells
*knechten*) and two signs under blots. No sign of the text is missing from the key, and no key value had to be
changed. An internal check: the writer repeats the clause *ind raitslagen woe gy die veylich averkrigen* (L08-L09 and
L10-L11); the two copies were transcribed separately and give the same 35 signs.

## Transcription

Sign conventions (`SIGN_CONVENTIONS.md`) were written before any value was applied. Pass 1 on scan 193 (strips at
1.4x), pass 2 on scan 1 (fresh strips at 1.6x). They differed in 4 places, settled on scan 193 at 3x (listed at the head
of `transcription_ewsum.txt`): two struck groups, one blotted final sign (L12, a double cross, not a star), and one
group (L18, one lying eight, not two).

## Reading

`reading_ewsum.md` (marked text and the text as sentences), `translation_ewsum.md` (English).
`scripts/check_marks.py` rebuilds `decryption_ewsum.txt` from the transcription and the frozen key and fails on any
unmarked departure in the reading: PASS. Word count: 123 cipher words; 120 verbatim from the signs, 1 with a marked
repair, 0 guesses, 2 holes (the blotted last letter of *ambasiate[n]*, one blotted sign in *be[...]lo*). Counting
rule: a word with a sign under a blot is counted as a hole even where the reading proposes a letter for it, so the
L03 mark `[?ambasiaten=ambasiate?]` (a guess for the blotted letter) is counted once, as a hole, not also as a
guess. Struck groups are not counted.

The text is not a recipe, as the catalogue guessed from the facing page. It holds:

- **A.** A letter to "good friends": the soldiers' pay arrived yesterday with the envoys and Hendricus; send the
  account and receipt at once and see how you can get it over safely; about twenty soldiers who were out with the
  colonels could be used for it as well, so that at Wedde on 10 July the envoy and those not covered by the payment
  are summoned.
- **B.** A note to "Heer Drost", signed Hendricus: the truce between "my gracious lords" and the cities of the Sticht
  has been extended by a month, but Jorien Schenck (probably Georg Schenck van Toutenburg) will not keep to it, so travelling over the open country
  will be dangerous.
- **C.** An address set off by a stroke: "Aen Hacfort ind Meynert van Ham, averste" (to Hackfort and Meinert van Ham,
  colonel(s)).
- **D.** Under a rule, between colons: *ergo : tergo : be[...]lo*, followed by the clear Latin caption "ad
  perforandum caput gallinae". This looks like a charm or trick formula and is not part of the letter.

Proposed state: **read**. 120 of the 123 words are read from the signs and the other 3 are marked; the sentences are coherent
Low Saxon. Two renderings are doubtful in sense, not in the signs: *sich verechtert hebben* (L14-L15, "have fallen
behind"?) and the syntax of L17-L20 (*dat vm Wedde decima Ivly die ambasiat en nyet van der betalonge syen werden
ontbaden*).

### Dan's reading checker

`docs/_check_reading.py --file` (origin/main of 12 Nov 2026, run in a throwaway worktree): reading_ewsum.md clean
share 0.571 (77 sentences, language picked by the checker: fr); decryption_ewsum.txt 0.400 (de); translation_ewsum.md
0.714 (en; 0.684 before the doubtful L17-L20 rendering was marked [?] after the review).
On the sentence section alone: 0.167 (auto), 0.0 with nl or de fixed. The low figures come from the word lists, not
the text: the nl list does not know *gecomen*, *heren*, *lant*, *alhier*, *bestant* or *drost*, and none of the lists
covers 16th-century Low Saxon spelling (*vrvnden*, *averkrigen*, *raitslagen*, *nyet*). The checker cannot score
this language; a human reader of Middle Low German or Middle Dutch should judge the sentences.

## Prior art (checked 12 Nov 2026)

- Catalogue vetting of 11 Nov 2026: DECODE (Ewsum, Groningen: 0 records), cryptiana (0 hits), Perton 2017 and
  Kluyver 1900 opened, no reading of this cipher.
- Web search 12 Nov 2026 for *van Ewsum geheimschrift* with the Latin caption: nothing on this item.
- Web search 12 Nov 2026 for Meinert van Ham, Hackfort, Schenck and Ewsum: background only (Wikipedia, Meindert van
  Ham; local history of Wedde and Hackfort); no edition or reading of this text.
- Rutgers' 1899 inventory of the Ewsum archive not opened.

## Images

- Viewer: https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=5&miview=inv2&milang=nl&micode=696&mizk_alle=geheimschrift
  (item 595, scans 1 and 193).
- Full images from the archive's IIP server (what the viewer loads), fetched once each on 12 Nov 2026:
  scan 193 `https://preserve3.archieven.nl/iipsrv/iipsrv12.fcgi?FIF=cache/fonc-gra/dcec8ad18e86a6bdba5df6e9c6d4cf22.jp2&WID=3130&CVT=jpeg`,
  scan 1 `https://preserve3.archieven.nl/iipsrv/iipsrv12.fcgi?FIF=cache/fonc-gra/984e29d787f122088505b7922bb8bfb9.jp2&WID=2615&CVT=jpeg`.
  These requests returned copies of 2653 x 3000 px (scan 193) and 2225 x 3000 px (scan 1), apparently scaled by the
  server to at most 3000 px; the transcription and the crops were made on these copies, not on the full 3130 x 3540
  and 2615 x 3525 px images. The cache names come from the viewer (`scripts/anl_probe.py`, a port of the sweep's `anl_view2.js` that logs image
  requests) and may change. Scans are not in this folder.

## Remaining gaps

- Two blotted signs: the last letter of *ambasiate-* (L03) and the third sign of *be[...]lo* (R10); struck groups in
  L04, L11, L17 and R10 not read.
- Sense of *sich verechtert hebben* and of the clause L17-L20; a reader of Middle Low German should check. The
  reviewer noted that the English for L17-L20 ("the envoy and those who are not [included] in the payment") supplies
  more than the words carry; it is now marked [?] in `translation_ewsum.md`.
- Who wrote it: "Hendricus" signs note B; whether the opening is Johan van Ewsum's copy of intercepted or received
  letters, drafts, or a cipher exercise is not settled. The "Heer Drost" is not identified.
- Date: probably 1533-1536 from the persons named, on the contributor's identifications; not yet checked against
  Meinert van Ham's dated career or the dated truces between the Guelders side and the Oversticht/Sticht cities
  (raised by the reviewer). The July of the letter and the one-month truce extension were not matched to a dated
  event. The slug is a placeholder.
- Whether A-C are one letter with its address or two pieces to different people is open; they are kept together here
  because they share one opening and one key.
- The rest of the register was paged through in the 11 Nov sweep at contact-sheet size only (no other cipher found).
