# radziwill1656: Bogusław Radziwiłł's two ciphered German postscripts, Tykocin 13 Mar 1656 and Labiau 3 Dec 1656 (catalogue 1594)

Status: in progress (intake of 24 Nov 2026; no page yet; the held-out test cannot be recomputed here until the contributor sends the run ids). Next steps: the contributor's run ids or scoring script, then a re-read of the hole words on the scans, which open in Chrome since 24 Nov 2026.

Contributed by SeldomPhooey (issue #784, 18 Nov 2026): transcription, key, decryption, reading and translation, made by
his statement with Claude-family AI agents. Checked and filed here on 19 and 24 Nov 2026 by the maintainers' AI agent.
No person has read the German or compared the transcription with the manuscript. His issue text is kept unchanged in
`prior/issue784_SeldomPhooey_2026-11-18.md`.

By the README read bar both postscripts are deciphered in part: 71 of the 106 cipher words of A and 60 of the 99 of B
count as read (67.0% and 60.6%; `count_reading.py`, 24 Nov 2026). The key was recovered from the ciphertext alone by
his account. Our reply of 19 Nov 2026 gave "about 79% of A and 82% of B from your own lists": that was an estimate
from his list of uninterpreted words and is replaced by the count here.

## Documents

AGAD (Archiwum Główne Akt Dawnych, Warsaw), Archiwum Warszawskie Radziwiłłów (zespół 354), dział IV, unit 46:
1/354/0/4/46, "Bogusław Radziwiłł", 76 scans in 25 objects on
[szukajwarchiwach, unit 17873460](https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/17873460).

- **A.** Object 16, scans 42-43 (old ff. 40-41): "Post Scriptum", signed "Signatum Tykocin" on 1[3] March 1656 (the second
  figure of the day is uncertain). This is the item of catalogue entry 1594. 112 cipher runs, 673 two-digit groups.
- **B.** Scans 39-40 (old ff. 37-38): "P. S.", "Labiau den 3. Decembris 165[6]" (the last figure is underlined and read
  as 6; the docket reads "Datiert Labiau d. 3. Xbris Ao. 56", by his reading). Scan 39 has a four-line note written
  vertically in the left margin; scan 40 is a separately signed sheet. 102 cipher runs, 598 groups. Not in the catalogue
  before the issue.
- Scan 41 is a cover, used by him for the addressee only.

German, with the secret words in digit runs among clear words. The addressee is not named on the postscripts. He takes
him to be the commandant at Słuck, Major Jan Gross, from the cover (scan 41), the run of letters to Gross in the same
unit and the words "Herr Maior" and "Slucko": an inference, not checked here.

Not covered: the "dodatek cyfrowany" of Dec 1769 (Karol Stanisław Radziwiłł, 1/354/0/4/261/17), a different cipher
that the catalogue entry split off; and seven further letters to Gross in units 46-47 (Feb 1656 to Aug 1657), which
he says the same table reads but for which he offers no readings.

## System and key

A simple substitution: two-digit odd numbers 11 to 57 in alphabetical order, a = 11 to z = 57, with i and j on 27 and
u and v on 49. The digits of a run are written without breaks. An overline over a group doubles the letter; the
transcription writes the group twice (33 33 = mm). No nulls, homophones or code numbers are reported. `key.tsv`:

- 19 numbers carry no mark in his table: by his account they were fixed by the frozen test below. He writes "the 20
  values without a mark"; the table in the issue has 19 (the frozen table also held 53, as k).
- 29 = k and 39 = p are proposed from context (sluc-29-o for Slucko, cores-39-ondentz) and from the alphabetical order.
- 53: his frozen table gave k; the context (wala-53 beside the clear "Wallax") and the order point to x. Proposed.
- 41 (q) and 55 (y) do not occur.

The table is a reconstruction. No period key was found.

## How the key was tested

His record (issue #784), not recomputed here:

- Test 1, held-out. A had 112 runs and 675 groups as first transcribed (673 after the corrections). The table was built
  from "construction runs" only, frozen, and scored on 48 held-out runs (265 letters) against a German word-coverage
  threshold set in advance: held-out score 0.839, threshold 0.325, best of 20 within-run shuffles 0.184. A synthetic
  positive control passed. The issue does not say how the table was built from the construction runs.
- Tests 2 to 4, exposed. The unchanged table also reads B and the seven further letters to Gross; those transcriptions
  were made by someone who knew the table, so they show that the key carries over and are not independent checks.

What was run here:

- `decode.py`, written from his key table and not from his scripts: all 214 runs (1,271 groups) decode to his
  decryption column, 112 of 112 in A and 102 of 102 in B (19 Nov 2026, again 24 Nov 2026).
- The house statistical validation (`python docs/_validate.py radziwill1656`, 24 Nov 2026, `validation.tsv`, model
  de-1640s, order 4, no n-gram across two runs): 1,256 read groups of 22 kinds score -2.275 per letter; 200 random keys
  of the same shape average -6.835 (z 6.2); a key annealed onto the shuffled ciphertext reaches -4.170 at best (mean
  -4.281, z 23.7); the same annealer started from random keys on the real ciphertext reaches -2.275. Verdict: pass.
  This tests the table against chance and overfitting. It does not test the transcription, the three proposed values
  one by one, or the reading of any word.

## What the postscripts say

From his summary; where a point rests on a word that is not understood, he says so.

A. The Major is told how the Lieutenant-Colonel (written wala-53 and, in clear, Wallax) is to be relieved of the
command at Słuck. The letter relieving him is not to be handed over until men of a regiment (nimirischen, not settled)
have been dealt with (the verb is not understood). The handover is to pass with nothing untoward. Money is at hand in a
sum but cannot be sent safely. Some 1000 gulden are named with a Herr stratn mirs-29-i and the Amtmann at Słuck,
apparently for pay. Slow-matches are at hand. The Confederates and a flying army are mentioned. Wallax is to be told
of an arrest and to stay at Słuck over actions that offended the nobility without Radziwiłł's order; he keeps his
sword and is to be watched.

B. Herbacewski (herbacews-29-i) is reported to keep secret correspondence with his brother-in-law Judycki
(iudic-29-i) and to seek to betray the fortress. The Major is to hold him under arrest in the castle, discreetly and
on Radziwiłł's order. Grain and other victuals are to be listed and used for the garrison. A sum of up to 6000 gulden
is named. The margin concerns a dead lieutenant, the regiment and Herbacewski's wife, who may stay in the town. On scan
40 two doctors who asked to live at Słuck are to be received in the castle but are to keep no correspondence elsewhere.

His context, not checked here: Radziwiłł's clear letters in the same unit (obj. 14, 28 Feb; obj. 18, 6 Apr; obj. 17,
17 Apr 1656) record that Wallax was relieved, that the command passed to Gross and that Wallax had begun hostilities
without authority. A letter of Samuel Leźnicki, Słuck, 29 Jan 1657 (AGAD AR dz. V 8451) names a "P. Harbacewski". He
notes that this agreement concerns content only and does not validate the decipherment.

## Counts

`python count_reading.py`, 24 Nov 2026, by the README rule (cipher words only, sure words only). A cipher word is a
word written wholly or partly in cipher, in the first of the two divisions where his readers disagree. It is a hole
when he marks it as not understood or uncertain, when it has a group 29, 39 or 53, when it has a group he could not
read, or when it has one of the 18 groups his second pass left unresolved. `words.tsv` has one row per word.

| document | cipher words | holes | sure | share | marked by him | proposed value only | unreadable group | unresolved group |
|---|---|---|---|---|---|---|---|---|
| A | 106 | 35 | 71 | 67.0% | 27 | 4 | 3 | 1 |
| B | 99 | 39 | 60 | 60.6% | 22 | 12 | 4 | 1 |

Both are under the 95% bar, so both are deciphered in part. The same counts come out of the house measure
(`research/reading_audit/v10_relabel.py` on `reading.md`, cipher words in bold).

For comparison only: with the 16 words whose single doubt is a proposed value taken as read, A is 75 of 106 (70.8%)
and B 72 of 99 (72.7%); with the second division, A is 71 of 107 and B 61 of 99; with the 15 words that are counted
as read but still carry a doubt mark on a group in his table as holes, A is 64 of 106 and B 52 of 99.

Checks made by the same script: the cipher words of `reading.md` are, in order, the cipher words of his full text; their
letters are the decryption of the transcription group for group, except at one place where his own text and table
differ (the faint run A056 at line 42.19: `##ig` in the table, `###` in the full text). A one-off comparison found all
301 words of A and 287 of B in `reading.md`, clear and cipher, equal to his text.

Other small differences inside the issue: the unreadable group of run B003 (39.02) is not in his list of the 18
unresolved groups; his line numbers skip 40.06; the context cell of run B016 has "laengst d" where his full text has
"laengst dass"; his tables keep 81 doubt marks (66 groups written NN?, 15 unreadable) although the second pass is said
to have settled all but 18.

## Image check of 24 Nov 2026

On 19 Nov 2026 the archive's viewer blocked us and nothing was compared. On 24 Nov 2026 curl still got the bot-check
shell (Imperva), but the unit page opened in Chrome, and the largest images it serves (scan 42: 1677 x 2622 px, scan
39: 1522 x 1894, scan 40: 1513 x 1885, scan 43: 1666 x 2606) were read on screen in enlarged crops by the AI agent,
with his table in hand. So this is an exposed check, not a blind transcription, and it covers part of the text.

Places compared, group for group:

- Scan 42, lines 1 to 5 (runs A001 to A016): as he has them, with the overline on the 33 of A005 and no extra group in
  A016.
- Scan 42, lines 10 to 13 and 31 to 37 (A026, A028 to A030, A033, A038, A084, A088, A091, A093, A094, A097, A100, A103,
  A104): as he has them. In A088 the fifth pair is a clear 29 (sluc-29-o).
- Scan 43, lines 1 to 3 (A107, A109, A111, A112): as he has them.
- Scan 39, lines 2 to 9 (B001, B004 to B026, B028, B030, B032): as he has them. B001 has a small 4 raised above the line
  before the 7, which he reads as 47.
- Scan 40, lines 7 and 8 (B095 to B099, B101): as he has them.

About 70 of the 214 runs. No group was found that clearly differs. Three places where the scan may read otherwise;
nothing is changed for them:

- A031 (42.11), first pair: 45 as he has it, or 43; not told apart here. 43 would give raich after the clear "über".
- A018 (42.06), third pair: 45 or 47, as he says himself; 47 would give notig.
- B029 (39.08), sixth pair: he has 25 (h). The first digit looks like the crossed 4 of the 43 in the same run, which
  would make it 45 (s) and the word expres-s-. The last pair runs into the gutter shadow.

Two clear words looked different from his reading and were not pursued: "ankombt" for his "ankommen" (42.12) and "Er"
for his "Ihr" (43.02).

## Prior art

His search (issue #784): this repository on 17 Nov 2026; the rest of unit 46 and unit 47 (scans 1-93) for a period
copy or decode; the correspondents' papers he names; archive.org full text. No decipherment, decode or plaintext copy
found. Kotłubaj, *Galerja nieświeżska portretów Radziwiłłowskich* (Wilno 1857), read for the life of Bogusław (pp.
168-176): three letters to Gross summarised on p. 173 (24 Jul 1656, 14 Jul 1657, 29 Dec 1657), neither of these two.
Not read by him: Wasilewski 1979; the Polona copy of Kotłubaj. He makes no claim of first decipherment.

Catalogue vetting of 3 Nov 2026 (entry 1594): not on DECODE (harvested dump), no hit for Radziw on Tomokiyo's cryptiana
or in Lasry's GL.htm, no print found; the Słuck garrison study in AGAD Miscellanea t. 29 and Przegląd Historyczny 1956
came up and were not opened. Nothing was added to this search on 24 Nov 2026.

## Credits

In his own words (issue #784): "How to credit you: SeldomPhooey". A personal name was not given; the handle is used.

- "Transcription of the digit groups, the key recovery and its frozen held-out test, decoding, the image checks of
  corrections, word division, reading, translation and the literature checks were done by Claude-family AI agents
  (Anthropic), using Python scripts for the key test and the decoding. Transcription, decode and division were all done
  within one model family; no human cryptographer or historian, and no other model, has checked this work."
- "Catalogue entry 1594 found the postscript, viewed scans 41-43, saw that the digit runs stand for the secret words
  of a German text, and recorded the prior-art checks ... Its `verify` field said: view the scans, measure the cipher,
  look for a key in the same fonds. We followed that route."
- "We do not know whether these letters were deciphered before ... We make no claim of priority or originality."

He is credited for the solution and for the transcription (`profile.json`, `contributors.json`). Catalogue entry 1594
came from this project's Chrome pass of Nov 2026.

## Not checked here

- The held-out score 0.839: his scoring script, word list and the ids of the 48 held-out runs were not sent.
- The transcription as a whole: about 70 runs were compared on the scans (above); the others were not.
- The seven further letters in units 46-47 and his statement that the table reads them.
- His clear-text reading, word by word, and his translation against the German beyond the integration reading.
- His historical context and his literature checks.
- No person has read the German. The `reading_review` in the profile is by an AI agent for the maintainers.

## Asked of the contributor, still open

Asked on the issue on 19 Nov 2026 and not received by 24 Nov 2026 (the issue had no reply):

1. The held-out scoring script and the German word list, or the ids of the 48 held-out runs, so that the 0.839 can be
   recomputed.
2. A count of cipher words per document with the holes, by word. This count was made here on 24 Nov 2026
   (`words.tsv`); his own count, or his corrections to ours, are still welcome.

Also to ask: which name he wants used; whether his transcription may go to DECODE if a record is made.

## Catalogue and leads

- Catalogue 1594 stays, with what is known and open refreshed on 24 Nov 2026.
- Postscript B (3 Dec 1656) has no catalogue entry and no lead of its own: it is in the same unit and the same key, so
  it is worked here under 1594 (one key, one entry).
- The Dec 1769 item (1/354/0/4/261/17) has no catalogue entry and no lead in `research/leads.json`. It is named only in
  the `split_off` note of entry 1594 and in the sweep files `research/chrome_pass_2026-11/candidates.json` and
  `research/vetting_2026-11/`. It still needs its own lead.
- No DECODE record is known for either postscript (`decode_updates/queue.json`, skip of 24 Nov 2026).

## Remaining gaps

- 27 cipher words of A and 22 of B that he marks as not understood or uncertain (`words.tsv`, "marked") - blocker: not-attempted; not re-read here against the scans, which open in Chrome since 24 Nov 2026; his own check of fourteen candidate readings changed seven places and left the rest
- the proposed values 29 = k, 39 = p and 53 = x, which alone keep 4 words of A and 12 of B from counting - blocker: not-attempted; no test of them is on record; the seven further letters to Gross in units 46-47 could serve as one
- 19 digit groups unread or unresolved (his list of 18 and the ?? of run B003), in 8 words of A and 7 of B - blocker: illegible; faint, ligatured or in the gutter shadow on the microfilm scans by his two passes (largest online image about 1,680 x 2,620 px); not re-read group by group here
- prior-art reading not finished: Wasilewski 1979, AGAD Miscellanea t. 29, Przegląd Historyczny 1956 - blocker: not-attempted; no online copy was looked for on 24 Nov 2026

## Escalation

- [x] siblings: by his record the same table reads seven further letters to Gross in units 46-47 (Feb 1656 to Aug 1657), transcribed with the table in hand; no readings offered; not opened here
- [x] clear-pages: he searched the rest of unit 46 and unit 47 (scans 1-93) for a period copy or decode and found none; the clear letters of the unit (obj. 14, 17, 18) give context only
- [ ] known-keys: no period key in units 46-47 by his search, none held here for Bogusław Radziwiłł (catalogue vetting); the rest of the Radziwiłł archive was not searched for a key table
- [ ] print: Kotłubaj 1857 read by him (neither postscript), archive.org full text, cryptiana and GL.htm (catalogue vetting); Wasilewski 1979, AGAD Miscellanea t. 29 and Przegląd Historyczny 1956 not read
- [x] key-rebuild: table rebuilt from the ciphertext by the contributor, three values proposed; decode reproduced here and the house validation passes (24 Nov 2026)
- [ ] retry: his second pass and his check of fourteen candidates are done; nothing retried here; next is a re-read of the hole words on the scans without the expected word in hand, then a regrade

## Transcription doubts

- 94 groups his first pass marked uncertain (both postscripts) - read: as in `transcription_A.txt` and `transcription_B.txt`; checked: image, decode; his second pass (same model family) changed one group and left 20 unresolved, two of them read later; 18 keep their mark and are holes
- 22 changes in 21 runs, daggered in his table (`decode_A.tsv`, `decode_B.tsv`, column "corrected") - read: the corrected groups; checked: image, decode; by the contributor, guided by the expected word, so exposed
- 12 places he checked and did not change (einezogen, nosig, auffesen, mefinden, beswaziog, lnformiren, belsamen, bssertwegen, Perruohn, tluc-o, uag tein, wolle nanten) - read: as transcribed; checked: image, decode; the image does not support the expected word
- A031 first pair (42.11) - read: 45; checked: image, decode; here on 24 Nov 2026 45 and 43 were not told apart on the scan; stays 45
- A018 third pair (42.06) - read: 45; checked: image, decode; 45 or 47, not settled by him or here; stays 45
- B029 sixth pair (39.08) - read: 25; checked: image, decode; here on 24 Nov 2026 the first digit looked like a 4, which would give 45; left for the contributor to check; stays 25
- B001 (39.02) - read: 45 33 47 19 29 after 35 37 51 11 23; checked: image, decode; the digits stand as he has them, with a small 4 raised before the 7; the word is not understood

## Files

- `prior/issue784_SeldomPhooey_2026-11-18.md`: the issue text, unchanged (the live issue was compared on 24 Nov 2026:
  same text, no attachment, no reply).
- `extract.py`: cuts his two tables into `transcription_A.txt`, `transcription_B.txt` (run and groups) and `decode_A.tsv`,
  `decode_B.tsv` (his whole rows: run, corrected, line, clear words around the run, groups, decryption), no value edited.
- `key.tsv`; `decode.py` (reproduces his decryption column; `--write` writes `decryption_A.txt` and `decryption_B.txt`,
  the unedited output of the key; `--validation` writes `validation.tsv`).
- `reading.md`: his German as sentences with the holes marked, and his English translation; `count_reading.py` and
  `words.tsv`: the count.
- Access: szukajwarchiwach needs Chrome. From the unit page with `_Jednostka_delta=100` the thumbnails are
  `photos.szukajwarchiwach.gov.pl/<hash>_mid` in scan order and the full image is `<hash>_max`.
