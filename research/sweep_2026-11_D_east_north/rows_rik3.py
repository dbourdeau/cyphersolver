import sys, io, contextlib
sys.stdout.reconfigure(encoding='utf-8')
from cand import add
if True:
    from rows_rik import row
rows = [
    row('R0003637', '1wvyAzfQqL3W6GbBAfICcD', [227, 482, 29, 86, 114, 397, 539], year=1742, date='1742',
        title="Höpken and Carlson (Constantinople) to the chancery president, 1742: French and Swedish passages in four-digit code with interlinear plaintext",
        correspondents='Carl Fredrik von Höpken and Edvard Carlson -> the chancery president (Gyllenborg) and the King', place='Constantinople', language='Swedish, French',
        period='1701-1800', shelfmark='Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/28 (Brev till kanslipresidenten, 1742)',
        folio_note='567 images (R0003637). Image 227: a French "extrait de la traduction" of a letter with whole lines of four-digit numbers and French written between them; image 482: a Swedish letter of 22 Sept 1742 with three number blocks glossed in Swedish; underlined interlinear passages also at about 29, 86, 114, 397, 539 (thumbnails).',
        cls='A', status='Catalogue: plain letters to the chancery president. Same four-digit code as the sibling volumes 9/20-9/23 and 9/29; glosses written over the numbers show the passages were read on receipt.',
        why='The last Höpken-Carlson volume (1742, after the Swedish defeat in Finland): the Ottoman side of the Hat government\'s foreign policy, with plaintext cribs for every passage.',
        importance=3, solvability=5, difficulty=2,
        verify='View images 227 and 482 at full size; transcribe, align numerals and glosses, and pool with 9/20-9/23 to rebuild the whole code.'),
]
for r in rows:
    add(r)
