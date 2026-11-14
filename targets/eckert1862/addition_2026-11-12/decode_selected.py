"""Reproduce selected No.2 substitutions; unrecognized words are NOT certified clear.
Run python3 -I targets/eckert1862/addition_2026-11-12/decode_selected.py.
Key extraction is partial. Explicit occurrence exclusions prevent plain names,
headings and the post-signature null tail from being mistaken for code words.
"""
from pathlib import Path
import csv, json, re

HERE = Path(__file__).resolve().parent
RAW = HERE / 'source_records'
key = {r['code'].lower(): r for r in csv.DictReader((HERE/'key_book2_selected.tsv').open(), delimiter='\t')}
derived = {
    'patenting': ('patent','advancing'), 'quickened': ('quicken','detached'),
    'rewarding': ('reward','following'), 'swindled': ('swindle','moved'),
    'jaunts': ('jaunt',"Lee's"), 'javelins': ('javelin',"Lee's"),
    'horaces': ('horace',"Richmond's"), 'saints': ('saint','forces'),
    'pacifics': ('pacific','batteries'), 'wafers': ('wafer','rivers'),
    'widows': ('widow','troops'), 'tobsy': ('topsy','12:30 p.m.'),
    'abbott': ('abbot','James'),
}
u1 = '''For Nestor It is the opinion of
Midas that Early is patenting on World
Bermuda and the Bard & Biscay Walnut
with a large salem quickened from Jaunts
Peru Wiley Lady Tobsy nasty day this'''
texts = {'U1': u1}
for p in [9,10]:
    text = json.loads((RAW/f'eckert19_p{p}.json').read_text())['transc']
    # Explicit image corrections, preserving downloaded volunteer JSON unchanged.
    if p == 9: text = text.replace('Snake Pine Talbot', 'Snake Peru Talbot')
    if p == 10: text = text.replace('For Tulip.', 'For Grant Tulip.')
    texts[f'p{p}'] = text
out, ledger = [], []
for name, text in texts.items():
    out.append(f'== {name}\n')
    for n,line in enumerate(text.splitlines(),1):
        # These tails follow signature/time material in the inspected sources.
        # A word can be a code elsewhere (e.g. Nasty) without being body text here.
        tail_marker = 'nasty day this' if name == 'U1' else 'How you make it go' if name == 'p10' else None
        tail_start = line.find(tail_marker) if tail_marker else -1
        def sub(m):
            w=m.group(); k=w.lower()
            if tail_start >= 0 and m.start() >= tail_start: return w
            # Book number, operator and plain signatures remain outside lookup.
            if name=='p9' and n==1: return w
            if name=='p9' and w=='Baldwin': return w
            # Day/month-number meanings are not inferred from proper-name headings.
            d=derived.get(k)
            if d: base,meaning=d; row=key[base]
            elif k in key: row=key[k]; meaning=row['meaning']
            else: return w
            ledger.append([name,n,w,meaning,row['page'],row['note']])
            return '['+meaning+']'
        out += [line, '→ '+re.sub(r'[A-Za-z]+',sub,line), '']
(HERE/'literal_selected.txt').write_text('\n'.join(out)+'\n')
with (HERE/'applied_key_ledger.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['message','line','cipher_word','meaning','key_page','note']);w.writerows(ledger)
print(f'{len(key)} selected key entries; {len(ledger)} substitutions. Unmatched words still require review.')
