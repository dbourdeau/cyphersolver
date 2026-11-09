import json

def L(i, label):
    return {"href": "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/%s" % i, "label": label}

common = dict(language="Spanish", region="Spain", needs_archive_scan="no",
              source="Spain nobility / ACA sweep (PARES, AHN Diversos-Colecciones), 9 Nov 2026",
              seen="scan")

def pa(extra):
    return ("open as far as checked (9 Nov 2026): known.py on the signatura, PARES id and correspondents finds nothing; "
            "two web searches (shelfmark / correspondents with cifra, cifrada, descifrada) found no edition, study or "
            "decipherment; " + extra)

rows = [
    dict(year=1837, date="8 Sep 1837",
         title="Manuel Azuares (Carlist agent) to the Carlist Secretary of State: letter from London, partly in letter-substitution cipher, no. 780 (duplicate)",
         correspondents="Manuel Azuares -> encargado de la Primera Secretaria de Estado of the pretender Carlos V",
         place="London", period="1801-1900",
         shelfmark="Madrid, AHN, DIVERSOS-COLECCIONES,161,N.2 (PARES 3735838)",
         folio_note="12 pages, 12 images; cipher runs on image 3 (lines 2-3 of the text) and image 5 (six lines of letters)",
         cls="A",
         status="PARES: 'La carta esta parcialmente cifrada' (news of the court of Maria II of Portugal after the Carlist success near Madrid). Images seen: cipher runs written in letters inside clear Spanish, plus some digit groups ('4607229'). No interlinear or marginal decipherment on the leaves seen (images 1-3, 5, 8 of 12); a duplicate copy, so the original may be elsewhere in the fonds.",
         why="Carlist foreign-agent correspondence of the First Carlist War in a letter cipher with clear context on both sides of every run, so cribs are plentiful (court of Maria II, Lisbon, Dona Maria de la Gloria). Sister of N.5 (same fonds, same year).",
         importance=3, solvability=4, difficulty=2,
         score_note="Images viewed 9 Nov 2026 (pares.cultura.gob.es, zoom 10): cipher confirmed on image 3 and image 5.",
         verify="Read all 12 images; compare with N.5 (Villafranca, St Petersburg, Aug 1837) and the other Carlist items of volume 161 (correspondencia carlista).",
         links=[L(3735838, "PARES description (DIVERSOS-COLECCIONES,161,N.2)")],
         access_note="images online without login (PARES ViewImage.do, dbCode 30041306)",
         prior_art=pa("PARES describes the cipher but gives no decipherment")),
    dict(year=1837, date="12-21 Aug 1837",
         title="Marques de Villafranca (duke of Medina Sidonia): two letters from St Petersburg for the Carlist cause, the second enclosing a long sheet in cipher explaining the key",
         correspondents="Pedro Alvarez de Toledo, marques de Villafranca -> encargado de la Primera Secretaria de Estado of the pretender Carlos V",
         place="St Petersburg", period="1801-1900",
         shelfmark="Madrid, AHN, DIVERSOS-COLECCIONES,161,N.5 (PARES 3738591)",
         folio_note="4 documents, 20 pages/images; image 14 is the '2o pliego', a full page of dotted single letters, 14 lines, each letter struck through by a diagonal pen stroke",
         cls="A",
         status="PARES: 'La segunda carta adjunta un extenso pliego en cifra, explicando con detalle la clave usada'. Image 14 seen: lines of single letters separated by dots (a.c.ll.b.f.o.q...; 'll' counted as one letter), clearly an enciphered sheet; image 3 is clear text about the embassy and the Ambassadors of France and England. No decipherment seen on images 1-3, 8, 12, 14, 17, 20.",
         why="A long running cipher sheet (several hundred letters, a Spanish alphabet with ll and n-tilde) from a Carlist envoy at the Russian court; the covering letters give context. If the sheet explains its own key it may be partly self-reading.",
         importance=3, solvability=3, difficulty=3,
         score_note="Images viewed 9 Nov 2026: cipher confirmed on image 14 ('2o pliego').",
         verify="View images 4-20 for the key explanation; compare with N.2 (Azuares, London): same fonds, possibly the same Carlist cipher.",
         links=[L(3738591, "PARES description (DIVERSOS-COLECCIONES,161,N.5)")],
         access_note="images online without login (dbCode 30041338)",
         prior_art=pa("none found")),
    dict(year=1840, date="6 May 1840",
         title="Juan Van Halen to the acting commander of the Division auxiliar del Norte: Igualada letter with a numeric cipher passage (Ejercito de Cataluna, Brigada de Reserva)",
         correspondents="Juan Van Halen (general, Isabelline army of Catalonia) -> brigadier, comandante accidental de la division auxiliar del Norte",
         place="Igualada (Barcelona)", period="1801-1900",
         shelfmark="Madrid, AHN, DIVERSOS-COLECCIONES,195,N.14 (PARES 4151130)",
         folio_note="3 images (cover, 2 pages); about 120 numbers on image 2, 16 on image 3",
         cls="A",
         status="PARES: 'Carta cifrada'. Images seen: the letter is clear except for five runs of dot-separated numbers 1-34 and 70 (70 perhaps a space or null). No decipherment on the leaves.",
         why="A short numeric cipher of the First Carlist War with plain context (Tarragona, Cervera, Solsona, Llacuna) that gives cribs; a quick win and a sibling for other Isabelline army ciphers.",
         importance=2, solvability=5, difficulty=1,
         score_note="Images viewed 9 Nov 2026: numeric cipher confirmed on images 2 and 3.",
         verify="Count distinct numbers, test simple substitution with a space symbol; the plain words around the runs give cribs.",
         links=[L(4151130, "PARES description (DIVERSOS-COLECCIONES,195,N.14)")],
         access_note="images online without login (dbCode 30062480)",
         prior_art=pa("Van Halen's biography and Baroja's book not checked for the letter")),
    dict(year=1875, date="1875 (series from 8 Jan 1875)",
         title="Ramon Garcia Montes (Carlist colonel) to Nicolas Candalija: cipher letters, with the cipher alphabet for transcribing them, in the Toreno papers",
         correspondents="Ramon Garcia Montes -> Nicolas Candalija (and Francisco de Borja Queipo de Llano)",
         place="Valencia / Albacete / Murcia (per index terms)", period="1801-1900",
         shelfmark="Toledo, AHNOB, TORENO,C.71,D.35-59 (PARES 4036228)",
         folio_note="25 documents; no images online",
         cls="B",
         status="PARES: 'Incluye cartas cifradas de Ramon Garcia Montes, enviadas a Nicolas Candalija ... y alfabeto cifrado para la transcripcion de las cartas'. No decipherment mentioned; the key (alphabet) is in the series.",
         why="Third Carlist War cipher letters with their own key in the same bundle: letters plus key make a straightforward reading once photographed.",
         importance=2, solvability=5, difficulty=1,
         score_note="Scored from the PARES description; not viewed (no images).",
         verify="Ask the Archivo Historico de la Nobleza (Toledo) for photographs of D.35-59.",
         links=[L(4036228, "PARES description (TORENO,C.71,D.35-59)")],
         access_note="description only on PARES; reproduction on request from AHNOB (Toledo)",
         prior_art=pa("none found"),
         seen="catalogue", needs_archive_scan="yes"),
]
for r in rows:
    for k, v in common.items():
        r.setdefault(k, v)
json.dump(rows, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

keys = [
    dict(year=1635, date="1635", title="Clave del cifrado general del ano 1635 (to be sent to Cardinal Gaspar de Borja) and a particular cipher given to Diego de Saavedra for Bavaria",
         shelfmark="Toledo, AHNOB, OSUNA,C.3456,D.108 and D.109 (PARES 6449391, 6449434)",
         note="Key-only items in the duque de Arcos papers, next to the Ronquillo cipher letters of 1646 (C.3456,D.102-106). Images online.",
         links=[L(6449391, "PARES D.108"), L(6449434, "PARES D.109")]),
    dict(year=1600, date="c. 1600", title="Cifras empleadas por el Cardenal Borja Velasco en su correspondencia",
         shelfmark="Toledo, AHNOB, OSUNA,C.844,D.20 (PARES 3927628)", note="Key-only; no images online.", links=[L(3927628, "PARES")]),
    dict(year=1700, date="undated", title="Tabla para descifrar determinados documentos",
         shelfmark="Toledo, AHNOB, LUQUE,C.307,D.113 (PARES 3993075)",
         note="Key-only; images online; already listed as a key lead in research/pares_ags.", links=[L(3993075, "PARES")]),
]
json.dump(keys, open('key_leads.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
