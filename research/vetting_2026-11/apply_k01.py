"""Second look at the 10 entries removed as key lookups on 2 Nov 2026, under the rule of 3 Nov that a key does not block a lead, and catalogue 864.

Stay out, with a reading on record: 11 (rennes1563), 17 (maisse1593, clear copies in Brienne 13), 120 (harley1582r8499, clear copy at the BL),
559 (the file's own 19th-century sheet gives the deciphered words; leads 1943, 1944, 1622), 637 (appleton1823, 15 of 18 groups read),
849 (a key table with about 10 sample signs, no text). 650, 681 and 813 return narrowed to their unread part; 615 returns as a lead with its blocker.
864 leaves the catalogue: Warburton prints the letter in plain and a deciphered copy is catalogued at the BL.
    python research/vetting_2026-11/apply_k01.py"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _check_catalogue as C
sys.stdout.reconfigure(encoding='utf-8')
out = json.loads((HERE / 'out_k01.json').read_text(encoding='utf-8'))
removed = {x['id']: x for x in json.loads((ROOT / 'research/vetting_2026-10/removed_2026-11-02.json').read_text(encoding='utf-8'))}
doc, leads = C.load(C.LEADS, 'leads')
cat, entries = C.load(C.CAT, 'entries')
for i in (615, 650, 681, 813):
    e = dict(removed[i])
    b = dict(out[str(i)])
    if 'verdict' in b:
        e.update(b.pop('lead_updates', None) or {})
        e['vetting'] = b
    else:
        e.pop('vetting', None)
        e['vetting_note'] = b['unvetted']
    leads.append(e)
e = next(x for x in entries if x['id'] == 864)
entries.remove(e)
b = out['864']
e['vetting'] = dict(e['vetting'], verdict=b['verdict'], closed=b['closed'], evidence=b.get('evidence', ''), date='2026-11-03')
leads.append(e)
leads.sort(key=lambda x: x['id'])
C.save(C.LEADS, doc)
C.save(C.CAT, cat)
print(C.promote([i for i in (650, 681, 813) if out[str(i)].get('verdict') == 'open']))
