"""Build task.json for Pelissier 1592: truth = pass-3 primary letters (cands.txt), start = pass-2 key (dec.K0)."""
import os, sys, json
P = os.path.join(os.path.dirname(__file__), '..', '..', 'targets', 'pelissier1592')
sys.path.insert(0, P); os.chdir(P)
import beam
from dec import K0
truth = {t: v[0][0] for t, v in beam.C.items()}
files = ['../../targets/pelissier1592/t4[6-9][rv].txt', '../../targets/pelissier1592/t50r.txt']
import glob, re
toks = set()
for pat in files:
    for f in glob.glob(os.path.join(os.path.dirname(__file__), pat)):
        for l in open(f, encoding='utf-8'):
            m = re.match(r'(C\d+):\s*(.*)', l)
            if m: toks.update(m.group(2).split())
truth = {t: (truth.get(t, '') if truth.get(t, '').isalpha() else '') for t in toks}
start = {t: K0.get(t, '') for t in toks}
spec = dict(name='pelissier1592-pass2-to-pass3', model='fr-1600-letters', norm='early', spaces=False,
            token_files=files, truth_key=truth, start_key=start)
json.dump(spec, open(os.path.join(os.path.dirname(__file__), 'pelissier_task.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(toks), 'tokens;', sum(truth[t] != start[t] for t in toks), 'differ')
