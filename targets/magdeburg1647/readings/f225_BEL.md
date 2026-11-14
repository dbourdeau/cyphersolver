# No. 20: local reconciliation and reading package

All four blocks now have a conservative source transcript, complete A/B difference inventory, unchanged-key literal, and full line-by-line proposed German/Latin and English. There are 164 source rows: 160 cipher-bearing or mixed rows and four clear-only rows. No omitted-row placeholders are counted. The filename `settled` means a frozen adjudication stage; many glyphs and constructions remain unresolved. This is not a complete or independently human-verified decipherment.

| Group | Source | Rows | Cipher/mixed | Clear only | Main output |
|---|---|---:|---:|---:|---|
| n20a | 0256 right, 225r | 38 | 38 | 0 | n20a_settled_line_record.tsv |
| n20b | 0257/0258 left, 225v | 41 | 41 | 0 | n20b_settled_line_record.tsv |
| n20c | 0257/0258 right, 226r | 42 | 42 | 0 | n20c_settled_line_record.tsv |
| n20d | 0259 left top + right, 226v/227r | 43 | 39 | 4 | n20d_settled_line_record.tsv |

The four TSVs are in this `reading/` directory. Each has passage, line, literal, proposed German/Latin, English, and status. Each group also has `_settled_reading.md` for scope and caveats and `_settled_reconciliation.md` preserving the complete A/B texts, original notes, token differences, and selected shapes. Frozen glyph TSVs are in `transcription/`; mechanical literals in `mech/`; manifests in `log/`. Own scripts and crops are in `crops/n20_settled/`.

Source transcripts and reconciliation reports were frozen and hashed before each block's mechanical decoding. The documented worksheet key was applied unchanged, SHA-256 `4c4824b0fa67abd5c9c9278befb9ee4948890e68da3a835664d20f07c8e3478f`. No key fitting occurred. This third-reader reconciliation used both prior transcripts and the glyph sheet; later blocks were examined after the key had been read for n20d. It is not a blind third transcription. Original A/B files and notes still pass all 16 original manifest entries.

The language proposals are explicitly editorial. n20a–c bracket the entire proposed field, so every repair is declared even where a finer individual-character markup would be cumbersome. n20d brackets local repairs. Spacing, punctuation and capitalization are editorial in proposed fields. No language repair has been back-written into the frozen cipher text. Symbols retain descriptions, not assigned actor values. Their uncertain segmentation and relation to nearby letters remain part of the apparatus.

Apparent interlinear source wording “beyseit gesetzet” over 226v L08 and detached at L13 is separately identified; it is not used to repair cipher letters. Source-clear Bernar/B on 225v is distinguished from decoded words, with classification uncertainty retained. The uncertain interlinear group below raw 1870 remains unread. Raw numeral strings 92, 9879, 1870, 9896, and digit-like symbols are not converted into dates. No whole-text percentage or first-reading priority is claimed.

The coherent portions discuss negotiations, grievances, the Diet, voting and sovereign rights, religious and political liberty, restitution, a Hanover report and confidentiality, and cautious cooperation and credentials. These are proposed readings of continuous letter text, not secure identification of the actors behind the symbols. Weak clauses, source losses, proposed names and abbreviations remain marked in the line records.

## Verification actually run

From the project root:

```sh
python3 -I output/deep_2026-11-12/osnabrueck1647_cipheronly/crops/n20_settled/verify.py
```

Result: PASS; 47 source/reading manifest entries matched; all 164 mechanical literal rows reproduced exactly; row IDs, counts, copied literal columns and populated proposal/English fields matched. This verifies file integrity and deterministic substitution, not linguistic accuracy.

From the cipher-only root:

```sh
shasum -a 256 -c log/n20a_A.sha256 log/n20a_B.sha256 log/n20b_A.sha256 log/n20b_B.sha256 log/n20c_A.sha256 log/n20c_B.sha256 log/n20d_A.sha256 log/n20d_B.sha256
```

Result: all 16 original reader transcript/note entries OK. Each `log/n20[a-d]_settled.sha256` was also checked separately before decoding (7, 8, 8, and 7 entries respectively). No posting, commits, source-download changes or catalogue edits were made.

## Outstanding before a publishable contribution

A reviewer should compare the linguistic proposals to the source, especially glyphs selected from a scaffold despite live alternatives, resolve symbol identities against an independently checked key, inspect the marked gutter/strike/interlinear losses, and review German/Latin syntax and English clause connections. Dates and personal identifications need their own evidence. The package is concrete and reviewable, but hash-valid does not mean merge-ready or fully read.


---

# No.20 first page: provisional full line record

`n20a_settled_line_record.tsv` contains all38lines with untouched mechanical literal, a bracketed German/Latin reconstruction, and English. The **entire proposed field** is bracketed because numerous c/e,q/g,t/l and word-division repairs remain linguistic inference rather than a second image-verified alphabet. Internal brackets identify especially doubtful words, symbols and source numerals. This coarse repair convention is deliberately explicit; it does not imply that every letter inside the reconstruction was doubtful. Compare the literal column and complete A/B difference inventory for exact departures.

The page appears to introduce a discussion between two trusted people. Its mixed Latin/German text concerns the conduct of peace negotiations, grievances and the public Diet, rights of voting, moderation in raising controversial matters, the Peace of Prague (explicitly named in decoded letters), and failures or conditions of restitution. Württemberg, a fragment of Hildesheim, and a possible Wolfenbüttel fragment occur in the letter text; these are linguistic proposals, not external historical identifications. The anonymous symbols have not been assigned values here. Several clauses remain incomplete, especiallyL05,L19–20,L25,L33 and the subtitle's exact inflections.

Raw92,L02;9879,L14;and7,L34 are source numeral strings. They are not dates established by this reading. In particular, the surrounding word proposed as anno does not establish how9879 should be interpreted. No annex-based date or whole-text reading percentage is claimed.

The source is0256right. Full opening plus eight own strips were viewed. Selected strings retain uncertainty, and the preserved reader alternatives remain live even where a particular shape is selected. The source-stage freeze was verified before decoding using the unchanged worksheet key. Source-clear heading Extra seriem Discursus is separate from cipher subtitleL01. Margin text atL06 is included separately; apparent interlinear correction toL08 is uncertain. Original A/B records and raw downloads were not edited.

Verification from cipher-only root: `shasum -a 256 -c log/n20a_settled.sha256`. Decoder is `crops/n20_settled/decode.py` invoked with Python -I; it verifies the freeze before substitution, preserves clear/symbol spans, and refuses overwrites. No claim of complete decipherment, secure actor attribution or independent human review is made.


---

# No.20 second page: full provisional line record

The41-row`n20b_settled_line_record.tsv` provides literal output, bracketed proposed German/Latin and English for every source line. The entire reconstructed field is bracketed: it is a linguistic working proposal, not a replacement for frozen source glyphs. Every exact departure remains inspectable against the literal column and A/B reconciliation report. Nested question marks/uncertain labels identify especially weak places, not the full uncertainty of all editorial spelling repairs.

The most coherent sections concern political and religious liberty, restraint of interference, a report received from Hanover about an encounter, a request not to disseminate it with the correspondent's name, and confidential remarks about cooperation toward[Phi]. The wish that forces of all parties be led against “Christiani nominis hostem” is legible with ordinary look-alike repairs, but it does not by itself identify the opponent. Unvalued symbols prevent secure attribution of actors. “Iesuitis” is a proposed expansion of a damaged decoded aside, not independently established identification. The place-name proposals inL22 and religious wording inL20 likewise remain linguistic readings.

Source-clear Bernar atL04 and abbreviatedB atL06 are visually present in a larger Latin script; their clear-versus-code classification is provisional, and no full personal identity is assigned. Raw1870 atL20 is retained. The adjacent z?-shaped token may be cipher or numerals; interlinear strokes are??? and not the unverified16?5 reading of one witness. No year or dating follows from these strings. No whole-text percentage is claimed.

Source0257left was inspected as a full opening and eight own strips;0258full and three own details were checked for the name, numeral/interlinear passage and gutter endings. Many gutter losses and common shape ambiguities remain. The source-stage freeze was verified before mechanical substitution with the unchanged key; originalA/B and downloads are intact. Reproduce checks with `shasum -a 256 -c log/n20b_settled.sha256` from cipher-only root. The shared decoder verifies this freeze before substitution and preserves source-clear/symbol spans.


---

# No.20 third page: full provisional line record

All42source rows appear in`n20c_settled_line_record.tsv`, each with frozen mechanical literal, entirely bracketed German/Latin reconstruction, English and status. Bracketing the complete reconstruction is a coarse declaration that the language repairs have not been re-promoted to source glyph facts. Exact departures are visible in the literal column; especially weak clauses also carry internal doubts. No part of the English overrides the source record.

The strongest stretches concern avoiding excessive conditions/compensation, a proposed assembly and objections to its voting/procedure, flexible modes of negotiation, common and separate grievances, communications through representatives described as directors of the Hanseatic cities, and a language common to the participants. The concluding passage is cautious about giving an impression of excessive familiarity with the opposing party before the negotiations and a recommended cooperation are settled; it mentions letters of credence and discreet contacts. Actors remain hidden by unvalued symbols. The possible Pomerania name atL01 and rare word corycaeis atL40 are language proposals, not external identifications or independently confirmed readings.

The first and last clauses continue across page boundaries. L05–06about a free man/king/wounds/killing is linguistically recognisable but its construction is not securely resolved. L24andL29–31contain sign-dependent or damaged links. L41–42is particularly provisional. The four digit-like signs atL03remain descriptions; no date is inferred from them. No whole-text share-read percentage is claimed.

Both0257and0258openings were inspected, together with eight0257right strips and three0258right detail strips. A/B disagreements remain in full in the reconciliation report. Initials, letter/symbol ambiguity and blotted passages remain unresolved where necessary. No source changes were made after the source-stage freeze. The hash manifest was verified before substitution with the unchanged worksheet key. Originalreader files and downloads remain intact. Verify with`shasum -a 256 -c log/n20c_settled.sha256` from the cipher-only root.


---

# No.20 final pages: literal output and provisional reading

The full line record is `n20d_settled_line_record.tsv`:43rows, with frozen mechanical literal, proposed German/Latin, English and status for every line. The source reconciliation was frozen and verified before the worksheet key was applied. The key was neither changed nor fitted to this text.

The clearest continuous passage is227rL09–24: subjects contrasted with holders of rights of majesty; a reservation concerning embassies sent in the name of the whole imperium; fears of renewed attack after a settlement; restitution; and instructions concerning restoration to former integrity and defence of liberty. These are provisional linguistic readings of the letter substitution. Anonymous symbols still control many actors and grammatical links, so this is not a secure historical identification of who said or intended each thing.

226v is especially limited by gutter losses. It appears to turn from negotiations and invitations to the use of Latin and German in drafting projects. Source-clear “beyseit gesetzet” appears over226vL08 and again detached atL13. It is separately identified, not used to overwrite the mechanically decoded cipher. This could be a source editorial insertion, not an independent decipherment: its exact relation to the damaged cipher remains unresolved.

## Editorial rules and limits

- Every repair to the literal is square-bracketed in the proposed-language field. Brackets may enclose a letter, word or span. All such changes here are **linguistic proposals**, not newly source-verified corrections. Even ordinary-looking corrections (q→d, missing doubled consonants, q/g, t/l, inflection repairs) are not silently promoted into the frozen glyph record. `?` inside brackets marks particularly uncertain proposals.
- Mechanical literals, including apparent nonsense, remain untouched in a separate column. Spacing/capitalization/punctuation in the proposed column are editorial for readability. Hyphenated line continuations are editorial. No added decipherment for a symbol is claimed; symbol names in translation denote shapes only.
- Source-clear words in227rL25/L27–30 and226vL13 are transcription attempts, not decoded words. Their weak Kurrent readings remain bracketed or fragmentary. Proposed names such as Langenberg and weekday-like Monday are uncertain language guesses; no historical identification is established.
- The numeral9896 in227rL14 is simply retained. The proposed phrase around it resembles a restitution clause, but neither the numeral nor document dating has been resolved. No year is inferred from it or from the annex number.
- No whole-text word percentage, successful-solution claim, or new first-reading priority is asserted. The report is a concrete partial reading with full gaps, not a fluent continuous translation.

## Reproduce

From project root, run the existing own helper with Python -I: `python3 -I output/deep_2026-11-12/osnabrueck1647_cipheronly/crops/n20_settled/decode.py n20d` (it deliberately refuses to overwrite the existing result; use a temporary output adaptation for reruns). The exact original interpreter was `python3`. The decoder first verifies `log/n20d_settled.sha256`, then copies clear/symbol spans and substitutes each remaining character using key_v3. `shasum -a 256 -c log/n20d_settled.sha256` from the cipher-only root verifies the source-stage freeze.
