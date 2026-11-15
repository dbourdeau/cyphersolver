# bonde1675code246: Carl Bonde to a Chancery Councillor, Paris, 13 Nov 1675, in a second code (1-246)

Stockholm, Riksarkivet, Diplomatica Gallica, SE/RA/2105/I/A/24/54 (Envoyén Carl Bonde, Brev till Kungl. Maj:t
1674-1678; image series R0003797), images 113 right and 114 left
(<https://sok.riksarkivet.se/bildvisning/R0003797_00113>, <https://sok.riksarkivet.se/bildvisning/R0003797_00114>).
Same volume as `bonde1676` (catalogue 2317). No images or crops are published here: link the Riksarkivet viewer.

**State: read in part, from the period decipherment.** The chancery's ink gloss deciphers the whole letter. Its first
half (gloss lines G01-G20 of 113 right) is read here as sentences with scattered holes (about 90% of words). The rest
of the gloss (G21-G33 and 114 left lines 1-4) is read only in part, with many holes, and stays "decoded, not read".
The draft key built from the gloss is **not validated** (0.66 resubstitution after pass 4, see below).

## What the document is

One letter in cipher filling image 113 right (33 lines of numbers) and running on to image 114 left (32 lines). It
opens `Herr Cantzlirådet` (pencil, letter by letter over the first numbers, and the ink gloss) and ends, in the gloss
of 114 left line 4, `willigheet. Carolus Bonde Paris d. 13 Novembris` with `1675` on line 5. The last cipher line of
114 left is `18/28` (in figures) and `50.77.34.42.22.16.112.55.149`, which a later pencil hand wrote out letter by
letter as `Novembris`, followed by `1675` in clear.

Carl Bonde, Swedish envoy in Paris (1674-1678), writes to a Chancery Councillor in Stockholm, not to the King. He
thanks him for the affection he showed him while Bonde was in Stockholm, and asks him to put to Charles XI his humble
request to be allowed to take the four thousand riksdaler granted for his maintenance in Paris from the subsidies
falling due in January. The sum does not cover what he must lay out, but he is content and will spare nothing in the
King's service, provided he is not unfairly shut out of the royal grace that the other ministers enjoy. The second
half (decoded, not read) speaks of his confidence (`förtröstning`), of being helped, of the King, of serving with zeal
and affection, of finding an occasion to show it, and closes with his readiness (`beredvilligheet`) and signature.
The subsidies are presumably the French subsidies paid to Sweden under the alliance of 1672; that is context, not
something the letter is shown to say.

**Who the recipient is** is open. The postscript on image 112 right (despatch of 12/22 Nov 1675) says that the
enclosed letter goes to H. Hoghusen "efter gamla chiffrer" (in the old cipher). That postscript is itself written a
second time in yet another letter-for-letter code (34 = o, 42 = u, values 335 and 484), not this one. This letter may
be the one it announces; the date (13 against 12/22 Nov) and the title `Cantzlirådet` have not been checked against
Hoghusen. A hypothesis only.

## Why it is its own target

KEY_v10 of the main Bonde system (`bonde1676`, Malcolm McBratney) does not read it: in that system values start at
19, while here 9-18 are frequent and 216 and 246 are common, and both pages open with `17.246`. `bonde1676` NOTES had
noted 114 left as "a different code"; 113 right is the first page of the same letter. Daniel Bourdeau checked on the
images that the last line of 114 left is `Novembris`, one number a letter, and that the gloss reaches the signature on
114 left line 4, so it covers the bare lines (issue #629). He asked for this second key to be its own target.

## The system

Homophonic substitution, one number per letter, numbers written with dots between them, no word division. Values 1-246;
121 distinct numbers in the 978 training numbers (one reading of 346 is above the range, probably a misreading). No
syllables, no code words and no nulls were identified. Swedish plaintext with the chancery spelling of the time
(`hafver`, `thet`, `iagh`). Example: `hafver at` = 46.38.12.34.70.27.17.246 (113 right L01).

## The gloss runs ahead of the cipher

Each gloss line carries about 2.2 times as many letters as the cipher line it stands over. So the gloss is not a
line-by-line decipherment but the clear of the whole letter written continuously between the lines: G01 to the start of
G19 is the clear of the 33 cipher lines of 113 right, and the rest of G19 to G33, with the gloss of 114 left lines 1-4,
is the clear of the 32 cipher lines of 114 left. The "bare" lines of 114 left are therefore already deciphered at the
time. (The same drift was what defeated our first line-by-line alignment of the main system on image 102 right.)

## Transcriptions (the cipher numbers)

Format of the TSV files: line id, numbers separated by dots, the gloss over that line as read by that pass, notes.
`3|9` = doubtful (likelier first), `?` = unreadable, `[?]` = lost in the binding. Conventions of the hand (a flat-topped
3 easily read as 8 or 9; 6 written like `б`): protocol/CONVENTIONS-TRANSCRIPTION.md.

| file | lines | who |
|---|---|---|
| transcriptions/113R_L01-L18_pass1.tsv, 114L_G01-G32_pass1.tsv | 113R L01-L18, 114L G01-G32 | pass 1, Opus sub-agent |
| transcriptions/113R_L01-L18_pass2_blind.tsv, 114L_G01-G32_pass2_blind.tsv | same | pass 2, Opus sub-agent blind to pass 1 |
| transcriptions/113R_L01-L18_pass3_final.tsv, 114L_G01-G32_pass3_final.tsv | same | pass 3 with arbitration (final) |
| transcriptions/pass3/ | 321 positions | pass 3 items, the two blind readers' answers per page, the arbitration |
| transcriptions/113R_L01-L18_pass4_final.tsv, 113R_pass4_corrections.tsv | 113R L01-L18 | pass 4: pass 3 with 7 numbers corrected by a person (see below) |

Passes 1 and 2 agreed on 367 of 392 numbers of 113 right L01-L18 (94%). Pass 3 re-read every position where the two
passes differed, where pass 1 marked a doubt, or where the decode with the lot-13 key did not match the gloss (the
decode only said where to look; no reader saw it): 321 positions, each read by two blind Opus readers who saw only the
neighbouring numbers as landmarks; 293 agreed, 28 went to an arbiter on the image. 45 numbers changed from pass 1 and
18 positions were dropped (binding, unreadable, no group). The readers' notes are in French.

Pass 4 (15 Nov 2026): Brice Dudout answered a blind digit-form sheet of 21 doubtful numbers and 3 control numbers
(one digit framed at a time, digit shapes to choose from, no letters, no key; the sheet's rules were frozen by SHA-256
before it was built). He got the 3 controls right. Seven numbers of 113 right changed (L01 no. 6 28→23, L03 no. 2 27→77,
L03 no. 12 28→23, L04 no. 4 37→27, L04 no. 13 49→40, L11 no. 15 28→23, L16 no. 21 28→23; the list is in
transcriptions/113R_pass4_corrections.tsv). The seven doubtful `34` were all confirmed as 3, not 9, so the flat-topped 3
is a 3 here. 114 left is unchanged from pass 3.

**113 right lines L19-L33 (301 numbers) are kept aside** and are not in this folder: they were set apart as a held-out
test portion before any key was built, transcribed by two blind sub-agents and an arbiter, frozen by SHA-256, and
never decoded (the test was not run, see "The draft key"). They stay available for a future test.

## The period gloss and its reading

- gloss/113R_G01-G20_fable.tsv: G01-G20 of 113 right read from the images by Claude Fable 5.2 (14 Nov 2026), with
  every doubtful letter as `{x|y}` and unread zones `‹…n›`, and per-line notes.
- Check (fixed in writing before the draw, protocol/PROTOCOLE-VERIF.md): three blind Claude Opus 5.5 sub-agents, who
  saw neither Fable's reading nor ours, the key or the held-out lines, chose among shuffled options (Fable's letter or
  letters plus confusable ones, "other", "unreadable"), with the target letter masked in a context of two letters, on
  151 items of G05-G20: a 10% sample (51) of the 503 letters Fable marked sure, all 95 doubtful groups, all 5 unread
  zones. **Disagreement on the sure letters: 4 of 51 = 7.8%** (our acceptance bar was 10%). Of the doubtful groups, 83
  kept one of Fable's options and 12 were left unresolved; the unread zones stayed unread. Log:
  gloss/113R_G05-G20_blind_check_log.tsv; the checked text: gloss/113R_G05-G20_after_blind_check.tsv.
- gloss/113R_G19-G33_subagents.tsv: G19-G33, read by Opus sub-agents (two passes and an arbiter); many words doubtful.
- gloss/114L_lines1-5_gloss.tsv: the gloss of 114 left lines 1-5, two passes; many words unread.
- readings/113R_gloss_G01-G20.md and translations/113R_gloss_G01-G20_en.md: G01-G20 normalised into sentences and
  translated, with each hole explained. 16 of 161 words are holes (read share 0.90 by research/reading_audit/v2_score.py).

## The draft key

key/key.tsv (120 values) and key/METHOD.md. Built from the period gloss by alignment and majority vote over the pass-3
numbers of 113 right L01-L18 and 114 left. **Character agreement with the gloss: 0.65** (0.736 on 113 right L01-L18,
0.599 on 114 left), **measured on its own training text (resubstitution). This is not a validation.** Our protocol
(protocol/PREREG-CODE246.md and addenda 1-3, frozen by SHA-256 before each step) allowed one test on the held-out
lines only if resubstitution reached 0.85 and the test then beat 200 shuffled keys by 0.30. Resubstitution stayed
below 0.85, so the test was not run and the held-out lines were not decoded. We make no claim to a new reading.

The decodes (decryptions/113R_L01-L18_draftkey.txt, decryptions/114L_G01-G32_draftkey.txt) still follow the gloss word
for word (spaces added here; letters in brackets are ones the decode lacks or gets wrong), e.g. 113 right: `hercastzliirådet hafverat påthet flitvänligaste ... såsom ... min närva[r]u uthi stookholm
... afection förhvilckes iag finer mighpåthethögsta obligerv[a]t ... hvns maiestet mi[n] underdåsig[a] begieran ...
fyra tuses[n]de ri[x]dal[er] hans maietet nådigst ...`; 114 left: `... förtröstning ... blifva hulpen ... honom
medalzeleochefection ... finna [n]o[g]on occasion at viisa ... beredviligheet c[a]rolus bonde paris de[n] novembris`.
The figure stays low because the gloss abbreviates and does not always follow the cipher word for word, the later
gloss is poorly read, and the numbers still carry errors (key/METHOD.md).

**Pass 4.** Re-voting the key on the pass-4 numbers (same method, same script with new paths) gives exactly the same
120 values as key/key.tsv; the seven corrected numbers alone raise resubstitution to **0.6605** (113 right 0.754, 114
left 0.599). Still under 0.85: no test.

**A second Fable run (15 Nov 2026), for the key.** With Brice Dudout's approval and a 5 USD cap for the one run
(protocol/PREREG-CODE246-ADDENDUM-4.md, frozen before the call), Claude Fable 5.2 was given the pass-4 training numbers,
the training gloss as normalised words, the draft key and the scoring script, and asked for a better key with reasons
for each value. It saw none of the held-out numbers. Its key (key/fable_lot14_proposal.json, 144 values, 24 of them for
numbers never seen, taken from the table alone) scores **0.6544** by our own scoring, slightly *below* the draft key;
Fable found the same and reported that even an unconstrained fit stops at 0.664, so the ceiling comes from the gloss
(the later gloss above all) and the number readings, not from the key. The rule was a test only at 0.85 or more, so
**no test was run and the held-out lines were again not decoded.** The run cost 2.93 USD.

What the run adds is structure. The key is laid out as a regular table in blocks of nine or ten cells, running in
alternate directions: a-h over 17→9, 38→46, 74→66, 94→102 (with a second `f` cell), i-q over 18→26, 55→47, 83→75,
103→111 (with a second `l` cell), r-z over 65→56, 93→84, 112→121 and 27→37, and å ä ö on 161-169
(key/fable_lot14_table.tsv). We checked it ourselves: in Fable's key, 94 of 127 pairs of consecutive numbers carry
neighbouring letters, against at most 17 in 200 keys with the letters shuffled (the draft key: 55 of 86, at most 14).
The table was read off the same key, so this is a strong pattern, not an independent proof. Fable also suggests that a
few cells stand for doubled letters (11 = `ff`, perhaps 63 = `ss` and 30 = `tt`), which a one-letter-per-number key
cannot express. Both are hypotheses for whoever takes the key further; the draft key in key/key.tsv is unchanged.

## The date: the cipher says 18/28, the gloss 13

The cipher's last line on 114 left begins with the date in figures, written as a fraction: `18` over `28` (read so by
both pass-3 readers; one saw `18` above, separated by a stroke). The gloss signature on 114 left line 4 reads
`Paris d. 13 Novembris` (pass 1), or `13/23 Novembris` (pass 2, which saw a `13` written over `23`). Both pairs are
Old Style / New Style dates ten days apart. In this hand a flat-topped 3 is easily read as 8, so we asked a person to
look. On a blind digit-form check (Brice Dudout, 15 Nov 2026: one digit framed at a time, shapes to choose from, no
context, 3 of 3 control digits right), the upper number of the fraction is `18`: the cipher is dated
**18/28 Novembris**, while the gloss gives **d. 13 Novembris**. Either the letter was drafted on the 13th and enciphered
or sent on the 18th, or the gloss writer slipped. We do not settle which. (Issue #629.)

## Prior art

Not found in print as far as checked for `bonde1676` (its NOTES, prior_solution); no study of this second code was
found. The reading is the chancery's own decipherment of the time, so this is not a first break.

## Credits

- The Swedish chancery's interlinear decipherment of 1675 (the gloss): the reading.
- Malcolm McBratney broke the main Bonde system (KEY_v10, `bonde1676`); this second code was recognised against it.
- Daniel Bourdeau checked the `Novembris` line and the reach of the gloss on the images (issue #629).
- Brice Dudout: identification of the second code and of the letter, transcriptions, gloss reading and draft key,
  with Claude agents (Opus 5.5 for transcription, checks and key; Fable 5.2 for the gloss of G01-G20).

## Remaining gaps

- Gloss G21-G33 of 113 right and 114 left lines 1-4: read only in part (illegible in places for our readers); a careful
  palaeographic reading of these lines would give the second half of the letter.
- The scattered holes of G01-G20 (listed in the reading).
- The draft key is untested; 113 right L19-L33 are kept aside for one test. Resubstitution is stuck near 0.66 with
  the present gloss reading (Fable's key included); a better reading of G21-G33 would help more than a new key.
- The block table and the doubled-letter cells (Fable's hypotheses) are unchecked against new text.
- Why the cipher (18/28) and the gloss (13) differ, and the recipient (Hoghusen?), are open.
