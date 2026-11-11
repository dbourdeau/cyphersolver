# Builds candidates.json for the 11 Nov 2026 printed-series sweep. Rows were read by hand from the printed editions.
import json

TODAY = "2026-11-11"
BY = "claude cloud sweep 11 Nov printed_series"
PRIB = "https://archive.org/details/bub_gb_oIkJAAAAIAAJ"
PRIB_TXT = "https://archive.org/download/bub_gb_oIkJAAAAIAAJ/bub_gb_oIkJAAAAIAAJ_djvu.txt"
SRC = "printed series sweep (archive.org full text)"
AIS = "https://www.archivinformationssystem.at/detail.aspx?ID=%d"

S_DECODE = {"query": "DECODE RecordsList search 'Lisola'; 'Polen I'; 'Polonica'",
            "result": "Lisola: R1915-R1918 and R2040 only (Geheime Staatsregistratur 61 fasc. 46, 1669-74); 'Polen I' and 'Polonica': 0 records."}
S_AIS = {"query": "AIS (archivinformationssystem.at) full text: 'Lisola 1657', 'Lisola Polen', 'Lisola 1656', 'Lisola Chiffre', 'Lisola Chiffrenschlüssel'",
         "result": "No item-level record of these reports and no key under Lisola's name; StAbt Polen I is described by Karton only (IDs 227463-227553 walked)."}
S_W1 = {"query": "Lisola Berichte 1657 chiffriert \"nicht dechiffrirt\" Pribram Chiffre entziffert Polonica Haus-, Hof- und Staatsarchiv",
        "result": "NDB entry and Pribram's 1887 edition only; HistoCrypt and Cryptologia hits concern other Habsburg ciphers (Ferdinand III, key instructions); no decipherment of a Lisola report."}
S_W2 = {"query": "Lisola 1657 Königsberg Wehlau relation cipher deciphered Leopold \"Lisola\" cryptology HistoCrypt OR Cryptologia OR cryptiana",
        "result": "Nothing on Lisola; only Ernst's Zifra Piccolominea (1640-41) and a Cryptologia paper citing a 1657 HHStA key (DECODE R1280, no name on it)."}
S_W3 = {"query": "Franz von Lisola Dankow 3 Juni 1657 Bericht Kaiser Karl Gustav Schlippenbach edition \"Lisola\" Wójcik OR Kubala relacje Lisoli szyfr",
        "result": "No Polish or other edition of the report found; pamphlets from Dankow of May 1657 and general Northern War pages only."}
S_W4 = {"query": "Lisola Bericht Warschau 3. März 1656 Karl Gustav Pöttingen chiffriert Relation entziffert",
        "result": "Only citations of Pribram's edition (AÖG 70) and his 1894 biography; nothing on the report of 3 March 1656 or its cipher."}
S_W5 = {"query": "Lisola Königsberg 4 September 1657 Bericht Leopold Wehlau Gonsiewski \"Lisola\" Chiffre ungelöst OR dechiffriert OR deciphered Polen I HHStA",
        "result": "Nothing on the Königsberg reports of September 1657; the same Cryptologia citation of an unnamed 1657 HHStA key."}


def lisola(year, date, place, no, page, karton, ais_id, krange, extent, quote, subject, searches, imp, vet=True, extra_verify=""):
    row = {
        "year": year, "date": date,
        "title": "Franz Paul von Lisola → %s, %s: report with cipher the editor found not deciphered (Pribram no. %s)" % (
            {1656: "Ferdinand III", 1657: "Leopold, King of Hungary and Bohemia"}.get(year, "Leopold I"), place, no),
        "correspondents": "Franz Paul von Lisola (imperial envoy) → the Emperor / court of Vienna",
        "place": place, "language": "Latin", "region": "Central Europe", "period": "1651-1700",
        "shelfmark": "Vienna, ÖStA HHStA, Staatenabteilungen, Polen I (Polonica), Karton %s (%s): Lisola's report of %s; printed in part by Pribram, Archiv für österreichische Geschichte 70 (1887), no. %s" % (karton, krange, date, no),
        "folio_note": "%s (Pribram p. %s). The Karton is assigned from the AIS date ranges; the report is not itemised in the AIS and Pribram gives no folio." % (extent, page),
        "cls": "A",
        "status": "Pribram printed the report from the original in the Vienna Staatsarchiv and notes: \"%s\". The clear and contemporaneously deciphered parts are printed; the passages he names had no decipherment with them. Not on DECODE (searched 11 Nov 2026)." % quote,
        "why": subject,
        "importance": imp, "solvability": 2, "difficulty": 3,
        "score_note": "Scored from the printed edition during the 11 Nov 2026 printed-series sweep (research/sweep_2026-11-11_printed_series/); original not viewed",
        "verify": "Order the leaf from HHStA (Polen I Karton %s; if not there, Brandenburgica or Suecica of the same months%s). Lisola's other reports of 1655-60 in the same Kartons carry contemporary decipherments (Pribram prints them between asterisks), so the key can be rebuilt from siblings." % (karton, extra_verify),
        "links": [{"label": "AIS: HHStA StAbt Polen I %s" % karton, "href": AIS % ais_id},
                  {"label": "Pribram 1887 (AÖG 70), scan", "href": PRIB + "?q=dechiffrirt"},
                  {"label": "Pribram 1887, OCR text", "href": PRIB_TXT}],
        "seen": "catalogue", "source": SRC,
        "prior_art": "open (checked 11 Nov 2026: Pribram's edition opened and says not deciphered; DECODE, cryptiana, web searches)",
        "needs_archive_scan": "yes",
        "access_note": "Not digitised: HHStA reading room or a scan order; Karton-level record only.",
    }
    if vet:
        row["vetting"] = {
            "date": TODAY, "by": BY,
            "seen": {"kind": "not online",
                     "where": "Pribram, Die Berichte des kaiserlichen Gesandten Franz von Lisola 1655-1660, AÖG 70 (1887), no. %s, p. %s (archive.org bub_gb_oIkJAAAAIAAJ and bub_gb_tZ_NAAAAMAAJ, OCR read 11 Nov 2026); original HHStA StAbt Polen I %s, not online" % (no, page, karton),
                     "extent": extent,
                     "cipher": "No archive description at item level exists (AIS lists the Karton only). The editor, who worked from the original, describes it: \"%s\". Cipher system not stated; Pribram marks ciphered passages of sibling reports with asterisks and prints their decipherments." % quote},
            "prior_art": {
                "decode": "DECODE RecordsList searched for Lisola, 'Polen I' and Polonica on 11 Nov 2026: only R1915-R1918 and R2040 (Lisola 1669-74, Geheime Staatsregistratur); no record of this %s report." % date,
                "tomokiyo": "cryptiana index and variable3.htm read: Lisola appears only as a name inside a c. 1657-59 Porcia key (Chirtulov's reading); no page on Lisola's own reports of %d." % year,
                "lasry": "No Lasry paper on Lisola or the imperial envoys' ciphers of 1655-60 came up in the web searches; nothing in the repo's notes (known.py 'Lisola').",
                "edition": "Pribram 1887 is the edition and was opened at no. %s: it prints the readable text and states the passage is not deciphered. Urkunden und Actenstücke VIII (cited by Pribram for the same weeks) prints Brandenburg and French papers, not this report." % no,
                "literature": "Web searches on the report (place, date, cipher) returned only Pribram's edition and his 1894 biography; no HistoCrypt or Cryptologia study of Lisola's 1655-60 cipher."},
            "key_check": "No key for Lisola's 1655-60 cipher is held in the repo or named on DECODE. Nothing could be tested because no ciphertext is online.",
            "key_held": "Imperial keys of the period exist on DECODE (HHStA Staatskanzlei Interiora Chiffrenschlüssel, e.g. R1280, undated homophonic key with nomenclator) and Lisola's own later ciphers (R1915-R1918, R2040); none identified as his 1655-60 key, none tested.",
            "duplicates": "known.py 'Lisola', 'Pribram', 'Polen I', 'Polonica': catalogue entries for Lisola 1643 and 1667 (Spanien Varia / 20-4-10) and DECODE 1669-74 only; no entry, lead or target for the 1655-60 reports.",
            "verdict": "open",
            "searches": searches,
        }
    return row


rows = [
    lisola(1657, "3 Jun 1657", "Dankow", "LX", "284-285", "69", 227534, "02.1657-08.1657",
           "About one and a half pages and two lines of cipher without decipherment, in three places of the report",
           "Zum Theile nicht dechiffrirt ... Folgt eine halbe Seite nicht dechiffrirt ... Folgt ungefähr eine nicht dechiffrirte Seite ... Folgen zwei Zeilen nicht dechiffrirt",
           "Lisola's assessment of Charles X Gustav's plans after the Danish declaration of war, days after the Austro-Polish alliance: the unread passages follow his forecast of a Swedish strike through Silesia.",
           [S_W1, S_W3, S_DECODE, S_AIS], 4),
    lisola(1657, "4 Sep 1657", "Königsberg", "LXXV", "316", "70", 227535, "09.1657-03.1658",
           "Two and a half pages of cipher without decipherment",
           "2 1/2 Seiten nicht dechiffrirt",
           "Lisola's mediation of the Treaty of Wehlau between Poland and Brandenburg, in the last days before signature (the treaty gave the Elector sovereignty in Ducal Prussia).",
           [S_W5, S_W2, S_W1, S_DECODE, S_AIS], 4, extra_verify="; the Königsberg reports may be filed with Brandenburgica"),
    lisola(1657, "11 Sep 1657", "Königsberg", "LXXVI", "317", "70", 227535, "09.1657-03.1658",
           "One further page of cipher without decipherment at the end of the report",
           "Folgt noch eine nicht dechiffrirte Seite",
           "Report on the conclusion of the Wehlau treaty (8 Sept.) and the war plans agreed with the Elector and Gosiewski; the last page is unread.",
           [S_W5, S_W2, S_W1, S_DECODE, S_AIS], 4, extra_verify="; the Königsberg reports may be filed with Brandenburgica"),
    lisola(1656, "3 Mar 1656", "Warsaw", "XXIX (note)", "148", "66", 227531, "12.1655-04.1656",
           "A whole report, length not given",
           "Ein Bericht vom 3. März ist nicht dechiffrirt",
           "Lisola with Charles X Gustav in occupied Warsaw during the imperial mediation attempt; the report of the day before the printed one of 4 March was left out because it is in cipher.",
           [S_W4, S_W1, S_DECODE, S_AIS], 3, extra_verify="; Lisola was accredited to the Swedish king, so Suecica is possible"),
    lisola(1660, "6 Feb 1660", "Danzig", "CLX", "547", "74", 227539, "07.1659-02.1660",
           "One passage of cipher without decipherment, length not given",
           "Folgt eine nicht dechiffrirte Stelle",
           "Oliva peace congress: Lisola on intercepted evidence of Swedish designs; one passage unread.",
           [], 3, vet=False),
]

UA = "https://archive.org/details/%s"


def lead(year, date, title, corr, place, lang, region, shelf, folio, status, why, imp, solv, verify, links, access, cls="C"):
    return {"year": year, "date": date, "title": title, "correspondents": corr, "place": place, "language": lang,
            "region": region, "period": "1651-1700", "shelfmark": shelf, "folio_note": folio, "cls": cls, "status": status,
            "why": why, "importance": imp, "solvability": solv, "difficulty": 3,
            "score_note": "Scored from the printed edition during the 11 Nov 2026 printed-series sweep (research/sweep_2026-11-11_printed_series/); not viewed",
            "verify": verify, "links": links, "seen": "catalogue", "source": SRC,
            "prior_art": "edition opened (says not deciphered); DECODE searched by name, 0 records; no web search run for this row, so no vetting block",
            "needs_archive_scan": "yes", "access_note": access}


rows += [
    lead(1666, "8/18 Oct 1666", "Christoph von Brandt → Elector Frederick William, London: full relation of his audience with Charles II, almost all in cipher, not deciphered",
         "Christoph von Brandt (Brandenburg envoy) → Frederick William, Elector of Brandenburg", "London", "German", "Germany",
         "Berlin, GStA PK, I. HA Geheimer Rat, Rep. 11 Auswärtige Beziehungen (England), relation of 8/18 Oct 1666; unit number not given by the edition (Urkunden und Actenstücke XII, 1892, p. 637 n. 1)",
         "One relation, 'fast ganz in Chiffern'",
         "Editor (Brode, UA XII p. 637): \"Die ausführliche Relation über diese Audienz vom 8./18. October ist fast ganz in Chiffern geschrieben und nicht dechiffriert.\" A short clear relation of the same day is printed.",
         "Brandenburg's attempt to mediate in the Second Anglo-Dutch War; the envoy's full account of Charles II's words survives only in cipher.", 4, 2,
         "Find the unit in the GStA database (Rep. 11 England, Brandt's mission 1666) and order scans; the printed short relation and Pufendorf X § 21 are cribs.",
         [{"label": "UA XII (archive.org), search 'nicht dechiffriert'", "href": UA % "urkundenundacten12berluoft" + "?q=dechiffriert"}],
         "GStA PK Berlin, not digitised", cls="B"),
    lead(1662, "26 May 1662", "Johann von Hoverbeck → Elector Frederick William, Warsaw: relation mostly in unresolved cipher",
         "Johann von Hoverbeck (Brandenburg resident) → Frederick William, Elector of Brandenburg", "Warsaw", "German", "Germany",
         "Berlin, GStA PK, I. HA Geheimer Rat, Rep. 9 Polen, Hoverbeck's relation of 26 May 1662; unit number not given by the edition (Urkunden und Actenstücke IX, 1879, p. 352)",
         "One relation, 'meist unaufgelöste Chiffern'; several lines more in his relations of spring 1662 (UA IX pp. 330, 351)",
         "Editor (Hirsch, UA IX p. 352), heading of the Elector's answer of 28 May/7 Jun 1662: \"Auf die Relation vom 26. Mai, meist unaufgelöste Chiffern\". Other Hoverbeck relations are printed with the cipher resolved.",
         "Polish royal succession intrigues and the Lauenburg-Bütow question in 1662, from the Elector's long-serving resident.", 3, 2,
         "Find the unit in the GStA database (Rep. 9 Polen, 1662) and order scans; sibling relations with resolved cipher give the key.",
         [{"label": "UA IX (archive.org), search 'unaufgelöste'", "href": UA % "urkundenundacten09berluoft" + "?q=unaufgel%C3%B6ste"}],
         "GStA PK Berlin, not digitised", cls="A"),
    lead(1661, "20 May 1661", "Prince Johann Moritz of Nassau and Daniel Weiman → Elector Frederick William, London: relation mostly in unresolved cipher",
         "Johann Moritz of Nassau-Siegen and Daniel Weiman (Brandenburg ambassadors) → Frederick William, Elector of Brandenburg", "London", "German", "Germany",
         "Berlin, GStA PK, I. HA Geheimer Rat, Rep. 11 Auswärtige Beziehungen (England), embassy of 1661, relation of 20 May 1661; unit number not given by the edition (Urkunden und Actenstücke IX, 1879)",
         "One relation, 'meist in unaufgelösten Chiffern'",
         "Editor (Hirsch, UA IX), heading of the Elector's answer, Cleve 25 May 1661: \"Auf die Relation vom 20. Mai: meist in unaufgelösten Chiffern\". Weiman's journals (then in the Düsseldorf archive) cover the same embassy in clear.",
         "The Brandenburg embassy to Charles II on the Orange guardianship and the 1661 alliance treaty.", 3, 2,
         "Find the unit in the GStA database (Rep. 11 England 1661); Weiman's journal (Landesarchiv NRW) is a crib.",
         [{"label": "UA IX (archive.org), search 'unaufgelösten'", "href": UA % "urkundenundacten09berluoft" + "?q=unaufgel%C3%B6sten"}],
         "GStA PK Berlin, not digitised", cls="B"),
    lead(1685, "17 Sep 1685", "Baron Fridag → Emperor Leopold I, Berlin: original report with a long passage not deciphered",
         "Franz Heinrich von Fridag (imperial envoy in Berlin) → Leopold I", "Berlin", "German", "Central Europe",
         "Vienna, ÖStA HHStA, Staatenabteilungen, Brandenburgica, Fridag's report of 17 Sept 1685 (Or.); Karton not given by the edition (Urkunden und Actenstücke XIV/2, 1891, p. 1186 n. 1)",
         "'ein längerer nicht dechiffrirter Passus'",
         "Editor (Pribram, UA XIV/2 p. 1186): \"Auf diese Stelle folgt ein längerer nicht dechiffrirter Passus, der, wie zu ersehen, von der Stellung Brandenburgs zu den verschiedenen Grossstaaten Europas handelt.\"",
         "The Great Elector's position between the Emperor and France weeks before the Edict of Potsdam, as reported by the imperial envoy.", 4, 2,
         "Locate the Brandenburgica Karton for 1685 in the AIS (StAbt Brandenburgica is listed by Karton) and order the leaf; Fridag's other reports in UA XIV/2 are printed with cipher resolved.",
         [{"label": "UA XIV/2 (archive.org), search 'dechiffrirter'", "href": UA % "pt2urkundenundac14berl" + "?q=dechiffrirter"}],
         "HHStA Vienna, not digitised", cls="A"),
    lead(1667, "27 Jul and 24 Aug 1667", "Millet → Lionne, Berlin: two despatches for the most part not deciphered",
         "Guillaume Millet de Jeurs (French envoy in Berlin) → Hugues de Lionne", "Berlin", "French", "France",
         "Paris, Archives du ministère des Affaires étrangères, Correspondance politique, Brandebourg (Prusse), 1667: Millet's despatches of 27 July and 24 Aug 1667; volume not given by the edition (Urkunden und Actenstücke II, 1865, pp. 460, 468)",
         "Two despatches; 'grösstentheils undechiffrirt' and 'zum grossen Theil nicht dechiffrirt'",
         "Editor (Simson, UA II): 27 July 1667 \"Grösstentheils undechiffrirt\"; 24 Aug 1667 \"Zum grossen Theil nicht dechiffrirt. Vgl. Mignet II p. 285\". The printed text is the clear part only. Lionne's office normally deciphered incoming despatches, so a decipherment may lie elsewhere in the volume. DECODE has two Millet letters of 1665 from Poland (R2679, R2681, Mélanges de Colbert), a different mission.",
         "French soundings of the Great Elector during the War of Devolution (Rhine alliance, the offer of Guelders, the Polish crown).", 3, 2,
         "Check the AAE volume (Correspondance politique Brandebourg vol. for 1667; many CP volumes are online at the AAE reading-room site) for a marginal decipherment; Mignet, Négociations relatives à la succession d'Espagne II p. 285 prints an extract.",
         [{"label": "UA II (archive.org), search 'dechiffrirt'", "href": UA % "urkundenundacten02berluoft" + "?q=dechiffrirt"}],
         "AAE La Courneuve; digitisation of this volume not checked", cls="B"),
]

json.dump(rows, open("candidates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), sum(1 for r in rows if "vetting" in r))
