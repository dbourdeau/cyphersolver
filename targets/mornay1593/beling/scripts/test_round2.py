"""The pre-registered tests of PREREG_round2.md, one run.

Test 3: the Rohan 1594 key (key/rohan1594_key.tsv, unchanged) on the new Rohan figures (transcription/v9v12_figures.tsv,
writer = Rohan). Test 4: the same key plus the four values inferred in round 1 (672 roy, 134 lo, 38 g, 160 ro) against
200 controls with random values on those four figures. Extras: the folded 1593 key and the Rohan key on the 1599
Duplessis passages; the Rohan key on the unsigned 1612 letter.

Usage, from the beling/ folder:  python3 -I scripts/test_round2.py <path to mmoiresetcorre06morn_djvu.txt>
Writes results/round2_result.json and results/round2_mechanical.txt; prints a summary. Standard library only.
The language model, parse and scoring are copied unchanged from scripts/test_folded.py (round 1).
"""
import json, math, random, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
N_NULL, LANG_SIGN = 200, 190
INFERRED = {'672': 'roy', '134': 'lo', '38': 'g', '160': 'ro'}


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


def passages(writer, vol=None):
    out = []
    for line in (HERE / 'transcription/v9v12_figures.tsv').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        if f[1] == writer and (vol is None or f[2] == vol):
            out.append((f[0], toks(f[6])))
    return out


# ---------- language model (as round 1) ----------
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
    tot = sum(lm.logp(p) for p in pieces if p)
    n = sum(len(p) for p in pieces)
    return tot / n if n else float('nan'), n


# ---------- parses (as round 1) ----------
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
    return not (' ' in val or int(fig) >= 600 or (val[0].isupper() and len(val) > 2))


def run(pas, key, mode):
    n = ok = 0
    pieces, lines = [], []
    for pid, gs in pas:
        cur, shown = '', []
        for g in gs:
            if not g.isdigit():
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


def summary(name, pas, key, mode, lm, seed):
    n, ok, pieces, lines = run(pas, key, mode)
    L, nl = lang_score(lm, pieces)
    rng = random.Random(seed)
    figs, vals = list(key.keys()), list(key.values())
    null = []
    for _ in range(N_NULL):
        v2 = vals[:]
        rng.shuffle(v2)
        null.append(lang_score(lm, run(pas, dict(zip(figs, v2)), mode)[2])[0])
    good = [x for x in null if x == x]
    beaten = sum(1 for x in null if L == L and x == x and L > x)
    r = {'name': name, 'groups': n, 'read': ok, 'coverage': round(ok / n, 4) if n else None,
         'letters_scored': nl, 'lang_score': round(L, 4) if L == L else None,
         'lang_null_mean': round(sum(good) / len(good), 4) if good else None,
         'lang_null_best': round(max(good), 4) if good else None,
         'lang_beats': beaten, 'lang_sign': beaten >= LANG_SIGN}
    return r, lines


def verdict(r):
    if r['read'] < 20 or r['letters_scored'] < 30:
        return 'too small'
    if r['coverage'] >= 0.50 and r['lang_sign']:
        return 'fits'
    if r['coverage'] < 0.30 or not r['lang_sign']:
        return 'does not fit'
    return 'inconclusive'


def test4(pas, key, lm, seed):
    ext = dict(key)
    ext.update(INFERRED)
    occ = [(pid, g) for pid, gs in pas for g in gs if g in INFERRED and len(gs) >= 2]
    n, ok, pieces, lines = run(pas, ext, 'rohan')
    L, nl = lang_score(lm, pieces)
    r = {'occurrences_in_runs': occ, 'lang_score_extended': round(L, 4) if L == L else None,
         'letters_scored': nl}
    base = lang_score(lm, run(pas, key, 'rohan')[2])[0]
    r['lang_score_base_key'] = round(base, 4) if base == base else None
    if not occ:
        r['verdict'] = 'not testable'
        return r, lines
    pool = [v for f, v in key.items() if rohan_scored(f, v)]
    rng = random.Random(seed)
    null = []
    for _ in range(N_NULL):
        k2 = dict(key)
        for f in INFERRED:
            k2[f] = rng.choice(pool)
        null.append(lang_score(lm, run(pas, k2, 'rohan')[2])[0])
    beaten = sum(1 for x in null if L > x)
    r.update({'null_mean': round(sum(null) / len(null), 4), 'null_best': round(max(null), 4),
              'beats': beaten, 'ties_or_better_in_null': sum(1 for x in null if x >= L),
              'verdict': 'supported' if beaten >= LANG_SIGN else 'not supported'})
    return r, lines


def main():
    lm = Tri(Path(sys.argv[1]).read_text(encoding='utf-8', errors='replace'))
    rohan = read_key('key/rohan1594_key.tsv')
    folded = read_key('key/key_dudout.tsv')
    R = passages('Rohan')
    R11 = passages('Rohan', '11')
    Rruns = [p for p in R if len(p[1]) >= 2]
    D = passages('Duplessis')
    U = passages('unknown')

    res, mech = {}, []
    for name, pas, key, mode, seed in [
        ('T3_rohan_on_new_Rohan (primary)', R, rohan, 'rohan', 2026),
        ('T3_side_1611_12_only', R11, rohan, 'rohan', 2026),
        ('T3_side_runs_of_2_or_more', Rruns, rohan, 'rohan', 2026),
        ('extra_folded_on_Duplessis_1599', D, folded, 'folded', 2026),
        ('extra_rohan_on_Duplessis_1599', D, rohan, 'rohan', 2026),
        ('extra_rohan_on_unsigned_1612', U, rohan, 'rohan', 2026),
    ]:
        r, lines = summary(name, pas, key, mode, lm, seed)
        res[name] = r
        mech.append(f'## {name}  (key: {"key_dudout" if mode == "folded" else "rohan1594"}; [n] = no value)')
        mech += lines
        mech.append('')
    res['verdict_T3'] = verdict(res['T3_rohan_on_new_Rohan (primary)'])
    t4, lines4 = test4(R, rohan, lm, 2027)
    res['T4_inferred_values'] = t4
    mech.append('## T4  rohan1594 + 672 roy, 134 lo, 38 g, 160 ro  ([n] = no value)')
    mech += lines4
    res['lm'] = {'corpus_letters': lm.n, 'alphabet': lm.V}
    (HERE / 'results/round2_result.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'results/round2_mechanical.txt').write_text('\n'.join(mech) + '\n', encoding='utf-8')
    for k, v in res.items():
        print(k, v)


if __name__ == '__main__':
    main()
