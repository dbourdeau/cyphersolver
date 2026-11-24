# Fonds Roux MS 35c, f. 26v: the copyist's name in a colophon of Muharram 883 AH (catalogue 3812)

Status: in progress

Worked 23 Nov 2026 in one session. **Not solved.** The scan was found, the colophon was read, and the "secret
script" is most likely two-tier writing in ordinary letters, not a cipher. No word of the copyist's name is read
with confidence: a first reading ("Muhammad ibn Abd Allah") was withdrawn when an enhanced image showed that
"Ubayd Allah" fits the same strokes. No site page: the name is not read and nothing has had a second reader.
No image is to be requested from the MMSH (user, 23 Nov 2026); the Nakala scan is the only source.

## The document

- Aix-en-Provence, Médiathèque de la MMSH, Fonds Arsène Roux, MS 35c. 27 loose leaves, 207 x 147 mm, two columns.
  Kept with 35a and 35b in one leather cover (MS 35).
- Van den Boogert, *Catalogue des manuscrits arabes et berbères du Fonds Roux* (1995), item 35c: anonymous verse work
  on Qur'an readings, colophons on f. 26v, "name of copyist written in a sort of secret script", Muharram 883.
- The Nakala record (deposited 2025) repeats this: "Le nom du copiste semble écrit dans une graphie secrète."

## Access

- The catalogue entry said no public scan exists. One does: Nakala `10.34847/nkl.756deh54`, 33 JPEGs and a PDF,
  Etalab 2.0 licence. Found through the Nakala search API (`https://api.nakala.fr/search?q=MS_035c` with
  `fq=collection=10.34847/nkl.6e0dvw7q`, the Roux manuscripts collection).
- Images: `https://api.nakala.fr/iiif/10.34847/nkl.756deh54/<sha1>/full/900,/0/default.jpg`; the original file is
  `https://api.nakala.fr/data/10.34847/nkl.756deh54/<sha1>`. Both work with curl. Originals are 300 dpi
  (image 28: 3,878 x 2,771 px for the opening), and that is the best there is: the PDF holds the same images.
- Cinumed (`cinumed.mmsh.univ-aix.fr`) shows a "prove you are human" slider to curl and to the built-in browser.
  It was not needed. The Wayback Machine was unreachable from this machine. Calames serves a script-only page.
- Other Roux manuscripts are in the same Nakala collection with the same routes.

## What is on the leaf

- Image 27, left page = f. 26r. Image 28, right page = f. 26v. They are one leaf: the cut lower corner matches.
- f. 26r, right column, in the poem itself: "تم بحمد الله هذا الرجز / في خامس العشرين من ربيع / عام ثمانمائة وعشر",
  the poem was finished on 25 Rabi' 810. A few lines on: "ميمون في يمن وسعد طالع". Left column:
  "جاد به المنسوب للفخار / ميمون ...". So the author names himself: Maymun, known as al-Fakhkhar.
- f. 26v: two closing verses of blessing on the Prophet, then the copyist's colophon in four lines of smaller script,
  then two verses giving the number of lines, then hadith and prayers in other hands, and notes written up the
  right margin. The modern pencil number at the top is "31".
- The colophon's first line calls the work "الدرة". With the author's name and the subject (the pointing of the
  hamza and the vowels) this points to *al-Durra al-jaliyya* of Maymun al-Fakhkhar (d. 816 AH). Not checked against
  the printed edition; the catalogues list the work as anonymous.

## The colophon

Full text and translation in `reading.md`; crop in `colophon.jpg`.

- Line 1: the work was completed, with the usual blessing. Read.
- Line 2: "by the hand of the ... sinful, poor servant ..., who hopes for the pardon of his Lord", then the name
  group. Two words in the clear part are not read.
- Line 3: finished "في أوائل المحرم عام ثلاثة وثمانين وثمانمائة", the first days of Muharram 883 (the month began
  about 4 April 1478). Read. This agrees with the catalogue's date.
- Line 4: "he wrote it for himself and his brothers, then for whomever God wills after him". Read.

## The name group

Crop in `name_group.jpg` (four times enlarged). Looked at in colour and in stretched greyscale, at four, seven, ten
and twelve times; four to seven times is the useful range, above that the strokes dissolve.

- It is the end of line 2. The scribe had run out of line and wrote the rest in two tiers in the height of one,
  with long parallel connecting strokes, then turned up into the left margin with very small writing.
- No sign in it is foreign to Maghribi script. What can be followed is letters: an initial ha with a long stroke to
  a mim, alif-lam pairs, nun bowls with their dots, a ta with two dots.
- Secure: upper tier, first word "تعلى" (ta'ala), which closes "عفو ربه تعالى".
- Lower tier, first word: "محمد" or "عبيد الله", not decided. Three dots sit under the stroke, one then two reading
  right to left; "عبيد" (ba, ya) explains them, "محمد" does not. The looped blot suits the mim of "محمد" better.
- Next: a word beginning with ayn over a large bowl with one dot ("عبد", or "عمر بن"), then a word in "الـ" with a
  kaf-like top stroke and a final mim ("الكريم" fits best; "الحكيم", "الرحيم" possible). "عبد الكريم" is a candidate.
- Then a small stacked group, a word with two uprights (a nisba), and tiny marginal words.
- The enhanced image is `name_group_enhanced.jpg`: blue channel, divided by a 70-px Gaussian background, CLAHE,
  bilateral filter, eight times. It shows more than the colour crop; greater enlargement adds nothing.
- So the catalogue's "sort of secret script" is most likely this cramped two-tier ending. That is a judgement from
  one image; a clear photograph could still show a deliberate device in the part that cannot be followed.

## The sibling MS 35b: an enciphered signature that can be seen

Found at the end of this session. MS 35b (Nakala `10.34847/nkl.cd896va1`, 73 images), kept in the same leather cover
as 35c, ends on its last page (image 73, f. 72v) with a colophon whose formula matches the 35c one:
"... ولا حول ولا قوة إلا بالله العلي العظيم على يد كاتبه لنفسه ولمن شاء الله بعده", then the scribe's name in a mix of
Arabic letters and non-Arabic signs, then "المتعلم" and a large word read "الاسراع" with a long tail. Crop:
`ms35b_f72v_signature.jpg`.

- Transcription, right to left, as the signs stand: `سرسر ابرا oB برظ 7 ابر عأ سرسر سراعم / المتعلم الاسراع`.
  "o" is a small closed circle, "B" a Latin-B shape, "7" a hooked stroke, "ظ" a ṭāʾ-like loop with a dot. The
  Arabic letters are clear; only the signs are foreign.
- The hand of 35b (small, 20 long lines) is not the hand of the 35c poem. Whether the 35b colophon hand is the
  35c colophon hand, and whether the left tip of the 35c knot (small digit-like marks) uses the same signs, could not
  be settled at 300 dpi.
- Tested on the Arabic letters of the signature (`sig35b.py` in the session scratchpad, not kept): every shift and
  the mirror order of the Maghribi, Mashriqi and alphabetical orders, and the ayqaġ swaps within abjad value groups.
  No family gives a single name. "بر" twice suggests "بن", which none of these families produces.
- Not tried: reading the signs as ghubār or Fāsī numerals with abjad values (no reliable sign table to hand), and
  a free monoalphabetic fit (too few letters).
- One hypothesis, not tested further: "ابرا" + "oB" is "ابراهيم" with the signs standing for its last letters, "بر" is a
  loosely written "بن", and the "سرسر" runs are zigzag fillers, giving "Ibrāhīm ibn [sign word] ibn [ʿ...]". If so,
  the signs replace only some letters, and "Ibrāhīm" would not fit the 35c knot's first word (محمد or عبيد الله).
- This is a separate cipher, not catalogue 3812. It is the best route to 3812 if the two scribes are one man.

## Remaining gaps

- The copyist's whole name, nine or more words, and the marginal words - blocker: illegible; on the 300-dpi Nakala scan, the only image online, the strokes are about three pixels wide and the two tiers overlap; candidates only (محمد or عبيد الله, then عبد الكريم)
- Two words in the clear part of line 2, after "العبد" and before "الراجي" (outline ىوىد) - blocker: illegible; paper damage at the first, the second too small to choose between readings

## Escalation

- [x] siblings: f. 26r (the facing side of the leaf) read, it gives the author and the poem's date; MS 35, 35a and 35b records opened on Nakala; all 73 images of 35b seen, its last page carries an enciphered signature (section above), not read; the Roux collection's copyist fields searched, no fifteenth-century scribe
- [x] clear-pages: all 33 images seen as 900-px contact sheets, no second signature or ownership note seen at that size; the notes up the right margin of f. 26v enlarged, too small to read
- [n/a] known-keys: no substituted signs were seen, so no alphabet table applies
- [x] print: web search for the poem's closing verses and for al-Durra al-jaliyya: one forum thread, nothing on this manuscript; the printed edition not seen
- [n/a] key-rebuild: there is no key, the group is ordinary letters written in two tiers
- [x] retry: the group re-read in colour, stretched greyscale and a flattened blue channel with CLAHE at four to twelve times from the original JPEG; the first reading was withdrawn, nothing is decided

## Transcription doubts

- تعلى (line 2, upper tier) - read: تعالى; checked: image, decode; two dots over the first letter, ayn head, long stroke to a tall lam; fits the formula after ربه
- first word of the lower tier (line 2) - read: undecided, محمد or عبيد الله; checked: image, decode; the three dots underneath favour عبيد, the looped blot favours محمد
- word in الـ after the ayn word (line 2) - read: undecided, الكريم preferred; checked: image, decode; kaf-like top stroke and final mim with tail
- الدرة (line 1) - read: الدرة; checked: image, decode; could be الدرر, the last letter is small

## Files

- `ms35b_f72v_signature.jpg`: the 35b signature (Nakala, Etalab 2.0).
- `transcription.txt`: the four lines as they stand. `reading.md`: the colophon, Arabic and English, and the
  description of the name group.
- `colophon.jpg`, `name_group.jpg`, `name_group_enhanced.jpg`: crops from the original image. `f26r_spread.jpg`, `f26v_spread.jpg`: the two
  openings at 900 px. Image credit: Médiathèque de la MMSH, Fonds Arsène Roux, MS 35c, via Nakala, Etalab 2.0.
- `pages/`: all 33 images at 900 px, the original of image 28 and working crops (git-ignored).
- `profile.json`.
