"""Held-out test for 2393: apply the FROZEN key (Dudout v6, imported unchanged, key_frozen.tsv) to the whole 2393
transcription (no line of 2393 was used to build v6), and compare with control keys in which the consonant values
of the base signs are shuffled (vowel digits, word signs and codes kept). Scoring: Dan's docs/_check_reading.py
(--file) on the unspaced mechanical text: Italian coverage and clean-sentence share.
    python scripts/heldout.py <cyphersolver worktree> [n_controls]"""
import json, pathlib, random, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE)); import decrypt as D
wt = pathlib.Path(sys.argv[1]); n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
def score(K, tag):
    out = ROOT / 'work' / f'heldout_{tag}.txt'
    with open(out, 'w', encoding='utf-8') as f:
        for lab, toks in D.lines(ROOT / 'transcription_666.txt'):
            f.write(lab + ': ' + ''.join(D.decode(toks, K)) + '\n')
    r = subprocess.run([sys.executable, 'docs/_check_reading.py', '--file', str(out)], cwd=wt, capture_output=True, text=True, encoding='utf-8', env={'PYTHONUTF8': '1', **__import__('os').environ})
    j = json.loads(r.stdout[r.stdout.index('{'):])
    return j['coverage'], j['clean_share']
K = D.load_key(ROOT / 'key_frozen.tsv')
res = {'frozen': score(K, 'frozen')}
cons = [b for b, v in K['base'].items() if v not in ('et', 'non', 'per', 'ancora', 'senza') and len(v) <= 2]
rng = random.Random(2393)
for i in range(n):
    K2 = json.loads(json.dumps(K)); vals = [K['base'][b] for b in cons]; rng.shuffle(vals)
    for b, v in zip(cons, vals): K2['base'][b] = v
    res[f'control{i+1}'] = score(K2, f'control{i+1}')
for k, (c, s) in res.items(): print(f'{k}\tcoverage {c:.3f}\tclean_share {s:.3f}')
