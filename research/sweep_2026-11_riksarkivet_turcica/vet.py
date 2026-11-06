"""Vetting blocks for leads 2256-2260 (5 Nov 2026). Writes them into research/leads.json; promotion and closing go
through docs/_check_catalogue.py. Run from the repository root: python research/sweep_2026-11_riksarkivet_turcica/vet.py"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEADS = ROOT / 'research' / 'leads.json'
BY = 'Claude Opus 5.5, Riksarkivet Turcica vetting pass'
DATE = '2026-11-05'

DECODE = ('Not on DECODE: the harvested DECODE dump (research/catalogue_harvest/decode list.json and views*.jsonl, Oct 2026) '
          'has no record naming {names}, Turcica, Polonica or Tunisica; its Riksarkivet records are the Chifferklaver key boxes '
          '(låda II), Oxenstierna, Bremen and the Erik Brahe diary. Live DECODE not queried.')
TOMOKIYO = ("No entry: cryptiana's index (crypto.htm), unsolved.htm (whole page) and ai.htm fetched 5 Nov 2026 mention no Swedish "
            'diplomatic cipher of this period and none of {names}; local unsolved.htm grepped too.')
LASRY = ("No Lasry work: his publication list and searches on Lasry/Megyesi with Swedish, Charles XII, Christina, Charles X Gustav "
         'found nothing on these letters; local GL.htm (targets/gramont1529) has no match. DECODE itself not queried via the API.')
LIT = ('HistoCrypt, Cryptologia and scholar searches on Swedish chancery ciphers (chiffer, chiffernyckel, Kanslikollegium, '
       'fältkansli) found no study of these letters; nearest Swedish cipher work is Waldispühl and Kopal on Heusner 1637 and '
       'the HistoCrypt key-corpus paper. ')

LEADS_VET = {
    2258: dict(
        seen=dict(
            kind='scan',
            where='Riksarkivet image series 40008933 (Diplomatica Turcica SE/RA/2119/2119.1/I/2/2, NAD '
                  'https://sok.riksarkivet.se/arkiv/eWy9xynckH1kcXy2OkH6B5), contact sheets of 42 + 24 images and images 18, 22, '
                  '23, 24, 34, 68, 74, 77, 87, 88, 104, 114, 120, 126 at 760-900 px, 114 and 18 zoomed at 2400 px; Referer route, '
                  '5 Nov 2026',
            extent='132 images. Number cipher in letters of Rålamb and Vellingk to Charles X Gustav, Constantinople 1657, on at '
                   'least images 18, 22-23, 74, 77, 87-88, 104 and 114: runs of small groups (1-110, a few 800s and four-digit '
                   'groups) inside clear Swedish, from a few groups to half-page blocks. Not paged leaf by leaf.',
            cipher='Small-number code, dot-separated, in Swedish despatches. Image 114: about ten runs of 5-15 groups each '
                   '(e.g. 71.6.80.8.16.70.84.34.37.17.32.36; 12.8.64.34.6; 4.40.10.41.34.37.74.34.102) with no interlinear writing, '
                   'no gloss in the margin and no decipherment on the facing page, zoomed at 2400 px; image 104 shows the same bare '
                   'runs at 760 px. Other letters carry a decipherment written over the numbers (22, 23, 74, 77, 87, 88; image 18 in '
                   'faint lighter ink): those passages are cribs, not open text.'),
        prior_art=dict(
            decode=DECODE.format(names='Rålamb, Vellingk'),
            tomokiyo=TOMOKIYO.format(names='Rålamb, Vellingk, Charles X Gustav'),
            lasry=LASRY,
            edition="Rålamb's diary is edited (C. Callmer, Diarium under resa till Konstantinopel 1657-1658, Historiska handlingar "
                    '37:3, 1963); not seen, appendices of despatches not confirmed. Babinger 1937 printed Hiltebrandt\'s narrative and '
                    "Vellingk's memorandum to the Porte (secondary citation), not these despatches. No edition of the cipher "
                    'despatches found.',
            literature=LIT + 'Forss 2021 (Legatio, "Knowledge and agency: the case of Claes Rålamb") cites Turcica I vol. 3 and never '
                       'mentions cipher; Turkish articles on the embassy and The Sultan\'s Procession (2006) say nothing on ciphers.'),
        key_check='No printed or published key found for Swedish chancery codes of 1657. The interlinear glosses in the same '
                  'volume give plaintext-cipher pairs from which the code can be rebuilt (not done).',
        key_in_volume='Decipherments written over the number runs in several letters of the same volume (images 18, 22-23, 74, '
                      '77, 87-88): cribs for the same code; not a key table, not tested.',
        key_held='Possible: DECODE R4201 (Riksarkivet Chifferklaver låda II 82, dated 1657, 4 pp., key record) and R4195 (låda '
                 'II 76, 1658); the dump names no correspondent for either. Not tested.',
        duplicates='known.py on Rålamb, Ralamb, Vellingk, Wellingk, the shelfmark 2119.1/I/2/2 and series 40008933: only this '
                   'lead and its sweep files; Vellingk in catalogue 452 is Mauritz Vellingk at Hamburg 1714, another man and '
                   'series. DECODE dump: no record.',
        verdict='open'),
}

CLOSE = {
    2257: ('read', 'Every cipher passage seen in the four volumes carries a contemporary decipherment written over the numbers: '
                   'Perman I/7/16 images 20, 24, 32, 49, 70, 77 (sheet of 36 images, four at 760 px), Funck I/6/10 images 58, 66, '
                   'I/6/9 image 335, von Müllern I/6/14 images 69-70. A crib corpus read from an existing decipherment, not an '
                   'open text. Its use is as key material for catalogue 1769 (Funck I/6/13, the same code unglossed); a bare '
                   'passage elsewhere in the 1,022 images cannot be excluded.'),
    2259: ('partly_read', 'The only cipher in Polonica I/5/17 (all 72 images sheeted, dense pages at 800 px) is one letter of '
                          'about three pages, images 9-11 (1648), and nearly every number row carries a Swedish decipherment '
                          'written over it (zoomed at 2400 px); a few rows on image 9 have none and could be filled from a key '
                          'rebuilt from the glossed rows. Too small and too fully glossed for an open entry. Possible key: DECODE '
                          'R4160 / R4172 (Chifferklaver låda II 47 and 55, dated 1648), not tested.'),
}

CLOSE[2256] = ('partly_read', 'Glossed throughout (sheets of about 72 images over 1-437 plus every 2-3 images over 245-337; '
                              'images 86, 125, 253, 254, 261, 266, 271, 295, 306, 308, 311, 314, 322, 327, 332, 335 at 900 px). '
                              'All cipher sits in images about 253-335, some 12-15 letters of May-Oct 1712, in a 2-3 digit '
                              'number code and, on 261 and 322, a letter cipher "par le chiffre de Mr de Grothus"; the French is '
                              'written over every cipher line except short tails (last lines of 253 and 254, one line of 266, '
                              'parts of 306 and 314, about 10-15 lines), which a key rebuilt from the glosses would fill. '
                              'No key sheet in the volume. Agent-assisted check, 5 Nov 2026.')

# 2260 is held, not promoted or closed: bare cipher is plentiful, but two checks are open (see "pending").
HOLD = {
    2260: dict(
        seen=dict(
            kind='scan',
            where='Riksarkivet R0003585 (Diplomatica Turcica, bihang Tunisica SE/RA/2119/2119.7/2), sheets of about 72 images over '
                  '1-732, every image over 118-160, every 4th over 160-450; images 120, 122, 123, 138, 144, 152, 153, 158, 176, '
                  '365, 366, 367 at 700-900 px or zoomed; 5 Nov 2026 (agent-assisted)',
            extent='About 16-18 pages of undivided digit cipher in 7-8 letters, roughly 15,000-20,000 digits: March-June 1765 '
                   '(images 120-176) and July-Sept 1770 (365-366). Lines of 70-75 digits, 16-18 lines a page. Images 180-450 '
                   'only thinly sampled.',
            cipher='Unbroken digit strings with no separators inside clear French letters to the Kanslipresident. Bare on '
                   '120 right, 122, 123, 138, 144, 152, 153, 158, 176, 365, 366. Image 120 left carries an interlinear French '
                   'decipherment in another hand, with the stream divided by commas and slashes; it stops before the last row. '
                   'Image 365 has the ink note "Dubbletten dechifferad" (the duplicate deciphered) and a pencil note of March 1937.'),
        prior_art=dict(
            decode=DECODE.format(names='Molinari, Tunis'),
            tomokiyo=TOMOKIYO.format(names='Molinari, Tunis'),
            lasry=LASRY,
            edition='Mehdi Jerad, La correspondance de Jean Antoine Molinari, consul suédois à Tunis 1764-1778, introduite et '
                    'annotée (FLSH Sousse / FSHS Tunis, 2015), at least 587 pp., cited in Jerad, Rives méditerranéennes 64 (2023) '
                    '137-154 (https://journals.openedition.org/rives/9665), which quotes letters of 1765-70 from it and never '
                    'mentions cipher. No copy or catalogue record found; whether it prints the cipher letters, in figures or '
                    'deciphered, is unknown.',
            literature=LIT + "Jerad's 2019 Hespéris-Tamuda article (Rönling, 1738-40) has no cipher; Bdira 1990 not seen."),
        key_check='No key found in print or in the volume (126-127 are Italian payment lists).',
        duplicates='known.py on Molinari, Tunisica, the shelfmark and R0003585: only this lead and its sweep files.',
        pending='Not promoted, 5 Nov 2026: (1) "Dubbletten dechifferad" on image 365 means the chancery deciphered the duplicate, '
                'so a deciphered copy may be filed elsewhere in Riksarkivet (Kanslikollegium or Handelskollegium series); (2) '
                "Jerad's 2015 edition may print the plaintext. Promote only after both are checked; close as read if either "
                'gives the text.'),
}

RETITLE = {
    2258: dict(
        title="Clas Rålamb's despatches from Constantinople, 1657: number cipher, some letters glossed, others bare",
        status='Catalogue: the volume title only. Vetting 5 Nov 2026: bare number runs with no decipherment on images 104 and '
               '114; other letters (18, 22-23, 74, 77, 87-88) carry a decipherment written over the numbers, so the code can be '
               'rebuilt from those pairs and applied to the bare passages.'),
}

d = json.loads(LEADS.read_text(encoding='utf-8'))
leads = d['leads'] if isinstance(d, dict) else d
for e in leads:
    if e['id'] in RETITLE:
        e.update(RETITLE[e['id']])
    if e['id'] in LEADS_VET:
        v = dict(date=DATE, by=BY)
        v.update(LEADS_VET[e['id']])
        e['vetting'] = v
    if e['id'] in HOLD:
        v = dict(date=DATE, by=BY)
        v.update(HOLD[e['id']])
        e['vetting'] = v
    if e['id'] in CLOSE:
        verdict, why = CLOSE[e['id']]
        e['vetting'] = dict(date=DATE, by=BY, verdict=verdict, closed=why)
LEADS.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('written', sorted(LEADS_VET) + sorted(CLOSE))
