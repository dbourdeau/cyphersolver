# LJS 51: prior art, second pass (27 Nov 2026)

Follows `identity_ibn_durayhim.md` (its section 4 asked for Mrayati vol. 3) and `research/ljs51_pass/prior_art.md`.
Everything below was read in the sources named. Arabic quotations are kept short; the rest is paraphrase.
Page images of the printed books were checked where a reading depends on them (OCR of the archive.org scans is poor).

## Sources read

| Source | Where | What was used |
|---|---|---|
| Mrayati, Mir 'Alam, al-Tayyan, *'Ilm al-ta'miya wa-istikhraj al-mu'amma 'inda al-'Arab*, vol. 1 (Majma' al-Lugha al-'Arabiyya, Damascus, 1987; preface by Shakir al-Fahham) | https://archive.org/details/origins_of_ancient_arab_criptography_and_criptanalysis (file `ta3miyah1.pdf`, 420 pp.; same scan also at archive.org `BBib-Alex-03259` and `aawaam`) | biography pp. 100-104; analysis of the *Miftah* pp. 163-187; edition pp. 309-ff. Page images checked: pp. 309, 310, 311, 313, 335 |
| Same, vol. 2 (Damascus, 1997) | same item, file `ta3miyah2.pdf` (also `BBib-Alex-03260`) | contents; p. 169 (Ibn Wahb compared with the tree script) |
| Yahya Mir 'Alam, *Mu'jam a'lam al-ta'miya wa-istikhraj al-mu'amma fi l-turath al-'Arabi wa-l-Islami* (Kuwait, al-Wa'y al-Islami, 2018) | https://archive.org/details/ALM2018ARAR (djvu text) | entry no. 51 on Ibn al-Durayhim; entry no. 11 on al-Mutarjim al-Baghdadi; bibliography |
| al-Qalqashandi, *Subh al-a'sha* (Shamela 9429 = Cairo ed.) | https://raw.githubusercontent.com/OpenITI/0825AH/master/data/0821Qalqashandi/0821Qalqashandi.SubhAcsha/0821Qalqashandi.SubhAcsha.Shamela0009429-ara1.mARkdown | vol. 9, pp. 229-232 (markers PageV09P229-232) and the following pages on solving |
| al-Nuwayri, *Nihayat al-arab* (OpenITI JK009238) | https://raw.githubusercontent.com/OpenITI/0750AH/master/data/0733Nuwayri/0733Nuwayri.NihayatArab/0733Nuwayri.NihayatArab.JK009238-ara1 | term search only |
| Ibn Wahshiyya (attrib.), *Shawq al-mustaham fi ma'rifat rumuz al-aqlam*, ed. and tr. J. Hammer, *Ancient Alphabets and Hieroglyphic Characters Explained* (London, 1806) | https://archive.org/details/ancientalphabets00ibnw (PDF and djvu text) | Arabic p. 38 (plate, image checked); English pp. [8] and the translator's preface |
| OPenn LJS 51 record | https://openn.library.upenn.edu/Data/0001/html/ljs51.html | full record |
| Internet Archive copy of LJS 51 | https://archive.org/details/ljs51 | description (date given as 1400) |
| Penn facsimile (D. Porter, 2015) | https://repository.upenn.edu/handle/20.500.14332/46351 (read through the DSpace API, `/server/api/core/items/7f9310b7-dff2-485b-9630-c83f9ce19ec6`) | metadata |
| Schoenberg Database of Manuscripts, manuscript SDBM_MS_15170 | https://sdbm.library.upenn.edu/manuscripts/15170; entries 55241 (Christie's 1996), 196171 (*Transformation of Knowledge*, 2006), 252191 (OPenn) | entry fields (JSON) |

## (1) Mrayati, Mir 'Alam and al-Tayyan

Only the Arabic series was reachable. The English *Arabic Origins of Cryptology* vol. 3 (KFCRIS/KACST) was not:
pdfcoffee returns 403 to scripts, and in Chrome it showed a bot check and then a 503 (no CAPTCHA was touched).
The Arabic vol. 1 (1987) is the edition the English vol. 3 translates: vol. 1 contains al-Kindi, Ibn 'Adlan and Ibn
al-Durayhim. Mir 'Alam (2018, entry 51) says the English translation of the *Miftah* is vol. 3 of the English series.

### Biography (vol. 1, ch. 3, pp. 100-104)

'Ali b. Muhammad b. 'Abd al-'Aziz, Taj al-Din, known as Ibn al-Durayhim. Born in Mosul in Sha'ban 712, grew up
there an orphan with wealth. Studied with many scholars. Travelled as a merchant between Damascus and Cairo more than once.
Was appointed teacher at the Umayyad Mosque. Went to Egypt (the year is garbled in the OCR; Mir 'Alam 2018 has 760). Sultan
al-Malik al-Nasir sent him as envoy to the king of Abyssinia. He went unwillingly, reached Qus and died there in Safar 762.
Fields: fiqh, hadith, usul, readings, tafsir, arithmetic, riddles, solving ciphers, magic squares, the properties of letters.
Main source cited: Safadi, *A'yan al-'asr* (a photocopy of a Damascus manuscript, ff. 94b-95b), with *al-Durar al-kamina*,
*al-Badr al-tali'*, *Kashf al-zunun*, *Hadiyyat al-'arifin*, *al-A'lam*, *Mu'jam al-mu'allifin* and Brockelmann, *GAL* S II 213.
The editors note that Safadi lists about eighty of his works, copied from his own hand. They print 19 that touch the
occult sciences and ciphers. The cipher titles are: *Idah al-mubham fi hall al-mutarjam* (named in the *Miftah*
preface; *al-Mubham* in the *Durar* and *Hadiyya*); *Mukhtasar al-Mubham*; *Qasida fi hall rumuz al-aqlam al-maktuba
'ala l-barabi*; *Miftah al-kunuz fi idah al-marmuz*; *Nazm li-qawa'id fann al-mutarjam wa-dawabitihi* (a verse rule-book,
named in the *Miftah* preface). No *Ajwiba* title, no collection of letters and no book of solved ciphers is in the
editors' list. Mir 'Alam (2018) repeats the biography (death "762 or 766") and quotes Safadi's account at length.
That account includes the three verses on Ibn Dunaynir and Ibn al-Durayhim, already used in `identity_ibn_durayhim.md`.

### The edited treatise (vol. 1, part 3, pp. 309-ff.)

- **Title.** The editors print *Miftah al-kunuz fi idah al-marmuz*. Their note on p. 309: that is the title in the author's
  preface (MS f. 47b) and in *Kashf al-zunun* (p. 1770). The contents leaf of the codex and Safadi's *A'yan al-'asr* (f. 95b)
  have «مفتاح الكنوز في حل الرموز». *Hadiyyat al-'arifin* (2:723) and *Mu'jam al-mu'allifin* (4:210) have "fi idah al-rumuz".
  The *Durar*, *Badr*, *A'lam* and Brockelmann do not list it. So "fi hall al-rumuz" is attested, by Safadi and by the
  manuscript's own contents leaf. LJS 51's "fi hall al-marmuz" (f. 102v) is not attested, but it sits exactly between
  the two forms.
- **Manuscript.** One copy only: Istanbul, Süleymaniye Library, Esad Efendi 3558. It is a small-format collection of occult
  treatises (zairja, jafr, magic squares, geomancy, talismans), in good naskh. The *Miftah* fills ff. 47b-59a and is
  complete. Copied by Sidqi Mustafa b. Salih, Friday 10 Ramadan 1149 (pp. 309-310, image checked). The editors found it
  in 1981 (vol. 1, p. 105 note).
  Facsimiles of the contents leaf and of the first page are on pp. 311-312. **P. 313 reproduces the manuscript page that
  carries the tree script.** The last page is reproduced after p. 316.
- **The author's preface.** He had written *Idah al-mubham fi hall al-mutarjam*, then an abridgement, and had no copy
  of it with him. On request he versified what he remembered and added this commentary, the *Miftah* (p. 321).
- **Kinds of encipherment.** The text introduces them with «أنا ذاكر منها أصولا وقواعد». The first section ends «وهو من
  باب المقلوب», and the paragraph closes «بل من باب المقلوب» (pp. 324-326). So **al-maqlub is the author's own term**. It
  covers reversing a word, letter swaps within a word or between neighbouring words, and take-one-skip-n reorderings: all
  transposition, with no letter added or changed. The headings of the following sections are the editors' (in square
  brackets). The text itself calls substitution «إبدال» throughout, from «ومنهم من يصطلح على إبدال حرف بحرف» on. The
  editors' analysis (p. 163) sorts the kinds into eight classes: (1) **al-maqlub**, transposition;
  (2) **al-ibdal**, substitution, divided into "unregulated" (fixed pairings such as the qalam qummi, a verse key such
  as قد ضج زح..., the Pahlavi pen) and "regulated" (shifts in abjad, Maghribi abjad or alphabetical order, single or in
  pairs, 28 or 58 keys each); (3) adding or dropping letters; (4) devices (chessboard, a board with 28 holes and a thread,
  beads); (5) abjad numbers for letters; (6) letters hidden in words, including spelling letters out, nulls, and
  acrostic and grille-like schemes; (7) letters as names of genera (*dhu ribat wa-sharh*); (8) invented shapes. The
  editors say Ibn al-Durayhim's value lies more in listing and analysing methods than in solving.
- So the order of the first two chapters, maqlub then ibdal, is the treatise's own. LJS 51 f. 102v names "the chapter
  of al-maqlub" in "my book *Miftah al-kunuz*" and expects it to be taken for "al-ibdal". That matches the edited text.

### The tree script in the *Miftah* (vol. 1, p. 335; analysis p. 185; manuscript page p. 313)

At the end of the class of letters replaced by words or pictures (things drawn, such as birds, animals, plants or trees),
the text goes on: «وينبغي هنا أن نذكر القلم المشجر، وهو مبني على كلمات (ابجد)». Paraphrase of the rest, read from
the printed page image: draw a stroke. If the letter's abjad word is the first word, make one branch on the right; for
the second word two, and so on up to the eighth. If the letter is the first of its word, make one branch on the left; if
the second, two, and so on up to the fourth, since no abjad word has more than four letters. The example is
"محمد ابن عم علي", drawn as 12 trees. The editors' note: the copyist swapped the shapes of alif and dal. In the printed
figure alif is a simple Y fork (one branch each side).

This is the LJS 51 f. 63v system as decoded in `keys_eye/63v.trees.json`: right-side branches give the word (1-8),
left-side branches give the place in the word (1-4), and alif = 1 + 1. The sides agree too. Checked in the printed
figure on p. 335: the first م has 4 branches on the right (word 4, كلمن) and 3 on the left (place 3).

The *Miftah* sets out the abjad order in the same chapter. Its Eastern order is أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ.
It warns that Maghribi correspondents use «صعفض ... ظغش». That is relevant to the ص = 1/5 anomaly on 63v (mixed order),
but the treatise does not describe such a mixed order.

The editors (p. 185) call the tree script one of the curiosities of the treatise. They say Ibn al-Durayhim alone mentions
it, among the treatise authors they studied: al-Kindi, Ibn 'Adlan, and in vol. 2 Ibn Tabataba, Ibn Wahb, the *Adab
al-shu'ara'* extract, Ibn Dunaynir and al-Jurhumi. In vol. 2 (p. 169) they compare Ibn Wahb's method with it. Ibn Wahb
encodes each letter by its place in a pangram key verse, as "the first of the sixth word" and so on. The editors note
that the *mushajjar* uses the abjad words instead of a verse, and drawing instead of writing.

### What the series does not have

No mention in vols. 1-2, or in Mir 'Alam's *Mu'jam* (2018, with a full bibliography), of LJS 51, Penn or Schoenberg.
Nor of any book of Ibn al-Durayhim's solved verses or correspondence, or of al-'Ala'i / Ibn Fadl Allah as his patron.
The *Mu'jam* has an entry on Ahmad b. 'Abd Allah, Shihab al-Din al-Baghdadi al-Mutarjim (no. 11, after Safadi, *Wafi*
7:95-96), but it does not tie him to Ibn al-Durayhim. The *Mu'jam* bibliography lists an edition by M. H. al-Tayyan,
"Qasidat Ibn al-Durayhim fi hall rumuz al-mukatabat (al-nass al-muhaqqaq)", *Majallat Ma'had al-Makhtutat al-'Arabiyya*
56/2 (Nov. 2012), and al-Tayyan, "Ibn al-Durayhim wa-juhuduhu fi 'ilm al-ta'miya", *Majallat al-Bayan* (Sept. 2000).
**Not read.** The 2012 poem on solving the ciphers of correspondence is the closest known text to LJS 51's subject.

## (2) Penn and Schoenberg descriptions

- **OPenn / Penn catalogue / archive.org / facsimile (Porter 2015).** The same text in each: "Collection of encrypted
  correspondence between the compiler and various correspondents, in approximately 150 alphabets, accompanied by
  transcriptions of the letters in Arabic". The compiler cites Shihab al-Din al-Jindi al-'Ala'i, Burhan al-Din al-Qudsi
  and Taqi al-Din Muhammad ibn Ja'far al-Husayni as authorities for some alphabets. The manuscript lacks its beginning and
  end. Origin "Possibly written in Syria, in the 15th century"; date "14--" (archive.org: 1400). 106 leaves, 13 lines,
  naskh. Provenance: Christie's 1996; Sam Fogg to L. J. Schoenberg, June 1996; gift to Penn 2015.
  No compiler is named, no text identified, and Ibn al-Durayhim is not mentioned.
- **SDBM_MS_15170** has three entries. Christie's 1996 (entry 55241): title "Alphabets and Encoded Letters", Syria,
  c. 1450, 106 ff. *Transformation of Knowledge* 2006 (entry 196171): no. "51", title "Alphabets and Encoded Letters",
  "xv cent", Syria, half-leather binding. OPenn 2018 (entry 252191). None names an author.
- ***Transformation of Knowledge* (2006), p. 43**: the text itself was not reachable. It is not in Google Books full text
  (Google Books search in Chrome found nothing; the API quota was exhausted), not on archive.org, and not on HathiTrust
  (not tried, being a 2006 in-copyright book). Its SDBM digest gives only title, date and place, as above. The Christie's
  1996 and Sam Fogg 1996 catalogues were not found online.

## (3) The tree system elsewhere

- **al-Qalqashandi, *Subh* 9:229-232.** He condenses Ibn al-Durayhim's kinds of encipherment by name (the 17-letter
  Mongol script, the qalam qummi, reversal, swapping, abjad numbers, names of men, lunar mansions, countries, fruits,
  trees, "pictures of birds and other animals"), then invented shapes. **He leaves out the qalam mushajjar.** No
  occurrence of مشجر in a cipher context in the whole OpenITI text. Mrayati's edition footnotes confirm that Qalqashandi
  copies the *Miftah* here.
- **al-Nuwayri, *Nihayat al-arab*.** No مشجر in a cipher sense and no description of this system (term search of the
  OpenITI text; the cipher terms occur only 3 times).
- **Ibn Wahshiyya (attrib.), *Shawq al-mustaham*, Hammer 1806, Arabic p. 38** (book 4, section 16): "the script of the
  sage Dioscorides, «وهو المشجر»". He is said to have written his book of herbs and plants, their properties, uses,
  harms and secrets in it, and later sages used it in their books. The plate gives 28 tree signs in abjad order. Alif is
  a Y fork, and the next signs add branches on one side as the letter moves along its abjad word. So it looks like the
  same branch-count system, but the 1806 print is too small to check every sign. No rule is stated in the text. Hammer's
  English (p. [8], section XVI) calls it "commonly called the Tree alphabet". In his preface he calls it the commonest of
  the book's alphabets, still used by Turks, Arabs and Persians as a secret cipher. The date of the *Shawq* is uncertain;
  Mrayati vol. 1 (pp. 52-53) treats it as Ibn Wahshiyya's, d. 296.
- **Ibn 'Adlan, Ibn Dunaynir.** The editors' statement (vol. 1, p. 185) and the vol. 2 contents show the device is not in
  their treatises. Not checked line by line here.
- **Persian.** Malkam Khan's *Meftah al-romuz* (1902) names a *qalam-e mushajjar* (Encyclopaedia Iranica, already in
  `research/ljs51_pass/prior_art.md`); not re-checked.
- **Not read:** C. E. Bosworth, "The section on codes and their decipherment in Qalqashandi's *Subh al-a'sha*", *JSS* 8
  (1963) 17-33; I. A. Al-Kadi, "Origins of cryptology: the Arab contributions", *Cryptologia* 16 (1992) 97-126; the English
  *Arabic Origins of Cryptology* vols. 1-6. Since Qalqashandi omits the tree script, Bosworth is unlikely to describe it
  (not checked).

**Answer to the question.** Yes: a tree script whose branch counts give the abjad word on one side and the place within
it on the other is described in print. Ibn al-Durayhim's *Miftah al-kunuz fi idah al-marmuz* describes it explicitly
(Mrayati et al., vol. 1, 1987, p. 335, with a worked example). The same right-word / left-place convention is used in
LJS 51 f. 63v. A tree alphabet called al-mushajjar, in abjad order, is also drawn without a rule in the *Shawq
al-mustaham* (Hammer 1806, p. 38), so the script was not Ibn al-Durayhim's alone.

## Bearing on the questions

(a) **Ibn al-Durayhim identification: strengthened.**
- The *Miftah*'s own text calls its first kind of encipherment "bab al-maqlub" and follows it with substitution (ibdal),
  as f. 102v assumes.
- The title form "fi hall al-rumuz" is attested twice (Safadi; the contents leaf of Esad Efendi 3558), close to LJS 51's
  "fi hall al-marmuz".
- The rare tree script of f. 63v is the one the *Miftah* describes, down to which side counts what. Among the cryptology
  treatises the Damascus editors studied, only Ibn al-Durayhim's describes it.

The tree script is not proof by itself, since the *Shawq* also has a tree alphabet. The *Miftah* survives only in an 1149 AH
copy, and nothing in the series says Ibn al-Durayhim compiled a book of solved verses.

(b) **Is LJS 51 or its tree script already known?**
- LJS 51 as such: no sign in the Penn/Schoenberg records (no author or text identified), Mrayati vols. 1-2, Mir 'Alam 2018,
  or Qalqashandi. The 2006 catalogue text and the Christie's/Fogg descriptions were not seen.
- The tree system: the method is published (the *Miftah*, ed. 1987), and Hammer printed a tree alphabet in 1806. Its use
  in LJS 51 and the decipherment of f. 63v are not reported in anything read.

## Not reached

- English *Arabic Origins of Cryptology* vol. 3 (pdfcoffee: 403, then a bot check and 503 in Chrome).
- *Transformation of Knowledge* (2006) p. 43.
- The Christie's 1996 and Sam Fogg 1996 catalogues.
- al-Tayyan 2012 (the poem on solving correspondence ciphers) and 2000.
- Bosworth 1963 and Al-Kadi 1992.
- Mrayati's Arabic vol. 3 (Ibn 'Adlan's *al-Mu'allam*?); the archive.org description says it was in preparation.
