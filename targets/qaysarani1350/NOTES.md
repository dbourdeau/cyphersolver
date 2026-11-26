# Ibn al-Qabāqibī to the compiler of a Mamluk book of cipher verses (Penn LJS 51, f. 106v)

The folder name `qaysarani1350` is kept from the first reading of the sender's name, which was wrong (see
"Corrections from Alan Elbaum" below).

Status: read
Outcome: key recovered based on adjacent plaintext (a red gloss over the first five signs), 16 Nov 2026; one damaged
word of line 2 is open again since Alan Elbaum's corrections of 23 Nov 2026 (20 of 21 words read).
Catalogue: Unsolved Catalogue no. 2882 (class A), from the Arabic sweep of 15 Nov 2026
(`research/sweep_2026-11-15_arabic/part_A.md`).

## The document

University of Pennsylvania, Kislak Center, LJS 51, f. 106v (OPenn image 0084_0217), lines 6-12. The volume is a
first-person account by an unnamed Mamluk secretary of the cipher verses he exchanged with colleagues; after each
cipher he writes that he solved it and gives the verses. The sweep dates the text to about 1330-1370 (an estimate from internal evidence: an anecdote dated 730-odd AH and the people
named, one of a Damascus chancery family of that century) and Penn dates the manuscript "14--" ("possibly Syria, 15th century" for its origin) and gives
no date for the text. This is the last text in the volume. It is introduced by "wa-kataba li Ibn
al-Qabāqibī" (ابن القباقبي; Elbaum's reading, 23 Nov 2026, checked on the master TIFF the same day: the sweep's
"Ibn al-Qaysarani" and the parallel attack's "al-Qubabi / al-Qabbani" are both wrong). Under the cipher the compiler
writes فحللتها في الحال بحضوره وجدته جعل اللام الف (Elbaum's reading: "I deciphered it immediately in his presence, and I
found that he rendered the lām-alif [as a single letter]"; the bracketed words are his supplement) and the manuscript
breaks off, so the plaintext that followed is lost.

Images: https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_0217.tif (2339 x 2959 px, plain curl).
No image is committed here except the site crop.

## The system

Monoalphabetic substitution of invented signs for Arabic letters, written right to left, words divided by a
vertical stroke with three dots over it. 89 signs, 22 distinct, 21 words (measured on `cipher_tokens.txt`).
Lam-alif is one sign, with a small plain alif written above the line before it in line 1. Final alif maqsura is written as alif; no hamza, no shadda, no vowels. A word runs over the
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
| Y | ج | 5 | cup over a stem that ends in a closed loop under or left of the stem |
| G | ت | 4 | slanted stroke into a bowl with a loop at its end, like a 6 |
| S | د | 2 | hook and wave on the baseline |
| R | ر | 4 | triangle, bar, small loop |
| E | س | 3 | figure 8 (round in line 1, flat-topped in lines 4 and 6) |
| F | ي | 3 | loop or lozenge on a vertical stem |
| B | ف | 3 | flag with a small square or loop at the foot |
| D | ع | 2 | two loops of about equal size joined on the baseline |
| W | ض | 2 | three teeth with a stem down at the left |
| U | ح | 2 | cup on a stem whose foot turns to the right (a hook or a loop on the right of the stem) |
| O | ة | 1 | circle with an inner curl, abraded |
| J | لا | 1 | tall stroke joined to a bowl, abraded |
| A | ق | 1 | arrowhead over a stem and a circle crossed by the stem |
| Q | خ | 1 | flat bar over a stem and a circle crossed by the stem |
| C | ث | 1 | open curve with a loop on top, like an e |
| X | ص | 1 | one stem with a loop on each side of its top |

## How the key was recovered

1. Red letters stand over the first five signs of line 1. I read them as و ن ا ع س; they are و ت ا ع س (Elbaum; the
   second is a ta with two dots, as the parallel attack also read it). The value ن for the second sign comes from the
   word, not from the gloss: whoever added the red letters was still working the cipher out. With the sixth sign as ة the
   first word is وناعسة ("and many a drowsy-eyed woman"), a common opening of love verse.
2. The group Y B K T (..ان) follows J in line 1, وا in lines 4-5 and وا in line 7, the last time with H K after
   it. الاجفان / واجفان. / واجفانها: Y = ج, B = ف, H = ه, and J is the lam-alif sign the compiler mentions.
3. Line 1 and the first two words of line 2 then scan as a ṭawīl hemistich if the two-sign word is قد: "wa-nāʿisati l-ajfāni qad jaʿala l-hawā".
   جعل gives M = ل, الهوا confirms K M = ال.
4. ولم انم / ولم تسهر / ونامت (lines 5-6) give Z = م and G = ت; سهرت and تسهر share E H R. (First read ولم تسهد, with
   the damaged last sign of line 6 taken as S; it is R, see the corrections.)
5. The rhyme words ا.ضا (line 4) and م.ضا (line 7) with the same middle sign as in سه.ت: ارضا, مرضا, سهرت.
   R = ر, W = ض. The rhyme is -ḍā.
6. The second hemistich must scan faʿūlun mafāʿīlun faʿūlun mafāʿīlun and end in لها ارضا: ... مهجتي مثوا وخدي
   لها ارضا. Its first word stands in a damaged patch of line 2. It was read لها (lower loop of ل, ه whole, the body of
   ا, then a stroke taken as the divider without its dots); Elbaum points out at least two more letters there, so the
   word is **not read** (see the corrections). لها is what the metre allows, not what the page shows.
7. Line 5, the word between واجفاني and ولم انم: four signs, pattern short-long-long, third sign ا: صحاح
   ("sound"), set against مرضى ("sick") in the last hemistich.

Two false starts are in `WORKLOG.md` (جهنم for the damaged word; ع for the R sign).

## The reading

`reading.md` (Arabic, as enciphered and in normal spelling), `translation_en.md`.

وناعسةِ الأجفانِ قد جعلَ الهوى / [..ه..] مهجتي مثوًى وخدّي لها أرضا
سهرتُ وأجفاني صِحاحٌ ولم أنمْ / ونامتْ ولم تسهرْ وأجفانُها مرضى

Many a girl with drowsy eyelids: love has made my heart [her] dwelling and my cheek the ground beneath her. I lay
awake, though my eyelids are sound, and did not sleep; she slept and did not lie awake, though her eyelids are sick.
("her" in brackets stands for the damaged, unread word.)

## Checks

- Metre: both verses scan as ṭawīl in all four hemistichs (the second hemistich with لها supplied for the unread word), and both end in -rḍā (ارضا, مرضا).
- The key is one-to-one: 22 signs, 22 different letters; no sign has two values.
- The compiler's remark under the cipher says the writer made the lam-alif one letter; the reading has exactly one
  lam-alif sign, in الاجفان.
- The second verse is a known verse (Ibn al-ʿAdīm, *Bughyat al-ṭalab*, attributed to al-Agharr ibn Sinān al-Ḥalabī; see
  `reading.md`): it has صحاح and تسهر, as the page does.
- Statistical validation (run on the text before the corrections of 23 Nov 2026, one letter different, not rerun): **inconclusive at 89 signs** (Dudout's review, issue #714); it shows only that the text is Arabic-like under
  the key, and the annealer on the real text (-2.799) cannot find the reading by itself. It does not carry the reading, which rests on the
  metre, the rhyme, the grammar and the red gloss. Details (16 Nov 2026), `docs/_validate.py` with the new `lang/` model `ar-mamluk` (2.17 M letters: the
  diwans of Safi al-Din al-Hilli and Ibn Nubata, al-Safadi's Kashf al-hal and Alhan al-sawaji', al-Umari's al-Ta'rif; OpenITI),
  order 4, `validation.tsv`: reading -2.537 per letter; random keys -4.901 (z 5.3); keys refitted to the shuffled signs mean
  -2.881, best -2.745 (z 3.4): **pass**, narrowly. Seeds 2-4: weak (z 2.7), pass (5.7), pass (6.3); in all four runs the
  reading beats every refit. Negative control (`--control`): underdetermined (z 0.5). Short text: 89 signs, 4 tokens per type.
- Not checked against the solved alphabets on ff. 1r-106r: no sibling alphabet was compared.
- Uniqueness (issue #714): 7 of the 22 signs (8 of 89 tokens) rest on the sense of one word each (ح, ص, ث, خ, ق, ة, لا); 12 signs are forced (the five glossed signs and seven signs in several words: ج ف ه ل م ت ي); س ر ض are fixed by whole-verse sense and the rhyme pair, and no alternative competes. A word-list search over about 30 MB of OpenITI
  found 21,037 one-to-one keys that keep the gloss and make all 21 words attested forms, but only 6 distinct assignments for the
  multi-word signs, five differing only in ض. The words قد, مثوى, وخدّي and صحاح are chosen by sense (شحاح "stingy" scans too but breaks the
  antithesis).
- Reading review: grade B by an AI model's review for Brice Dudout (issue #714), replacing the authoring session's grade A. One word is read against the page and one is damaged (see `reading.md`); counted as read as one-digit slips, 19 of 21 words stand without them.

## Doubtful readings (grade M or I)

- Line 1, sign 6 (O): abraded circle; ة from the word (I).
- Line 1, sign 7 (J): abraded; lam-alif from الاجفان and the compiler's remark (I). A small plain alif stands above
  the line before it, so the text as written is الاجفان.
- Line 2, the word before مهجتي: **not read.** A damaged patch; a loop below the baseline, a whole ه, a third sign and
  a stroke survive, with room and traces for at least two more letters.
- Line 6, last sign: damaged in the middle; read R (ر) with Elbaum, from the small loop at its right end.
- A (ق) and Q (خ) differ only in the top (arrowhead or flat bar) and occur once each: قد and وخدي by sense. If
  they are one sign the second word is وقدي ("and my stature"), which reads less well.
- The red gloss: و ت ا ع س; the second letter does not agree with the value ن of the sign under it.

## Corrections from Alan Elbaum (23 Nov 2026)

Alan Elbaum (Princeton Geniza Project) sent eight corrections to the published page by email to Daniel Bourdeau on
23 Nov 2026. Each was checked the same day on the OPenn master TIFF (crops at 2x and 3x); seven are adopted as
confirmed, one as far as the image shows.

1. **Sender's name.** ابن القباقبي, Ibn al-Qabāqibī; there is no al-Qaysarānī, al-Qubabi or al-Qabbani. Confirmed.
2. **The compiler's remark.** فحللتها في الحال بحضوره وجدته جعل اللام الف [حرفا واحدا]. Confirmed for the words on the
   page (بحضوره had not been read); the last two words are Elbaum's supplement for the lost continuation.
3. **Supralinear alif.** A small alif stands above the line before the lam-alif sign of line 1. A small stroke is
   there on the TIFF; the earlier statement that no alif stands before the sign was wrong.
4. **The word before مهجتي (line 2).** At least two more letters than لها accounts for; Elbaum has no better reading.
   On the TIFF: a short stroke left of the divider and a loop below the baseline before the ه, an abraded gap, and after
   the ه a sign and a tall stroke on the lifted flap. Agreed that the ink is not accounted for by لها; the word is now
   open. Blocker: surface loss.
5. **تسهر, not تسهد** (line 6, last sign), in the manuscript and in the known poem. On the TIFF the sign is broken in
   the middle by surface loss; its right end is a small closed loop, as in the R sign, which the S sign does not have.
   Adopted.
6. **The red letters** are و ت ا ع س. Confirmed (two dots over the second). ن stays the value of the second sign.
7. **The ع of جعل (line 2).** The earlier note that it is as close to the ر sign was wrong: it has two loops of about
   equal size, like the ع of line 1; the ر sign has a triangle, a long bar and a small loop. Doubt withdrawn.
8. **The last letter of صحاح (line 5).** The earlier note that it is written like ج was wrong: its foot turns to the
   right of the stem, as in the ح before it (whose foot is abraded); the ج sign has its loop under or left of the stem.
   Doubt withdrawn; the word is صحاح as written, no emendation.

Effect: the key is unchanged (22 signs); one letter of the reading changes (تسهر); two emendations fall away; one
word of 21 goes from doubtful to unread. Elbaum calls the verses a "known poem"; his source was not stated.

## Who was Ibn al-Qabāqibī? (open dating question, 24 Nov 2026)

The two men of this nisba found so far both lived in the early 15th century: Shams al-Dīn Muḥammad b. Khalīl
al-Ḥalabī Ibn al-Qabāqibī, a scholar of the Qur'an readings, born in Aleppo 777/778 (1375-76), died in Jerusalem
20 Rajab 849 (22 Oct 1445) (TDV İslâm Ansiklopedisi; YEK authority record), and a Burhān al-Dīn Ibrāhīm al-Qabāqibī,
d. c. 850 (web results only, not checked). The works listed for Shams al-Dīn are on the Qur'an readings, plus
*takhmīs* poems and a *badīʿiyya*. None is a cipher or riddle work, and no source ties him to the compiler.
If the sender is one of these two men, the text dates from about 1395-1445, not 1330-1370. That would not conflict
with Penn's "14--" for the manuscript. The identification is not proven: it rests on the nisba alone. So the date
on the page stays as it is until a source places the sender, or the compiler's circle, in a decade.

Check of images 0067-0068, 24 Nov 2026 (name line cropped from master TIFF 0084_0067):
- **What the text says.** Ḥasan Ibn al-Qalāya(?) al-Mawṣilī brought the compiler a cipher written without word
  dividers, which he said had been enciphered by «ابن القبا[..]ي الحيسوب». The compiler solved it and mentioned it to
  "al-makhdūm". The makhdūm said that this Ḥasan had sent him a cipher in the same metre and claimed to know how to
  solve ciphers.
- **The name** has the skeleton ا ل ق ق/ف ا ى: two qāf-type teeth, each with two dots above, then alif and final yā'.
  That is shorter than القباقبي (ق ب ا ق ب ي), so it is either a defective spelling of the same name or a different
  one. It cannot be settled at this resolution.
- **The epithet** al-Ḥaysūb ("the great reckoner") is not given for Shams al-Dīn in TDV or YEK.
- **The circle.** The man works in the compiler's circle alongside "al-makhdūm". The 15 Nov sweep took al-makhdūm to be
  the volume's "al-maqarr al-makhdūmī al-ʿAlāʾī" and connected him with Ibn Faḍl Allāh, but neither identification has
  been checked. If both are right, this is ʿAlāʾ al-Dīn Ibn Faḍl Allāh, head of the chancery (kātib al-sirr), who died
  in 769/1368, before Shams al-Dīn (b. 1375) was born.

Both checks, run the same day (master TIFFs 0084_0217 and 0084_0067; web images 0038, 0083 and 0152):
- **The spellings differ.** f. 106v has ابن القبا…بي: final yā' with two dots below, a bā' dot before it, and a long
  kashida in the middle that may hide the second qāf (Elbaum: القباقبي). 0067 has ابن القبا[ن] الحيسوب: after the
  alif comes a bowl with one dot above, a nūn and not a yā'. So 0067 most likely names someone else (al-Qabbān?). It
  cannot date the sender of f. 106v.
- **The patron is an Ibn Faḍl Allāh, head of the chancery.**
  - f. 17r (image 0038) praises him in verse: «على باب ابن فضل الله حطت ركاب كل سباق عليم … الكريم ابن الكريم ابن
    الكريم» ("at the gate of Ibn Faḍl Allāh every learned racer has halted … the noble son of the noble son of the
    noble"). Three generations in the post.
  - f. 39v (image 0083): «فان ابن فضل الله صار بكفه مدار…».
  - f. 74r (image 0152): the compiler calls himself al-mamlūk, asks for his appointment decree (tawqīʿ) to be renewed,
    and sends ciphers to the qāḍī Nāṣir al-Dīn Ibn al-Shāṭ[?]ī, muwaqqiʿ al-dast al-sharīf. So the compiler is a clerk
    of the chancery.
  - "Noble son of the noble son of the noble" fits either ʿAlāʾ al-Dīn ʿAlī b. Yaḥyā (in office 1340s to 1368, d.
    769/1368; father and grandfather both chancery heads) or his son Badr al-Dīn Muḥammad (in office from 1368, with a
    break, d. 796/1394). The volume's "al-ʿAlāʾī" points to the first, but its folio was not found in this check.
- **Consequence.** The compiler served an Ibn Faḍl Allāh, and the last of them in office died in 1394. Shams al-Dīn
  Ibn al-Qabāqibī was born in 1375. He could have written to the compiler only as a teenager under Badr al-Dīn, and not
  at all under ʿAlāʾ al-Dīn.

**The patron is settled (page-through of images 0111-0222, 24 Nov 2026).** He is «المقر المخدومي العلائي» in at least
ten places (0151, 0160, 0170, 0179, 0181, 0189, 0190, 0197, 0204, 0208). Two were checked on the image here:
- 0197: «وكتب لي المقر المخدومي العلائي بسط الله ظلاله مترجما جواب الابيات المتقدمة», "the maqarr al-makhdūmī al-ʿAlāʾī,
  may God extend his shade, wrote me the answer to the verses above, in cipher".
- 0146: «امين الدين عبد الوهاب بن وهبان المزي الحنفي قاضي حماه اليوم», "Amīn al-Dīn ʿAbd al-Wahhāb Ibn Wahbān al-Mizzī,
  the Ḥanafī, qadi of Hama today".

No «بدر الدين» or «البدري» occurs. So the patron is ʿAlāʾ al-Dīn ʿAlī b. Yaḥyā Ibn Faḍl Allāh (d. 769/1368). Other
people the volume names:
- Zayn al-Dīn ʿUmar Ibn al-Wardī is mentioned as dead (رحمه الله, 0147). He died in 749/1349.
- The Ilkhan Abū Saʿīd (d. 1335) appears in the same anecdote.
- The vizier Ibn Zunbūr (0207).
- Ibn Wahbān is qadi of Hama "today" (0146). From memory, not checked: he died in 768/1367, so the date needs a source.

Taken together, the text was written about 1349-1367, in the lifetime of the patron. Shams al-Dīn Ibn al-Qabāqibī
(b. 1375) is excluded.

**First half (images 0001-0110) agrees.** «المقر المخدومي العلائي» appears about 25 more times (e.g. 0007, 0012,
0013, 0028, 0063-0066, 0071). Badr al-Dīn here is only Shaykh Badr al-Dīn Ḥasan al-Jawlānī, a correspondent; no year
is given. These hits come from an agent's page-through and were not checked on the image here.

**Hypothesis tested and not supported (24 Nov 2026): the compiler is NOT Ibn al-Durayhim (ʿAlī b. Muḥammad, 712-762/1312-1360).**
Read on images 0103-0104 here: the compiler quotes Ibn Dunaynīr and Ibn al-Durayhim as authorities («إذا عرض المرموز فالخل جوهرا من ابن دنينير وابن درهم») and builds a riddle on their names. He explains that «الدريهم» was the nickname
of a remote ancestor, the diminutive of dirham. That is the story Arabic Wikipedia gives for Ibn al-Durayhim's laqab, so he knows
the man's biography, which is how one writes of a third party. Also: f. 61v puts Ibn ʿAdlān, Ibn Dunaynīr and al-Kindī among the dead authorities; the compiler is a chancery clerk
(mamlūk, asks for his tawqīʿ, f. 74r), while the biographies of Ibn al-Durayhim (TDV; ar.wikipedia) show a merchant-scholar, a müderris at the Umayyad Mosque, and an envoy who died
at Qūs in 762/1360, with no vizierate of Syria in either source (the Alukah article, 403, and al-Ṣafadī's A'yān al-'aṣr vol. 3 pp. 521-528, were not read).
The vizierate passage (0095-0097) and the verse rhymed on علي (0110) are about another man and stay unidentified. The clues first raised were:
- 0095-0097: the compiler refused the vizierate of Syria and asked the patron to have him excused.
- 0103-0104: a play on Ibn Dunaynīr and Ibn al-Durayhim that mentions "the great-grandfather's nickname al-Durayhim".
- 0110: a solution matches "his noble name and the mamlūk's name" in a verse rhymed on علي, which suggests both men
  were called ʿAlī.
- 0209: the book «مفتاح الكنوز في حل المرموز» is named.

Verdict (24 Nov 2026): the redating is not supported, and the page keeps "about 1330-1370". The sender is probably an
earlier member of the family that bore the nisba. The internal evidence above narrows the page's "about 1330-1370" to
about 1349-1367. Narrowing the page is optional and waits on a source for Ibn Wahbān's death date. Source: `research/sweep_2026-11-24_arabic_treatises/README.md` (YEK section), branch
`worktree-agent-ad884b8b47d2b32f1`.

## Prior work

First modern reading of the cipher lines, corrected in eight places by Alan Elbaum (above); the compiler's own solution, which his remark says he made, is lost with the leaf that followed. Not "never solved
before". Penn's record (OPenn TEI, "approximately 150 alphabets", authorities al-Jindi al-Ala'i, Burhan al-Din al-Qudsi, Taqi al-Din al-Husayni) does not mention
Ibn al-Qaysarani and gives no reading of f. 106v.

The catalogue entry's vetting (15 Nov 2026) found no study of the manuscript and no reading: Penn TEI, Digital
Scriptorium DS738, DECODE, Tomokiyo, Lasry's key list, web searches, Voynich Ninja thread 4685. On 16 Nov 2026 two
web searches for the exact phrases of the two verses found no match, so the verses were not identified in a diwan
or an anthology. They are not the sender's own: the second verse is quoted by Ibn al-ʿAdīm (d. 1262) under an earlier poet (`reading.md`), found after the reading.

## The attempt from the images alone on the same leaf (`targets/ljs51/`)

A separate session attacked f. 106v from the images alone (with the red gloss and the compiler's remark as given) on 15-16 Nov 2026 (PR #706, folder
`targets/ljs51/`) and did not read it. Main keeps that folder as a labelled record of a superseded, failed parallel attempt
(`Status: no write-up`; this folder is the target of record): `NOTES.md` (its log), `profile.json` (its profile), its transcription (`transcription.txt`,
with `transcription_divshift.txt` for its divider hypothesis), `solve.py`, `wordsearch.py`, `scansearch.py` and `BRIEF_arabist.md`. The classical Arabic
poetry model it needed is `ar-classical-poetry` in `lang/` (788,143 verses, scheme `arabic28`; build with `python -m lang.build_ar_poetry`). Its
transcription and values were compared with this folder's on 16 Nov 2026 by sign position with `targets/ljs51/compare_with_key.py` (output in
`targets/ljs51/compare_with_key.txt`; the images were not opened for it):

- **Transcription: agrees in the main.** Both read seven lines; the sign counts per line match in six (line 6: 13 against 12;
  90 signs against 89). The attack used 25 labels, this folder 22. At 85 aligned positions (line 6 omitted from its
  third word, where the divisions differ) the attack's labels, each matched to this folder's sign it most often stands on (a best fit, since its labels are arbitrary: 25 labels onto 22
  signs), agree at 77 (91%), eight of them labels used once; the
  other 8 are where its label covers a different sign of this folder (its Y covers ج, ح and خ; its D ه, ل and ص; its F, P and Q two
  each), and it split some of this folder's signs in two or three (for example its H and L are both ا, and its C, R and Z are all م).
  So the two sessions saw the same shapes in the main, but the shape classes are not identical; the images were not
  compared again for this note.
- **Values: the attack recovered few.** It named 10 signs "firm". At the 63 aligned positions where it had a firm value, 37
  match this folder's key; 26 of those are its alif (17) and waw (9), the two commonest signs. For the other 8 signs
  11 of 37 positions match (lam for its A, ha for D, dad for X); the rest are wrong (its Y = mim, K = tha, M = lam, P = ya,
  F = kaf are in this folder ج, ف, ن, ر, ي/ق). Its red-gloss values for line 1 differ from this folder's in two of five letters (ta
  and ghayn against nun and ayn); with its values I find no word for the first
  group, with this folder's it is وناعسة.
- **Key structure: the attack's hypotheses were wrong.** It needed homophones (two signs for lam, two for ha) and an alif
  sign that also stands for lam; the accepted key is one-to-one over 22 signs and the sign it took as alif-and-lam is alif
  at all 17 of its positions (18 alifs in the text). It tested "lam-alif is one sign" (the compiler's formula) and found no sign that takes it: this
  folder's lam-alif is the rubbed single sign of line 1 (the attack's T, which it had read as alif). Its theme ("a reply on the
  taṣḥīf of jim and ha") was not borne out: the verses are a love couplet.
- **Metre and rhyme: agrees.** The attack established ṭawīl on its own and a rhyme in -ā, with the second-last letter ض;
  it had ي where the accepted reading has ر (ايضا against ارضا). Its bayt 1 scans in its skeleton; its bayt 2 was a syllable too long and
  scanned only with a null alif added (its step 15); the accepted reading needs no null.
- **Sense: not read.** Its best skeleton read about half of the signs as words (the closing half of its first bayt, هما
  كانوا وما كلها ايضا), none of them the accepted words; a few short words coincide (الهوى, لها). Its own conclusion was a
  scanning candidate, not a reading, and the metre could not choose among over 100,000 readings of the opening half
  (`targets/ljs51/scansearch.py`). So the independent search **failed** to read the text; it found the metre, the rhyme class, the
  glyph inventory and a handful of letters, and it is the evidence from the images alone for how far metre alone gets on an
  89-sign, 22-sign cipher with six single-use signs.
- **A fault in the attack's language model, found on integration.** `lm.norm(..., 'arabic28')` turned vowel signs into spaces instead of
  dropping them, so a vowelled verse of the corpus (the build keeps the signs) was cut into letter fragments. It is fixed in
  `lang/lm.py`. The attack's runs (annealing scores, `wordsearch.py`, the syllable table of `scansearch.py`) predate the fix and
  were not rerun here (the corpus is not in the checkout, and was not rebuilt), so the failure is that of the search as run; it
  is not shown that the fixed model would also fail (the attack's 100,000-readings count also comes from the pre-fix syllable table), and the scores in the attack's log should not be compared with `ar-mamluk`.
- **The attack was right about one gloss letter (ta at position 2; Elbaum, 23 Nov 2026) and wrong about the other.** As written on 16 Nov: the gloss letters at positions 2 and 4 (ta and
  ghayn, against the key's nun and ayn) and the sender's name (next bullet). The key's own checks (the words وناعسة and الاجفان, the metre,
  the rhyme) fit nun and ayn; the images were not re-read for this note.
- **The sender's name (settled 23 Nov 2026: Ibn al-Qabāqibī, neither reading below).** The attack re-read the name after "wa-kataba li" at 5x as Ibn al-Qubabi (or
  al-Qabbani), the same man as "Ibn al-Qubabi al-Haysub" on images 0067-0068 of the volume, not Ibn al-Qaysarani. This folder
  took the name from the sweep and did not re-read it. The two readings are not reconciled; the title keeps the sweep's
  name until someone re-reads the leaf.
- The attack's "brief for an Arabist reader" (`targets/ljs51/BRIEF_arabist.md`) was written for a reply on the taṣḥīf and for a reading that was not
  established; it is kept as a record, not as a statement of the text.

## Remaining gaps

Twenty of 21 words read (86 of the 89 transcribed signs). Open:

- **Line 2, the word before مهجتي.** Blocker: illegible (surface loss and a lifted flap); at least two letters more than
  the three signs transcribed. Elbaum has no reading either. Needs the leaf itself or multispectral images.

Three checks would strengthen the reading (Dudout, issue #714), none of them an outside blocker to the reading itself:

1. Done 23 Nov 2026 on the master TIFF with Elbaum's corrections: صحاح stands as written; the first word of the second hemistich is unread.
2. al-Qalqashandi, *Subh al-a'sha*, vol. 9 (the chapter on cipher), and *Arabic Origins of Cryptology* (Mrayati, Meer Alam, at-Tayyan; Ibn
   Adlan, Ibn ad-Durayhim): the likeliest places for these verses to have been printed before. Not searched.
3. The 22 signs against the solved alphabets on ff. 1r-106r: a shared alphabet would confirm A/Q and the one-word signs independently of the sense.

## Escalation

- [x] siblings: ff. 105r-106r viewed; they hold other writers' messages in other alphabets, each with its plaintext
- [n/a] clear-pages: the plaintext leaf that followed f. 106v is lost
- [n/a] known-keys: the volume uses a different alphabet for almost every message; none was needed
- [x] print: no edition of the manuscript; exact-phrase searches for the verses found nothing
- [n/a] key-rebuild: the key is complete
- [x] retry: the damaged word of line 2 re-read on the master TIFF at 3x on 23 Nov 2026 with Elbaum's corrections; not legible
