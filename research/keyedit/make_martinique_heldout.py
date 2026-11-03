"""Held-out check for the open run on Martinique f.88. Blank N interlinear-valued groups of the start key (the
editor cannot tell them from the genuinely unknown ones); truth = key_bouille. heldout.py grades a session:
recovery of the blanked groups, damage to the kept ones, and fills of the genuinely unknown groups."""
import os, json, random
from make_martinique_task import M, H, norm, key, start   # reruns the builder (idempotent)
from collections import Counter
cnt = Counter(t for l in open(os.path.join(H, 'martinique_f88_tokens.txt'), encoding='utf-8') for t in l.split()[1:])
kb = {}
for l in open(os.path.join(M, 'key_bouille.tsv'), encoding='utf-8'):
    if l[:1].isdigit():
        g, v = l.split('\t')[:2]; kb[g] = norm(v.split('/')[0].replace('M.', 'monsieur').replace('1er', 'premier'))
elig = [t for t in cnt if kb.get(t) and len(kb[t]) > 0]
N = 15
for seed in (1, 2, 3):
    r = random.Random(100 + seed)
    held = sorted(r.sample(elig, N))
    sk = dict(start)
    for t in held: sk[t] = ''
    spec = json.load(open(os.path.join(H, 'martinique_task_f88.json'), encoding='utf-8'))
    spec.update(name=f'martinique1778-f88-held{seed}', start_key=sk, truth_key={t: kb.get(t, '') for t in start}, heldout=held)
    json.dump(spec, open(os.path.join(H, f'martinique_task_f88_h{seed}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(seed, 'held', len(held), 'groups =', sum(cnt[t] for t in held), 'tokens:', held)
