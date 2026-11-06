"""Build candidates.json for the Riksarkivet consular-volume paging sweep (6 Nov 2026).
Every image of 25 Maroccana and Turcica bihang (Algerica, Tunisica, Tripolitana) volumes was paged on 300-px contact
sheets, scored by two digit detectors, and suspects viewed at 800 px and cropped at 2400-2600 px (findings.md).
Wulff (Maroccana II/I, lead 2314), von Stauden (Maroccana I/I, lead 2318) and Molinari (Tunisica 7/2, lead 2260) are
already leads: their new image numbers are in findings.md, not here."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Riksarkivet consular volumes, full paging (Maroccana, Turcica bihang Algerica/Tunisica/Tripolitana; IIIF, Referer route), Nov 2026'
SCORE = ('Scored from a full paging of the volume (every image on 300-px contact sheets, two digit-run detectors, suspects at '
         '800 px, cipher pages cropped at 2400-2600 px) during the Riksarkivet consular sweep, 6 Nov 2026 '
         '(research/sweep_2026-11_riksarkivet_consuls/)')
ACCESS = ('scans public on Riksarkivet (sok.riksarkivet.se), no login; scripts need the header '
          'Referer: https://sok.riksarkivet.se/ for the lbiiif image route')
PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the shelfmark or the correspondents; '
         'DECODE, Tomokiyo, Lasry and the editions not searched for these letters')


def links(rec, man, imgs):
    out = [{'href': f'https://sok.riksarkivet.se/arkiv/{rec}', 'label': 'NAD record'} if rec else None,
           {'href': f'https://lbiiif.riksarkivet.se/arkis!{man}/manifest', 'label': 'IIIF manifest'}]
    out += [{'href': f'https://sok.riksarkivet.se/bildvisning/{man}_{i:05d}', 'label': f'image {i}'} for i in imgs]
    return [x for x in out if x]


WEST = {u['man']: u['id'] for u in json.load(open(os.path.join(HERE, '..', 'sweep_2026-11_riksarkivet_west', 'units.json'),
                                                   encoding='utf-8')) if u.get('man')}
TURC = {u['man']: u.get('id') for u in json.load(open(os.path.join(HERE, '..', 'sweep_2026-11_riksarkivet_turcica', 'units.json'),
                                                      encoding='utf-8')) if u.get('man')}

ROWS = [
    dict(
        year=1776, date='1775-1776',
        title="Consul Johan Magnus Wenström's despatches from Salé in a 3-digit consular code, deciphered between the lines "
              "(probable key to consul Wulff's bare cipher)",
        correspondents='Johan Magnus Wenström (Swedish consul, later consul general, at Salé and Tangier) -> the Kanslipresident '
                       'and the Kanslikollegium (Stockholm)',
        place='Salé (Morocco)', language='Swedish (cipher: 3-digit groups 100-799, comma-separated, in rows between clear lines)',
        region='Other',
        shelfmark='Riksarkivet, Diplomatica Maroccana, SE/RA/2112/II/II - IX (Generalkonsuln Johan Magnus Wenström i Tanger, '
                  'skrivelser 1775-1787)',
        folio_note='281 images (series R0003633), all paged. Cipher at 13 (Salé 6 Nov 1775), 15, 16 (6 Nov 1775), 18 (= 19, '
                   'second exposure; Salé 20 Feb 1776), 23, 24, 27 (Salé 15 May 1776). No cipher after May 1776.',
        cls='A',
        status='Catalogue: consul\'s letters, no mention of cipher. Glossed: on 13, 15, 16 (2600 px) the decipherment is written '
               'above each digit row (13: `sjö vid flera tillfällen nog orsakt igenom dess djerfhet` over `406658430188...`); on '
               '23, 24, 27 the digit rows are struck through with heavy strokes, the clear text written between. Groups '
               '`374,507`, `212,380`, `380` recur here and in consul Wulff\'s bare Salé string `4471683745073806223843` (lead 2314, '
               '1764-65), which splits as `447 168 374 507 380 622 384`; von Stauden\'s 1775 reports (lead 2318) use the same '
               'layout. Probably one Kanslikollegium consular code for Morocco 1764-76.',
        why='Glossed pairs from the same consulate a decade after Wulff: if the code is the same, Wenström\'s letters give the '
            'table to read Wulff\'s bare cipher of 1764-65 (the peace presents for the Sultan) and von Stauden\'s bare rows of 1775.',
        importance=3, solvability=5, difficulty=2,
        verify='Transcribe the glossed rows of 13, 15, 16, 18 into group/plaintext pairs; test the table on Wulff\'s bare strings '
               '(Maroccana II/I images 11-14, 17, 18, 22, 24) and on von Stauden\'s bare rows (Maroccana I/I images 76, 79); compare '
               'with Molinari\'s glossed Tunis groups (Tunisica 7/2, lead 2260).',
        links=links(WEST.get('R0003633'), 'R0003633', [13, 15, 16, 18, 23, 24, 27]),
    ),
    dict(
        year=1736, date='1736',
        title="Consul George Logie at Algiers: Swedish letters with 4-digit code words, the plain word written above each group",
        correspondents='George Logie (Swedish consul at Algiers), and a letter about him probably by his secretary -> the '
                       'Kanslikollegium / Kanslipresident (Stockholm)',
        place='Algiers', language='Swedish (code: underlined 4-digit groups 1000-1999 inside clear sentences)',
        region='Other',
        shelfmark='Riksarkivet, Diplomatica Turcica, bihang Algerica, SE/RA/2119/2119.2/2/2 (Svenska konsulers skrivelser, '
                  'Georg Logie, 1729-1739)',
        folio_note='526 images (series R0002319), all paged (267-526 again at 600 px). Code at 281-282 (letter signed George Logie, '
                   'Algiers 24 May 1736; signature on 283) and 300 (letter of June-July 1736, docket No. 162 of 12 July 1736 on 299). '
                   'Images 2-266 seen only at 300 px, where this form does not show.',
        cls='A',
        status='Catalogue: consul\'s letters, no mention of cipher. Glossed: every code group carries its plain word written above '
               '(2600 px crops of 281, 282, 300): `Signaler 1557.1126.1255.1655.1062`, `Deyen 1233` (in both letters), '
               '`Amiralen 1675.1324.1705.1655`, `Algierisk 1443.1657`, `Caparen 1311.1110.1712`, `Turcar 1297`, `Levanten 1259`, '
               '`Tractat 1584`, `Sverige 1531`. Words are spelled with several groups (syllables or a small nomenclator). No key in '
               'the volume.',
        why='An early Swedish consular code from the Barbary coast (two years after the 1729 Swedish-Algerian treaty), dated and '
            'glossed: key material for any bare Algiers letters of the 1730s.',
        importance=2, solvability=5, difficulty=2,
        verify='Collect the group/word pairs from 281, 282, 300; page 2-266 of this volume and Algerica 2/3 (R0002320) at 600 px for '
               'more letters in this code, glossed or bare; look for the table in the Kanslikollegium cipher collections.',
        links=links(TURC.get('R0002319'), 'R0002319', [281, 282, 299, 300]),
    ),
]

rows = []
for r in ROWS:
    r.setdefault('prior_art', PRIOR)
    r.update(source=SRC, score_note=SCORE, access_note=ACCESS, seen='image', needs_archive_scan='no',
             period='1701-1800')
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
