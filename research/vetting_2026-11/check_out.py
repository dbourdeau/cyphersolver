"""Check a batch's output before it counts: python research/vetting_2026-11/check_out.py b01
Refuses shared boilerplate, so an "open" rests on searches made for that lead. Prints result: pass or result: fail."""
import collections, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'docs'))
import _check_catalogue as C
sys.stdout.reconfigure(encoding='utf-8')
nn = sys.argv[1]
leads = {str(x['id']): x for x in json.loads((HERE / f'in_{nn}.json').read_text(encoding='utf-8'))}
out = json.loads((HERE / f'out_{nn}.json').read_text(encoding='utf-8'))
bad = []
for i in leads:
    if i not in out: bad.append(f'{i}: not in the output')
for i in out:
    if i not in leads: bad.append(f'{i}: not in this batch')
blocks = {i: b for i, b in out.items() if i in leads and 'verdict' in b}
for i, b in out.items():
    if 'verdict' not in b and not (isinstance(b.get('unvetted'), str) and len(b['unvetted']) >= 25):
        bad.append(f'{i}: needs a verdict, or "unvetted" naming the blocker')
qs = collections.Counter()
for i, b in blocks.items():
    e = dict(leads[i]); e.update(b.get('lead_updates') or {})
    e['vetting'] = {k: v for k, v in b.items() if k != 'lead_updates'}
    if b['verdict'] == 'open':
        bad += [f'{i}: {p}' for p in C.vetting_problems(e)]
    elif not C.text_ok(b.get('closed')):
        bad.append(f'{i}: verdict {b["verdict"]} needs "closed" saying exactly what shows it')
    if b['verdict'] != 'open':
        continue
    s = b.get('searches')
    if not (isinstance(s, list) and len(s) >= 3 and all(isinstance(x, dict) and C.text_ok(x.get('query')) and C.text_ok(x.get('result')) for x in s)):
        bad.append(f'{i}: needs "searches": at least 3 of {{"query", "result"}}, run for this lead')
    else:
        for q in {x['query'].strip().lower() for x in s}: qs[q] += 1
    seen = b.get('seen') or {}
    if re.search(r'\b(presumably|probably|likely|perhaps|possibly|may contain|should be)\b', str(seen.get('cipher')), re.I):
        bad.append(f'{i}: seen.cipher hedges that cipher is there: show it, or write "unvetted"')
    if seen.get('kind') == 'not online' and '"' not in str(seen.get('cipher')) and '“' not in str(seen.get('cipher')) and "'" not in str(seen.get('cipher')):
        bad.append(f'{i}: seen.cipher must quote the description')
for q, n in qs.items():
    if n > 2: bad.append(f'query used for {n} leads, run one for each: {q[:70]}')
opens = [b for b in blocks.values() if b['verdict'] == 'open']
for k in C.PRIOR_ART:
    c = collections.Counter(str((b.get('prior_art') or {}).get(k)).strip() for b in opens)
    for t, n in c.items():
        if n > 2: bad.append(f'prior_art.{k} is the same text on {n} leads; say what was found for each: {t[:60]}')
for x in bad: print(x)
print(f'{len(out)}/{len(leads)} ids;', dict(collections.Counter(b.get('verdict', 'unvetted') for b in out.values())))
print('result: pass' if not bad else f'result: fail ({len(bad)})')
sys.exit(1 if bad else 0)
