"""Decode 27 May 1549 c.31r with the frozen key and score it against the contemporary decipherment (c.12r).
Run: python3 -I decode_cv1549.py   (reads 27may1549_31r.tsv, key_cv1549.tsv, ref_blocks.json from this folder)
Rules, fixed before the first run:
 - each shape label decodes to its key value; basis 'none' -> '?' (a hole); 'slash' is a separator and is skipped.
 - brace tokens are clear text. The three anchors that split the blocks ({Quanto alos}, {y es muy ...}, {Enlo demas tocante})
   are not scored. The short clear-letter words inside cipher (em, ne, sa, tus, quod, nec, pre) are code words not in the key:
   holes ('?').
 - blocks: B1 = after {Quanto alos} to before {y es muy...}; B2 = after it to before {Enlo demas tocante}; B3 = the rest of 31r.
 - scoring is per letter. Both texts are lower-cased, spaces and punctuation removed, v->u, j->i, ç->c (one normalisation for both).
   A hole is one character '#' that matches nothing. Alignment: Levenshtein with unit costs. B1 and B2 are aligned globally
   (their whole decipherment passage); B3 stops at the foot of 31r, so its alignment lets the reference end anywhere (free end gap
   in the reference only), and the reference letters counted are those up to the chosen end.
 - strict figure = reference letters matched by an identical decoded letter / reference letters in the span. No emendation.
"""
import json, os, sys, random
D = os.path.dirname(os.path.abspath(__file__))
CODE = {'em','ne','sa','tus','quod','nec','pre'}
ANCH = ['Quanto alos', 'y es muy', 'Enlo demas tocante']

def load_key(path=os.path.join(D,'key_cv1549.tsv')):
    k = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        k[f[0]] = (f[1], f[2])
    return k

def load_tr(path=os.path.join(D,'27may1549_31r.tsv')):
    out = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        out.append((int(f[0]), f[1], f[2]))
    return out

def blocks(tr):
    b = {'B1': [], 'B2': [], 'B3': []}; cur = None
    for ln, tok, fl in tr:
        if tok.startswith('{'):
            t = tok[1:-1]
            if t.startswith(ANCH[0]): cur = 'B1'; continue
            if t.startswith(ANCH[1]): cur = 'B2'; continue
            if t.startswith(ANCH[2]): cur = 'B3'; continue
        b[cur].append((ln, tok, fl))
    return b

def dec(tokens, key):
    units = []
    for ln, tok, fl in tokens:
        if tok == 'slash': continue
        if tok.startswith('{'):
            units.append((ln, tok, '?')); continue
        v, basis = key[tok]
        units.append((ln, tok, '?' if basis == 'none' else v))
    return units

def norm(s):
    s = s.lower().replace('ç','c').replace('v','u').replace('j','i')
    return ''.join(ch for ch in s if ch.isalpha() or ch == '#')

def align(a, r, free_end):
    """a decoded (with #), r reference. Returns (matches, ref_len_used, ops)."""
    n, m = len(a), len(r)
    INF = 10**9
    dp = [[0]*(m+1) for _ in range(n+1)]
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i
        for j in range(1, m+1):
            c = 0 if (a[i-1] == r[j-1] and a[i-1] != '#') else 1
            dp[i][j] = min(dp[i-1][j-1]+c, dp[i-1][j]+1, dp[i][j-1]+1)
    jend = min(range(m+1), key=lambda j: (dp[n][j], -j)) if free_end else m
    i, j, match, ops = n, jend, 0, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + (0 if (a[i-1]==r[j-1] and a[i-1]!='#') else 1):
            ok = a[i-1]==r[j-1] and a[i-1]!='#'; match += ok
            ops.append((a[i-1], r[j-1], 'M' if ok else 'S')); i, j = i-1, j-1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            ops.append((a[i-1], '-', 'I')); i -= 1
        else:
            ops.append(('-', r[j-1], 'D')); j -= 1
    return match, jend, ops[::-1]

def score(key, tr, refs, detail=False):
    b = blocks(tr); res = {}
    for name in ('B1','B2','B3'):
        u = dec(b[name], key)
        s = norm(''.join('#' if v == '?' else v for _,_,v in u))
        r = norm(refs[name])
        m, jend, ops = align(s, r, free_end=(name == 'B3'))
        res[name] = dict(units=len(u), holes=sum(v=='?' for _,_,v in u), matched=m, ref_letters=jend, decoded=s, ref=r[:jend], ops=ops if detail else None)
    return res

if __name__ == '__main__':
    key, tr = load_key(), load_tr()
    refs = json.load(open(os.path.join(D,'ref_blocks.json'), encoding='utf-8'))
    res = score(key, tr, refs, detail=True)
    with open(os.path.join(D,'27may1549_decryption.txt'),'w',encoding='utf-8') as f:
        f.write('# 27 May 1549 c.31r decoded with key_cv1549.tsv (first pass, figure of record). [unit] per sign; ? = hole.\n')
        for ln in sorted({l for l,_,_ in tr}):
            us = [(t, v) for l,t,v in dec([x for x in tr if x[0]==ln and not (x[1].startswith('{') and any(x[1][1:-1].startswith(a) for a in ANCH))], key) if l == ln]
            clear = [x[1] for x in tr if x[0]==ln and x[1].startswith('{') and any(x[1][1:-1].startswith(a) for a in ANCH)]
            f.write(f'{ln}\t' + (' '.join(clear) + ' ' if clear else '') + ' '.join(f'[{v}]' for t,v in us) + '\n')
    tot_m = sum(r['matched'] for r in res.values()); tot_r = sum(r['ref_letters'] for r in res.values())
    with open(os.path.join(D,'27may1549_score.txt'),'w',encoding='utf-8') as f:
        for k, r in res.items():
            line = f"{k}: units {r['units']}, holes {r['holes']}, matched {r['matched']} of {r['ref_letters']} reference letters = {100*r['matched']/r['ref_letters']:.1f}%"
            print(line); f.write(line+'\n')
            f.write('  decoded:   '+r['decoded']+'\n  reference: '+r['ref']+'\n  aligned:   '+''.join(o[0] for o in r['ops'])+'\n             '+''.join(o[1] for o in r['ops'])+'\n             '+''.join({'M':'|','S':'x','I':'+','D':'-'}[o[2]] for o in r['ops'])+'\n')
        line = f"ALL: matched {tot_m} of {tot_r} = {100*tot_m/tot_r:.1f}%"
        print(line); f.write(line+'\n')
