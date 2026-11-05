"""Apply a vet_*.json file: attach vetting to 'open' leads and promote them; close the others (read, partly_read,
duplicate, key_lookup, not_cipher). 'unvettable' leads are left alone.  python apply.py vet_arch01.json"""
import json, os, subprocess, sys
env = dict(os.environ, PYTHONUTF8='1')
run = lambda *a: subprocess.run(['python', 'docs/_check_catalogue.py', *a], capture_output=True, text=True, env=env, encoding='utf8').stdout.strip()
v = json.load(open('research/vetting_2026-11-04/' + sys.argv[1], encoding='utf8'))
p = 'research/leads.json'
d = json.load(open(p, encoding='utf8'))
opens = [k for k, e in v.items() if e['verdict'] == 'open']
for x in d['leads']:
    if str(x['id']) in opens:
        x['vetting'] = v[str(x['id'])]['vetting']
json.dump(d, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1); open(p, 'a').write('\n')
if opens:
    print(run('--promote', *opens))
for k, e in v.items():
    if e['verdict'] in ('read', 'partly_read', 'duplicate', 'key_lookup', 'not_cipher'):
        print(run('--close', k, e['verdict'], e['note']))
    elif e['verdict'] == 'unvettable':
        print(k, 'unvettable (left)')
