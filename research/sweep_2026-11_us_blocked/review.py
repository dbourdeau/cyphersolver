"""Write the review pass (README, "Review pass") into research/leads.json and catalogue.json. Keyed on shelfmark, so it survives
a renumbering when main moves. Closed leads go through docs/_check_catalogue.py --close; this prints those commands' arguments."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CLOSE = {
    'State Library of Victoria, letter': ('read', 'Printed: Gurwood, Dispatches of Wellington ix, Villa Toro, 17 Oct 1812, to Commodore Sir Home Popham (grepped from archive.org dispatchesoffie09welluoft, 3 Nov 2026).'),
    'Morgan Library, MA 1346-177': ('key_lookup', 'Key on cryptiana mary.htm: SP53/23 no. 2/8 (1560), "Cipher between the Queen Dowager and the Cardinal of Lorraine and Duke of Guise". Camden Fifth Series calendars a letter of this date. The ciphertext was not seen.'),
    'American Philosophical Society, Franklin Papers part 14': ('key_lookup', 'Morris and Livingston to Franklin use the printed-template codes of Weber: cryptiana frankli2.htm and livingst.htm identify WE008, and cryptiana index.htm decodes Livingston to Franklin of 9 Aug, 5 and 18 Sept, 21 Nov and 3 Dec 1782.'),
    'Morgan Library (ArchiveGrid 270513594)': ('key_lookup', 'Bossuet correspondence with the abbé Bossuet 1697-98 is on Lasry\'s GL.htm (NAF 28227(9)): 41 numerical codes, key in the same volume.'),
    'New-York Historical Society, Sir James Henry Craig coded let': ('key_lookup', 'Craig used the British southern Common cipher (Saberton, Journal of the American Revolution 2019: key by alignment, method given).'),
    'ArchiveGrid 80964934': ('not_cipher', 'Record read 3 Nov 2026: the word is only "lifetime secretary and Keeper of the cipher, Apollonio Bassetti". 309 dispatches at the Getty, no cipher reported.'),
}
UPDATE = {  # shelfmark prefix: fields or a note appended to status
    'New-York Historical Society, Loosey papers': dict(title='Imperial Mexican consulate at New York (Charles de Loosey): 54 telegrams to and from Maximilian and Carlota, "many of them in code", 1866-67', date='1866-1867', year=1866, correspondents='Maximilian, Carlota ↔ Charles Frederick de Loosey', language='Spanish; French; German', importance=5, cls='B',
        status='Record read 3 Nov 2026: "54 telegrams to and from Maximilian and Empress Carlota, many of them in code, 1866-1867" (36 vols., official records of the Imperial Mexican Consulate). A Diccionario telegráfico (Mexico, 1866) is listed in cryptiana telegraph2.htm as a candidate. Not on cryptiana by name.',
        why='The Second Empire\'s last year in its own telegrams.', verify='Reach the N-YHS finding aid; test the 1866 Diccionario telegráfico.'),
    'Brigham Young University': dict(title='Carlo d\'Aragona Tagliavia and others → Paolo Sfondrati and the future Gregory XIV: 27 letters of 1583, "many ... partially or entirely in code"', date='1583', year=1583),
    'Beinecke, Spinelli archive': dict(note='Domnina, "Ciphers in Early Tudor Diplomacy" (Geheime Post 2015), cited on cryptiana henryvii.htm, studies Thomas Spinelly\'s cipher with Leonardo Spinelli: compare first.'),
    'Beinecke, Osborn Manuscript Files, OSB MSS FILE 11791': dict(note='Perwich\'s 1670 transposition paragraph to Arlington was only solved in 2025 (Biermann and Lasry; Brown; TNA report, per cryptiana unsolved.htm). This letter a year earlier may share the system.', importance=4),
    'Morgan Library, MA 1267': dict(note='Webbe to Murray 1804 in the same set: "One letter, MA 1287.5, is partially in cipher" (ArchiveGrid 270588788, 935727252). Morgan\'s 16-item set also has one letter "almost entirely in ciphers".'),
    'Morgan Library (ArchiveGrid 270466362)': dict(note='Record quotes the letter: "I have desired Doyle to give him a Cypher". Rawdon used the southern Common cipher (Saberton 2019), so this is probably a key lookup once seen.'),
    'University of Chicago, Special Collections, Diplomatic docum': dict(note='Record read 3 Nov 2026: 65 documents, originals and copies; nothing more on the cypher.'),
    'Gilder Lehrman Collection, GLC01523': dict(note='Reviewed 3 Nov 2026: Burr is not on cryptiana for 1804 (only the 1806 Entick dictionary code, bookcode.htm). Gilder Lehrman\'s AMDigital record still says undecoded. Kline still not compared.'),
    'American Philosophical Society, Benjamin Franklin Papers, Ms': dict(note='Founders Online prints Wharton to Bancroft of 10 Jan 1777 (Franklin 01-23-02-0089); the May 1778 letters were not found there by web search.'),
    'Morgan Library (ArchiveGrid 270477800)': dict(note='Cryptiana henryii.htm has no item for this letter; Ribier could not be reached.'),
    'Morgan Library (ArchiveGrid 270477885)': dict(note='Cryptiana henryii.htm lists Babou to the King, 11 Jun 1558, with cipher and decipherment in the same series: same channel, key likely there. Ribier could not be reached.'),
    'Morgan Library (ArchiveGrid 270598970)': dict(note='No print found by web search; Arckenholtz not compared.'),
    'UT Austin, Benson Latin American Collection': dict(note='Reviewed 3 Nov 2026: ArchiveGrid re-search returned no record and TARO ignores queries, so the sentence is still unread. Weakest rows here.'),
}


def main():
    p = os.path.join(ROOT, 'research', 'leads.json')
    d = json.load(open(p, encoding='utf-8'))
    close = []
    seen = set()
    for e in d['leads']:
        sm = e.get('shelfmark', '')
        for k, u in UPDATE.items():
            if sm.startswith(k):
                seen.add(k)
                u = dict(u)
                note = u.pop('note', None)
                e.update(u)
                if note and note not in e['status']:
                    e['status'] = e['status'].rstrip() + ' ' + note
        for k, c in CLOSE.items():
            if sm.startswith(k):
                seen.add(k)
                close.append((e['id'], c[0], c[1]))
    missing = (set(UPDATE) | set(CLOSE)) - seen
    if missing:
        print('NOT FOUND', missing)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(p, 'a', encoding='utf-8').write('\n')
    # strengthen the vetting text on whatever already moved to the catalogue, then the older-row corrections
    cp = os.path.join(ROOT, 'catalogue.json')
    c = json.load(open(cp, encoding='utf-8'))
    L = c['entries'] if isinstance(c, dict) and 'entries' in c else c
    fix = json.load(open(os.path.join(HERE, 'catalogue_corrections.json'), encoding='utf-8'))
    for e in L:
        if str(e['id']) in fix:
            e['status'] = fix[str(e['id'])]
    json.dump(c, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(cp, 'a', encoding='utf-8').write('\n')
    for i, v, w in close:
        print(subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_catalogue.py'), '--close', str(i), v, w], capture_output=True, text=True, encoding='utf-8').stdout.strip()[:120])


if __name__ == '__main__':
    main()
