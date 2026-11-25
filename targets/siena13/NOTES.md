# Siena nos. 13 and 16 — a letter on the Pope and Bologna, deciphered from its plaintext twin (DECODE R4801, R4804)

Status: read; key recovered based on adjacent plaintext (the clear copy no. 16) by George Lasry with CTTS and Claude Fable 5.1. Contributed result, filed here 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2:
- no. 13, the cipher letter: DECODE [R4801](https://de-crypt.org/decrypt-web/RecordsView/4801) (Concistoro_2308_55);
- no. 16, **the clear copy** of the same letter: DECODE [R4804](https://de-crypt.org/decrypt-web/RecordsView/4804)
  (Concistoro_2308_58). Both catalogued "1500-1599", no status.

## Source

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (17 Oct 2026), consolidated report sent by email to
Daniel Bourdeau, pp. 35-36, section H "Pieces with an interlinear or separate plaintext". Quoted whole in
[`lasry_report.md`](lasry_report.md); key figure [`key_lasry.jpg`](key_lasry.jpg). Not re-edited here.

## What the report gives

- **Status (Lasry):** solved. Transcription and initial key with CTTS (the author); Claude Fable 5.1 finalised the
  key and the transcription from the given plaintext of no. 16 (R4804). 17-18 October 2026.
- **Ciphertext:** 553 cipher symbols on 10 lines with ten clear stretches; the plaintext is no. 16.
- **Key:** 37 distinct signs; homophonic substitution, one or two signs per letter (many numerals), four doubled-letter
  signs (ll, gg, ss, cc), one null, no word codes.
- **Contents:** to "V. S. Ill.ma"; the Pope's agreements and the delay of his coming to Bologna have left "qualche
  ruggine"; the writer would spend everything to abase the neighbours and, claiming some castle, do as Lautrec did when
  he took Modena and Reggio, "perché al peggio non si ha sinon a rendere". Dated 1527-1530 from the content; unverified.
- **Open (Lasry):** writer, addressee, exact date; the first word (baca?) and "sabbatte".

## Prior state in the repository

The siena1421 survey (24 Sept 2026) had already found that no. 16 is the clear decipherment of no. 13 and made a
partial alignment (bologna, accordi con; "a sign with superscript n = doubled letter"), but entered the pair only as
"read at the time" and did not rebuild the key. George's report rebuilds the key from that plaintext and deciphers the
cipher sign by sign: method "key recovered based on adjacent plaintext" (the plaintext is a separate folio in the
same fascicle). His key (one doubled-letter sign each for ll, gg, ss, cc) replaces the survey's guess of a general
doubling mark.

## One key, one entry

No. 13's key (report p. 35) is built on numeral-shaped signs: "23" = a, "19" and "111" = e, "10" and "15" = i,
"13" = l, "12" = m, "11" = n, "17" = g, a bar = r, θ and 6 = t. It shares no value with the section-G keys of nos. 17,
15 and 5? (in no. 17, for instance, the single digits 9, 3, 4, 6 are a, r, s, u). No. 16 is clear text, not a second
cipher, so nos. 13 and 16 are one entry with one key.

## Files

- `lasry_report.md`: the report's section, verbatim; `reading.txt`, `translation.txt`: his decipherment and translation, verbatim.
- `key_lasry.jpg`: his key figure; `key.md`: the same key as a table.

**Count question for George:** the report's text gives 553 cipher symbols; the counts printed in the key figure add up to 283.

## Remaining gaps

- the first word (baca?) and "sabbatte"; writer, addressee and date - blocker: illegible; doubtful in the report even with the plaintext twin.

## Escalation

- [x] siblings: no. 16 is the plaintext twin; every piece of fasc. 2 opened in the survey.
- [x] clear-pages: no. 16 used (it is the source of the key).
- [x] known-keys: no filed key of fasc. 1 matched (survey).
- [x] print: none known.
- [x] key-rebuild: key complete per the report.
- [n/a] retry: nothing open in the cipher except two doubtful words already checked against the plaintext.

## 14 Nov 2026: the cipher has no transcription, and why (audit section I, "no transcription file")

- In the folder: the report's reading, translation and key figure; not the CTTS transcription (553 cipher symbols on
  10 lines by the report).
- DECODE R4801, public record page: one image, no text attachment; the full-size image needs a login. No other online
  copy of Concistoro 2308 is known here.
- `outcome.texts[0].transcription_missing` replaces the empty `transcription` list. Unblocks it: George Lasry's CTTS
  transcription, or the image at full size to transcribe against `key_lasry.jpg` and the clear copy no. 16 (R4804).
