# Builds candidates.json for the Milan state-archive sweep of 2 Nov 2026 (see README.md). Rows are leads, not catalogue entries.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
INV = 'https://web.archive.org/web/2024/https://archiviodistatomilano.cultura.gov.it/fileadmin/risorse/Patrimonio_archivistico/Fondi_e_Inventari/Visconteo-Sforzesco__1183-1593_/Potenze_sovrane_e_altre_voci-VS_2-1.pdf'
PRIOR = ('open as far as checked (2 Nov 2026: known.py, local ledgers, two web searches; Cerioni 1970 is the keys reference, not read; '
         'no scan or DECODE record seen for these items)')
R = [
 dict(year=1528, date='1494; 1526-1531 (Italian Wars) and later', title='Sforza chancery "Chiavi e cifrari", scat. 1591: cipher letters of the Italian Wars with keys (82 docs)',
      correspondents='Camillo Ghilini (Flanders), Paolo Sforza 1528, G. S. da Robbio (Cremona) 1530, Giorgio Andreasi (Mantua) 1528, Massimiliano Stampa 1527, Bartolomeo Landriano 1526, F. Taverna, conte della Somaglia 1527, Amico Taegio 1531; no. 43 a cipher letter to Ludovico il Moro 1494',
      place='Milan; various', language='Italian', region='Italy', period='1497-1559',
      shelfmark='Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, Cancelleria segreta, Chiavi e cifrari, scat. 1591 (82 docs; nos. 63-64 are DECODE R5297-R5298, see lead 1311)',
      folio_note='82 leaves; 1494-1736 per the inventory; cipher letters and keys mixed, number of cipher letters not stated', cls='B',
      status="Inventory (ASMi, Danelli; read from the Wayback copy 2 Nov 2026): 'chiavi di cifra, cifrari e alcune lettere in cifra'; no. 40 a cifra of 1736, no. 43 a cipher letter to Ludovico il Moro 1494. Not viewed: the ASMi host did not answer and no scan is online.",
      why='Letters of the war of the League of Cognac (1526-31) from named Milanese agents, mostly outside the 15th-century Cerioni edition; the keys in the same box give a route in.',
      importance=3, solvability=3, difficulty=3, score_note='Scored from the ASMi inventory text, not from a scan (Nov 2026 Milan sweep)',
      verify='Order scans from ASMi (as-mi@cultura.gov.it) or find the DECODE records beyond R5297-98; apply the keys in the box and Cerioni 1970.',
      links=[{'label': 'ASMi inventory VS 2/1 (Wayback), p. 216-217', 'href': INV}], seen='catalogue', source='ASMi inventory via Wayback', prior_art=PRIOR,
      needs_archive_scan='yes', access_note='no scans online found; ASMi site unreachable 2 Nov 2026'),
 dict(year=1460, date='1455-1467 (single lines)', title='Sforza ducal family letters with cipher lines, Potenze sovrane (Bianca Maria, Galeazzo Maria, Francesco I)',
      correspondents='Pietro Cotta (signed cipher message); Bianca Maria, Galeazzo Maria and Francesco Sforza',
      place='Milan area', language='Italian', region='Italy', period='1451-1500',
      shelfmark='Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, Potenze sovrane: scat. 1457 no. 353; scat. 1458 nos. 69, 116-117, 128, 149, 186 (1465-66); scat. 1459 no. 317 (1467); scat. 1462 no. 17 (1455)',
      folio_note='short cipher passages in family letters; extent not stated', cls='C',
      status="Inventory lists 'messaggio in cifra firmato da Pietro Cotta', 'alcune righe in cifra' and 'documento in cifra'. Not viewed; not on the DECODE records checked.",
      why='Cipher lines inside Sforza family letters of the 1460s: possible short crib material next to the Cerioni keys.',
      importance=2, solvability=2, difficulty=3, score_note='Scored from the ASMi inventory text (Nov 2026 Milan sweep)', verify='Order scans; compare with the 1465-67 keys in Cerioni 1970.',
      links=[{'label': 'ASMi inventory VS 2/1 (Wayback)', 'href': INV}], seen='catalogue', source='ASMi inventory via Wayback', prior_art=PRIOR,
      needs_archive_scan='yes', access_note='no scans online found; ASMi site unreachable 2 Nov 2026'),
]
with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)
print(len(R))
