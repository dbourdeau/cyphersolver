"""Write the vetting blocks of the two NYC leads (4 Nov 2026)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BY = 'claude NYC archives sweep (research/nyc_sweep/)'
TOMO = ('cryptiana.web.fc2.com/code/livingst.htm fetched 4 Nov 2026 and grepped for Duportail and Gouverneur: only the Morris-Jay '
        '(WE006) and Morris-Franklin (WE008) codes, which Gouverneur Morris filled out for the Finance Office; no Duportail, no 1794 '
        'item. The rest of the cryptiana text pages were mirrored and grepped for other names on 3 Nov 2026 (no hit).')
LAS = 'GL.htm (the copy in a repo worktree) grepped 4 Nov 2026 for Duportail, Pinckney, Gouverneur Morris and Livingston: no hit. No Lasry or HistoCrypt item found by web search.'
V = {
 'Columbia RBML, Gouverneur Morris papers, 1768-1816, Box 3, items 241, 1094 and 1099': dict(
    seen=dict(kind='not online', where='Columbia finding aid, item page https://findingaids.library.columbia.edu/archives/cul-4079134_aspace_982555e91ea23a06ff64cf9bb3167165 (item 241, read 4 Nov 2026 in Chrome); items 1094 and 1099 from the search results of the same finding aid. No digital object',
              extent='item 241 is 4 p.; 1094 and 1099 are 1 p. each',
              cipher='Item 241: "Document type: transcription, in Morris\' hand, of cypher message transmitted to Morris through Thomas Pinckney. Place: [London]. Notes: and message in cypher, 4 p." Items 1094 ([Pinckney], May 1794?) and 1099 (Pinckney, London, 23 Aug 1794): "enclosing message in cypher, 1 p." No decipherment is mentioned; whether the "transcription" is of the groups or a decipherment is not stated.'),
    prior_art=dict(decode='Not on DECODE: known.py on Duportail, Gouverneur Morris and Pinckney found no DECODE record (hits are catalogue rows on other Morris and Pinckney papers and this sweep\'s own README).',
        tomokiyo=TOMO, lasry=LAS,
        edition='Web searches of 4 Nov 2026 (Duportail 1794 cypher Morris Pinckney; Morris diary 1794) found no print of these three items. The Diaries of Gouverneur Morris have a gap from 5 Jan 1793 to 12 Oct 1794; Founders Online prints Pinckney to Jefferson of 1793 on the swapped Morris and Pinckney cyphers. Davenport\'s and Sparks\'s editions not checked page by page.',
        literature='No study of Duportail\'s 1794 message or of the Morris-Pinckney cypher found by web search.'),
    key='No key held. Pinckney\'s letters to Jefferson of Feb and Mar 1793 (Founders Online) say he had lost and then recovered Morris\'s cypher and compared it with his own, so a Morris-Pinckney cypher existed; it is not in the finding aid. The Morris-Jay (WE006) and Morris-Franklin (WE008) codes of 1782-83 are known and not tested.',
    dup='known.py "Duportail", "Gouverneur Morris", "Pinckney": no catalogue or lead entry for these Columbia items. Other Morris items in the same finding aid (Morris to Jay 1 Jan 1783, printed with its decipherment in the Papers of John Jay; Robert Morris 8 Aug 1790, transcription of the decoded text) were closed and left out.'),
 'Center for Brooklyn History, Mid-Atlantic early manuscripts collection 1974.002, Box 1, Folder 25': dict(
    seen=dict(kind='not online', where='https://findingaids.library.nyu.edu/cbh/1974_002/all/ (read 4 Nov 2026 in Chrome, after the NYU human check); no digital object',
              extent='one letter in a folder of mixed items',
              cipher='Finding aid: "1803 letter from Robert R. Livingston at Paris to his brother re: negotiations for the Louisiana purchase, mentions James Monroe and Talleyrand, partly in cipher handwriting." No decipherment mentioned; "cipher handwriting" may only mean cursive.'),
    prior_art=dict(decode='Not on DECODE: known.py "Livingston" finds catalogue and lead rows on his 1781-82 letters, none on this folder.',
        tomokiyo=TOMO, lasry=LAS,
        edition='Web search of 4 Nov 2026 found the famous coded letter to Madison of 12-13 April 1803 (Historic New Orleans Collection; Papers of Madison, Founders Online) and no brother letter in print.',
        literature='No study of a Livingston letter to a brother at Brooklyn History found.'),
    key='No key held. The Madison letter of April 1803 used the State Department number code, decoded in print; whether this letter does is unknown.',
    dup='known.py "Livingston": no entry for this folder or for a letter to his brother.'),
}
p = os.path.join(ROOT, 'research', 'leads.json')
d = json.load(open(p, encoding='utf-8'))
done = []
for e in d['leads']:
    v = V.get(e.get('shelfmark'))
    if not v:
        continue
    e['vetting'] = dict(date='2026-11-04', by=BY, seen=v['seen'], prior_art=v['prior_art'], key_check=v['key'],
                        duplicates=v['dup'], verdict='open')
    done.append(e['id'])
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(p, 'a', encoding='utf-8').write('\n')
print('vetted', done)
