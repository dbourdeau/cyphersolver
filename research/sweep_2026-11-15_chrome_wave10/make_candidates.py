"""Chrome wave 10 (15 Nov 2026): Badator export (RAH Salazar y Castro index) -> candidates.json (one lead per sender/key).
Needs badator_groups.json (badator_groups.py)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(HERE, 'badator_groups.json'), encoding='utf-8'))
SRC = ("Badator (artxibo.euskadi.eus, Archivo Historico de Euskadi) 'Exportar Busqueda' CSV of the search 'cifra' "
       "(1,892 records), run in Chrome 15 Nov 2026, wave 10; the records reproduce the Salazar y Castro index (RAH, 49 vols, 1949-79)")
LINK = {"href": "https://www.artxibo.euskadi.eus/webartxi00-container/es/ad53aArchivoHistoricoWar/badator/maintSimple?locale=es",
        "label": "Badator simple search (term 'cifra', Coleccion Salazar y Castro)"}
rows = []


def fol(lst, cap=70):
    s = '; '.join(f'{d} {f}' for d, f, _ in lst[:cap])
    return s + (f'; ... and {len(lst) - cap} more' if len(lst) > cap else '')


def add(key, year, date, title, corr, place, lang, shelf, why, imp, sol, diff, extra, period='1497-1559', cls='C'):
    g = G[key]
    unf = g['unfiled']
    rows.append(dict(
        year=year, date=date, period=period, language=lang, region='Spain', cls=cls, title=title,
        correspondents=corr, place=place, shelfmark=shelf,
        folio_note=(f"Index lists {g['n']} cipher rows for this sender, of which {g['n_filed']} have a decipherment filed "
                    f"with the letter (marginal, interlinear or a 'Texto descifrado' leaf) or are duplicate copies of such a letter, and {len(unf)} do not. Letters without "
                    f"a filed decipherment (date, volume and folios): " + fol(unf) + ". " + extra),
        status=("Index description only (Badator export, 15 Nov 2026). The Salazar y Castro index quotes each record as 'Original, en cifra' "
                "or similar; the ciphertext is in the RAH volumes and no image is linked from the Badator record. No image seen. "
                f"{g['n_filed']} of the {g['n']} rows record a filed decipherment (or copy a deciphered letter), which the lead excludes and uses as a crib source."),
        why=why, importance=imp, solvability=sol, difficulty=diff,
        score_note="Scored from the index wording (15 Nov 2026, wave 10); no leaf seen",
        verify="Ask the RAH (Madrid) for images of the volume's cipher letters; check whether the filed decipherment leaves give a key.",
        links=[LINK], source=SRC, ark="", needs_archive_scan="yes", seen="catalogue"))


add('perez', 1526, '1524-1529',
    "Juan Perez, Charles V's secretary and (from 1527) ambassador at Rome -> Charles V, cipher letters without a filed decipherment, 1524-29",
    "Juan Perez (Rome) -> Charles V", "Rome", "Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-32 to A-44 (the index row dated 1572 at A-40 f.320 is 7 Apr 1527)",
    "The largest single-sender cipher run in the 1520s Rome correspondence of Charles V (the Sack of Rome year), by one writer on one key; the letters with a filed decipherment give cribs. The Calendar of State Papers (Spain) quotes some of these with their decipherments.",
    3, 3, 3, "Near-duplicate copies ('Ejemplar duplicado', 'triplicado') are separate sheets in the index and are counted. Alonso Sanchez, Lope de Soria and Lope Hurtado have their own targets and are not included.")
add('caracciolo', 1527, '1524-1529',
    "Marino Caracciolo, protonotary and imperial envoy at Venice and in Italy -> Charles V and Gattinara, cipher letters without a filed decipherment, 1525-29",
    "Marino Caracciolo (Venice, Milan) -> Charles V / Mercurino de Gattinara", "Venice, Milan", "Italian, Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-34 to A-44",
    "A second large one-writer series of the 1525-29 war, by the man who became Cardinal Marino Ascanio Caracciolo (targets/caracciolo1537, whose 1537 cipher is Luo's Cifrario 38, a different cipher that may or may not descend from his 1520s one); the letters with a filed decipherment give cribs.",
    3, 3, 3, "Several letters are in Italian (the index says 'en italiano' for some). The 1537 Milan letters of the same man are in targets/caracciolo1537.")
add('herrera', 1526, '1525-1526',
    "Comendador Miguel de Herrera (Rome) -> Charles V, cipher letters 1525-26 without a filed decipherment",
    "Miguel de Herrera, alcaide of Pamplona -> Charles V", "Rome", "Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-36, A-37",
    "A short one-writer run (December 1525 triplicate, March-June 1526) in the same volumes as the Perez and Caracciolo letters.",
    2, 3, 3, "")
add('lannoy', 1523, '1522-1527',
    "Charles de Lannoy, viceroy of Naples -> Charles V, cipher letters 1522-27 without a filed decipherment",
    "Charles de Lannoy -> Charles V", "Naples, Gaeta, Rome", "Spanish, French",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-26, A-28, A-29, A-41",
    "A viceroy's own cipher to the emperor; the catalogue already holds his 10 Sep 1523 letter to Lope de Soria (a different recipient), and the index here has the letters to Charles V.",
    3, 3, 3, "The index says of one (A-29 f.41) 'cuyo texto descifrado no sigue a continuacion'. Kolosova's book is said to give Lannoy's own cipher (see the existing Lannoy entry).")
add('colonna', 1523, '1522-1523',
    "Prospero Colonna -> Charles V, three cipher letters, Dec 1522 - Jan 1523",
    "Prospero Colonna -> Charles V", "Lombardy", "Italian",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-27 and the Apendice B documents",
    "The imperial general Prospero Colonna's own cipher; one letter is four folios wholly in cipher, and the index notes that the few readable phrases are Italian.",
    2, 3, 3, "targets/sanchez1522 mentions Colonna in its text only.")
add('adorno', 1523, '1522-1524',
    "Girolamo and Antoniotto Adorno (Genoa) -> Charles V, cipher letters 1522-24 without a filed decipherment",
    "Gerolamo Adorno / Antoniotto Adorno, doge of Genoa -> Charles V", "Milan, Genoa", "Italian, Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-22, A-23, A-29, A-32",
    "Two Genoese correspondents of one family; the index separates Girolamo's 1522 letters from Antoniotto's 1523 ones, which are two keys unless a folio check shows otherwise.",
    2, 3, 3, "Split by writer after a folio check if the two use different ciphers (one-key rule). Hieronymus Adorno of the 1545 Turkei lead is a different man.")
add('adrian', 1522, '1522-1523',
    "Pope Adrian VI -> Charles V, cipher letters of 1522-23 (A-26, A-27)",
    "Adrian VI -> Charles V", "Rome (and on the journey)", "Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-26 f.58, f.331, f.337; A-27 f.172",
    "Four letters from the pope who had been Charles V's tutor and regent (targets/adrian1520 holds his earlier cipher as regent); the same secretary may use the same system.",
    3, 3, 3, "Compare with the Adrian VI to Charles V entry in the catalogue (Kolosova).")
add('tribulcio', 1653, '1652-1654',
    "Cardinal Teodoro Trivulzio (Tribulcis) -> Luis Mendez de Haro, five cipher letters, Rome 1652-54, none with a decipherment",
    "Cardinal Giovanni Giacomo Teodoro Trivulzio -> Luis Mendez de Haro", "Rome", "Spanish or Italian",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-98 f.127, 134, 135, 136, 137",
    "Every one of the five rows says the decipherment does not follow, so nothing is filed; one letter is torn and mutilated. Not among leads 1085-1090 (Sarmiento, Juan Jose, Medici).",
    2, 3, 3, "", period='1651-1700')
add('leopoldo', 1652, '1650-1656',
    "Archduke Leopold Wilhelm (Brussels) -> Luis Mendez de Haro and Philip IV, cipher letters 1650-56",
    "Archduke Leopold Wilhelm -> Luis Mendez de Haro / Philip IV", "Brussels, army camps", "Spanish",
    "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, A-92 and A-97",
    "Four to five letters of the governor of the Spanish Netherlands, marked as having no decipherment; Philip IV's 1653 answer in A-92 f.228 is also in cipher. Thomas Ernst's work on Ferdinand III's Leopold Wilhelm cipher is a different correspondence.",
    2, 3, 3, "", period='1651-1700')
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'candidates')
