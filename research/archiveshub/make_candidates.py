"""Build research/archiveshub/candidates.json (hand-written from the Archives Hub hits, 2 Nov 2026)."""
import json, os

H = 'https://archiveshub.jisc.ac.uk'
SRC = 'Archives Hub sweep'
NOTE = ('Scored from the archive description during the Nov 2026 Archives Hub sweep (research/archiveshub/); '
        'not viewed')


def row(**k):
    base = dict(seen='catalogue', source=SRC, score_note=NOTE, cls='C', difficulty=3)
    base.update(k)
    return base


CLIVE = H + '/search/archives/ac3230ba-1657-31b3-b49e-08d4bd9d7643'
rows = [
    row(year=1757, date='28 Apr - Jun 1757 (letters ff.54-67)',
        title='William Watts and Scrafton to Robert Clive, letters in cypher during the Plassey campaign (Clive Collection)',
        correspondents='William Watts (Murshidabad) and Mr Scrafton -> Robert Clive',
        place='Murshidabad / Calcutta', language='English', region='Other', period='1701-1800',
        shelfmark='BL Asia, Pacific and Africa Collections, Mss Eur G37/8/4 ff.54-67, 73-74 (cipher lists: Mss Eur G37/7/20 ff.1-13)',
        folio_note='ff.54-60 (7 ff.), ff.61-66 (6 ff.), f.67 letter in code on the articles of agreement with Mir Jafar, ff.73-74 (Scrafton, one in cypher); ff.70-72 (Select Committee, 23 Jun 1757) has a decryption attached = a ready crib',
        status='Hub wording: "Letters in cypher, probably in William Watts\' handwriting"; "Letter in code ... outlining the articles of the agreement with Mir Jafar"; "Two short letters from Mr Scrafton, one in cypher". Mss Eur G37/7/20 holds "Lists of cyphers ... numbered, i.e. 2d cypher dispatched to Mr Scrafton" with notes on how the codes were used (partial key, sibling). No decipherment is mentioned for ff.54-67, 73-74. known.py: no hits in repo or DECODE.',
        why='The secret negotiations that set up Clive\'s alliance with Mir Jafar before Plassey, with cipher lists and an attached decryption in the same collection.',
        importance=4, solvability=3, cls='B',
        verify='View the Mss Eur G37 images (BL Explore Archives and Manuscripts); read G37/7/20 for the lists; search the Plassey literature (Hill, Bengal in 1756-57; Forrest, Life of Clive) for printed decipherments.',
        links=[{'label': 'Hub: Clive Collection', 'href': CLIVE}],
        prior_art='Not searched beyond the Hub text and the repo ledgers (literature/web check still to do, 2 Nov 2026)',
        needs_archive_scan='unknown', access_note='BL Mss Eur; online images not confirmed from the Hub record'),
    row(year=1774, date='5 Jan 1768 - 30 Nov 1774',
        title='Philip Francis to Robert Clive, two letters, one partly in cypher (Clive Collection)',
        correspondents='Philip Francis -> Robert Clive', place='unknown', language='English', region='Other',
        period='1701-1800',
        shelfmark='BL Asia, Pacific and Africa Collections, Mss Eur G37/9/1 ff.7-10',
        folio_note='4 folios; one letter partly in cypher',
        status='Hub wording: "Two letters from P. Francis to Clive concerning events in India. One is partly in cypher." No decipherment mentioned. known.py: no hits.',
        why='Francis (Junius suspect, Hastings\'s rival) writing to Clive, with a short cipher passage.',
        importance=3, solvability=2, difficulty=4,
        verify='View the folios; check Parkes and Merivale, Memoirs of Sir Philip Francis (1867).',
        links=[{'label': 'Hub: Clive Collection', 'href': CLIVE}],
        prior_art='Not searched beyond the Hub text (2 Nov 2026)',
        needs_archive_scan='unknown', access_note='BL Mss Eur; online images not confirmed'),
    row(year=1750, date='c. 1750 (reports of Easter 9 - Easter 11 George II)',
        title='Law reports "in cipher", all central London courts (a volume of enciphered notes)',
        correspondents='unknown', place='London', language='English', region='England', period='1701-1800',
        shelfmark='Cambridge University Library MS Add.110 (old mark M.3.29)',
        folio_note='1 volume, about 216 folios; fo. 1 "enciphered notes in main hand"; ffos 1v-5v index in a second hand; fos 6, 7, 212v-216 blank',
        status='Hub title "Law reports in cipher"; scope note says enciphered notes in the main hand. Possibly shorthand or a private alphabet; no decipherment mentioned. The bibliography note says some cases appear in the published reports (a plaintext crib). known.py: no hits.',
        why='A whole volume of private cipher with printed parallels for the same cases.',
        importance=2, solvability=4, difficulty=3,
        verify='View on Cambridge Digital Library if digitised; decide shorthand vs substitution; match cases to the English Reports.',
        links=[{'label': 'Hub record', 'href': H + '/data/gb12-msadd.110'}],
        prior_art='Not searched beyond the Hub text (2 Nov 2026)',
        needs_archive_scan='unknown', access_note='CUL MS Add.110; digitisation not confirmed'),
    row(year=1730, date='c. 1730',
        title='Notes of mistakes in Reichenbach\'s cypher; notes of mistakes in a cypher (Hotham papers, Berlin mission)',
        correspondents='Sir Charles Hotham, 5th Bt (envoy to Berlin) and the Prussian circle',
        place='Berlin', language='unknown', region='Central Europe', period='1701-1800',
        shelfmark='Hull University Archives (Hull History Centre) U DDHO/3/19 and U DDHO/3/30',
        folio_note='1 item each, in the Hotham series U DDHO/3 (Berlin mission papers)',
        status='Hub item titles only. They are notes on errors in a cipher, not ciphertext, but they point to a Prussian (Reichenbach) cipher; neighbouring items in U DDHO/3 may hold the cipher letters and keys. known.py: Reichenbach appears only as a name in targets/schiner1516.',
        why='Hotham\'s 1730 mission to Berlin (Frederick William I, the royal marriage plan) and its cipher traffic.',
        importance=3, solvability=2, difficulty=3,
        verify='Read the U DDHO/3 series list on the Hub for ciphered letters and keys; ask Hull for scans.',
        links=[{'label': 'Hub: Hotham papers', 'href': H + '/search/archives/dded631d-e0f4-34df-8da4-0c4ed02006cd'}],
        prior_art='Not searched beyond the Hub text (2 Nov 2026)',
        needs_archive_scan='yes', access_note='Hull History Centre; no online images indicated'),
    row(year=1830, date='1811-1847',
        title='John Urpeth Rastrick, notes and calculations in his "private cipher" (civil engineer\'s papers)',
        correspondents='John Urpeth Rastrick (1780-1856)', place='unknown', language='English', region='England',
        period='1801-1900',
        shelfmark='Senate House Library MS325 (and AL340)',
        folio_note='MS325 about 100 items; "Many of the notes and calculations are written in Rastrick\'s private cipher"',
        status='MS325 scope note. A private cipher in engineering notebooks, so the plaintext is technical English with numbers. No decipherment mentioned. known.py: no hits.',
        why='Private cipher of an early railway and ironwork engineer with technical vocabulary as a crib.',
        importance=2, solvability=3, difficulty=3,
        verify='Ask Senate House Library for sample images; AL340 matched the same search words.',
        links=[{'label': 'Hub: MS325', 'href': H + '/search/archives/2da8b01d-bcbe-378d-97bc-e620ad6c6034'},
               {'label': 'Hub: AL340', 'href': H + '/search/archives/faf5bf02-d15e-3559-a006-3201af0f45b2'}],
        prior_art='Not searched beyond the Hub text (2 Nov 2026)',
        needs_archive_scan='yes', access_note='Senate House Library; reading room'),
    row(year=1889, date='Nov 1889 - Sep 1891 (about 12 items)',
        title='IBEA Co. and Emin Pasha Relief Expedition telegrams "in code" to and from Zanzibar (Mackinnon papers)',
        correspondents='William Mackinnon, P.L. McDermott, EPRE Committee, Inheritor (Zanzibar), Stanley',
        place='London / Zanzibar', language='English', region='Other', period='1801-1900',
        shelfmark='SOAS PP MS 1/EPRE/1/56/64, 67, 77, 89, 90, 284, 404, 407; PP MS 1/EPRE/1/22/27; PP MS 1/IBEA/1/23/3',
        folio_note='Single telegrams; 1/56/284 is "Telegram in code. No translation"; 1/22/27 is a "Decyphered telegram"; 1/12/44 mentions a code book left at Balinakill',
        status='SOAS descriptions. Most are catalogued with their gist, so the code is probably a commercial word code. Too short and keyless unless the code book survives. known.py: no hits.',
        why='Commercial telegraph-code traffic around the Emin Pasha relief expedition and the Tippu Tip claim.',
        importance=2, solvability=1, difficulty=4,
        verify='Check whether the telegram code book survives in the same papers; otherwise too short.',
        links=[{'label': 'Hub: Mackinnon papers', 'href': H + '/search/archives/97625e6e-7a88-3d89-a1c7-9be6222d7602'}],
        prior_art='Not searched (2 Nov 2026)',
        needs_archive_scan='yes', access_note='SOAS Special Collections'),
]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candidates.json')
json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows))
