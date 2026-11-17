"""Build proposals.json for wave 20 batch b11 (16 Nov 2026). Run: python -I -X utf8 make.py"""
import json, os

DATE = '2026-11-16'
BY = 'claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting'
ACTA = ('GStA PK ACTApro record fetched by plain HTTP on 16 Nov 2026 through '
        'https://archive.spk-berlin.de/actaproweb/document/Vz_<uuid> (actadoc.py in this folder; the archive.xhtml permalink '
        'returns only the page frame) or through a scripted POST of the search form (actapro.py)')


def tom(terms):
    return (f'Tomokiyo, cryptiana.web.fc2.com/code/unsolved.htm (fetched 15 Nov 2026), grepped as text for {terms}: '
            'no entry for this item (the only substring hits are unrelated words).')


def las(terms):
    return (f'Lasry list cryptiana.web.fc2.com/code/GL.htm (fetched 15 Nov 2026), grepped as text for {terms}: '
            'no entry for this item.')


P = {}


def add(lid, verdict, conf, note, access, access_note, vetting=None, **extra):
    d = {'verdict': verdict, 'confidence': conf, 'note': note, 'access': access, 'access_note': access_note}
    d.update(extra)
    if vetting is not None:
        v = {'date': DATE, 'by': BY}
        v.update(vetting)
        v['verdict'] = verdict
        d['vetting'] = v
    P[str(lid)] = d


# ---------------------------------------------------------------- 2502
add(2502, 'open', 'low',
    'The full ACTApro records were read: Nr. 304 is "Gesandtschaftsberichte Bd. 1", 1810-12, containing only partly ciphered copies, and its old shelfmark '
    '"Rep. 1 B Oestreich" shows these are reports of the Westphalian legation in Austria, not Berlin; Nr. 393 is a press-affairs file of 1811 that also holds '
    '"chiffrierte Berichte an den westphaelischen Gesandten in Berlin, Baron von Linden". No decipherment is noted, but whether the ciphered pieces carry their '
    'clear text is not stated, and all three units (304, 393 and the Chiffrierbuch 541) are marked unproducible until 31 May 2029.',
    'archive',
    'Not digitised. ACTApro marks Nr. 304, 393 and 541 "Unbestellbar bis 31.05.2029, Archivale nicht vorlegbar (Magazininstandsetzung)": no reading-room '
    'access or scan order before June 2029.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': V. HA Koenigreich Westphalen Nr. 304 (Vz_489e7916-61bc-46e4-a119-abfe70661163), Nr. 393 (Vz_86c46ff1-38bb-4e4e-8481-f6436c329c12) '
                     'and Nr. 541 (Vz_cad825e8-62f6-41a9-b106-873fd0a0b069); raw text in raw_actapro6.txt.',
            'extent': 'Nr. 304: one volume of legation reports 1810-1812 (old shelfmark V. HA Rep. 1 B Oestreich Nr. 14 I), leaf count not given; Nr. 393: a 1811 '
                      'press-affairs file in which the ciphered reports to Linden are one item among newspaper copies; leaf counts not given.',
            'cipher': 'Archive wording, verbatim: Nr. 304 "enth. nur: z.T. chiffrierte Abschriften"; Nr. 393 "chiffrierte Berichte an den westphaelischen Gesandten '
                      'in Berlin, Baron von Linden". No Aufloesung or Dechiffrierung is mentioned in either record; the leaves themselves were not seen.',
        },
        'prior_art': {
            'decode': 'known.py on "Westphal", "Linden", "Koenigreich Westphalen" and "Nr. 393": hits are only this lead, its sweep file and unrelated catalogue '
                      'entries (Dutch legation at the Westphalian court, Peace of Westphalia files); no DECODE record of the Westphalian ministry.',
            'tomokiyo': tom('"Westphal", "Linden", "Koenigreich Westphalen"'),
            'lasry': las('"Westphal", "Linden"'),
            'edition': 'No printed edition of the Westphalian legation reports from Vienna or of the 1811 instructions to Linden was found; the record does not cite '
                       'one, and the 11 Nov sweep found none. The Kassel ministry files were not printed as far as a web search shows.',
            'literature': 'No study of the Westphalian diplomatic cipher found in the sweep notes or by known.py; the ministry\'s own code book (Nr. 541) is '
                          'undated and unpublished.',
        },
        'key_check': 'The same fonds holds the Westphalian "Chiffrierbuch (Chiffre chiffrant et dechiffrant)", V. HA Koenigreich Westphalen Nr. 541, undated: '
                     'a likely key for these pieces, recorded here; it is also unproducible until 31 May 2029.',
        'duplicates': 'known.py finds no other entry or lead on V. HA Koenigreich Westphalen Nr. 304 or 393; the Dutch envoy\'s letters from the Westphalian '
                      'court in the catalogue are a different fonds and sender.',
    },
    correct_correspondents='Nr. 304: Westphalian legation in Austria (Vienna) to the Kassel foreign ministry, copies; Nr. 393: Kassel ministry to Baron von Linden, Berlin.')

# ---------------------------------------------------------------- 2602
add(2602, 'read', 'high',
    'Politische Correspondenz Friedrichs des Grossen vol. 18 (1759) prints about 28 of Frederick\'s 1759 orders to Wedel "nach der Ausfertigung im Wedell\'schen '
    'Familienarchiv zu Ludwigsdorf", the very originals now in Nl Wedel Nr. 3, and prints no. 11314 (Beeskow, 3 Aug 1759) "nach einer Abschrift der '
    'dechiffrirten Ausfertigung" there; the file itself holds five Dechiffrierungen.',
    'archive', 'Not digitised; GStA PK reading room or scan order. The edition is on the Internet Archive.',
    {
        'seen': {
            'kind': 'transcription',
            'where': ACTA + ': VI. HA Nl Wedel, K. H. v., Nr. 3 (Vz_46a81587-b29c-44fc-8b62-7d1f51d84cbd): "40 Kabinettsordres, fuenf Abschriften '
                     '(Dechiffrierungen) und zwei Einzelschreiben", 98 Blatt. Printed texts read in Politische Correspondenz vol. 18, Internet Archive '
                     'politischecorres181freduoft and politischecorres182freduoft (OCR searched for Wedel and dechiffr), e.g. no. 11314 on p. 469-470.',
            'extent': '40 cabinet orders of 1759 with five deciphered copies, 98 leaves; how many orders were sent in cipher is not stated in the record.',
            'cipher': 'The record itself files five decipherments with the orders, and the edition prints the orders from the Wedel family archive, one of them '
                      'from the deciphered copy, so the ciphered orders are read.',
        },
        'prior_art': {
            'decode': 'known.py on "Wedel", "Nl Wedel" and "Kabinettsordre": only this lead and its sweep files; the catalogue Wedel hits are other people. No DECODE record.',
            'tomokiyo': tom('"Wedel", "Kabinettsordre"'),
            'lasry': las('"Wedel"'),
            'edition': 'Politische Correspondenz Friedrichs des Grossen, vol. 18 (Berlin 1890-91), both halves: about 28 orders to Wedel are printed with the source '
                       'note "Nach der Ausfertigung im Wedell\'schen Familienarchiv zu Ludwigsdorf in Schlesien"; no. 11314 to Generallieutenant von Wedell, '
                       'Beeskow 3 Aug 1759, is printed "Nach einer Abschrift der dechiffrirten Ausfertigung im Wedell\'schen Familienarchiv".',
            'literature': 'Not searched further: the edition settles the question.',
        },
        'key_check': 'Frederick II\'s field cipher with his generals is not held in this repo; not needed, since the decipherments are filed and printed.',
        'duplicates': 'No other entry or lead on Nl Wedel Nr. 3; catalogue 590 (Bevern/Schwerin) is a different recipient.',
        'closed': 'Read: the five Dechiffrierungen are filed with the orders and the Politische Correspondenz prints the 1759 orders to Wedel from these '
                  'originals, one from the deciphered copy.',
    })

# ---------------------------------------------------------------- 2596
add(2596, 'open', 'low',
    'The ACTApro record reads "Notizheft mit Angaben zu verschiedenen Orten und Personen (z. T. verschluesselt)", ca. 1777-1781: the archive itself calls the '
    'notebook partly enciphered, no decipherment or edition was found; whether it is a true cipher or shorthand/Rosicrucian sigla cannot be told without the leaves.',
    'archive', 'Not digitised (no digital object on the record); GStA PK reading room or scan order. No access restriction shown.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': search hit for "Notizheft" returning VI. HA Nl Woellner, J. C. v., Nr. 6 with its full title (raw_actapro2.txt); the permalink '
                     'id 21a70622-d7ea-5b30-a6c4-7eb14c4ca5ce does not load by the /document/ route.',
            'extent': 'One notebook, ca. 1777-1781; extent not given in the record.',
            'cipher': 'Archive title, verbatim: "Notizheft mit Angaben zu verschiedenen Orten und Personen (z. T. verschluesselt)". No decipherment is mentioned; '
                      'the notebook was not seen, so the kind of concealment (cipher, shorthand or order sigla) is not established.',
        },
        'prior_art': {
            'decode': 'known.py on "Woellner", "Woellner" with umlaut, "Rosenkreuz" and "Rosicruc": only this lead and its sweep files, plus unrelated Rosicrucian '
                      'items (andreae1616); no DECODE record.',
            'tomokiyo': tom('"Woellner", "Rosenkreuz", "Rosicruc"'),
            'lasry': las('"Woellner", "Rosicruc"'),
            'edition': 'No edition of Woellner\'s notebooks found: a web search (Woellner Nachlass Notizheft verschluesselt Geheimschrift Rosenkreuzer) returned the '
                       'GStA Nachlass listing and the Deutsche Biographie article only.',
            'literature': 'The Deutsche Biographie entry and the GStA inventory of Nachlaesse were found; neither mentions a ciphered notebook or a decipherment.',
        },
        'key_check': 'No key known; the Gold- und Rosenkreuzer order used cipher and order names, but no key for Woellner\'s notebook is held or published as far as searched.',
        'duplicates': 'known.py finds no other entry or lead on Nl Woellner Nr. 6.',
    })

# ---------------------------------------------------------------- 2608
add(2608, 'not_cipher', 'medium',
    'The four ACTApro records were read in full: Nr. 48 a (Thulemeier), Nr. 52 (Wilhelmine) and Nr. 54 (Goertz) are clear letters that only mention ciphers '
    '(sending by courier for the cipher\'s safety, a letter not yet deciphered, "two ciphered lines" received elsewhere); only Nr. 8, Blumenthal 1786, one leaf, '
    'says "Der Rest ist nicht dechiffrierbar", which more likely means illegible than enciphered.',
    'archive', 'Not digitised; GStA PK reading room or scan order. A scan of Nr. 8 would settle the one doubtful leaf.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': VI. HA Nl Schlitz v. Goertz Nr. 8 (Vz_dff887d8-ca15-4d71-bbe0-fe306b1f56fd), Nr. 48 a (Vz_713ccf60-183c-4e6a-86de-868acdd45919), Nr. 52 (Vz_8efe6403-447e-430c-8c7c-19fd91ff5168), '
                     'Nr. 54 (Vz_4b488b32-f62e-424a-befe-d4449f3392d2); full summaries with long translated quotations in raw_actapro1.txt.',
            'extent': 'Four single letters of 1-2 leaves each (Nr. 8: 1 leaf, German; 48 a: 2 leaves, French; 52: 1 leaf, French; 54: 2 leaves, French).',
            'cipher': 'Nr. 48 a, 52 and 54 are summarised and translated at length from clear French text; their cipher words refer to other documents. Nr. 8 '
                      '(Blumenthal, Berlin, July 1786) is summarised to mid-letter and ends "(Der Rest ist nicht dechiffrierbar.)": no cipher is described.',
        },
        'prior_art': {
            'decode': 'known.py on "Goertz", "Thulemeier", "Blumenthal", "Wilhelmine": hits only in unrelated catalogue entries (Goertz the Swedish minister, the '
                      'Schoening/Thulemeier target); no DECODE record of these letters.',
            'tomokiyo': tom('"Goertz", "Thulemeier", "Blumenthal"'),
            'lasry': las('"Goertz", "Thulemeier"'),
            'edition': 'The archive summaries themselves translate the letters; no printed edition was needed to establish that three are clear.',
            'literature': 'Not searched further for these four letters.',
        },
        'key_check': 'None needed; no ciphertext is described.',
        'duplicates': 'No other entry or lead on Nl Schlitz v. Goertz Nr. 8, 48 a, 52 or 54.',
        'closed': 'Not cipher: three of the four letters are clear letters that only mention ciphers, and the fourth (Nr. 8) carries an archivist\'s note that the '
                  'rest could not be read, with no cipher described.',
    })

# ---------------------------------------------------------------- 2501
add(2501, 'read', 'medium',
    'The only cipher piece in FA Lusi Nr. 3 is the received royal letter "Friedrich Wilhelm II. an Lusi, Berlin, 1. Oktober 1790 (chiffriert)". The sending side '
    'holds the same correspondence in Berlin: I. HA Rep. 96 Nr. 164 G (the Cabinet\'s correspondence with Lusi, Aug-Dec 1790) and I. HA Rep. 11 Nr. 10691 '
    '("Schriftwechsel mit Lusi (Abschriften und Dechiffrierungen)", 1790), where the clear minute and decipherments of the 1790 cipher letters should stand.',
    'archive', 'Not digitised; GStA PK reading room or scan order (FA Lusi Nr. 3, Rep. 96 Nr. 164 G, Rep. 11 Nr. 10691).',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': VI. HA FA Lusi Nr. 3 (Vz_cb052f2b-f43c-437c-ab3a-e49265e78b3b), I. HA Rep. 11 Akten Nr. 10691 (Vz_c1b02d23-bd30-48b5-8b72-525a434b65b1), '
                     'I. HA Rep. 96 Nr. 164 G (Vz_391a833f-0510-4a27-80d0-b687ea59fea4); text in raw_actapro5.txt.',
            'extent': 'One ciphered royal letter of 1 Oct 1790 inside a file of Lusi\'s report drafts in Lombard\'s hand (clear), Aug-Nov 1790.',
            'cipher': 'Archive wording: "enth. auch: Friedrich Wilhelm II. an Spiridion Graf von Lusi, Berlin, 1. Oktober 1790 (chiffriert)". The government series '
                      'Rep. 11 Nr. 10691 is titled "Abschriften und Dechiffrierungen" of the same 1790 correspondence.',
        },
        'prior_art': {
            'decode': 'known.py on "Lusi", "Spiridion", "Lombard": only this lead, its sweep files and unrelated catalogue words; no DECODE record.',
            'tomokiyo': tom('"Lusi", "Spiridion"'),
            'lasry': las('"Spiridion"; "Lusi" gives only substring hits in unrelated French words'),
            'edition': 'No edition of the 1790 Lusi mission found (11 Nov web search, recorded in the lead); the plaintext side is the archival copy series named above.',
            'literature': 'Not searched further.',
        },
        'key_check': 'No Prussian 1790 cipher held in this repo; not needed if the minute in Rep. 96 Nr. 164 G is confirmed.',
        'duplicates': 'No other entry; the 14 Nov GStA deep sweep already linked Rep. 11 Nr. 10691 as the plaintext side of FA Lusi Nr. 3.',
        'closed': 'Read on the sending side: the King\'s ciphered letter of 1 Oct 1790 belongs to a correspondence whose clear minutes and decipherments are filed '
                  'in Berlin (Rep. 96 Nr. 164 G, Rep. 11 Nr. 10691); not confirmed leaf by leaf.',
    })

# ---------------------------------------------------------------- 2503
add(2503, 'partly_read', 'low',
    'The full record reads "Scharnhorst, 23 Schreiben an Boyen, vier an Scharnhorst (Konzepte), sieben chiffrierte Schreiben, vier masch. Transkriptionen" '
    '(1810-1813): typed transcriptions lie in the same file as the seven ciphered letters. What they transcribe is not stated, and the Kunisch edition of '
    'Scharnhorst\'s Private und dienstliche Schriften, whose later volumes cover 1810-13, could not be opened.',
    'archive', 'Not digitised; GStA PK reading room or scan order. Kunisch et al. (Boehlau 2002-) is in print, not online.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': VI. HA Nl Boyen d. Ae. Nr. 648 (Vz_2d6c0141-2f56-427a-8c9d-c95102a0eef1); raw_actapro5.txt.',
            'extent': '23 letters of Scharnhorst to Boyen, four drafts to Scharnhorst, seven ciphered letters and four typed transcriptions, 1810-1813; leaf count not given.',
            'cipher': 'The archive names "sieben chiffrierte Schreiben" and, in the same unit, "vier masch. Transkriptionen"; the transcriptions may be of the '
                      'ciphered letters.',
        },
        'prior_art': {
            'decode': 'known.py on "Scharnhorst" and "Boyen": only this lead, the sweep files and the unrelated SMS Scharnhorst entry (catalogue 1411); no DECODE record.',
            'tomokiyo': tom('"Scharnhorst", "Boyen"'),
            'lasry': las('"Scharnhorst", "Boyen"'),
            'edition': 'Scharnhorst, Private und dienstliche Schriften, ed. Kunisch, Stieve and Sikora (Boehlau, 2002-): vol. 6 covers the crisis after 1809, the later '
                       'volumes 1810-13; not online, not opened. Linnebach, Scharnhorsts Briefe I (1914, IA bub_gb_e8wrAQAAIAAJ) was downloaded but its Fraktur '
                       'OCR is unreadable (no hit even for Boyen).',
            'literature': 'Two web searches (Kunisch volume contents, Boyen and Chiffre) found no description of these ciphered letters.',
        },
        'key_check': 'No Scharnhorst-Boyen key held or found.',
        'duplicates': 'No other entry or lead on Nl Boyen Nr. 648.',
        'closed': 'Partly read: typed transcriptions are filed with the ciphered letters in the same unit; which letters they cover, and whether Kunisch prints the '
                  'rest, is not checked.',
    })

# ---------------------------------------------------------------- 2622
add(2622, 'key_lookup', 'high',
    'The full ACTApro record is only "Lord Strangford an von Miltitz (Briefe)", 1825-1828, "Enthaelt auch: 2 Schluessel zu Chiffern": two keys, and no '
    'ciphered letter is named.',
    'archive', 'Not digitised; GStA PK reading room or scan order.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': VI. HA Nl Miltitz, A. v., II, Nr. 26 (Vz_23a83ffd-a0af-4302-ae60-4b3948f168ce); raw_actapro1.txt.',
            'extent': 'Letters of Strangford to Miltitz 1825-1828 with two cipher keys; count of letters and leaves not given.',
            'cipher': 'Archive wording, verbatim: "Enthaelt auch: - 2 Schluessel zu Chiffern." No letter is described as ciphered.',
        },
        'prior_art': {
            'decode': 'known.py on "Strangford" and "Miltitz": only this lead and its sweep files (the catalogue Miltitz hits are the 16th-century Heinrich von Miltitz); no DECODE record.',
            'tomokiyo': tom('"Strangford", "Miltitz"'),
            'lasry': las('"Strangford", "Miltitz"'),
            'edition': 'Not searched: no ciphertext is described, so there is nothing to find a reading of.',
            'literature': 'Not searched for the same reason.',
        },
        'key_check': 'The two keys are the content of the lead; they belong with key material, not with the catalogue of ciphertexts.',
        'duplicates': 'No other entry or lead on Nl Miltitz II Nr. 26.',
        'closed': 'Key lookup: the unit holds two cipher keys with Strangford\'s letters, and no ciphered letter is described.',
    })

# ---------------------------------------------------------------- 1620: no verdict
add(1620, None, None,
    'Not assessed: the recorded blocker stands. The edition that would print or calendar the 1419 Grand Master letter (Koeppen, Die Berichte der '
    'Generalprokuratoren vol. 3, Johann Tiergart 1419-1428, Goettingen 1966-71) is not online, and the Archivportal-D record cannot be reread (proof-of-work page).',
    'archive', 'Archivportal-D record only; no image. Needs the printed Koeppen vol. 3 or a GStA copy of OBA 2987.')

# ---------------------------------------------------------------- 2595
add(2595, 'read', 'medium',
    'Of the three OBA units only Nr. 22687 (Grand Master to Schoenberg, 1 Oct 1519) is ciphertext, and the archive files it "Chiffren, mit Uebertragung", '
    'with draft and copy; Nr. 22442 is a letter whose head-regest lists "Benutzung v. Chiffren" as a topic, and Nr. 23213 is Margrave Kasimir asking for a '
    'cipher alphabet to decipher a letter. The unit belongs with lead 2625 (Schoenberg-Albrecht letters with their Aufloesung, closed read).',
    'archive', 'Not digitised; GStA PK reading room or scan order.',
    {
        'seen': {
            'kind': 'not online',
            'where': ACTA + ': search hits giving the Kopfregest of XX. HA OBA Nr. 22442 (Vz_ce2d626f-2e0e-43e6-9857-89106bc9b346), Nr. 22687 (Vz_c7803fae-25a3-42ef-8f78-e8d58fa2ff82) and Nr. 23213 '
                     '(Vz_5dd3a8f0-d9e9-420e-a4a1-8b4aa309edc1); raw_actapro2.txt and raw_actapro3.txt.',
            'extent': 'Three single units of 1519-1520; Nr. 22687 adds a slip in cipher (news of Bishop Job).',
            'cipher': 'Verbatim: Nr. 22687 "Chiffren, mit Uebertragung. Auch Entwurf u. Abschrift. 1 Zettel (Chiffren): Nachrichten d. Bischofs Job"; Nr. 22442 '
                      '"Polen. Zeitungen aus Deutschland. Muenzen v. Geld. Georg Anger. Benutzung v. Chiffren"; Nr. 23213 "Markgraf Kasimir an Hochmeister: Bitte '
                      'um ein Chiffern-Alphabet z. Entzifferung eines von ihm ...".',
        },
        'prior_art': {
            'decode': 'known.py on 22442, 22687, 23213, Kasimir and Schoenberg: catalogue 553 already lists 22687 among the units "with contemporary or modern '
                      'Aufloesung"; otherwise only leads 2595/2625/2626 and the GStA sweep files. No DECODE record.',
            'tomokiyo': tom('"Kasimir", "Schoenberg", the OBA numbers'),
            'lasry': las('"Kasimir", "Schoenberg"'),
            'edition': 'Joachim, Die Politik des letzten Hochmeisters vol. 2 (IA OCR, local copy) searched for Chiffr/Ziffer: only no. 36, cipher instructions of 1519 '
                       'from Nikolaus von Schoenberg; 22687 was not found printed, which does not matter as its Uebertragung is filed with it.',
            'literature': 'As for lead 2625: no study of the Schoenberg-Albrecht cipher found.',
        },
        'key_check': 'The chancery\'s Chiffrenbuch OBA 27584 (key_leads.json) is the nearest key; Nr. 23213 is a request for an alphabet, not a key.',
        'duplicates': 'Catalogue 553 names 22687 in its side list of units with an Aufloesung; lead 2625 holds the other Schoenberg-Albrecht pieces with decipherments.',
        'closed': 'Read: the one ciphertext unit (OBA 22687) is filed with its Uebertragung, and the other two units are not ciphertext as described.',
    })

# ---------------------------------------------------------------- 2505
add(2505, 'partly_read', 'medium',
    'Joachim, Politik des letzten Hochmeisters III no. 197 (p. 339-340) prints the same letter (Klingenbeck to the Grand Master, Onolzbach 9 Oct 1524) from '
    'the clear "Reinkonzept" A.S.C. 252: the first half summarised, the second in full. The regest\'s ciphered topics are "Koenig Christiern; das '
    'evangelische Wesen": the evangelical matter is in the printed text, but King Christiern is not in Joachim\'s summary, so that passage is in the clear '
    'draft but not in print.',
    'archive', 'Not digitised; GStA PK reading room or scan order. Joachim vol. 3 is on the Internet Archive (diepolitikdeslet03joac).',
    {
        'seen': {
            'kind': 'transcription',
            'where': 'Joachim, Die Politik des letzten Hochmeisters in Preussen, vol. 3 (Leipzig 1895), Internet Archive diepolitikdeslet03joac, no. 197 '
                     '(OCR read 16 Nov 2026, p. 339-340); the OBA regest as quoted in the lead from the 11 Nov GStA read.',
            'extent': 'One letter, partly in cipher; length of the ciphered passage not stated.',
            'cipher': 'GStA regest "(teilweise Chiffern)" on the topics Koenig Christiern and das evangelische Wesen, with no Aufloesung noted; Joachim prints the '
                      'clear Reinkonzept, so the plaintext exists for the whole letter, but the Christiern passage is only in the manuscript draft.',
        },
        'prior_art': {
            'decode': 'known.py on "27275" and "Klingenbeck": only leads 2505 and 2627 and the GStA sweep files; no DECODE record.',
            'tomokiyo': tom('"Klingenbeck", "27275"'),
            'lasry': las('"Klingenbeck"'),
            'edition': 'Joachim vol. 3 no. 197 prints the letter from the clear Reinkonzept A.S.C. 252, first half in German summary, second half verbatim '
                       '(Pope and cardinals luring the Grand Master); footnote "Nicht bei Tschackert".',
            'literature': 'Tschackert\'s Urkundenbuch zur Reformationsgeschichte Preussens does not print it (Joachim\'s note); no study of the cipher found.',
        },
        'key_check': 'Klingenbeck\'s cipher is not held; the chancery\'s Chiffrenbuch OBA 27584 is the nearest key; not tried.',
        'duplicates': 'Lead 2627 is Klingenbeck\'s 1525 letter (OBA 27533) with its Aufloesung, closed read; no other entry on OBA 27275.',
        'closed': 'Partly read: the letter is printed from its clear draft, the evangelical passage verbatim, while the King Christiern passage survives in clear '
                  'only in the unprinted part of that draft.',
    })

# ---------------------------------------------------------------- 1157
add(1157, 'partly_read', 'medium',
    'TNA Discovery gives 38M49/1/10/1-51 as "Letters from Francis Drake, Genoa, Milan, Padua and Venice", 1795-97, "with enclosures, some in cipher", and '
    '38M49/1/141/4 as "Plan of a cypher", c1798 (a key). The 1870 Correspondence of William Wickham prints Drake\'s ciphered letters to Wickham in clear, e.g. '
    '"Mr. Drake to Mr. Wickham, Venice, August 3, 1796 ... (Cypher.)", from these papers; the rest of the enclosures are not itemised online.',
    'archive', 'Hampshire Archives (Winchester), not digitised; no item list online. Wickham Correspondence (1870) on the Internet Archive.',
    {
        'seen': {
            'kind': 'transcription',
            'where': 'TNA Discovery API details for 95a07122-3f60-46b7-8255-9f617e6db81a (38M49/1/10/1-51) and 8959aca6-3352-4d43-b0f3-79dc376e85b0 (38M49/1/141/4), '
                     'fetched 16 Nov 2026 (raw/tna_*.json); The Correspondence of the Right Honourable William Wickham from the year 1794 (London 1870), vol. 1, '
                     'Internet Archive correspondencew00wickgoog, OCR searched for cypher and Drake.',
            'extent': '51 items of Drake letters 1795-97 with enclosures, some in cipher; the cipher share is not itemised. 38M49/1/3/1-9 was not re-read.',
            'cipher': 'Archive wording "With enclosures, some in cipher"; the edition prints Drake\'s Venice letter of 3 Aug 1796 marked "(Cypher.)" in clear text, '
                      'and Wickham\'s own cipher drafts to Grenville marked "(Cypher.)" or "To be decyphered by Mr. Canning".',
        },
        'prior_art': {
            'decode': 'known.py on "Wickham" and "38M49": only this lead and catalogue 1156 (Drake papers in Devon, a different deposit); no DECODE record.',
            'tomokiyo': tom('"Wickham", "38M49", "Drake"'),
            'lasry': las('"Wickham", "Drake"'),
            'edition': 'The Correspondence of William Wickham (1870), vol. 1: about 20 Drake mentions, Drake\'s 3 Aug 1796 cipher letter printed in clear; vol. 2 '
                       '(correspondencew01wickgoog) has Wickham deciphering a 1799 Pichegru letter. Not every Drake enclosure was matched.',
            'literature': 'Catalogue 1156 records that Drake\'s cipher letters in Devon have no printed decipherment; not this deposit.',
        },
        'key_check': '38M49/1/141/4 "Plan of a cypher" (c1798) is a key in the same papers; recorded, not seen.',
        'duplicates': 'Catalogue 1156 is the Drake papers at Devon (1700m), the other side of a related correspondence, not the same documents.',
        'closed': 'Partly read: Drake\'s ciphered letters to Wickham are printed in clear in the 1870 Correspondence from these papers; the remaining cipher '
                  'enclosures are not itemised and a key is filed in the same deposit.',
    })

# ---------------------------------------------------------------- 1134
add(1134, 'not_cipher', 'medium',
    'The calendar entry in BRAH 98 reads "El Conde Sinzendorf al de Harrach, Aloisio Luis. (En aleman y en parte indescifrable.) W. S. A. Span. Varia Fasz. 39": '
    'the same calendar uses "indescifrable" for illegible handwriting ("una nota en letra para mi indescifrable") and marks real cipher as "(en cifra)" or '
    '"(Sigue en cifra)", so the note means the German hand was partly unreadable, not that the letter is in cipher.',
    'archive', 'HHStA Wien, Spanien Varia Fasz. 39; not digitised.',
    {
        'seen': {
            'kind': 'transcription',
            'where': 'Boletin de la Real Academia de la Historia vol. 98, "Documentos de la Casa de Austria en Espana", Internet Archive boletindelareala98madr '
                     '(OCR read 16 Nov 2026), entry Paris 6 Sep 1699 and the other uses of "cifra" and "indescifrable" in the same volume.',
            'extent': 'One calendared letter; the calendar gives a German summary of its content (visits to the Dukes of Anjou and Berry, Villars).',
            'cipher': 'No cipher is described: "en parte indescifrable" is the calendarist\'s phrase for a hand he could not read, used elsewhere in the volume '
                      'of a Portuguese note.',
        },
        'prior_art': {
            'decode': 'known.py on "Sinzendorf", "Harrach", "Span. Varia": only catalogue 511 (Harrach/Trautson letters, other units) and this lead; no DECODE record.',
            'tomokiyo': tom('"Sinzendorf", "Harrach"'),
            'lasry': las('"Sinzendorf", "Harrach"'),
            'edition': 'BRAH 98 calendars the letter with a content summary; the summary itself shows the calendarist read most of it.',
            'literature': 'Not searched further.',
        },
        'key_check': 'None needed.',
        'duplicates': 'Catalogue 511 covers other Harrach units of Spanien Varia; Fasz. 39 for 1699 is listed there only as 39-1 in catalogue 512 (Grana/Mansfeld). No duplicate of this letter.',
        'closed': 'Not cipher: the calendar\'s "en parte indescifrable" means partly illegible, as its own usage elsewhere shows, and no cipher is described.',
    })

# ---------------------------------------------------------------- 2655
add(2655, 'key_lookup', 'medium',
    'The finding aid of Marburg 3 Nr. 712 says only "Dabei: Chiffrenalphabet": a cipher alphabet filed with the 1544 envoys\' letters. No letter in the file is '
    'described as ciphered, so the lead is a key until the volume is seen.',
    'archive', 'Archivportal-D record only (proof-of-work page to curl); digitisation on Arcinsys Hessen not found; order from HStA Marburg.',
    {
        'seen': {
            'kind': 'not online',
            'where': 'Finding-aid text as quoted in the lead (Archivportal-D item FOL5BKWF3YDLCF57K2LAKETHJPM2NOC2, read in the 14 Nov sweep); Archivportal-D now '
                     'serves a proof-of-work page and was not re-read.',
            'extent': 'Letters of Guenterode and Keudel (and Rehlinger, and to Duke Moritz), Jul-Aug 1544, with one cipher alphabet; leaf count not known here.',
            'cipher': 'Archive wording "Dabei: Chiffrenalphabet". Whether any letter uses it is not said.',
        },
        'prior_art': {
            'decode': 'known.py on "Guenterode", "Keudel", "Nr. 712", "Politisches Archiv": only this lead and its sweep file; other Philip of Hesse keys in the '
                      'catalogue are different numbers. No DECODE record.',
            'tomokiyo': tom('"Guenterode", "Keudel", "Philipp"'),
            'lasry': las('"Guenterode", "Keudel"'),
            'edition': 'Not searched in print beyond the web: a search for Chiffrenalphabet, Marburg Politisches Archiv, Guenterode, Keudel 1544 returned two other '
                       'Marburg "Chiffernschluessel" records of Philip\'s archive (one dated 1536) and nothing on Nr. 712.',
            'literature': 'No study of the 1544 envoys\' cipher found.',
        },
        'key_check': 'The cipher alphabet in Nr. 712 is itself the item; Marburg 3 also holds other Philip-era Chiffernschluessel records (web search), not compared.',
        'duplicates': 'No other entry or lead on Marburg 3 Nr. 712.',
        'closed': 'Key lookup: the finding aid describes a cipher alphabet filed with the letters and no ciphertext.',
    })

# ---------------------------------------------------------------- 1725
add(1725, 'open', 'medium',
    'AIS 4172844 (re-read by curl): Spanien Varia 28-3, "Einsichtsakten der kaiserlichen Botschaft in Madrid", 1672, Berlin, Wien u.a., fol 1-146, '
    '"teilweise verschluesselt", no reproduction. Same kind of unit as catalogue 1728, 1729 and 1735 (Einsichtsakten 1666, 1670, 1671), entered open; the '
    'Pribram/Landwehr Poetting edition does not cite Spanien Varia.',
    'archive', 'HHStA Wien; AIS shows no scan; Zugaenglichkeit "Oeffentlich", no permission needed.',
    {
        'seen': {
            'kind': 'not online',
            'where': 'AIS record https://www.archivinformationssystem.at/detail.aspx?ID=4172844 (HHStA StAbt Spanien Varia 28-3), fetched by curl 16 Nov 2026 '
                     '(raw/ais_4172844.html); no image link or digital-copy flag.',
            'extent': 'fol 1-146 of embassy Einsichtsakten, 1672, German and Spanish; share in cipher not stated.',
            'cipher': 'AIS Bemerkungen "teilweise verschluesselt"; no decipherment is mentioned and no leaf could be seen.',
        },
        'prior_art': {
            'decode': 'known.py on "Spanien Varia 28", "4172844", "Poetting", "Einsichtsakten": only this lead, its sweep file and the separate catalogue entries '
                      '510 (Poetting letters, Spanien Varia 15-26) and 1728/1729/1735 (other Einsichtsakten units); no DECODE record.',
            'tomokiyo': tom('"Spanien Varia", "Poetting", "Einsichtsakten"'),
            'lasry': las('"Spanien Varia", "Poetting"'),
            'edition': 'Pribram and Landwehr, Privatbriefe Kaiser Leopold I. an Poetting (FRA II 56-57; IA privatbriefekai00pribgoog and 01pribgoog, both OCR texts '
                       'downloaded 16 Nov 2026): 1672 is covered, but "Varia" and "Einsicht" occur nowhere, so this unit is not the source of that edition. A '
                       'Google Books search on Poetting, Madrid 1672, chiffriert (earlier vetting pass) found no edition.',
            'literature': 'As for catalogue 1728: Olivan Santaliestra 2016 on Poetting\'s agents does not describe a decipherment of these files.',
        },
        'key_check': 'No key for this unit held; Pribram\'s preface reports three rebuilt chancery ciphers of the Poetting embassy, not tested here.',
        'duplicates': 'known.py finds no other unit with shelfmark 28-3; catalogue 1728 (24-2-4, 1670), 1729 (20-3-4, 1666) and 1735 (26-4-11, 1671) are sibling units, not the same documents.',
    })

# ---------------------------------------------------------------- 1708: no verdict
add(1708, None, None,
    'Not assessed: the covering edition, Mur Raurell, Diplomacia secreta y paz / Geheimdiplomatie und Friede (Madrid, Biblioteca diplomatica espanola, Fuentes 4), '
    'is a bilingual Spanish-German edition of the Ripperda correspondence of 1724-27 on exactly this peace; whether it prints the HHStA 52-3 pieces is unknown '
    '(not online; the Perspectivia review page served a bot check).',
    'archive', 'AIS 4291348 re-read by curl: fol 387-708, "teilweise verschluesselt", no scan. Needs the Mur Raurell source list.')

# ---------------------------------------------------------------- 1713
add(1713, 'open', 'low',
    'AIS 4327122 (re-read): Spanien Varia 58-1-1, "Korrespondenzen an den Grafen Orsini-Rosenberg", 1757-1764, German/French/Latin, "teilweise verschluesselt", '
    'no scan. The only edition identified (Juretschke/Kleinmann, Berichte der diplomatischen Vertreter des Wiener Hofes aus Spanien) prints the envoys\' '
    'reports, not letters received by them; it was not opened, hence low confidence. The neighbouring unit 58-1-5 (catalogue 1737) was entered open.',
    'archive', 'HHStA Wien; AIS shows no scan; Zugaenglichkeit "Oeffentlich".',
    {
        'seen': {
            'kind': 'not online',
            'where': 'AIS record https://www.archivinformationssystem.at/detail.aspx?ID=4327122 (HHStA StAbt Spanien Varia 58-1-1), fetched by curl 16 Nov 2026 '
                     '(raw/ais_4327122.html); no image link.',
            'extent': 'Extent not given; correspondence addressed to Rosenberg-Orsini (imperial envoy in Madrid) 1757-1764.',
            'cipher': 'AIS Bemerkungen "teilweise verschluesselt"; no decipherment mentioned; leaves not seen.',
        },
        'prior_art': {
            'decode': 'known.py on "Spanien Varia 58-1", "4327122", "Rosenberg": only this lead, its sweep file and catalogue 1723/1737 (other 58-1 units, other '
                      'senders); no DECODE record.',
            'tomokiyo': tom('"Spanien Varia", "Rosenberg"'),
            'lasry': las('"Spanien Varia", "Rosenberg"'),
            'edition': 'Juretschke and Kleinmann, Berichte der diplomatischen Vertreter des Wiener Hofes aus Spanien in der Regierungszeit Karls III. (Madrid, 1970s): '
                       'identified in the earlier pass (snippet view only); by its title and index it prints the envoys\' Berichte, while this unit is letters to '
                       'Rosenberg. Not opened.',
            'literature': 'No study of cipher in this unit found (earlier pass and this one).',
        },
        'key_check': 'No key held for the Vienna-Madrid embassy ciphers of 1757-64.',
        'duplicates': 'No other unit with shelfmark 58-1-1; catalogue 1723 (58-1-4, Firmian) and 1737 (58-1-5, Starhemberg) are siblings with other senders.',
    })

# ---------------------------------------------------------------- 1726: no verdict
add(1726, None, None,
    'Not assessed: "Originalberichte aus Madrid an den Kabinetts-Sekretaer Baron Neny und Weisungen an Lebzeltern" (1765-68) are exactly the envoys\' reports '
    'that Juretschke/Kleinmann, Berichte der diplomatischen Vertreter des Wiener Hofes aus Spanien vols. III-IV, would print, and no copy of those volumes is '
    'online; an open verdict would rest on an unanswered edition check.',
    'archive', 'AIS 4328197 re-read by curl: French, "teilweise verschluesselt", no extent, no scan. Needs a library copy of Juretschke III-IV.')

# ---------------------------------------------------------------- 1220: no verdict
add(1220, None, None,
    'Not assessed: still a cluster of 68 Hungaricana regests (Hungaricana returns 403 to scripts) with no single document chosen. New fact: Fazekas, Fodor and '
    'Glueck, Reports of the Habsburg Envoys in Constantinople 1568-1574 (Budapest 2025) prints Karl Rijm\'s despatches to 1 Nov 1574 (contents and preface PDFs '
    'on tti.abtk.hu read 16 Nov 2026), so the 1573-74 part of this lead may be in print; the documents themselves are not online.',
    'archive', 'HHStA Tuerkei I Kt. 29-36, no scans in AIS. Needs item selection, the 2025 edition\'s documents section, and scans.')

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proposals.json')
json.dump(P, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(P), 'proposals:', {k: v['verdict'] for k, v in P.items()})
