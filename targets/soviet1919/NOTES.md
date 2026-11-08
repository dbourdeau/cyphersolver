# Soviet Transpositions in German, 1919–1920: seven courier letters, NARA M336 roll 75

Status: keys recovered, six parts read, one read in part. Contributed by George Lasry (8 Nov 2026). The work was done
with Claude (Anthropic) agents under his direction; every ciphertext letter that does not fit the decryption was
checked by eye on the NARA images.

## 1. The documents

- **Source.** NARA RG 59, Central Decimal File 1910–29, file 862.20261 (Germany/Russia; cross-references 862.20201,
  862.20241, 861.00), microfilm M336 roll 75, frames 0456–0470,
  [naId 574886726](https://catalog.archives.gov/id/574886726).
- **What they are.** Typed copies of letters from communists in Germany to Soviet officials in Russia, sewn into the
  clothes of couriers on a German aeroplane forced down in Latvia on 6 April 1920. The US Commissioner at Riga sent the
  copies to the Secretary of State with despatch No. 155 of 21 April 1920 (frame 0457).
- **Cipher text.** Frames 0462–0464. Seven parts, each opening with an indicator (27001 or 27003) and its letter count:

| Part | Date | Frame | Indicator | Letters |
|---|---|---|---|---|
| Anfang | 23 Dec 1919 | 0462 | 27001 | 296 |
| Fortsetzung 2 | 23 Dec 1919 | 0462 | 27003 | 400 |
| Fortsetzung 3 | 23 Dec 1919 | 0462 | 27001 | 287 |
| Fortsetzung 4 | 23 Dec 1919 | 0462 | 27001 | 304 |
| Fortsetzung 5 | 23 Dec 1919 | 0463 | 27003 | 340 |
| Schlussmitteilungen | 25 Dec 1919 | 0463 | 27001 | 498 |
| Zusatz | 19 Feb 1920 | 0464 | 27003 | 940 |

- **Contemporary reading.** The State Department read the letters in 1920. Its instruction No. 16 to Riga (5 Aug 1920,
  frame 0456) says the code material "has proven of great interest" and encloses translations. The confidential
  memorandum "Re: Intercepted Cipher Messages from Communists in Germany to Soviet Officials in Russia" (frames
  0468–0470) gives English translations of Anfang, Fortsetzung 3, 4, 5 and Schlussmitteilungen. No German plaintext and
  no key are in the file. Fortsetzung 2 and Zusatz have no contemporary translation there.

## 2. The system

Single columnar transposition of German plaintext. No nulls, no word division; Ä, Ö and Ü are single letters. The
plaintext is written in rows under a numbered key and the columns are read top to bottom in the order of the key
numbers; when the last row is short, the long columns are the leftmost ones.

| Indicator | Columns | Key (number over each column, left to right) | Columns read in the order |
|---|---|---|---|
| 27001 | 19 | 5 1 15 16 8 4 7 17 12 18 13 2 19 14 9 6 3 10 11 | 2 12 17 6 1 16 7 5 15 18 19 9 11 14 3 4 8 10 13 |
| 27003 | 25 | 1 3 10 24 6 11 12 4 2 16 5 7 14 13 8 20 15 22 17 25 23 18 19 21 9 | 1 9 2 8 11 5 12 15 25 3 6 7 14 13 17 10 19 22 23 16 24 18 21 4 20 |

`decryption.md` shows the key and the full transposition rectangle of every part.

## 3. How the keys were recovered

1. Letter counts: all seven parts have a German profile (E high, or R high where the copy types R for E) and no
   dependence between adjacent letters, so a transposition.
2. Simulated annealing over column orders with a German 4-gram score recovered the 19-column key from Fortsetzung 4
   and Schlussmitteilungen (indicator 27001), and the 25-column key from Zusatz (27003, 940 letters). No plaintext was
   used. The 25-column key decrypts Fortsetzung 2 and 5 as well.
3. Fortsetzung 3 reads with the 27001 key once the three groups missing from the copy (15 letters) are located.
4. Anfang reads with the 27001 key once a struck-out group after TSUWI (five letters, a solid blot on the frame) is
   removed: the remaining letters are exactly the 296 of the indicator line.
5. The contemporary English translation was used afterwards, to check the readings and to settle some names.

## 4. The transcription and its errors

The copy on the microfilm is a blurred carbon. Many letters are blotted (E, R, B, H, K, M and N fill in), and the
1920 typist made slips. `transcription.txt` gives the letters as they stand on the page. For each part, the corrected
plaintext was re-enciphered and compared letter by letter with that transcription; every difference was checked on the
image. `ciphertext_corrected.txt` is the ciphertext as it fits the decryption, with `?` only where a letter is lost or
illegible. `decrypt.py` decrypts it and checks it against `plaintext.txt`:

```
python decrypt.py --typed
```

**Checked here (8 Nov 2026).** `reading.md` records how many letters of the typed copy are blotted or mistyped in each
part (33, 89, 35, 3, 107, 36 and 115 for the seven parts in order; Fortsetzung 5, 107 of 340 letters, is the worst), mostly
visual confusions of the blurred carbon (R for E, P for F, N and M). The project did not re-measure these counts and did
not see the images. `decrypt.py` only decrypts the corrected ciphertext and compares it with the plaintext file written
from it, so it is a consistency check of the files, not a test of the reading.

## 5. The readings

`reading.md` has, for each part, a summary, the German as sentences, the English translation and the notes. In brief:

- **Anfang.** The air consignment arrived; asks for letters by Lenin, Trotsky and Zinoviev for Italy and France;
  Osipoff is unreliable and must not be sent again; Koriniez's address is invalid and he must be recalled.
- **Fortsetzung 2.** A man travelled on his own to Switzerland and Moscow and is highly suspicious; couriers Else,
  Olga and Hilde arrived from Riga with old material; courier addresses in Berlin; the Commissariat demands material.
- **Fortsetzung 3.** Pochitonoff is said to be in Switzerland; negotiations with Sylvia, money given, more handwritten
  English wanted from her; Litvinov answers neither couriers nor letters; Dzerzhinsky's confidential man is wanted.
- **Fortsetzung 4.** The secretariat urgently needs money and material, names its newly elected members, reports
  contact with Holland and its own publications (Russische Korrespondenz).
- **Fortsetzung 5.** A branch is set up in Vienna; contact with all countries; a congress in January or February;
  Radek or Bukharin is needed; signed Thomas (James).
- **Schlussmitteilungen.** Fedoroff's stones handed over for France; a plea not to fund individual countries but
  mainly the party press; a commission for Balabanoff.
- **Zusatz.** The failed conference in Holland and the arrests that followed, police pressure on the secretariat, a
  radio station ready, journalists exchanged with the Frankfurter Zeitung, and an urgent need of money for Bulgaria,
  Serbia and France.

## 6. Prior work

The State Department's 1920 translations (section 1) are an earlier reading of five parts; they were found in the same
file during the work. The cyphersolver catalogue and repository were searched on 8 Nov 2026 (M336 roll 75, Riga,
Latvia, the indicators, the names in the letters): nothing on these letters. No printed edition of the German text is
known to us.

## Remaining gaps

- Fortsetzung 2: about 34 letters decrypt but do not read (the opening GALIEIE, OE after "verdächtig", the names PEL…ZIERSKI and RELCW, VILARDOVRRHAFEET before "jetzt frei") - blocker: illegible; the blurred copy is the only witness and there is no contemporary translation of this part
- Zusatz: one letter of the name O?galski - blocker: illegible; blotted on the copy
- Fortsetzung 3: the 15 letters of three groups missing from the copy, supplied from the sense and the 1920 translation - blocker: illegible; the groups are not on the copy
- Fortsetzung 5: "Es geht schön vorwärts" rests on two letters corrected against the copy and matches the 1920 translation - blocker: illegible; the copy is the only witness
- Schlussmitteilungen: "Auftrag auf Zürich [?]", the copy has ZURUCK and the 1920 translation "Order on Zuruch" - blocker: illegible; the typed copy is the only witness
- A human check of the corrected ciphertext against the NARA images beyond the places George Lasry compared by eye - blocker: needs-physical-access; the project's environment cannot reach the NARA images

## Escalation

- [x] siblings: the seven parts of the one file read together; no other leaf of M336 roll 75 carries a transposition
- [x] clear-pages: none; the file's English memorandum (frames 0468-0470) is a translation of five parts, used afterwards to check the readings
- [x] known-keys: no earlier key for these indicators is known; none found in the repository or in print on 8 Nov 2026
- [x] print: repository and catalogue searched on 8 Nov 2026 (roll 75, Riga, the indicators, the names); no printed German text known
- [x] key-rebuild: both keys recovered by annealing with a German 4-gram score, then every part re-enciphered and compared letter by letter with the copy
- [n/a] retry: the remaining holes are blots on a single blurred carbon copy; a second pass on the images could not be made from here

## Files

| File | Content |
|---|---|
| `transcription.txt` | the seven parts as typed on the copy (frames 0462–0464) |
| `ciphertext_corrected.txt` | the ciphertext as it fits the decryption |
| `plaintext.txt` | the literal plaintext, letter for letter |
| `decryption.md` | keys and transposition rectangles |
| `reading.md` | German, English, summaries and notes per part |
| `decrypt.py` | decrypts `ciphertext_corrected.txt` and checks it against `plaintext.txt` |
| `profile.json` | the target profile |
