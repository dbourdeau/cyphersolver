"""Write the vetting blocks of the leads this sweep could check, and the Yale PDF corrections to older catalogue rows."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BY = 'claude US blocked-sources sweep (research/sweep_2026-11_us_blocked/)'
TOMO = 'All 320 text pages of cryptiana.web.fc2.com/code mirrored and grepped 3 Nov 2026 for {}: no hit on this item.'
LAS = 'GL.htm (repo copy and live mirror) grepped 3 Nov 2026 for {}: no hit. No Lasry or HistoCrypt item found by web search.'
V = {
 'Indiana University, Lilly Library, Cryptographic manuscript 1780-1867': dict(
    where='ArchiveGrid record https://researchworks.oclc.org/archivegrid/collection/data/656417069 (read 3 Nov 2026); no scan linked',
    extent='15 handwritten pages',
    cipher='Catalogue: "Unique and unpublished late 18th century (ca. 1780 per dealer\'s description) cryptographic manuscript, with 15 handwritten pages of undeciphered code in the form of fractions, numerals and slash-marks." No decipherment mentioned.',
    decode='Not on DECODE: known.py "Cryptographic manuscript" and "Indiana University" found no DECODE record.',
    edition='No edition known; web search of 3 Nov 2026 for the title and its description found no publication.',
    literature='Web search (3 Nov 2026) for the manuscript with Lilly Library, fractions and slash-marks found no study; Schmeh\'s lists and Copiale results came up but none describes this item.',
    key='No key known or held; the system is not identified from the description, so no held key could be tried.',
    dup='known.py "Cryptographic manuscript", "Indiana University", "Lilly": no hit in catalogue, leads, targets or DECODE.',
    grep='Lilly, Indiana'),
 'Mount Vernon, Washington Library, Historic manuscript collection, 1776/1777 item': dict(
    where='ARVAS record https://search.arvasarchive.org/catalog/vimtvl_repositories_3_resources_34_c01_c05_c02 (read 3 Nov 2026); no digital object listed',
    extent='First 7 of 32 pages of one journal; 4 items in all',
    cipher='Finding aid: "Revolutionary War Journals of James Humphrey, written partially in code, with separate marching orders and review of procedures - 4 items. A 32 page journal, the first seven pages being in code". No decipherment mentioned.',
    decode='Not on DECODE: known.py "Humphrey" hits only Humphrey Covert 1601, an unrelated catalogue entry.',
    edition='No edition found: a web search of 3 Nov 2026 for the journal found other Humphreys (William Humphrey\'s 1775 Quebec journal, a Capt. James Humphrey memorial) and no print of this one.',
    literature='The same search found no study; the nearest result was Charles Herbert\'s prison journal, a different author, with its cipher provided.',
    key='No key known or held for a private journal code; none tried, as no ciphertext is online.',
    dup='known.py "Humphrey", "Mount Vernon": no entry for this journal.',
    grep='Humphrey (only David Humphreys, Portugal, in jeffers2.htm and state.htm)'),
 'West Virginia & Regional History Center, Wylie-Tomlinson Letter Collection, A&M 4068, Items 366, 369, Box 2 f. 51': dict(
    where='WVU ArchivesSpace item pages https://archives.lib.wvu.edu/repositories/2/archival_objects/138999 and /139002, collection /resources/3387 (read 3 Nov 2026); no digital object listed',
    extent='2 postcards wholly in code (11 and 22 Aug 1880); other letters in the group "occasionally" in code',
    cipher='Finding aid: "postcard written completely in code"; series note: "His letters to Sarah Isabella are tender and almost obsessive, and are occasionally written in a secret code." No decipherment mentioned.',
    decode='Not on DECODE: known.py "Tomlinson" and "Wylie" found no DECODE record.',
    edition='No edition known: web search of 3 Nov 2026 found only the WVU catalogue entries.',
    literature='The same web search found no article on the collection\'s code.',
    key='No key known or held; a private courtship code, none to try without the images.',
    dup='known.py "Tomlinson", "Wylie": no hit.',
    grep='Tomlinson, Wylie (only an unrelated Tomlinson in thurloe.htm)'),
 'Connecticut Historical Society, Letter to Benjamin Farar': dict(
    where='ArchiveGrid record https://researchworks.oclc.org/archivegrid/collection/data/778803090 (read 3 Nov 2026); no scan linked',
    extent='1 letter, wholly in code',
    cipher='Catalogue: "A letter, written in code, addressed to Mr. Benjamin Farar of Southington, from a Goshen resident who signed only the first and last letters of his first and last names". No decipherment mentioned.',
    decode='Not on DECODE: known.py "Farar" found no record.',
    edition='No edition known: web search of 3 Nov 2026 found no print of the letter.',
    literature='The same search found Culper and Benjamin Church material on other Connecticut and Massachusetts codes, nothing on Farar.',
    key='No key known or held; private and undated in system, none to try without the image.',
    dup='known.py "Farar": no hit.',
    grep='Farar, Southington, Goshen'),
 'Morgan Library, Philip IV to Velada, 35 letters (ArchiveGrid 953696074)': dict(
    where='ArchiveGrid record https://researchworks.oclc.org/archivegrid/collection/data/953696074 (read 3 Nov 2026); Morgan record found by web search, its page behind a human check; no scan linked',
    extent='35 letters, 29 Jun 1636 to 29 Mar 1641; "many" in numerical cipher',
    cipher='Morgan: "Autograph signatures to letters (35) : Madrid, to the Marquis de Velada, Spanish Ambassador to England ... Many letters are in a numerical cipher. 23 of the letters are not deciphered". The catalogue itself states the 23 have no decipherment.',
    decode='Not on DECODE: known.py "Velada" finds only catalogue 372 (The Hague, a separate letter of 17 Dec 1640) and catalogue 843 (AHNOB register, 1645).',
    edition='No edition found: web search of 3 Nov 2026 returned the Morgan records only. The Morgan also holds a copy to Malvezzi of 25 Jun 1640 and cipher copies to the Infante Fernando of 17 Dec 1640.',
    literature='The same search found no study of these letters or of the 1636-41 cifra.',
    key='No key held. Catalogue 372 concluded the 1640 Velada/Malvezzi cifra (Simancas, Estado, Inglaterra) is needed and not in hand. The 12 deciphered letters of this same group may give a crib; not seen.',
    dup='known.py "Velada", "Morgan" on the date range: catalogue 372 is a different letter at another holder; related, not a duplicate.',
    grep='Velada'),
}
p = os.path.join(ROOT, 'research', 'leads.json')
d = json.load(open(p, encoding='utf-8'))
done = []
for e in d['leads']:
    v = V.get(e.get('shelfmark'))
    if not v:
        continue
    e['vetting'] = dict(date='2026-11-03', by=BY,
        seen=dict(kind='not online', where=v['where'], extent=v['extent'], cipher=v['cipher']),
        prior_art=dict(decode=v['decode'], tomokiyo=TOMO.format(v['grep']), lasry=LAS.format(v['grep']), edition=v['edition'], literature=v['literature']),
        key_check=v['key'], duplicates=v['dup'], verdict='open')
    done.append(e['id'])
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(p, 'a', encoding='utf-8').write('\n')
print(done)
