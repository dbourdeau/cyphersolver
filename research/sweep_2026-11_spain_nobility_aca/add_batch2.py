import json
base = 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/'
row = dict(
    year=1837, date="29 May - 16 Sep 1837 (letters nos. 726-747)",
    title="Conde de Alcudia (Vienna) to the Carlist Secretaries of State Sierra and Arias Teijeiro: twelve letters, several wholly in letter cipher, tens of pages",
    correspondents="Conde de Alcudia (Carlist envoy at Vienna) -> Wenceslao Maria de Sierra and Jose Arias Teijeiro, encargados of the Primera Secretaria de Estado of the pretender Carlos V",
    place="Vienna", language="Spanish", region="Spain", period="1801-1900",
    shelfmark="Madrid, AHN, DIVERSOS-COLECCIONES,161,N.1 (PARES 3735700)",
    folio_note="61 images (about 12 letters and covers); clear letters nos. 726, 727, 744, 745 on images 3-8, 14-18; cipher on images 11-12 (no. 728, 2 pages), 20-24 (no. 746) and 25-36 and later (no. 747, 'cuatro pliegos' of cipher, over 12 pages seen), more beyond image 40 not opened",
    cls="A",
    status="PARES: 'Varias cartas estan cifradas' (nine letters to Arias Teijeiro, 2-15 Sep 1837, three to Sierra, 29 May 1837). Images seen (1-40 of 61): each cipher letter is a run of single letters (about 18-20 distinct, x, g, y, b, l, p, t, m frequent) with no word spaces, written over whole pages, interleaved with letters in clear that carry the same news (Don Carlos's expedition, the Estella court, correspondence routes). No decipherment, interlinear or marginal, on any leaf seen. Same fonds, same year and same hand type of cipher as N.2 (Azuares) and N.5 (Villafranca) from the first batch (merged as leads 2421-2424).",
    why="By far the largest ciphertext in the Carlist-war volumes of the Deposito de la Guerra: several thousand letters in one or two related monoalphabetic or nomenclator-light systems, with plain letters of the same date as cribs and the matching Carlist court context. A joint attack with N.2 and N.5 (same correspondents' office) could give one key for a whole file.",
    importance=4, solvability=4, difficulty=2,
    score_note="Images 1-40 viewed 9 Nov 2026 on contact sheets (pares.cultura.gob.es, zoom 10); cipher confirmed on images 11-12, 20-36. Images 41-61 not opened.",
    verify="Open images 41-61; type the cipher letters of nos. 728, 746, 747 and test frequency (index of coincidence) for a simple or homophonic substitution; use the clear letters nos. 726, 727, 744, 745 for crib context. Compare the cipher alphabet with N.2 (Azuares) and N.5.",
    links=[dict(href=base + "3735700", label="PARES description (DIVERSOS-COLECCIONES,161,N.1)")],
    access_note="images online without login (PARES ViewImage.do, dbCode via catalogo/show/3735700)",
    source="Spain nobility / ACA sweep, second pass (AHN Carlist series 'Correspondencia carlista', PARES contiene/3735630), 9 Nov 2026",
    prior_art="open as far as checked (9 Nov 2026): known.py (Alcudia, Arias Teijeiro, shelfmark) finds nothing; web searches on the correspondents and shelfmark with cifra/cifrada, and on Carlist cryptography, returned no edition, study or decipherment",
    seen="scan", needs_archive_scan="no")
cand = json.load(open('candidates.json', encoding='utf-8'))
if not any(r['shelfmark'] == row['shelfmark'] for r in cand):
    cand.append(row)
json.dump(cand, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump([row], open('candidates_batch2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
keys = json.load(open('key_leads.json', encoding='utf-8'))
k = dict(year=1837, date="26 Nov 1837 - 1838", title="Madrid, Direccion General del Cuerpo de Estado Mayor to the Ejercito de Reserva de Andalucia: reserved letters, one sending a cipher key ('adjunta clave')",
         shelfmark="Madrid, AHN, DIVERSOS-COLECCIONES,167,N.19 (PARES 3899002)",
         note="134 pages of clear 'reservado' letters (7 sampled); image 3 sends the recipient a key for ciphered correspondence, the key page itself not seen. Key-only if found; no ciphertext seen.",
         links=[dict(href=base + "3899002", label="PARES")])
if not any(x['shelfmark'] == k['shelfmark'] for x in keys):
    keys.append(k)
json.dump(keys, open('key_leads.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(cand), len(keys))
