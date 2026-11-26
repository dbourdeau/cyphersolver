# YEK scanned records: image screening (26 Nov 2026, signed-in Chrome)

Viewer works when signed in: detail page -> green "Image" icon (link text "Image"/"Goruntu") opens an overlay with thumbnails and a "Page [n] / N  Go" box.
Routine: navigate to /works/detail/<bib>, click the Image link by JS, type the page number in the box, click Go, wait 3 s, screenshot. Pages load in
3-4 s; thumbnails fill in slowly. Image counts are spreads (two folios per image) plus covers. Printed books (matbu) show no Image link even when the
facet is 1.

Classes: real ciphertext / cipher key or alphabet table / worked examples in the text / plain / magic / other.

## Per-item table (appended as screened)

| bib | shelfmark | title | date | folios / images | what the pages show | class |
|---|---|---|---|---|---|---|
| 707036 | Arkeoloji 00557 | Rumuz al-kunuz (Shuja' al-Din Ilyas al-Akhisari) | copied 1047, composed 965/967 | I+51+I ff., 57 images | Ottoman Turkish prose, 19 lines, red rubrics and marginal numerals (images 1, 20 seen). Jafr/cifr prophecies about statesmen under Suleiman | plain (occult prose) |
| 209748 | Vehbi Efendi (Bagdat) 01592 | Tashil al-majaz ila fann al-mu'amma wa'l-alghaz (Tahir al-Jaza'iri) | printed Damascus 1303 AH, 128 pp. | no scans online (printed, no Image link) | -- | not screened |
| 324419 | Reisulkuttab 01197-001 | al-Marmuzat al-'ishrun (Sadr al-Din Muzaffar) | copied Ramadan 705 | 47 ff., 203 images | Arabic prayer/supplication text, verse and prose with red rubrics (image 20) | plain (Sufi supplications) |
| 715204 | Esad Efendi 01704 | Marmuzat-i Asadi (Najm al-Din Daya) | copied 735 | 61 ff., 68 images | Persian Sufi prose, 23 lines, glosses in margins (image 14) | plain |
| 120865 | Konya Yusuf Aga YY4887/3 | Kashf rumuz (attributed Ibn Wahshiyya) | copied 707 | 57 ff. of a 201-image volume; class 540 (alchemy) | Images 100, 110, 117 (other texts: Arabic/Persian prose) and 150 (20-line naskh prose) seen; the span of /3 not located. No sign runs, tables or alphabets in any sampled image | plain (alchemical prose, sampled only) |
| 584479 | Ankara Adnan Otuken 06 Hk 1108 | al-Tiraz al-asma 'ala kanz al-asma fi'l-lughz wa'l-mu'amma (Ibn al-Bukka') | 1122 | 27 images | Rubricated Arabic treatise, chapter headings on kinds of riddle (taqlib, tabdil, tashif style); no tables or signs (image 8) | plain (name-riddle theory) |
| 93193 | Manisa Il Halk 2976/8 | al-Tiraz al-asma (Ibn al-Bukka') | undated | volume of 289 images (muamma collection) | Opened; page image did not load, thumbnails 1-9 are rubricated Arabic text pages | plain (same text as 584479; not seen at reading size) |
| 93197 | Manisa Il Halk 2976/9 | Kenz al-asma fi 'ilm al-mu'amma (Nahrawali) | undated | same 289-image volume | Arabic prose, red rubrics, no signs (image 10) | plain |
| 261943 | Hafid Efendi 00296 | Kenz al-asma fi kashf al-mu'amma (Nahrawali) | undated | 20 images | Arabic prose with red rubrics, no signs (image 12) | plain |

Step 1 result: none of the signed-in "worth a first look" items holds ciphertext, sign alphabets or tables. Bagdat 1592 is a printed book with no scan. The mu'amma
treatises (Ibn al-Bukka', Nahrawali) are the name-riddle genre (letter-value and letter-transposition riddles), not cryptography.

## Step 4: the Ottoman Fourth Army pair (answer)

| bib | shelfmark | title | date | extent | what the pages show | class |
|---|---|---|---|---|---|---|
| 708867 | Arkeoloji 01652 | Sifre miftahi defteri | undated (Fourth Army cipher, Erzurum and Van) | 35 ff., 85x140 mm, 91 images; written images about 5-38, the rest blank | Seen: images 4, 6, 8, 13, 20, 30, 34, 36, 40, 45, 80. Image 6 (f. 5b) is headed "(for) the Fourth Imperial Army, Erzurum, Van and (vilayets): the key to the cipher": a 4-row letter table, each Arabic letter with two or three **two-digit numbers** (e.g. alif 14, 76 ...; homophonic substitution, numbers 11-99). Images 7-34 are a vocabulary: Ottoman words and names, several variants per entry, each with a **three-digit number** (427-899 seen, e.g. 445 vilayat, 447 vaka', 477 Yunanistan), entries ticked or struck through; image 8 headed "words special to the arrangement of the key". Image 36 (f. 35) repeats the letter table in pencil (letter + number), with a column of numbers 14-19 | cipher key (homophonic letter table plus code vocabulary) |
| 708872 | Arkeoloji 01660 | Makam-i Seraskeri ve Ordu-yi Humayunlar Musiriyyet-i Celilelerine yazilan sifreli telgrafnameler | 1305-1306 AH (1889-91) | 112 ff., 200x320 mm, 115 images (cover, flyleaves, then one message per leaf, versos blank) | Seen: images 3, 20, 40, 55, 70, 85, 100, 115. Every message is **clear Ottoman Turkish in rika script**, 2-10 lines, headed "Makam-i Seraskeri'ye" (or the army command), one telegram on each recto, versos blank (about 100 messages). Cover (image 115) reads "sifreli telgrafnameler 1305, 1306". No number groups, no cipher text in any sampled image; thumbnails 1-16 look alike | decoded copies only (plain) |

**Answer.** The 01660 register is a fair copy of the *deciphered* text of outgoing cipher telegrams ("sifreli telgraf suretleri", as the catalogue summary has it), not
the figures. 01652 is the matching key (the Fourth Army's table for Erzurum and Van: a letter table with 2-3 two-digit homophones per letter plus a vocabulary of
about 400+ words and names with three-digit numbers, so a nomenclator). No telegram of 01660 is in figures in any of the 8 sampled images (3, 20, 40, 55, 70,
85, 100, 115 of 115), so the pair gives **a key without ciphertext**, not a plaintext/ciphertext pair. Extents: 01660 112 ff. (about 100 telegrams, one per leaf),
01652 35 ff. with about 33 written pages. 01652 itself is a transcribable late-Ottoman nomenclator (letter table 32 letters, about 400 vocabulary lines); the
catalogue "end lines" of 01652 give pairs like letter:number (la 25, m 27, n 19, w 18, y 93), i.e. the same letter table in the final pencil copy.

## Step 3: Ibn Dunaynir and Ibn 'Adlan, Fatih 5300 (one volume, 192 images)

| bib | shelfmark | title | extent | what the pages show | class |
|---|---|---|---|---|---|
| 244314 | Fatih 05300-003 | Zubdat al-fusul (Ibn Dunaynir), fi hall al-taraajim | catalogue ff. 54-88; images about 55-93 (leaf numbers 53-93 pencilled) | Arabic naskh prose, 17 lines, one hand with 5300-004. Images 56, 60, 76, 92: prose. **Images 68 and 85-86 hold worked tables**: a ruled 8x4 grid of letter shapes over digits (image 68, right page, "the form of ..." heading; a line of eastern digits in the left page), a 5-row grid of dotless letter shapes, a 4x4 table of two-letter groups (image 86, "the cipher letters in a table") and rows of single signs. They illustrate the shape-reduction and 'tarjama' procedure, not a message to solve | worked examples in the text (letter-shape tables), known printed text |
| 244315 | Fatih 05300-004 | al-Mu'allaf li'l-Malik al-Ashraf fi hall al-taraajim (Ibn 'Adlan) | catalogue ff. 89-119; the treatise really fills **images 94-134** (about 41 images, leaf numbers 93-133; image 135 is a blank leaf with the heading "Risalat anbab" in a new work that runs on to about image 185) | Images 94-125 seen in sequence, then 130, 134-135, 140, 147, 155, 162, 170, 178, 185. Dense 19-21 line prose throughout. **Non-prose pages: image 100 (a line of separated letters), 106 and 110 (lines of word-pattern examples, e.g. a row of four- and three-letter word forms), 112-114 and 118-119 (rows of dotless skeletal letter shapes with counts above them, two tables of about 30 shapes each; image 119 has the shape row again), 123-130 (centred lists of words grouped by letter patterns).** No cryptogram, no message in cipher, no figure, no invented signs. Image 120 begins a new chapter (basmala heading). The treatise is the literature the Damascus edition prints | worked examples in the text (shape tables, word-pattern lists); no ciphertext |

Findings. The extent of 5300-004 in the catalogue (ff. 89-119, 31 ff.) understates the treatise: by the leaf numbers on the images it occupies about 41 images (images 94-134); the
file's later images (135-185) are another work ("Risalat anbab ..."), not part of Ibn 'Adlan. Not compared in detail with the Damascus edition (Mrayati, Meer Alam, Tayyan 1987);
its text was not found online in this session, so the chapter order of the manuscript against the edition is not checked. Both items are the published treatises and carry
tables only of letter shapes: nothing in them is an unread ciphertext.

## Step 3 (continued): Ibn al-Durayhim, Miftah al-kunuz fi idah al-marmuz

| bib | shelfmark | extent | what the pages show | class |
|---|---|---|---|---|
| 718705 | Esad Efendi 03558-006 | ff. 47b-59a (21 lines), copied by Mustafa Sidqi b. Salih, 10 Ramadan 1149; images about 50-62 of 95 (leaf number = image - 3) | Images 50-62 seen in sequence. 21-line naskh with red rubrics and marginal glosses. Image 55: a red row of eight signs. Image 56: number and letter rows. **Images 58-59: a block of eight rows of invented signs with red dots (a sign alphabet and sign-written sample lines).** Image 62 (f. 59a): colophon, the next work (red heading) starts at leaf 60. Image 20 (leaf 17) of the same volume shows a red-ruled table of signs from another text | cipher alphabets and sign-written examples (Ibn al-Durayhim's own chapters), printed text |
| 30092 | Bursa Inebey Genel 4808 | 13 ff., 23 lines, 13 images, undated | Image 1: title page, triangular text. Images 7-9 prose with red marks. **Images 10-11: rows of signs and numeral rows, red and black, at the head of the left page and again at the foot of the right page** (the same sign chapter as 718705). Images 12-13 prose | cipher alphabets and sign-written examples, printed text |

Both copies are the *Miftah al-kunuz* edited by Mrayati, Meer Alam and Tayyan (Damascus 1987); the sign rows are presumably the treatise's chapters on sign alphabets (not read; only seen as rows of signs). The Damascus edition's apparatus was not seen: which of the two copies it used is unchecked. This session has no text of the edition and did not compare the sign rows with it.
Not a lead for the catalogue (published treatise, nothing unread).

## Step 2: the rest of ranked_top60.tsv (spot checks; the list is noise, as the README says)

Opened on the viewer (one or two images each; thumbnails 1-25 glanced). None shows a sign run, cipher table or message in cipher.

| bib | shelfmark | title | extent | what the pages show | class |
|---|---|---|---|---|---|
| 363381 | Koprulu Haci Ahmed 00361-003 | Divan al-cifr (Bosnali Katib Hasan Efendi, 1143) | 20-59 ff., 83 images, 17 lines | Framed Ottoman Persian-style prose/verse pages (image 10), no signs | plain (cifr = divination, as the title says) |
| 263366 | Halet Efendi 00221-004 | Terceme-i fasl-i sadis 'asar fi beyan al-halateyn min Risalat Miftah al-kunuz (al-Hajj Muhyi al-Din ...) | 314-317 ff., 324-image volume, 25 lines | Ottoman Turkish prose (image 10) | plain (translation of a Sufi chapter; not the Ibn al-Durayhim title) |
| 715596 | Esad Efendi 01905 | Manhaj al-sawab fi qubh istiktab al-kuttab (catalogued under Ibn al-Durayhim) | I+70+I ff., 74 images, 17 lines | Arabic prose (image 8) | plain (about employing clerks, not cryptography) |
| 30117 | Bursa Genel 4828/2 | Rumuz al-haqa'iq (Ahmed Hamdi Yenisehirli?) | 87-102 ff., 153-image volume, 13 lines | Ottoman prose (image 6) | plain |
| 175833 | Nuruosmaniye 02688 | Rumuz al-kunuz (Abu'l-Hasan Sayf al-Din Ali b. Muhammad, copy dated 612) | 118 ff., 119 images | Arabic prose, early naskh (image 8) | plain (Kunuz al-rumuz family) |
| 178751 | Nuruosmaniye 04256 | al-Hulal al-mutarraz fi fann al-mu'amma | 250 ff., 254 images | Framed pages of riddle verse and commentary (image 10) | plain (name riddles) |

Titles of the list **not opened** (all fall in the families the README classes as noise: Qur'an-reading commentaries, Sufi rumuz/kunuz books, riddle collections): Kunuz al-rumuz
(430824, 328756, 27877, 117518, 430823, 545324, 688285, 688284, 181811, 226568, 717650, 332424, 635160, 331516), Rumuz al-kunuz (261363, 521435, 362660, 353680), Izah al-rumuz wa miftah
al-kunuz (359498, 33603, 592867, 100277, 241338, 363552), Hall al-rumuz wa mafatih al-kunuz (715247, 328697, 102089), al-Zaha'ir al-ashrafiyya fi'l-alghaz (37557, 328161, 712951),
Durr al-bihar wa kunuz al-akhyar (543583-543586, 543586), al-Ajwiba al-zakiyya (363243), Hall al-alghaz al-nahwiyya (567678), Kunuz al-ussak (705104), Kunuz al-wadi'a (355947),
Ref'u hicab al-'uyun (34099), Kasif al-rumuz (362626), al-Rumuz wa'l-amthal al-lahutiyya (175831), Kunuz al-asrar (272606), Cami' al-kunuz (29944), Cami' al-rumuz (37475),
Hilyat al-fadl (704995), al-Bulgha al-mutarjama (387821), Rumuz al-'arifin (331516), Ma'asir al-inafa (31928), Kunuz al-anwar (174074), Kunuzu'l-esrar. None has "cifr", "ta'miya" or
"mu'amma-as-cryptography" in its title; the catalogue notes do not suggest cipher either. The rest of the 60 are therefore closed on the title, not on an image.

## Step 5: records the facet counted as having images

Detail pages of **Millet Ali Emiri Muteferrik 6001 (395111), Beyazit BM11616 (574079), Esad Efendi 03817-012 (721421), Esad Efendi 01984-001 (715759), 01984-003 (715761)
and Huseyin Semsi-Fa 78-001 (248397) show no Image/Goruntu icon** when signed in (only the star, comment and quote icons), so there are no scans online for them. The facet
dkym_status=1 count includes some records with no viewable images (for 01984 and Huseyin Semsi the catalogue line is "Durr al-munazzam fi'l-sirr al-a'zam, class 133.3, numerology (cifr)", which is divination).
The portal marks printed books (Bagdat 1592 / 209748) the same way.

## Summary of findings

- **Real ciphertext on an image: none.** Cipher *keys*: Arkeoloji 01652 (Fourth Army, new, homophonic letter table plus 3-digit vocabulary). Sign alphabets and worked tables: Ibn al-Durayhim copies
  (Esad 3558-006 images 55-59; Bursa 4808 images 10-11) and Ibn Dunaynir (Fatih 5300-003 images 68, 85-86), Ibn 'Adlan (5300-004, images 94-134, shape tables at 112-119): all published treatises.
- **Ottoman pair:** 01660 is the decoded register, 01652 the key; see Step 4.
- **Corrections to the catalogue:** Fatih 5300-004 (Ibn 'Adlan) covers images 94-134, not ff. 89-119 of 31 ff.; images 135-185 are a different work ("Risalat anbab"). Esad 3558-006
  is images 50-62 with the colophon on f. 59a. Bursa Genel 4808 has 13 images.
- **Viewer behaviour:** works signed in; loads a spread in 3-6 s; thumbnails stop around image 25 for large volumes until paged; Chrome output cap unaffected for images.
- **Not done:** the other 40 of the 60 were closed on their titles; the full Kashf rumuz span in Konya 4887 was not located; 01660 was sampled (8 of 115 images), not read through; the Damascus
  edition was not compared (no text found).
