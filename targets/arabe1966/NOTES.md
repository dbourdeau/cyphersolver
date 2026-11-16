# BnF Arabe 1966: one line of numerals under a colophon of 732 AH (catalogue 2890)

Status: in progress

Worked 15 and 16 Nov 2026 in two sessions. **Not solved.** The line was transcribed (23 numerals) and seventeen
families of system were tested; none gives a reading. What follows is the record, so the next attempt does not repeat it.

## The document

- Paris, BnF, Département des Manuscrits, Arabe 1966 (old Suppl. ar. 611), 47 leaves. Gallica ark
  `btv1b11001551n`, a black-and-white microfilm scan. `gallica.bnf.fr` answers 403 to scripts; the IIIF route
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b11001551n/f50/...` works.
- The main text is a short life of the Prophet and of the Ten Companions (title page, view 9: "Kitāb fīhi mukhtaṣar
  al-sīra", by ʿAbd al-Ghanī al-Maqdisī). Maghribi pieces are bound in front (views 4 to 8).
- Colophon, view 50, right-hand page: "... on Wednesday, of the month of Jumādā I, year 732" (Feb 1332). The day of
  the month is not given. It ends "wa-sallama taslīman kathīran / ilā yawm al-dīn".
- De Slane's catalogue, no. 1966: "A la fin du volume se trouve une ligne d'écriture secrète en chiffres indiens."

## What is on the page

Seen at native resolution (crop `pct:52,74,40,12`, 2,329 x 533 px) and enlarged four times.

- The last line of the colophon holds two things. At the right, in the black ink of the colophon, the words
  الى يوم الدين ("until the Day of Judgement"), which finish the blessing of the line above. The catalogue entry
  took these for "three or four Arabic letters" belonging to the cipher; they do not belong to it.
- The rest of the line, to the left, is 23 Eastern Arabic numerals in a paler ink (grey on the film, so perhaps red).
  The catalogue entry said "about 28".
- Left to right as they stand: `7 1 5 8 9 2 1 7 2 1 8 9 2 1 5 1 8 4 2 1 9 2 4` (`transcription.txt`).
  Right to left: `4 2 9 1 2 4 8 1 5 1 2 9 8 1 2 7 1 2 9 8 5 1 7`.
- Shapes: 4 has the old ʿayn-like head; 5 is the closed B-like form; 9 is a loop with a short tail. The 4 (twice) could
  be a 3 and the 9 (three times) a 6; both alternatives were run (below).
- No dots stand on or between the numerals, except one above the line between the last two at the right (2 . 4).
  A light-end contrast stretch shows no fainter dots. So zeros are not written.
- Spacing is even (centre-to-centre 27 to 66 px, no regular groups): no word or group division is visible.
- Under the line are two collation notes in other, darker hands, one dated Rajab 734. They are not a gloss.
- No other writing in the pale numeral hand was found in the volume (all 54 views looked at as contact sheets at
  1,000 px per opening; small pale marginal notes would not show at that size).

## Measured

- 23 digits, 7 distinct: 1 x6, 2 x5, 8 x3, 9 x3, 4 x2, 5 x2, 7 x2. No 3, no 6, no 0.
- Read right to left, every 1 is followed by 2, 5 or 7, and four of the five 2s follow a 1: `1 2` occurs four times.
- Read as numbers up to 28 the line cuts cleanly either way: left to right `7 15 8 9 21 7 21 8 9 21 5 18 4 21 9 24`
  (16 numbers), or with the digits reversed `4 2 9 12 4 8 15 12 9 8 12 7 12 9 8 5 17` (17 numbers).
- Digit sum 99.

## Tested, with result

Scripts are in `scripts/`. The word lists are the `wordfreq` Arabic list (modern) and a vocabulary counted from
Ṣaḥīḥ al-Bukhārī (12,927 word forms seen three times or more, from the `hadith-json` data on GitHub).

1. **Letters by abjad value with the zeros lost** (each digit one of three or four letters: 1 = ا ي ق غ, 2 = ب ك ر ...).
   `abjad_seg.py`, both directions, best word segmentation. Nothing reads. The absence of 3 and 6 also speaks against
   it: an Arabic text of 23 letters with no ل ج ش and no و س خ is very unlikely. Re-run with 4 read as 3 and 9 read as
   6: nothing reads. **Ruled out** as far as the transcription holds.
2. **Full abjad values** (40 8 40 4 for محمد): needs zeros, and none are written. **Ruled out.**
3. **Whole-word abjad sums** run together (92 = محمد, 715 = نسخه, 421 = الفقير all occur as substrings).
   `wordsum.py`, `wordsum2.py`. With no separators every cut of the string finds some word, so the test cannot
   confirm or refute anything. **Open, not testable at this length.**
4. **Alphabet position 1 to 28**, four orders (abjad, Maghribi abjad, hijāʾī, Maghribi hijāʾī), counted from either
   end, every way of cutting the digits into numbers, both directions (`ordinal.py`, 12,672 candidates); then the
   same with every shift and affine map mod 28 on the two clean cuts (`shift.py`). Nothing reads. **Ruled out** for
   these orders.
5. **Digit followed or preceded by a place marker** (1 = tens, 2 = hundreds), and the vertical strokes taken as
   zeros or as separators: letter strings worked out by hand, none reads. **Ruled out.**
6. **Plain substitution, one digit one letter.** The `1 2` pattern suggests ال, لا or يا. `subst.py` and
   `classical.py` with 1 = ا, 2 = ل; then `allpairs.py`, which fixes 1 and 2 to every ordered pair of letters in both
   directions and searches the other five digits. The best strings are word salad at the same score as hundreds of
   others (e.g. "ولي الوهاب اليه العاليه باع"). With seven symbols the key space is small enough that a real plain
   text in this vocabulary should stand out; none does. **Failed.** A plain text of rare names would escape it.
7. **Substitution on the 16 or 17 numbers** of the two clean cuts: nine distinct symbols over 16 or 17 places is
   below what a search can settle. Pattern fits such as "... الحاج الحسن" for the 17-number cut are easy to find and
   prove nothing. **Open, underdetermined.**
8. **Pairs of digits** (row and column of a table, the eight abjad words, the nine ايقغ groups): 23 is odd, and no
   pairing gives second digits in 1 to 4. **Ruled out.**
9. **Not a text**: a horoscope (16 numbers as eight sign-and-degree pairs: signs above 12 occur), numbers from the
   sīra (ages of 63, years 10, 13, 40 would need 0, 3, 6), the buduh square (4 9 2 / 3 5 7 / 8 1 6), a doubling
   series. None fits. A talismanic number string written as a preservative at the end of the book (Gacek, Vademecum,
   "Popular culture in manuscripts") stays possible and would have no reading.

10. **Digit = digital root of the letter's place in the alphabet** (hijāʾī in two orders of the last letters,
    Maghribi hijāʾī, Maghribi abjad), each digit standing for three or four letters (`classes.py`, both directions,
    both vocabularies). Short words turn up everywhere (ابن, ابو, ربنا, بعد for the hijāʾī order read right to left),
    as they must with three letters to a digit, but no cut makes a phrase. **Failed.**
11. **Two digits summing to a letter's value** (the splitting of a value into addends described for the medieval
    Arabic cryptologists): pairs from either end give sums that are not letter values (11, 13). **Ruled out.**

Prior art: the catalogue vetting of 15 Nov 2026 found none (DECODE, Cryptiana, de Slane, web). This session added
Gacek's *Arabic Manuscripts: A Vademecum for Readers* (full text on the Internet Archive): its entries on secret
alphabets, abjad and popular culture describe no numeral cipher of this kind and do not mention this manuscript.

## Second attempt, 16 Nov 2026

A second session re-read the image and ran further tests. **Still not solved.**

- The transcription was checked independently on the native crop (three enlargements, and a light-end contrast
  stretch): the same 23 numerals. The second numeral from the right (read 2) has a notched head and could be a 3.
  A small raised squiggle with dots stands between the last numeral and the black words; it is not read.
- The grey of the numerals on the film matches the grey of the drop-shaped ornaments beside the colophon lines, so
  the numerals are probably in the rubricator's red and of the time of the copy. Not confirmed without colour.
- The colophon names no scribe. A hidden scribe's name is therefore a reasonable guess for the content; it is a guess.

Tested, with result (scripts in `scripts/`; corpora fetched to scratch, not committed):

12. **Repeat-pattern (isomorph) search**, one token one letter, spaces ignored, for the three tokenisations (23
    digits; 16 numbers `7 15 8 9 21 ...`; 17 numbers `4 2 9 12 ...`) in both directions: against the whole Qur'an
    (Tanzil simple-clean, `iso_quran.py`) and the nine hadith collections of `hadith-json` (`iso_hadith.py`).
    No full-length match in either. Windows shortened by four tokens match only unrelated hadith phrases.
    **Failed**: the line is not a simple substitution of a Qur'an verse or of running prose found in these corpora.
    A personal name would escape this test.
13. **Reduced abjad values and digital roots after a shift of the alphabet** (28 shifts, abjad and hijāʾī orders,
    both directions, `reduced_shift.py`, Qur'an vocabulary plus a hand list of colophon words and names). Every shift
    gives word salad at the same score. **Failed.**
14. **Digit with a zero-count marker** (a digit followed or preceded by 1, 2 or 3 standing for tens, hundreds,
    thousands; also 2, 3, 4), every parse, both directions (`marker.py`, 5,440 letter strings scored). Nothing
    reads. **Ruled out.** This repeats item 5 by machine.
15. **Whole-word abjad sums with a colophon lexicon** (`ws.py`): `715` = نسخه at the left end and `421` = الفقير
    near the right end both fit, but 19 full parses exist with a small hand lexicon and none is a sentence. Against
    this family: 23 digits with no 0, 3 or 6 is very unlikely for a run of word sums. **Open, not testable** (as item 3).
16. **Letter positions in the basmala** as a key text (17-number cut): begins اسلم, then nothing. **Failed.**
17. **Not a text**, further: the digit sum is 99; the string holds `1518` next to `924` (924 AH is 1518 CE) and
    cuts into valid sura:verse pairs (7:158, 9:21, 72:18, ...). Each is the kind of fit a 23-digit string gives by
    chance and none extends to the whole line. **Noted, not a reading.**

### Independent third reading, 16 Nov 2026

A separate agent transcribed the line without seeing the earlier reading first and got the same 23 numerals. It
doubts the last numeral as well as the one before it (either could be a 3), and reads the squiggle as a terminal mark.

- **Structure (new):** the first 14 numerals are two seven-digit blocks differing in two places, `7 1 5 8 9 2 1` and
  `7 2 1 8 9 2 1`, followed by a nine-digit tail `5 1 8 4 2 1 9 2 4`. Against 20,000 shuffles of the same digits,
  `2 1` four times together with the repeated `8 9 2 1` has p = 0.008. The line is structured, not random numerals.
- **Whole-word abjad sums:** the best parse of the real string scores no better than its own shuffles (8th
  percentile). Items 3 and 15 move from "open" to **no signal**.
- Tested without a reading, both directions and with the 3/4 variants: multiplied abjad values (a·v+b, a 1 to 12,
  full decimal and zeros dropped); non-modular affine, squares and triangular numbers on alphabet position; index
  into fourteen key texts (Fātiḥa, Ikhlāṣ, shahāda, the colophon's own lines and others); differences, sums,
  running sums and period-2 keys on all three cuts (44,352 strings); letter-name values; Greek, Coptic, Latin,
  Hebrew, Syriac, Persian, Armenian and Georgian alphabets for the 1 to 28 cuts; the vertical strokes as dividers;
  decimal expansions, powers of two, amicable numbers; a date in the Seleucid, Yazdegerd or Coptic calendar
  (each needs a 0, 3 or 6).
- Print: a paraphrase of Ibn al-Durayhim's numeral methods (sites.wcsu.edu/mbxml/html/arab_ciphers.html) lists
  numerals for abjad values, splitting a value into addends and multiplying by 2 to 5; all need zeros or place
  marks and are covered above. No study of this colophon and no matching end-of-book numeral formula was found.

### Block structure followed up, 16 Nov 2026

- In writing order the 17-number cut falls into `4 2 9 | 12 4 8 15 | 12 9 8 12 7 | 12 9 8 5 17`, each later group
  opening on 12. Tried 12 as a word divider, as ال, as و and as an alphabet position: nothing reads.
- The three blocks as plain numbers (7158921, 7218921, 518421924, and reversed) show no arithmetic relation.
- The blocks as sign, degree and sexagesimal parts (`7 15 8 9 21`, `7 21 8 9 21`, `5 18 4 21 9 24`), checked
  against planetary longitudes for the Wednesdays of Jumādā I 732 computed with PyEphem: Saturn stood at 5 signs
  18 degrees in mid February 1332, which fits the third block, but no planet or node stood in sign 7 for the other
  two, and the Sun (signs 10 to 11) is absent. One fit in three is within chance. **Not a horoscope as it stands.**

## Remaining gaps
- the whole line, 23 numerals - blocker: too-short; seven symbols over 23 places with no word division, no second text in the same hand and no key; every standard numeral system tested fails

## Escalation
- [x] siblings: all 54 views of the volume looked at as contact sheets; no other line in the pale numeral hand. The two other numeral ciphers of the same sweep (BnF Arabe 2562, Wellcome MS Arabic 449) bear dots and letters and are a different system; neither has been worked
- [x] clear-pages: the two notes under the line are collation notes (one dated Rajab 734), not a decipherment
- [x] known-keys: no key is held; abjad values, reduced values and four alphabet orders tried as the known systems
- [x] print: de Slane no. 1966 and Gacek's Vademecum searched; the catalogue vetting covered DECODE, Cryptiana and the web
- [n/a] key-rebuild: nothing reads yet, so there is no key to extend
- [n/a] retry: nothing reads yet, so there is nothing to re-run

## What would move it

- The colour scan or the leaf itself: whether the numerals are red and of the scribe's time, whether dots were lost
  on the film, and the doubtful 4/3 and 9/6 shapes.
- Another line by the same hand, in this volume's margins (not visible at the size viewed) or in a sister
  manuscript of the same copyist or owner.
- A documented scribal numeral cipher of fourteenth-century Syria or Egypt to test. Ibn al-Durayhim's *Miftāḥ
  al-kunūz* (c. 1350) lists numeral methods; the edition (Mrayati and others, *Arabic Origins of Cryptology* 3) was
  searched for and is not online in full, so only the methods remembered from it were tried (items 1, 2, 5, 11).
