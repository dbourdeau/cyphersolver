"""Build candidates.json (and key_leads.json) for the Czech Chrome pass (6 Nov 2026).

Follow-up to research/sweep_2026-11_czech_slovak/ for the portals that needed a browser (SOA Litoměřice,
SOA Třeboň, ZA Opava) and the Gallas thesis. Row format follows research/sweep_2026-11_czech_slovak/make_candidates.py.

The Piccolomini rows were found through Václav Vlnas's 2017 Hradec Králové BA thesis (theses.cz/id/p3p2kb), whose
appendix zip (P_lohy_A_a_B.zip, 90 photographs of microfilm frames from RA Piccolomini, SOA Zámrsk) was opened in
Chrome's memory and every frame looked at (README, "Piccolomini microfilm frames"). Only the frames with ciphertext and
no contemporary decipherment on them are rows; the glossed siblings are named in each row as key material.
known.py was run on the shelfmarks and correspondents of every row: no hits.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Czech regional archives, Chrome pass (SOA Litoměřice, SOA Třeboň, ZA Opava, theses.cz), Nov 2026'
SCORE_SEEN = ('Scored from the photographs in the appendix of Vlnas 2017 (theses.cz/id/p3p2kb), viewed frame by frame in '
              'Chrome on 6 Nov 2026 (research/sweep_2026-11_czech_chrome/)')
SCORE_DESC = 'Scored from a citation in a 2026 thesis (research/sweep_2026-11_czech_chrome/); not viewed'
VLNAS = {'href': 'https://theses.cz/id/p3p2kb/', 'label': 'Vlnas 2017 thesis (text + appendix zip of the photographs)'}
ACC_PICC = ('photographs of the microfilm frames in the appendix zip of Vlnas 2017 (theses.cz/id/p3p2kb, file '
            'P_lohy_A_a_B.zip, 14.5 MB, behind a JavaScript proof-of-work page that Chrome passes); the originals and the '
            'microfilms are in SOA Zámrsk (RA Piccolomini is not item-indexed on ARON and has no digital objects)')
PICC = 'SOA Zámrsk, Rodinný archiv Piccolominiů (Náchod)'
PRIOR_PICC = ('open as far as checked (6 Nov 2026): known.py on the inventory numbers, Piccolomini, Claudia de\' Medici, '
              'Frankenthal, Amalfi, Zámrsk: no hit beyond catalogue #577 (Claudia de\' Medici to Baden 1633, another '
              'archive); Vlnas 2017 deciphered four other frames of the same microfilm (inv. 25039, 24873, 24790, 25106) '
              'and printed their keys, but left these frames undeciphered (his appendix B); Lasry, DECODE and Tomokiyo '
              'not searched beyond the known.py dumps')


ROWS = [
    dict(
        year=1646, date='1646 (sibling letters dated 9 Feb - Dec 1646, Innsbruck)',
        title="Archduchess Claudia de' Medici to Ottavio Piccolomini, Innsbruck 1646: two letters with cipher passages and no interlinear decipherment",
        correspondents="Claudia de' Medici, Archduchess, regent of Tyrol (signs 'Claudia') -> Ottavio Piccolomini, Duke of Amalfi",
        place='Innsbruck', language='Italian', region='Central Europe', period='1611-1650',
        shelfmark=f'{PICC}, inv. č. 24793 and 24800 (microfilm frames labelled "31/2")',
        folio_note='24793: one page, about 20 lines of cipher (letters, digits and signs such as + and a triangle) inside an Italian '
                   'letter; 24800: about 8 cipher lines, dated "Insprugg a 25 di ... 1646". No gloss over or beside either.',
        cls='B',
        status='Seen on the thesis photographs (6 Nov 2026): bare. The same writer\'s other letters on the microfilm (inv. 24784, '
               '24786, 24787, 24788, 24789, 24794, 24796, 24799, 24806, dated Feb-Dec 1646) carry an interlinear decipherment, '
               'and Vlnas 2017 (ch. 4.3) rebuilt the system from inv. 24790: a simple substitution of letters by signs, with a few '
               'code groups (his table 5). So the key is in the volume and in print; no reading of 24793 or 24800 is known.',
        why='The regent of Tyrol writing in cipher to the imperial field marshal in the last campaign years before Westphalia '
            '(Münster negotiations, Spanish and Dutch talks are in the glossed siblings).',
        importance=3, solvability=5, difficulty=1,
        verify='Rebuild the substitution from the glossed siblings (or Vlnas\'s table 5), apply it to 24793 and 24800, and order '
               'clean scans of the two inventory numbers from SOA Zámrsk.',
        links=[VLNAS], access_note=ACC_PICC, seen='image', score_note=SCORE_SEEN, prior_art=PRIOR_PICC,
        needs_archive_scan='no',
    ),
    dict(
        year=1646, date='1646 (sibling dated "febraro 1646")',
        title='Unidentified correspondent with an enciphered signature to Ottavio Piccolomini, 1646: number-cipher letter without decipherment',
        correspondents='unidentified writer ("Devotissimo Servidore", signature in cipher "3127301016152...") -> Ottavio Piccolomini',
        place='not stated (news of Spain, Flanders, the Emperor)', language='Italian', region='Central Europe', period='1611-1650',
        shelfmark=f'{PICC}, inv. č. 24854',
        folio_note='One page: about 6 lines of digit groups mixed with clear Italian words, and the closing "Devotissimo Servidore" '
                   'followed by the signature in cipher digits. No gloss.',
        cls='B',
        status='Seen (6 Nov 2026): bare. The same writer\'s letters inv. 24852 and 24853 (same signature "3127301016152...") have '
               'the digit groups glossed between the lines, so the key can be rebuilt from them. The signature itself is in cipher '
               'on all three, and is not glossed on the frames seen.',
        why='An agent who enciphered even his own name, reporting to Piccolomini in 1646; reading the signature identifies him.',
        importance=3, solvability=4, difficulty=2,
        verify='Transcribe 24852-24854 from the thesis photographs, rebuild the digit table from the glosses of 24852-53, read 24854 '
               'and the signature.',
        links=[VLNAS], access_note=ACC_PICC, seen='image', score_note=SCORE_SEEN, prior_art=PRIOR_PICC,
        needs_archive_scan='no',
    ),
    dict(
        year=1646, date='12 August 1646 (siblings 1646)',
        title='Spanish commander at Frankenthal to Ottavio Piccolomini, "Del Campo a Frankenthal, 12 de agosto 1646": number cipher without decipherment',
        correspondents='writer signing "Joh. Re... von ..." (not read), Spanish garrison of Frankenthal -> Ottavio Piccolomini',
        place='Frankenthal (Palatinate)', language='Spanish', region='Central Europe', period='1611-1650',
        shelfmark=f'{PICC}, inv. č. 25071',
        folio_note='One page, about 15 lines of long digit strings within a Spanish letter, dated "Del Campo a Franckental 12 de '
                   'Agosto 1646". No gloss.',
        cls='B',
        status='Seen (6 Nov 2026): bare. The same writer\'s letters inv. 25063, 25065, 25067 (3 pages), 25069 (2 pages), all 1646 '
               'and in the same digit cipher, are glossed between the lines; one of them lists regiments and strengths with the '
               'numbers glossed (inv. 25026, 8 Feb 1646). Key to be rebuilt from the glosses.',
        why='Spanish garrison reports from Frankenthal in 1646 (Turenne\'s and the Swedes\' moves on the Rhine) to the commander '
            'of the Spanish army in Flanders.',
        importance=3, solvability=4, difficulty=2,
        verify='Transcribe 25063-25071 from the thesis photographs, rebuild the number table from the glossed letters, read 25071.',
        links=[VLNAS], access_note=ACC_PICC, seen='image', score_note=SCORE_SEEN, prior_art=PRIOR_PICC,
        needs_archive_scan='no',
    ),
    dict(
        year=1646, date='c. 1646 (microfilm of 1646 letters; own date not on the frame)',
        title='Italian letter to Ottavio Piccolomini in a two-digit number cipher, without decipherment',
        correspondents='unidentified -> Ottavio Piccolomini',
        place='not read', language='Italian', region='Central Europe', period='1611-1650',
        shelfmark=f'{PICC}, inv. č. 25054',
        folio_note='One page: about 10 lines of two-digit groups (many 3x and 4x numbers: 34 44 13 ...) within Italian clear text. '
                   'One or two isolated words written above the lines; no running decipherment.',
        cls='B',
        status='Seen (6 Nov 2026): practically bare. inv. 25040, a few frames earlier, uses two-digit groups and is glossed between '
               'the lines; whether it is the same cipher is not checked.',
        why='Part of the 1646 Piccolomini intelligence stream; a short two-digit cipher with a possible glossed sibling.',
        importance=2, solvability=3, difficulty=2,
        verify='Compare the number set with inv. 25040; if it matches, apply the glossed values; otherwise solve as a two-digit '
               'substitution with the Italian clear text as context.',
        links=[VLNAS], access_note=ACC_PICC, seen='image', score_note=SCORE_SEEN, prior_art=PRIOR_PICC,
        needs_archive_scan='no',
    ),
    dict(
        year=1646, date='c. 1646 (undated on the frames)',
        title='Two Italian letters to Ottavio Piccolomini in a vowel-to-digit cipher, without decipherment (key printed by Vlnas 2017)',
        correspondents='unidentified -> Ottavio Piccolomini',
        place='not read', language='Italian', region='Central Europe', period='1611-1650',
        shelfmark=f'{PICC}, inv. č. 24874 and 24876',
        folio_note='24874: about 25 lines, almost all in cipher; 24876: about 6 cipher lines then clear text. Consonants written '
                   'plain, vowels as odd digits. No gloss.',
        cls='C',
        status='Seen (6 Nov 2026): bare. Vlnas 2017 (ch. 4.2) deciphered the neighbouring inv. 24873 in the same system: vowels '
               'a e i o u = 1 3 5 7 9, consonants unchanged. That makes these two readable at sight; nobody has published their '
               'text. A key lookup more than a cryptanalytic target.',
        why='Completes the reading of this writer\'s letters; low difficulty, useful as a control.',
        importance=2, solvability=5, difficulty=1,
        verify='Transcribe from the thesis photographs and substitute the five vowels.',
        links=[VLNAS], access_note=ACC_PICC, seen='image', score_note=SCORE_SEEN, prior_art=PRIOR_PICC,
        needs_archive_scan='no',
    ),
    dict(
        year=1574, date='1573-1575',
        title="Vilém z Rožmberka's ciphered correspondence with his supporters in Poland during his candidacy for the Polish throne",
        correspondents='Vilém z Rožmberka (Wilhelm von Rosenberg), Oberstburggraf of Bohemia <-> his partisans in Poland-Lithuania',
        place='Český Krumlov / Prague / Poland', language='Czech, Latin or Polish (not stated)', region='Central Europe',
        period='1551-1610',
        shelfmark='SOA Třeboň, oddělení Třeboň, Historica Třeboň (NAD 124, II T 1), sign. 4834/36',
        folio_note='Signature as cited; extent not stated',
        cls='C',
        status='Cited by L. Staněk, BA thesis, České Budějovice 2026 (theses.cz/id/hotwcc), note 657: "Srov. šifrovanou '
               'korespondenci jihočeského velmože a jeho tamějších stoupenců v SOA Třeboň, Historica Třeboň, sign. 4834/36", '
               'beside M. Slach, "Kandidatura Viléma z Rožmberka na polský trůn v l. 1573-1575", Jihočeský sborník historický 33 '
               '(1964), pp. 130-148. Neither the thesis nor DigiArchiv shows the item; the Historica Třeboň finding aids (nos. 87, '
               '88, 498, 502, 505) are listed on DigiArchiv but their scans are not shown to an anonymous visitor. Whether Slach '
               'printed or deciphered the letters is not checked.',
        why='Sixteenth-century Bohemian magnate cipher for the 1573-75 Polish elections, outside the Habsburg chancery corpus; '
            'the repo notes (research/oldest) know of Rožmberk ciphers only in general.',
        importance=3, solvability=2, difficulty=3,
        verify='Read Slach 1964 for the letters and any decipherment; ask SOA Třeboň for scans of Historica Třeboň 4834/36 and check '
               'its finding aid (Historica Třeboň IV, 1571-1592) entry.',
        links=[{'href': 'https://theses.cz/id/hotwcc/', 'label': 'Staněk 2026 thesis (citation, note 657)'},
               {'href': 'https://digi.ceskearchivy.cz/f/21200001000124', 'label': 'DigiArchiv fond record Historica Třeboň'}],
        access_note='description only (a citation); scans to order from SOA Třeboň', seen='catalogue', score_note=SCORE_DESC,
        prior_art='open as far as checked (6 Nov 2026): known.py on Historica Třeboň, 4834, Rožmberk, Rosenberg: no row; '
                  'Slach 1964 not seen', needs_archive_scan='yes',
    ),
]

OPAVA = 'https://digi.archives.cz/da/permalink/'
KEY_LEADS = [
    dict(year=1640, date='/1640/ (archive: last third of the Thirty Years\' War)',
         title='Key for ciphered letters, by persons and places, late Thirty Years\' War',
         shelfmark='Zemský archiv v Opavě, pobočka Olomouc, Arcibiskupství Olomouc (NAD 1694), finding aid 697 (díl 2, nelistinná '
                   'část), inv. č. 293, sign. I40',
         note='ZA Opava digital reading room: "Klíč pro šifrované dopisy podle uvedených osob a míst asi z poslední třetiny '
              'třicetileté války (-), něm., 16 x 21 cm, nevázáno". German, unbound, no images online. Probably a key of the '
              'Olomouc bishops (Archduke Leopold Wilhelm was bishop 1637-62).',
         links=[{'href': OPAVA + 'D3F97CB683C111E187A40025649FEBC7', 'label': 'ZA Opava record'}]),
    dict(year=1679, date='1679 (items undated)',
         title='Cipher keys filed with Polish and Upper Hungarian news of 1679 (Bishop Karl Liechtenstein-Castelcorno\'s papers)',
         shelfmark='Zemský archiv v Opavě, pobočka Olomouc, Arcibiskupství Olomouc (NAD 1694), finding aid 697, karton 105',
         note='Folder of 1679: "Obžaloby pokladníka polského království (se zprávami francouzského vyslance) (b.d.); Šifrovací klíče '
              '(b.d.); Zprávy ze Slovenska - rebelové na Spiši ..." Keys only are stated; ciphered reports may be in the same carton.',
         links=[{'href': OPAVA + 'D3F9922F83C111E187A40025649FEBC7', 'label': 'ZA Opava record'}]),
    dict(year=1683, date='1683, between 6 and 7 Feb',
         title='Two cipher keys filed with the 1683 news (Lisola refused at the Polish court, Tököly on Poland)',
         shelfmark='Zemský archiv v Opavě, pobočka Olomouc, Arcibiskupství Olomouc (NAD 1694), finding aid 697, karton 114',
         note='Folder of 1683: "... příčiny, pro které císařskému vyslanci baronu de Lisola byl zakázán vstup k polskému dvoru (b.d.) '
              '... 2 šifrovací klíče (mezi 6.2. a 7.2.); E. Tököly o Polsku - připojen novodobý přepis (19.4.) ..."',
         links=[{'href': OPAVA + 'D3F9923683C111E187A40025649FEBC7', 'label': 'ZA Opava record'}]),
    dict(year=1740, date='/1740/',
         title='French decipherment key ("Dešifrovací klíč, franc.") in the owners\' archive of the Deštné estate',
         shelfmark='Zemský archiv v Opavě, Velkostatek Deštné (NAD 173), finding aid 239, 2. Majitelský archiv, B. aktový materiál, '
                   'inv. č. 140',
         note='Description only: "Dešifrovací klíč, franc.", dated /1740/; filed among "nevázané anebo brožované deníky vojenské" '
              '(military diaries), i.e. an owner\'s papers from the War of the Austrian Succession.',
         links=[{'href': OPAVA + '4604EBA32B8A11E8A363F04DA233FD45', 'label': 'ZA Opava record'}]),
]


def main():
    rows = []
    for r in ROWS:
        r = dict(r)
        r.setdefault('source', SRC)
        rows.append(r)
    json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(KEY_LEADS, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(rows), 'rows,', len(KEY_LEADS), 'key leads')


if __name__ == '__main__':
    main()
