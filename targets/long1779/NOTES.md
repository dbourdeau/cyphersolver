# Enoch Long's journal, Tiverton and Newport, 1779-1780 (pension file W. 16138)

Status: in progress (both alphabets recovered; after a blind second reading, 49% of the cipher words are read with
confidence and 25% more are probable; the site page waits for a human check of the readings against the images and the
claims review)

**Source.** National Archives, Revolutionary War Pension and Bounty-Land Warrant Application File W. 16138 (Enoch Long,
widow Molly), microfilm M804 roll 1580; free images in the National Archives Catalog, NAID 196199890
(https://catalog.archives.gov/id/196199890), images 11-31 of 57. The images are public-domain federal records; this
folder commits only small crops of signs and evidence. The full-size images are the catalog's own objects
(`.../export_M804-RevolutionaryWarPensionAppFiles_1580_9193/images/4160708_00394.jpg` to `..._00414.jpg`).

**Who found it.** Our Fold3 sweep (13 Nov 2026), from the pension clerk's wrapper note on image 10, "Journal partly
written in Cipher". **Who read it before.** Nobody we can find. The widow's 1840 declaration and the son's affidavit used
the journal only for dates of service; no decipherment is on any page; searches listed under Prior work found no
transcription or mention.

## The object

A pocket notebook kept by Enoch Long junior of Hopkinton, New Hampshire, a private (corporal from 16 September 1779) in
Capt. Samuel Runnels's company of Col. Hercules Mooney's regiment at Tiverton, Rhode Island, July 1779 to January 1780,
with entries of 1780. Plain entries (weather, guard, deserters, fleets, the British leaving Newport, the march home,
accounts, road lists) alternate word by word with cipher. Cipher on 17 page-sides of images 11-29 (image 17 left and
18 right are the same page photographed both ways up). The pages are photographed out of order.

## The system

**System A** (29 July - 23 September 1779, and 1780): one sign per letter, word division kept, signs that are altered
letters (a short stroke for a, a turned e, a slanted stroke for h, a dot for i, a cross for m, a dash for n, a v for r,
an ezh for s, an inverted v for v, a wave for w, an f-like sign for y). o also stands for u in some words (up, but,
upper, run). Key: `key_systemA_frozen.json` (sha256 `aaafa6c11f174bed54228fdfea8e2b4b6af32a94111f24c0cdab6c9b2803df9e`).
Sign crops: `signs/` (context crops from pass B; several are a line off, labelled by sign). Not in the frozen key: a curl
sign that ends both "ink" and "silk" on 16L (`evidence/R2_A_16L_l13-15_silk_and_ink_k-sign.png`) is probably his k
(compare the k of system B, a 2-shape); the name read as Kimball begins with the z-shaped s sign, not a k.

**System B** (from 4 October 1779): the 4 October entry (image 16 right) opens with two rows of signs and nothing else,
18 + 7 = 25 signs, with no letters written beside them. We read them as his new alphabet in alphabetical order: with 25
signs for 26 letters one letter has no sign, and we take it to be j, which the alphabets of the time did not separate
from i, so the first row runs a-s and the second t-z. The letter values are inferred from that order, not written by
him, and were then checked against words (last night, I dreamed, that, home, thought, followed, furlough, to bed). Key: `key_systemB_frozen.json` (sha256
`1a449ea4b28f51ca82f646d4b0533cc5e2af938b8686cb7879af767b879e0f0c`). Changed: t (a looped L), e (a dash), d, b, f (6),
r, u, v, w and m, y (a colon), l (a slash); + now stands for x. Crop of the key line:
`evidence/KEY_B_16R_alphabet_line_a_to_s.png`. Seen on his own rows (15 Nov 2026): m is a cursive w-shape (cups), w a
cursive m-shape (humps); z is a longer double dash. In the text he writes d as a straight slash, the same shape as l
(and, bed, shed, down), and twice uses the first alphabet's inverted v for v (love, loved).

**Signs that are easily confused on this film** (from the two readings of 15 Nov 2026, counted where they disagreed):
- System A: e and s (the "=" sign and the ezh; the most frequent confusion), i and a (a dot against a short stroke),
  a and l (short against tall stroke), f, r and y (hooked or descending strokes; "of" was read "or" again and again),
  p, g and d (loops with or without a descender), b and d, t and h, m and t (the height of a cross), u and a.
- System B: e, n and z (dashes; e and n are identical in his own rows), r and s (two ezh-like signs), m and w (cups or
  humps), d and l (both straight slashes in practice), a and l (a flag at the top or not), b and o.

## Method (who did what)

All work by Andrew Beling with AI agents, 13-15 Nov 2026. No person has checked the readings against the images.

1. **Pass A** (first agent): system A key from plain-cipher mixtures ("Last [night]", "you may [read writing where] you
   could see none", "the [countersign was Huntington]") and word patterns; key frozen from images 11, 13R, 14L, 14R;
   readings of most of 29 Jul - 23 Sep; a sign transcription of the held-out pages 15L-16L (`pass_a/`).
2. **Pass B** (second agent, blind): every cipher word transcribed as shape codes and frozen (`pass_b/passB.tsv`,
   sha256 `f76fbb51fa942e294311fe510a26a619d3637a4401322236c65a82da5df44a60`) before pass A's folder was opened; an
   independent key from the guard roster (plain "Sergt Cate, Corpl Jonson" and "For Guard" above the same words in
   cipher). The blind key gives the same letters as the frozen key for a, e, g, i, l, m, n, o, p, r, t, u, w, y and the
   pronoun I; it merged b/c/d, e/s and a/i/h and had f and v wrong. Pass B's shape codes match 48% of pass A's 116
   held-out words letter for letter and 81.5% of its signs in order (69.5% by chance).
3. **Reconciliation** (second agent): line by line on line strips of the catalog's full-size images, both keys and both
   passes open. Every cipher word is in `reconciled_transcription.tsv` (built from `reconciled_source.txt` by
   `scripts/build_reconciled.py`).
4. **Blind second reading and adjudication** (15 Nov 2026; `second_reading/`). Plan and word list written and hashed
   first (`second_reading/TEST_PLAN_blind.md`). Every cipher line (235 lines; six lines of the ink recipe kept out as
   worked examples) was cut as a crop and shown in shuffled order to eight Opus readers who had not seen any reading;
   each wrote every cipher word sign by sign. Every disagreement and every weak word (663 items) was then judged on the
   image by eight more Opus agents, shown the two readings as X and Y in random order. The worker (also an AI agent)
   then checked on the image every word of the private passages and every name, and changed 73 results
   (`second_reading/overrides.tsv`, each with its reason). Rules, fixed before the run: a word is confident only if two
   readings agree sign for sign, or its signs are individually clear, and it is English that fits; if the signs allow
   two words both are given; a word the context suggests but the signs do not support stays unread. The per-word
   record is `second_reading/second_reading.tsv`.

The confidence marks in the transcription (confident, probable, doubtful) are the author's agents' own: PRELIMINARY:
author's self-check, not a reviewer's grade. For a maintainer to confirm or replace. No `reading_review` grade is
recorded for the journal (see "Reading status and the Reading check" below).

## Tests

- **Pass A held-out test** (`pass_a/HELDOUT_TEST.md`): 105 words of 15L-16L, 84.8% dictionary words; 200 shuffled keys
  mean 5.5%, maximum 26.7%. Caveat: the same agent transcribed the held-out words already knowing the key.
- **Clean held-out test** (`pass_b/HELDOUT_TEST_passB.md`, written before running): the frozen key, unaltered, on the blind
  pass B transcription (blind applies to the transcription only: the map from pass B's shape codes to pass A's signs,
  and two names added to the lexicon, were made after pass B had seen pass A's key) of 15L, 15R, 16L, 18R, 19L, 22L and 29 (409 words): **57.9% English; 200 shuffled keys mean
  11.4%, 99th percentile 23.0%, maximum 30.3%. Pass.** Pass B's merged signs count a word as English if any expansion is;
  the shuffled keys get the same allowance.
- **Blind second reading, 15 Nov 2026** (pass mark written first): sign for sign the blind readers agreed with 399 of the
  721 words then marked confident (55%), and with **29 of the fixed sample of 60 confident words (48%; pass mark 95%:
  failed)**. Where the word lengths matched, 86% of signs agreed in system A and 75% in system B. On the weak words they
  agreed with 4 of 24 probable, 8 of 60 doubtful and none of the 4 nonsense words, and gave a reading for 192 of the 208
  unread words (65 of them an English word). Because the sample failed, every confident word in the private passages
  was judged again on the image (all lines were in the test). In adjudication the earlier reading was upheld in 114 of
  663 items, the blind reading in 325, neither in 209; 8 were illegible and 7 misaligned.
- **`docs/_validate.py`**: pass (1,494 system A signs from the confident reading, `validation.tsv`, built by
  `scripts/build_validation.py`). The signs in that file are the key's encoding of the reading; the test shows the key
  reads better than chance and than a key fitted to shuffled text, not that every sign was read right.

## How sure the reading is

Here the journal is known only from the National Archives microfilm (M804), scanned by Fold3 for the National Archives. The online images are
2064 x 2689 pixels; a lower-case letter is about 15 pixels high. The catalog serves nothing larger (its IIIF full size is
the same file) and Fold3 shows the same scan. Ink is faint in places, some lines are struck through or overwritten, and
the cipher signs are small pen strokes whose differences (a dot or a short stroke, a cross set high or low, a loop with
or without a tail) are often at the limit of the film.

All the reading was done by AI agents, in two independent readings and an adjudication on the image; no person has
checked it against the images. The two readings agreed sign for sign on only about half the words the first reading
had called confident (48% of a fixed sample of 60), so the first reading's confidence was too high. After the second
reading, of 1,041 cipher words 513 (49%) are confident, 262 (25%) probable, 60 (6%) doubtful and 206 (20%) unread. Many
probable words differ from a confident reading by one look-alike sign.

Confident share by passage (words now; confident before and after the second reading; probable, doubtful and unread
after):

| passage | words | confident before | confident now | probable | doubtful | unread |
|---|---|---|---|---|---|---|
| 29 Jul 1779, thoughts of Polly | 13 | 9 (69%) | 7 (54%) | 1 | 3 | 2 |
| 1 Aug, "my love is great" | 12 | 7 (58%) | 4 (33%) | 5 | 1 | 2 |
| 8 Aug, three letters | 44 | 36 (82%) | 24 (55%) | 13 | 2 | 5 |
| 9 Aug, invisible-ink recipe | 26 | 24 (92%) | 24 (92%) | 2 | 0 | 0 |
| 16 Aug, long dream | 135 | 99 (73%) | 73 (54%) | 39 | 5 | 18 |
| 17 Aug, father as captain | 8 | 8 (100%) | 7 (88%) | 1 | 0 | 0 |
| 20 Aug, thinking over dreams | 34 | 29 (85%) | 18 (53%) | 8 | 1 | 7 |
| 22 Aug, punishment | 18 | 11 (65%) | 7 (39%) | 5 | 3 | 3 |
| 24 Aug, accounts | 44 | 21 (48%) | 18 (41%) | 10 | 2 | 14 |
| 26-30 Aug, dream of Polly at Newbury | 72 | 59 (82%) | 30 (42%) | 16 | 8 | 18 |
| 6 Sep, dream of home | 43 | 42 (98%) | 26 (60%) | 12 | 2 | 3 |
| 8 Sep, dream at Newbury | 16 | 15 (94%) | 10 (62%) | 4 | 0 | 2 |
| about 10-15 Sep, intimate passage | 50 | 41 (84%) | 36 (72%) | 6 | 3 | 5 |
| 19 Sep, silk gown and white ink | 31 | 29 (94%) | 19 (61%) | 10 | 1 | 1 |
| 23 Sep, dream of home on furlough | 25 | 23 (92%) | 16 (64%) | 4 | 1 | 4 |
| 4 Oct, intimate passage | 36 | 32 (86%) | 21 (58%) | 8 | 1 | 6 |
| 6 Oct, dream (earlier read as of his mother) | 26 | 22 (85%) | 13 (50%) | 5 | 4 | 4 |
| about 8 Oct, coming away | 40 | 30 (77%) | 29 (72%) | 5 | 1 | 5 |
| 8 Aug, prayer | 32 | 15 (47%) | 13 (41%) | 10 | 3 | 6 |
| 12 Oct, accounts | 7 | 0 | 0 | 2 | 3 | 2 |
| 22 Oct, "I think of my Polly" | 28 | 14 (50%) | 8 (29%) | 9 | 2 | 9 |
| image 28, accounts | 11 | 3 (27%) | 0 | 4 | 1 | 6 |
| 28 Jun 1780, "your sweet heart" | 13 | 8 (62%) | 4 (31%) | 2 | 1 | 6 |
| 27 Jul 1780, dream at his uncle's | 89 | 55 (62%) | 34 (38%) | 26 | 5 | 24 |

The most private passages are among the least certain where it matters most: the words a reader would look for (the
name on 4 October, the word after "my" on 6 October, the words after "laid with my", the man punished on 22 August)
are unread or doubtful, and every passage is printed with each doubtful or unread word marked. The journal texts are
generated from the word-by-word file (`scripts/build_journal.py`), so the running text cannot say more than the
transcription.

## Settled on the image, and what the second reading changed

- **Polly.** In the first alphabet the name begins with the looped p (with a descender) in four places read by the worker
  on the image: 13R l4, 15L l16, image 11 l2 and l3 (`evidence/NAME_A_*`, `R2_A_13R_l4_*`). In three more (15R l11, 22L
  l11 and l16) and in the second alphabet on 25L it is probable. On 15R l3 the first sign is a loop with a curl and no
  descender, d rather than p (Polly or Dolly). On 16R l8 (4 October) the signs read l or d, a, l, l, y: **the name there
  is not Polly on the signs** and is left unread (`evidence/R2_B_16R_l8_*`). Both Polly and Molly are pet forms of Mary;
  the 1840 extract of the 1784 marriage entry in the file says Molly Kimball.
- **Kimball.** In both places on 13R the surname's first sign is the z-shaped s sign; the rest reads i m b l l (no a).
  "Kimball" rests on the marriage record, not on the signs, and is marked doubtful (`evidence/R2_A_13R_l4_*`). The
  second Kimball's first name (13R l3) reads l, a or o, v, i, d or f: not settled.
- **Invisible ink, 9 August 1779** (13R): every word settled, unchanged: "I wrote in my letter to my dear this, if I
  send you a letter with the upper part plain rub it with your hot box iron and you may read writing where you could see
  none." On 19 September (16L): "I sent her a letter [yesterday??] wrote with white [ink?]" (the interlined word is too
  small to read in full; "ink" ends in the probable k sign).
- **10-15 September (16L)**: "I was on century [sentry] by the river", not "on sentinel of the river"; "the house &
  Hannah [...] her", a name not read before (h a n n a h, six clear signs; both readings agree).
- **4 October (16R)**: "[she??] went to bed and I followed [after?]": "bed" stands (b, e and the straight-stroke d), "her"
  after "followed" was a misreading of a word that reads "after".
- **6 October (17L)**: "my mother was married" is **withdrawn**. The word after "my" has about seven signs (m or w, o, a,
  r or s, r or s, ...) with no t or h sign, so it is not "mother"; the word after "was" reads m or w, a, r or s, d or l,
  e, d or l: not "married" (`evidence/R2_B_17L_l3-4_*`). Both are left unread. "he was loved" at the end of the entry is
  clear.
- **22 August (14R)**: "whipt" is not on the image. The entry reads "[... 3] [had?] to [run?] the [gantlet??]
  through the [company??] for [going/getting??] to [sleep?] on [his?] post": a man made to run the gauntlet, the word
  itself doubtful (`evidence/R2_A_14R_l21-22_*`). His name is not read.
- **8 August prayer (image 29)**: "the sabbath [of?] the lord", "glory and honour to the", "heaven" are now read
  (sabbath, lord, glory, honour, heaven checked by the worker on the image).
- **Accounts, image 28**: "I owe" is not supported; the creditor is not read.
- **14R**: "the night before last I dreamed that father was come to us, the [Capt?] of a company" stands.

## Independent check (14 Nov 2026)

A second AI agent of ours solved the first alphabet from the images before seeing our key and agreed with it on all 21
letters, compared readings word by word (43 of 45 agree), and reran both held-out tests and `_validate.py` with
identical results (`output/push_2026-11-13/verify/long1779_VERIFY.md`, outside this repository). Its corrections were
applied on 14 Nov; the second reading of 15 Nov revised some of them ("silk" and "yesterday" are now probable and
doubtful; "she" before "went to bed" doubtful).

## Reading status and the Reading check (15 Nov 2026)

The repository's rules (`CONTRIBUTING.md`): "A document counts as read only when 95% of its words read as sense (the
README read bar); one that builds coherent sentences under that is marked "read in part"." and "A document that decodes
but does not yet build sentences can still be sent, marked "decoded, not read"". After Daniel Bourdeau's review of PR
#670 (15 Nov 2026, his first option), `outcome.texts` has two entries. The **ink recipe of 9 August 1779** (image 13
right, lines 11-16; `ink_recipe_1779-08-09.md`) is its own entry, **read**: its 22 cipher words are all read with
confidence and nothing in it is a hole, guess or supplied word (`read_share` 1.0); the review reports that all 22 agree
on NARA image 13 read with the alphabet A key. The **rest of the journal** is **decoded, not read**: 491 of its 1,019
cipher words are confident (48.2%); 513 of 1,041 (49.3%) for the whole journal. Our earlier `read_share` for the
journal as one entry, 0.752 (`research/reading_audit/v2_score.py`, probable words counted as holes), included the plain
text. The target stays read in part.

A "read" or "read in part" entry requires a `reading_review` graded A or B, "recorded by the reviewer, not by the
author of the reading". For the recipe the reviewer gave grade A in the review of PR #670 (16 Nov 2026; a model
reviewer, no person has checked it); it is entered in `profile.json` verbatim, at the reviewer's request. For the
journal our agents never wrote one, and none is added now: grade A ("coherent with scattered
holes") does not fit a text whose sentences mostly hold more than one hole in ten (`_check_reading.py` clean share 0.47
on `journal_as_written.md`, 0.45 on `journal_modernized.md`), and grade B ("coherent but raw") would assert a coherence
that the failed blind check (48% of a fixed sample of confident words reproduced, against a mark of 95%) does not let
the author's agents vouch for. The journal entry, decoded, not read, needs none.

**Holes are counted by words.** `CONTRIBUTING.md`: "Holes are counted by words: `[...]` is one unread word, and a hole that
covers more carries its size, `[... 4]` for four unread words; ... a mark whose extent you cannot tell stays bare and is
listed there as "extent unknown"". In both journal files, generated by `scripts/build_journal.py`, a run of unread cipher
words is one mark with its size, counted from the "?" tokens of `reconciled_source.txt` (one per unread word): 156 marks
covering the 206 unread words (128 single, 25 of two, 11 of three, one of four). An interlineation, a struck word or a
plain word ends a run. **Extent unknown**: each bare `[...]` in plain text (plain words the first agents did not
transcribe: 31 places, on images 13R, 15R, 16R, 23, 24, 25R, 28, 31 and the 24 August and 21 October plain entries),
the struck heading on image 19 left, and the vertical margin column of image 11 (about 30 signs). The sentence score
rose from 0.456 to 0.466 with this change only because `_check_reading.py` counts a mark, not its size; no reading changed.

## Results

`journal_as_written.md` (his spelling, cipher marked) and `journal_modernized.md`, both generated from
`reconciled_source.txt` by `scripts/build_journal.py`.
Share read (cipher words, `reconciled_transcription.tsv`): 1,041 counted. **Read with confidence: 513 (49.3%).**
Probable 262 (25.2%), doubtful 60 (5.8%), unread 206 (19.8%), nonsense 0. Confident and probable 74.4%; 80.2% including
the doubtful readings. These are upper bounds: unread stretches may hold more words than counted, and image 11's margin
column (about 30 signs) is not counted. Before the second reading: 743 confident, 24 probable, 60 doubtful, 208 unread,
4 nonsense of 1,039 (two words dropped where no sign is on the image, four added where the second readers found one).

## What he hid

*What the journal says, as now read.* In cipher: his dreams, nearly every cipher entry ("last night I dreamed ..."), of
home, of Newbury and an uncle's house there, of his father coming to camp as a captain; his love for Polly ("my true love
Polly [Kimball??] the joy [of?] my [eyes?]"); his letters home; the invisible-ink recipe and a letter written "with white
[ink?]"; a prayer; and a few camp matters (the night's countersign, a man made to run the [gantlet??] for sleeping on his
post, news that the regulars were sent for to the West Indies). The 6 October dream mentions someone after "my" whose
name or word is not read. In plain: dates, guard turns, the company list, deserters, the Hessian sentinel taken by boat,
enemy strength, prize ships, d'Estaing bound for Georgia, the British loading their cannon and leaving Newport, the
march home, and his accounts. The line runs through single sentences.

*Established history.* NH State Papers vol. 15 (Rolls II, ed. Hammond, 1886; Internet Archive `rollsofsoldiersi02hamm`):
p. 654, the House vote of 23 June 1779 raising 300 men in six companies for Rhode Island under Col. Hercules Mooney,
Capt. Samuel Runnals of Durham among the captains; p. 663, the enlistment of 5 July 1779 signed by "Enoch Long Jr",
Hopkinton; pp. 684-685, [5-288] "Pay Roll of Cap Saml Runnels Compy in Col Herc Mooney's Regt ... defence of Rhode Island
1779": **Enoch Long, Private, engaged July 5, promoted Corporal Sept 16, discharged Jany 13 [1780]**; the same roll has
James Runnels promoted Ensign on Sept 16 (the journal: "Sergt Runnels promoted to an Ensign", entered 25 Sept), Andrew
Cate serjeant and James Johnson corporal (the roster's "Sergt Cate, Corpl Jonson"). Vol. 16 p. 694: Hopkinton paid
Enoch Long Jr £30 bounty and £12 travel to Providence, 14 July 1779. Command in Rhode Island: Horatio Gates, who
reached Providence on 3 April 1779 after Sullivan left for the Six Nations expedition, and left on 8 November 1779
(editorial notes, Papers of George Washington, Founders Online, Washington/03-20-02-0559 and 03-23-02-0184). The British
left Newport on 25-26 October 1779; the journal records the embarkation on the 25th and the march into Newport on the
27th. Lord (1890), pp. 372, 428, 550: marriage of Enoch Long jr and Molly Kimball, 22 Jan 1784; their son Isaac; the
father Enoch Long a cooper from West Newbury, Mass.

*Inference.* "Newbury" is the family's home town. The second alphabet, written into the notebook itself, guarded against
a casual reader in camp, not against loss of the key; the change may mean he thought the first had been seen (not
established).

## Prior work

Searched 13-14 Nov 2026: HathiTrust full text (Chrome; "journal of Enoch Long" no hits; "Enoch Long" with cipher,
Hopkinton, journal: Lord's town history first, which mentions him but not the journal), Google Books ("Enoch Long"
Tiverton 1779: no hits), Internet Archive metadata and the full text of NH State Papers vols 15-16 and Lord (1890),
NH Historical Society collections catalogue (no Long journal), Southern Campaigns Revolutionary War Pension Statements
(no file w16138), genealogy sites (WeRelate; other Enoch Longs). No transcription or mention of the journal or cipher.

## Remaining gaps

- 206 unread and 60 doubtful cipher words - blocker: illegible; listed with their legible signs in
  `second_reading/second_reading.tsv`; no sharper image online (catalog full size and Fold3 checked 15 Nov 2026).
- Image 11, boxed lines and insertions of 3-8 Aug 1779 and the vertical margin column - blocker: illegible; overwritten
  and boxed on the film.
- Names - blocker: illegible; the 4 October name, the second Kimball's first name, the man punished on 22 August, the
  creditor on image 28, "Nessy" (23 Sep) and Uncle "Bartlett" (doubtful).
- Words after "my" and "was" (6 Oct) and after "laid with my" (8 Oct) - blocker: illegible; look-alike signs (m/w,
  r/s, d/l) that the film does not separate.
- Groups the second readers saw that are not in the transcription - blocker: needs-physical-access; listed in
  `second_reading/second_reading.tsv` and the "B-" items in `second_reading/adjudication/`, for a reader with the
  original to place.

## Escalation

- [n/a] siblings: a private journal in a pension file, not a letter series; the rest of the file (the widow's
  declaration, the son's affidavit, the clerk's wrapper) carries no decipherment (see "Who read it before").
- [x] clear-pages: the plain entries and the plain-cipher mixtures were used to recover alphabet A; the 4 October
  alphabet line gave alphabet B.
- [n/a] known-keys: a private cipher of his own; no other key of Long's is known.
- [x] print: printed editions, state papers, the town history and full-text libraries searched (see Prior work); no
  transcription of the journal found.
- [x] key-rebuild: two keys made independently (pass A and the blind pass B) and compared; key B checked against words.
- [x] retry: every cipher line read again blind on 15 Nov 2026 and every disagreement and weak word adjudicated on the
  image (`second_reading/`).

Tried: two passes, one blind; reconciliation; a second blind reading of every line with adjudication on the image; line
strips up to 4x; both keys; context. No sharper image exists online. Next: the original notebook in the pension file at
the National Archives in Washington (Textual Reference, Record Group 15), where a person can read the strokes the film
loses (dots, cross heights, loops and tails) and settle most of the look-alike pairs above. A human check of the
readings against the images is owed before a site page.

## Files

`key_systemA_frozen.json`, `key_systemB_frozen.json`, `reconciled_source.txt` (the authority), `reconciled_transcription.tsv`,
`ciphertext_systemA.txt`, `ciphertext_systemB.txt`, `journal_as_written.md`, `journal_modernized.md`,
`ink_recipe_1779-08-09.md` (the 9 August 1779 recipe, its own entry in `outcome.texts`), `validation.tsv`,
`signs/`, `evidence/`, `pass_a/`, `pass_b/`, `second_reading/`, `scripts/` (`build_reconciled.py`, `build_journal.py`,
`build_validation.py`, `heldout_passB.py`), `profile.json`.
