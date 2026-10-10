# Walsingham's enclosure to John Somer, 21 July 1581 — TNA SP 53/11 no. 50

Status: no write-up (found already solved: Biermann and Lasry 2023, published by Tomokiyo on 16 Sept 2026; checked here 23 Sept 2026, nothing added beyond the check; catalogue item 296 removed 10 Oct 2026)

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
