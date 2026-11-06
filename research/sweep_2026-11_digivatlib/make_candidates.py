"""Build candidates.json for the DigiVatLib / BAV manuscripts OPAC sweep (6 Nov 2026). See README.md.
Rows come from opac.vatlib.it item records; two were opened on DigiVatLib IIIF and seen bare, the rest are
undigitised (manifest 404) and need archive photos."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'BAV manuscripts OPAC (opac.vatlib.it/mss) item records + DigiVatLib IIIF, DigiVatLib sweep, Nov 2026'
SEEN_SCORE = ('Scored from the DigiVatLib IIIF images viewed during the DigiVatLib sweep, 6 Nov 2026 '
              '(research/sweep_2026-11_digivatlib/)')
CAT_SCORE = ('Scored from the BAV OPAC item record only, 6 Nov 2026 (research/sweep_2026-11_digivatlib/); '
             'volume not digitised (IIIF manifest 404), not viewed')
ACCESS_DIG = ('digitised on DigiVatLib; IIIF manifest https://digi.vatlib.it/iiif/MSS_<shelfmark>/manifest.json, '
              'images by canvas label (plain GET works from this network, 6 Nov 2026)')
ACCESS_ARCH = ('not digitised (DigiVatLib manifest 404, OPAC "Not Digitized"); BAV reading room or a reproduction order')
PRIOR = ('open as far as checked (6 Nov 2026): known.py on the shelfmark and the correspondents finds nothing; '
         'catalogue.json and research/leads.json have no entry for the volume; DECODE, Tomokiyo, Lasry and the '
         'literature not searched')


def opac(item_id, label='BAV OPAC item record'):
    return {'href': f'https://opac.vatlib.it/mss/detail/{item_id}', 'label': label}


def dvl(sm):
    return [{'href': f'https://digi.vatlib.it/view/MSS_{sm}', 'label': 'DigiVatLib viewer'},
            {'href': f'https://digi.vatlib.it/iiif/MSS_{sm}/manifest.json', 'label': 'IIIF manifest'}]


ROWS = [
    dict(
        year=1524, date='26 [month in cipher] 1524 (the next leaf, f. 299r, is an extract dated Venice 24 June 1524)',
        title='Extract of a Mantuan agent\'s letter, 1524, half in a symbol cipher, no decipherment',
        correspondents='a Mantuan informant (name and place written in cipher in the heading) -> Federico II Gonzaga, '
                       'marquis of Mantua (captain general of the Church)',
        place='not stated (the heading names it in cipher; Venice or Rome likely)',
        language='Italian (clear text with cipher runs)', region='Italy', period='1497-1559',
        shelfmark='BAV, Vat. lat. 8214, f. 298r-v',
        folio_note='f. 298r full page (about 27 lines) and 298v (about 9 lines): clear Italian with cipher runs in almost '
                   'every line (letters, numerals and signs such as 7, 8, 9, x, a crossed 8 and a boxed sign); the heading '
                   '"Ex litt[eris] ... dat[is] ... 26 ..." has the writer, place and month in cipher. OPAC: "Al f. 298r, '
                   'lettera in cifra" in a volume of news letters sent to Federico II Gonzaga in 1523-1524.',
        cls='A',
        status='Bare: no interlinear, marginal or facing decipherment at 1200 px; f. 297v and 299r carry no key or gloss '
               '(299r is a clear extract of Jo. Batt. Malatesta, Venice, 24 June 1524).',
        why='An early-Cinquecento Gonzaga cipher with plenty of clear context around each run: a crib-rich target; '
            'the Gonzaga keys of the 1520s (ASMn, Archivio Gonzaga) may fit.',
        importance=3, solvability=4, difficulty=2,
        verify='Transcribe 298r-v at full size; compare the signs with the Gonzaga ciphers of 1520-1530 in the repo and on '
               'DECODE; solve from the clear context.',
        links=[opac('25568')] + dvl('Vat.lat.8214'),
        seen='image', score_note=SEEN_SCORE, access_note=ACCESS_DIG, needs_archive_scan='no',
    ),
    dict(
        year=1380, date='undated marginal note in a 14th-century codex (the note itself may be later)',
        title='One line of symbol cipher in the lower margin of a 14th-century Durand, Repertorium (Borghese papal library)',
        correspondents='unknown (a reader or owner of the codex)',
        place='unknown (the Borghese codices came from the Avignon papal library)', language='unknown (Latin likely)',
        region='Papacy', period='unknown',
        shelfmark='BAV, Borgh. 239, f. 16r (lower margin)',
        folio_note='About 26 signs in one line under the two text columns (signs like v, o, 3, +, d, 2, a crossed o, a long '
                   'dash, T, x, m, #, h). OPAC (from Maier, Codices burghesiani, 1952): "In margine inferiori f. 16r '
                   'alicuius scripturae cryptographicae specimen".',
        cls='B',
        status='Bare: nothing else on the page explains it; seen at 1600 px and in a crop at full size.',
        why='A pre-1425 cipher specimen in a papal-library codex; short, but a candidate for the oldest-cipher list.',
        importance=3, solvability=2, difficulty=3,
        verify='Transcribe at full resolution; date the hand of the note; try simple substitution and the Avignon '
               'curial alphabets (DECODE R23, R202-R204); look for more such notes in the codex.',
        links=[opac('214787')] + dvl('Borgh.239'),
        seen='image', score_note=SEEN_SCORE, access_note=ACCESS_DIG, needs_archive_scan='no',
    ),
    dict(
        year=1641, date='Madrid, 5 Feb 1641',
        title='Luis Revelo to Cardinal Francesco Barberini, original letter in cipher, 1641',
        correspondents='Luis Revelo (f. 1641-1642) -> Cardinal Francesco Barberini',
        place='Madrid', language='unknown (Italian or Spanish)', region='Papacy', period='1611-1650',
        shelfmark='BAV, Barb. lat. 9892, f. 313r',
        folio_note='One letter, f. 313r. OPAC: "Originale. In cifra." (no decipherment noted, unlike the "cifra e decifrato" '
                   'letters of the Barberini Spanish series).',
        cls='B',
        status='Catalogue only: the volume is not digitised. Bareness inferred from the note, which elsewhere in the '
               'series says "cifra e decifrato" when a decipherment is present.',
        why='A Madrid cipher letter to the Cardinal Nephew in the year of the Catalan and Portuguese revolts; '
            'the Barberini cifrari (Barb. lat. 9914-9915) are in the same fondo.',
        importance=3, solvability=3, difficulty=3,
        verify='Order a photo of f. 313r; compare with the Barberini cifrari in Barb. lat. 9914-9915 and with the Mancini '
               'cipher-and-decipher letters of 1644-55 (Barb. lat. 9848-9849, digitised).',
        links=[opac('204997')],
        seen='catalogue', score_note=CAT_SCORE, access_note=ACCESS_ARCH, needs_archive_scan='yes',
    ),
    dict(
        year=1666, date='22 Aug 1665 - 1 May 1666 (38 letters)',
        title='Domenico Giannuzzi to Marco Gallio, nuncio at Cologne: 38 letters of Roman court news, partly in cipher, with the cifrario enclosed',
        correspondents='Domenico Giannuzzi (f. 1665-1666) -> Mgr Marco Gallio, bishop of Rimini, nuncio in Cologne',
        place='Rome', language='Italian', region='Papacy', period='1651-1700',
        shelfmark='BAV, Borg. lat. 587, ff. 37r-231r passim (cifrario at f. 141r)',
        folio_note='38 original letters, ff. 37r-231r passim. OPAC: "In parte in cifra; a f. 141r, è accluso il cifrario."',
        cls='B',
        status='Catalogue only: not digitised. No decipherment is mentioned; the key is in the volume (f. 141r).',
        why='A run of cipher passages with their own key sheet: a quick reading once photographed, and a key for other '
            'Gallio nunciature traffic (Cologne 1659-1666).',
        importance=3, solvability=5, difficulty=1,
        verify='Order photos of f. 141r and a sample of the letters; check whether the cipher passages carry interlinear '
               'decipherments; then decipher with the enclosed key.',
        links=[opac('214437')],
        seen='catalogue', score_note=CAT_SCORE, access_note=ACCESS_ARCH, needs_archive_scan='yes',
    ),
    dict(
        year=1702, date='Madrid, 6 Jan 1701 - 31 Dec 1704',
        title='Giovanni Battista Facini, Barberini agent in Madrid, to Urbano Barberini and Giuseppe Valuta, 1701-1704: letters with cipher, no decipherments noted',
        correspondents='Giovanni Battista Facini (f. 1698-1705) -> Urbano Barberini, prince of Palestrina, and Giuseppe Valuta',
        place='Madrid', language='Italian', region='Papacy', period='1701-1800',
        shelfmark='BAV, Barb. lat. 9885 (ff. 1r-150r, 3r-152r) and Barb. lat. 9886 (ff. 1r-132r)',
        folio_note='Two volumes of signed letters, 1701-1702 and 1702-1704. OPAC general note: "Cifre" / "Firme autografe, '
                   'cifre", where Facini\'s own 1698-1700 volumes (Barb. lat. 9883-9884) say "Cifre e decifrati".',
        cls='B',
        status='Catalogue only: not digitised. The change from "cifre e decifrati" to "cifre" suggests the War of the '
               'Spanish Succession letters were filed without decipherments; unconfirmed.',
        why='Madrid news of 1701-1704 (accession of Philip V, the succession war) in the Barberini agent cipher; '
            'the glossed 1698-1700 letters of the same writer would give the key.',
        importance=3, solvability=4, difficulty=2,
        verify='Order a sample of each volume; confirm no decipherments; rebuild the key from Barb. lat. 9883-9884 '
               '("cifre e decifrati", same writer).',
        links=[opac('45722', 'BAV OPAC, Barb. lat. 9885 (to Urbano Barberini)'),
               opac('45718', 'BAV OPAC, Barb. lat. 9885 (to Valuta)'),
               opac('45723', 'BAV OPAC, Barb. lat. 9886')],
        seen='catalogue', score_note=CAT_SCORE, access_note=ACCESS_ARCH, needs_archive_scan='yes',
    ),
    dict(
        year=1669, date='Madrid, 1 and 11-12 Nov 1669',
        title='Domenico Millanta and the nuncio Federico Borromeo, Madrid 1669: three cipher pieces with no decipherment noted',
        correspondents='Domenico Millanta (Barberini agent) <-> Federico Borromeo (nuncio in Spain 1668-1670)',
        place='Madrid', language='Italian', region='Papacy', period='1651-1700',
        shelfmark='BAV, Barb. lat. 9863, f. 479r and ff. 505r-507r',
        folio_note='f. 479r Millanta to Borromeo, 1 Nov 1669, copy, OPAC "Cifra"; ff. 505r-507r Borromeo to Millanta, '
                   '11 and 12 Nov 1669, OPAC "Cifre". The rest of the volume is Millanta\'s "cifre e decifrati".',
        cls='C',
        status='Catalogue only: not digitised. "Cifra" on a copy may name a clear copy of a cipher letter; unconfirmed.',
        why='Nuncio-to-agent cipher in Madrid: a different key from the Barberini agent series, possibly the nunciature\'s.',
        importance=2, solvability=3, difficulty=3,
        verify='Order photos; see whether the pieces are ciphertext or clear copies; compare with the Spagna nunciature '
               'keys of the 1660s.',
        links=[opac('179010', 'BAV OPAC, f. 479r'), opac('178981', 'BAV OPAC, ff. 505r-507r')],
        seen='catalogue', score_note=CAT_SCORE, access_note=ACCESS_ARCH, needs_archive_scan='yes',
    ),
]

rows = []
for r in ROWS:
    r.update(source=SRC, prior_art=PRIOR)
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
