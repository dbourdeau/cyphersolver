"""Build candidates.json for the Italian state archives retry (6 Nov 2026).
Rows come from the ASF Mediceo avanti il Principato (MAP) images viewed during the sweep; see README.md."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'ASF Mediceo avanti il Principato (MAP) images + archive.org OCR of the MAP inventory, Italian state archives retry, Nov 2026'
SCORE = ('Scored from the MAP images viewed during the Italian state archives retry, 6 Nov 2026 '
         '(research/sweep_2026-11_italian_state_retry/)')
ACCESS = ('scans public on the ASF MAP site, no login, curl works: /map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc> and '
          'IIIF images from /iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif (1600 px max)')
PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza, the document or the correspondent; '
         'the Google Books feed shows these items only in the MAP inventory itself; DECODE, Tomokiyo and Lasry not searched. '
         'Marco Vito (Vienna) is working on encrypted MAP letters of 1486-1491 (research/medici_bia/README.md): check overlap.')
B = 'https://archiviodistatofirenze.cultura.gov.it'


def links(filza, doc, ids, ptif=None):
    out = [{'href': f'{B}/map/ricerca/ricerca-su-filza/?f={filza}&d={doc}&c=', 'label': f'MAP filza {filza}, doc. {doc}'}]
    out += [{'href': f'{B}/map/riproduzione/?id={i}', 'label': f'image id {i}'} for i in ids]
    if ptif:
        out.append({'href': f'{B}/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/{ptif}/full/full/0/default.jpg',
                    'label': 'IIIF image, recto'})
    return out


ROWS = [
    dict(
        year=1478, date='16 Jan 1478 (as written; Florentine style would make it 1479)',
        title="Giovanni Mazzinghi's cipher letter of 16 January 1478, bare; the same cipher is glossed in MAP 72/170 a week later",
        correspondents='Giovanni Mazzinghi -> (the Medici; addressee not named on the page)',
        place='not stated (Rome likely: the sibling letter reports papal news)', language='Italian (symbol cipher with clear words)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXXIX, doc. 142 (old c. 149)',
        folio_note='One leaf, recto full of cipher (about 45 lines, some clear words between runs); verso blank but endorsed '
                   '"1478 ... adi 16 di gennaio ... Gio. Mazinghi" and "Cifra". Inventory vol. 3: "Giovanni Mazzinghi. (cifrato). s. l., 1478 gen. 16, n. 142".',
        cls='A',
        status='No decipherment on, over or beside the cipher (checked at 1600 px). The sign set (x, ‡, H, =, 5-like signs) is the '
               'one of MAP LXXII doc. 170 (23 Jan 1478), which carries a full interlinear decipherment.',
        why='A pre-1497 Florentine cipher letter of the Medici circle in the months around the Pazzi conspiracy, unread on the page, '
            'with a glossed sibling in the same system: a short route to a reading.',
        importance=4, solvability=5, difficulty=2,
        verify='Transcribe MAP 72/170, build the key from its interlinear pairs, apply it to 89/142; check the date style and '
               "Mazzinghi's post (Rome?) in the letter itself.",
        links=links(89, 142, [94455, 94456], '00100089/A0000463.ptif'),
    ),
    dict(
        year=1478, date='23 Jan 1478 (as written)',
        title='Anonymous cipher letter of 23 January 1478 with full interlinear decipherment (key source for Mazzinghi 89/142)',
        correspondents='anonymous -> anonymous (Medici circle)',
        place='not stated (Rome likely: pope, palace, papal briefs in the gloss)', language='Italian (symbol cipher with clear words)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 170 (old c. 202)',
        folio_note='One leaf, recto: about 40 lines, head "+ ... di gennaio 1478"; verso blank (show-through only). '
                   'Inventory vol. 3: "Anonimo (in cifra), ad anonimo. s. l., 1478 gen. 23, n. 170".',
        cls='B',
        status='Glossed: a second hand wrote the decipherment above nearly every cipher run. Read at the time. Same sign set as MAP 89/142.',
        why='Gives the key (letters and nomenclator) for the bare Mazzinghi letter of 16 Jan 1478 and for any other letter of this system.',
        importance=3, solvability=5, difficulty=1,
        verify='Transcribe cipher and gloss pairwise; rebuild the table; fold into the Mazzinghi row if the editor prefers one entry per key.',
        links=links(72, 170, [79506, 79507], '00100072/A0000397.ptif'),
    ),
    dict(
        year=1483, date='undated (filza XLVIII holds papers of 1482-83)',
        title='"Documento cifrato": a full page of symbol cipher, no date, address or gloss',
        correspondents='unknown -> (Lorenzo de\' Medici?)', place='unknown', language='unknown (symbol cipher; one clear phrase "Poi ...")',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XLVIII, doc. 214 (old c. 222)',
        folio_note='One leaf, recto: about 20 lines of cipher (letters, numerals and a dozen invented signs), a few clear words; verso blank. '
                   'Inventory vol. 2, p. 484: "Documento cifrato. s. d., n. 214" (the OCR prints it under filza XLVII; the leaf is in XLVIII).',
        cls='A',
        status='Bare: no interlinear or marginal decipherment (checked at 1272 px, the maximum). No decipherment filed next to it in the inventory.',
        why='An unread Laurentian-era cipher page; the MAP key sheets (filza LXXII nos. 178-188, LXXXII nos. 72 and 142, LXXXVII n. 414, '
            'XCVII n. 473) are the first keys to try.',
        importance=3, solvability=3, difficulty=3,
        verify='Transcribe; compare the sign set with the MAP key sheets and the Gabbrielli/Dieci keys; if none fits, homophonic solve.',
        links=links(48, 214, [60059, 60060], '00100048/A0000545.ptif'),
    ),
    dict(
        year=1490, date='undated (filza LXXII mixes papers of 1460s-1520s)',
        title='"Lettere in cifra": two all-cipher slips in one sign set, no clear word, no gloss',
        correspondents='unknown', place='unknown', language='unknown (symbol cipher with numerals and Greek-like signs)',
        region='Italy', period='unknown',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 213 and 214 (old cc. 256, 257)',
        folio_note='Two oblong slips, rectos only: 213 has two blocks (about 15 lines), 214 about 15 lines; versos blank. '
                   'Inventory vol. 3: "Lettere in cifra. n. 213; n. 214".',
        cls='A',
        status='Bare. Different sign set from the Rucellai 1482 cipher on doc. 207 of the same filza (which is deciphered by doc. 208).',
        why='Two unread cipher texts filed with the Medici key sheets of filza LXXII (nos. 178-188: Piero Alamanni, Baccio Ugolini, '
            'Paolantonio Soderini, Andrea Cambini, Agostino Biliotti ...), so a matching key may be in the same filza.',
        importance=3, solvability=4, difficulty=3,
        verify='View the key sheets LXXII 178-188 on the MAP site and match sign sets; transcribe both slips.',
        links=links(72, 213, [79620, 79621, 79622, 79623]),
    ),
    dict(
        year=1494, date='undated (filza LXXIII: papers of c. 1491-94)',
        title='"Poscritto in cifra": an 8-line cipher postscript ending in clear words',
        correspondents='unknown -> (Piero di Lorenzo de\' Medici?)', place='unknown', language='Italian (symbol cipher; clear tail)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIII, doc. 371 (old c. 413)',
        folio_note='One slip, recto: 8 lines of cipher and a clear close; verso blank. Inventory vol. 3: "Poscritto in cifra. s. d., n. 371".',
        cls='B',
        status='Bare (no gloss seen at 800 px). Filza LXXIII also holds a clear "Copia di cifrato" (n. 354) of another text.',
        why='Short unread cipher of the last Laurentian / Piero years; the clear tail gives a crib.',
        importance=2, solvability=3, difficulty=3,
        verify='Fetch at 1600 px; transcribe; try the Lyon/Vigevano 1493-94 keys rebuilt from the decifrati in filze LXXIV-LXXV.',
        links=links(73, 371, [81019, 81020]),
    ),
    dict(
        year=1494, date='undated per the inventory; foot date read as "... 1459" or "1499" (unclear at 1,364 px)',
        title="Letter attributed to Piero di Lorenzo de' Medici to a Florentine ambassador in France, partly in cipher",
        correspondents="Piero di Lorenzo de' Medici (per the inventory) -> a Florentine ambassador at the French court",
        place='unknown', language='Italian (clear text with short code groups)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XVII, doc. 211 (old c. 223)',
        folio_note='Two pages of cursive; only short code groups in the text. Inventory vol. 1: "(In parte in cifra), s. d., n. 211".',
        cls='C',
        status='No gloss seen. The cipher share is small and the attribution and date need checking against the hand.',
        why='Possible Medici-France cipher of the 1490s; low value until the cipher share is measured.',
        importance=2, solvability=2, difficulty=3,
        verify='Read the clear text to fix sender and date; list the code groups.',
        links=links(17, 211, [19271, 19272]),
    ),
]

rows = []
for r in ROWS:
    r.update(source=SRC, score_note=SCORE, access_note=ACCESS, prior_art=PRIOR, seen='image', needs_archive_scan='no')
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
