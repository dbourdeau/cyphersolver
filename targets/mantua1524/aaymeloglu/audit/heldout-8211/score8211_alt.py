"""Secondary figures for HELDOUT-8211.md: (B) reading 2 at every disagreement, (C) only segments both readings agree on.
Same lexicon/null/bar as score8211.py, which is imported for them (its headline run also executes and rewrites result.json)."""
import sys, re, json
sys.path.insert(0, '/Users/aaymeloglu/.claude-assistant/research/unsolved-ciphers/mantua-1524/solve')
import score8211 as S
from cipherkit.controls import permutation_z_key
L = S.L


def reading2(text):
    text = re.sub(r'\[([^\]]*?)/([^\]]*?)\]\??', lambda m: m.group(2), text)   # [r1 / r2]? -> r2
    out = []
    for x in text.split():
        if x == '.':
            continue
        m = re.fullmatch(r'(.*?)\{(.*)\}\??', x)
        if m:
            a, b = m.groups()
            if b == '-':
                continue                      # only in reading 1
            x = b[1:] if b.startswith('+') else b
        out.append(x.rstrip('?'))
    return ' '.join(out)


rows = [r for r in S.rows if r['kind'] == 'cipher']
variants = {'B_reading2': [L.units(reading2(r['text'])) for r in rows],
            'C_agreed': [L.units(r['text']) for r in rows if '{' not in r['text'] and '[' not in r['text']]}
res = {}
for lab, segs in variants.items():
    segs = [u for u in segs if u]
    S.segs[:] = segs
    zz = permutation_z_key(lambda m: S.hits(m), dict(S.key), None, n=200, seed=0)
    zz['segments'] = len(segs)
    zz['share'] = zz['observed'] / len(segs) if segs else 0
    zz['pass_bar'] = zz['share'] >= 0.40 and zz.get('z', 0) >= 5
    res[lab] = zz
    print(lab, {k: round(v, 3) if isinstance(v, float) else v for k, v in zz.items()})
json.dump(res, open(L.HERE + 'heldout8211/result_alt.json', 'w'), indent=1)
