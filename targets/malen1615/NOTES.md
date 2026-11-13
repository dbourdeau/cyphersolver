# J. van Malen to his brother Van Malen de Bautersem (catalogue 2532)

Gelders Archief (Arnhem), 0372 Huis Ammerzoden, inv. nr. 52: two letters, 8 scans (NL-AhGldA_0372_52-0001 to -0008).
Permalink: https://proxy.archieven.nl/0/69A9B00BC5F844C596AD986F5A60678C (archieven.nl viewer). No scans in git.

Status: in progress (not yet written up). Letter 1 read in part, letter 2 decoded, not read (12-13 Nov 2026); the
Dutch passages of letter 2 are not transcribed and escalation steps remain open (see the end of this file).

## Documents

| doc | scans | date | language | cipher | state |
|---|---|---|---|---|---|
| malen1 | 1-3 | "28e de Xbre" (no year; the inventory gives 1615-1619) | French | opening word, 3 lines at the foot of p. 1, 26 lines on p. 2 (clear words between), place name on p. 3 | read in part |
| malen2 | 5-8 | 21 October (from the catalogue entry, not checked on the scan) | French opening, then Dutch | about 14 lines on p. 1 and 5 on p. 2 | decoded, not read |

The two letters have the same writer, the same recipient and the same key, so they go in one target folder.

## System

Letters are replaced by invented signs (Greek-like letters and figure-like signs), with a few homophones. Word breaks
are mostly kept. We found 23 signs: a L; b F, U; c W; d Z; e D, O; f N; g M (two joined o's); h Q; i/j P;
l C (cursive x); m I; n E; o Y; p G; q K; r T, V; s X (straight x); t H; u/v A; y R. We did not find k, w, x or z.
Some numbers are written as figures inside the cipher: 3 distinct numbers with 4 occurrences in letter 1 (60 once,
59 twice, 68 once) and, in the part of letter 2 transcribed so far, 59 once. They look like code numbers for persons
or powers and are not identified (`de la mageste 59`, `l'ambassadeur de 59`). Letter 1 has 781 cipher signs
(5 unread, 2 `&`), letter 2 so far 179 (`scripts/signs.py`).

## Key source

There is no key, no gloss and no clear copy on any of the 8 scans. We found the key ciphertext-only on letter 1,
p. 2. The clear word `Monsieur` comes before a 12-sign word with the pattern of `lambassadeur`: one sign at
positions 2, 5 and 8, and a doubled sign at 6-7. That gave a, s, d, e, u, r, m and b. The words `aultre`, `faict`,
`qu'ils`, `laisseront` and `nous` gave the rest. The key was frozen as `key_frozen.tsv` after p. 2 (L05-L32).
`key_frozen.tsv` has 23 entries, one per sign, under two comment lines; `key.tsv` is the same file, because no value
was changed after the freeze.

## Held-out test

See `heldout.md`. Letter 1 pp. 1 and 3 and the first eight cipher lines of letter 2 were transcribed after the
freeze. With the frozen key, 54 of their 58 words come out as French words that fit the context. One is wrong
(`voy` for `vos`) and 3 are holes from faint signs, so 54 of the 55 legible words (98%) decrypt correctly.

## Transcription

Pass 1 of p. 2 (`transcription_malen1_pass1.txt`) was made from 1.5x crops before any value was tried. It merged the
straight and the cursive x, the two hooks, and the single o and the joined oo. Pass 2 (`transcription_malen1_pass2.txt`,
reconciled as `transcription_malen1.txt`) separates them by shape on fresh 1.5x-1.6x crops. Pass 2 was made after
the first key hypothesis, so that separation is not blind. Pages 1 and 3 have one pass only. An independent blind
transcription is still needed.

## Reading (letter 1)

The reading is in `reading_malen1.md` and the English in `translation_malen1.md`. `scripts/check_marks.py` rebuilds
the decryptions from the transcriptions and the frozen key and checks that every departure is marked: PASS.

Letter 1 has 165 cipher words. 154 are verbatim from the signs (93.3%). 3 have a marked repair (`d'{i/h}ollande`,
`donnera{+i}en{+t}`, `{-m}aultres`), 3 are guesses (Rees, Anholt, sieges) and 5 are holes (faint signs and the two
`&` signs). No word comes from a gloss. The share is below 95%, so the state is `read in part`.

We ran Dan's checker (`docs/_check_reading.py --file`, origin/main of 12 Nov 2026). On the running text of letter 1,
13 of 17 sentences are clean (0.765). The whole reading file scores 0.606, because its marked block counts the line
ids and the marks. `decryption_malen1.txt` scores 0.531, because its words run together.

Content: Van Malen thanks his brother for good news. He thinks the Jülich dispute will be settled only by arms. He
calls it a mistake to think that 60 or 59 will let themselves be crowned by 68 out of regard for their
confederation. "They" threaten to break the truce, but "we" do not tremble: let them begin, our camp waits for
nothing else. He expects little difficulty over the restitution of the town of [Rees]. He calls the reports of the
embassies of the baron [Anholt] inventions of "those gentlemen of Holland", and says the [sieges] are indeed made in
the name of His Majesty 59. He also mentions the league of the marquis of Brandenburg and others, errands done with
the Spanish ambassador, and a safe-conduct and letters of recommendation. The date line reads "De Londres le 28e de
Xbre": the place name is in cipher and decrypts as `londres`. No historian has checked this reading, and we do not
date the letter more closely here.

## Letter 2

Only the first eight cipher lines (scan 5, the French opening) are transcribed, in one pass from 1x crops, and
decrypted: "... laquelle j'ay communicque a monsieur l'ambassadeur de 59, qui a este aussi fort aise d'avoir vo{y/s}
bonnes nouvelles. ... 12 florins par mois a la personne que dictes, pourveu qu'il nous chasque huict face avoir ses
nouvelles. Voire il promet de luy bailler ... jours". `reading_malen2_partial.md` gives this as a working text, not as
a reading. The Dutch cipher passages (lower on scan 5 and on scan 6) are not transcribed. A first look at them shows
Dutch words (`dat`, `hem adviseren dat hy`), so the same key applies.

## Remaining gaps

- Letter 2 Dutch passages (scans 5, 6) - blocker: not-attempted; to be transcribed in two passes and read with the
  same key.
- Letter 1: an independent blind transcription - blocker: not-attempted; the X/C, Y/R and O/M splits were made with
  the key in mind.
- Letter 1: faint signs at the right edge of p. 1 (L02-L04) - blocker: illegible; faint on the image at full size.
- Letter 1: the two heavy `&` signs (L22, L29) - blocker: open-codes; not in the alphabet, may be code signs.
- Letter 1: the guesses `reses` (Rees?), `aneot` (Anholt?) and `ciieges` (sieges?) - blocker: not-attempted; not
  checked against other sources.
- The code numbers 59, 60 and 68 - blocker: open-codes; not identified.
- The year of either letter - blocker: not-attempted; the inventory gives 1615-1619.
- Clear script of letter 1 - blocker: not-attempted; read only to place the cipher. Points raised at the
  independent review, not yet checked on the image: `je pense qu'il n'aurat de la difficulte` is translated "there will be no
  difficulty", which depends on the clear words; `Et m'a faictes la moindre doubte` may be `Et n'en faictes ...`;
  `practiques des de ces messieurs` has a doubled article (clear `des` before cipher `de ces`).

## Independent review (13 Nov 2026)

An AI language-model agent that had not worked on the solve checked the files. It copied seven lines (L03, L04, L07,
L14, L18, L19, L33; about 200 signs) from the scans by shape before opening the transcription and found no
value-changing disagreement (one D/O doubt in L07, both e). It reproduced `check_marks.py`, the held-out result and
the reading checker (13 of 17 sentences clean on the running text), and read the reading against the translation.
It graded letter 1 B, `read in part`, and kept letter 2 at `decoded, not read`. It found one error, fixed here: the
header of `key_frozen.tsv` named the wrong freeze range (L05-L14). This is not a second blind transcription.

## Prior art (checked 12 Nov 2026)

We ran two web searches: "van Malen" Bautersem Steenbergen drossaard 1615, and Huis Ammerzoden archief "van Malen"
brieven geheimschrift. Neither found an edition, study or decipherment of these letters. The catalogue vetting of
11 Nov 2026 found nothing in DECODE, Cryptiana or the HistoCrypt papers. We did not check printed inventories of the
Ammerzoden archive beyond the online inventory note.

## Images

The scans were fetched on 12 Nov 2026 through the archieven.nl viewer in headless Chromium (`scripts/fetch_scans.py`).
The viewer loads Zoomify tiles from preserve2.archieven.nl. We fetched those tiles one request at a time and stitched
them at full size (2904x4080 and 3000x4097). The IIIF image URLs in the manifest answer "Geen rechten", and we did not
use that route.

## Method and credits

WAINUT (lccompany) set the task. AI language-model agents transcribed the letters, found and froze the key, ran the
held-out test and made the reading. No human palaeographer or historian has checked the text.

## Escalation

- [x] siblings: all 8 scans of inv. 52 opened; letter 2 uses the same key; other inventory numbers of 0372 not opened
- [x] clear-pages: all 8 scans viewed; no decipherment, gloss or clear copy of the cipher passages on them
- [x] known-keys: no known key of this writer or archive; DECODE and Cryptiana searched in the vetting of 11 Nov 2026
- [ ] print: two web searches only; printed inventories of the Ammerzoden archive not checked
- [x] key-rebuild: key rebuilt ciphertext-only, all 23 signs valued; the code numbers 59, 60, 68 and the `&` sign open
- [ ] retry: faint signs of L02-L04 not retried beyond the first crops; letter 2 Dutch passages not transcribed

## Integration check (13 Nov 2026)

- Reproduced: `scripts/check_marks.py` PASS (154 of 165 words verbatim, 3 repairs, 3 guesses, 5 holes), `signs.py`
  (781 and 179 signs), `_check_profile.py` valid, `_check_reading.py` as quoted in the PR. An independent decoder written
  from `key_frozen.tsv` reproduces `decryption_malen1.txt` on all 33 lines.
- Images: scan 2 fetched on 13 Nov 2026 (Zoomify tiles, one request at a time). The line layout, the word counts and the
  clear words of L07-L10 agree with the transcription; signs are not separable by eye at that scale between the paired
  shapes (X/C, Y/R, D/O), so no sign-by-sign blind comparison was made. The X/C, Y/R and O/M splits stay the open gap.
- Strict share: 154 of 165 = 93.3% (the contributor already counted strictly). With the 4 unresolved code-number
  occurrences (60, 59 twice, 68) counted as holes it is 154 of 169 = 91.1%. Letter 2 has 8 of about 19 cipher lines
  transcribed, so the whole target is lower. Class: read in part.
- The held-out test is ordered by the contributor's record (single commit); the freeze header names L05-L32, and the
  X/C split in the held-out lines was made with the key in mind (stated in `heldout.md`).
- Duplicates: no other target covers Gelders Archief 0372 inv. 52 or the Van Malen letters.
- The Dutch cipher passages of letter 2 and a blind transcription are workable, so the target stays in progress with
  no page.
