# sirdar1909: Sirdar (Wingate) to Herbert, Khartoum to Cairo, 9 Jan 1909 (catalogue 2907)

Durham University Library, Abbas Hilmi II papers, HIL/64/400. Promoted by the wave 16 Durham sweep
(research/sweep_2026-11-15_wave16_durham), which also listed the cipher/clear pairs of the same file used here.

## Key
Simple substitution, letters run together and regrouped in fives, a null at each end of a run. Built only on
HIL/64/402 = 403 (3 Jan 1909) and HIL/64/239 sheet 1 = HIL/64/118 (30 Nov 1908): `verification/build_v1.txt`,
`verification/key_v1.tsv`. Not reciprocal throughout, though many pairs are (a/p, b/m, c/l, d/k, e/y, f/h, o/t, r/x,
s/w). Unknown: cipher i, n, z. Clerks' variants: w written h once ("railway"); g and q confused.

## Held-out test v1 (tools/holdout, #1014 convention)
Manifest `verification/MANIFEST_v1.sha256`, SHA-256 a9259625e324fbb71b62a30cdb539d205924ce711ad488f30b64f02c0aafbccc,
frozen 2026-11-27 11:49:45 UTC, hash posted in the body of issue #1023 (created 12:03:41 UTC) before the run.
Held-out: HIL/64/240 = 119 (same telegram, sheet 2) and HIL/64/214 = 62 (26 Sept 1908), 301 signs, two blind passes
merged mechanically. Measured once, 2026-11-27 12:30 UTC:

**char 0.3051, best of 200 shuffled controls 0.2237 (mean 0.1115, z = 5.03, 0/200 at or above): NOT VALIDATED.**

Per run, for information only (not decisive, reported as announced in the protocol): 240 run A 0.75, run B 0.81;
214 0.17. The Nov 1908 runs decode as the clear copy apart from the blind passes' '?' and one clerk's k for o; the
Sept 1908 telegram does not decode at all. The risk declared in the protocol came true: 214 is in another alphabet. The
measurement does not validate the key; the passage is burnt and a new test would need a new passage of the
Nov 1908 - Jan 1909 alphabet (none other found in HIL/64-65 by the sweep).

## Reading
Decryption (`decryption_400.txt`, made by `decode_400.py`): key_v1 applied to `transcription_400.txt` sign by sign,
nothing edited: `·kigdlywiremeagyremarksyoumayha‹z›etomake·`.

`reading_400.md`: "kindly wire me any remarks you may have to make", 10 cipher words: 5 sure, 5 probable. Only sure
words count as read, so the read share is 0.50 (5 of 10). The text is under 40 cipher words, so the short-text floor
applies (at most 2 holes); it has 5 holes, so it is read in part by the floor. Images not included (Durham's reuse
terms not checked).

## Transcription doubts

- last letter of group 3 (`yBypg`) - read: g (= g, read as n in the reading); checked: image, decode, transcription; passes B and the keyed pass read g, pass A [g/q]; the decode needs n (q in the key), so {kindly} and {any} stay probable
- the 4-shaped letter in group 2 (`cesux`) and group 4 (`exyBp`) - read: x (= r); checked: image, decode, transcription; both blind passes read x, Daniel Bourdeau's check of the Durham image agrees (#1025); {wire} and {remarks} stay probable since no clear copy confirms the value
- first letter of group 4 (`exyBp`) - read: e; checked: image, decode, transcription; pass A [e/c], the other passes e; e (= y) gives "any"
- group 4, catalogue `eyybp` - read: `exyBp`; checked: image, decode; the second letter is the 4-shaped x, not y (confirmed on the image in #1025)
- group 5, catalogue `xdwrt` - read: `xdwet`; checked: image, decode; the fourth letter is e (the catalogue gave "r or e"), giving "you"
- group 8, catalogue `bpdjv` - read: `Bpdyv`; checked: image, decode; the fourth letter is y, giving "make"

## Remaining gaps

- {kindly}, {any}: the letter read g stands for n (n is q in the key) - blocker: illegible; g and q are hard to tell apart in these hands, and no clear copy of HIL/64/400 is known
- {wire}, {remarks}: the 4-shaped letter taken as x (= r) - blocker: illegible; both blind passes read x, but nothing outside the passage confirms the value here
- {have}: cipher z has no value in key v1 (nor i, n) - blocker: no-key-material; z does not occur in the two training pairs, v is from sense only
- key v1 not validated (held-out test v1 failed, passage burnt) - blocker: no-key-material; a new test needs another cipher/clear pair of the Nov 1908 - Jan 1909 alphabet, none other found in HIL/64-65

## Escalation

- [x] siblings: HIL/64/402 = 403 and HIL/64/239-240 = 118-119 used (key and held-out); HIL/64/214 = 62 is in another alphabet
- [x] clear-pages: all 546 frames of HIL/64 and HIL/65 looked at by the wave 16 sweep; no clear copy of HIL/64/400
- [x] known-keys: no published key for the Sudan Government letter alphabet of 1908-09 found
- [ ] print: the Sudan Archive (Wingate papers, Durham SAD) not searched for the telegram or its clear copy
- [x] key-rebuild: key_v1 built only on the two named pairs and frozen (manifest a9259625) before the held-out test
- [n/a] retry: the key was not extended after the test; z, i and n stay without a value
