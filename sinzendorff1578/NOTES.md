# Johann Joachim von Sinzendorff, Constantinople, 3-7 September 1578, to Rudolf II: a despatch wholly in cipher

Status: in progress (blocked: the ciphertext is not online; HHStA photographs of Türkei I 37-2 ff. 1-8 needed)

Session of 24 September 2026. Catalogue entry 343. Goal set by Daniel: solve it. Sibling target: catalogue 342,
`ungnad1576/` (Ungnad's 1576 despatch, blocked the same way).

## What the target is

Láng 2015 (*Titkosírás a kora újkori Magyarországon*, repertory p. 252) lists it as **C.Sin.03**: Sinzendorff →
Rudolf II, 3-4 and 6-7 September 1578, ÖStA HHStA Türkei I Karton 37 Konv. 2 (1578 IX-X) fol. 1-8, German,
"megfejtetlen" (no decipherment), "teljes" (wholly in cipher). The same table lists his two later ciphered
despatches, written jointly with Friedrich Breuner, as deciphered ("feloldva", partly in cipher):

| Láng | date | shelfmark | state |
|---|---|---|---|
| C.Sin.03 | 3-4 and 6-7 Sept 1578 | Türkei I 37-2 ff. 1-8 | German, undeciphered, wholly in cipher |
| C.Sin.01 | 4 Mar 1581, Constantinople (with Breuner) | Türkei I 43-3 ff. 3-5, 21-23, 6-19 | German, deciphered, partly in cipher |
| C.Sin.02 | 24 May 1581, Constantinople (with Breuner) | Türkei I 44-2 ff. 69-70, 79-80, 71-83 | German, deciphered, partly in cipher |

Láng, *Real Life Cryptology* (2018), p. 195, counts six German letters of Breuner, Sinzendorff, Ungnad and Rudolf II
in Türkei I Kartons 32-110 and prints no reading.

Context. Sinzendorff (1544-1594), Reichshofrat, left Vienna on 10 November 1577 as Ungnad's successor, reached
Constantinople on 1 January 1578, had his first audience on 17 January and stayed until 1581/82 (Hammer-Purgstall,
GOR iv, 1827, p. 51-52; Schweigger, *Newe Reyßbeschreibung*, 1608; his chaplain was Salomon Schweigger). September
1578 falls in the first year of the Ottoman-Safavid war: Lala Mustafa's army had won at Çıldır (10 August 1578) and
was taking Shirvan. Hammer cites "Ungnad's und Sinzendorf's Bericht im k. k. Hausarchive" for 1577-78, and
Sinzendorff's reports again for 1583-84, but never the September 1578 despatch.

## Where the ciphertext is not (checked this session)

| source | result |
|---|---|
| ÖStA Archivinformationssystem | Türkei I 37 = ID 967789 (Turcica 07-11.1578, former Turcica 27). Three files: **37-1** ID 3855632 (07-08.1578, fol. 1-253), **37-2** ID 3855633 (09-10.1578, fol. 1-313), **37-3** ID 3855634 (09-10.1578, fol. 1-189). All "Öffentlich", none with item records or scans. |
| DECODE (list dump, 10,106 records; API views) | No Türkei I ciphertext, nothing for Sinzendorff, Breuner 1581 or Constantinople 1578. |
| HCPortal (index checked for 342) | Nothing for Türkei or Constantinople. |
| Láng 2015 PDF (real-d.mtak.hu/922) | Repertory rows only (above); the ELTE-library Constantinople letters he mentions are Kuefstein's of 1628-29, not ours. |
| Hammer-Purgstall, GOR iv (1827, archive.org `geschichtedesosm04hamm`) | 13 mentions of Sinzendorf; used his reports but quotes nothing from the September 1578 despatch and says nothing of a cipher. |
| Web search (German, English, Hungarian) | No edition of Sinzendorff's 1578 despatches, no image or transcription. A Vienna Magisterarbeit "Die Reise des kaiserlichen Gesandten ..." turned out to be Ferus 2007 on Ungnad's 1572 journey (phaidra copy behind a bot check, not opened). |

## The key: not found yet, but its series is on DECODE

Imperial envoys to the Porte got a personal cipher from the court, filed afterwards in the Staatskanzlei
Chiffrenschlüssel (HHStA Stk Interiora, Kt. 13-14, Fasc. 20), which DECODE photographed in 2020 (R1192-R1555,
mostly left unnamed, dated by default "1500-1699" or "1600-1799"). Fetched this session with the project cookie
(images git-ignored in `decode/`):

| DECODE | folio | what it is (from the endorsement, read here) |
|---|---|---|
| **R1384** | Kt. 14 f. 129-130 | **"Ciffra pro Dno Joanne Preyner, Prima Maij 1575"**: Hans Breuner's key for his 1575 embassy to the Porte (Hammer's list of envoys: "Freyherr v. Preyner i. J. 1575"). German. Letter signs with homophones for a, e, i, o, u; 15 double-letter signs (bb … ll, mm, nn, pp, rr, ß, tt, w, st, sch); 8 nulls; nomenclator X-XVIII (Kay. Mt., Türkisch Kaiser, Mehmet Bassa, Bassa zu Ofen, Beglerbeg in Bosnien?, Sangiackbeg zu Gran?, Weyda in Sibenburg, Constantinopel, Wien). Transcribed in `key_r1384.txt`. DECODE has it unnamed ("..."), 1575. |
| R1382 | Kt. 14 f. 127 | "Ciffra pro Dno Joan. Kobenzl, Ult.a Martij 76": Latin, Polish affairs (Rex Pol., Ord. Litv., Laski, Chodkiewicz, Zborowski). Not Constantinople. |
| R1383 | Kt. 14 f. 131 | "Verschreiben mit Herrn Don Joan Manrique, 21 [Sept?] 79". Not Constantinople. |
| R1515 | Kt. 14 f. 332 | alphabet with a note "Mal. Balassa". |
| R1516 | Kt. 14 f. 333 | "Doctor Schwendi's Ziffer". |
| R1511 | Kt. 14 f. 326 | German key for Polish-Prussian affairs (Albert Laski, Johann Chodkiewicz, Danzig, Elbing). |
| R1374 | Kt. 14 f. 107 | "Ciffra pro Dno Vito a Dornberg Oratore Caesareo Venetiis, 17 Septemb. 1575": the imperial ambassador at Venice. Latin/Italian nomenclator. |
| R1375-R1377 | Kt. 14 ff. 109-120 | a Rome key (cardinals), an Italian key dorsed "7 July 75", a Polish-Lithuanian key (Chodkiewicz, Laski, the Polish estates). |
| R1378, R1379 | Kt. 14 ff. 122-124 | bare alphabets; R1379 with a Latin null-word list. No Ottoman nomenclator. |
| **R1380** | Kt. 14 f. 125 | Italian-Latin key for Ottoman affairs: papa, Imperatore, re Catholico, re di Franza, re di Pol., Mosco, Wayda Sybin., Moldavus, Bekesch, Walach, Venetia, Don Juan d'Austria, Sultan Selim, Persarum Rex, Mehmet Bassa, Bassa Budensis, Tartar Han, Arabes, Uluzaly, Sinan Bassa, Piali Bassa, Mustafa Bassa. Under Selim II, so c. 1571-74; too early for Sinzendorff. |
| **R1381** | Kt. 14 f. 126 | German letter key (signs for sch, schw, schreiben, ch, st …) with a Latin cover-word nomenclator for A-B only (Archidux = Albus, Adrianopolis 8, Agens Budensis = Ater, Agens Transylvanus = Astus, Baylus Florentiae = Basis, Bosphorus = Boreas, Caes. Mtas = sign, Carolus Archidux = Cosmus). No endorsement seen; Ottoman frontier, possibly Inner Austria. A weaker candidate. |
| R1385-R1391 | Kt. 14 ff. 132-138 | printed French key forms of the 1590s ("Le Roy", "La Ligue") and a key "avec le Roy de France". |
| R1590 | Stk Int. Fasc. 21 f. 60-65 ("Breuner?") | an 18th-c. three-digit code, endorsed for "H: gr: Breuner", 1749; not the 1581 Friedrich Breuner. |
| R1228 | Kt. 13 f. 68-69 ("Constantinople") | Italian numeric syllabary (checked for 342). |
| R392 | OSZK Quart. Lat. 2254 f. 23 | Ungnad's key, Gévay's copy (transcribed in `ungnad1576/KEY.md`). |

Kt. 14 ff. 107-138 hold the keys of 1571-1579 roughly in date order (Dornberg 1575, Kobenzl 1576, Breuner 1575,
Manrique 1579), and ff. 320-333 run alphabetically by holder (Sanches, Schönborn, Schwendi, Balassa). No sheet
endorsed for Sinzendorff was found in either run; all of ff. 107-138 were opened and looked at. A sweep of DECODE's own transcriptions of
the HHStA key records (`decode/sweep_docs.py`, `sweep_f20.py`) fetched 278 of the 286 record pages in R1192-R1555
(121 carry a DECODE transcription) plus part of the later range: the "Sinzendorf" entries there are 18th-c.
(Chancellor, Cardinal, "in Holland"; R1229 an Osnabrück election key naming Prince Eugene), and the Constantinople
and Bassa entries belong to 17th-18th-c. keys or to R1319, a Rome key of c. 1600 (Aldobrandini, Borghese).
DECODE transcribed no endorsement naming Sinzendorff; a key issued to him, if it survives, would be one of the
many untranscribed, unnamed sheets.

Sinzendorff took over the embassy while Ungnad was still in Constantinople (January-June 1578), so he may have
inherited Ungnad's cipher (R392), or have brought a new one issued in late 1577 on the model of Breuner's
(R1384). Both are the first two keys to try once the despatch can be seen.

## Result so far

No image of the despatch exists online, so nothing can be read in this session. The candidate keys are in hand
(R392 transcribed for 342, R1384 transcribed here). Every gap is blocked from outside.

## Remaining gaps

- the whole despatch, Türkei I 37-2 ff. 1-8 (3-7 Sept 1578) - blocker: needs-physical-access; not digitised, not on DECODE, HHStA reproduction order required

## Escalation

- [x] siblings: Láng's C.Sin.01-02 (1581, deciphered at the time, Türkei I 43-3 and 44-2) would give the key; not digitised (ÖStA AIS has file-level records only for these Kartons). Blocked the same way.
- [x] clear-pages: Türkei I 37-2 and 37-3 cover the same months and may hold a covering letter or a later decipherment, but neither file has images.
- [x] known-keys: R392 (Ungnad) and R1384 (Breuner 1575) found and transcribed; R1374-R1383, R1385-R1391, R1511, R1515, R1516, R1590, R1228 opened (R1380, R1381 Ottoman-front keys, not Sinzendorff's); DECODE's key transcriptions for R1192-R1555 swept, no Sinzendorff key.
- [x] print: Láng 2015/2018, Hammer GOR iv, web: no edition of the despatch.
- [n/a] key-rebuild: no ciphertext to rebuild a key from.
- [n/a] retry: nothing has been read yet, so there is nothing to retry.

## Next steps

1. Order digital reproductions from the HHStA together with no. 342: AT-OeStA/HHStA StAbt Türkei I 37-2 fol. 1-8
   (and, as the deciphered control, 43-3 fol. 3-23 and 44-2 fol. 69-83, Sinzendorff and Breuner 1581). The files
   are public and need no permission.
2. With the images: transcribe the signs; try R392 and R1384 first; if neither fits, break it ciphertext-only
   (German, `lang/`), since 8 folios of a mono- or lightly homophonic German cipher are ample.
