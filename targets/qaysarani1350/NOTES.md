# Ibn al-Qaysarani to the compiler of a Mamluk book of cipher verses (Penn LJS 51, f. 106v)

Status: read
Outcome: key recovered based on adjacent plaintext (a red gloss over the first five signs), complete. 16 Nov 2026.
Catalogue: Unsolved Catalogue no. 2882 (class A), from the Arabic sweep of 15 Nov 2026
(`research/sweep_2026-11-15_arabic/part_A.md`).

## The document

University of Pennsylvania, Kislak Center, LJS 51, f. 106v (OPenn image 0084_0217), lines 6-12. The volume is a
first-person account by an unnamed Mamluk secretary of the cipher verses he exchanged with colleagues; after each
cipher he writes that he solved it and gives the verses. The sweep dates the text to about 1330-1370 and Penn dates
this copy to the 15th century. This is the last text in the volume. It is introduced by "wa-kataba li Ibn
al-Qaysarani" (so read by the sweep; the name is written small at the end of line 5 and I did not re-read it
letter by letter). Under the cipher the compiler begins "fa-halaltuha fi l-hal ... wa-wajadtuhu ja'ala al-lam alif"
(I solved it at once ... and found he had made the lam-alif) and the manuscript breaks off, so the plaintext that
followed is lost.

Images: https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_0217.tif (2339 x 2959 px, plain curl).
No image is committed here except the site crop.

## The system

Monoalphabetic substitution of invented signs for Arabic letters, written right to left, words divided by a
vertical stroke with three dots over it. 89 signs, 22 distinct, 21 words (measured on `cipher_tokens.txt`).
Lam-alif is one sign. Final alif maqsura is written as alif; no hamza, no shadda, no vowels. A word runs over the
line end twice (lines 2-3 and 4-5), with no divider at the line end.

Sign list (labels of `transcription.txt`; shapes as seen on the TIFF):

| Label | Value | Count | Shape |
|---|---|---|---|
| K | ا | 18 | small loop with a flag to the left and a tick up to the right |
| N | و | 9 | zigzag like a slanted N |
| H | ه | 7 | two stems with loops at the top joined by a bar |
| Z | م | 7 | small triangle, bar to the right, stroke down ending in a hook or a bowl |
| T | ن | 6 | tall stroke, a loop on its right, a tail swept to the left |
| M | ل | 6 | loop at the lower left, second loop above, tail to the right |
| Y | ج | 5 | cup over a stem that ends in a closed loop |
| G | ت | 4 | slanted stroke into a bowl with a loop at its end, like a 6 |
| S | د | 3 | hook and wave on the baseline |
| R | ر | 3 | triangle, bar, small loop |
| E | س | 3 | figure 8 (round in line 1, flat-topped in lines 4 and 6) |
| F | ي | 3 | loop or lozenge on a vertical stem |
| B | ف | 3 | flag with a small square or loop at the foot |
| D | ع | 2 | two loops on the baseline (line 1); in line 2 close to R |
| W | ض | 2 | three teeth with a stem down at the left |
| U | ح | 2 | cup on a stem with a hook to the right at the foot |
| O | ة | 1 | circle with an inner curl, abraded |
| J | لا | 1 | tall stroke joined to a bowl, abraded |
| A | ق | 1 | arrowhead over a stem and a circle crossed by the stem |
| Q | خ | 1 | flat bar over a stem and a circle crossed by the stem |
| C | ث | 1 | open curve with a loop on top, like an e |
| X | ص | 1 | one stem with a loop on each side of its top |

## How the key was recovered

1. Red letters stand over the first five signs of line 1. I read them as و ن ا ع س. With the sixth sign as ة the
   first word is وناعسة ("and many a drowsy-eyed woman"), a common opening of love verse.
2. The group Y B K T (..ان) follows J in line 1, وا in lines 4-5 and وا in line 7, the last time with H K after
   it. الاجفان / واجفان. / واجفانها: Y = ج, B = ف, H = ه, and J is the lam-alif sign the compiler mentions.
3. Line 1 and the first two words of line 2 then scan as a ṭawīl hemistich if the two-sign word is قد: "wa-nāʿisati l-ajfāni qad jaʿala l-hawā".
   جعل gives M = ل, الهوا confirms K M = ال.
4. ولم انم / ولم تسهد / ونامت (lines 5-6) give Z = م, G = ت and confirm S = د; سهرت and تسهد share E H.
5. The rhyme words ا.ضا (line 4) and م.ضا (line 7) with the same middle sign as in سه.ت: ارضا, مرضا, سهرت.
   R = ر, W = ض. The rhyme is -ḍā.
6. The second hemistich must scan faʿūlun mafāʿīlun faʿūlun mafāʿīlun and end in لها ارضا: لها مهجتي مثوا وخدي
   لها ارضا. The first لها stands in a damaged patch of line 2 (lower loop of ل, ه whole, the body of ا, then a
   stroke that is the divider without its dots).
7. Line 5, the word between واجفاني and ولم انم: four signs, pattern short-long-long, third sign ا: صحاح
   ("sound"), set against مرضى ("sick") in the last hemistich.

Two false starts are in `WORKLOG.md` (جهنم for the damaged word; ع for the R sign).

## The reading

`reading.md` (Arabic, as enciphered and in normal spelling), `translation_en.md`.

وناعسةِ الأجفانِ قد جعلَ الهوى / لها مهجتي مثوًى وخدّي لها أرضا
سهرتُ وأجفاني صِحاحٌ ولم أنمْ / ونامتْ ولم تسهدْ وأجفانُها مرضى

Many a girl with drowsy eyelids: love has made my heart her dwelling and my cheek the ground beneath her. I lay
awake, though my eyelids are sound, and did not sleep; she slept and was never wakeful, though her eyelids are sick.

## Checks

- Metre: both verses scan as ṭawīl in all four hemistichs, and both end in -rḍā (ارضا, مرضا).
- The key is one-to-one: 22 signs, 22 different letters; no sign has two values.
- The compiler's remark under the cipher says the writer "made the lam-alif ..."; the reading has exactly one
  lam-alif sign, in الاجفان.
- Statistical validation (16 Nov 2026), `docs/_validate.py` with the new `lang/` model `ar-mamluk` (2.17 M letters: the
  diwans of Safi al-Din al-Hilli and Ibn Nubata, al-Safadi's Kashf al-hal and Alhan al-sawaji', al-Umari's al-Ta'rif; OpenITI),
  order 4, `validation.tsv`: reading -2.537 per letter; random keys -4.901 (z 5.3); keys refitted to the shuffled signs mean
  -2.881, best -2.745 (z 3.4): **pass**, narrowly. Seeds 2-4: weak (z 2.7), pass (5.7), pass (6.3); in all four runs the
  reading beats every refit. Negative control (`--control`): underdetermined (z 0.5). Short text: 89 signs, 4 tokens per type.
- Not checked against the solved alphabets on ff. 1r-106r: no sibling alphabet was compared.

## Doubtful readings (grade M or I)

- Line 1, sign 6 (O): abraded circle; ة from the word (I).
- Line 1, sign 7 (J): abraded; lam-alif from الاجفان and the compiler's remark (I). The cipher has no separate
  alif before it, so the text as written is لاجفان.
- Line 2, the first لها: three signs in a damaged patch, the divider after them without its dots (M).
- Line 2, جعل: the middle sign looks like R (ر) as much as D (ع); read ع from the word (I).
- Line 5, last sign of صحاح: its foot is a closed loop like Y (ج), not the hook of the U before it; read ح from
  the word (I). As written it may be صحاج, a slip of the writer or the copyist.
- A (ق) and Q (خ) differ only in the top (arrowhead or flat bar) and occur once each: قد and وخدي by sense. If
  they are one sign the second word is وقدي ("and my stature"), which reads less well.
- The red gloss: the mark over the first sign is small; و from the word.

## Prior work

The catalogue entry's vetting (15 Nov 2026) found no study of the manuscript and no reading: Penn TEI, Digital
Scriptorium DS738, DECODE, Tomokiyo, Lasry's key list, web searches, Voynich Ninja thread 4685. On 16 Nov 2026 two
web searches for the exact phrases of the two verses found no match, so the verses were not identified in a diwan
or an anthology. Whether they are Ibn al-Qaysarani's own is not known.

## Remaining gaps

None: every sign has a value and both verses read. The doubtful signs above are single signs inside words that
read.

## Escalation

- [x] siblings: ff. 105r-106r viewed; they hold other writers' messages in other alphabets, each with its plaintext
- [n/a] clear-pages: the plaintext leaf that followed f. 106v is lost
- [n/a] known-keys: the volume uses a different alphabet for almost every message; none was needed
- [x] print: no edition of the manuscript; exact-phrase searches for the verses found nothing
- [n/a] key-rebuild: the key is complete
- [n/a] retry: no unread sign is left
