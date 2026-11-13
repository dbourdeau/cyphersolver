# Biermann to Klingenberg, 1675: the Klingenberg cipher of the Biermann copybook (Unsolved Catalogue no. 465)

Status: read in part. Key rebuilt from the ciphertext (no key sheet, no decipherment). Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic); issue #424. Folder prepared 12 Nov 2026; 22 further passages added 13 Nov 2026 (PR #490, see "The 22 further passages" below; they are not in the count of record); their German readings and English translations added 13 Nov 2026 (PR #496, "Integration check of PR #496" below).

## What this folder is, and what it is not

`targets/biermann1675` holds the copybook survey and the letters to Høeg and Meyercron read with the image-55 key sheet (K55) by the repository and by Brice Dudout. That work is theirs. Nothing here uses K55, and nothing here claims those letters. This folder is a separate entry for one of the families that folder lists as "key unknown": the German letters to Paul von Klingenberg at The Hague ("2xx-525 with letter signs"). It is a new folder because the key is a different key; no file of `targets/biermann1675` is changed. The letters were chosen from that folder's `survey_B.tsv` (credit to the repository).

The documents are the secretary Conrad Biermann's outgoing letters to Klingenberg: 24 in the copybook (6 February to 24 June 1675, images 43-256 of https://api.rigsarkivet.dk/ao/v1/images/<48573951+n>) and 3 drafts in the unit that follows it in the same image series ("1675-76 Koncepter til Skrivelser fra Conrad Biermann, 1675 Juli-Sept", start card at image 258; drafts on images 267, 271-273, 279-280; image ids 48573951+n). Clear German and cipher alternate inside the sentence.

## The system

1. Letter signs, one per letter (`key.tsv`, kind sign). In the copybook hand c is a large double-barred sign (#) and g a small single-bar one (H).
2. A syllable table 432-525 in alphabetical order: a vowel row (432 a, 433 e, 434 a stop, 435 o, 436 u) and rows of five for b c f g h j k l m n p r s t v w z (437 ba ... 525 zu). The d row has four: 447 de, 448 di, 449 do, 450 du (da is the word code 158). 446 is cu (tentative; it was read da until 29 May showed difficulteten).
3. Numbers 1-430: words, names and frequent word parts, in no order we have found. Map v4 gives 106 of them a value; each value has its contexts listed in `evidence/` (`key.tsv` names the file and the map in which the value first stood).

Maps: v1 (50 values), v2 (54), v3 (78), v4 (106; 364 changed from viel to wenig). `maps/` holds the frozen files; their sha256 are in the timestamp manifests (`timestamps/README.md`).

## The count of record (`counts.txt`, `scripts/count.py`)

A token is one cipher group. It counts as read only when it lies in a word whose groups decode letter for letter to the intended word (the model's gloss, written after decoding), under a map frozen before that letter was first decoded. A code with no value in that map is never counted, whatever the context suggests.

| letters | map | read | of | share |
|---|---|---|---|---|
| 4 May 1675 (the letter of issue 424) | v3 | 551 | 729 | 75.58% |
| 8, 11 May, 1, 5, 8, 12, 24 June (never seen before v3 was frozen) | v3 | 2,006 | 2,524 | 79.48% |
| three drafts, 28 June and July (never seen before v4 was frozen) | v4 | 1,091 | 1,456 | 74.93% |
| all eleven | | 3,648 | 4,709 | 77.47% |

551 + 2,006 + 1,091 = 3,648; 729 + 2,524 + 1,456 = 4,709. Only the short letter of 1 June reaches 95% (90 of 94). "Lenient" in the issue meant: Levenshtein distance of at most 1 between decode and intended word (at most 2 for words of nine letters or more); it is given in `counts.txt` and is not a share read.

Limits of these figures: the intended words (the gloss files) were written after decoding, by the same model that built the key; the transcriber knew the key as it then stood; there is no blind second transcription. The shuffled-map control (0 of 5,000) re-scores against that same gloss. The reviewer's own controls separate the signs and the syllable table strongly and the word-code layer only weakly.

## What each letter gets

- 4 May 1675 and the three drafts: transcription, decryption, gloss, German reading with every hole in place, full English with the same holes. State: read in part.
- The seven copybook letters of 8 May to 24 June: transcription, decryption, glosses (v3 and v4), rule-built German reading with a punctuated copy, full English with the same holes. State: read in part. The English was added on 12 Nov 2026 at the reviewer's request; it adds no read token, and every count in this file is unchanged.
- Sixteen further letters (6 February to 21 June) on which the key was built: transcription and decryption only, as evidence for the key. No count of record.
- The 22 further passages (PR #490, readings added by PR #496, 13 Nov 2026): transcription, decryption, ledger, word units, blind second transcription, and for each a rule-built German reading (holes in place; an E unit printed `decode[?word]` only where it passes the contributor's similarity test) and an English translation line for line with the holes in the same order, by an AI model and not checked by a German reader. State: read in part, no passage reaches 95%; not in the count of record.

The German readings are built by rule (`[?word]`, `[n]`, `[...]`; see the head of each file), not polished: no punctuation or capitals of ours in the cipher passages. The readings of the seven copybook letters also carry a second section, `Punctuated reading`: the punctuation there is ours; the word division is the rule-built one from the gloss, also ours, since the cipher marks none; no decoded letter, capital or hole is changed (checked by stripping our marks and comparing token for token).

## Emendations and overrides, all declared

- Two numerals of the 4 May transcription, changed on 12 Nov 2026 after the reviewer's comparison with the images and our own check: line 83, 441 -> 447 (the third digit has the hooked top of the 7 in 476 on the same line; the 441 on the line above has a plain stroke): certain. Line 44, 511 -> 501 (the middle sign is a small closed loop, not a stroke; compare 501 two lines from the end): probable. The frozen text is kept (`..._transcription_frozen.txt`). With both, v3 gives 561 of 729; that is not the count of record.
- One sign of the 8 May letter was re-read after decoding (9? -> y, image-checked); the frozen file is unchanged and is the one given here.
- Every word printed `[?word]` because its decode differs from the intended word: `emendations.tsv`, 120 rows over the eleven letters (letter, token span, decode, intended word).
- Word values taken into v4 from letters they then appear in (training status): listed in `holes.md` for 4 May. 236 Flotte is one of them: under v3 it is an open code, and the issue printed "Flotte" unmarked.
- Sign map: PP = q and the inverted T = z were added on 11 Nov after the 29 May and 17 April letters had been scored; 446 = cu likewise.
- No override of any image reading in favour of sense other than those above. Clear text is approximate.

## The signs for c and g in the drafts

In the copybook (a clerk's fair hand) the two signs are distinct and, on the reviewer's sample, correctly transcribed. In the three drafts (Biermann's own hand) our reader wrote every hash-like sign as #. After decoding, 96 failed tokens were found in words that differ from the intended word only by c where g is wanted (muclich, fertic, handlunc). A what-if that turns those into g gives 81.5%; it was made after decoding, by the judge, and must not be quoted. The honest state: the drafts stand at 1,091 of 1,456 until someone who does not know the intended words reads those glyphs again.

Update (PR #490, 13 Nov 2026): run b116 re-read the hash-like signs of the three drafts by form only (74 candidate boxes on 34 crops, classified H or # against a chart of 12 and 12 from the copybook hand, frozen 12 Nov 05:43:43 UTC, md5 acd67760; mapped afterwards to 70 positions). Decoded once with v4, the glyph transcriptions give 1,181 of 1,456 tokens (81.11%; 28 June 219/259, July b 578/720, July c 384/477). This is NOT the count of record, which stays 1,091 of 1,456 = 74.93%: the classifier had read the integration note quoting the 81.5% what-if and the 96 tokens (not blind to the expected result), it wrote no per-draft decryption, ledger or gloss (the 1,181 cannot be recounted from the folder), and the signs it classed H were fixed before any mapping but by one reader. A later blind reader (b176) found six sites where the first reader's # is a single-barred H in drafts of the same hand family, so the confusion is real and not confined to the three drafts.

## Errors of ours, found by the reviewer or in preparing this folder

1. Open codes in the 4 May letter: 54 tokens, not 42 (12 stood inside glossed words). The reviewer is right.
2. The issue's key text said five syllables per consonant; the d row has four. The reviewer is right.
3. "Flotte" was printed unmarked while 236 had no value in the map of record.
4. The issue's reading was an excerpt and its English a gist.
5. 65.0% (29 May) and 69.0% (17 April) reproduce only with the table and sign map of the day; with the final ones they are 299 of 437 and 171 of 239. The issue did not say the map had moved.
6. The first scripts skipped every transcription line that began with the sign #; the 20 March figure made with them is withdrawn. The 16 March figure (36 of 157) is not reproduced to the token.
7. Map v1 holds 50 values; our log said 51.
8. The 4 May heading and salutation were not re-read for this folder; the direction (Biermann to Klingenberg) was checked on the headings of the seven later letters.

## Remaining gaps

- Word codes with no value in the map of record (54 tokens of the 4 May letter under v3, 25 under v4; mostly names and nouns seen once to five times: 143, 418, 71, 353, 112, 180, 352, 329, 416, 385) - blocker: open-codes; more letters or Klingenberg's own deciphered letterbook would fix them.
- The sign for c against the sign for g in the three drafts (96 failed tokens differ from the intended word only by c for g) - blocker: illegible; the reader wrote every hash-like sign as #, and the corrected pass of run b116 (1,181 of 1,456, 81.11%, not the count of record) had no ledger or gloss and a classifier that had read the 81.5% what-if; a blind re-reading with a ledger is still owed. The count of record is not changed.
- Sixteen further letters (6 February to 21 June) used to build the key, with no reading and no count of record - blocker: too-short; the key was built on them, so they cannot be held out, and 20 March is its first page only.
- Clear text between the cipher passages, read approximately - blocker: illegible; one long clear passage of the 4 May letter only in part.
- Prior decipherment in Klingenberg's own papers (Rigsarkivet guide nos. 278 and 327) - blocker: needs-physical-access; not checked, so priority is not established.
- The 22 further passages of PR #490: 335 of the 733 E units hold a code with no value in v4 (329 occurrences of 111 distinct codes; most often 211, 110, 250, 5, 139, 143, 354; "0" is the O-as-0 slip of 287R-289L) - blocker: open-codes; more letters or Klingenberg's deciphered letterbook.
- Ten passages parked by the first reader (59R-60L, 70R, 254R, 263L, 274R, 72L-72R P.S., 112R-113, 134R-136L body, 151R P.S., 152L; 253R-254L not transcribed) - blocker: illegible for 112R-113 and 253R-254L (bleed-through, overwriting); for the others the transcriptions were not sent to us, only md5 values and logged figures (322 of 455 word units, 70.77%), so they cannot be checked here.

## Escalation

- [x] siblings: the other letters of the copybook surveyed in `targets/biermann1675` (K55 letters to Høeg and Meyercron, a different key); the sheet at images 94/95 compared (below); the three drafts of the unit that follows the copybook transcribed
- [x] clear-pages: no decipherment in the copybook or the drafts; the clear German between the cipher passages is read approximately
- [x] known-keys: K55 does not read these letters; sheet 94/95 reads none of the frequent groups (below); the chancery key volume swept in `targets/biermann1675/keyhunt.md` without a fit
- [x] print: Dudout's L'Europe chiffree names Klingenberg only; web searches found no decipherment; Klingenberg's legation archive not checked; the printed Privy Council protocol of 1675 (Aarsberetninger fra det Kongelige Geheimearchiv VI, pp. 117-126) and Historisk Tidsskrift 5. R. IV pp. 446-450 checked on archive.org (13 Nov 2026): they print the policy, not the letters or any cipher (see the page and `evidence/prior_art_aarsberetninger_VI_1675.md`)
- [x] key-rebuild: signs, syllable table and 106 word values rebuilt from the letters themselves, each map frozen before the letter it was tested on
- [x] retry: every letter decoded again with each later map; the counts of record use the map frozen before the letter was first decoded

## Relation to targets/biermann1675 and the sheet at images 94/95

`targets/biermann1675` reads the letters to Høeg and Meyercron with the image-55 sheet (K55); this folder rebuilds the key of a different family of letters, those to Klingenberg, and uses nothing of K55. The sheet at images 94/95 (a German key endorsed 1675, whose declared null row is this sign set) is the sibling lead of `targets/biermann1675/keyhunt.md`; it is not this key as it stands: its 117 is "durch", 140 "Envoye Gioe", 200 "Graf Waldeck" and 224 "Hie", where the letters here give 117 be, 140 den, 200 sein and 224 das, and its blank slots 295, 254, 389, 120 and 369 are the frequent groups that read here as die, in, ver, und and nicht. A sibling relation (a later or earlier sheet of the same system) is not excluded.

## Integration check (12 Nov 2026)

The folder was verified before it was written up.

- `scripts/count.py` run in a copy reproduces all 27 lines of `counts.txt`: 551 of 729 (4 May, v3), 2,006 of 2,524 (seven letters, v3), 1,091 of 1,456 (three drafts, v4), 3,648 of 4,709 over the eleven (77.47%), and the lenient 90.8% of the drafts. An independent decoder written from `key.tsv` alone gives the contributor's decryption of the 4 May letter token for token (729 of 729; only the spelling auss/auß differs) and agrees on the other letters it could align (zero to five differences in clear-text layout or marks).
- The md5 of every transcription in `counts.txt` matches its file; the frozen 4 May text matches the sha256 in the first stamp. The three Sectigo tokens carry their manifest hashes (11 Nov 2026 21:08:16, 21:29:44 and 21:43:21 GMT). Map v3 (sha256 cf804c28...) is in the first stamp, before the seven letters appear in any stamp (the second, together with their v3 decodes); map v4 (9ac253c2...) is first stamped at 21:29:44, before the three drafts' transcriptions (21:43:21). So the maps were fixed before the test transcriptions were stamped. When the transcriptions were made, and that the maps were not touched between, rests **on the contributor's record**; the certificate chains and the OpenTimestamps proofs were not verified.
- Images (Rigsarkivet answered curl, 4128 x 3436 px): the project's verifier (a model check, not a person) compared 333 groups of the 4 May letter (331 agree; the two corrections, 447 and 501, are in the folder), 62 groups of 1 June (img 209R; all agree) and 63 groups of the 28 June draft (img 267; all agree). The other letters have not been compared with the images. The c/g question of the drafts could not be tested.
- Controls: shuffled signs and syllables, 0 of 5,000 (z 7.6); the word-code layer is weakly separated by a character model (z 3.1), so the word values rest on context and on exact decoding of later letters. At integration `docs/_validate.py` was run on the tokens read under the maps of record (`validation.tsv`, written at integration from `counts_input.tsv` and `scripts/count.py`): see the validation block of `profile.json`. The German corpus of the repository was partial in that run.
- One counting rule is used in the whole folder: the contributor's strict count (a token is read only if its word decodes letter for letter to the intended word under the map frozen before the letter, and a code with no value is never counted). Its limits are stated above: the glosses were written after decoding, the transcriber knew the key, word-code values are context values. The word-code values are held to be context-only; the share of tokens in glossed words that decode from signs and syllables alone, with no word map, is 1,334 of 4,709 (28.3%, last column of `counts.txt` A, recomputed at integration). The 77.47% is the headline; the 28.3% is the floor.
- Corrections already carried by this folder from the verification of the issue: 447 and 501 in the 4 May transcription, 54 open codes (not 42), the d row of four syllables, "Flotte" (236) an open code under v3, the 65.0% and 69.0% explained, the 81.5% what-if not quoted.
- Catalogue 465 is narrowed to the letters still unread (Lilienkron, Gioe, Schroder, Reetz, Lindenow, Lincker, Lente); Klingenberg leaves it.

## The 22 further passages (PR #490, 13 Nov 2026; not in the count of record)

Contributed by Malcolm McBratney with AI agents (issue #424, PR #490). The contributor's own account is `NOTES_addition_2026-11-13.md`; this section is what holds after the integration check below. 22 passages of the drafts units (18 in unit 260195, 4 in unit 260196; images in the table on the page), each transcribed once by the first reader (the model that built the key, not blind), decoded once under map v4 (md5 e9698159, table M3 38c7c1e5, unchanged by these passages; the logs assert the md5 before each decode), and judged by word units after decoding. Second transcriptions by blind readers (b158, b161, b166, b172, b176) exist for all 22. Per passage, in `texts/<id>_klingenberg_*`: transcription, decryption, ledger (`_ledger.tsv`), word units, blind transcription, decryption and word units, shuffle outputs.

Figures, all recomputed at integration from the ledgers with an own parser and an own decoder (0 differences in the decode column over all 3,386 units):

- First reader, word units: 2,561 of 3,386 = 75.63% (S 2,561, E 733, N 92); without 10 "." units counted S: 2,551 of 3,376 = 75.56%. Per passage in the page table; the range is 66.9% (50R-51R) to 91.2% (214R-216R); no passage reaches 95%.
- The same rule as the count of record, in tokens (a token is read only inside a word whose decode equals the intended word letter for letter): 6,103 of 8,587 = 71.07%. This is the figure comparable with the 77.47%.
- The floor, tokens in words built only from letter signs and table syllables, no word code: 2,032 of 8,587 = 23.66% (the count of record has 28.3%). Word-code values are context values; on the README bar as written they are holes.
- Blind second readers, `?` units as holes: 16 passages 1,976 of 2,567 = 76.98% (holes left out 90.89%); first reader on the same 16, 1,992 of 2,683 = 74.25%; six passages of b176 with unread units in the denominator 579 of 693 = 83.55%; all 22, 2,555 of 3,260 = 78.37%. The two readers cut word units independently, so the denominators differ. These are the contributor's judging files recounted by us; the blind readers knew the key and the maps.
- Not pooled with the eleven letters: different unit (word units and tokens), single not-blind judge, passages chosen by page order and then by a filing rule.

Order of events, by the contributor's record, with one outside fact: all 22 first transcriptions and decodes are lines of nine RFC 3161 manifests (Sectigo, TSA times 12 Nov 2026 13:21:03 to 16:26:00 GMT; imprint equal to the manifest sha256, checked here; three first requests were rejected and the retry granted; certificate chains and the OpenTimestamps proofs not verified). The ledgers and word-unit files (the intended words) are mostly not in a manifest, and the blind transcriptions are not stamped: "frozen before" for those is the contributor's record, with md5 values that match the files.

Disclosed by the contributor and kept: partial blindness breaches (b161 saw the H/# chart with H = g and # = c; b172 saw the sign map after freezing 136R; b166 saw the first reader's file names; b176 saw the chart); umlaut-less spellings counted S; first-pass figure of 104R-106R 178 of 273 = 65.20% against the filed 191 of 278 = 68.71% after 11 clerical fixes; 68R-72L conservative bound about 350 of 514 = 68.1%; 287R-289L: O written as digit 0 in six places (six units wrong, scored as frozen); code 262 queried from a glossed copy (no key change); "." units counted S; 247R: a left-margin cipher insert missed by both readers; 235L: a margin block in a different cipher (Delta family, signs triangle, psi, pi, theta, numbers in the 600s), outside this key and excluded; at six sites (194, 215L, 235R, 236L, 288L, 288R) the first reader's # is a single-barred H (found by b176 on 4-5x crops; the first reader's figures are not rescored).

Selective filing: the first reader set a filing rule (German 4-gram shuffle 0/5,000 and strict about 65%) and parked ten passages that failed it. Logged figures (files not sent): 59R-60L 35/41, 70R 3/4, 254R 2/3, 263L 9/14, 274R 15/16, 72L-72R P.S. 33/51, 112R-113 34/71, 134R-136L body 158/215 (shuffle 1/5,000 at one seed), 151R P.S. 26/33, 152L 7/7: 322 of 455 = 70.77%. Pooled with the 22 filed: 2,883 of 3,841 = 75.06%. A pool of filed passages flatters (0.6 point here); the page gives per-passage figures and does not pool.

Prior art (checked on archive.org, 13 Nov 2026): the printed protocol of the Privy Council 1675 (Aarsberetninger VI, pp. 117-126) and the review in Historisk Tidsskrift 5. R. IV pp. 446-450 print the policy the letters carry (fleet subsidies, the declaration against Sweden, Lüneburg troops, Bremen, the state before Brömsebro) but neither a letter to Klingenberg nor a cipher. Every quotation of `evidence/prior_art_aarsberetninger_VI_1675.md` was found in the OCR under the stated printed page (not compared with page images). For 13 of the 22 drafts (287R, 44, 57R, 68R, 73R, 85R, 104R, 168R, 189R, 193R, 214R, 247R, 248R) the content is already in print in summary: RISK on content; the deciphered wording is not. Six of the 13 rest only on entries of pp. 125-126 (3 Aug 1675 and 13 Jan 1676). The matching of drafts to protocol entries is the contributor's, by hand, from the drafts' filing lines, and was not redone draft by draft. For the other nine nothing was found.

Controls: the contributor reports 0/5,000 shuffles per passage (German 4-gram, two seeds) for every filed passage; the script is not in the folder (only `shuffle_words.py`) and three passages have no output file. A control of our own (`de-modern`, order 4, no spaces; v4 word values shuffled over the word codes, signs and table fixed; 1,000 shuffles; seed 1675) gives 0 of 1,000 at or above the real score for 13 passages and 1 to 29 of 1,000 for nine (09-06, 09-23, 136R, 149R, 177R, 193R, 10R, 235R, 251R); z 1.6 to 4.5. As for the eleven letters, the word layer is weakly separated by a character model.

Not done, with no outside blocker (open to anyone): a German reader's judgment of the intended words (written by the model that built the key after decoding; the blind readers knew the key); a script for the contributor's 4-gram control. (The reading file and English translation of each passage were added by PR #496, 13 Nov 2026, see the last section.) What the passages are not: not read to the README bar (no passage reaches 95%); the class stays "read in part".

## Integration check of PR #490 (13 Nov 2026, round 5)

- Reproduced: every figure of the PR (table on the page): ledger sums, token sums, blind sums, b176 per letter, glyph-pass arithmetic; `scripts/count.py` under `python3 -I` reproduces `counts.txt`. An own decoder (signs from `key.tsv`, table, v4) reproduces the decode column of all 22 ledgers, 3,386 units, 0 differences.
- Manifests: 9 of 9 granted tokens carry the manifest sha256 as imprint; all 22 first transcriptions and decodes are listed lines; 46 of 56 FROZEN md5 lines match a file here, the other ten are the parked passages.
- Images (api.rigsarkivet.dk answered): 136R, 79 groups, all agree; 214R-216R (image 215), 124 groups, all agree; 203 groups, no disagreement on digits; sign identity (F, K, H against #) is a judgment on glyph forms. The other 20 passages were not compared with the images here.
- Own control and own filing arithmetic as above. The prior-art file was checked against archive.org text.
- Nothing already in the folder (NOTES.md before this section, profile.json, counts.txt, the page) was changed by the PR; the count of record is unchanged.

## Integration check of PR #496 (13 Nov 2026, round 6): readings and translations of the 22 passages

Verified by own scripts over all 22 passages (not a sample): stripping our punctuation from the punctuated reading gives the reading back line for line; the table of E units at the end of each reading has exactly as many rows as the ledger has E units (733 in all) and as many printed emendations as the reading has `[?word]` (210); the English has every `[n]` and `[blot]` in the same order as the German (21 of 22; 27 March differs only by the six `[0]`, the O sign written as the digit 0, which the contributor discloses); the reading equals the ledger's decode column word for word on 3,384 of 3,386 units (the other two are one unit with two blots shown as one `[blot]`, 68R-72L). Five passages (214R-216R, 10R-11L, 287R-289L, 50R-51R, 136R) were read as German sentences against their English: they build clauses with holes; the English follows.

What this changes and does not: no key value, ledger or figure changed; every passage stays read in part (best 214R-216R, 93 of 102 word units = 91.18%; 87.9% by tokens). The emendations `decode[?word]` are the first reader's intended words (written after decoding) and are not read words; 523 of 733 E units stay as decoded. The English is by an AI model, not checked by a German reader (stated in each file): that check is open to anyone. The 16 short cipher lines in 10 passages that the contributor lists are word for word only. The profile now lists the 22 passages as documents and `read in part` texts (reading_review grade B by the integration pass, not independent of the contributor's AI translation). The claims review of the changed page sentences is by line-by-line fallback; an independent reader is still owed.

## Files

`key.tsv`; `maps/`; `evidence/`; `texts/` (per letter: transcription, decryption, and where they exist gloss, gloss_v4, reading, translation); `counts.txt` and `counts_input.tsv`; `emendations.tsv`; `holes.md`; `scripts/count.py` (the counter; `scripts/original/` the first scripts, as stamped); `timestamps/`. PR #490 adds, for the 22 further passages, `texts/<id>_klingenberg_{transcription,decryption,ledger,wordunits,..._blind,shuffle}`, `evidence/blind/`, `evidence/filed/`, `evidence/first_reader/` (logs and parked lists), `evidence/glyph_pass_b116/`, `evidence/prior_art_aarsberetninger_VI_1675.md`, `timestamps/20261112T*` and the contributor's `NOTES_addition_2026-11-13.md`.

## Claims review by a second reader (12 Nov 2026)

An independent reader checked the page against this folder. Changed:

- The 333-group comparison of the 4 May letter with the images (331 agree) was the project's verifier, a model check, not a second person; the page said a person.
- "Frozen before each letter was decoded" is stated as by the contributor's record in the hero and the glance box.
- The glance box says 29 letter signs (key.tsv has 29 sign rows), not about 25; likewise the README row and the Full-texts card (`profile.json`).
- "The word the judge intends" is defined where first used: the intended word, the model's gloss written after decoding.
- The quotation from the 4 May reading is given as the file has it, with `[?de] auß ... [?schwerlich]`.
- One spelling, Høeg, throughout.
