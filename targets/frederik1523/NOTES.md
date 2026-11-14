# Duke Frederik and Lübeck, 1523: negotiation papers with name signs (catalogue 466) — NOTES

Status: no write-up

**Verdict: closed, already in print (1910).** Session 2026-10-26. The "chifferskrift" is a name code: clear Low German
letters in which single signs replace names, Sundays and weekdays, and the words for troops. The key survives, and
the letters are printed with every sign resolved in

- D. Schäfer and F. Techen (eds.), *Hanserecesse von 1477-1530*, Bd. 8 (Leipzig 1910). Hansischer Geschichtsverein
  digitisation: https://www.hansischergeschichtsverein.de/file/hanserecesse_3_8_low.pdf (996 PDF pages; the PDF
  and its text are in `work/hr/`, git-ignored).
  - n. 279 (Lübeck to Frederik, 1 Feb 1523), note 1: the first letter to use the signs. The key is in the
    Rigsarkivet, Gemeinschaftliches Archiv cap. XIII, 38, on a parchment strip about 15 cm wide and three times as
    long, endorsed by chancellor Wolf von Utenhof as the ciphers made with Lübeck "zu zceit der vede". Below them
    is a letter alphabet that the editors say was never used. The editors numbered the signs that were used
    (Ch. 1-72) and reproduced the strip on a plate facing p. 312.
  - the introduction says the signs are used in the letters up to n. 354. Ciphered passages are in nn. 278, 279,
    292, 293, 299, 309 and 312 (PDF pp. 329-355), each printed in clear with a "Ch. n" footnote at every sign.
  - **n. 292** (Frederik to Lübeck, Gottorp, Sunday after Valentine = 15 Feb 1523), pp. 324-326, is image 94 here.
    The edition prints the Lübeck original (L) and collates K = XIII, 38, K1 = **XIII, 47 c, Konzept** (image 94's
    old mark "Lauen. Arch. XIII 47c") and K2 = XIII, 47 n, an uncoded draft ("nicht chiffrirt").

Earlier mentions: Waitz, *Quellensammlung der Schleswig-Holstein-Lauenburgischen Gesellschaft* II, 1, 80 (extracts
of nn. 288 and 292); Allen, *De tre nordiske Rigers Historie* III, 3, 365 used K.

## The item

Rigsarkivet, Sønderjyske Fyrstearkiver, Hertug Frederik (1.), "Sager vedrørende udlandet" 1495-1523 (Daisy heid
11587371), Arkivalieronline epid 14908271, image ids from 41301821 (fetched with `../biermann1675/fetch.sh` into
`work/img`, git-ignored). The series has 24 items, not 14 as the catalogue says (the Daisy description lists 24).
Item slips: image 2 (item 1), 8, 59, 83, 90, **93** (item 8, id 41301913: "Sager vedr. forhandlingerne mellem hertug
Frederik og Lübeck 1523. Delvis med anvendelse af zifferskrift. ... Pergamentsbreve E 16-23"), 130 (item 9). **Item 8 =
images 94-129.**

- 94 (id 41301914): n. 292 K1, chancery copy "Ex:", docket "1523 14/2". Transcribed (`transcription_094.txt`) before
  the edition was found.
- 95: its continuation (survey row: dated "am dage Valentini anno xxiii").
- 112-113 and on: a clear copy of the Frederik-Lübeck alliance treaty (presumably Hanserecesse n. 280; not collated), no signs.
- The rest of item 8 was only partly surveyed (`survey_A.tsv`, `survey_B.tsv`; the survey stopped when the edition
  turned up).

## The system

72 numbered signs on the strip (`key.tsv`, from the plate): the Sundays Invocavit to Pentecost and the weekdays
(Ch. 1-21), a null "nichts bedudende" (22), Elbe and Belt, persons (keyser, koningk = rectangle, hertog Frederich =
circle with bar, the queen, Duke Christian, the bishops of Bremen and Minden ...), places (Lübeck = circle with cross,
Hamburg, Gottorp, Copenhagen, Jutland, Zealand, Funen, Scania, Sweden ...), and rutere / knechte / krygesvolck
(Ch. 64-66). One sign stands for one name, with no homophones. The circle-bar sign for hertog Frederich also
appears where the uncoded draft K2 has "wy".

## What was done before the edition was found

The system was identified as a name code from image 94, and the page was transcribed with ad hoc sign labels. Three
values were guessed from context: the two signs counted in "den bedungeden tall der ..." are troops, the rectangle
is King Christian, and the q-sign is a prince on the troops' route. All three agree with the edition: rutere,
knechte, koningk, bisschop van Bremen. No sign value was taken from the edition before then.

## Control

The transcription of image 94 was checked against the printed n. 292. Every sign label falls on one Ch. number. The
four small signs of line 21 are Ch. 58, 59, 56, 60 (Sehelandt, Fune, Copenhagen, Schonen). The F4 label covers two
signs: Hamburg (Ch. 42, l. 24) and Schonen (Ch. 60, l. 21). The "12" at the start of l. 5 is the Hadersleven sign
(Ch. 47). Two disagreements were checked on the scan. At l. 16 the sign is Lübeck's, so the first pass was wrong and
is corrected. At l. 10 the scan shows Frederik's sign where the edition gives Ch. 41 (Lübeck) for K1. The sense needs
Lübeck, so it is recorded as a slip on the page, not changed. `decryption_094.txt` has the page with the signs
resolved; nine words the first pass had left uncertain are taken from the print and marked. `translation_094_en.txt`
is the English.

## What was not done

The rest of item 8 was not transcribed, and the letters were not re-collated against the print. The decipherment
is complete in Hanserecesse, so a new reading would add nothing. The parchment key strip (XIII, 38) was not looked
for among the item-8 images. The slip's "Pergamentsbreve E 16-23" may be where it is now filed.

## Independent verification by Brice Dudout (PR #572, 14 Nov 2026)

Brice Dudout (PR #572, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) typed the K1 sign sequence from the
apparatus of Hanserecesse III/8 n. 292 and compared it with `transcription_094.txt`: the edition gives 51 signs for K1
(image 94) and the transcription has 51 labels (not 50, as the transcription step said); 50 of 51 agree, the one
difference being the l. 10 sign already recorded above. All 51 values of `key.tsv` stand in `decryption_094.txt`.
Re-run here: same figures. He also corrected one of the ten words given "as printed" in `decryption_094.txt`: l. 29
`<durchtheent>` to `<durchthendes>`. Checked here in the edition (PDF p. 345): the text has "in synen gebeden
krygesvolk durchthendes", and note a* gives "knechte adir rutere", also in signs, for K1. No key correction; read share
1.0 as recorded. Image 95 and the other letters of item 8 were not looked at by him or here.

