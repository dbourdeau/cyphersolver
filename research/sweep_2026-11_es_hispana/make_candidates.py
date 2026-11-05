# Builds candidates.json for the Hispana sweep of 2 Nov 2026 (see README.md). One row; all rows are leads.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
r = dict(
    year=1610, date='1610-1611 (four undated-in-print leaves; others of the series 27 Jan - 23 Jul 1610/11)',
    title="Philip III → Rodrigo Niño Laso, conde de Añover: reales cédulas in cipher (four with no decipherment bound in)",
    correspondents='Philip III (secretary Antonio de Aróstegui) → Rodrigo Niño Laso, conde de Añover, Consejo de Guerra',
    place='Lerma / Madrid', language='Spanish', region='Spain', period='1601-1700',
    shelfmark='Madrid, Biblioteca Histórica (Ayuntamiento de Madrid), I 242,29 (Hispana idBib 58678726, Memoria de Madrid 424541); siblings Hispana idBib 58438217, 58438218, 58678720',
    folio_note='I 242,29 = 2 leaves, ff. 53 and 60 of the bound volume; 5-page PDF; 12 lines; numeric groups with a few letter syllables',
    cls='B',
    status="Hispana/Memoria de Madrid records 'Real cédula cifrada'. Page 2 of the scan viewed: whole page of 2-4 digit groups mixed with a few letters (la, de, fal, ba), no interlinear or banderilla decipherment. Eight sibling cédulas of the same series have the decipherment bound in on a slip (banderilla), which gives cribs.",
    why="Philip III's cipher to the Spanish commander in Flanders during the Condé flight and the Dutch truce talks; same series has eight glossed leaves, so a key can be rebuilt from siblings.",
    importance=3, solvability=4, difficulty=2,
    score_note='Scored from the scan (page 2 of I 242,29 viewed in Chrome, 2 Nov 2026) and from the Hispana records of the series',
    verify='Read the glossed siblings (idBib 58438206, 58438211, 58438294, 58678722, 58678826, 58678829, 58678890, 58678891) for a key, then apply it to 58678726, 58438217, 58438218, 58678720.',
    links=[{'label': 'Memoria de Madrid viewer', 'href': 'https://www.memoriademadrid.es/view/424541/'},
           {'label': 'Hispana record', 'href': 'https://hispana.mcu.es/es/registros/registro.do?idBib=58678726&tipoRegistro=MTD'}],
    seen='image', source='Hispana sweep (Chrome), 2 Nov 2026',
    prior_art='open as far as checked (2 Nov 2026: known.py no hit for Añover/Niño Laso/Biblioteca Histórica; 2 web searches found nothing on this series; Tomokiyo page on Philip III ciphers not read; Lasry and DECODE: nothing in local dumps)',
    needs_archive_scan='no', access_note='scans public on memoriademadrid.es, Creative Commons, no login')
json.dump([r], open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
