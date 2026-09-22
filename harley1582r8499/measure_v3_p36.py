"""Measure final_v3_p36.txt: non-null cipher signs of p3/p6 (transcription_v2.txt) vs [?n] left unread."""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
NULLS = {'3', '-2', 'r', 'q', 'q=', '9', 'ft', 'xo', 'rho', '0', 'th', '3r', 'tl', 'XX', 'e',
         'NULL_LOOP', 'NULL_LOOP_BAR', 'CE_UNSEEN'}
tot, nul = {}, {}
for l in open(os.path.join(HERE, 'transcription_v2.txt'), encoding='utf8'):
    if not l.startswith(('p3.', 'p6.')): continue
    tag, body = l.split(' ', 1)
    toks = [t for t in re.sub(r'\[[^\]]*\]', ' ', body).split() if t not in ('.', ':')]
    tot[tag] = sum(t not in NULLS for t in toks); nul[tag] = sum(t in NULLS for t in toks)
unread = {}
for l in open(os.path.join(HERE, 'final_v3_p36.txt'), encoding='utf8'):
    m = re.match(r'(p[36]\.\d\d) \|(.*)', l)
    if m: unread[m.group(1)] = sum(int(n) for n in re.findall(r'\[\?(\d+)\]', m.group(2)))
bad = [t for t in tot if t not in unread or unread[t] > tot[t]]
assert not bad, bad
T, U = sum(tot.values()), sum(unread.values())
print(f'# measure: {T} non-null signs ({sum(nul.values())} nulls excluded), {U} unread, {T-U} read = {100*(T-U)/T:.1f}%')
for pg in ('p3', 'p6'):
    t = sum(v for k, v in tot.items() if k.startswith(pg)); u = sum(v for k, v in unread.items() if k.startswith(pg))
    print(f'#   {pg}: {t-u}/{t} = {100*(t-u)/t:.1f}%')
