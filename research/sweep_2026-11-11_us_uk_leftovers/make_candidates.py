"""Builds candidates.json, key_leads.json and catalogue_corrections.json for the 11 Nov 2026 US/UK leftovers sweep.

python3 research/sweep_2026-11-11_us_uk_leftovers/make_candidates.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BY = 'claude cloud sweep 11 Nov us_uk_leftovers'
CDM = 'https://cdm15999.contentdm.oclc.org/digital/collection/SCMisc/id/'
IIIF = 'https://cdm15999.contentdm.oclc.org/digital/iiif/SCMisc/%s/full/1200,/0/default.jpg'

# Searches run on 11 Nov 2026 for the Terranova -> Sfondrati letters of 1583 (BYU).
SF_SEARCHES = [
    {'query': 'WebSearch: Sfondrati family letters 1583 Carlo d\'Aragona Tagliavia Paolo Sfondrati cipher "Vault MSS 771" OR "Brigham Young" deciphered',
     'result': 'Nothing on the BYU letters: hits were Mary Stuart, Ferdinand of Aragon (CNI 2018), Valle de la Cerda and other unrelated decipherments.'},
    {'query': 'WebSearch: duque de Terranova gobernador de Milán 1583 cartas cifradas Paolo Sfondrato embajador Saboya Turín cifra descifrado',
     'result': 'Scalisi, "La correspondencia del duque de Terranova" (Libros de la Corte, 2023: his government 1580-86, Escorial papers) and a 1583 instruction by Scipio di Castro; no decipherment of letters to Sfondrati. The Scalisi PDF sits behind an Anubis bot check on revistas.uam.es and was not opened.'},
    {'query': 'WebSearch: "Paolo Sfondrati correspondence" BYU "Vault MSS 518" Carlo d\'Aragona Tagliavia letter 1583 October code',
     'result': 'Only the SNAC stub for BYU "Paolo Sfondrati correspondence" and a CCFr record of a copy of Sfondrato to Philip II, 13 Dec 1582; no study, transcription or decipherment of the 5 Oct 1583 letter.'},
    {'query': 'WebSearch: "Add MS 28418" Sfondrato embajador Saboya Felipe II cartas descifradas 1583 Terranova cifra',
     'result': 'BL Add MS 28418: "copies and decipherings of letters from Paolo Sfondrato, Count of Riviera, Spanish ambassador at Turin, to Philip II and Juan de Idiaquez", 1580-85. That is Sfondrati\'s own outgoing mail in the royal cipher, not Terranova\'s letters to him; a place to look for the same cipher, no reading of this letter.'},
    {'query': 'DECODE RecordsList search (curl, cmd=search): Sfondrati; Terranova; Tagliavia; Brigham',
     'result': 'Sfondrati 0, Tagliavia 0, Brigham 0. Terranova 1: R9318, a key headed "Duca di Terranova" in Munich, BayHStA Kurbayern Äußeres Archiv 4591 f. 95 (no ciphertext, not these letters).'},
    {'query': 'cryptiana.web.fc2.com: spanish2, spanish2A-C, spanish3, savoy, savoy2, italian .htm fetched and grepped for Terranova / Sfondrat',
     'result': 'No occurrence of either name on any of the eight pages.'},
]

SF_PRIOR = {
    'decode': 'DECODE RecordsList searched 11 Nov 2026 for Sfondrati, Tagliavia and Brigham (0 records each) and Terranova (1: R9318, a "Duca di Terranova" key at Munich, BayHStA KAA 4591 f. 95). No record of this letter or of any BYU item.',
    'tomokiyo': 'Fetched cryptiana spanish2, spanish2A, spanish2B, spanish2C, spanish3, savoy, savoy2 and italian.htm and grepped for Terranova and Sfondrat: no hit. The repo copy unsolved.htm has neither name.',
    'lasry': 'targets/gramont1529/GL.htm (the repo copy of Lasry\'s list) grepped for Sfondrat, Terranova, Tagliavia: no hit; the web searches returned no Lasry or DECRYPT paper on Milan-Turin Spanish traffic of 1583.',
    'edition': 'No edition or calendar of Terranova\'s letters to the ambassador in Savoy was found. Scalisi\'s 2023 article on Terranova\'s correspondence (Escorial papers) is a study, not an edition; its PDF was not opened (Anubis check on revistas.uam.es). BL Add MS 28418 holds contemporary decipherings of Sfondrati\'s own letters to Philip II, a different side of the correspondence.',
    'literature': 'Web searches on Terranova/Sfondrato with cifra/descifrado and on the BYU shelfmarks returned no cryptologic or historical paper reading these letters; BYU\'s item notes say only "Portions of letter written in code".',
}

rows = []
key_leads = []
corrections = []

rows.append({
    'year': 1583, 'date': '5 Oct 1583',
    'title': 'Carlo d\'Aragona Tagliavia, duke of Terranova (governor of Milan) → Paolo Sfondrati, Spanish ambassador in Savoy: letter partly in cipher, Milan',
    'correspondents': 'Carlo d\'Aragona Tagliavia, duke of Terranova → Paolo Sfondrati, baron of Valsassina',
    'place': 'Milan', 'language': 'Spanish', 'region': 'Spain', 'period': '1560-1589',
    'shelfmark': 'Brigham Young University, L. Tom Perry Special Collections, Vault MSS 518 (Paolo Sfondrati correspondence), folder 3, item 2',
    'folio_note': '4 page images (CONTENTdm SCMisc 53906, pages 53902-53905); p. 1 has 5 lines of clear Spanish then about 17 lines of cipher, continued on p. 2',
    'cls': 'B',
    'status': 'BYU item note: "Portions of letter written in code." Viewed 11 Nov 2026: no decipherment on the leaf. Same hand, cipher and month as the 13 cipher letters of Vault MSS 771 (catalogue 2077); folder 3 of MSS 518 holds 38 more Terranova letters of 1583 in clear. Not on DECODE.',
    'why': 'The governor of Milan to Philip II\'s ambassador at Turin in the weeks of the Savoy marriage negotiations and the Saluzzo question; it belongs with catalogue 2077 and should be worked with it.',
    'importance': 3, 'solvability': 4, 'difficulty': 3,
    'score_note': 'Scored from the page images during the 11 Nov 2026 US/UK leftovers sweep (research/sweep_2026-11-11_us_uk_leftovers/); pages 1-2 viewed at 900 px',
    'verify': 'Transcribe with the 2077 set (about 30 cipher pages in all, clear passages in the same letters as cribs). Test the DECODE key R9318 ("Duca di Terranova") and compare BL Add MS 28418 (decipherings of Sfondrati\'s own letters, 1580-85).',
    'links': [{'label': 'BYU digital item (MSS 518 f. 3 item 2)', 'href': CDM + '53906'},
              {'label': 'Page 1 image (IIIF)', 'href': IIIF % '53902'},
              {'label': 'BYU finding aid entry', 'href': 'https://archives.lib.byu.edu/repositories/14/archival_objects/62602'}],
    'seen': 'image', 'source': 'US/UK leftovers sweep 11 Nov 2026 (BYU CONTENTdm)',
    'prior_art': 'open (checked 11 Nov 2026: DECODE search, cryptiana Spanish/Savoy/Italian pages, Lasry list, web searches; no decipherment found)',
    'needs_archive_scan': 'no',
    'access_note': 'Images open on cdm15999.contentdm.oclc.org (IIIF, no login); the host answers from this network though it timed out on 3 Nov',
    'vetting': {
        'date': '2026-11-11', 'by': BY,
        'seen': {'kind': 'scan',
                 'where': 'BYU CONTENTdm SCMisc 53906, IIIF pages 53902 and 53903 downloaded at 900 px and read',
                 'extent': 'p. 1: about 17 lines of cipher after 5 clear lines; p. 2: 3 more cipher lines, the dating clause "De Milan a 5 de 8bre 1583" and the signature',
                 'cipher': 'Spanish chancery cipher of the Philip II type: numbers (8, 11, 14, 17, 33, 38, 58 ...), small letter signs with dots and strokes above, two-letter groups (re, xa, be, ge) and three-letter words (hom, sim, hol, vil, com, roe). No interlinear or marginal decipherment and no deciphered copy among the four images.'},
        'searches': SF_SEARCHES,
        'prior_art': SF_PRIOR,
        'key_check': 'No key is filed with the letter. Not tested: DECODE R9318 (Terranova key, Munich) and the Philip II general ciphers printed by Devos and on cryptiana spanish3.htm; no key was tried in this pass.',
        'key_held': 'DECODE R9318, key headed "Duca di Terranova" (BayHStA Kurbayern Äußeres Archiv 4591 f. 95): not tested, date and correspondent unknown. BL Add MS 28418 (decipherings of Sfondrati\'s letters 1580-85) may show the same nomenclator: not seen.',
        'duplicates': 'known.py "MSS 518", "Sfondrati", "Tagliavia": only catalogue 2077 (Vault MSS 771, the sibling set) and its sweep notes; this item (MSS 518 f. 3 item 2) is not in 2077. DECODE search: no record.',
        'verdict': 'open',
    },
})

corrections.append({
    'id': 2077,
    'what': 'Catalogue 2077 (BYU Vault MSS 771) was promoted as "not online". The images are online and were viewed on 11 Nov 2026; several fields are wrong.',
    'fields': {
        'title': 'Carlo d\'Aragona Tagliavia, duke of Terranova (governor of Milan) → Paolo Sfondrati, Spanish ambassador in Savoy: 13 letters of Aug-Sep 1583 mostly or partly in cipher',
        'correspondents': 'Carlo d\'Aragona Tagliavia, duke of Terranova → Paolo Sfondrati',
        'place': 'Milan', 'language': 'Spanish', 'region': 'Spain', 'period': '1560-1589',
        'date': '14 Aug - 26 Sep 1583',
        'folio_note': '13 of the 27 items carry cipher (items 6, 7, 9, 12, 13, 14, 16, 18, 19, 21, 25, 26: BYU notes "Most of the letter is written in code" on items 6, 9, 12, 14, 16, 21); 46 page images, roughly 30 with cipher',
        'needs_archive_scan': 'no', 'access': '(remove "archive")', 'seen': 'image',
        'access_note': 'Images open on cdm15999.contentdm.oclc.org (IIIF, no login)',
        'links_add': [{'label': 'Item 6, 14 Aug 1583 (most in cipher)', 'href': CDM + '50211'},
                      {'label': 'Item 6 page 1 (IIIF)', 'href': IIIF % '50207'},
                      {'label': 'BYU CONTENTdm search: Sfondrati', 'href': 'https://cdm15999.contentdm.oclc.org/digital/collection/SCMisc/search/searchterm/Vault%20MSS%20771'}],
    },
    'items': {'6': 50211, '7': 50679, '9': 50684, '12': 50229, '13': 50233, '14': 50238, '16': 50248, '18': 50254,
              '19': 50258, '21': 50266, '25': 50292, '26': 50283},
    'vetting_seen': {'kind': 'scan',
                     'where': 'BYU CONTENTdm SCMisc, the 12 compound objects listed in "items" (46 pages), all downloaded at 900 px and viewed on contact sheets; item 6 p. 1 (page 50207) read at full size',
                     'extent': 'about 30 pages with cipher; item 6 alone is 2.5 pages of solid cipher (22 lines on p. 1)',
                     'cipher': 'Spanish chancery cipher: numbers, letter signs with dots and strokes, two-letter groups and three-letter code words (hom, sim, cem, vil, hol, gal, roe). Letters open "Muy Illustre Señor" and are dated "De Milan"; addressed to the ambassador with the duke of Savoy. No marginal or interlinear decipherment on any page seen.'},
    'vetting_note': 'The earlier block called BL Add MS 28418 "a different person\'s correspondence": it is the same Paolo Sfondrati (ambassador at Turin), his letters to Philip II with decipherings, so it is a source for the cipher. DECODE R9318 is a "Duca di Terranova" key (Munich). Searches and prior_art as in this sweep\'s MSS 518 row.',
    'searches': SF_SEARCHES,
})

key_leads.append({
    'title': 'Niccolò Sfondrati (bishop of Cremona, later Gregory XIV) → Paolo Sfondrati, 20 letters from the Council of Trent, 13 Nov 1561 - 5 Mar 1562, cipher passages with the decipherment in the margin',
    'shelfmark': 'Brigham Young University, L. Tom Perry Special Collections, Vault MSS 521, folder 1, items 4-8, 11-13, 15, 21-23, 26, 31, 33, 36, 38, 40-42',
    'note': 'BYU: "Portions of text written in code, with de-coded text in margin." Viewed item 4 (pages 48291-2) and item 31 (48252-3): letter-and-digit cipher runs (e.g. "8ff5xfda..."), contemporary marginal decipherment. Read at the time, so not a candidate; the pairs give the family cipher of 1561-62 in full. Italian.',
    'links': [{'label': 'Item 4, [1561] Nov 13', 'href': CDM + '48295'}, {'label': 'Item 31, 2 Feb 1562', 'href': CDM + '48256'}],
})
key_leads.append({
    'title': 'Key headed "Duca di Terranova" (DECODE R9318)',
    'shelfmark': 'Munich, BayHStA, Kurbayern Äußeres Archiv 4591 f. 95',
    'note': 'Found by DECODE search "Terranova". Candidate key for catalogue 2077 and the MSS 518 row here; not tested.',
    'links': [{'label': 'DECODE record 9318', 'href': 'https://de-crypt.org/decrypt-web/RecordsView/9318'}],
})

exec(open(os.path.join(HERE, 'more_rows.py')).read()) if os.path.exists(os.path.join(HERE, 'more_rows.py')) else None

for name, data in (('candidates.json', rows), ('key_leads.json', key_leads), ('catalogue_corrections.json', corrections)):
    json.dump(data, open(os.path.join(HERE, name), 'w'), indent=1, ensure_ascii=False)
    print(name, len(data))
