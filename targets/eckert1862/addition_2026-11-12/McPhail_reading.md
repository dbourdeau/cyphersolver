# McPhail report, 14–15 February 1864: No. 2 and textual variants

Huntington mssEC 19 pp. 9–10, images [8901](https://hdl.huntington.org/digital/collection/p16003coll11/id/8901) and [8902](https://hdl.huntington.org/digital/collection/p16003coll11/id/8902). Header: S. H. Beckwith, “2”, Washington 15 February 1864. The report quoted inside is dated Baltimore 14 February. Root inspected both images and Cipher Book No. 2, mssEC 47. The key works in normal ledger reading order; no route reversal is needed at this stage.

Status: **read in substantial part with an extant key; already published clear in OR I/33 p.559**. This is not a previously unknown intelligence report. The codebook match and documented variants are the contribution. The printed page and a second No. 2 key copy were visually checked. Both key copies (mssEC47 and mssEC48, p17) read **Java = Johnston**, with **Ink = Beauregard** separately above it. This is a textual discrepancy, not proof of which officer's actual strength the informant meant.

`literal_selected.txt` preserves every source line and partial-key substitution; `applied_key_ledger.tsv` gives the key page for each match. Unmatched words are not automatically certified clear. Source JSON is the volunteers' transcript, retained unchanged. Explicit image corrections: p9 `Pine` → **Peru** (Army); p10 omitted **Grant** restored in “For Grant Tulip.” No dictionary values were invented from the OR text.

## Readable report

The outer message is forwarded for Grant and Schofield by order of the Secretary of War. It quotes cipher operator Baldwin explaining that McPhail obtained the information at Colonel Sharpe's request, by sending a reliable man as a blockade runner. An outer `whims` word remains unresolved; “telegrams” is plausible context, but not a verified entry in the extracted key.

The quoted report, with punctuation and numerals normalized:

> Fifteen thousand between Weldon and Wilmington, said to attack New Berne, but thought to overawe the Union sentiment. General Pickett's forces all in North Carolina. Beauregard, nineteen thousand all told in and about Charleston. No troops left **Johnston** except those on furlough; he has thirty-five thousand men. Longstreet has twenty thousand; has moved his headquarters to Morristown; seven thousand of his men are shoeless. Five companies of heavy artillery in the defences of Richmond; four light batteries; two companies cavalry; one hundred twenty [Greers/Greys?] men; City Battalion, six hundred forty men; four thousand citizen soldiers could be turned out. Four hundred cavalry on the Chickahominy between James and York rivers. **Seven hundred infantry** at Hanover Junction. Lee had [one?; ledger Allen] month ago had forty-six thousand, besides cavalry. [A] brigade, seventeen hundred, left for North Carolina; six thousand furloughed. Has now thirty-five thousand. Hampton's cavalry, six thousand, and Lomax's brigade of Fitz Hugh Lee's division, sixteen hundred, are all the cavalry Lee has. Fitz Lee disbanded four thousand for want of [forage?]. Signed, J. L. McPhail. Please forward copy to Schofield.

The final “forage” is supported by key **Rusty = Forage**, p21, and by the printed parallel. The source initial is R/D-like and volunteers read `Dusty`; preserve this as an explicit proposed transcription repair, not a new Dusty mapping. Likewise `Allen` may be a copied/volunteer form of numeral **Alton = 1**, but it is not silently changed in the literal output.

## Differences from the printed witness

| Location | Ledger/key reading | OR I/33 p559 |
|---|---|---|
| Officer after “No troops left” | Java = Johnston, confirmed in two keys | Beauregard |
| Hanover Junction | Cushing Snyder Star = seven hundred infantry | seven hundred and eighty Maryland Line |
| Brigade sent to North Carolina | no visible “Hoke” in the copied line; Palmetto Lewis Smith = brigade 1700 | Hoke's brigade (1700) |
| Personal/unit name after 120 | Greers/Greys uncertain handwriting | Green's men |
| Final want of supplies | Rusty/Dusty, proposed forage from key and parallel | forage |

These variants argue for preserving both witnesses. Do not rewrite the cipher to agree with OR or describe the OR version as definitively erroneous without checking its manuscript source.

## Second telegram on p.10

16 February 1864, 3:30 p.m., to Grant, signed Halleck:

> It is deemed important that leased plantations on the Mississippi River receive due protection, and the Secretary of War desires that General Elliott's Marine Brigade be assigned to that service. It is understood that it has been so assigned temporarily by Sherman.

The source has “For Grant” although the volunteer JSON omits Grant. Key entries Republic/important, Agnew/Mississippi, Wafer/river, Costume/Secretary of War, Spark/general, Summit/marine, Palmyra/brigade, Fortune/Sherman and Lady/Halleck are directly image-read. `Elliotts` is the plain name in the source, not the numeral code Elliott. The trailing “How you make it go” is retained as check/null material.

**Prior-publication update:** the matching message is indexed in a [reproduction of OR series I, volume XXXII, part II, p407](https://www.civilwar.com/battles/923-official-record/series/volume/campaign/forrest-s-expedition-part-ii/202575-407-series-i-volume-xxxii-ii-serial-58-forrest-s-expedition-part-ii.html), with the same date and time. That text has “by the Government” after important, “Ellet's” instead of ledger `Elliotts`, and “General Sherman.” Keep these witness differences; do not silently rewrite the ledger. The coordinator subsequently downloaded and visually checked the original printed p407 from [the digitized volume](https://archive.org/details/warofrebellion013202rootrich/page/n415/mode/1up). It confirms all three variants and the date/time. The scan is `sources/raw/english_conflict_survey_2026-11-12/or32ii_p407.jpg`; OCR object 414 maps to image leaf415 (leaf414 is printed p406, also retained). Metadata and the page-mapped OCR are preserved with source URLs and hashes. This closes the earlier primary-print verification gap.

Credit remains with Huntington, the period correspondents/operators, the OR editors, Decoding the Civil War's volunteer transcribers, and WAINUT's earlier repository work. We add the No. 2 application, source corrections, and collation. This was exploratory and not a fresh blind key test.


## Additional printed witness verified during portable packaging

OR I/32 part II **p394** also prints this McPhail report. Its print image has now been visually checked:
**Johnston**, **Greer's [?]**, and no **Hoke**. Thus the ledger/No.2 reading agrees with one printed version on
Johnston, while OR I/33 p559 reads Beauregard. Both print versions nevertheless give 780 Maryland Line at
Hanover Junction against the ledger's 700 infantry. See `printed_parallels.md` for the three-witness comparison,
OCR extracts and print-error distinctions. The printed p394 redundant "35,000 thousand" is retained as a print
variant, not carried into the ledger. This additional witness does not settle which report was historically accurate.
