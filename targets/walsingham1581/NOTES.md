# Walsingham's enclosure to John Somer, 21 July 1581 — TNA SP 53/11 no. 50

Status: in progress. Not read (14 Nov 2026): the published key decodes the enclosure through a label concordance, three of thirteen sentences hold, the rest break on the key's unknown signs. Solved by Biermann and Lasry in 2023; their plaintext is unpublished.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): the folder holds the numeric ciphertext and the one-clause opening Tomokiyo published; the Biermann-Lasry plaintext is unpublished. no. 50I is *decoded, not read* (excerpt only) in profile.json; class already solved is kept; fraction_read 0.09 marked estimated.

**23 Oct 2026, re-read** (REREAD_BRIEF batch b37, Claude Opus 5.5): **concordance built, still decoded, not read.**
Tomokiyo's numeric labels cannot take his published opening one value per label (crib search, none found): his
transcription merges look-alike glyphs. A label-to-glyph concordance was therefore built on the f. 138 image line by
line with his glyph key (`texts/no50I_concordance.tsv`; lines 1-10 checked, 11-14 in part); the opening comes out
exactly. Decode `texts/no50I_decode.txt` (`research/reading_audit/b37_wals_dec.py`); partial reading
`texts/no50I_reading.md` / `_en.md`: the bearer, Shrewsbury's servant, is to pass in a captain's caravel to buy hawks
and has offered to carry the packet; "I durst vryte nothing of importance be him"; "You may sovnd and try him, and be
him send me ansver"; "that there be nothing aganist [58] and [95] stait [49] the realme ... vhitner [72] the present
pacqvet ... cvm to [87] handis vel closit or not". 0.154 clean sentences on explicit holes: 20 labels have no value
(seven are the key's own unknowns). Log: `texts/no50I_reread_log.md`.

**23 Oct 2026, r2k (lines 11-14 checked):** the last four lines (141 tokens) compared glyph by glyph with the
concordance on the full-size DECODE R3839 P3 image (3567 px; no larger TNA image is freely available), each sloping
line cropped on its own centre at 3x. Settled from the key's glyphs: 49 = OF (the OF glyph), 59 = *m* (#, *realme*),
72 = null, 87 = YOUR; 95 is a lone dot, not a sign; 58 is the key's own queried "THE QUEEN?" sign, kept [?the Queen].
Three look-alike labels corrected by position (`texts/no50I_position_corrections.tsv`); 14:14 is *n*, not *h*, which
gives "sealed of the *vnicorne*" (the unicorn seal). The tail reads: "that ther be nothing aganist [?the Queen] and
stait of the realme. And fayle not to advertis me vhitner the present pacqvet and [?is] cvm to your handis vel closit
or not, [91] [?hardvam] and sealed of the vnicorne". Decoder `research/reading_audit/r2k_wals_dec.py`. Score
unchanged (0.154 explicit holes): the holes are in lines 2-10. Still decoded, not read.

Earlier status (before the 22 Oct 2026 reading audit): no write-up (found already solved: Biermann and Lasry 2023, published by Tomokiyo on 16 Sept 2026; checked here 23 Sept 2026, nothing added beyond the check; catalogue item 296 removed 10 Oct 2026)

## Outcome (checked 23 September 2026)

**Previously solved in part; external read found.** Norbert Biermann and George Lasry solved the cipher in 2023. Satoshi Tomokiyo first published the result on **16 September 2026**, six days before the tracker entry that called it unread. His [solution page](https://cryptiana.web.fc2.com/code/mary3.htm) gives the opening as:

> “The beirar is domestik servand to the erle of shrevisbvry”

The source prints two underscores before this opening and says that some symbols remain unidentified. Its [reconstructed glyph key](https://cryptiana.web.fc2.com/code/mary_sp53_11_50b.png) identifies letters, whole-word signs, and nulls, but supplies no concordance from the numeric labels in its [transcription](https://cryptiana.web.fc2.com/code/SP53_11_50b.txt) to those glyphs. I cannot verify a continuous reading beyond the quoted opening. The author and recipient of the enclosed note are not established by the cover; its date is no later than Walsingham's cover letter. The language of the verified plaintext is Scots-inflected English, not French.

This is **not a new decipherment**. Credit the 2023 solution to Biermann and Lasry, published by Tomokiyo in 2026. The present work found and checked that publication, isolated the manuscript and tested whether the read could be extended reliably.

## Record anatomy and sources

- [DECODE R3839](https://de-crypt.org/decrypt-web/RecordsView/3839) contains Walsingham's English cover (the local `IMG_R3839_I23203_P1.jpg`, folio 132) and the cipher enclosure (`IMG_R3839_I23203_P3.jpg`, folio 138; enlarged as `cipher_f138.png`). Its second scan is a blank/backing or intermediate view. The enclosure has 14 lines; Tomokiyo's semicolon-separated file has **562 tokens and 78 distinct numeric glyph labels** after excluding its header and final empty line.
- The cover is dated London, **21 July 1581**, to **John Somer(s)**. [*Calendar of State Papers, Scotland*, vol. 6, item 45](CSP_Scotland_v6_1581-1583.pdf) says the cipher was found in an intercepted letter of Mary, Queen of Scots. Walsingham had first given it to his servant Philips, who was seriously ill, and Elizabeth wanted Somer to work on it before Walsingham left for Paris. The calendar describes the enclosure as a cipher letter for which there was no key. This is evidence about the 1581 investigators' starting point, not evidence that no modern solution exists.
- [DECODE R3840](https://de-crypt.org/decrypt-web/RecordsView/3840) is a different nearby item: readable extracts from Mary's letters and an Italian letter, corresponding to the calendar's July 26–28 entries 46–47. It is not the ciphertext.
- The L'Abbadia material is separate. Tomokiyo's [earlier inventory](https://cryptiana.web.fc2.com/code/mary.htm) identifies SP 53/11 no. 35 as Somer's deciphering worksheet, with its key on folio 39. It does not supply this enclosure's key. Our local `IMG_R3838_I23200_P1.jpg` and `P2.jpg` preserve the nearby worksheet/key scans.

## Attempts to extend the read

I inspected the original cipher image, the 2026 reconstructed key, Tomokiyo's numeric transcription, nearby SP 53/23 key scans, and the [2023 study of Mary's Castelnau cipher](https://www.tandfonline.com/doi/full/10.1080/01611194.2022.2160677). The Castelnau and Mary–Beaton tables belong to other alphabets; several of this enclosure's common glyphs do not match those tables as homophones. The 2026 key is specific to this enclosure. The long French dowry instructions dated 10 July in Labanoff, vol. 5, are not a plaintext mate for this brief Scots-English note.

Before finding the newly published solution, French 5-gram homophonic annealing (48 restarts × 10 million iterations) produced fluent-looking nonsense, not a read. A rare-word-sign pass likewise produced nonsense; a later English pass became degenerate under the calendar-trained model. These runs have **no evidential value against** the published solution. They do demonstrate why assigning the remaining label values from an unconstrained language score would be unsafe.

I tried to align the published opening and key against a segmented high-resolution first line (`segment_line.py` / `line1_segments.png`). The page's 562 tokens use arbitrary numeric labels, while the key shows graphical shapes only. Several adjacent marks touch and a few signs are still unknown even in the published key. Without a checked glyph-to-label concordance, the short opening does not uniquely determine the rest; I did not turn plausible fragments into claimed plaintext.

## Reproducible route to a complete read

1. Obtain the Biermann–Lasry machine-readable key or a glyph-to-number concordance for Tomokiyo's transcription, if one exists; otherwise align each glyph label to repeated manuscript samples on folio 138 and the published key. Verify each mapping against multiple occurrences, keeping all uncertain assignments marked.
2. Apply only verified mappings to all 562 tokens, preserving the 14 manuscript lines and marking unknowns, nulls, and word signs separately. Use the quoted opening as a check, not as a forced crib.
3. Resolve residual signs from repeated contexts and the original scan. Compare any resulting full text against contemporary copies before assigning an author, recipient, or exact date.

The case should leave the “still unread” queue. Its accurate status is **solved in part in 2023, published 2026; full plaintext not published or independently verified here**. The original tracker fields “Portugal → France” and “French” came from the unrelated L'Abbadia item and should be removed.

## 14 Nov 2026: classed not read

Audit section J: the target's only document is *decoded, not read*, so the target is not a reading. Tried first
(`texts/no50I_reread_log.md`, section "14 Nov 2026"): cryptiana re-fetched (unchanged, opening clause only); the DECODE
R3839 image is behind a login (the public API marks the ciphertext private), so no glyph was checked; three proposals
from context (91 = WITH, 43 = WHICH, *vhtil I*) noted and not adopted. Nothing lifted.

`profile.json`: class `not read` (was already solved), method `read with known key` (was read from existing
decipherment: no full decipherment is in hand, only Tomokiyo's published key and opening clause; the key was applied
through the concordance of 23 Oct), fraction_read 0 (was 0.09 estimated). That Biermann and Lasry solved it in 2023
stays in the credits and in `method_basis`.

## Remaining gaps

- no. 50I: 14 signs without a value (labels 07, 09, 39, 44, 46, 77, 79, 82, 86, 89, 91, 92, 97, 98) and the Γ-like sign at 13:9 - blocker: no-key-material; most are the unknown signs of the published key; all 14 lines now checked on the image (49, 58, 59, 72, 87, 95 settled 23 Oct 2026, r2k); the Biermann-Lasry plaintext is unpublished (ask Lasry)
- no. 50I lines 2-10: words resting on merged labels (10 b/k, 35 null/d, 13 l/w) and the open signs keep the reading at 0.154 - blocker: no-key-material; lines 11-14 closed 23 Oct 2026 (r2k): checked glyph by glyph, the tail reads

## Escalation

- [x] siblings: SP 53/11 no. 35 (Somer's worksheet) and the SP 53/23 keys checked; other alphabets
- [n/a] clear-pages: none with the enclosure
- [x] known-keys: the Castelnau and Mary-Beaton tables do not fit; Tomokiyo's 2026 glyph key does
- [x] print: Tomokiyo, cryptiana mary3.htm (16 Sept 2026)
- [x] key-rebuild: glyph-to-label concordance built 23 Oct 2026 (b37), lines 1-10 checked; 20 signs open
- [x] retry: 23 Oct 2026 (b37) all 562 tokens decoded through the concordance; partial reading 0.154
- [x] retry: 14 Nov 2026 the decode re-read without the image (login); three context proposals, none adopted; classed not read
- [x] retry: 23 Oct 2026 (r2k) lines 11-14 checked glyph by glyph on the full DECODE image; six labels settled, three position corrections; still 0.154
