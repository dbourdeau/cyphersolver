"""Write proposals.json for wave 20 batch 16 (16 Nov 2026). python -I -X utf8 make_proposals.py"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BY = 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting'
TOMO = ("Tomokiyo's list of unsolved ciphers (cryptiana unsolved.htm, fetched 15 Nov 2026) grepped for %s: no entry; "
        "its only Chinese entries are unrelated later telegrams.")
LASRY = "Lasry's list (cryptiana GL.htm, fetched 15 Nov 2026) grepped for %s: no entry."
AP403 = ("Abhilekh Patal answered HTTP 403 'Request blocked' (CloudFront) to curl on 16 Nov 2026 at the first request "
         "(item 76980e89-..., lead 2466); not retried around it, so no NAI record or page was opened in this batch.")

P = {}

P['1387'] = dict(verdict=None, confidence='low',
    note=("Not assessed: NA 2.10.62 inv. 2914 is still PHYSICAL with no scans (Nationaal Archief API "
          "zvt.nationaalarchief.nl/api/eads/2.10.62/clevels/2914 re-read 16 Nov 2026: 'scans': [], availability PHYSICAL). "
          "The description ('door Bk. Makassar onderschepte, bij Republikeinse groeperingen gebruikte coderingen') cannot tell "
          "code tables from coded messages, so the 9 Nov blocker stands."),
    access='archive', access_note='Nationaal Archief scan order or reading room; API shows no scans on 16 Nov 2026.')

P['2468'] = dict(verdict=None, confidence='low',
    note=("Not assessed: NAI Confidential B Frontier 1905 File 67/77 (72 pp.) is known only from its title; whether the "
          "Russian groups are copied in it, and whether any reading is filed, is not shown. " + AP403),
    access='online', access_note=AP403 + ' Needs Daniel\'s logged-in Chrome session.')

P['2466'] = dict(verdict='partly_read', confidence='medium',
    note=("The file title itself reports 'Discovery of a Key to the Chinese Cypher by Captain Campbell', and the one "
          "contributor who has opened File 45506 (Brice Dudout, for targets/peking1912, 11 Nov 2026) recorded from it "
          "Campbell's 'transparency' key with worked code pairs (5391->5411, 0365->0025) and a General Staff column formula: "
          "the traffic was being read at the time and the method is on file. How many of the copied telegrams carry a "
          "reading was not seen, hence partly_read rather than read."),
    access='online', access_note=AP403 + ' Contents known from targets/peking1912/frozen/PREREG.md (H2, H3) and profile.json notes.',
    vetting=dict(date='2026-11-16', by=BY,
        seen=dict(kind='transcription',
            where=("Not opened in this batch (Abhilekh 403). Second-hand: targets/peking1912/frozen/PREREG.md, hypotheses H2-H3, "
                   "and targets/peking1912/profile.json 'notes' (contributor Brice Dudout, 11 Nov 2026, who saw NAI Foreign Dept. "
                   "1907 File 45506 after login): 'Campbell's transparency key, the General Staff's column formula, Webster's "
                   "dictionary, a 5-digit code'. Record title from research/sweep_2026-11-11_asia (PR_000006228785)."),
            extent="40 pp. (File 45506) plus 10 pp. sequel (PR_000004129545); number of telegrams not recorded.",
            cipher=("Chinese telegraph code disguised by a page/column shift ('transparency' relation, e.g. code 5391 sent for "
                    "5411, 0365 for 0025) and a General Staff column formula (+/-20..380 by column, sign by page parity); "
                    "Campbell's key and example equivalences are filed in the same file, so a decipherment method and readings "
                    "are with the piece."),
        ),
        prior_art=dict(
            decode='DECODE RecordsList searched 11 Nov 2026 (sweep) for Yatung, Tibet, Chinese telegram: 0 records; known.py on 45506, Chumbi, Yatung, Campbell 16 Nov 2026: only the lead itself and targets/peking1912.',
            tomokiyo=TOMO % 'Chinese, Tibet, Chumbi, Campbell',
            lasry=LASRY % 'Chinese, Tibet, Chumbi, Campbell',
            edition=('No edition of the telegrams known; the British Blue Books on Tibet (Cd. papers 1904-1910) were noted in the '
                     'sweep as printing no cipher text. The reading is in the file itself (Campbell\'s key), not in print.'),
            literature=('Web search 11 Nov 2026 (Campbell Yatung Chinese cypher telegrams Chumbi 1907 key) found only narrative '
                        'histories of the Chumbi occupation; targets/peking1912 (1912 telegram, read 11-12 Nov 2026) used the '
                        'file\'s methods as hypotheses and needed none of them.')),
        key_check=("Campbell's key is in the file (title and contributor's notes). It was not needed for the 1912 telegram "
                   "(plain standard code read by rows), so it has not been tested on any text here."),
        key_in_volume="Campbell's 'Key to the Chinese Cypher' and the General Staff column formula are filed in File 45506; not tested here (file not opened).",
        duplicates=("known.py on 45506, Chumbi, Yatung, Campbell, 19/45, Gyantse: duplicate record PR_000004256746 (dated 1908) is "
                    "the same file; lead 2467 (1908-15 General Staff acquisitions) is a sibling series, not the same telegrams; "
                    "lead 2465 / targets/peking1912 is a different 1912 telegram."),
        verdict='partly_read',
        closed=("Campbell's key to the Chinese cypher, with worked equivalences and the General Staff formula, is filed in "
                "File 45506, so the 1907-08 Chumbi telegrams were read at the time; how many readings are written out was not "
                "seen (Abhilekh blocked)."),
    ))

P['2469'] = dict(verdict=None, confidence='low',
    note=("Not assessed: NAI Cypher Confidential 1909 Nos. 72-75 and siblings (89 + 44 + 9 + 13 + 14 pp.) are known from "
          "titles only (arrangements to take foreign cypher telegrams at Gulf offices); no record shows the groups are copied. " + AP403),
    access='online', access_note=AP403)

P['2467'] = dict(verdict=None, confidence='low',
    note=("Not assessed: File 19/45 (67 pp.) and siblings are known from titles only. One fact against 'open': File 45506 "
          "(lead 2466) already holds the General Staff's 1908 column formula for the Chinese cypher (targets/peking1912 "
          "PREREG H3), so the General Staff, for whom these telegrams were acquired, could read the traffic from 1908; whether "
          "readings are filed in 19/45 was not seen. " + AP403),
    access='online', access_note=AP403)

P['2470'] = dict(verdict=None, confidence='low',
    note=("Not assessed: File 72/81 (26 pp.) forwards intercepted German wireless messages to London; Room 40 read German "
          "diplomatic codes of this family, and the 1915 sibling concerns the Bushire code books themselves, but whether "
          "the Indian file holds groups or readings was not seen. " + AP403),
    access='online', access_note=AP403)

P['2471'] = dict(verdict=None, confidence='low',
    note=("Not assessed: Deposit Cypher 1917 No. 19 (71 pp.), title only; if the groups are the public four-figure Chinese "
          "telegraph code (as in targets/peking1912) they would be a key_lookup, but nothing was seen. " + AP403),
    access='online', access_note=AP403)

P['2472'] = dict(verdict=None, confidence='low',
    note=("Not assessed: External-B 1917 Nos. 38-42 (18 pp.) is about releasing detained Siamese telegrams; whether copies "
          "are attached is unknown. " + AP403),
    access='online', access_note=AP403)

P['2473'] = dict(verdict=None, confidence='low',
    note=("Not assessed: External-B Nov 1920 No. 64 and July 1920 Nos. 192-199, titles only. Web search 16 Nov 2026 "
          "(Jukowsky Russian cipher expert 1920 German Legation Tehran) found nothing on Jukowsky or a result; the QDL "
          "'Persia: German agents' files came up but do not name him. " + AP403),
    access='online', access_note=AP403)

P['2474'] = dict(verdict=None, confidence='low',
    note=("Not assessed: External 1943 File 79-X-43-Sec. (32 pp.), title only; whether the Tibetan code message is copied, "
          "and whether the British read it, is not stated. " + AP403),
    access='online', access_note=AP403)

P['2763'] = dict(verdict=None, confidence='low',
    note=("Not assessed: the Neuchatel records 102MsR-101.15/16 are reachable only through archives-online.org (Chrome "
          "form + SignalR, per the 15 Nov sweep), not by script; two web searches 16 Nov 2026 (Rousseau Conti 1767 chiffre / "
          "'Tables de chiffrement' Rousseau 1767) found neither the records nor the Garnier tables. The 15 Nov note stands: "
          "a printed 1767 cipher table and Leigh's edition make an existing reading likely, unproven."),
    access='archive', access_note='Needs archives-online.org in Chrome (record notes field) and Leigh, Correspondance complete, 1767 volumes.')

P['2093'] = dict(verdict=None, confidence='low',
    note=("Not assessed: only the ArchiveGrid line 'Simple cryptogram possibly written by a person named Lewis'; ArchiveGrid "
          "is on today's bot-check list and no N-YHS catalogue record or scan was reached; the 3 Nov searches found nothing more."),
    access='archive', access_note='ArchiveGrid bot check; needs N-YHS scan.')

P['2092'] = dict(verdict=None, confidence='low',
    note=("Not assessed: series-level phrase 'some of them worded in code' (ArchiveGrid, bot check today); no item or leaf. "
          "Most likely a commercial telegraph code (a key_lookup if so), but the holder and the code were not established."),
    access='archive', access_note='ArchiveGrid bot check; needs N-YHS inventory and a sample.')

P['2654'] = dict(verdict='read', confidence='medium',
    note=("Arcinsys (record 61404, read 16 Nov 2026) lists 'Bericht ueber die Truppen des Rittmeisters Maudt vor Lemgo (1630, "
          "verschluesselt und Aufloesung)': the archive's own description says the decipherment is filed with the ciphered "
          "report. The volume is digitised (115 images, NLA OS film 0200/109 01); four images were looked at full size and "
          "the cipher leaf itself was not located."),
    access='online',
    access_note=("Digitised: https://www.arcinsys-digitalisate.niedersachsen.de/nla_os/rep_100/abschnitt_256_nr._4/"
                 "m_os_rep_100_abschnitt_256_nr._4_aufn_0001.jpg ... _0115.jpg (full images about 37 s each by curl; thumbs under "
                 "/thumbs/). Archivportal-D (the lead's link) is behind an Anubis proof-of-work check; Arcinsys answers by script."),
    correct_link='https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=61404',
    vetting=dict(date='2026-11-16', by=BY,
        seen=dict(kind='scan',
            where=("Arcinsys Niedersachsen record 61404 (NLA OS, Rep 100, Abschnitt 256 Nr. 4), description read 16 Nov 2026; "
                   "all 115 thumbnails fetched and viewed as contact sheets; full images aufn_0047 (f. 44, letter dated 15 Mar 1630), "
                   "0063 (f. 60, postscript), 0113 and the first image viewed at 1400-1600 px: all plain German."),
            extent=("One ciphered report in a volume of 1626-1632 (115 images); the cipher leaf was not located in the images "
                    "viewed, so its length is not measured."),
            cipher=("Archive's description: 'Bericht ueber die Truppen des Rittmeisters Maudt vor Lemgo (1630, verschluesselt "
                    "und Aufloesung)': a ciphered report filed with its Aufloesung (decipherment). The images looked at were all "
                    "plain text.")),
        prior_art=dict(
            decode='known.py on Rep 100, Maudt, Franz Wilhelm, Osnabrueck (16 Nov 2026): no DECODE record or ledger entry for this volume.',
            tomokiyo=TOMO % 'Osnabr, Wartenberg, Lemgo, Maudt',
            lasry=LASRY % 'Osnabr, Wartenberg, Lemgo, Maudt',
            edition='No edition of this volume known; the reading is the contemporary Aufloesung filed with the report, per the archive description.',
            literature=('Not searched beyond the repo: the decisive fact (decipherment filed with the piece) is in the finding aid. '
                        'Franz Wilhelm von Wartenberg files elsewhere in catalogue.json are different volumes.')),
        key_check='No key in the volume is described; a key is not needed, since the Aufloesung is filed with the report.',
        duplicates=('known.py on the shelfmark, Maudt, Franz Wilhelm and Osnabrueck: no catalogue or lead duplicate; other Franz '
                    'Wilhelm files in catalogue.json are different units.'),
        verdict='read',
        closed=("The archive describes the 1630 Maudt report as 'verschluesselt und Aufloesung': the contemporary decipherment "
                "is filed with it in NLA OS Rep 100 Abschnitt 256 Nr. 4."),
    ))

P['2021'] = dict(verdict=None, confidence='low',
    note=("Not assessed: Arcinsys record 1683898 re-read 16 Nov 2026 still shows only 'Original Akte' (no digitisation) for "
          "Cal. Br. 15 Nr. 3805, 'Beschlagnahme von chiffrierter Korrespondenz ... Sixtinus mit seinem Bruder zu Kassel', 1636-37; "
          "the 3 Nov blocker (a scan) stands. Sixtinus key of Dec 1635 (targets/malsburg1637, HStAM 4 d Nr. 1218) to try afterwards."),
    access='archive', access_note='NLA Hannover scan order; not digitised (Arcinsys 16 Nov 2026).')

P['1977'] = dict(verdict=None, confidence='low',
    note=("Not assessed: Arcinsys 1680530 and 1684901 re-read 16 Nov 2026: Cal. Br. 15 Nr. 2225 ('z.T. in Chiffre verfasst', "
          "ca. 11 Bl.) and Nr. 2233 ('z.T. in Chiffre') show only 'Original Akte', no digitisation; the Hanoverian chancery "
          "habitually interlined decipherments, so the blocker (a scan) stands."),
    access='archive', access_note='NLA Hannover scan order; not digitised (Arcinsys 16 Nov 2026).')

P['1936'] = dict(verdict=None, confidence='low',
    note=("Not assessed: manuscripts.nls.uk answered a Cloudflare 'Just a moment' challenge to curl on 16 Nov 2026; the record "
          "still cannot tell cipher from shorthand. Needs the leaves or NLS microfilm Mf.Sec.MSS.699."),
    access='archive', access_note='NLS catalogue behind Cloudflare to scripts; needs Chrome and an NLS scan.')

P['2810'] = dict(verdict=None, confidence='low',
    note=("Not assessed: the 82-item list of Adv.MS.33.1.13 (NLS ArchivesSpace) is behind Cloudflare to scripts (16 Nov 2026), "
          "and a web search on the shelfmark found nothing; no item is yet shown to be enciphered."),
    access='archive', access_note='NLS catalogue behind Cloudflare to scripts; read the component list in Chrome.')

ORDER = '1387 2468 2466 2469 2467 2470 2471 2472 2473 2474 2763 2093 2092 2654 2021 1977 1936 2810'.split()
out = {k: P[k] for k in ORDER}
json.dump(out, open(os.path.join(HERE, 'proposals.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'proposals')
