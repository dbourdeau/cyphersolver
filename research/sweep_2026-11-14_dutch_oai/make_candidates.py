import json
G = 'https://harvest.archieven.nl/OAI/OAIHandler?verb=GetRecord&metadataPrefix=oai_ead&identifier='
SRC = 'archieven.nl OAI-PMH (harvest.archieven.nl, oai_ead), Dutch regional archives, rest-of-sets harvest, 14 Nov 2026'
PRIOR = ('open as far as checked (14 Nov 2026): known.py on the fonds name and inventory number finds nothing in catalogue.json, '
         'leads.json, the targets or any sweep; no DECODE, Tomokiyo or Lasry search made in this sweep')


def row(year, date, lang, region, period, title, corr, place, shelf, fn, cls, status, why, imp, sol, dif, verify, guid, label, access, prior=PRIOR):
    return {'year': year, 'date': date, 'language': lang, 'region': region, 'period': period, 'title': title,
            'correspondents': corr, 'place': place, 'shelfmark': shelf, 'folio_note': fn, 'cls': cls, 'status': status,
            'why': why, 'importance': imp, 'solvability': sol, 'difficulty': dif, 'verify': verify,
            'links': [{'href': G + guid, 'label': label}], 'source': SRC,
            'score_note': 'Scored from the one-line EAD inventory entry in the archieven.nl OAI feed '
                          '(research/sweep_2026-11-14_dutch_oai/); not viewed',
            'prior_art': prior, 'seen': 'catalogue', 'needs_archive_scan': 'yes', 'access_note': access}


R = []
R.append(row(
    1783, '14 Oct 1783', 'Dutch', 'Low Countries', '1701-1800',
    "J. van Meeteren (Dinther) letter to the Dordrecht patriot society 'De Vrijheid', 14 Oct 1783, 'gedeeltelijk in geheimschrift' (Pieter van Beest papers)",
    "J. van Meeteren, Dinther -> Patriottisch Exercitiegenootschap 'De Vrijheid' (Pieter van Beest's papers)", 'Dinther / Dordrecht',
    "Regionaal Archief Dordrecht, toegang 325 (Patriottisch Exercitiegenootschap 'De Vrijheid'), inv. 44, section Pieter van Beest",
    "Inventory note: 'De brief is gedeeltelijk in geheimschrift'. The letter concerns another letter that was to be printed with an introduction",
    'B',
    "Finding aid as quoted (EAD from the OAI feed). A Dutch Patriot-period letter with a flagged cipher passage; no decipherment or scans seen.",
    "A rare Dutch Patriot-movement (1780s) item with a flagged cipher passage; probably a short substitution used for names, so a small but possibly quickly read piece. Part of the Van Beest papers, so check the neighbouring letters.",
    2, 3, 2,
    "Open inv. 44 in the Regionaal Archief Dordrecht (or its scan if any) and see whether the cipher is a letter substitution or numbers; look at the neighbouring inventory numbers in the Van Beest section for the same hand.",
    '921A504B14A74A67BC3993AE59712FD1', 'EAD, toegang 325 (OAI GetRecord)',
    'description only in the EAD; digitisation of inv. 44 not checked (Regionaal Archief Dordrecht, now Stadsarchief Dordrecht)'))
R.append(row(
    1594, '25 May 1594', 'Dutch', 'Low Countries', '1589-1598',
    "Copy of a report, 25 May 1594, of a meeting between Jan ten Buerenston and the nobleman Laurens Plouch about returning Groningen to the States General, 'gedeeltelijk in cijfers'",
    "Jan ten Buerenston and Laurens Plouch (as reported), Groningen 1594", 'Groningen',
    "Groninger Archieven, toegang 1032 (Catalogus), 'Verzameling van afschriften' (VVA), inv. 735; copy in vol. 62 of the Verzameling van stukken, p. 53",
    "Inventory note: 'Deze mededeeling is gedeeltelijk in cijfers'. The entry describes a copy (afschrift), so the ciphered original is elsewhere",
    'C',
    "Catalogue entry of a copy; the original (in the Groningen city or Ommelanden papers around the 1594 Reductie of Groningen) not identified.",
    "Cipher passages in a Groningen document of the weeks before the Reductie of Groningen (July 1594), when the city moved to the States General. Probably short numeric or symbol substitution inside Dutch text; the copy may have carried the cipher over unsolved.",
    2, 2, 3,
    "Find the original behind VVA inv. 735 (the entry points to vol. 62, p. 53 of the Verzameling van stukken) and see whether the cipher passages survive in the copy.",
    '186191573DB348E5AAB9FF18CE14E09D', 'EAD, toegang 1032 (OAI GetRecord)',
    'description only in the EAD; Groninger Archieven reading room or its digital collection'))
R.append(row(
    1594, '16 Dec 1589 - 8 Aug 1594', 'Dutch with Latin, Greek, German, French, Spanish and Hebrew-letter words', 'Low Countries', '1589-1598',
    "Journal of Johan Julsing, secretary of the city of Groningen, 1589-94: multilingual private diary with Hebrew-letter words; deciphered copy by W.B.S. Boeles attached ('Het geheime dagboek', Assen 2006)",
    "Johan Julsing (city secretary of Groningen), private diary", 'Groningen',
    "Groninger Archieven, toegang 835 (Catalogus), inv. 256",
    "Inventory note: manuscript damaged by damp; 'Een ontcijferd afschrift ... vervaardigd door Mr. W.B.S. Boeles, is erachter gevoegd'; edition 'Het geheime dagboek van Johan Julsing' (Assen 2006)",
    'C',
    "Already deciphered and published (Boeles copy; 2006 edition). The 'cipher' is script mixing (several languages, Hebrew letters), not a key; listed so that nobody re-finds it as an open cipher.",
    "Kept only as a duplicate guard and as a possible script-mixing control: a 16th-century private diary in several languages with Hebrew-letter words, with an existing decipherment. Probably not a cipher in the cryptographic sense.",
    1, 1, 2,
    "Check Assen 2006 for how 'geheim' is meant: coded text or just private, multilingual writing.",
    '7A1304C5BA034D8997C73AB530C03BD7', 'EAD, toegang 835 (OAI GetRecord)',
    'description only in the EAD; Boeles copy bound with the manuscript; scans not checked',
    prior='deciphered copy by W.B.S. Boeles attached to the manuscript; edited Assen 2006 (per the inventory note); no further search made'))
R.append(row(
    1850, 'undated (19th c. assumed)', 'Dutch', 'Low Countries', '1801-1900',
    "Masonic cipher papers of the lodge 'La Flamboyante', Dordrecht: 'Stukken betreffende het maconniek geheimschrift' (inv. 803) and 'Aantekeningen in geheimschrift' (inv. 847), undated",
    "Freemasons' lodge 'La Flamboyante', Dordrecht", 'Dordrecht',
    "Regionaal Archief Dordrecht, toegang 383 (Vrijmetselaarsloge 'La Flamboyante'), inv. 803 (Documentatie) and 847 (items unconnected with the archive)",
    "Two undated items: inv. 847 is notes 'in geheimschrift', inv. 803 is documentation on the Masonic cipher",
    'C',
    "Finding aid as quoted. Probably the standard Masonic (pigpen) alphabet, which is read at sight; both items belong to one lodge archive, so one group.",
    "Lodge notes in a Masonic cipher: a pigpen-type monoalphabetic cipher, low difficulty, little historical value without a date.",
    1, 5, 1,
    "Open inv. 847 and 803 and check the cipher type and the date of the notes.",
    'E15A1476101948B49EC9DCBCCB34A252', 'EAD, toegang 383 (OAI GetRecord)',
    'description only in the EAD; digitisation not checked'))
R.append(row(
    1871, '1871', 'Dutch', 'Low Countries', '1801-1900',
    "'Geheimschrift' sheet signed J. M. Sijtsma, 1871: a matrix alphabet (each line shifted one position), Nanninga and related families",
    "Jene M. Sijtsma (1852-1876)", 'Groningen province',
    "Groninger Archieven, toegang 561 (Familie Nanninga en aanverwante families), inv. 439, under Familie Sijtsma / Jene M. Sijtsma",
    "Inventory: 'Geheimschrift. Blad met matrix waarin het alfabet is geschreven. Per regel verspringen de letters een positie'",
    'C',
    "Finding aid as quoted. A Vigenere-type tableau (a youth cipher alphabet); a key table only, no message in the entry.",
    "A teenage cipher tableau; useful only if a message by the same hand turns up in the same family papers (neighbouring inventory numbers not checked).",
    1, 4, 1,
    "Open inv. 439 and its neighbours in toegang 561 for a message enciphered with the tableau.",
    'B237FD7AA56C4E3E92E1C2D96BA94B13', 'EAD, toegang 561 (OAI GetRecord)',
    'description only in the EAD; digitisation not checked'))
json.dump(R, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(R))
