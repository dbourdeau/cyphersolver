# Plan, written before any decoding: malvezzi1550 (lead 892), HHStA Türkei I 8-3-12

Written by an AI agent (Claude Opus 5.5), 23 Nov 2026, about 00:45 Eastern. Not checked by a person.
Hashed (SHA-256) into `PLAN_malvezzi1550.md.sha256` before the transcriptions are decoded.

## Piece

Ferdinand I to Giovanni Maria Malvezzi, Brünn (Brno), 28 April 1550, Latin, fully ciphered between a clear
salutation and a clear dating clause. HHStA Wien, StAbt Türkei I 8-3-12 (AIS ID 7048437), fol. 167-171:
Duplikat (AIS images 1-2), Ausfertigung (images 3-4) and a 19th-century decipherment (images 5-6).
The piece decoded is the **Ausfertigung** (images 3-4): 42 cipher lines, cut into `lines/A01-A21` (image 3, right
page) and `lines/B01-B21` (image 4, left page).

Disclosure: when choosing the piece I looked at a small (800 px) survey image of the 19th-century decipherment and
read its opening lines. The two transcribers have not seen it. Decoding is mechanical from their files.

## Frozen key

K = upstream `targets/malvezzi1548/KEY_BRIEF.md` (the DECODE R367 / R386 alphabet as used there), unchanged:
SHA-256 66f98502297ed3ff111122bae75b21c309325b8adc1f4cc8c37d9fcd8c7793fd (same file at upstream 7d9b91fb8 and
a9063ac86). Its source transcription `k367.txt`: b49fc5ef...432c.

The upstream key describes signs in words, not pictures. The link from each 1550 shape to a key description is in
`sign_values_frozen_key.json` (SHA-256 50a3a583...1cb37) and `sign_sheet_with_values.png`, made before decoding.
Rules used there: each shape takes the value the key gives the shape it most resembles; where the key gives two
values for one shape, both are kept as a candidate set (q = e|u; 8 = d|mm; b = n|null). Shapes the key does not
describe (square u `U`, star `*`, capital `B`) get no value and are holes. Nulls from the key: n, z, and the clear
words Cum, Porro, Spo, Dar, atq and the like; `Ras` = Imperator Turcorum. & keeps the key's value x.
No value will be added or changed after decoding.

## Transcriptions

Two transcriptions of all 42 lines in the sign codes of `sign_sheet_blind.png`, each by a separate helper agent
given only the line images and the blind sheet (no values, no plaintext, no decipherment). Report sign-by-sign
agreement (aligned per line).

## Test

Reference: the 19th-century decipherment (images 5-6), transcribed by me after this plan is hashed.
It covers the whole ciphered text, so the whole piece is scored (no held-out part is left over).

1. Decode each transcription mechanically with K (nulls dropped; holes `?`; candidate sets kept).
2. Letters only, lower case, u=v, i=j, ae=e. Align the decoded string to the decipherment's string (global
   alignment, match +1, mismatch -1, gap -1). A decoded position agrees when the decipherment letter is the value
   or in the candidate set. Score = agreeing letters / letters of the decipherment.
3. **Pass mark 0.85** (letters, primary score on transcription 2, the second blind one; also reported for 1).
4. Controls: 200 keys made by shuffling the values among the sign codes (null/hole status kept), scored the same
   way. The real key must beat the best control.
5. What counts as read: a word of the decipherment counts as read only when every one of its letters is matched by
   the decoded key value at that position; a word with any supplied, missing or wrong letter is a hole. Report
   words read / words, and say whether the decoded text builds sentences.
6. Report what the key lacks (signs without value, word signs, nulls, names).

A miss is reported as a miss.
