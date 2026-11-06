"""Fold the per-volume Tarouca rows into series rows and add vetting blocks (5 Nov 2026, main session).

    python consolidate_vet.py      reads candidates_volumes.json (the sweep's 62 per-volume rows), writes candidates.json

The sweep wrote one row per bound volume. Three Tarouca series (the Corte-Real copy-books A.T. 26, the Alegrete
letters A.T. 163 + 164, the embassy volumes A.T. 229) are one correspondence and one key each, so each becomes one
row, as catalogue #394 does for the Torre do Tombo Tarouca series. Every row that is not online gets a "not online"
vetting block (docs/_check_catalogue.py) from the checks made in this session; rows whose prior art is still
unchecked, or whose description leaves the cipher in doubt, keep no block and stay leads.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, 'candidates_volumes.json'), encoding='utf-8'))
DATE, BY = '2026-11-05', 'main session 2026-11-05 (BNP sweep merge)'

COMMON = {
    'tomokiyo': 'cryptiana.web.fc2.com has no page on {t}; web search 5 Nov 2026 (cryptiana, Portuguese cipher, the correspondents) found nothing',
    'lasry': 'No Lasry or HistoCrypt paper on {t}; the HistoCrypt Portuguese papers (Dinnissen & Araujo 2022 on Teles da Silva 1649, the 1646 Pina paper) use Hague WIC material, not BNP volumes',
}


def at(r):
    return r['shelfmark'].split('A.T. ')[1]


def series(idx, **kw):
    mem = [rows[i] for i in idx]
    base = dict(mem[0])
    recs = [m['links'][0]['href'].rsplit('/', 1)[1] for m in mem]
    cif = '; '.join(f"A.T. {at(m)} ({m['date']}): {m['folio_note'].split('catalogue: ')[-1]}" for m in mem)
    places = sorted({p.strip() for m in mem for p in m['place'].split(';') if p.strip() and p.strip() != 'unknown'})
    base.update(kw)
    base['folio_note'] = f"{len(mem)} bound volumes; catalogue cipher notes per volume: {cif}"
    base['status'] = (f"BNP catalogue records {', '.join(recs)}: each volume noted 'partes do texto em cifra' or with "
                      "the cipher folios listed; no decipherment noted (the archive notes decipherments where they exist, "
                      "e.g. A.T. 158//2). Not digitised. Not on DECODE, not in the repo. Folded from the sweep's "
                      f"{len(mem)} per-volume rows (candidates_volumes.json).")
    base['place'] = '; '.join(places)
    base['links'] = [{'label': f"BNP A.T. {at(m)}", 'href': m['links'][0]['href']} for m in mem]
    base['prior_art'] = 'open (checked 5 Nov 2026: DECODE and repo via known.py, cryptiana, HistoCrypt, web search on Tarouca / Alegrete / Corte-Real cipher; Cluny 2006 not seen)'
    return base


S_COPY = series(range(21, 37),
    year=1712, date='1712-1737',
    title='Conde de Tarouca ↔ secretary of state Diogo de Mendonça Corte-Real: official copy-books 1712-37 (Utrecht, The Hague, Vienna), cipher passages in 16 volumes',
    correspondents='João Gomes da Silva, 4th conde de Tarouca ↔ Diogo de Mendonça Corte-Real (secretary of state)',
    shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 26//3-6, 8-16, 18, 19, 22 (16 vols)',
    why="Portugal's plenipotentiary at the Utrecht congress, then envoy at The Hague and Vienna, and Lisbon's secretary of state: the ciphered parts carry the confidential side of Utrecht, the Quadruple Alliance and the 1735-37 crisis with Spain.",
    importance=4)
S_ALEG = series(list(range(37, 46)) + list(range(49, 62)),
    year=1711, date='1711-1731',
    title='Marquês de Alegrete ↔ his brother the conde de Tarouca: family-political letters 1711-31, parts in cipher (22 volumes, part of a key bound in A.T. 164//11)',
    correspondents='Fernando Teles da Silva, 2nd marquês de Alegrete ↔ João Gomes da Silva, 4th conde de Tarouca',
    shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 163//2-17 (9 vols, Alegrete to Tarouca) and A.T. 164//2-19 (13 vols, Tarouca to Alegrete)',
    why="Both sides of a twenty-year exchange between a court grandee in Lisbon and the envoy abroad; the cipher hides court politics and diplomatic news the brothers kept from the posts.",
    importance=3)
S_EMB = series(range(46, 49),
    year=1686, date='1681-1732',
    title='Negociações políticas nas cortes de Heidelberg, Viena e Madrid: embassy despatch volumes 1681-1732 (Alegrete, Tarouca, Cunha Brochado, Guedes Pereira), parts in cipher',
    correspondents='Manuel Teles da Silva, 1st marquês de Alegrete; conde de Tarouca; José da Cunha Brochado; António Guedes Pereira ↔ the Crown and secretaries of state',
    shelfmark='Biblioteca Nacional de Portugal, Arquivo dos Condes de Tarouca, A.T. 229//1-3 (3 vols)',
    why="The 1st Alegrete's embassy for Pedro II's marriage to Maria Sofia of Neuburg (Heidelberg 1686-87) and later Vienna and Madrid missions; the cipher carries the marriage and alliance negotiations.",
    importance=3)

singles = {i: rows[i] for i in range(0, 21)}
out = [singles[i] for i in range(0, 21)] + [S_COPY, S_ALEG, S_EMB]

# rows that stay leads without a vetting block, and why
HOLD = {
    4: 'printed Correspondência do Visconde de Santarém (1918-19) not checked for this 1829 letter',
    10: 'single letters standing for names (Z, O) in a clear letter: a name code, not a ciphertext',
    13: 'the catalogue summarises the content, so the cataloguer may have read the invented alphabet',
    14: 'which of 761 folios carries cipher is not stated; nothing to vet against',
    9: 'the catalogue describes only the key ("[Cifra do diário]", n. 13); whether any diary entry is enciphered is not stated',
}

TOPIC = {1: 'the royal letters to the conde de Soure', 2: 'the 1894 railway-company telegrams', 3: 'the 1669 letters to Pedro Antonio de Aragón',
         5: "Cipriano Ribeiro Freire's Madrid despatches", 6: 'the Goa Vedor da Fazenda letter-book', 7: "António Teles da Silva's letters from Bahia",
         8: "Padre Nuno da Cunha's Rome papers", 9: "Ribeiro Saraiva's diary", 11: "Saldanha's 1871 telegrams", 12: "the conde da Lousã's 1859 telegram",
         15: "Corte-Real's 1734 despatches to Tarouca", 16: "Corte-Real's 1730 letters to Tarouca", 17: "Abrantes' letters to Tarouca",
         18: "Tarouca's letters to Abrantes", 19: "Tarouca's letters to Luís da Cunha", 20: "the 1735-37 despatches to Tarouca"}

EDITION = {
    1: "No edition of these royal letters; Laranjo Coelho's Cartas dos governadores da província do Alentejo prints the governors' letters to the king, not these; the 2022 Évora thesis the agent cited could not be found online",
    2: 'No edition known; the telegrams are unpublished company papers',
    3: 'No edition of this BNP volume known; the Aragón letters in the repo (targets/aragon1676, BNE Mss/2043) are a different volume',
    5: 'No edition of the Ribeiro Freire letter-book known (web search 5 Nov 2026)',
    6: 'No edition of the 1745-49 Goa letter-book known (web search 5 Nov 2026)',
    7: 'No edition of the A.T. 128 letters known; Dinnissen & Araujo 2022 and Ackel 2025 (LaborHistórico 11) edit only the 1649 Hague cipher letters (NA OWIC 1.05.01.01/65 and 77)',
    8: 'No edition known; Gatti 2019 (Tempos Históricos 23) on Nuno da Cunha cites Ajuda and Vatican codices, not A.T. 140, and quotes no cipher',
    9: 'No edition of the diary known; Brito 1914 on the Ribeiro Saraiva manuscripts lists the collection',
    11: 'No edition of the Fontes Pereira de Melo telegrams known', 12: 'No edition of the Fontes Pereira de Melo telegrams known',
}
LIT = {
    7: 'Ackel 2025 and Dinnissen & Araujo 2022 read or study the 1649 ciphers only; no study of the BNP Bahia letters found',
    8: 'Gatti 2019 and her USP thesis (2021) do not use A.T. 140 or its cipher',
}
KEY = {
    7: 'No key in the volume. Held elsewhere: the Teles da Silva keys of 1649 in NA The Hague, WIC (Dinnissen & Araujo 2022), not yet tried on these 1643-48 letters',
    9: 'No other key tried; the diary key is bound in the same unit (key_in_volume)',
}
KIV = {9: 'MSS. 169 n. 13 "[Cifra do diário]" is the diary key in the same unit; not seen or tested (not online)'}
KEYHELD_TAROUCA = 'BNP COD. 4418 f. 16-23 "Cifra por que se hade escrever" (Tarouca embassy key 1707-09) and the partial key bound in A.T. 164//11; neither seen or tested (not online)'


def vet(r, i, topic, edition, literature, key_check, kiv=None, kheld=None):
    quote = r['folio_note'].split('catalogue: ')[-1] if 'catalogue: ' in r['folio_note'] else r['status'].split("'")[1] if "'" in r['status'] else r['folio_note']
    quote = quote.strip(" '")
    v = {'date': DATE, 'by': BY,
         'seen': {'kind': 'not online',
                  'where': ', '.join(l['href'] for l in r['links'][:6]) + (' ...' if len(r['links']) > 6 else ''),
                  'extent': r['folio_note'][:600],
                  'cipher': f"BNP catalogue description: '{quote[:400]}'; no decipherment noted in the record"},
         'prior_art': {'decode': f"Not on DECODE: known.py (DECODE list, 10,106 records) on the correspondents and shelfmark gives nothing; DECODE holds no BNP {('Arquivo Tarouca ' if 'Tarouca' in r['shelfmark'] else '')}record",
                       'tomokiyo': COMMON['tomokiyo'].format(t=topic),
                       'lasry': COMMON['lasry'].format(t=topic),
                       'edition': edition,
                       'literature': literature},
         'key_check': key_check,
         'duplicates': f"known.py on the correspondents, shelfmark and date: no catalogue, lead or target row; catalogue #394 (Tarouca to Assumar, ANTT N-V-28) and leads 1236-1242 (BNP via Manuscriptorium) are different items",
         'verdict': 'open'}
    if kiv: v['key_in_volume'] = kiv
    if kheld: v['key_held'] = kheld
    r['vetting'] = v


TAROUCA_ED = 'No edition of the Tarouca correspondence volumes found; Carlos da Silva Tarouca published family papers in Brotéria, not these ciphers; Cluny, O Conde de Tarouca e a diplomacia na época moderna (2006), uses the archive and was not seen'
TAROUCA_LIT = 'Web search 5 Nov 2026 on Tarouca / Alegrete / Corte-Real / Abrantes with cifra, cipher, decifrada found no study of the cipher; Cluny 2006 not seen'

for i, r in enumerate(out):
    if i == 0 or i in HOLD:
        if i in HOLD:
            r['vetting_hold'] = HOLD[i]
        continue
    r['needs_archive_scan'] = 'yes'      # row 5 was "partly": digitised by the BNP but not public, so nothing is viewable
    if i >= 21 or 'Tarouca' in r['shelfmark'] and i != 7 and i != 8:
        t = r['title'].split(':')[0] if i >= 21 else TOPIC[i]
        vet(r, i, t, TAROUCA_ED, TAROUCA_LIT,
            'No decipherment in the records; the Tarouca keys held at the BNP (COD. 4418, A.T. 164//11) and the cipher-plus-decipherment letters of A.T. 158//2 are the first to try; nothing tried, nothing online',
            kheld=KEYHELD_TAROUCA)
    else:
        vet(r, i, TOPIC[i], EDITION[i], LIT.get(i, f'Web search 5 Nov 2026 on {TOPIC[i]} with cifra / cipher found no study of the cipher'),
            KEY.get(i, 'No key known in the volume, at the BNP or in print; nothing tried, nothing online'), kiv=KIV.get(i),
            kheld=KEY[7].split('Held elsewhere: ')[1] if i == 7 else None)

json.dump(out, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'rows;', sum('vetting' in r for r in out), 'with vetting;', len(HOLD), 'held as leads')
