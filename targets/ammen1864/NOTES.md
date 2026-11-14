# ammen1864: Headquarters Department of the Ohio to Brig. Gen. Ammen, Knoxville, 29 Sept 1864, "Dispatch in cypher": Union route cipher

Status: in progress (integration check, 14 Nov 2026: read in part, 83 of 90 words sure = 92.2% by the README rule: the three code words whose value comes only from the printed text, the probable "was = forces", the unresolved "rig" and the two initials emended from the grid ("or" = N., "T." = L.) are holes. The contributor counted the two emended initials as sure: 85 of 90 = 94.4%. The code words can still be looked for in the Union cipher books, so no page yet.)

Contributor's status: read in part by the strict count (85 of 90 words sure; contributed by Brice Dudout, Europe chiffree, with a Claude Opus 5.5 agent; 3 Nov 2026). The content is EXISTING (printed in the Official Records); not a new text. Not in catalogue.json or targets. Daniel has it as leads 1432 and 2097 ("Coded letter from unknown author to Jacob Ammen", the leads date it 29 Sep 1862: the sheet itself says "Sept. 29 '64"; the two leads are one object). Daniel's vetting of lead 1432 (4 Nov 2026) already corrects the date and cites the Official Records page.

## Document
Henry County Historical Society (New Castle, Indiana), Ammen Civil War Collection, digitised by Ball State University Digital Media Repository, collection LSTACivWar, compound object 2072 (pages 2070 = HCHS_L_18640929_01, 2071 = docket "No signature / Dispatch in cypher"). Rights statement NoC-US 1.0; commercial use subject to HCHS permission; watermarked. No image is included here. Author: Lt. Col. G. M. Bascom, A.A.G., for Maj. Gen. Schofield, Headquarters Department of the Ohio, Knoxville; relays Sherman's order of 28 Sept 1864 recalling Brig. Gen. Burbridge.

## System and key
Union route cipher of the Stager family: the plain words are written into two grids of 6 columns (8 rows for the relayed Sherman order, words 1-54; 7 rows for Schofield's own message, words 55-107) and sent by route: column 6 up, 1 down, 5 up, 2 down, 4 up, 3 down; "Friend" marks the start; one or two null words per column (now, men, send, news, freedom, quiet, how, G, Odd, I, not, hell, well, newer, are); code words for proper names (ink = Nashville, muscle = Sherman, maxim = Maj. Gen. Schofield, was = forces). key.json is that route and code list. A "54" is written at the foot of the sheet (end of the first grid).

## Reading
decryption.txt gives the sentence-by-sentence reconstruction and reading.md the reading: 85 of 90 words sure = 94.4 % (strict count), 86 with the probable "was = forces" (95.6 %); 3 code words restored from the printed text and 1 unresolved "rig" before "W. T. Sherman". Read: Recall General Burbridge with his forces to this city or the nearest convenient point on the Louisville and Nashville Railroad; forward the above to Burbridge, acknowledge receipt; "I do not know that he has this cypher."

## Validation
None in the held-out sense (frozen/PROTOCOL.md declares the standard criterion not applicable); one descriptive measure, 0.455 against 0.250 for 200 control routes, with the declared bias. See validation.txt.

## Prior art
Printed in clear: The War of the Rebellion, Official Records, series I, vol. XXXIX, part 2 (serial 78), p. 524 (Headquarters Department of the Ohio, Knoxville, 29 Sept 1864, to Brigadier-General Ammen, with Sherman's order of 28 Sept). The reconstruction was made with that text in view (found before the attempt, used as the check). Nothing else on this letter found.

## Remaining gaps

- Code words ink (Nashville), muscle (Sherman), maxim (Maj. Gen. Schofield) - blocker: not-attempted; their values rest on the Official Records text only; the Union cipher books of 1864 (Huntington Library, Eckert Papers, online; see targets/eckert1862) not yet searched for the book this dispatch used (book 1, mssEC43, has other values: Ink = President, Maxim = Gen. Gillmore/Boyle)
- "rig" before "W. T. Sherman" - blocker: not-attempted; written "rig." on the sheet (the r has the shape of this writer's r in "recall", "recd", "rail"); a code word, or a slip for "Sig." (signed), not decided; the same cipher books would settle it
- "was" = forces (probable) - blocker: not-attempted; as above
- word 17 "or" and word 21 "T." read as "N." and "L." (L. & N. rail road) - blocker: not-attempted; emendations from the grid and the printed text; the sheet has "or" and "T."
- Reuse rights of the images (HCHS / Ball State) unconfirmed; no image is reproduced

## Escalation

- [ ] siblings: other cipher dispatches in the Ammen collection not searched
- [x] clear-pages: the docket (page 2071, "No signature / Dispatch in cypher") read
- [ ] known-keys: the Union cipher books (Eckert Papers, Huntington; book 1 checked through targets/eckert1862: no match) not searched for ink, muscle, maxim, rig, was
- [x] print: Official Records I/39/2 p. 524 found (the clear text, paraphrased and cut short)
- [x] key-rebuild: the route is fully rebuilt (two grids of 6 columns; reproduced in the integration check)
- [ ] retry: after the cipher books

## Integration check (14 Nov 2026)

Verified for the maintainer before merging PR #562 (Brice Dudout). The PR carries no scripts; the checks below were made with a route decoder written for the check from key.json.

- **Image.** Ball State's CONTENTdm serves the page over IIIF with curl (`https://dmr.bsu.edu/iiif/2/LSTACivWar:2070/full/full/0/default.jpg`; the vetting of lead 1432 had found the host unreachable). All 107 words of the transcription compared with the image: all agree, including the interlinear "newer", the "54" at the foot and "rig." (as written).
- **Route.** Undoing the route of key.json (grid 1: 8 rows, columns 6 up, 1 down, 5 up, 2 down, 4 up, 3 down; grid 2: 7 rows, same route) on transcription.txt gives decryption.txt word for word. Seventeen words fall out as nulls or the commencement word: Friend, now, men, send, news, freedom, quiet, how, G, Odd, all, hell, I, not, well, newer, are (the null list in NOTES and reading.md has 15 and leaves out "all", token 72, which key.json does count as a null).
- **Count.** 90 words in the two grids, as stated. Strict: 83 sure (92.2%). Holes: ink, muscle, maxim (values from the printed text only), was (probable), rig (unresolved), and "or" = N., "T." = L. (emended). The contributor's count, 85 of 90 (94.4%), takes the two emended initials as sure. Either way under 95%: read in part.
- **Validation.** None: the protocol declared the standard test not applicable before the work (no held-out portion in a 107-word route), and the one descriptive measure carries a declared bias (blocks cut with the reconstruction). The route is accepted on the reading and on agreement with the printed text. Order of events by the contributor's record (hashes self-recorded; the frozen working files are not in the PR, so the SHA-256 list cannot be checked).
- **Outcome method.** "Key recovered based on plaintext from external sources" kept: the route was rebuilt with the Official Records text in view (found before the attempt). "Read from existing decipherment" does not fit: the printed text paraphrases and stops before the end, and nothing on the sheet deciphers it; "read with known key" does not fit: no route was on record for this dispatch.
- **One key, one entry.** A Union route cipher changes route and code words with the cipher book and the message; the other route-cipher folders (milroy, Stager No. 7 of 1861-62; eckert1862, the War Department ledgers; union1864, the NARA telegram books) are other books and other messages. Separate folder.
- **Leads.** Leads 1432 and 2097 are this sheet; their date fields (1862) set to 29 Sept 1864, and both point to this folder. Lead 1432's vetting (verdict read, 4 Nov 2026) already had the 1864 date and the Official Records page.
- **Checkers.** `_check_profile.py ammen1864`: valid. `_check_catalogue.py`: valid.
