# Builds candidates.json for the Hebrew-script sweep of 6 Nov 2026 (see README.md). Rows scored from PGP/CUDL descriptions and
# from the images viewed in this sweep. Same schema as research/sweep_2026-11_ottoman_turkish/candidates.json.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
PGP = 'https://geniza.princeton.edu/en/documents/'
IIIF = 'https://images.lib.cam.ac.uk/iiif/'
PRIOR = ('open as far as checked (6 Nov 2026: known.py, PGP, Cambridge Genizah blog, Bohak 2010; Tomokiyo, Lasry, DECODE '
         'have no Hebrew-script record; Elbaum has an unpublished partial key for NS J479; coordinate with the Princeton Geniza Project)')


def row(**k):
    base = dict(seen='image viewed', source='Hebrew-script sweep (Princeton Geniza Project + CUDL IIIF)', prior_art=PRIOR,
                needs_archive_scan='no', region='Other', language='Judaeo-Arabic / Hebrew script', cls='B')
    base.update(k)
    base['score_note'] = 'Scored in the Hebrew-script sweep (research/sweep_2026-11_hebrew/); images viewed 6 Nov 2026'
    return base


R = [
    row(year=1300, date='undated Geniza fragment, probably 12th-14th c. (unassessed)', title='Pen-trial bifolio with word-divided cipher blocks in Hebrew letters and in invented glyphs',
        correspondents='unknown scribe', place='Fustat/Cairo (Geniza)', period='1251-1400', shelfmark='Cambridge University Library, T-S AS 187.240',
        folio_note='bifolio, recto and verso; roughly 30-40 short lines in cipher, in ruled-off blocks',
        status='PGP (2026): "section written in a cipher, merits examination, might be solvable based on the surrounding formulae". No edition. Not read.',
        why='Repeated formula lines in two systems (Hebrew-letter and glyph) give cribs; word division by dots; images fetchable by curl.',
        importance=3, solvability=3, difficulty=3,
        verify='Transcribe one block; test atbash, albam, ayak-bekar and the CUL Or.1080 J277 keys; then crib-seeded substitution. Ask A. Elbaum (PGP) whether it is already in hand.',
        links=[{'label': 'PGP 42435', 'href': PGP + '42435/'}, {'label': 'CUDL image (recto)', 'href': IIIF + 'MS-TS-AS-00187-00240-000-00001.jp2/full/full/0/default.jpg'}],
        access_note='CUDL IIIF works with plain curl'),
    row(year=1300, date='after mid-13th c. (cites al-Busiri, d. 1295); paper; Mamluk or Ottoman era per Elbaum', title='Judaeo-Arabic jottings in an idiosyncratic symbol cipher, both sides of one folio',
        correspondents='scribe signs "al-faqir Ishaq al-yahudi"', place='Egypt (Geniza)', period='1251-1400', shelfmark='Cambridge University Library, T-S NS J479',
        folio_note='one folio, both sides full, text in several directions; about 22 recurring symbols, some Hebrew letters with more than one glyph',
        status='Not read. A. Elbaum (Princeton Geniza Project) tentatively mapped about 22 symbols to Hebrew letters, unpublished; two pornographic passages, one ending "all this is lies".',
        why='Cribs: signature repeated, two verses of the Burda (known text), a legal formula, the alphabet written several times. Images clean.',
        importance=3, solvability=3, difficulty=4,
        verify='Contact Elbaum for the mapping before starting; verify the date by paper and hand; plan the write-up around the content.',
        links=[{'label': 'PGP 8804', 'href': PGP + '8804/'}, {'label': 'CUDL image (recto)', 'href': IIIF + 'MS-TS-NS-J-00479-000-00001.jp2/full/full/0/default.jpg'},
               {'label': 'Elbaum, Cambridge Genizah blog', 'href': 'https://genizahfragments.lib.cam.ac.uk/2022/06/22/qa-wednesday-secret-codes-and-erotic-prose-with-alan-elbaum/'}],
        access_note='CUDL IIIF works with plain curl'),
    row(year=1139, date='after 1 Nisan 1139 (about April-Dec 1139)', title='Yitzhaq b. Avraham Ibn Ezra (Spain) to Halfon b. Netanel ha-Levi: letter with Coptic-numeral code in three places',
        correspondents='Yitzhaq b. Avraham Ibn Ezra to Halfon b. Netanel ha-Levi', place='Spain to Egypt', period='1101-1150', shelfmark='Cambridge University Library, T-S 13J18.19 (India Book IV, 41)',
        folio_note='recto lines 11-12 and verso line 5; about 11 numerals on the verso, doubtful readings in PGP',
        status='Coptic numerals "presumably substituting for Hebrew letters, mechanism not determined" (PGP/Goitein-Friedman). Not read.',
        why='Oldest dated unread Hebrew-script cipher found; a numeral-for-letter key of this kind is in CUL Or.1080 J277 and Bodl. MS heb. f 102/28.',
        importance=2, solvability=2, difficulty=3,
        verify='Test the J277/f 102/28 Coptic-numeral key on the 11 verso numerals and the two recto lines; the plaintext is probably a name or a code word ("al-nun", "the elephant").',
        links=[{'label': 'PGP 9097', 'href': PGP + '9097/'}, {'label': 'CUDL image (recto)', 'href': IIIF + 'MS-TS-00013-J-00018-00019-000-00001.jp2/full/full/0/default.jpg'},
               {'label': 'Key specimen: PGP 34004 (CUL Or.1080 J277)', 'href': PGP + '34004/'}],
        access_note='CUDL IIIF works with plain curl'),
    row(year=1250, date='undated Geniza letter, probably 11th-13th c.', title='Letter from a son in Qus to his mother, lines 7-12 in cipher',
        correspondents='son in Qus to his mother in Fustat', place='Qus / Fustat', period='1101-1250', shelfmark='JTS, ENA 4100.7b',
        folio_note='six lines in cipher inside a Judaeo-Arabic letter; verso a second letter in mixed script', cls='C',
        status='PGP tags it "cipher, to examine"; noticed by O. Zinger; probably Judaeo-Arabic plaintext. Not read.',
        why='Short, but a family letter with predictable greeting formulae.',
        importance=2, solvability=2, difficulty=3,
        verify='Fetch the JTS image (via PGP/FGP; not tried); check whether it is Zinger\'s "every word begins with alef" letter, which would not be a plain substitution.',
        links=[{'label': 'PGP 11951', 'href': PGP + '11951/'}], access_note='JTS image route not tested', needs_archive_scan='yes'),
]

if __name__ == '__main__':
    with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf8') as f:
        json.dump(R, f, indent=1, ensure_ascii=False)
    print(len(R), 'rows')
