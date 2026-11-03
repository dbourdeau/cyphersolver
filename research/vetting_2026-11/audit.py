"""Tally the batches and sort what is left: python research/vetting_2026-11/audit.py"""
import collections, glob, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
leads = {}
for f in sorted(HERE.glob('in_b*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')): leads[str(x['id'])] = x
out = {}
for f in sorted(HERE.glob('out_b*.json')):
    out.update(json.loads(f.read_text(encoding='utf-8')))
c = collections.Counter(b.get('verdict', 'unvetted') for b in out.values())
print(len(leads), 'leads', len(out), 'answered', dict(c))
FLAG = re.compile(r'not opened|could not open|unopened|could not be opened|not seen|unverified|did not open|lending|may be|might|not shown|not excluded|could not', re.I)
hold = []
for i, b in out.items():
    if b.get('verdict') != 'open': continue
    t = json.dumps(b.get('prior_art'), ensure_ascii=False) + ' ' + b.get('key_check', '')
    m = FLAG.findall(json.dumps(b.get('prior_art'), ensure_ascii=False))
    if m: hold.append((int(i), sorted({x.lower() for x in m}), leads[i]['title'][:60]))
print('open with a caveat in prior_art:', len(hold))
kinds = collections.Counter(b['seen']['kind'] for b in out.values() if b.get('verdict') == 'open')
print('open by seen.kind', kinds)
un = {i: b for i, b in out.items() if 'verdict' not in b}
host = collections.Counter()
chrome = []
for i, b in un.items():
    t = b['unvetted']
    if re.search(r'chrome', t, re.I): chrome.append(int(i))
    for x in leads[i].get('links') or []:
        h = re.sub(r'^https?://(www\.)?', '', x.get('href', '')).split('/')[0]; host[h] += 1; break
print('unvetted', len(un), 'naming Chrome', len(chrome))
print(host.most_common(30))
json.dump({'hold': hold}, open(HERE / 'audit_hold.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
