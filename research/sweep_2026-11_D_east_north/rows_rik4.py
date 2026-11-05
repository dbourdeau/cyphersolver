import sys
sys.stdout.reconfigure(encoding='utf-8')
from cand import add
from rows_rik import row
import json
v = {x.get('man'): x for x in json.load(open('rik_vols.json', encoding='utf-8'))}
spec = [
    ('R0003590', 1737, '1735-1739', '9/24', 'to the chancery president, 1735-39', [40, 106, 139, 205],
     '333 images (R0003590). Underlined interlinear number passages at about images 40, 106, 139, 205 (thumbnail size).', 3, 4),
    ('R0003628', 1740, '1740', '9/25', 'to the chancery president, 1740 (also Lillienberg and Troilius)', [8, 53, 99, 329],
     '463 images (R0003628). Image 8 shows a heavily underlined interlinear opening; images 53, 99 and 329 carry rows of numbers (thumbnail size).', 3, 4),
    ('R0003635', 1741, 'Jan-Jun 1741', '9/26', 'to the chancery president, Jan-Jun 1741', [147, 8, 54, 100, 240, 286],
     '468 images (R0003635). Image 147: a full page of rows of four-digit numbers with French plaintext between the rows; underlined interlinear passages also at about 8, 54, 100, 240, 286.', 4, 5),
    ('R0003636', 1741, 'Jul-Dec 1741', '9/27', 'to the chancery president, Jul-Dec 1741 (also Lillienberg)', [50, 93, 8, 135],
     '430 images (R0003636). Images 50 and 93: whole openings of number rows with writing between them; underlined interlinear passages at about 8 and 135.', 4, 5),
]
for man, yr, dates, vol, what, imgs, fol, imp, sol in spec:
    x = v[man]
    add(row(man, x['id'], imgs, year=yr, date=dates,
            title=f"Höpken and Carlson (Constantinople) {what}: four-digit code passages with interlinear plaintext",
            correspondents='Carl Fredrik von Höpken and Edvard Carlson -> the chancery president and the King', place='Constantinople', language='Swedish, French', period='1701-1800',
            shelfmark=f"Riksarkivet, Diplomatica Turcica, {x['ref']} ({x['caption']}, {x['date']})", folio_note=fol, cls='A',
            status='Catalogue: plain letters; cipher seen at thumbnail size only. Same hand and same four-digit code as the sibling volumes 9/20-9/23, 9/28 and 9/29; the numbers are glossed between the lines.',
            why='Sweden-Ottoman diplomacy in the run-up to the 1741 Russo-Swedish war; one more slice of the same code with plaintext cribs.',
            importance=imp - 1 if imp > 3 else imp, solvability=sol, difficulty=2,
            verify='View the listed images at full size; transcribe numerals and glosses and pool with 9/20-9/29.'))
