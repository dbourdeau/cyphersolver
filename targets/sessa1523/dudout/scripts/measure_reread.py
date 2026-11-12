"""One measure per PREREG_measure.md: re-read vs b34 (a) on the changed lines of R9660 ff.141v-146v, one fixed key,
400 controls (200 permuted letter keys, 200 within-line shuffles), seed 1523.
usage: measure_reread.py b34_lines.json align_table.json changes.tsv LANG_PARENT_DIR"""
import json, re, sys, random, importlib.util, os
sys.path.insert(0, sys.argv[4]); from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('mk', os.path.join(HERE, 'make_reread.py'))
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
FIX = {'ɞ': 'r', 'ꝛo': 's', 'ꝺ': 'u', 'ꝗ': 'd', 'ɔ': 'q', '∠': 'ñ', '6': 'e', '⅄': 'z', 'ꝍ': 'r', 'Ɉ': None, 'L': None,
       'ne': 'p', 'nf': 'p', 'nꝑ': 'p', 'v': 'm', 'b': 'v', 'Є': 'h', 'ε': 'h', 'qes': 'es'}
SKIP = {'f~', 'v:db', '▷db', '/', '..', '...', '¶', "''"}
def build_key(T):
    K = {}
    for t, c in T.items():
        vals = [(n, v) for v, n in c.items() if v != '?' and not v.startswith('[')]
        if vals: K[t] = max(vals)[1]
    K.update(FIX); return K
def cipher_tokens(lines):
    """lines: list of (a) texts in reading order -> list of token lists (quotes tracked across lines)."""
    out, q = [], False
    for a in lines:
        buf = ''
        for ch in a:
            if ch == '"': q = not q; buf += ' '; continue
            if not q: buf += ch
        buf = re.sub(r'\([^()]*\)', ' ', buf)
        out.append([t for t in buf.split() if t not in SKIP and not t.startswith('[')])
    return out
def decode(toks, K):
    s = ''
    for t in toks:
        v = K.get(t)
        if v is None: s += ' '
        elif len(t) <= 2 and len(v) == 1: s += v
        else: s += ' ' + v + ' '
    return s + ' '
def score(m, lines_toks, K):
    text = lm.norm(''.join(decode(t, K) for t in lines_toks), 'early')
    return m.per_char(' ' + text + ' '), len(text.replace(' ', ''))
if __name__ == '__main__':
    recs = json.load(open(sys.argv[1])); K = build_key(json.load(open(sys.argv[2])))
    ch = {tuple(l.split('\t')[:2]) for l in open(sys.argv[3]).read().splitlines()[1:]}
    idx = [i for i, r in enumerate(recs) if (r['page'], r['line']) in ch]
    new_all = cipher_tokens([mk.apply(r) for r in recs]); old_all = cipher_tokens([mk.norm_old(r) for r in recs])
    new = [new_all[i] for i in idx]; old = [old_all[i] for i in idx]
    m = lm.load('es-golden-age')
    s_new, n_new = score(m, new, K); s_old, n_old = score(m, old, K)
    rng = random.Random(1523)
    letters = sorted(t for t, v in K.items() if v and len(v) == 1 and len(t) <= 2)
    perm, shuf = [], []
    for _ in range(200):
        vals = [K[t] for t in letters]; rng.shuffle(vals)
        K2 = dict(K); K2.update(zip(letters, vals)); perm.append(score(m, new, K2)[0])
    for _ in range(200):
        sh = []
        for toks in new:
            t2 = list(toks); rng.shuffle(t2); sh.append(t2)
        shuf.append(score(m, sh, K)[0])
    allc = perm + shuf
    p = (1 + sum(1 for c in allc if c >= s_new)) / (1 + len(allc))
    print(f'portion: {len(idx)} lines; decoded letters re-read {n_new}, b34 {n_old}')
    print(f'S re-read  = {s_new:.4f}')
    print(f'S b34 (a)  = {s_old:.4f}')
    print(f'permuted keys (200): max {max(perm):.4f} mean {sum(perm)/200:.4f}')
    print(f'shuffles (200):      max {max(shuf):.4f} mean {sum(shuf)/200:.4f}')
    print(f'empirical p = {p:.4f}')
    c1 = s_new > max(allc); c2 = s_new > s_old
    print(f'criterion 1 (above all 400 controls): {"PASS" if c1 else "FAIL"}')
    print(f'criterion 2 (re-read > b34 under same key): {"PASS" if c2 else "FAIL"}')
    print(f'void (< 300 letters): {n_new < 300}')
