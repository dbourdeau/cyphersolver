"""Build candidates.json for the Nov 2026 'half-done runs' sweep (research/sweep_2026-11_A_halfdone/).

    python research/sweep_2026-11_A_halfdone/make_candidates.py

Five rows, scored from archive descriptions (PARES description pages fetched 4 Nov 2026 with pares_desc.py; the
szukajwarchiwach detail pages read in Chrome the same day). None is viewed on an image.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Half-done runs sweep (Nov 2026)'
CHK = 'checked 4 Nov 2026: known.py on shelfmark and names, no hit'


def row(**kw):
    base = {'cls': 'C', 'seen': 'catalogue', 'source': SRC, 'needs_archive_scan': 'unknown'}
    base.update(kw)
    return base


rows = [
    row(
        year=1554, date='4 Jul 1554 (PARES creation date; letters undated, "S.F.")',
        title='Tierra Firme: five cipher letters, 13 folios (AGI Indiferente 737 no. 171); the first letter is deciphered in Panama 29',
        correspondents='Alvaro de Sosa, governor of Tierra Firme (first letter) and others → officials at Seville / Consejo de Indias',
        place='Tierra Firme (Panama)', language='Spanish', region='Americas', period='1497-1559',
        shelfmark='AGI, Indiferente General, 737, N.171 (PARES 300401); decipherment of letter 1 in AGI, Panama, 29, R.6, N.23',
        folio_note='"Cinco cartas cifradas. S.F. 13 f." Four of the five have no decipherment named; images online (PARES flags IMG).',
        cls='A',
        status=('PARES description (read 4 Nov 2026): "Cinco cartas cifradas ... Nota: El texto descifrado de la primera carta se halla en el '
                'legajo Panama,29,R.6,N.23 (Copia de carta de Alvaro de Sosa, Gobernador de Tierra Firme a los oficiales de Sevilla, 1554, '
                'Julio, 4. 2 + 2 f.)". So letter 1 has a clear copy (a crib) and letters 2-5 are open. Not on DECODE (known.py).'),
        why='A same-hand plaintext for the first letter gives a key for the other four, in an Indies cipher of the 1550s that nobody has published.',
        importance=3, solvability=4, difficulty=2,
        score_note='Scored from the PARES description during the Nov 2026 half-done runs sweep (research/sweep_2026-11_A_halfdone/); not viewed',
        verify=('Open PARES 300401 (13 folios), transcribe letter 1, align it with the clear copy in Panama 29 R.6 N.23 (PARES search '
                '"Panama,29,R.6,N.23"), then read letters 2-5 with the recovered table.'),
        links=[{'label': 'PARES Indiferente 737 N.171', 'href': 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/300401'}],
        prior_art=('open (%s; one web search on Alvaro de Sosa, Tierra Firme, 1554 and Indiferente 737 found no decipherment; '
                   'Tomokiyo and Lasry not searched)' % CHK),
        needs_archive_scan='no',
        access_note='Images on PARES, no login (the description page links the scans).',
    ),
    row(
        year=1917, date='1917',
        title='Russian Embassy in Rome: cipher telegrams on the Provisional Government and the Polish organisations (8 pp.)',
        correspondents='Russian Provisional Government / Foreign Ministry → Russian Embassy in Rome',
        place='Rome', language='Russian', region='Other', period='1901-1950',
        shelfmark='AAN, Komitet Narodowy Polski (zesp. 39), 2/39/0/13/2067 ("Archiwum poufne"; old mark Dzial X t.10)',
        folio_note='8 pages; microfilm no. 22793. Detail page says "Brak kopii cyfrowych".',
        cls='C',
        status=('Catalogue title: "Archiwum poufne. Telegramy szyfrowe otrzymane przez Ambasade Rosyjska w Rzymie o stosunku tymczasowego '
                'rzadu rosyjskiego do organizacji polskich." No decipherment noted; the file may hold only the deciphered text.'),
        why='Russian diplomatic cipher telegrams of 1917, kept by the Polish National Committee, on how the Provisional Government treated Polish bodies.',
        importance=3, solvability=1, difficulty=4,
        score_note='Scored from the catalogue description during the Nov 2026 half-done runs sweep (research/sweep_2026-11_A_halfdone/); not viewed',
        verify='Ask AAN for the microfilm (22793) or a scan; check first whether the pages are cipher groups or the clear translation.',
        links=[{'label': 'szukajwarchiwach', 'href': 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/5324621'}],
        prior_art='open as far as checked (%s; Tomokiyo, Lasry, editions not searched)' % CHK,
        needs_archive_scan='yes',
        access_note=('Not digitised (detail page, 4 Nov 2026). The search-list scan flag in the szh harvest said 1: for AAN units that flag '
                     'is not reliable.'),
    ),
    row(
        year=1940, date='1940-1941',
        title='Photocopies of secret cipher telegrams sent to I. J. Paderewski (AAN)',
        correspondents='Polish government in exile (London) and others → Ignacy Jan Paderewski, USA',
        place='London / New York', language='Polish, French, English', region='Poland-Lithuania', period='1901-1950',
        shelfmark='AAN, Archiwum Ignacego Paderewskiego (zesp. 100), 2/100/0/19/4508',
        folio_note='File no. 4508; page count not given. "Brak kopii cyfrowych".',
        cls='C',
        status='Catalogue title only: "Kserokopie tajnych szyfrogramow kierowanych do I. J. Paderewskiego". No decipherment noted.',
        why='Paderewski\'s last year, with the Sikorski government\'s secret telegrams; a modern cipher, but a closed file nobody has read.',
        importance=2, solvability=1, difficulty=4,
        score_note='Scored from the catalogue description during the Nov 2026 half-done runs sweep (research/sweep_2026-11_A_halfdone/); not viewed',
        verify='Request a scan from AAN. Paderewski\'s private code of 1922 is 2/100/0/5.2/1118 (a code book, held by lead 1892 notes).',
        links=[{'label': 'szukajwarchiwach', 'href': 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/5338933'}],
        prior_art='open as far as checked (%s; Tomokiyo, Lasry, editions not searched)' % CHK,
        needs_archive_scan='yes',
        access_note='Not digitised (detail page, 4 Nov 2026).',
    ),
    row(
        year=1919, date='Sep-Dec 1919',
        title='Paderewski cabinet: notebook of enciphered telegrams on the internal situation in Poland (48 pp.)',
        correspondents='Warsaw → Paris (Paderewski, peace conference), probably',
        place='Warsaw / Paris', language='Polish', region='Poland-Lithuania', period='1901-1950',
        shelfmark='AAN, Archiwum Ignacego Paderewskiego (zesp. 100), 2/100/0/4.15/781',
        folio_note='48 pages, a "zeszyt" (exercise book); "Brak kopii cyfrowych".',
        cls='C',
        status=('Catalogue title: "Depesze szyfrowane dotyczace przede wszystkim sytuacji wewnetrznej w Polsce; (zeszyt)". Sibling of the June-Aug 1919 '
                'file 2/100/0/4.15/779 (lead 1892 in research/leads.json). No decipherment noted.'),
        why='Same Warsaw-Paris cipher as file 779 over a second period; the two together give more text for one cipher.',
        importance=3, solvability=2, difficulty=4,
        score_note='Scored from the catalogue description during the Nov 2026 half-done runs sweep (research/sweep_2026-11_A_halfdone/); not viewed',
        verify='Request scans of 779 and 781 together; try the KNP cipher-section copies 2/39/0/2/256 (1919) as plaintext.',
        links=[{'label': 'szukajwarchiwach', 'href': 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/5335056'}],
        prior_art='open as far as checked (%s apart from sibling lead 1892; Tomokiyo, Lasry, editions not searched)' % CHK,
        needs_archive_scan='yes',
        access_note='Not digitised (detail page, 4 Nov 2026).',
    ),
    row(
        year=1633, date='2 Jun 1633 (letters); chapter undated, 1633',
        title='Genoa 1633: enciphered chapter of a Turin letter on the French king and the Cardinal-Infante, with a second copy and Melo\'s covering letters',
        correspondents='Francisco de Melo, extraordinary ambassador in Genoa → Count-Duke of Olivares; chapter from Turin',
        place='Genoa / Turin', language='Spanish', region='Italy', period='1611-1650',
        shelfmark='AGS, Estado, leg. 3591, ff. 176, 177 (Melo letters), 181 no. 2 (cipher chapter), 183 (second chapter copy)',
        folio_note='PARES ids 3681308, 3681252, 6174713, 3681402; all flagged with images.',
        cls='A',
        status=('PARES titles: 181,2 "Capitulo cifrado de carta proveniente de Turin con impresiones del rey de Francia ante la llegada a Italia del '
                'Cardenal-Infante"; 183 "Capitulo de carta ... " (same words, no "cifrado": probably the decipherment). So a cipher/clear pair, '
                'likely read at the time but not recorded. Outside the pares_ags Genoa rows (those start in 1638 and 1534-1603).'),
        why='A cipher chapter with its own clear copy on the Cardinal-Infante\'s march to Flanders (1633), a crib pair for the Genoa-Turin cipher of the 1630s.',
        importance=2, solvability=3, difficulty=2,
        score_note='Scored from the PARES hit list during the Nov 2026 half-done runs sweep (research/sweep_2026-11_A_halfdone/); not viewed',
        verify='Open PARES 6174713 and 3681402, compare the two; check that 183 is a deciphered copy, then look for the key in leg. 3591.',
        links=[{'label': 'PARES 181,2 cipher chapter', 'href': 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/6174713'},
               {'label': 'PARES 183 chapter', 'href': 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3681402'}],
        prior_art=('open as far as checked (%s; Tomokiyo, Lasry, HistoCrypt and the Genoa literature not searched)' % CHK),
        needs_archive_scan='no',
        access_note='Images on PARES, no login.',
    ),
]

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(rows), 'rows written')
