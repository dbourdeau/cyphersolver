# meyerfeldt1713: J. A. Meyerfeldt to the King, Pommeranica vol. 149 (catalogue 451), letter 143535 read in part with the key of the time

Status: read in part (Brice Dudout with Claude, 24 Nov 2026; letter 143535, 47 of 68 cipher words sure, 55 read with probable and restored words; under the 95% bar).

## Source

Riksarkivet (Swedish National Archives), Pommeranica, Skrivelser till Kungl. Maj:t från myndigheter: Generalguvernörer,
vol. 149 (SE/RA/2404/I A 2/149), 1712-1714; catalogue entry 451 ("J.A. Meyerfeldt. Åtskilliga chiffrerade"). Not on
DECODE.

**Images: Riksarkivet, Pommeranica vol. 149, samples supplied by the archive (J. Mispelaere), 24 Nov 2026** (14 views
of this volume, taken 13 Nov 2026; Riksarkivet references RA-FF 2026/93920 and 2026/95675). They were sent for a
research enquiry; no reuse licence was asked for or given, so **no image, crop or derivative is committed** here.
AI analysis was not raised with the archive; the project's method was not presented to it at the time.

Views used: 20261113_143535 (the letter read here), 20261113_143346 and 20261113_143443 (the key). Seen but not read:
143510 (22 Feb 1713, a more cursive hand) and 143523 (10 May 1712 or 1713; line 1 only decoded).

## The letter

View 143535, dated in another hand "d. 15 Januarij", archivist's pencil "1712 el. 1714?". Probably Johan August
Meijerfeldt, governor-general of Swedish Pomerania, to Charles XII. A cipher block (9 lines and a short line), four
lines in clear German, and a second cipher block of 2 lines. No gloss or decipherment of the time on the page.

## Key (`key.tsv`)

A key of the time is in the same volume, twice:
- 143443: the isolated form, one sign per line against its letter, with two trial words in joined signs;
- 143346: the same key in **joined signs on a base line**, above the alphabet a b c d e f g h i k l m n o p q r s t u w
  x y z, with "Signat:" and a dotted circle (signature sign). An archivist's pencil note (Swedish) says the same key
  served for letters among the papers of the Pomeranian government of 1712 and 1713.

The cipher is a joined script on a base line: each letter is a stroke or loop above or below a continuous line, one
form per letter (simple substitution). `key.tsv` gives one shape code per sign, its value and its source. v and w share
the "house"; no sign for j; x and y are struck through or absent and do not occur in the passage. The key was
transcribed and frozen by SHA-256 before decoding (our working files).

## Transcription (`transcription/`)

By Claude for Brice Dudout, 24 Nov 2026, by eye on straightened copies enlarged 2-3x. **Declared deviation: it is not
blind.** The joined forms were identified with the key, and a working reading went on at the same time, so the cut
between joined signs may have been guided by the sense. The transcription and a pre-registration were hashed before
the single decode run. There is no held-out validation against controls (a key of the time, no gloss to test against).
Block 1 has 272 cipher letters, under the 300 of a measured portion, so no 95% verdict is possible on it alone.

## Blind sign sheet 2411 (`sign_check/`)

The key's k, l and m are all double loops on a stem in the joined form, and v1 of the transcription could not tell k
from m (code DL, decoded (k|m)). Brice Dudout read a blind sheet of 14 questions: 8 k/m/l targets and 2 l controls,
then 3 g/h/s/t/r targets and 1 s control. Options were the key's forms, with no values or readings. The rule
(`sheet-2411-rule.md`, in French, byte for byte, SHA-256 c88aedfe...) was hashed before the thumbnails; the key of the
sheet (`sheet-2411-key.json`, boxes only) was opened after the answers were exported. **Controls 3/3.**

- The double loop splits in three: **DK** (two loops side by side) = k; **DM** (small low loop then large loop) = m,
  the isolated m of 143443, described by the reader as "the reverse of form 2"; **LH** (large loop then small) = l.
  The joined m of 143346 is struck through (the reader's remark at q02) and is not used.
- g (L2, first sign) and t (L6 end) confirmed by the shape; a "slanting H" at L7 (new code HP) gets no value.
- Effect: möchten, wegkrigen, können, Regimenter (and lamentiret in block 2) become sure; a small a-stroke seen at L10
  gives "kan". Sure words 41 -> **47 of 68**; the read share is unchanged (81%). Results: `sheet-2411-results.tsv`.

## Files

| file | content |
|---|---|
| `key.tsv` | the key of the time, shape codes and values, with the k / l / m split |
| `transcription/143535_block1.txt`, `transcription/143535_block2.txt` | shape codes, one manuscript line per line (v2, after the sheet) |
| `decode.py` | decoder: `python3 decode.py transcription/143535_block1.txt transcription/143535_block2.txt` |
| `decryption.txt` | its output |
| `reading.md` | reading (sure / {probable} / [restored] / ‹unresolved›), translation, count |
| `sign_check/` | blind sheet 2411: rule, key, answers, results, SHA256SUMS |

## Reading and count

See `reading.md`. Letter 143535: 68 cipher words, **47 sure** (69%), 5 probable, 3 restored, 13 unresolved; 55 read
(81%). Block 1 alone: 49 of 56 read (87.5%). Under the 95% bar: **read in part**. The reading, in German: Muscovite
deserters, very few; some sent to Sweden, the others distributed among the regiments "so that they do not eat the
bread uselessly" until they can be sent safely to Sweden; then, in clear, letters from Stralsund from Major General
Mevius.

## Remaining gaps

- 143535: 13 unresolved words (reading.md) - blocker: illegible; ink blots at L1-L2, L4, L8 and in block 2 on the sample views, and the cut between joined signs in L3 (‹wengen›, ‹lehgen›) and block 2 line 11 is not settled at 2-3x
- 143510 (22 Feb 1713) and 143523 (10 May 1712 or 1713), the other cipher letters among the samples - blocker: not-attempted; 143523 line 1 decoded only ("hier ist {nichts} ‹…›"), 143510 not transcribed (a more cursive hand)
- printed editions and the year of 143535 - blocker: not-attempted; Historiska handlingar and Charles XII's letters not searched; 1712 or 1714 not settled by the text read

## Escalation

- [x] siblings: the 14 sample views of the volume opened; the key found on 143346 and 143443; 143510 and 143523 seen (not read)
- [x] clear-pages: the clear passage of 143535 read; it continues the letter and is not a decipherment of the cipher blocks
- [n/a] known-keys: the key of the time is in the same volume and reads the letter; no other key was needed
- [ ] print: printed Swedish editions (Historiska handlingar, Karl XII:s bref) not searched
- [n/a] key-rebuild: the key of the time is complete for the letters met, apart from x and y, which do not occur
- [x] retry: every doubtful k / m / l and g / h / s / t / r sign retried with the blind sheet of 24 Nov 2026 and regraded (sign_check/)

## Transcription doubts

- double loop k / m / l (143535 L1, L3, L5, L7, L10; block 2 L10) - read: DK = k, DM = m, LH = l; checked: image, decode, blind sheet 2411 q01-q10 (controls 3/3)
- first sign of L2 (143535) - read: g (DS); checked: image, decode, blind sheet q13; "gehr" is no word, so the word stays {sehr}
- slanting H between ei and l (143535 L7) - read: HP, no value; checked: image, decode, blind sheet q12; the word stays {verteilet}
- slanting loop at the end of L6 (143535) - read: t (LN); checked: image, decode, blind sheet q11; the run after it stays unresolved
- small loop XX before the k of moskowitsche (143535 L1) - read: not identified; checked: image, decode; the word stays {moskowitsche}
- stroke under the line after h (143535 L3, "habe") - read: a (TK), nearly upright; checked: image, decode; the word stays {habe}
- small a-stroke at L10 (143535) - read: a (TK), omitted in v1 and added in v2; checked: image, decode; gives "kan"

## Credit

- Key of the time: Swedish chancery (Riksarkivet, Pommeranica vol. 149).
- Images: Riksarkivet, samples supplied by the archive (J. Mispelaere), 24 Nov 2026; none committed.
- Transcription, decoding and reading: Claude (Opus 5.5) for Brice Dudout.
- Blind reader of the sign forms: Brice Dudout.
