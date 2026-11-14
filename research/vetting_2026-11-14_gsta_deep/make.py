import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), GStA deep-sweep vetting"
D = "2026-11-14"
ACTA = "GStA PK database ACTApro (archive.spk-berlin.de/actaproweb), full record of %s, read in a Chrome tab on that origin on 14 Nov 2026 (same-origin fetch, 1.5 s apart); no digital copy or image is attached to the record."
out = {}


def lead(i, upd, seen_where, extent, cipher, pa, key_check, dup, searches, key_in_volume=None, key_held=None):
    b = {"date": D, "by": BY,
         "seen": {"kind": "not online", "where": seen_where, "extent": extent, "cipher": cipher},
         "prior_art": pa, "key_check": key_check, "duplicates": dup, "searches": searches,
         "verdict": "open", "lead_updates": dict(upd, access="archive")}
    if key_in_volume: b["key_in_volume"] = key_in_volume
    if key_held: b["key_held"] = key_held
    out[str(i)] = b


GEN_TOM = "Web search naming Tomokiyo, Cryptiana, Prussian diplomatic cipher, Frederick the Great and Klinggraeffen (14 Nov 2026)"
S_TOM1 = {"query": "Tomokiyo Cryptiana Prussian diplomatic cipher Frederick the Great deciphered cabinet orders Klinggräffen (web search)",
          "result": "Cryptiana and Klaus Schmeh's blog items on Mary Stuart, Louis XIV and Frederick I of Prussia's transposition ciphers; nothing on Frederick II's cabinet ciphers or Klinggraeffen."}
S_LAS1 = {"query": "Lasry Prussian diplomatic cipher eighteenth century Frederick II cipher key Neuchâtel Rep. 64 (web search)",
          "result": "Lasry's German diplomatic messages 1900-15 (Cryptologia 2021), HistoCrypt papers; no Neuchatel, Rep. 64 or Frederick II item."}

# ---------------- 2599 Dresden: narrowed to Nr. 782
lead(2599,
     {"shelfmark": "GStA PK, I. HA Rep. 81 (Gesandtschaft Dresden), Nr. 782",
      "title": "Frederick II's ciphered cabinet orders to his envoy Klinggraeffen at Dresden, 1747, 'mit Aufloesung in franzoesischer Sprache', Rep. 81 Dresden Nr. 782",
      "date": "1747", "year": 1747, "correspondents": "Frederick II -> Joachim Wilhelm von Klinggraeffen (Prussian envoy at Dresden)",
      "folio_note": "Nr. 782 only (1747, Bd. 2 of the series). Sibling volumes with the same description, not part of this entry (one correspondent and period each): Nr. 781 (1744/46, Klinggraeffen and orders to Buelow, Anhalt-Dessau, Rutowsky, Wallenrodt), Nr. 783 (1748, Klinggraeffen and Voss), 784 (1748, Voss), 785-786 (1749-50, Voss), 787-790 (1750-55, Maltzahn), 791 (1756, Maltzahn). The sweep row named only Klinggraeffen; the finding aid shows Voss and Maltzahn from Nr. 783 on."},
     ACTA % "I. HA Rep. 81 Dresden Nr. 782",
     "One volume of 1747; the record gives no leaf count (the neighbouring volumes are 1.5 to 4 cm).",
     "Archive description, verbatim: 'Kabinettsordern Friedrichs II. an den preußischen Gesandten Joachim Wilhelm von Klinggräf, Bd. 2'; 'Enthält v. a.: - chiffrierte Kabinettsordern mit Auflösung in französischer Sprache.' The ciphertext and its contemporary French Auflösung are in the file. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Klinggräff', 'Klinggraeffen', 'Maltzahn' and 'Voss' on 14 Nov 2026: 0 records; 'Friedrich II' returned two Saxon-envoy letters in the Hague royal house archive (records 1043-1044), no GStA PK material.",
      "tomokiyo": "Web search naming Tomokiyo, Cryptiana, Frederick II's cabinet ciphers and Klinggraeffen (14 Nov 2026): no Cryptiana page on Prussian cabinet-order ciphers of the 1740s-50s.",
      "lasry": "Same search for Lasry: his papers on Mary Stuart, papal and 1900-15 German diplomatic ciphers; none on Frederick II's Dresden ciphers.",
      "edition": "Politische Correspondenz Friedrichs des Grossen vol. 5 (1746-47; Internet Archive politischecorres05fred, OCR searched 14 Nov 2026): no item is headed as an order to Klinggraeffen at Dresden; the volume only mentions orders to him 'en chiffres' (e.g. Podewils note of 16 Feb 1746) and prints Frederick's orders to Podewils and Hennicke. No printed decipherment of the 1747 Dresden orders was found; vol. 6 (1748) and later not searched.",
      "literature": "Web search 'Maltzahn Voss Dresden 1750 Kabinettsordern chiffriert' (14 Nov 2026): only the Trier PC catalogue (orders to Voss 13 Jan 1750 are listed); no study of these ciphers. Carlyle's Frederick II (vol. 17) tells of Maltzahn and the Saxon copyist Menzel at Dresden 1752-56, the plaintext side of the Saxon file (catalogue 593)."},
     "No key is held here. The contemporary Auflösung is filed in the volume; the archive also files Frederick's 1747 cipher change in Rep. 41 Nr. 145 (per the sweep); neither is online, nothing was tried.",
     "known.py 'Klinggr', 'Dresden', 'Rep. 81' on 14 Nov 2026: catalogue 593 is the Saxon cabinet's copies of Klinggraeffen's ciphered reports (HStA Dresden), the other side of this correspondence, not this file; no entry for Nr. 782 or its siblings; lead 2599 only (Nr. 781-791 before narrowing).",
     [{"query": "Politische Correspondenz Friedrichs des Grossen Klinggräffen Dresden 1748 Kabinettsordre chiffriert Dechiffrement (web search)", "result": "Trier PC catalogue pages (instruction for Klinggraeffen 30 Jan 1746; letters to him at Hanover 1748); no word on ciphered orders at Dresden."},
      {"query": "PC vol. 5 OCR (politischecorres05fred_djvu.txt): headings 'AN ... IN DRESDEN' and 'Klinggr*' near 'chiffr*'", "result": "Two headings to Graf Hennicke in Dresden only; Klinggraeffen's name occurs 52 times in notes and instructions; 'en chiffres' mentioned once (16 Feb 1746); no order to him printed."},
      {"query": "Maltzahn Voss Dresden 1750 Kabinettsordern Friedrich II. chiffriert Auflösung französisch Brühl Gesandter Chiffre Edition (web search)", "result": "Only Trier PC catalogue metadata (Voss 13 Jan 1750, Maltzahn 1751-56); nothing on these ciphers."},
      S_TOM1],
     key_in_volume="Each order is filed 'mit Auflösung in französischer Sprache' in the same volume (per the archive description); not online, not tested.",
     key_held="GStA PK I. HA Rep. 41 Nr. 145 (Klinggraeffen's cipher 1746-47, per the 14 Nov sweep) and Rep. 63 Nr. 1472 (1758 cipher system); not online, not tested.")

# ---------------- 2600 Dresden Nr. 798
lead(2600,
     {"shelfmark": "GStA PK, I. HA Rep. 81 (Gesandtschaft Dresden), Nr. 798",
      "folio_note": "Nr. 798 (1747-48): two ciphered letters 'mit Auflösung' (Bernes to Maria Theresia 13 May 1747; Weingarten to Uhlefeldt 1748). The two senders may use different keys: they are one lead because only two letters survive and the record gives one volume."},
     ACTA % "I. HA Rep. 81 Dresden Nr. 798",
     "One volume of 1747-48, 0.5 cm: two ciphered letters with Auflösung among a rescript and a copied decree.",
     "Archive description, verbatim: 'Enthält auch: - chiffriertes Schreiben mit Auflösung von dem österreichischen Gesandten Joseph von Bernes an Maria Theresia, 13.5.1747 - chiffriertes Schreiben mit Auflösung von Weingarten an Graf [Anton Corfitz] Uhlefeldt, 1748'. Remark: the file's earlier title said these reports of the Saxon government 'wahrscheinlich durch Weingarten verraten wurden'. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Weingarten' and 'Bernes' on 14 Nov 2026: 0 hits for Weingarten; 'Bernes' returned five HHStA Staatskanzlei Interiora Chiffrenschluessel records (DECODE 1595-1612, Austrian keys 1740-49 for other envoys), not this file.",
      "tomokiyo": "Web search naming Tomokiyo, Cryptiana, Prussian diplomatic ciphers and Frederick the Great (14 Nov 2026): nothing on Austrian ciphers of the 1740s or the Bernes and Weingarten letters.",
      "lasry": "Same search naming Lasry: his Mary Stuart, papal and 1900-15 papers only; no item on Austrian ciphers of the 1740s.",
      "edition": "No edition known: the Saxon-filed copies of these Austrian reports are not in the Politische Correspondenz (letters to Klinggraeffen are not printed there either, see lead 2599); Menzel's Dresden copies are described in Carlyle, History of Frederick II vol. 17, but his text does not print them.",
      "literature": "Web search on Weingarten, Menzel and Bernes (14 Nov 2026): Carlyle tells that Weingarten, secretary of the Austrian embassy at Berlin, gave the Prussians the Austrian glosses for two or three years before June 1756; no study of the 1747 ciphers or a decipherment."},
     "Austrian cipher keys of 1740-49 are on DECODE (HHStA Chiffrenschluessel fasc. 21-22, records 1595-1612) for other envoys; none is Bernes or Weingarten's, so none was tried.",
     "known.py 'Weingarten', 'Bernes', 'Uhlefeldt' on 14 Nov 2026: no entry; catalogue 593 is the Prussian envoy's reports, not Austrian letters.",
     [{"query": "Weingarten Bernes Austrian envoy Berlin 1747 cipher betrayed Saxon Menzel Prussian deciphered Maria Theresia Uhlefeld (web search)", "result": "Carlyle's account of the 1756 Menzel-Weingarten affair; nothing on 1747 or on any decipherment."},
      {"query": "decode_search.py Weingarten; Bernes (de-crypt.org RecordsList)", "result": "Weingarten 0; Bernes five HHStA key-sheet records of other Austrian envoys 1740-49."},
      S_TOM1],
     key_in_volume="Both letters are filed 'mit Auflösung' in the volume (per the archive description); not online, not tested.",
     key_held="DECODE HHStA Staatskanzlei Interiora Chiffrenschluessel fasc. 21-22 (records 1595-1612), Austrian keys 1740-49 for other envoys; none for Bernes or Weingarten, not tested.")

# ---------------- 2612 Neuchatel: Nr. 952
lead(2612,
     {"shelfmark": "GStA PK, I. HA Rep. 64 (Neuchatel), Nr. 952",
      "title": "Neuchatel succession: Frederick I's rescripts to Count Metternich, Jan-Oct 1709, 'teilsweise chiffriert mit gleichzeitiger Entschluesselung', Rep. 64 Nr. 952",
      "date": "1709", "year": 1709, "correspondents": "Frederick I of Prussia -> Count Ernst von Metternich (plenipotentiary in Switzerland and Neuchatel)",
      "folio_note": "Nr. 952 only (rescripts nos. 268-307 of 13 Jan-29 June 1709 and no. 308 of 26 Oct 1709). Sibling volumes of the old row, not part of this entry: Nr. 953 (Metternich's 1708 drafts, one fragment 'teils chiffriert'), 962 (Dupuy's papers with notes 'Verschluesselungen fuer die Chiffrierung'), 967 (Montmollin's letters 1711-13 'teilweise chiffriert mit gleichzeitiger Entschluesselung'), 992, 994 (Bondeli cipher numbers 176/177), 714, 724, 690. Nr. 722 and the other rows of the old grouping are separate."},
     ACTA % "I. HA Rep. 64 Nr. 952",
     "One volume of 1709: about 41 signed rescripts (nos. 268-308), some partly ciphered, with enclosures; leaves not counted (the volume's size is not in the record).",
     "Archive description, verbatim: 'Reskripte (Ausfertigungen, vom König eigenhändig unterschrieben; teilsweise chiffriert mit gleichzeitiger Entschlüsselung) vom 13. Januar 1709 bis zum 29. Juni 1709 (Nr. 268-307) und vom 26. Oktober 1709 (Nr. 308)'. The ciphertext and its simultaneous Entschluesselung are in the volume. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Neuchatel' and 'Neuchâtel' on 14 Nov 2026 (this session and the earlier Rep. 64 vetting): one picture postcard (record 3490), no GStA PK material; 'Metternich' not on DECODE for this file.",
      "tomokiyo": "Web search naming Cryptiana, Tomokiyo, Neuchatel and Metternich (14 Nov 2026): no Neuchatel item; the only Prussian Cryptiana item is Frederick I's transposition ciphertexts (DECODE), a different cipher system.",
      "lasry": "Search naming Lasry, Prussian diplomatic ciphers, Neuchatel and Rep. 64 (14 Nov 2026): nothing on this succession.",
      "edition": "Bachmann, Die preussische Sukzession in Neuchatel (1993) and Piaget 1933, cited by the HLS Metternich article, not opened; the 1709 rescripts are not known to be printed; Bourgeois 1887 stops at 1713 and was not opened.",
      "literature": "Web search on Metternich, the 1709 rescripts, Heinsius and Schmettau (14 Nov 2026): HLS and DDB finding-aid pages only; no work on the ciphered rescripts or their decipherment."},
     "No Neuchatel key is held here; the archive files a cipher table of 1703 in Rep. 64 Nr. 944 (lead 2495) and Bondeli cipher numbers in Nr. 994; nothing online, nothing tried.",
     "known.py 'Rep. 64', 'Neuchatel', 'Metternich' on 14 Nov 2026, and a number grep of 690, 714, 722, 724, 749, 756, 777, 798, 840, 846, 855, 952, 953, 962, 967, 992, 994 over catalogue.json and leads.json: no entry for Nr. 952; catalogue 2494, 2585 and leads 2495-2497, 2586-2587 are other volumes.",
     [{"query": "Metternich Neuchâtel 1709 Reskripte Friedrich I. chiffriert Entschlüsselung Heinsius Haager Friedenskonferenz Schmettau (web search)", "result": "HLS Metternich article, DDB/Archivportal-D finding aids; no edition or decipherment."},
      S_LAS1,
      {"query": "Cryptiana Tomokiyo Neuchâtel Prussia eighteenth century cipher Goltz OR Chambrier OR Metternich (web search)", "result": "Nothing on Neuchatel; one Cryptiana item on Frederick I's transposition ciphers."},
      {"query": "decode_search.py Neuchatel; Neuchâtel", "result": "One postcard (record 3490); no GStA PK holdings."}],
     key_in_volume="The Entschluesselung is written 'gleichzeitig' (at the same time) with the ciphered parts of the rescripts (per the archive description); not online, not tested.",
     key_held="GStA PK I. HA Rep. 64 Nr. 944 (cipher table sent 8 Nov 1703) and Nr. 994 (cipher numbers of 1705); not online, not tested.")

# ---------------- 2614 Neuchatel: Nr. 749
lead(2614,
     {"shelfmark": "GStA PK, I. HA Rep. 64 (Neuchatel), Nr. 749",
      "title": "Neuchatel administration 1723-24: unrest in Valangin, reports of Governor Froment and of Chambrier at Paris, 'gelegentlich chiffriert mit gleichzeitiger Entzifferung', Rep. 64 Nr. 749",
      "date": "1723-1724", "year": 1724, "correspondents": "Governor Froment and Prussian envoy Le Chambrier (Paris) -> the Berlin court (Ilgen, Knyphausen)",
      "folio_note": "Nr. 749 only (1723-24). Sibling volumes of the old row, not part of this entry: Nr. 798 (appointments 1719-24; one 'chiffrierter Teil ueber dominierende Familien' in Struenckede's report of July-Sept 1724), 756 (1726; one ciphered note of Desplasses to Bergeon), 777 (1742-48, Chiffrierung notes)."},
     ACTA % "I. HA Rep. 64 Nr. 749",
     "One volume of 1723-24 (6.5 cm class; the exact size is cut off in the record); ciphered passages in two groups of documents.",
     "Archive description, verbatim: 'Bemühungen des preußischen Gesandten Le Chambrier zwecks deren Ausweisung aus Frankreich ab Januar 1724 (gelegentlich chiffriert mit gleichzeitiger Entzifferung)' and 'Berichterstattung des Gouverneurs Froment ... (auch chiffriert mit gleichzeitiger Entzifferung)'. The ciphertext and its simultaneous Entzifferung are in the volume. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Neuchatel' and 'Neuchâtel' on 14 Nov 2026: one postcard (record 3490); no Froment, Chambrier or GStA PK records.",
      "tomokiyo": "Search for Cryptiana and Tomokiyo with Neuchatel, Chambrier and Prussian ciphers of the 1720s (14 Nov 2026): no item.",
      "lasry": "Search for Lasry with Prussian diplomatic ciphers and Rep. 64 (14 Nov 2026): no item on the Neuchatel files of 1723-24.",
      "edition": "No edition known: the HLS and BPUN searches (14 Nov 2026) returned local-history items on the Chambrier family and Lubieres; none prints the 1724 Paris reports.",
      "literature": "Web search 'Neuchatel 1724 Struenckede Valangin Bergeon Merveilleux Le Chambrier Paris Chiffren Froment' (14 Nov 2026): Neuchatel genealogy and Chambrier-family items; nothing on the ciphers or a decipherment."},
     "No Neuchatel or Froment key is held here; Rep. 64 Nr. 777 files Chiffrierung notes of 1742-48; not online, nothing tried.",
     "Number grep of Rep. 64 volumes over catalogue.json and leads.json on 14 Nov 2026: no entry for Nr. 749; catalogue 2494, 2585 and leads 2495-2497, 2586-2587 are other volumes.",
     [{"query": "Neuchâtel 1724 Strünckede Valangin Bergeon Merveilleux Le Chambrier Paris Chiffren Berichte Froment (web search)", "result": "Genealogy bulletins, HLS, Dupeyrou page; nothing on these reports or ciphers."},
      S_LAS1,
      {"query": "decode_search.py Neuchatel; Neuchâtel (second pass for Rep. 64 Nr. 749)", "result": "One postcard only."},
      {"query": "known.py 'Rep. 64' 'Neuchatel' 'Froment' 'Chambrier'", "result": "Only the volumes already catalogued or listed as leads 2494-2497, 2585-2587; none is Nr. 749."}],
     key_in_volume="Entzifferung written at the same time as the ciphered reports, in the same volume (per the archive description); not online, not tested.",
     key_held="GStA PK I. HA Rep. 64 Nr. 777 (Chiffrierung notes 1742-48); not online, not tested.")

# ---------------- 2615 Neuchatel Nr. 855
lead(2615, {},
     ACTA % "I. HA Rep. 64 Nr. 855",
     "One volume (5.5 cm), 1776-81: ciphered and deciphered reports of the Prussian envoy at Paris within a collection on the Swiss alliance of 1777; leaves not counted. The record notes 'Sperrung aus erschliessungstechnischen Gruenden' until 30.04.2026, now past.",
     "Archive description, verbatim: 'Haltung der katholischen Kantonen und des französischen Hofes (mit chiffrierten und entzifferten Berichten von Bernhard Wilhelm von der Goltz, Paris, 1780 und 1781; ...)'. Both the ciphertext and a deciphered version of Goltz's reports are in the volume. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Goltz Paris' and 'Zegelin' and 'Wedel' on 14 Nov 2026: no Goltz, Paris or GStA PK record; the Wedel hits are British Library Rantzau copies, unrelated.",
      "tomokiyo": "Search for Cryptiana and Tomokiyo with Goltz, Chambrier, Metternich and Neuchatel (14 Nov 2026): no item; only Frederick I's transposition ciphers.",
      "lasry": "No Lasry item on Goltz's Paris ciphers of 1780-81 in the 14 Nov 2026 search on Prussian diplomatic ciphers.",
      "edition": "The Politische Correspondenz (vols. 44-45, 1780-81, Trier edition) prints Frederick II's letters to Goltz at Paris, as the web search of 14 Nov 2026 shows by catalogue entries; Goltz's own reports to the king are not printed there (the PC prints the king's side, with notes). The Neuchatel file's reports were not matched against it.",
      "literature": "Web search on Goltz, 1780, the 1777 Swiss alliance and the Neuchatel clause (14 Nov 2026): only PC catalogue pages; no study of these despatches' ciphers."},
     "No Goltz key is held here; none was found online.",
     "Number grep over catalogue.json and leads.json on 14 Nov 2026: no entry for Rep. 64 Nr. 855; the same volume family is lead 2616 (Nr. 846, Goltz at Paris 1772) and catalogue 2494 (Nr. 828).",
     [{"query": "Goltz Paris 1780 Neuchâtel alliance Corps helvétique 1777 dépêches chiffrées déchiffrées Frédéric II (web search)", "result": "Only Trier PC catalogue pages for Frederick II's letters to Goltz (1777, 1780); nothing on ciphered reports."},
      {"query": "Cryptiana Tomokiyo Neuchâtel Prussia eighteenth century cipher Goltz OR Chambrier OR Metternich (web search)", "result": "Nothing on Neuchatel or Goltz."},
      {"query": "decode_search.py Goltz Paris; Zegelin; Wedel", "result": "No relevant record."}],
     key_in_volume="A deciphered version of Goltz's reports is filed with the ciphertext in the volume (per the archive description); not online, not tested.")

# ---------------- 2616 Neuchatel Nr. 846
lead(2616,
     {"shelfmark": "GStA PK, I. HA Rep. 64 (Neuchatel), Nr. 846",
      "title": "Neuchatel administration 1767-80: Goltz's 'teils chiffrierte Berichterstattung' of 1772-73 on the Doubs frontier, Rep. 64 Nr. 846",
      "date": "1772-1773", "year": 1772,
      "folio_note": "Nr. 846 only. Nr. 840 (1769-70) from the old row is not part of this entry: its note is an unread 'nicht entziffertes' remark on a title page, not a ciphered text. Nr. 855 is lead 2615."},
     ACTA % "I. HA Rep. 64 Nr. 846",
     "One volume, 1767-80; the ciphered part is Goltz's reporting of July 1772-Jan 1773 on the Doubs boundary incident; leaves not counted.",
     "Archive description, verbatim: 'Bearbeitung des Geschäftes im preußischen Hof (Denkschrift) und durch den Freiherrn von der Goltz (mit teils chiffrierter Berichterstattung), Juli 1772 - Januar 1773'. Whether a decipherment is filed is not stated. Leaf not seen: not digitised.",
     {"decode": "decode_search.py 'Neuchatel', 'Goltz Paris' on 14 Nov 2026: no relevant record.",
      "tomokiyo": "The Cryptiana and Tomokiyo search on Neuchatel, Goltz and Chambrier (14 Nov 2026) found no item for Goltz's 1772 reports.",
      "lasry": "No Lasry item on Goltz's despatches of 1772-73.",
      "edition": "The Politische Correspondenz prints Frederick II's letters to Goltz (Trier catalogue pages seen 14 Nov 2026), not Goltz's own reports; the 1772-73 volumes were not opened; no printed decipherment of these reports is known.",
      "literature": "known.py and the Goltz web search of 14 Nov 2026 found no study of Goltz's 1772 reports; no literature on their ciphers is known."},
     "No key is held here. Whether the Paris cipher of 1772 equals Goltz's of 1780 (lead 2615) is unchecked: keys are not online.",
     "Number grep over catalogue.json and leads.json on 14 Nov 2026: no entry for Nr. 846 or 840; Nr. 855 is lead 2615.",
     [{"query": "Goltz Paris 1780 Neuchâtel alliance Corps helvétique 1777 dépêches chiffrées déchiffrées Frédéric II (web search)", "result": "PC catalogue pages for letters to Goltz; nothing on Neuchatel reports."},
      {"query": "known.py 'Goltz' 'Doubs' 'Neuchatel' over the ledgers", "result": "No entry for this volume; Goltz appears only in lead 2615 and the catalogue 2494 notes."},
      {"query": "decode_search.py Neuchatel; Goltz Paris (Rep. 64 Nr. 846)", "result": "One postcard (record 3490); no Goltz or GStA PK record."}])

# ---------------- 2617 Frankfurt: Nr. 173
lead(2617,
     {"shelfmark": "GStA PK, I. HA Rep. 81 (Frankfurt a. M. / Rheinbund), Nr. 173",
      "title": "Prussian legation at Frankfurt (Confederation of the Rhine): royal orders and reports Jan-July 1813, 'chiffrierte Schreiben mit Aufloesung', Rep. 81 Frankfurt Nr. 173",
      "date": "1813", "year": 1813,
      "folio_note": "Nr. 173 only (Bd. 7, Jan-July 1813, 163 leaves; ff. 164-170 were moved in 1973 to Rep. 81 Kassel Lit. C Tit. I Nr. 1 Bd. 6). Siblings with the same kind of note, not part of this entry: Nr. 167 (1809, 'Chiffrierte Erlasse mit Aufloesungen durch die Gesandtschaft'), 171 (1811, 'Chiffren sind von der Gesandtschaft aufgeloest'); Nr. 168 (1810) carries no cipher note in the part read. Nr. 167, 171 and 173 are 'nicht vorlegbar' until 31.05.2029 (store repair)."},
     ACTA % "I. HA Rep. 81 Frankfurt a.M./R. Nr. 173",
     "One volume of 163 leaves, Jan-July 1813; the record does not say how many letters are ciphered.",
     "Archive description, verbatim: 'Akte nicht geheftet; chiffrierte Schreiben mit Auflösung; Folio 164 bis 170 wurden 1973 entnommen ...'. The ciphertext and the legation's Auflösung are in the file. Leaf not seen: not digitised and not orderable until 31.05.2029.",
     {"decode": "decode_search.py 'Frankfurt Rheinbund' and 'Zegelin' on 14 Nov 2026: 0 records; no GStA PK Frankfurt material.",
      "tomokiyo": "Search naming Cryptiana, Tomokiyo and Prussian diplomatic ciphers of 1813 (14 Nov 2026): no Cryptiana item on Napoleonic-era Prussian ciphers.",
      "lasry": "Same search for Lasry: his Cryptologia 2021 paper covers 1900-15 only; nothing on 1813.",
      "edition": "No edition of the Frankfurt legation's orders found: the web search of 14 Nov 2026 turned up only archive finding aids and a Dalberg finance file; the Prussian foreign-ministry orders of 1813 may sit in Oncken or Ranke editions, which were not opened.",
      "literature": "Web search on the Prussian envoy at Frankfurt 1813 and ciphered orders (14 Nov 2026): nothing on these ciphers or a decipherment."},
     "No key is held here; the Prussian cipher keys of 1806-19 are listed in the 14 Nov key_leads.json (Rep. 11 Nr. 10696 and others), not online, none tried.",
     "known.py 'Frankfurt' and 'Rheinbund' plus a number grep on 14 Nov 2026: no entry for Rep. 81 Frankfurt Nr. 167-173; the Mainz and Kassel files in leads 1672-1673 are other fonds.",
     [{"query": "preußischer Gesandter Frankfurt Fürstprimas Dalberg 1813 chiffrierte Erlasse Gesandtschaft Rheinbund Immediatberichte Quellenedition (web search)", "result": "Finding aids (Rep. 81 Darmstadt, DDB), a Dalberg finance file; no edition or decipherment."},
      {"query": "Napoleonic era Prussian diplomatic cipher 1813 deciphered despatches Frankfurt legation Lasry OR Tomokiyo OR Cryptologia (web search)", "result": "Lasry/Tomokiyo/Biermann 17th-century work, Scovell and Peninsular items; nothing on Prussian 1813."},
      {"query": "decode_search.py Frankfurt Rheinbund; Zegelin", "result": "0 records found on DECODE."}],
     key_in_volume="The legation's Auflösung is filed with the ciphered letters (per the archive description); not online, not tested.")

# ---------------- 2626 OBA 23682
lead(2626, {},
     ACTA % "XX. HA, OBA, Nr. 23682",
     "One letter of 10 May 1520 with its Aufloesung; leaf count not stated.",
     "Archive description, verbatim: 'Markgraf Kasimir an Hochmeister: seine Hülfe für diesen. Wolf v. Schönburg. Franz von Sickingen. D. v. Schönberg. Original in Chiffern; mit Auflösung. --- Zeitz 1520 Donnerstag nach Cantate.' Leaf not seen: not digitised in the record.",
     {"decode": "decode_search.py 'Kasimir Ansbach', 'Schoenberg' and 'Schönberg Albrecht' on 14 Nov 2026: 0 records.",
      "tomokiyo": "Web search naming Hochmeister Albrecht, Kasimir, Schoenberg, Klingenbeck and Chiffrenbrief (14 Nov 2026): no Cryptiana item; one Neues Archiv fuer saechsische Geschichte article on a cipher of a Margrave Albrecht, not this letter.",
      "lasry": "Search naming Lasry with the Teutonic Order's Grand Master Albrecht and ciphers (14 Nov 2026): no item.",
      "edition": "Joachim, Die Politik des letzten Hochmeisters vol. 2 (Internet Archive diepolitikdeslet02joac, OCR searched 14 Nov 2026): no letter headed Zeitz with a 1520 date found, so this letter is not printed there as far as the OCR shows; Joachim's convention is that italics mark deciphered passages (vol. 1 p. 237, per catalogue 553).",
      "literature": "Web search in German on Kasimir's cipher letter of 1520 (14 Nov 2026): ADB and Deutsche Biographie pages on Kasimir; nothing on ciphers."},
     "Kasimir's own cipher alphabet is requested in OBA 23213 (lead 2595); the Auflösung filed with this letter is the key evidence. Nothing is online, nothing was tried.",
     "known.py '23682', 'Kasimir', 'Joachim' on 14 Nov 2026 and number grep: no entry; catalogue 553-557 hold other OBA numbers (Schoenberg, Joachim I, Heydeck, Gundelfinger); leads 2505 and 2595 are other OBA letters.",
     [{"query": "Hochmeister Albrecht von Brandenburg Chiffre Briefe 1520 Markgraf Kasimir Schönberg Klingenbeck Chiffrenbrief Entzifferung (web search)", "result": "ADB/Deutsche Biographie on Kasimir; one Saxon-history journal article on a Margrave Albrecht's cipher; nothing on this letter."},
      {"query": "Joachim vol. 2 OCR (diepolitikdeslet02joac_djvu.txt): 'Zeitz' with 1520 and 'Kasimir' headings", "result": "Two 'Zeitz' hits, neither a letter of Kasimir of 10 May 1520."},
      {"query": "decode_search.py Kasimir Ansbach; Schoenberg; Schönberg Albrecht", "result": "0 records found on DECODE."}],
     key_in_volume="'mit Auflösung': the Auflösung is filed with the ciphered original (per the archive description); not online, not tested.",
     key_held="OBA Nr. 23213 (Kasimir's cipher alphabet requested; lead 2595) and Nr. 27584 (the chancery's Chiffrenbuch, key_leads.json); not online, not tested.")

# ---------------- 2627 Klingenbeck: Nr. 27533 only
lead(2627,
     {"shelfmark": "GStA PK, XX. HA, OBA, Nr. 27533",
      "title": "Georg Klingenbeck at the imperial court (Madrid) to Grand Master Albrecht, 19 Feb 1525: three letters, one 'in Chiffern mit Aufloesung', OBA 27533",
      "date": "1525", "year": 1525,
      "folio_note": "OBA 27533 only (19 Feb 1525, Madrid; 3 letters and a note, one in cipher with Auflösung). OBA 27275 (9 Oct 1524, 'teilweise Chiffern') was already lead 2505 and is not part of this entry."},
     ACTA % "XX. HA, OBA, Nr. 27533",
     "Three letters and one slip of 19 Feb 1525; one letter is the cipher with its Aufloesung.",
     "Archive description, verbatim: '3 Briefe (einer in Chiffern mit Auflösung) und 1 Zettel. --- Madrid am kaiserl. Hoflager 19. Febr. 1525.' (head: Klingenbeck's observations at the imperial court, Hannart, the Polish embassy, Schoenberg). Leaf not seen: not digitised in the record.",
     {"decode": "decode_search.py 'Klingenbeck' on 14 Nov 2026: 0 records.",
      "tomokiyo": "The Teutonic Order and Cryptiana/Cryptologia/HistoCrypt search (14 Nov 2026): no Cryptiana item on Klingenbeck or Albrecht's chancery.",
      "lasry": "Same search for Lasry and HistoCrypt: only Wallenstein and 1637 Oxenstierna items; nothing on Albrecht's cipher letters.",
      "edition": "Joachim, Politik des letzten Hochmeisters vol. 3 (Internet Archive diepolitikdeslet03joac, OCR searched 14 Nov 2026) lists 'Klingenbeck an HM. Madrid 19. Februar 1525. D. 534' among its sources; the passage seen is a source list, so a printed text or decipherment of the cipher letter is neither shown nor excluded.",
      "literature": "Web search on Klingenbeck and the 1525 mission to Charles V (14 Nov 2026): no study of the cipher."},
     "Klingenbeck's cipher is not held; the chancery's Chiffrenbuch OBA 27584 (key_leads.json) is the nearest key; nothing online, nothing tried.",
     "Lead 2505 holds OBA 27275 of the same writer; catalogue 553-557 hold other OBA numbers; no entry for 27533 (known.py 'Klingenbeck', '27533' on 14 Nov 2026).",
     [{"query": "Teutonic Order Grand Master Albrecht 1520s ciphered letters decipherment Cryptologia OR Cryptiana OR HistoCrypt (web search)", "result": "Wallenstein, Oxenstierna 1637 and other items; nothing on Albrecht's ciphers."},
      {"query": "Joachim vol. 3 OCR: 'Klingenbeck' with 1524/1525", "result": "Source-list citations including Madrid 19 Feb 1525 (D. 534); no text of the cipher letter seen."},
      {"query": "decode_search.py Klingenbeck", "result": "0 records found on DECODE."}],
     key_in_volume="'in Chiffern mit Auflösung': the Auflösung is filed with the cipher letter (per the archive description); not online, not tested.",
     key_held="OBA Nr. 27584 (Chiffrenbuch of Dietrich v. Schoenberg and the chancery, key_leads.json); not online, not tested.")

# ---------------- unvetted
UN = {
"2601": "Rep. 96 Nr. 97 E 1 and F: the records list 'Dechiffrierungscodes, [1745]' among war correspondence with Leopold I of Anhalt-Dessau, but name no ciphered letter; a code without ciphertext is a key lead (key_leads.json), not yet a cipher lead. Needs the volumes seen.",
"2602": "Nl Wedel Nr. 3: record says '40 Kabinettsordres, fünf Abschriften (Dechiffrierungen) und zwei Einzelschreiben', 98 leaves; it does not say which orders are ciphered, and the 1759 orders to Wedel are in the Politische Correspondenz vol. 18 (not opened). Check the PC before an entry.",
"2603": "Rep. 96 Nr. 90 G: the record lists 'Geheimcodes (Chiffres) mit Schmettau, 1759', a code and no ciphertext; the volume is Schmettau's Dresden capitulation papers. Key only.",
"2604": "Rep. 96 Nr. 85 Oo: 'Dechiffrierte Nachrichten' of Dohna, 1756-59: deciphered texts only, no ciphertext named. EM 19 c3 Nr. 14 not fetched.",
"2605": "Rep. 34 Nr. 6676: 'Dechiffrierungen von Briefen des de Beziers, 1668', enclosed with Copes's reports from The Hague; the record names the decipherments only. Whether ciphertext is filed is not stated.",
"2606": "BPH Rep. 35 Nr. 15: the full record did not come back in the search lists this session (the header was not in the hit set); only the sweep's quoted line is known. Re-fetch and check Urkunden und Actenstuecke before an entry.",
"2607": "Rep. 11 Akten Nr. 10691: the record reads 'Schriftwechsel mit dem Oberst Graf von Lusi (Abschriften und Dechiffrierungen)' and nothing on ciphertext; the ciphertext side is FA Lusi Nr. 3 (lead from the previous sweep).",
"2608": "Nl Schlitz v. Goertz: four letters from four writers (Blumenthal 1786, Wilhelmine 1786, Thulemeier 1787, Goertz 1790); the records are summaries of mostly plain French letters that mention ciphers, and Nr. 8 says 'Der Rest ist nicht dechiffrierbar'. No single cipher; one lead per letter and key would be needed, and no ciphertext leaf is described. Left unvetted.",
"2609": "Rep. 96 Nr. 206 K: the full record did not come back in the hit set; one leaf, 'Verschluesseltes Schreiben des Herrn Hohenfels, 15. Mai 1785'. Re-fetch before an entry.",
"2610": "Rep. 400 Nr. 191: a facsimile (1986 exhibition item) of Count Esterhazy's ciphered report of 6 Apr 1756 from the HHStA (StA Russland II Kt. 37 ff. 11-12); not orderable until 31.05.2029. The original is in Vienna and the report reached the Prussian side through Menzel and Weingarten; look for a reading in the Vienna copy and in the Seven Years' War literature before any entry.",
"2611": "Rep. 94 A V Nr. 26, document 5: Frederick II's order of 19 Nov 1775 to Zegelin is 'zum größten Teil chiffriert (Dechiffrierung ist überschrieben)', so a decipherment is written over the leaf; it is one sheet in a collection and the PC (vols. after 36) was not reachable. Not an open lead as it stands.",
"2613": "Rep. 64 Nr. 722: the full record did not come back in the hit set; the sweep quotes only an 'entchiffrierte' intercepted letter of 11 July in a wine-dispute file. Re-fetch before an entry.",
"2618": "Nl Gruner Nr. 57-58: titles are 'Depeschen auswärtiger Gesandter (Dechiffrements und Abschriften, Sammlung von Justus v. Gruner)', eleven and four named senders; the record shows deciphered copies, not that ciphertext is filed, and each envoy had his own key. Split one lead per envoy only after the volumes are seen.",
"2619": "Rep. 77 Tit. 437 Nr. 6 (1815-33): 'Dechiffrierung der von den Franzosen zu geheimen Korrespondenzen gebrauchten Chiffren'; the Beiheft is a printed 1810 book on cryptography (Tritheim, 'Vollständiges System der Geheimlese'), not a cipher. Ciphertext and decipherments are not itemised; needs the file seen.",
"2620": "Rep. 7 C Nr. 3144-3145: Nr. 3145 is 'Einige Schlüssel zu den ... Chiffres' of the revolutionary Poles (keys, no ciphertext), Nr. 3144 an 'Versuch der Entzifferung' of a ring inscription; no ciphered letter is named. Key lead.",
"2621": "Rep. 81 Bern Nr. 93: the title is 'Dechiffrierte Berichte des Geschäftsträgers von Olfers an den Staatsminister Ancillon' (1833-34): deciphered reports; the record does not say the ciphertext is filed; not orderable until 31.05.2029.",
"2622": "Nl Miltitz II Nr. 26: 'Lord Strangford an von Miltitz (Briefe)' with '2 Schlüssel zu Chiffern'; no ciphered letter is named. Key lead.",
"2623": "Westphalen Nr. 461: the full record did not come back in the hit set; the sweep quotes 'z. T. verschluesselte Berichte'. Re-fetch before an entry.",
"2624": "Rep. 89 Nr. 666: the cipher mention is deep in a long contents list ('Chiffre zur geheimen Korrespondenz zwischen Wilhelm II. und Sultan ...'), cut off in the part read; the record names a cipher, not ciphertext. Read the whole record first.",
"2625": "OBA, eleven Schoenberg to Albrecht letters 1519-23 'mit Auflösung': OBA 26245 (11 July 1523) is printed in Joachim, Politik des letzten Hochmeisters vol. 3 as Nr. 110 'Chiffrirter Beibrief' with its German text (OCR of 14 Nov 2026, so that letter is read in print); the 1522 letters of 16 Jan and 12 Feb are cited only in Joachim's source lists, and 3 Jan and 20 Jan 1520 only in vol. 2's. Check each of the other ten in Joachim vols. 2-3 (OCR in the session scratch) and split the rest by key year (1519-20, 1522, 1523) before an entry; catalogue 553 already holds Schoenberg letters without Auflösung.",
}
for k, v in UN.items():
    out[k] = {"unvetted": v}
json.dump(out, open(os.path.join(HERE, 'vetting.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
