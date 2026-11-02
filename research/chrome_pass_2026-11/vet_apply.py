# Applies the vetting pass of 2 Nov 2026 to research/leads.json (run once, from the repo root, before --promote and --close).
# Prior-art findings are in prior_a.json, prior_b.json, prior_c.json; what was seen on the scans is written here.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LEADS = os.path.join(HERE, '..', 'leads.json')
BY = 'Claude session (Chrome pass vetting, 2 Nov 2026)'
SZ = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/'


def prior(name):
    return json.load(open(os.path.join(HERE, f'prior_{name}.json'), encoding='utf-8'))


P = {**prior('a'), **prior('b'), **prior('c')}
ld = json.load(open(LEADS, encoding='utf-8'))
by_id = {x['id']: x for x in ld['leads']}

# Promotion candidates: the scan or the archive's wording was seen, and nothing found reads them.
e = by_id[1578]
e['date'] = 'May 1757 (dateline on the letter; the day is not read at this resolution)'
e['folio_note'] = '5 scans: cover, p. 1 with 3 clear French lines then about 10 lines of cipher, a two-page opening with about 37 more, end cover. About 50 lines, some 2,000 letters.'
e['seen'] = 'image'
e['score_note'] = 'Scored from the images during the Nov 2026 Chrome pass (research/chrome_pass_2026-11/).'
e['vetting'] = {
    'date': '2026-11-02', 'by': BY,
    'seen': {'kind': 'scan', 'where': SZ + '28224155 (scans 2-4 of 5 viewed at the public 800-pixel size in Chrome)',
             'extent': 'About 50 lines of about 40 letters each across three pages, after a clear French opening on p. 1.',
             'cipher': 'Evenly spaced lower-case letters, a few digits and no word divisions. No interlinear or marginal decipherment on the pages viewed; the catalogue says nierozwiązany.'},
    'prior_art': P['1578']['prior_art'],
    'key_check': "Fonds key 1/338/0/1/1196 ('Pour déchiffrer') was viewed: a numbered French code table, while this letter is letter cipher, so it does not apply as a table; it was not applied letter by letter. "
                 'The solved sibling no. 135 (1766) is 3-digit numbers with French between the lines, another system. Letters 128 and 130 of the fonds look like the same letter cipher but carry no solution.',
    'duplicates': P['1578']['duplicates'],
    'verdict': 'open',
}
e = by_id[1587]
e['vetting'] = {
    'date': '2026-11-02', 'by': BY,
    'seen': {'kind': 'not online', 'where': SZ + '17710151 (catalogue record; the unit shows no scans)',
             'extent': 'One letter, length unknown.',
             'cipher': "Archive description: 'Pisany nie rozwiązanym szyfrem, zapewnie różne wiadomości polityczne'. No decipherment noted."},
    'prior_art': P['1587']['prior_art'], 'key_check': P['1587']['key_check'], 'duplicates': P['1587']['duplicates'],
    'verdict': 'open',
}

# Corrections from the vetting.
e = by_id[1598]
e['title'] = 'Ferdinand → John II of Aragon, Córdoba, 4 Nov 1478: the one letter of the 1476-79 BNE group DECODE lists as not deciphered'
e['date'] = '4 Nov 1478'
e['shelfmark'] = 'BNE, MSS/20211/123'
e['decode_ids'] = [1172]
e['folio_note'] = 'One letter. Not viewed.'
e['status'] = ("Narrowed 2 Nov 2026. The group of ten letters that BNE matched as 'cifrada' is all on DECODE: R1170, R1171, R1175, R1176, R1178, R1179, R1180, R1181 and R1184 "
               'share the status of records known to be solved, and only R1172 (this letter) differs (research/catalogue_harvest/decode/list.json). '
               "Tomokiyo 2018, 'Spanish Ciphers before Accession of King Ferdinand: 1470-1479', reconstructs ciphers of this series; its letter list was not read (Academia 403).")
e['solvability'] = 4
e['links'] = [{'label': 'BNE card', 'href': 'https://bnedigital.bne.es/bd/es/card?id=efc87815-5336-44c7-930c-ad2af9bb5609'}]
e['verify'] = 'Read Tomokiyo 2018 for /123; view the letter when BNE is reachable; test the alphabets of the other letters.'

e = by_id[1582]
e['year'] = 1708
e['date'] = '2 June 1708 (541), 28 June 170? (544), as written on the letters'
e['title'] = 'Branicka (catalogued as Janowa, née Szembek) → unknown: French letters with number codes for names'
e['status'] += " Seen 2 Nov 2026: no. 541 is headed 'No 2, le 2 de Juin 1708' and no. 544 'No 7, ce 28 Juin 170?', so the catalogue's 1768 is wrong. French clear text with underlined number codes for names on the page of 541 examined; weak."
e['solvability'] = 2
e['seen'] = 'image'

NOTES = {
    1579: 'Seen 2 Nov 2026: 1398, 1399 and 1400 are letter cipher mixed with 3-digit numbers (845 frequent), 1399 after a French clear opening; 1401 is Polish clear text with underlined digit groups, so another system and to be split. No decipherment on the pages seen. Held back: the numeric part has not been tried against fonds key 1/338/0/1/1196, which needs a larger image than the 800-pixel one. The row year 1750 is assigned, the letters are undated.',
    1580: 'Seen 2 Nov 2026: 128 and 130 are pure letter cipher with no solution on the page (130 after clear French); 131 (11 July 1757) is clear Polish, then numbers and letters; the 143 page seen is clear French. Solved 135 (8 Feb 1766) is 3-digit numbers with French between the lines. Held back: mixed systems in one row, and the numeric letters are key-lookup candidates. The cover of 128 has a faint pencil note that may read rozwiązany.',
    1581: "Seen 2 Nov 2026: the letter is dated Cracow, 21 May 1715. The inner leaf (scan 4) has about 15 lines of graphic signs inside Polish clear text, no decipherment on it. Held back: DECODE keys R7460 and R7461 (ASang_85/3, graphic signs, Sanguszko) have not been compared, and they are the obvious first test.",
    1583: 'Seen 2 Nov 2026: French letter, no. 16, March 1757, with about 8 lines of 3-digit numbers on the opening viewed. Held back: a key-lookup candidate for fonds key 1/338/0/1/1196, untested for image size.',
    1584: 'Held back: the fonds lists solution sheets and a code, and the embassy is already worked in targets/chomentowski1713, whose syllabary was not applied. No scans.',
    1585: 'Held back: solution sheet nr 881 is close by in the series, unverified. No scans.',
    1586: 'Held back: solution sheets and cipher tables (nr 1373-1375) exist at AGAD, so this is probably read at the time or a key lookup. No scans.',
    1588: 'Held back. Nagielski, Miscellanea Historico-Archivistica XI (2000), 287-304, prints five deciphered sibling letters of 31 May to 30 June 1633 (none dated 1 June); a contemporary copy of the 7-letter fascicle is AR dz. II nr 1115, next to this unit. Frames seen 2 Nov 2026: a film card, a clear Polish page with signatures and a blank sheet; no cipher seen yet. Read Nagielski first.',
    1589: 'Held back: the catalogue wording is cut off in the export, so the cipher is unconfirmed. Not viewed.',
    1590: 'Held back: Targosz 1967 (Pinocci family archive transcripts) was not read and may print it. No scans.',
    1591: 'Held back: probably the same letters as catalogue 442 (DECODE R7520-R7522, August 1662, three items, Sanguszko archive); the concordance from unit 9071 to teka 282/2 is not confirmed.',
    1592: 'Held back: may be a copy of a despatch in the Dresden 1791 series of catalogue 433, untested. No scans.',
    1593: 'Held back: the scan viewed was too small to confirm the cipher. The row year 1760 is assigned; the catalogue says undated.',
    1594: 'Held back: two unrelated items in one row; not viewed.',
    1595: 'Held back: a key-lookup candidate for the Deboli keys and perhaps a copy from catalogue 416. No scans, so the key is untried.',
    1596: "Held back: 'nie rozszyfrowana' probably means an unidentified or illegible hand, not cipher. The 1987 inventory was not read.",
    1597: "Held back. Interlinear glosses cover part of the cipher on the page viewed, so partly read, and Tomokiyo 2018 (not readable, Academia 403) covers 1470. BNE's title says 'al Rey de Aragón', which in Oct 1470 would be John II: read the address. Not on DECODE. A sibling source for targets/ferdinand1473.",
    1599: "Held back: BNE blocked access before the leaf could be viewed. 'Carta cifrada' is known only from the title. A search summary of a SNAC record may point to a second exemplar at the Huntington, unverified.",
    1600: 'Held back: not viewed (BNE blocked access). Sibling R1189 (29 May 1548) is deciphered on DECODE and Tomokiyo assigns it to the Imperial Cipher of 1544-54, so a key family probably reads this.',
    1601: 'Held back only because the leaf was not viewed (BNE blocked access). Prior art clean so far: not on DECODE, nothing in Tomokiyo. Lead 1271 (Mirabel → Gondomar) is the possible key sibling.',
    1602: 'Held back only because the leaf was not viewed (BNE blocked access). Prior art clean so far: not on DECODE, nothing in Tomokiyo.',
}
for i, note in NOTES.items():
    by_id[i]['vetting_note'] = note + ' Prior art per lead: research/chrome_pass_2026-11/prior_a.json, prior_b.json, prior_c.json.'
by_id[1582]['vetting_note'] = 'Held back: name codes only on the page seen, and 544 is not yet checked for more. Prior art per lead: research/chrome_pass_2026-11/prior_a.json.'

with open(LEADS, 'w', encoding='utf-8') as f:
    json.dump(ld, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('ok', len(NOTES))
