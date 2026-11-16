"""Chrome wave 11 (15 Nov 2026): new Badator senders from the extra cipher terms -> candidates.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
LINK = {"href": "https://www.artxibo.euskadi.eus/webartxi00-container/es/ad53aArchivoHistoricoWar/badator/maintSimple?locale=es",
        "label": "Badator simple/advanced search (Coleccion Salazar y Castro; Archivo Municipal de San Sebastian)"}
SRC = ("Badator (artxibo.euskadi.eus) 'Exportar Busqueda' CSV exports of the terms cifrado, cifrada, cifradas, cifras, clave, descifrado, "
       "descifrar, abecedario (text records only), run in Chrome 15 Nov 2026, wave 11; one download per fresh tab")
marin = json.load(open(os.path.join(HERE, 'marin_narrowed.json'), encoding='utf-8'))
rows = [dict(
    year=1523, date="1522-1525", period="1497-1559", language="Spanish, Italian", region="Spain", cls="C",
    title="Fernando Marin, abbot of Najera (imperial agent with the army in Lombardy) -> Charles V, letters wholly or partly in cipher without a filed decipherment, 1521-25",
    correspondents="Fernando Marin, abad de Najera -> Charles V", place="Milan, Lombardy army camps", shelfmark="Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-22, A-27, A-28, A-30 and the Apendice B documents",
    folio_note=("Index lists 58 cipher letters of this sender; most carry a decipherment filed with them (a 'Texto descifrado' leaf, marginal or between the lines) and are left out. "
                "Letters without one (date, volume, folios; none is in the Calendar of State Papers Spain either): " + marin['list'] + ". The three most heavily enciphered: A-22 f.200 ('gran parte en cifra, muy estropeado'), A-27 ff.45-48 ('en su mayor parte en cifra, en italiano') and A-27 ff.453-456 (two copies, 'en su mayor parte en cifra'); the rest carry a paragraph or a few lines in cipher."),
    status="Index description only (Badator export, 15 Nov 2026); the ciphertext is in the RAH volumes and no image is linked from the Badator record. The filed decipherments of his other letters are the crib source for this one key.",
    why="One writer on one cipher over four years, with 40-odd decipherments filed for his other letters: the plaintext/ciphertext pairs of the same key sit in the same volumes as the letters left open.",
    importance=3, solvability=3, difficulty=3, score_note="Scored from the index wording (15 Nov 2026, wave 11); no leaf seen",
    verify="Ask the RAH (Madrid) for images of A-22 f.200, A-27 ff.45-48 and 453-456 and the filed 'Texto descifrado' leaves of the same man.",
    links=[LINK], source=SRC, ark="", needs_archive_scan="yes", seen="catalogue"),
    dict(
    year=1566, date="31 Oct 1560 - 30 Dec 1569", period="1560-1589", language="Spanish", region="Spain", cls="C",
    title="Philip II and Secretary Zayas -> Frances de Alava, ambassador in Paris: about 50 'cifrada' letters, 1560-69 (San Sebastian municipal archive)",
    correspondents="Philip II; Gonzalo Perez de Zayas -> Frances de Alava y Beamonte", place="Madrid / Paris", shelfmark="Archivo Municipal de San Sebastian (Donostiako Udal Artxiboa), Archivo de los Marqueses de San Millan y Villalegre, vol. 2, legajo 2 (inventory records 68 ff.)",
    folio_note="52 records in the Marqueses de San Millan y Villalegre inventory (1940), each a letter described as 'Cifrada', 'Toda cifrada', 'Cifrada casi toda' or 'Parte cifrada', Philip II autograph signature; no decipherment is mentioned in the descriptions. Dates from 31 Oct 1560 to 30 Dec 1569, mostly 1564-69.",
    status="Index description only (Badator export, 15 Nov 2026). A 1991 edition exists (Rodriguez and Rodriguez, 'Don Frances de Alava y Beamonte: correspondencia inedita de Felipe II con su embajador en Paris, 1564-1570', Instituto Doctor Camino / Caja Gipuzkoa), not seen: it very probably prints the deciphered texts, which would make the series read.",
    why="A one-writer, one-correspondent cipher run of Philip II's French embassy, held outside Simancas; Philip II's cipher for Paris is known to be a general cifra with changes (AGS Estado 1401 f.224, 1571).",
    importance=2, solvability=2, difficulty=3, score_note="Scored from the index wording (15 Nov 2026, wave 11); edition not seen",
    verify="Consult the 1991 edition: whether the cipher letters are printed deciphered.",
    links=[LINK], source=SRC, ark="", needs_archive_scan="yes", seen="catalogue")]
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows))
