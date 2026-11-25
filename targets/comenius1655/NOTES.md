# Comenius to Andreas Klobusiczky, cipher passages of 1655 (Unsolved Catalogue no. 474)

Status: written up 27 Oct 2026 (docs/comenius1655.html). 4 Aug 1655 sentence read from the existing decipherment
(Szilágyi 1890, Patera 1892), key rebuilt and identified with the printed Rákóczi table (MHH XXIII p. 740); 24 May 1655
passage attempted, not deciphered. Contributed by WAINUT (https://github.com/WAINUTAI), PR #102, 27 Oct 2026; review
pass by Claude for Daniel Bourdeau the same day (section "Review, 27 Oct 2026" below, which corrects parts of what
follows).

**In short (WAINUT's report; see the review for corrections).** The cipher sentence of 4 Aug 1655 was deciphered in print in 1892, in a footnote of Adolf Patera's
edition of Comenius's letters: "Poloniam periisse et papatum in illa". We transcribed it from both printed editions,
rebuilt the key from Patera's plaintext and checked it letter by letter. One letter does not fit (see below). The
cipher passage of 24 May 1655 is not deciphered: neither edition gives a decipherment, and our attempts gave no Latin.
The catalogue's "four letters, each with a ciphered sentence" needs refining. The 22 Jul letter puts its secret
text on a further page in invisible ink, which is not printed. The 6 Sept letter has passages in secret script, which
Patera prints already in clear, in italic (p. 183, note *). Its ciphertext is not printed. We also noted one short
cipher word, "(iyy)", in the body of the 4 Aug letter. It is not deciphered.

## The documents

Jan Amos Komenský (Comenius), then at Leszno in Great Poland, to Andreas Klobusiczky, councillor of Prince
George II Rákóczi of Transylvania. The originals are in the Hungarian National Archives, MNL OL (Budapest), E 190
Archivum familiae Rákóczi (the former Kamarai levéltár). They were not seen. EMLO gives the folios (5.t. 788
ff. 389-390v; 6962 ff. 351-354v; 5.t. 800 ff. 414-415v).

Two printed witnesses, both on archive.org, both read on the page images:

- Szilágyi (ed.), *Okmánytár II. Rákóczy György diplomacziai összeköttetéseihez*, Monumenta Hungariae Historica,
  Diplomataria XXIII (Budapest 1874), archive.org `okmnytriirkczyg01gygoog`. It prints the letters "from the original
  in the Hungarian Chamber Archive". It gives the ciphers without a decipherment.
- Adolf Patera (ed.), *Jana Amosa Komenského korrespondence* (Praha 1892), archive.org `bub_gb_xnVMAAAAYAAJ`.
  His notes say both letters were first printed in MHH XXIII.

| letter | Patera 1892 | MHH XXIII 1874 | secret text | state |
|---|---|---|---|---|
| 20 May 1655 | CLI, pp. 177-178 ([leaf n199](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n199)) | | none; refers to the "Schaumiana" read "ex pacto" | context only |
| **24 May 1655** | **CLII, p. 178** ([leaf n200](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n200)) | **no. CIII, pp. 178-179** ([leaf n194](https://archive.org/details/okmnytriirkczyg01gygoog/page/n194)) | **letter cipher, 50 letters and 3 numbers** | **not deciphered** |
| 22 Jul 1655 | CLIII, pp. 179-180 ([leaf n202](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n202)) | | invisible ink on a further page: "Addo occultiora pagina sequenti, carbo ostendet" | not printed |
| **4 Aug 1655** | **CLIV, ends p. 182** ([leaf n204](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n204)) | **no. CXXIX, pp. 217-219** ([leaf n235](https://archive.org/details/okmnytriirkczyg01gygoog/page/n235)) | **one cipher sentence, and the word (iyy)** | **sentence deciphered by Patera 1892; (iyy) open** |
| 6 Sept 1655 | CLV, pp. 182-183 ([leaf n204-n205](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n205)) | | secret script in the original, printed in clear in italic (note * p. 183); "Occulta scriptura nihil scribo hac vice" | plaintext printed by Patera 1892; ciphertext not printed |

Patera's footnote on p. 182 says the 6 Sept letter is also printed in Szilágyi, *Transsylvania et bellum
boreo-orientale* I (1890) pp. 393-394. That volume was not checked.

## 4 Aug 1655 (document A): Patera's decipherment, checked

**Transcription** (`ct_1655-08-04.txt`). The sentence stands after "4 Aug. 55. Tuus totus" (no signature) and before
the address "Generosissimo Viro Domino Andreae de Klobusitz". It is the same in both prints:

    Nihil certius quam Cyhyqbma cgzbbttg, et CmCasda 69 655 m.

The archive.org OCR of Patera has "(>i) (555" for the digits. The page images have "69 655".

**Patera's footnote** (p. 182, note *): "Značí: Poloniam periisse et papatum in illa." ("It means: ...").
Patera does not say who made the decipherment. MHH gives none.

**Key** (`key_1655-08-04.tsv`, rebuilt by `check.py`). Plain to cipher: a=m, e=g, i=b or 6, l=h or 5, m=a, n=q or 9,
o=y, p=c (also C), r=z, s=t, t=s, u=d. "et" is written in clear. It is a letter substitution with digits as extra
signs (homophones) for i, l and n. The pairs a/m and s/t occur in both directions, so the table may be reciprocal
(am, bi, cp, du, eg, hl, nq, oy, rz, st). This is a guess and is not used.

**Decryption, line by line** (`plain_1655-08-04.txt`):

| cipher | plain |
|---|---|
| Cyhyqbma | poloniam |
| cgzbbttg | periisse |
| et | et (clear) |
| CmCasda | p a p **m** t u m, read papatum |
| 69 | in |
| 655 m | illa |

**One conflict.** The fourth letter of "CmCasda" is "a". Everywhere else cipher a is plain m, so the strict
decryption is "papmtum". Patera reads "papatum", which is the only sensible word. Both prints clearly have "a" (checked
on the zoomed images). So either the writer put a plain "a" there, or this is a slip in the original or in both
prints. It does not change the reading.

**Controls** (`check.py`, seed 1). A shuffled key gives "ltptnman lremmuur et lalnion is illa". The correct key on
letters shuffled inside each word gives "nolmioap rispeesi et pmautmp in lali". Both are gibberish.

**Reading** (`reading_1655-08-04.txt`):

> Nihil certius quam Poloniam periisse, et papatum in illa.

**English** (`translation_1655-08-04.txt`): "Nothing is more certain than that Poland has perished, and the papacy in
it."

**Context.** The letter reports the Swedish advance from Poznań on Warsaw in the summer of 1655, the flight of the
Catholic clergy and the seizure of their goods, and the Swedes fortifying Poznań and Kalisz "to subdue and keep"
Poland. The cipher hides the one sentence that draws the conclusion. (At this time Comenius was pressing Rákóczi to
side with Sweden; that is background, not taken from this letter.)

**The word (iyy).** Near the end of the same letter: "Mire angitur bonus vir (iyy) de tantis sibi injectis remoris"
("The good man (iyy) is wonderfully troubled by the great delays put in his way"). MHH prints "iyy" in italic, as it
prints the cipher of 24 May (MHH sets the 4 Aug sentence itself in roman). Patera prints it in roman type. The 4 Aug key gives "?oo" (with the reciprocal guess,
"boo"), which is not Latin. It may be a code name for the "good man", perhaps Schaum, who is named just before. It
stays open [?].

## 24 May 1655 (document B): not deciphered

**Transcription** (`ct_1655-05-24.txt`). Comenius quotes news from a friend's letter from England dated 23 Apr 1655
(Polish and Swedish envoys in London, the Waldensians, the fleet in America). The cipher follows this news. It is not
the end of the letter: on p. 179 ([leaf n201](https://archive.org/details/bub_gb_xnVMAAAAYAAJ/page/n201)) come a P.S.,
"Tandem apulit [...] dominus Schaum" ("Schaum has at last landed"), which
answers the friend's "nondum his oris apparet" and so seems to belong to the English letter, then Comenius's own news
and the closing "Raptissime 24 Maji 1655". So the cipher may stand inside the quoted English letter. That is an
inference from the layout of the print. Both prints set the cipher in italic. [ſ/f?] marks the long-s glyph, which the italic does not separate
from f.

    Patera 1892: Lmqſxmyo. 7. Gpdlmuoyqnotlses: Pnofeyprp 865, ap 73 pyſ: pdyp: Xyopatus etc. etc.
    MHH 1874:    Lmqſxmyo.7. Gpdlmuoyqnotlses : Pnofeyprp 865, ap 73 pyſ: pdyp : Xyoapus. etc. etc.

The last word differs: "Xyopatus" (Patera), "Xyoapus" (MHH). Only the original can settle it. The archive.org OCR
of MHH has "Gpdlmnoyq'nothes"; the page has "Gpdlmuoyqnotlses". 50 letters, 17 distinct; numbers 7, 865, 73; word
lengths 8 / 16 / 9 / 2 / 3 / 4 / 8 (or 7). "pdyp" has the pattern ABCA.

**What was tried** (`check.py`, `anneal.py`, `plain_1655-05-24.txt`):

- The 4 Aug key, its inverse, and its pairs read as a reciprocal table: no Latin ("?ant?ao? ? e?u?a??on??s?t?t ...").
- The 4 Aug pairs combined with Caesar shifts on 22-, 23-, 24- and 26-letter alphabets: nothing.
- Caesar, affine and progressive shifts; Vigenère, Beaufort (both forms) and Porta with about 10,000 Latin keywords
  from Patera's Latin text, plus names (Schaum, Comenius, Rakoczi ...): nothing. These were run with research scripts
  that are not part of this folder.
- Annealing of a one-to-one letter substitution, with word division kept, scored by Latin 4-grams and a word bonus
  from `lang/lexicons/la.json.gz` (`anneal.py`). **Matched control:** the same annealer recovers two synthetic Latin
  texts of 56 and 50 letters exactly ("gallia est omnis diuisa in partes tres ...", "omnia uincit amor et nos cedamus
  amori ..."). On the 24 May passage it finds only nonsense, for example "empclman stheminapondecrc tongratyt ut tac
  that lantudic".

So the passage is not a simple substitution of Latin with this word division. It may use another key, contain names,
numbers or abbreviations, or be in another language. The layout ("... : ... 865, ap 73 ... : ... : ... etc. etc.")
looks like a list or a citation. In the 6 Sept letter Comenius cites Drabík's revelations by number and date, so
this could be something similar. That is a guess.

**A different key.** The 20 May letter says the April letters could not be read and should be read "eo modo, quo
Schaumiana legi necesse est ex pacto" (in the way the Schaum papers must be read, as agreed). This may refer to the
agreed invisible-ink method rather than to a letter cipher. MHH XXIII also has another writer's line "Haec Comenius
incognita scriptura" (about a later letter of his from Amsterdam), which fits invisible ink as one of Comenius's secret channels. If the
cipher does stand inside the English letter, its key may be the English correspondent's rather than Comenius's. A key
for the 24 May passage was not found.

## 22 Jul and 6 Sept 1655: secret text, but no ciphertext in print

Checked on the page images of Patera.

- **22 Jul (CLIII, p. 180).** The letter ends: "A Constantino Schaum habui vetustas ad Gen. Vestram *et ad principem*,
  sed *non mitto ob securitatem*. ... Addo *occultiora pagina sequenti, carbo ostendet*." The phrases in italic are as
  printed. Patera adds no note on them here. The "more secret things on the following page", to be shown with
  charcoal, are invisible ink. That page is not printed.
- **6 Sept (CLV, p. 183).** Patera's note * says: "Co ležatým písmem vytištěno, psáno v originále tajným písmem"
  ("What is printed in italic was written in secret script in the original"). The italic words are, in order: *Quid
  princeps agat*; *legatus Svecicus*; *Anglius promissus*; *et credatis Drabiciana?*; *principissae*; *Racocianam
  domum*; *excitet*; *Septentrionales, praedictum*; *perterreno perdere incipere illos*; *perdunt terram, Vestrum*;
  *Bisterfeldius*; *ab ira Dei*; *septentrionalibus jungi*; *Turcae*; *durities Vestra*; *gentium fidelium*; and, after
  the signature, *Occulta scriptura* (in "Occulta scriptura nihil scribo hac vice"). They sit in a numbered list of
  questions that cites Drabík's revelations by date. So the 6 Sept letter does contain secret text, and it is already
  printed in clear. The ciphertext, the key and the name of the decipherer are not given. This letter is also printed in
  Szilágyi, *Transsylvania* I (1890) pp. 393-394 (Patera's note ** p. 182), which was not checked. Whether "occulta
  scriptura" (here probably invisible ink) and the italic secret script are two different channels is open.

The first version of this folder said the 6 Sept letter had no secret text. That was wrong. It was based on the OCR,
which loses the italics.

## Prior art

- Patera 1892, p. 182, footnote: the decipherment of the 4 Aug sentence. This is the earlier solution.
- Patera 1892, p. 183: the secret passages of 6 Sept printed in clear, in italic (note *). The decipherer is not named.
- MHH XXIII (Szilágyi 1874), pp. 178-179 and 217-219: ciphertext only.
- EMLO (Comenius catalogue) marks the letters "Contains ciphered sentence" and notes no decipherment.
- Szilágyi, *Transsylvania et bellum boreo-orientale* I (1890), pp. 388-394: prints CLI, CLIII and CLV; not checked.
- The critical edition (*Dílo Jana Amose Komenského*, vol. 26, Academia) has reached 1641 (vol. 26/II, 2024), so the
  1655 letters are not yet edited there. Blekastad, *Comenius* (1969), was not checked. A web search found nothing on
  these ciphers.

## Review, 27 Oct 2026

A review pass (Claude Opus 5.5, for Daniel Bourdeau) on the five review items and the escalation steps. Downloads in
the session scratchpad, not in the repository.

**1. The key is printed: MHH XXIII (1874) p. 740.** At the end of Szilágyi's *Okmánytár* (archive.org
`okmnytriirkczyg01gygoog`, leaf n724), after the glossary: "A Harsányi és Balogh Máté által használt titkos írás
kulcsa" (the key of the secret script used by Harsányi and Máté Balogh, Rákóczi's envoys at the Porte):

    a=m  b=i  c=p  d=u,f  e=g  f=v  g=e  h=l  i=b  k=x  l=h  m=a  n=q  o=y  p=c  q=n  r=z  s=t  t=s  u=d,f  x=k  y=o  z=r  v,w=f

It is a reciprocal table (pairs am, bi, cp, du, eg, fv, hl, kx, nq, oy, rz, st). All 12 letter values rebuilt from
the 4 Aug crib agree with it (`python check.py`, "12 of 12"), so WAINUT's "reciprocal, a guess" is confirmed by print,
and Comenius was writing in the Rákóczi court's own table. The printed table has no digits.

**2. The digits.** 6=i, 9=n, 5=l are not in the printed table. In the table i, n, l are b, q, h, and a handwritten
b, q and h are easily taken for 6, 9 and 5. So "69 655m" is very probably "bq bhhm" misread by the printer: the
system would then be the plain reciprocal table with no digit homophones. A hypothesis (both prints have the digits;
Patera's text of these letters follows MHH, so one misreading would carry over); only the original can settle it.

**3. The conflict, re-checked.** `python check.py` gives "poloniam periisse et papmtum in illa": the fourth letter of
CmCasda is cipher a, which the rebuilt key and the printed table both make plain m. Patera and Szilágyi read papatum.
Both prints have "a" (page images re-checked). Either the writer put the plain a by slip or the printers misread an m
(cipher m = plain a) in the original. Reading kept as papatum; the decoder output is shown on the page with that
letter marked uncertain.

**4. An earlier printed decipherment: Szilágyi 1890.** Szilágyi, *Erdély és az északkeleti háború* I (= *Transsylvania
et bellum boreo-orientale*, Budapest 1890; archive.org `erdlysazsz01sziluoft`), section "Comenius jelentései",
pp. 388-394. P. 393 (leaf n404), letter d), 4 Aug 1655: "Jegyzet. A titkos jegyekkel írt utóírás így hangzik:
«nihil certius, quam Poloniam periisse, et papatum in illa." ("Note. The postscript written in secret signs reads:
...") with a reference to Okmánytár 217. This is two years before Patera, who prints the same plaintext. Neither
names the decipherer; Szilágyi, who had printed the Harsányi/Balogh table in 1874, could have applied it himself.

**5. The 22 Jul letter, its invisible ink, is partly printed.** Szilágyi 1890 p. 392 (leaf n403), letter c): the
italic phrases are secret script ("A dűlt betűkkel szedettek rejtelmesek", the words in italic were secret), i.e.
*et ad principem*, *non mitto ob securitatem*, *occultiora pagina sequenti, carbo ostendet*; and then: "On the next
page, written in a very rubbed, dissolved charcoal script, and brought out with heat, in secret writing, stand the
following:" "Londino 4. Junii Constantinus Schaum. Non satis dici potest, quam grata fuerit protectori notitia mea,
coram omnibus senatoribus dixit (in audentia) sub dirigente regimine suo nullum nuncium ab ullo regum prosperum
accepisse, quam a celsitudine sua. In ultima audentia secreta (in qua praeter (?) interpretem meum dominum etiam
secretarium status .... adfuit) zelum suum pro gloria dei, ut mihi lacrymis asseruisset ...". The rest, about 25
lines including a report of 25 June, was washed out; the note says it was copied from the third page of the letter,
written in chemical ink, three quarters of the page, made legible by holding it to the fire, and that no more could
be made out. So the invisible ink was read in the archive in the 19th century; what is left is illegible.

**6. The 6 Sept letter.** Szilágyi 1890 pp. 393-394, letter e): the same italic passages, with the same note
("rejtelmesek"), and a note that the Drabík revelations cited are in *Lux in tenebris* (1657). Plaintext only, as in
Patera. Szilágyi also identifies the 24 May letter as Comenius's (p. 390: "Comenius jelentése Schaum küldetéséről.
Közölve de aláírás nélkül, Okmánytár 178. l."), which MHH had printed as by "the Rákóczis' Polish correspondent"
("Irta a Rákócziak lengyel levelezője", MHH note to no. CIII). No decipherment of 24 May in either.

**7. Siblings.** Patera's register gives Klobusický at pp. 174, 178, 179, 181-183, 219: CXLVIII (1654 memorandum,
Czech), CLI-CLV (1655), and a mention on p. 219. CLVI (to Schaum, 31 Jan 1656, MHH no. CLXXVII) has no cipher
passage in Patera's text. MHH XXIII also has "A Domino Comenio literas [2]8. Januarii Amsterodami ... Comenius incognita
scriptura" (archive.org leaf n616), invisible ink again, not a letter cipher. No further letter-cipher passage of
Comenius was found in the two editions.

**8. The 24 May passage, pushed.**
- Printed table (MHH p. 740) on 24 May: "hantkaoy ? ecuhadyonqyshtgt cqyvgoczc ??? mc ?? cot cuoc koycmsdt". Not Latin.
  The digits read as letters (8 ?, 6=b=i, 5=h=l) give "865" = "?il", which would fit *nil*; but the letter words do
  not read, so it is not this table.
- Printed table combined with Caesar shifts on 23-, 25- and 26-letter alphabets, both orders, scored with the shared
  `la`, `en-modern`, `de-modern`, `hu-modern` and `pl-modern` models (order 4): best -4.9 per character, against -1.7
  for Patera's 4 Aug plaintext. Nothing.
- `anneal_lm.py` (new, uses the shared Latin model `la` from lang/, 5-grams with spaces, plus the word bonus):
  one-to-one substitution: the matched control (56 letters, 17 signs) is recovered exactly ("gallia est omnis diuisa
  ..."); the 24 May passage gives only nonsense at -3.1 to -3.5 per character ("opbmspai xenophiablitomum eliquaere de
  eam enae saiedthm"). Homophonic, letters and digits as signs (the system of 4 Aug as printed): the matched control (66
  signs, 23 distinct) is not recovered even with 60 restarts x 20,000 steps (best "nihil canuiue quam coloniam
  coniicco ..."), so on 56 signs this search is underdetermined and its 24 May optima ("icrescen e aspicanerentiere
  ...") mean nothing either way.
- Language: the letter around it is Latin, the 4 Aug cipher is Latin, and the passage stands inside news quoted from
  an English correspondent; no language is established for the cipher itself. Profile: documents B "unknown", and
  the text entry no longer says "la".

**Outcome.** The 4 Aug sentence: read from existing decipherment (Szilágyi 1890 p. 393; Patera 1892 p. 182), key
rebuilt from it and identified with the printed MHH XXIII p. 740 table, one letter in conflict. The 24 May passage:
attempted, not deciphered. Written up as "read from existing decipherment", extent partial.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher only. Document A, 4 Aug 1655:

- Old 0.95 -> new **0.833** (5 of 6 cipher words). **Read -> read in part** for document A. The recorded 0.95 was
  19 of 20 words of the whole letter passage with the clear text around the cipher (whole letter, clear included, not
  the measure).
- Separation: the cipher is the sentence after the signature, where `ct_1655-08-04.txt` shows "Nihil certius quam" and
  "et" in clear and the rest in cipher (Cyhyqbma cgzbbttg, CmCasda, 69, 655 m), plus the word (iyy) of the second
  sentence. The five words of the first sentence are read (Poloniam periisse papatum in illa); (iyy) is the one hole.
  The reading file now marks the cipher words in bold (`cipher_markup: **` in profile.json); this is a change of
  markup only, not of the reading. If papatum is also counted as not sure (the key gives papmtum at one letter), the
  figure is 4 of 6 (0.667).
  Counting the clear-Latin word (iyy) as a cipher word is itself a judgement call: with it, 5 of 6 (0.833); without it,
  the five words of the sentence are all read, 1.0 of five.
- Part A's extent in profile.json goes from complete to partial (5 of 6 cipher words, under the bar). Document B (24 May) is not read. The class (already solved, partial), fraction_read (29 of 88 cipher letters, a
  share of letters) and the page's statements are unchanged: the target was already partial.
- `python research/reading_audit/v10_relabel.py` does not list document A now that its state is read in part; the same
  measure on the entry (`v10_relabel.measure_detail`) gives 0.833 with the declaration.

## Remaining gaps

- 24 May 1655 passage (B), 50 letters and the numbers 7, 865, 73 - blocker: no-key-material; not the printed Rákóczi table, not a simple substitution of Latin (annealing, matched control); the original (MNL OL E 190) is needed for the readings and any key
- the word (iyy) in the 4 Aug letter - blocker: too-short; three letters, "boo" under the printed table, not Latin; perhaps a misprint or a code name
- 22 Jul 1655, the invisible-ink page - blocker: illegible; the first lines printed by Szilágyi 1890 p. 392, the remaining c. 25 lines washed out already in 1890
- 6 Sept 1655, the secret-script passages - blocker: needs-physical-access; printed only as plaintext (Patera p. 183, Szilágyi 1890 pp. 393-394); the ciphertext is on the original only
- the 4th letter of CmCasda (a, read as a by the printed decipherment, m by the table) - blocker: needs-physical-access; both prints agree, only the original can show whether the writer slipped

## Escalation

- [x] siblings: Patera CXLVIII, CLI-CLVI and MHH XXIII's Comenius items searched; no further letter-cipher passage; 22 Jul and 6 Sept secret script printed in clear (Szilágyi 1890)
- [x] clear-pages: Szilágyi 1890 prints the 22 Jul invisible-ink page as far as it could be read; nothing for 24 May
- [x] known-keys: the printed Rákóczi/Harsányi-Balogh table (MHH XXIII p. 740) fits 4 Aug 12/12 and fails on 24 May, also with Caesar shifts
- [x] print: Patera 1892, MHH XXIII 1874 (incl. p. 740 key), Szilágyi 1890 I pp. 388-394 checked on the page images; Blekastad 1969 not online (not checked)
- [x] key-rebuild: 4 Aug rebuilt from the crib (12 letters, 3 digits); 24 May annealed with the shared Latin model, one-to-one (control recovered, passage not) and homophonic (control not recovered: underdetermined)
- [x] retry: 4 Aug re-decoded with the printed table (same result, one conflict); (iyy) re-tried ("boo"); 24 May re-tried with the table, shifts and five languages

## Files

- `ct_1655-08-04.txt`, `ct_1655-05-24.txt`: transcriptions from both prints, with the archive.org page links.
- `plain_1655-08-04.txt`: the 4 Aug decryption, line by line. `reading_1655-08-04.txt`, `translation_1655-08-04.txt`:
  the reading as sentences and in English.
- `plain_1655-05-24.txt`: the 24 May trials (not a reading).
- `key_1655-08-04.tsv`: the 4 Aug key.
- `check.py`: rebuilds the key, decrypts, shows the conflict, runs the controls and the 24 May key trials.
- `anneal.py`: the 24 May annealing with the two matched controls (about a minute).
- `anneal_lm.py` (review pass): the 24 May annealing against the shared Latin model `la` (lang/), one-to-one and
  homophonic, each with a matched control (`--long` for 60 restarts x 20,000 steps).
- `check.py` also compares the rebuilt key with the printed MHH XXIII p. 740 table and, with `--reveal <path>`, writes
  the site's `docs/reveal/comenius1655.json`.

`check.py` and `anneal.py` use the Python standard library and relative paths (`python check.py`, `python anneal.py`); `anneal_lm.py` needs numpy and the repository's lang/ package.

Work done with AI language-model agents. Every cipher letter quoted here was checked against the archive.org page
images of both prints, and a second agent re-checked the readings, the key and the page numbers independently.
