# Selected Eckert telegrams: local contribution edition, 12 November 2026

This addition applies surviving keys per message, preserves complete source lines, and collates prior printed readings. It does not claim to solve the entire Eckert corpus or recover previously unknown historical plaintext. Prepared by **Andrew Beling (`ajbeling`) with OpenAI Codex AI agents**. Prior work by WAINUT (`lccompany`), William Echols on the separate 1862 filling, period operators, and the Decoding the Civil War volunteer transcribers is retained and credited. Huntington holds and digitized the manuscripts.

| Item | Cipher | Line-by-line literal | Full-length English reading, with gaps | Apparatus |
|---|---|---|---|---|
| U1, p4 | [source](transcription/U1.txt) | [literal](decoded/U1.txt) | [reading](reading/U1.md) | [notes](reading/U1_notes.md), [source discussion](U1_reading.md) |
| U2, p6 | [source](transcription/U2.txt) | [literal](decoded/U2.txt) | [reading](reading/U2.md) | [notes](reading/U2_notes.md), [source discussion](U2_reading.md) |
| U3, p7 | [source](transcription/U3.txt) | [literal](decoded/U3.txt) | [partial clear frame](reading/U3.md) | [notes](reading/U3_notes.md), [No.10 search](U3_search.md) |
| McPhail, pp9–10 | [source](transcription/McPhail.txt) | [literal](decoded/McPhail.txt) | [reading with holes](reading/McPhail.md) | [notes](reading/McPhail_notes.md), [source discussion](McPhail_reading.md) |
| Halleck to Grant, p10 | [source](transcription/Grant.txt) | [literal](decoded/Grant.txt) | [reading](reading/Grant.md) | [notes](reading/Grant_notes.md), [print witnesses](printed_parallels.md) |

All 65 source lines are retained, including operator headings and possible post-signature check wording. The reading body excludes those separately documented headings/check tails from its word denominator; it does not quietly decipher them. English needs no separate translation. Body conjectures remain holes. U2 retains one body hole, McPhail five, and U3 six. U3's six unresolved words are ciphertext labels, not reconstructed ranks/names. `reading_metrics.json` gives every reproducible denominator and count, not a whole-ledger success percentage.

## What changes

- U1 uses No.2, with World corrected and Tobsy/Topsy = 12:30 P.M.; Book1 Topsy would give midnight.
- U2 uses No.1 for four heading/address values; its body was already clear. Unity stays unresolved.
- McPhail and the Grant telegram use No.2. The full McPhail wrappers and forwarding request are included.
- **Three McPhail witnesses:** ledger/No.2 Java = Johnston; OR I/32 II p394 also Johnston, while OR I/33 p559 prints Beauregard. The two print versions also differ on Greer's/Green's and Hoke. Both print versions still differ from the ledger's 700 infantry at Hanover Junction. See [print collation](printed_parallels.md).
- The Grant telegram restores omitted Grant but preserves Elliotts against OR's Ellet's, plus two printed additions. Primary p407 verification is now complete; the older independent review correctly describes its earlier, narrower boundary.

The subsequent Stager register sweep inspected every digitized locality/account page. It found a No.10 custody trail through Baldwin/Baltimore and Culgan → David/Pittsburgh, but no vocabulary or direct locator. The 1865–1867 register cannot by itself establish U3’s February1864 codeword values. Evidence and retrieval hashes are linked in [U3_search.md](U3_search.md).

## Corrections and unresolved readings

| Item/line | Earlier transcript | Edition | Evidence/status |
|---|---|---|---|
| U1 L3 | Word | World | p4 image8896; No.2 World/West |
| U2 L1 | Beckmith | Beckwith | p6 image8898, operator name |
| U2 L2–3 | Ma / Callum | Mc / Callum | p6 image8898; normalized McCallum in reading |
| McPhail L10 | Snake Pine Talbot | Snake Peru Talbot | p9 image8901; No.2 Peru/Army |
| Grant L2 | For Tulip | For Grant Tulip | p10 image8902; omitted plain Grant restored |
| U1 L6, McPhail L2 | Tobsy | kept in cipher; Topsy mapping | explicit spelling variant, No.2 time page |
| McPhail L10 | Prove | kept; [?provost] in reading | contextual abbreviation proposal |
| McPhail L22 | Greers | kept; [?Greers] in reading | handwriting uncertain; p394 Greer's [?], p559 Green's |
| McPhail L26 | Allen | kept; [?one] in reading | Alton/one exists in numeral table, but repair is unproved |
| McPhail L36 | Dusty | kept; [?forage] in reading | Rusty/forage in key, R/D-like initial and printed parallels |
| McPhail L2 | whims | kept and marked hole | no verified selected-key value |
| U2 L3 | unity | kept and marked hole | punctuation/check function not proved |
| Grant L5 | Elliotts | kept; Elliott's normalized punctuation | plain name; not the numeric code Elliott; print Ellet's |

Ordinary word divisions (`Cleve = land`, `be = sides`, etc.) are joined in readings, and punctuation/numeric constructions are normalized. No missing General, Hoke, eighty, Maryland Line, or by the Government is supplied to make the ledger agree with print. `soon as possible` and `had ... had` remain without silent idiomatic repair.

## Reproduce

From the repository root:

```sh
python3 -I targets/eckert1862/addition_2026-11-12/decode_selected.py
python3 -I targets/eckert1862/addition_2026-11-12/decode_complete.py
python3 -I targets/eckert1862/addition_2026-11-12/measure_readings.py
python3 -I docs/_check_profile.py eckert1862
python3 -I docs/_check_reading.py eckert1862
```

The decoder uses only the standard library. The last reading checks require NumPy through the repository's language module. `decode_selected.py` is the prior decoder with only its raw-data path made relative; it must reproduce its two recorded hashes. `decode_complete.py` first verifies `INPUT_SHA256SUMS`, then writes 179 substitutions: all175 prior tuples in order plus four No.1 entries. It checks Java/Johnston, Ink/Beauregard, the No.2 time, restored Grant, plain Elliotts, and untouched unresolved/check tokens. Key entries total112 for No.2 and four selected No.1 entries, not entire codebooks. `applied_complete.tsv` supplies a page and derivation classification per match. Unmatched words are not automatically certified clear.

Sources have retrieval URLs and hashes in `source_records/SOURCE_URLS.tsv` and `U3_SOURCE_URLS.tsv`; unchanged volunteer p9/p10 JSON is included. Large images remain outside git. `REVIEW.md` is a dated context-aware review by a separate AI agent working for this contribution (not an independent or human check), not a blind test or external human verification; its original scope is preserved. The accompanying updated `verification.json` explicitly records the later p407 and p394 print checks. Source/raw originals and previous repository files are not overwritten.

Remaining barriers: U3 needs a verified No.10 filling or an exact period plaintext; five McPhail words, unity, and check-tail interpretation remain uncertain; most ledger pages are unattempted. [U3_search.md](U3_search.md) states what was actually checked and what remains available or access-limited. No publication, commit, push or PR has been made.
