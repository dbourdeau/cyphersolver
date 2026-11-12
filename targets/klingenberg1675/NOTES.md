# Biermann to Klingenberg, 1675: the Klingenberg cipher of the Biermann copybook (Unsolved Catalogue no. 465)

Status: read in part. Key rebuilt from the ciphertext (no key sheet, no decipherment). Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic); issue #424. Folder prepared 12 Nov 2026.

## What this folder is, and what it is not

`targets/biermann1675` holds the copybook survey and the letters to Høeg and Meyercron read with the image-55 key sheet (K55) by the repository and by Brice Dudout. That work is theirs. Nothing here uses K55, and nothing here claims those letters. This folder is a separate entry for one of the families that folder lists as "key unknown": the German letters to Paul von Klingenberg at The Hague ("2xx-525 with letter signs"). It is a new folder because the key is a different key; no file of `targets/biermann1675` is changed. The letters were chosen from that folder's `survey_B.tsv` (credit to the repository).

The documents are the secretary Conrad Biermann's outgoing letters to Klingenberg: 24 in the copybook (6 February to 24 June 1675, images 43-256 of https://api.rigsarkivet.dk/ao/v1/images/<48573951+n>) and 3 drafts in the unit that follows it in the same image series ("1675-76 Koncepter til Skrivelser fra Conrad Biermann, 1675 Juli-Sept", start card at image 258; drafts on images 267, 271-273, 279-280; image ids 48573951+n). Clear German and cipher alternate inside the sentence.

## The system

1. Letter signs, one per letter (`key.tsv`, kind sign). In the copybook hand c is a large double-barred sign (#) and g a small single-bar one (H).
2. A syllable table 432-525 in alphabetical order: a vowel row (432 a, 433 e, 434 a stop, 435 o, 436 u) and rows of five for b c f g h j k l m n p r s t v w z (437 ba ... 525 zu). The d row has four: 447 de, 448 di, 449 do, 450 du (da is the word code 158). 446 is cu (tentative; it was read da until 29 May showed difficulteten).
3. Numbers 1-430: words, names and frequent word parts, in no order we have found. Map v4 gives 106 of them a value; each value has its contexts listed in `evidence/` (`key.tsv` names the file and the map in which the value first stood).

Maps: v1 (50 values), v2 (54), v3 (78), v4 (106; 364 changed from viel to wenig). `maps/` holds the frozen files; their sha256 are in the timestamp manifests (`timestamps/README.md`).

## The count of record (`counts.txt`, `scripts/count.py`)

A token is one cipher group. It counts as read only when it lies in a word whose groups decode letter for letter to the word the judge intends, under a map frozen before that letter was first decoded. A code with no value in that map is never counted, whatever the context suggests.

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
- The sign for c against the sign for g in the three drafts (96 failed tokens differ from the intended word only by c for g) - blocker: illegible; the reader wrote every hash-like sign as #, and a blind re-reading of those glyphs is not done. No figure that assumes it is quoted.
- Sixteen further letters (6 February to 21 June) used to build the key, with no reading and no count of record - blocker: too-short; the key was built on them, so they cannot be held out, and 20 March is its first page only.
- Clear text between the cipher passages, read approximately - blocker: illegible; one long clear passage of the 4 May letter only in part.
- Prior decipherment in Klingenberg's own papers (Rigsarkivet guide nos. 278 and 327) - blocker: needs-physical-access; not checked, so priority is not established.

## Escalation

- [x] siblings: the other letters of the copybook surveyed in `targets/biermann1675` (K55 letters to Hoeg and Meyercron, a different key); the sheet at images 94/95 compared (below); the three drafts of the unit that follows the copybook transcribed
- [x] clear-pages: no decipherment in the copybook or the drafts; the clear German between the cipher passages is read approximately
- [x] known-keys: K55 does not read these letters; sheet 94/95 reads none of the frequent groups (below); the chancery key volume swept in `targets/biermann1675/keyhunt.md` without a fit
- [x] print: Dudout's L'Europe chiffree names Klingenberg only; web searches found no decipherment; Klingenberg's legation archive not checked
- [x] key-rebuild: signs, syllable table and 106 word values rebuilt from the letters themselves, each map frozen before the letter it was tested on
- [x] retry: every letter decoded again with each later map; the counts of record use the map frozen before the letter was first decoded

## Relation to targets/biermann1675 and the sheet at images 94/95

`targets/biermann1675` reads the letters to Hoeg and Meyercron with the image-55 sheet (K55); this folder rebuilds the key of a different family of letters, those to Klingenberg, and uses nothing of K55. The sheet at images 94/95 (a German key endorsed 1675, whose declared null row is this sign set) is the sibling lead of `targets/biermann1675/keyhunt.md`; it is not this key as it stands: its 117 is "durch", 140 "Envoye Gioe", 200 "Graf Waldeck" and 224 "Hie", where the letters here give 117 be, 140 den, 200 sein and 224 das, and its blank slots 295, 254, 389, 120 and 369 are the frequent groups that read here as die, in, ver, und and nicht. A sibling relation (a later or earlier sheet of the same system) is not excluded.

## Integration check (12 Nov 2026)

The folder was verified before it was written up.

- `scripts/count.py` run in a copy reproduces all 27 lines of `counts.txt`: 551 of 729 (4 May, v3), 2,006 of 2,524 (seven letters, v3), 1,091 of 1,456 (three drafts, v4), 3,648 of 4,709 over the eleven (77.47%), and the lenient 90.8% of the drafts. An independent decoder written from `key.tsv` alone gives the contributor's decryption of the 4 May letter token for token (729 of 729; only the spelling auss/auß differs) and agrees on the other letters it could align (zero to five differences in clear-text layout or marks).
- The md5 of every transcription in `counts.txt` matches its file; the frozen 4 May text matches the sha256 in the first stamp. The three Sectigo tokens carry their manifest hashes (11 Nov 2026 21:08:16, 21:29:44 and 21:43:21 GMT). Map v3 (sha256 cf804c28...) is in the first stamp, before the seven letters appear in any stamp (the second, together with their v3 decodes); map v4 (9ac253c2...) is first stamped at 21:29:44, before the three drafts' transcriptions (21:43:21). So the maps were fixed before the test transcriptions were stamped. When the transcriptions were made, and that the maps were not touched between, rests **on the contributor's record**; the certificate chains and the OpenTimestamps proofs were not verified.
- Images (Rigsarkivet answered curl, 4128 x 3436 px): the verifier compared 333 groups of the 4 May letter (331 agree; the two corrections, 447 and 501, are in the folder), 62 groups of 1 June (img 209R; all agree) and 63 groups of the 28 June draft (img 267; all agree). The other letters have not been compared with the images. The c/g question of the drafts could not be tested.
- Controls: shuffled signs and syllables, 0 of 5,000 (z 7.6); the word-code layer is weakly separated by a character model (z 3.1), so the word values rest on context and on exact decoding of later letters. At integration `docs/_validate.py` was run on the tokens read under the maps of record (`validation.tsv`, written at integration from `counts_input.tsv` and `scripts/count.py`): see the validation block of `profile.json`. The German corpus of the repository was partial in that run.
- One counting rule is used in the whole folder: the contributor's strict count (a token is read only if its word decodes letter for letter to the intended word under the map frozen before the letter, and a code with no value is never counted). Its limits are stated above: the glosses were written after decoding, the transcriber knew the key, word-code values are context values. The word-code values are held to be context-only; the share of tokens in glossed words that decode from signs and syllables alone, with no word map, is 1,334 of 4,709 (28.3%, last column of `counts.txt` A, recomputed at integration). The 77.47% is the headline; the 28.3% is the floor.
- Corrections already carried by this folder from the verification of the issue: 447 and 501 in the 4 May transcription, 54 open codes (not 42), the d row of four syllables, "Flotte" (236) an open code under v3, the 65.0% and 69.0% explained, the 81.5% what-if not quoted.
- Catalogue 465 is narrowed to the letters still unread (Lilienkron, Gioe, Schroder, Reetz, Lindenow, Lincker, Lente); Klingenberg leaves it.

## Files

`key.tsv`; `maps/`; `evidence/`; `texts/` (per letter: transcription, decryption, and where they exist gloss, gloss_v4, reading, translation); `counts.txt` and `counts_input.tsv`; `emendations.tsv`; `holes.md`; `scripts/count.py` (the counter; `scripts/original/` the first scripts, as stamped); `timestamps/`.
