# William Perwich to Lord Arlington, Paris, 9 April 1670 — solved in 2025, and reproduced here

Status: no write-up (deciphered by others first, Sept 2025; reproduced here only, nothing added. Outcome method: read from existing decipherment. A site page made 24 Sept 2026 was withdrawn the same day at Daniel's request).

TNA SP 78/129 f.180, published by the National Archives in August 2025 and transcribed by Satoshi
Tomokiyo. Roughly 500 cipher cells laid out as lines across two manuscript pages, embedded in an
otherwise plain English despatch.

## Status: solved (October 2025), and this project had it wrong

The National Archives announced on **14 October 2025** that the cipher had been broken twice,
independently: by **Matthew Brown**, and by **George Lasry, Norbert Biermann and Satoshi Tomokiyo**
([TNA blog](https://www.nationalarchives.gov.uk/explore-the-collection/the-collection-blog/secret-diplomatic-message-deciphered-after-350-years/)).
It is a **columnar transposition with 20 columns and nulls**, as first described.

An earlier version of these notes (15 September 2026) argued that it was *not* a transposition but a
substitution. That was wrong, and the error is instructive:

* **The chi-squared test was fooled by nulls.** The grid holds 8 q's where English of this length
  expects half of one; q alone contributes **106** of the whole-grid chi-squared of 160. On the
  plaintext cells only, chi-squared is **28.0**, which is ordinary English. The "sorted profile fits
  English" half of the argument was true and proved nothing: a transposition preserves the shape too.
* **The digram-repeat test assumed the wrong unit.** It treated the transcribed *columns* of the
  layout as the transposition's columns. The actual columns are the transcribed **rows**, so the
  search was over the wrong object and could only return noise.
* **The evidence against substitution was in the cells all along.** `ye`, `yt`, `ym`, `wt` and `&`
  are plaintext scribal abbreviations. A substitution would not leave four of them intact; a
  transposition, which moves cells without changing them, does.

## The structure, recovered from the transcription

* Transcribed **rows 2–21 are the 20 columns**, each written out as one line and padded at its
  right-hand end with nulls. That is why six of the eight q's sit at the right margin, as the solvers
  noticed.
* **Rows 1 and 22 are whole null lines** framing the block (`R m d g o r p w a r q d s m r o n d s u r c
  QR` and `m d p o r m h m a`); the final word *likelyhood* follows the cipher in clear.
* Read across the columns depth by depth in key order, giving **414 plaintext cells**. That is 20 full
  depths plus 14 cells, and it equals the token count of the published plaintext exactly. There are 47
  column-tail nulls besides the two null lines.
* **Key, as transcribed row numbers in plaintext column order:**
  `15 20 19 17 18 21 16 14 2 4 3 5 6 7 13 12 11 10 9 8`

A quadgram hill-climber over the order of rows 2–21 finds this cyclic sequence on its own, without
the published plaintext. Its starting point is then fixed by the text ("…grumble m" / "uch") and,
independently, by the column lengths: the 14 columns carrying an extra plaintext cell come first.

## Plaintext, as the transcription yields it

```
shcsouLdiersgrumbLemuch[yt][ye]kingisoflategrownecooltewards[ym]&giues[ym]not[ye]eneouragem
entinthciraddressesasheeusedtheyeomplainheeiswhoUygiwenuptohismmstresseswhoarenoeneeiesto[97]
norpeaee&eonsuqnentkydissuade[ye][60][96]pcrsuing[ye]frenchmanufaatere[wt]uigourknows[yt]pe
sceeanoneCyaduaneehimdnsignsIheardagreatoahsay[yt][ye][61]saydtohisbrotperheaishthimaotto[40]
peosemadamsgoingforfbrcausherIourneywasgoo[ye]interestofhiskinodsmewheruponmostdob6amtofaha
Uiapce
```

The published reading: *"The souldiers grumble much that the king is of late growne cool towards them
and gives them not the encouragement in their addresses as hee used. They complain hee is wholly given
up to his mistresses who are no enemies to 97 nor peace and consequently dissuade the 60 96 pursuing
the French manufactere with vigour knows that peace can onely advance his designs. I heard a great man
say that the 61 sayd to his brother he wisht him not to oppose madam's going for 40 becaus her journey
was for the interest of his kingdome wherupon most do boast of an alliance."* The numbers are
nomenclator codes and remain unread.

The residual misreadings are all transcription slips of a familiar kind, not cipher: `c`/`e`
confusion throughout (*eneouragement*, *eomplain*, *peaee*), `U` for `ll` (confirming Tomokiyo's
own suspicion), `6` for `o` in *boast*, `m m` for *mi* in *mistresses*, and in row 8 a `40` and an
`f` whose order the transcription has swapped (*…not to op[pose] … going for 40*).

## In print

M. Beryl Curran (ed.), *The Despatches of William Perwich* (Camden 3rd ser. 5, 1903), pp. 82-83, prints
this despatch and omits the block without a mark ("Where the original is in cipher, only the deciphered
portions have been printed", editor's preface). `camden1903.txt` is the Internet Archive text of the edition
(`despatchesofwill00perwrich`); the earlier file under that name was an archive.org error page.

## What is still open

Only the nomenclator: 40, 60, 61, 96, 97 (and 910, 192 in the null tails). From context 40 is a place
Madame is travelling to (Dover, 1670, is the obvious candidate), and 60 96 and 61 are persons.
The TNA's second blog post (14 Oct 2025) reads them tentatively from context: 97 the Dutch, 60 the
King, 96 Colbert (starting a new sentence), 61 the King, 40 England; it notes two numbers per entity.

Reproduce: `python solve20.py 10` (the keyless climb over rows 2–21), `python solve20.py report`
(plaintext, nulls, and the chi-squared with and without nulls). The earlier substitution-era scripts
(`masc.py`, `routes.py`, `stream.py`) are kept as the record of the wrong turn.
