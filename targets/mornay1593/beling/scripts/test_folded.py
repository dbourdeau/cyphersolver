"""The two pre-registered tests of PREREG.md, one run.

Test 1: Dudout's folded 1593 key (key/key_dudout.tsv) on the 1595-97 figures (part A: the repo's lomenie1595.txt and
duplessis1597.txt; part B: transcription/v7v8_figures.tsv, Duplessis passages). Control: the 1593 ciphertext.
Test 2 (Addendum 1): the Rohan 1594 key (key/rohan1594_key.tsv) on the Rohan 1597 figures (v7v8_figures.tsv, writer Rohan).

Usage, from the beling/ folder:  python3 -I scripts/test_folded.py <path to mmoiresetcorre06morn_djvu.txt>
Writes results/test_result.json and results/mechanical.txt; prints a summary. Standard library only.
"""
import json, math, random, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
N_NULL, LANG_SIGN = 200, 190


# ---------- inputs ----------
def read_key(path):
    key = {}
    for line in (HERE / path).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        key[f[0].strip()] = f[1].strip()
    return key


def toks(field):
    return [t.strip('.,') for t in field.split() if t.strip('.,')]


def repo_passages(path, gfield, keep):
    out = []
    for line in (HERE / path).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#') or '|' not in line:
            continue
        f = [x.strip() for x in line.split('|')]
        if keep(f[0]):
            out.append((f[0], toks(f[gfield])))
    return out


def v7v8(writer):
    out = []
    for line in (HERE / 'transcription/v7v8_figures.tsv').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        if f[1] == writer:
            out.append((f[0], toks(f[6])))
    return out


# ---------- language model: letter trigrams, add-0.1 ----------
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('j', 'i').replace('v', 'u')
    return ''.join(c for c in s if 'a' <= c <= 'z')


class Tri:
    def __init__(self, text, k=0.1):
        t = norm(text)
        self.k, self.V = k, len(set(t))
        self.u, self.b, self.t = {}, {}, {}
        for i, c in enumerate(t):
            self.u[c] = self.u.get(c, 0) + 1
            if i >= 1:
                self.b[t[i - 1:i + 1]] = self.b.get(t[i - 1:i + 1], 0) + 1
            if i >= 2:
                self.t[t[i - 2:i + 1]] = self.t.get(t[i - 2:i + 1], 0) + 1
        self.n = len(t)

    def logp(self, s):
        k, V, lp = self.k, self.V, 0.0
        for i, c in enumerate(s):
            if i == 0:
                lp += math.log((self.u.get(c, 0) + k) / (self.n + k * V))
            elif i == 1:
                lp += math.log((self.b.get(s[:2], 0) + k) / (self.u.get(s[0], 0) + k * V))
            else:
                lp += math.log((self.t.get(s[i - 2:i + 1], 0) + k) / (self.b.get(s[i - 2:i], 0) + k * V))
        return lp


def lang_score(lm, pieces):
    """Mean log-prob per letter over all pieces, each scored on its own."""
    tot = sum(lm.logp(p) for p in pieces if p)
    n = sum(len(p) for p in pieces)
    return tot / n if n else float('nan'), n


# ---------- the two parses ----------
def folded_read(key, g):
    if not g.isdigit():
        return None
    if g in key:
        return key[g]
    for k in range(1, len(g)):
        a, b = g[:k], g[k:]
        if a[0] != '0' and b[0] != '0' and a in key and b in key:
            return key[a] + key[b]
    return None


def rohan_scored(fig, val):
    """Letter and syllable values are scored; words (figures 600+), names and phrases are not."""
    return not (' ' in val or int(fig) >= 600 or (val[0].isupper() and len(val) > 2))


def run(passages, key, mode):
    """Return coverage numbers, LM pieces and a mechanical line per passage."""
    n = ok = 0
    pieces, lines = [], []
    for pid, gs in passages:
        cur, shown = '', []
        for g in gs:
            if not g.isdigit():          # letters printed by the editors: not a group, a cut
                if cur: pieces.append(cur)
                cur = ''
                shown.append('<' + g + '>')
                continue
            n += 1
            if mode == 'folded':
                v = folded_read(key, g)
                scored = v is not None
            else:
                v = key.get(g)
                scored = v is not None and rohan_scored(g, v)
            if v is None:
                shown.append('[' + g + ']')
                if cur: pieces.append(cur)
                cur = ''
                continue
            ok += 1
            shown.append(v)
            if scored:
                cur += norm(v)
            else:
                if cur: pieces.append(cur)
                cur = ''
        if cur:
            pieces.append(cur)
        lines.append(f'{pid}\t' + ' '.join(shown))
    return n, ok, pieces, lines


def coverage_null(passages, key, lo, hi, seed):
    rng = random.Random(seed)
    letters = list(key.values())
    out = []
    for _ in range(N_NULL):
        nums = rng.sample(range(lo, hi + 1), len(letters))
        k2 = {str(x): l for x, l in zip(nums, letters)}
        n, ok, _, _ = run(passages, k2, 'folded')
        out.append(ok / n)
    return out


def lang_null(passages, key, mode, lm, seed):
    rng = random.Random(seed)
    figs, vals = list(key.keys()), list(key.values())
    out = []
    for _ in range(N_NULL):
        v2 = vals[:]
        rng.shuffle(v2)
        k2 = dict(zip(figs, v2))
        _, _, pieces, _ = run(passages, k2, mode)
        out.append(lang_score(lm, pieces)[0])
    return out


def evaluate(name, passages, key, mode, lm, seed, cov_null_range=None):
    n, ok, pieces, lines = run(passages, key, mode)
    L, nletters = lang_score(lm, pieces)
    ln = lang_null(passages, key, mode, lm, seed)
    beaten = sum(1 for x in ln if L > x)
    r = {'name': name, 'groups': n, 'read': ok, 'coverage': round(ok / n, 4) if n else None,
         'letters_scored': nletters, 'lang_score': round(L, 4) if L == L else None,
         'lang_null_mean': round(sum(x for x in ln if x == x) / max(1, sum(1 for x in ln if x == x)), 4),
         'lang_null_best': round(max(x for x in ln if x == x), 4) if any(x == x for x in ln) else None,
         'lang_beats': beaten, 'lang_sign': beaten >= LANG_SIGN}
    if cov_null_range:
        cn = coverage_null(passages, key, *cov_null_range, seed)
        r['cov_null_mean'] = round(sum(cn) / len(cn), 4)
        r['cov_null_best'] = round(max(cn), 4)
        r['cov_margin'] = round(ok / n - max(cn), 4)
        r['cov_pass'] = (ok / n >= 0.85) and (ok / n - max(cn) >= 0.30)
    return r, lines


def main():
    corpus = Path(sys.argv[1]).read_text(encoding='utf-8', errors='replace')
    lm = Tri(corpus)
    folded = read_key('key/key_dudout.tsv')
    rohan = read_key('key/rohan1594_key.tsv')

    A = (repo_passages('transcription/repo/lomenie1595.txt', 2, lambda i: i[0] in 'LD')
         + repo_passages('transcription/repo/duplessis1597.txt', 2, lambda i: i[0] in 'CW'))
    B = v7v8('Duplessis')
    R = v7v8('Rohan')
    CTRL = repo_passages('transcription/repo/ciphertext.txt', 4, lambda i: i[0] in 'PS')

    results, mech = {}, []
    for name, pas, key, mode, seed, cov in [
        ('T1_folded_on_A (primary)', A, folded, 'folded', 1593, (2, 44)),
        ('T1_folded_on_B', B, folded, 'folded', 1593, (2, 44)),
        ('T1_control_folded_on_1593', CTRL, folded, 'folded', 1593, (2, 44)),
        ('T2_rohan_on_Rohan1597 (primary)', R, rohan, 'rohan', 1594, None),
        ('extra_folded_on_Rohan1597', R, folded, 'folded', 1593, (2, 44)),
        ('extra_rohan_on_A', A, rohan, 'rohan', 1594, None),
        ('extra_rohan_on_B', B, rohan, 'rohan', 1594, None),
    ]:
        r, lines = evaluate(name, pas, key, mode, lm, seed, cov)
        results[name] = r
        mech.append(f'## {name}  (key: {"key_dudout" if mode == "folded" else "rohan1594"}; [n] = no value, <x> = letter printed by the editors)')
        mech += lines
        mech.append('')

    t1, t2 = results['T1_folded_on_A (primary)'], results['T2_rohan_on_Rohan1597 (primary)']
    v1 = ('fits' if t1['cov_pass'] and t1['lang_sign'] else
          'does not fit' if (not t1['cov_pass'] and not t1['lang_sign']) else 'inconclusive')
    if t2['read'] < 20:
        v2 = 'too small'
    elif t2['coverage'] >= 0.50 and t2['lang_sign']:
        v2 = 'fits'
    elif t2['coverage'] < 0.30 or not t2['lang_sign']:
        v2 = 'does not fit'
    else:
        v2 = 'inconclusive'
    results['verdict_T1'] = v1
    results['verdict_T2'] = v2
    results['lm'] = {'corpus_letters': lm.n, 'alphabet': lm.V}

    (HERE / 'results/test_result.json').write_text(json.dumps(results, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'results/mechanical.txt').write_text('\n'.join(mech) + '\n', encoding='utf-8')
    for k, v in results.items():
        print(k, v)


if __name__ == '__main__':
    main()
