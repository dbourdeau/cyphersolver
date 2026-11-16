"""Write proposals.json for wave 17 (16 Nov 2026). python -I -X utf8 make_proposals.py"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = '2026-11-16'
BY = 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 17 vetting'
ASF = 'https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/'
DEC_MAP = ("DECODE RecordsList keyword search by curl (research/sweep_2026-11-11_german/decode_search.py), 16 Nov 2026: "
           "'Pandolfini', 'Soderini', 'Sassetti', 'Lanfredini' 0 records; 'Mediceo' returns only the ASFi Cifrari serie II vol. 9 "
           "key records of 1601-1800 (R7455-R7459 and neighbours). No DECODE record of any Mediceo avanti il Principato letter.")
TOMO = ("Tomokiyo's cryptiana unsolved.htm (repo copy img/raw/unsolved.txt, fetched 15 Nov 2026) grepped for {t}: no hit; its only "
        "Medici items are Catherine and Marie de Medici.")
LAS = ("cryptiana GL.htm (Lasry's decipherments; repo copy img/raw/GL.txt) grepped for {t}: no hit; its Florentine items are "
       "Acciaiuoli 13 Jun 1478 (R4800) and a 1597 Guicciardini letter, not this document.")
P = {}

P['2574'] = dict(verdict='open', confidence='medium', access='online',
  access_note='ASF MAP IIIF images by plain curl (server maximum 1272 px); the host answered again on 16 Nov 2026 after the outage of 6-11 Nov.',
  note=("A full page of Pandolfini's symbol cipher, about 19 lines, with no decipherment on the leaf or on the neighbouring cartae; "
        "nothing in DECODE, cryptiana or GL.htm, and the Google Books feed finds no Lettere note citing MAP XXXVIII 418, though "
        "the notes of Lettere VI were not read in full."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where=f"ASF MAP filza XXXVIII image positions 913 (doc. 418 recto) and 914 (verso), {ASF}00100038/A0000913.ptif and A0000914.ptif, full/max = 1272 x 1807 px each, downloaded 16 Nov 2026 and viewed whole and in crops; neighbours 912 (verso of doc. 417) and 915 (doc. 419) fetched at the same size and viewed.",
      extent="One leaf: recto has 4 clear opening lines ('Mce vir etc. Hiersera, benche non mi sentissi bene, vi scripsi una lettera ...'), then about 19 lines in which cipher runs carry the text with clear words between them ('il fatto dell'arcivescovo', 'del papa', 'alla dieta', 'grandis'), a clear closing 'Ho altro per hora, racchomandomi a voi ... Die xxvij Martij 1482' and the signature 'Petrusphilippus Pandolfi Rome ora[tor]'. Roughly 1,000 signs.",
      cipher="Symbol cipher of Latin-letter-like forms, digits and crossed or looped signs without word division. Nothing is written between the lines, in the margin (one short marginal note at the left of line 5, not a gloss) or at the foot. The verso holds the address 'Mco viro Laurentio de medicis Maiori' and the endorsement '1482 Da Pierphilippo pandolfini da Roma ad xxvij di marzo, recev. a di 31 detto'. Position 912 is the verso of doc. 417 (another Rome letter of 1482) and 915 is doc. 419, a clear letter in a different hand: no decipherment slip on either side."),
    prior_art=dict(
      decode=DEC_MAP,
      tomokiyo=TOMO.format(t="'Pandolfini', 'Medici', 'Florence', 'Firenze'"),
      lasry=LAS.format(t="'Pandolfini', 'Medici', 'Florence'"),
      edition=("Lorenzo de' Medici, Lettere VI (1481-1482, ed. Mallett) prints Lorenzo's letter no. 568 to Pandolfini of 27-28 Mar 1482 and its notes discuss Pandolfini's letters reaching Florence on the evening of 27 March (Google Books feed snippet, CSBdAAAAMAAJ, 16 Nov 2026). This letter of 27 March was received on the 31st, so it is a different one. Feed queries '\"XXXVIII, 418\"', '\"MAP, XXXVIII, 418\"', '\"XXXVIII, 418\" Pandolfini' and 'Pandolfini \"XXXVIII\" marzo' found no Lettere VI or VII page citing it. The archive.org copy of Lettere VI (bwb_KU-999-229_6) is a lending item whose full-text search answered 'Invalid filename', so the notes were not read in full. Lettere prints Lorenzo's own letters and only quotes incoming ones in notes."),
      literature=("Web search and the sibling lead 2559 (Pandolfini, Rome, Apr 1483; vetted open 13 Nov 2026) turned up no study or transcription of Pandolfini's Roman cipher letters of 1482-83. Marco Vito (Vienna) works on encrypted MAP letters of 1486-1491 (research/medici_bia/README.md); 1482 is before his range.")),
    key_check=("No key for 1482 held. The project rebuilt Pandolfini's January 1487 key from glossed letters in MAP (trackB, recorded in lead 2559's vetting) and it did not fit the 1483 letter; it was not tried on this one. The 1483 letter (lead 2559) looks like the same sign system, so the two give two samples of one system."),
    duplicates=("known.py 'XXXVIII' and 'Pandolfini' (16 Nov 2026): only this lead, the sibling 2559 (LIII 13, 1483), leads 1552/1553 (Lorenzo to Pandolfini, BNCF) and catalogue 2389 (Francesco Pandolfini, 1514-15); no row holds MAP XXXVIII 418."),
    verdict='open'))

P['2385'] = dict(verdict='open', confidence='medium', access='online',
  access_note='ASF MAP IIIF by curl, 16 Nov 2026 (doc. 15 recto 1465 x 812 px).',
  note=("A short personal note with one run of about 30 signs, bare; the glossed letters of the same writer (docs 14 and 17) sit beside it and give the key, but no reading of this run is on record anywhere."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where=f"ASF MAP filza LXXV, {ASF}00100075/A0000034.ptif (doc. 15 recto, 1465 x 812 px), A0000035 (doc. 15 verso, 812 x 1465) and A0000033 (doc. 14, 1428 x 2001), full/max, downloaded and viewed 16 Nov 2026 with crops of the cipher lines and the signature.",
      extent="One oblong note of 13 lines beginning 'Piero mio, io sono sano ...'; the cipher is one run of about 30 signs filling the second half of line 9 and the start of line 10, between clear words. Signed 'Cosimo suo salutem' with a date line ending '... 1494' (day and month only partly legible at this size).",
      cipher="Sign cipher: circles, crosses, a square, Greek-like letters (phi, psi, sigma forms), digit-like signs; no word division visible. No gloss above or below the run and nothing in the margin; the verso has only the address. Doc. 14 (Sassetti's letter of 8 June 1494) carries the same kind of signs with small interlinear plaintext above them, so the system is glossed elsewhere in the filza but this run is not."),
    prior_art=dict(
      decode=DEC_MAP,
      tomokiyo=TOMO.format(t="'Sassetti', 'Medici', 'Florence'"),
      lasry=LAS.format(t="'Sassetti', 'Medici'"),
      edition="No edition of Cosimo Sassetti's letters to Piero di Lorenzo found: earlier passes checked Desjardins, Négociations I (no Sassetti) and the MAP inventory vol. 3 (archive.org OCR), which does not flag the note as cipher; a web search on Cosimo Sassetti, June 1494, MAP LXXV found nothing printed.",
      literature="Web search (Cosimo Sassetti 1494 cifra Piero de' Medici Lione) and the repo's research/medici_bia notes: no study of Sassetti's cipher; Marco Vito's work covers 1486-91 letters to Lorenzo, not 1494 letters to Piero."),
    key_check="No key held. Key in volume: docs 14 (8 Jun 1494) and 17 (20 Jun 1494) of the same filza carry interlinear glosses over the same sign set, enough to build a table; not tested in this pass.",
    key_in_volume="MAP LXXV docs 14 and 17, Sassetti's glossed letters of 8 and 20 June 1494 (A0000033 and the following positions): interlinear plaintext over the signs; not yet transcribed or applied to doc. 15.",
    duplicates="known.py 'LXXV' and 'Sassetti' (16 Nov 2026): only this lead and its sweep row; the glossed letters 14 and 17 are not entries. If the lead agent prefers, this note can be folded into one entry with 14 and 17.",
    verdict='open'))

P['2387'] = dict(verdict='open', confidence='low', access='online',
  access_note='ASF MAP IIIF by curl, 16 Nov 2026 (1272 x 892 px, the server maximum).',
  note=("Five lines of dot-separated words in ordinary letters, most of them not Italian and crowded with z, h and ch, which looks like a word-preserving letter substitution; no transcription or substitution test was made, so the cipher call rests on sight only."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where=f"ASF MAP filza LXXIII, {ASF}00100073/A0000005.ptif (doc. 3, 1272 x 892 px) and A0000006 (verso), full/max, downloaded 16 Nov 2026; the five text lines viewed in 2x crops.",
      extent="One leaf: head '+ Ex urbe Rome 1494', five lines of about 15 dot-separated words each (about 70 words), signature 'Jacobi ...' with a second word not read; the verso has the address panel only.",
      cipher="Every word is followed by a dot, in a regular mercantesca. A few words read as Italian ('perche', 'sono', 'tre', 'amor', 'spero') but most do not ('chazap...', 'zhezno', words with repeated z/zh/ch clusters and few vowels), which fits a letter substitution that keeps word division (vowels replaced by consonants) better than a hard hand. No gloss, no interlinear or marginal writing, no clear copy on the neighbouring position."),
    prior_art=dict(
      decode=DEC_MAP,
      tomokiyo=TOMO.format(t="'Medici', 'Florence', 'Rome 1494'"),
      lasry=LAS.format(t="'Medici', 'Florence'"),
      edition="No edition: the writer is not identified, the MAP inventory (vol. 3, archive.org OCR) does not flag the item as cipher, and earlier passes found no print of a Rome letter of 1494 signed Iacobo.",
      literature="Web search on the item (Rome 1494, Iacobo, MAP LXXIII, cifra) in earlier passes and known.py found nothing; no study of Latin-letter substitution disguises in MAP letters of 1494 turned up."),
    key_check="No key held or seen in the volume; a simple substitution test on a transcription is the first step (not done).",
    duplicates="known.py 'LXXIII' (16 Nov 2026): only this lead and its sweep row.",
    verdict='open'))

P['2396'] = dict(verdict='not_cipher', confidence='medium', access='online',
  access_note='ASF MAP IIIF by curl, 16 Nov 2026 (1272 x 1789 px).',
  note=("At full size the dot-separated words read as northern Italian written phonetically (z for g: 'zenero', 'za'), not as substitution: 'dimostrazione', 'bisogno e consumarle', 'absoluto', 'el tempo', 'non e terminato', 'medesimo'; only a few words ('alpobbo', 'farake') are unclear and look like dialect or a cover name, not a cipher."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where=f"ASF MAP filza CXXXVII, {ASF}00100137/A0001719.ptif (c. 756r, 1272 x 1789 px) and A0001720 (c. 756v), full/max, downloaded 16 Nov 2026; the 'alpobbo' passage viewed in a 1.6x crop.",
      extent="Two full pages of a crude cursive, about 40 lines on the recto, every word followed by a dot; signature on the next leaf not checked.",
      cipher="Reads as dialect Italian: 'medesimo', 'Calandria (?) ... fara alpobbo, farake ... al passo alpobbo ... bisogno e consumarle, che za N.S. absoluto ... el tempo ... non e terminato', 'dimostrazione', 'provare', 'anno', 'amico', 'molto'. The z-for-g spelling (za = gia, zenero = genero) is Venetian/Lombard phonetics. 'alpobbo' (three times) may be 'al populo' or a cover name; nothing shows a letter substitution, and there are no signs or figures. No gloss anywhere on the leaf."),
    prior_art=dict(
      decode=DEC_MAP,
      tomokiyo=TOMO.format(t="'Medici', 'Florence'"),
      lasry=LAS.format(t="'Medici', 'Florence'"),
      edition="No edition known; the writer is not identified and the MAP inventory does not flag the item as cipher.",
      literature="No literature found or expected for an unidentified dialect letter; earlier passes (n20, t01) already leaned towards dialect Italian."),
    key_check="Not applicable: no cipher system seen; no key in the volume relates to it.",
    duplicates="known.py 'CXXXVII, doc. 747' (16 Nov 2026): only this lead.",
    verdict='not_cipher',
    closed="Closed as not cipher: at full size the dot-separated words are northern Italian dialect written phonetically, not a letter substitution; a possible cover word 'alpobbo' is not a cipher."))

P['2375'] = dict(verdict='not_cipher', confidence='medium', access='online',
  access_note='ASF MAP IIIF by curl, 16 Nov 2026 (doc. 11 at 1272 x 821 px).',
  note=("Doc. 11 at full size reads as ordinary Italian in a fast, much-corrected hand ('madonna', 'conforteranno', 'tutti loro', 'cavalli', dated 'in Milano a di 8 luglio 1477', signed Tomaso Soderini); the inked-out words are cancellations, and Lettere II cites doc. 13 of the run as ordinary prose."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where=f"ASF MAP filza XLVIII, {ASF}00100048/A0000023.ptif (doc. 11 recto, 1272 x 821 px) and A0000027 (doc. 13, 1352 x 1240), full/max, downloaded 16 Nov 2026; earlier passes (n18) viewed docs 11-15 at the server maximum.",
      extent="Doc. 11: one oblong page of 18 lines, date line 'in Milano a di 8 luglio 1477', signature 'Tomaso Soderini'; docs 12-15 are similar single pages.",
      cipher="No signs or figures. Most words read as Italian when the hand is followed ('madonna', 'conforteranno', 'tutti loro', 'cavalli', 'al campo', 'domani'); the words struck through with heavy ink are cancellations in the flow of the text, not code groups. Earlier passes found ordinary Italian vowel patterns and no gloss."),
    prior_art=dict(
      decode=DEC_MAP,
      tomokiyo=TOMO.format(t="'Soderini', 'Medici'"),
      lasry=LAS.format(t="'Soderini', 'Medici'"),
      edition="Lorenzo de' Medici, Lettere II (1474-1478, ed. Fubini; Google Books 1hpdAAAAMAAJ) p. 432 cites 'T. Soderini a Lorenzo, ... MAP, XLVIII, 13' and paraphrases it as ordinary content, with no mention of cipher (vetting_2026-11 batch c35).",
      literature="Rochon, La jeunesse de Laurent (1963) uses Soderini's 1477 letters in MAP XLVIII without mention of cipher (noted in batch n18); no study treats them as disguised."),
    key_check="Not applicable: no cipher system seen.",
    duplicates="known.py 'XLVIII' and 'Tommaso Soderini' (earlier passes): only this lead; Soderini's true sign cipher of August 1481 is a separate row.",
    verdict='not_cipher',
    closed="Closed as not cipher: Soderini's June-July 1477 letters are ordinary Italian in a hard, much-corrected hand, and the editor of Lorenzo's Lettere read one of them as prose."))

RIK_DEC = ("DECODE RecordsList keyword search, 16 Nov 2026: 'Banér'/'Baner' and 'Gardie' 8 pages each, all the Riksarkivet Chifferklaver key sheets (R4325-R4329 and neighbours) plus a 1639 Trauttmansdorff record; 'Oxenstierna' 9 pages (Oxenstiernska samlingen and Rusdorff letters). No record of a letter from Skrivelser till konungen (SE/RA/1133).")
P['2568'] = dict(verdict='open', confidence='medium', access='online',
  access_note='Riksarkivet IIIF with the Referer header (lbiiif.riksarkivet.se); images fetched 15 Nov 2026 by the earlier wave-17 run.',
  note=("Seven bare number-cipher passages in Banér's letter of 6 Apr 1627; DECODE has Banér key sheets but no record of this letter, and the HSH register lists no Banér letter of 1627."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where="Riksarkivet R0000623 images 356 and 357 (img/rik_R0000623_00356.jpg, 00357.jpg; crops 00357_a and 00357_b viewed 16 Nov 2026), from lbiiif.riksarkivet.se/arkis!R0000623_00357 with Referer https://sok.riksarkivet.se/; the 13 Nov sweep also opened image 358.",
      extent="Image 357 left page, about 25 lines of running Swedish with seven passages of comma-separated 1-3 digit groups (e.g. '85,26,3,15,32,96,51', '100,17,66,8,20,26', '116,33: 96,72: 35,65,45: 85,52,70,24,29,56,91,31,10,35,40'), roughly 150 groups; the letter ends on folio 43 with 'Datum ... den 6. Aprilis 1627'.",
      cipher="Numeric nomenclator of 1-3 digit groups with colons between words, inside clear Swedish ('Correspondera', 'Prowantroede'); a Roman 'III' and a year '1559' stand among them. Nothing is written between the lines or in the margin; image 358 (postscript) is clear."),
    prior_art=dict(
      decode=RIK_DEC,
      tomokiyo="cryptiana unsolved.htm (repo copy) grepped for 'Banér', 'Baner', 'Swed': no Banér item; the Swedish hits are Torbjörn Andersson's BnF fr. 2988 solution and HistoCrypt references.",
      lasry="GL.htm (repo copy) grepped for 'Banér', 'Baner', 'Swed', 'Oxenstierna': the Swedish items are Lasry's 'Swedish Cipher in Latin' (R4282) and the Rusdorff letters to Oxenstierna of 1625 (R4336-R4337), not this letter.",
      edition="Handlingar rörande Skandinaviens historia, Kronologiskt register (archive.org copy, img/raw/hsh_reg.txt) grepped: Johan Banér's entries (vols 25, 29, 32, 35, 36, 38) concern 1630s matters, none a letter of April 1627 to the king. A web search for printed Banér letters to Gustav II Adolf of 1627 found none.",
      literature="Web search (Johan Banér brev 1627 Gustav II Adolf, chiffer) found no study or decipherment; the project's own baner1640 target is a different letter and key period."),
    key_check="No key tested. Banér key sheets are on DECODE (R4122, R4123, R4325 via decode_updates/queue.json and targets/baner1640), of later date; whether one matches the 1627 groups is untested. The glossed Oxenstierna code of 1633-35 (1133.08/7-13) is a later chancery system.",
    key_held="DECODE Chifferklaver records R4122, R4123 and R4325 (Banér keys, from targets/baner1640): not tested against the 1627 groups.",
    duplicates="known.py on '1133.07/3', 'R0000623' and 'Johan Banér' (13 Nov sweep) and the catalogue scan for R0000623 (16 Nov): no other row holds this letter.",
    verdict='open'))

P['2567'] = dict(verdict='open', confidence='medium', access='online',
  access_note='Riksarkivet IIIF with the Referer header; images fetched 15 Nov 2026.',
  note=("Four short bare number-cipher passages in De la Gardie's despatch of 26 Mar 1632; no edition or DECODE record. Tartu University Library holds De la Gardie's drafts ('Konzepte der Berichte ... an seinen König'), which may contain the clear text: not checked."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where="Riksarkivet R0000783 images 198 and 199 (img/rik_R0000783_00198.jpg 2273762 bytes, 00199.jpg), Referer route, viewed 16 Nov 2026; the 13 Nov sweep also opened 196, 197 and 200.",
      extent="Image 198 right page (fol. 196): three passages of dot-separated groups ('0.2106.3185.229.82.73.77.26.31.98.17.82.72.47.92.26', '26.2837.rr.97.ium', '20.33.50.44.51.83.91.66.72.22.57', '26.31.3185.ll.26.1420.dg.3506.99.89.92', '43.93.33.2090') and a short group 'tt.26.24.73.26.80.86' lower on the page; about 60 groups in all.",
      cipher="Numeric nomenclator with 2-4 digit groups and a few letters (rr, ll, dg, tt) inside clear Swedish; no interlinear or marginal plaintext on the leaf."),
    prior_art=dict(
      decode=RIK_DEC,
      tomokiyo="cryptiana unsolved.htm (repo copy) grepped for 'Gardie', 'Swed': no De la Gardie item.",
      lasry="GL.htm (repo copy) grepped for 'Gardie', 'Swed', 'Oxenstierna': only R4282 and the Rusdorff letters; not this despatch.",
      edition="HSH Kronologiskt register grepped: Jakob De la Gardie's entries (vols 2, 8, 19, 32, 36) include no letter of March 1632 to the king. A web search found no printed edition of his 1632 despatches.",
      literature="Web search (Jakob De la Gardie brev Gustav II Adolf 1632 chiffer) found no decipherment; it did find Tartu University Library (dspace.ut.ee) manuscript files 'Konzepte der Berichte Jakob De la Gardies an seinen König und an andere Personen' and the king's letters to him 1627-1632, which were not opened."),
    key_check="No key tested. A draft of this despatch among the De la Gardie papers in Tartu (dspace.ut.ee, 'Konzepte der Berichte') could give the plaintext; not opened. The DECODE Chifferklaver sheets returned for 'Gardie' (R4325-R4329) were not compared.",
    key_held="DECODE Chifferklaver records R4325-R4329 (Riksarkivet key sheets matched by the search 'Gardie'): not compared with these groups.",
    duplicates="known.py on '1133.07/8', 'R0000783' and 'De la Gardie' (13 Nov sweep): no other row; the glossed letter on image 195 of the same volume is a different letter.",
    verdict='open'))

P['2570'] = dict(verdict='open', confidence='medium', access='online',
  access_note='Riksarkivet IIIF with the Referer header; images fetched 15 Nov 2026.',
  note=("The bare passages on images 55 and 56 are confirmed; nothing printed or on DECODE. The project's own target chemnitz1631 (PR #539) reads them in part from the image 57 glosses: that is this project's work, not prior art, and the target NOTES say the lead stays open."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where="Riksarkivet R0000624 images 55, 56 and 57 (img/rik_R0000624_00055.jpg, 00056.jpg, 00057.jpg, Referer route), image 56 viewed 16 Nov 2026; the 13 Nov brief-test vetting (research/vetting_2026-11-13_brief_test/vetting.json) opened 55-57 at 1800 px.",
      extent="Image 56 left page: one passage of about 8 lines of dotted numbers with letters (m, pf, st) inside a German letter dated 'Datum Nürnberg den 7. Xbris Ao 1631', signed '...Chemnitz'; image 55: a 7-line passage; image 57: a leaf almost wholly in cipher with an interlinear German decipherment.",
      cipher="Dot-separated 1-2 digit numbers with letters; on 55 and 56 nothing between the lines or in the margin. Image 57 is glossed word by word, so the system is deciphered on a sibling leaf, not on these two."),
    prior_art=dict(
      decode="DECODE RecordsList (brief-test vetting 13 Nov 2026): 'Chemnitz' 0, 'Skrivelser till konungen' 0, 'Gustav II Adolf' 0, 'Nürnberg' 1 (a 1908 postcard), 'Nuremberg' 2 unrelated; repeated 16 Nov for 'Oxenstierna' and 'Gardie': no record from SE/RA/1133.",
      tomokiyo="cryptiana unsolved.htm (repo copy) grepped for 'Chemnitz', 'Swed': no item on this letter.",
      lasry="GL.htm (repo copy) grepped for 'Chemnitz', 'Nürnberg', 'Swed': only the Swedish Latin cipher R4282 and the Rusdorff letters.",
      edition="Arkiv till upplysning om svenska krigens historia II (archive.org) has no Chemnitz letter of 1631; Irmer, Verhandlungen Schwedens mit Wallenstein I cites only a Chemnitz report of March 1632 (brief-test vetting). Irmer II-III and Soden were not opened.",
      literature="Web searches (Martin Chemnitz Nürnberg 1631 Gustav Adolf Chiffre) found biographies only. targets/chemnitz1631/NOTES.md (merged from PR #539, Brice Dudout) holds a reading in part (68 of 89 cipher words sure) made with the key rebuilt from image 57; this is the project's own work."),
    key_check="Key in volume: the interlinear decipherment of image 57 (same writer and file) gives 598 letter-group pairs; targets/chemnitz1631/key.tsv (79 values) was rebuilt from it and passed a held-out test on image 58.",
    key_in_volume="Image 57 of R0000624, a Chemnitz letter deciphered between the lines; applied in targets/chemnitz1631 (read in part, in progress).",
    duplicates="known.py '1133.07/4', 'R0000624', 'Chemnitz': only this lead, its sweep and targets/chemnitz1631; no catalogue entry.",
    verdict='open'))

P['2858'] = dict(verdict='open', confidence='high', access='online',
  access_note='DARA PDF AHPZ_C_CRAR_000040.pdf (two page images), fetched 15 Nov 2026 by the earlier wave-17 run.',
  note=("The 2025 monograph on Claver prints this very letter (Apéndice doc. 10) with the cipher left as '[diez líneas en cifra]', although Ivan Parisi deciphered Claver's other Milan and Naples despatches for the same book: the cipher passage is unread in print and bare on the leaf."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where="DARA record https://dara.aragon.es/opac/app/item?i=1056537 (C_CRAR/000001/0040), PDF attachment b4/11/AHPZ_C_CRAR_000040.pdf, two images extracted (img/dara_0040_p0_0.jpeg 1578 x 2211 px, recto; dara_0040_p1_0.jpeg 2219 x 1575 px, verso) and viewed 16 Nov 2026.",
      extent="One leaf, the end of the letter (the beginning is lost; DARA: 'Incompleta', torn at lower left): about 28 lines of clear Spanish, then about 13 lines of cipher, then the clear close 'y acreciente Dios las reales ... Fecha en Milán a XVIIII de junyo de 97' and the signature. Verso: address 'A los muy altos y muy poderosos principes ... el Rey y la Reyna de Spaña' and the endorsement 'De Claver xix de junio'.",
      cipher="Sign cipher of letter-like forms, digits, dots and colons with spaces between groups (word-separated), about 13 lines and roughly 400 signs; nothing written between the lines, in the margin or on the verso."),
    prior_art=dict(
      decode="DECODE RecordsList search 16 Nov 2026: 'Claver' 1 record, R9591 (RAH Salazar 9/8 ff. 20-21v, Claver, Naples 1500); 'Zurita' 0. No record of this Zaragoza letter.",
      tomokiyo="cryptiana unsolved.htm (repo copy) grepped for 'Claver', 'Zurita', 'Ferdinand': no Claver item; its Ferdinand entries are Garcilaso 1498 (Parisi), Espagnol 318 and Catherine of Aragon.",
      lasry="GL.htm (repo copy) grepped for 'Claver', 'Ferdinand', 'Fernando': no hit for Claver or this letter.",
      edition="Printed: C. Villanueva Morte and Á. Fernández de Córdova Miralles, El embajador Claver. Diplomacia y conflicto en las «Guerras de Italia» (1495-1504), Anejos del Anuario de Estudios Medievales, CSIC 2025 (open PDF https://zaguan.unizar.es/record/151256/files/BOOK-2025-316.pdf, downloaded 16 Nov 2026), Apéndice documental, Documento 10 (pp. 178-179) transcribes this letter from 'DARA 003006/0040' and prints the cipher as '[diez líneas en cifra]'; the text discussion (p. 69 n. 182) uses only the clear part.",
      literature="Same book, pp. 21-23: Ivan Parisi deciphered Claver's despatches from Milan and Naples and rebuilt his nomenclators 'casi por completo', and the decipherments printed in the appendix (docs of 1498-1502) are credited to him; Parisi, 'La decrittazione di cinque lettere cifrate di Juan Claver' (ASPN 137, 2019) covers 1500-02. Neither reads this 1497 passage. Web search (Juan Claver Milán 1497 carta cifrada) found nothing else."),
    key_check="No key tested. Key held in print: Parisi's reconstructed Claver nomenclators (1498 Ocaña despatches to the duke of Milan, and the Naples system of 1500-02, Parisi 2019 and the 2025 appendix) may cover the 1497 Milan system; not compared.",
    key_held="Parisi's Claver tables (ASPN 2019; El embajador Claver 2025, appendix decipherments): not compared with this 1497 passage.",
    duplicates="known.py 'Claver' and 'C_CRAR' (16 Nov 2026): the other Claver row is lead 1048 (RAH Salazar A-11 ff. 131-133, 23 Jun 1497), a different letter: the 2025 book cites 1048 separately (n. 183, report on the Gandía murder, printed by Suárez Fernández, Política internacional V docs 29-30). The CRAR catalogue entries 2854-2857 and 2865 are other letters.",
    verdict='open'))

P['2859'] = dict(verdict='not_cipher', confidence='high', access='online',
  access_note='DARA PDF AHPZ_C_CRAR_000029.pdf (two page images), fetched 15 Nov 2026.',
  note=("The whole PDF is two images: a wholly clear letter and its address. Ferdinand only mentions that two of John II's four letters were in cipher and that he will answer the ciphered matter by another messenger; there is no cipher in this item."),
  vetting=dict(date=D, by=BY,
    seen=dict(kind='scan',
      where="DARA record https://dara.aragon.es/opac/app/item?i=1055725 (C_CRAR/000001/0029), PDF attachment 79/f2/AHPZ_C_CRAR_000029.pdf (2 pages), images img/dara_0029_p0_0.jpeg (1617 x 2160 px) and dara_0029_p1_0.jpeg (1598 x 2157 px) viewed 16 Nov 2026.",
      extent="One letter of 24 lines on the recto, dated 'Dada en Guadalupe a xxv de enero año MCCCCLXXIX', signed by Ferdinand and countersigned; the verso has the address 'A la real magestat del señor e padre muy [honor]able' and endorsements '1479, Del Sr. Rey de Castella'.",
      cipher="No cipher: every line is clear Castilian. The text says 'quatro cartas juntas, dos en cifra e dos en llano, he recebido de vuestra magestat' and 'quanto a lo que scrive en cifra, por otro mensagero ... respondere'; the DARA summary's 'otro tema que queda en secreto (cifrado)' refers to that deferred answer."),
    prior_art=dict(
      decode="DECODE RecordsList search 16 Nov 2026: 'Zurita' 0; no record of this letter (not expected, as it holds no cipher).",
      tomokiyo="cryptiana unsolved.htm (repo copy) grepped for 'Zurita', 'Ferdinand': nothing on this letter.",
      lasry="GL.htm (repo copy) grepped for 'Ferdinand', 'Fernando': nothing on this letter.",
      edition="No edition looked for beyond the DARA summary, since the letter is wholly clear and readable on the scan.",
      literature="None needed; the item's interest is as a dated mention of John II's cipher letters of January 1479, which are not in this file."),
    key_check="Not applicable: no cipher in the item. The two cipher letters of John II it answers are not in C_CRAR/000001.",
    duplicates="known.py 'C_CRAR' (16 Nov 2026): the CRAR rows 2854-2857, 2865 and lead 2858 are other letters.",
    verdict='not_cipher',
    closed="Closed as not cipher: Ferdinand's letter of 25 Jan 1479 is wholly in clear and only mentions that two of his father's letters were in cipher."))

# Assessed, no vetting block
NOV = {
 '2312': ("Re-viewed at the server maximum (A0000427 1364 x 1252, A0000428 1358 x 1272) on 16 Nov 2026: dense mercantesca in clear with a few anomalous groups containing a digit ('z7to', 'zyzz7to', each before 'cremona' on recto lines 9 and 11) that may be code names; the verso foot date reads '... 17 di lug(li)o 1459' as the earlier pass found, so the inventory's attribution to Piero di Lorenzo cannot stand. Cipher share and sender still need a palaeographic reading of the clear text; no verdict.", 'online'),
 '2379': ("ASF host answers again (16 Nov), but the blocker is the edition: the volume of Lorenzo's Lettere for Aug 1488 - Feb 1489, which would print this minute and may give its 14 cipher runs in clear, is not online; Google Books feed '\"CXXXVII, 504\"' finds only Lettere XV's note (already recorded) and no other volume. Blocker stands.", 'online'),
 '2529': ("Blocker stands: HSH del 30 (1849) p. 91, which prints the letter according to the register, is still not online (feed: only a 2013 reprint record and register snippets); AOSB I:12 (1977) snippets show only its table of contents. AOSB II (Horn letters, 1897) notes another letter in the same water-damaged volume ('Oxenstiernas Skrifvelser till K. Maj:t och Rådet, ankomna 1634, Vol. II c. sid. 719 ... nästan utplånadt af vatten'), so the damage is known to the editors.", 'online'),
 '1243': ("Blocker stands: Staatsarchiv Zürich A 225.1 Nr. 182 has no image online and Tanner 1917 (Beilagen pp. 649-650, edition with facsimile) is still not found online; recorded six times between 29 Oct and 11 Nov, not repeated.", 'archive'),
 '1553': ("Blocker stands: internetculturale.it did not answer curl on 16 Nov (HTTP 000; CAPTCHA on 11 Nov), and Lorenzo's Lettere XVI (Böninger 2011) is not online. The BNCF record itself says a few words are glossed interlinear.", 'online'),
 '1564': ("Gosellini record not found by script: Lodovico's search page (ricercadl.aspx?keywords=Gosellini) loads its results by JavaScript and gives no record id; a web search found no record URL. Needs the record UUID (Chrome on Lodovico), then the IIIF route.", 'online'),
 '1573': ("Blocker stands: Gallica btv1b90007170 is another volume (16th-c. German papers), confirmed in five passes; no ark for the real Lorraine 367 found. Not repeated.", 'online'),
 '2884': ("Blocker stands (research/vetting_2026-11-15_arabic_1): the sign side is running text with no gloss, but it is not established as a cipher rather than an unidentified script; needs a palaeographer's identification and Bohak's inventory. The earlier wave-17 run fetched the CUDL images (img/tsk24_*) but that does not touch the blocker.", 'online'),
 '2888': ("Blocker stands (research/vetting_2026-11-15_arabic_2): f. 1a itself not seen (Qalamos unreachable) and the 16 signs on Sellheim's plate may be stroke-group numerals; not established as cipher.", 'online'),
 '2903': ("Seen on CUDL (img/add2255_40_col.jpg, f. 19v line 14): about 13 signs in three groups between dandas before 'likhitam' (e.g. a looped form, '4', '6', 'X'), unlike the Jaina Devanagari of the text. Not established as cipher: they could be a merchant script of the region (Mahajani/Lande) or a numeral notation rather than a cipher, and no prior art on Jain cryptic colophons was found (one web search). Needs that comparison first; no verdict.", 'online'),
 '1438': ("Blocker stands: NYPL serves only 538 x 760 px (Incapsula shell on digitalcollections), and Kavrus-Hoffmann, Manuscripta 50 (2006) pp. 21-76, which would describe the cryptographic prayer of Spencer Greek MS 2, is not online (web search 16 Nov).", 'online'),
 '1441': ("Blocker stands: Harvard id.lib.harvard.edu returned 403 Forbidden to the earlier wave-17 run (img/harv.html, 15 Nov), as in five earlier passes; the coded name is still unlocated.", 'online'),
}
for k, (n, acc) in NOV.items():
    P[k] = dict(verdict=None, confidence=None, access=acc, access_note='see note', note=n)

out = dict(sorted(P.items(), key=lambda kv: int(kv[0])))
json.dump(out, open(os.path.join(HERE, 'proposals.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'proposals;', sum(1 for v in out.values() if 'vetting' in v), 'with vetting blocks')
