"""Shared machinery for the ten-hypothesis rounds (round29.py onward).

Each test function returns (p, prediction, primary, robustness). run() applies Benjamini-Hochberg at 5% across the
round, writes reading/<name>_results.json and prints a table. report() appends the round to LEADS_REPORT.md and a
short entry to NOTES.md.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher4n as N4  # noqa: E402

M = N4.M
L6 = M.L6
K, J = L6.K, L6.K.J
I = J.I
H = I.H
G = H.G
F = G.F
X = F.X
T, B, D, Db, V, E = X.T, X.B, X.D, X.Db, X.V, X.E
ROOT = B.ROOT
rng = X.rng
grid = D.grid
LA, LB = X.LA, X.LB
KN_N, PY_N = T.KN_N, T.PY_N
RARE = X.RARE
REPS = 2000


def pv_hi(null, real):
    return (sum(n >= real for n in null) + 1) / (len(null) + 1)


def pv_lo(null, real):
    return (sum(n <= real for n in null) + 1) / (len(null) + 1)


def compare(a, b, f, lower=False, reps=REPS):
    """Label permutation between two lists of items; statistic f(a) - f(b)."""
    real = f(a) - f(b)
    pool, k, null = list(a) + list(b), len(a), []
    for _ in range(reps):
        rng.shuffle(pool)
        null.append(f(pool[:k]) - f(pool[k:]))
    return real, (pv_lo(null, real) if lower else pv_hi(null, real)), sum(null) / len(null)


def flag_compare(items, flag, value, reps=REPS, lower=False):
    """Items split by flag; compare the mean of value between flagged and unflagged, shuffling the flags."""
    fl = [flag(x) for x in items]
    vals = [value(x) for x in items]

    def stat(f_):
        a = [v for v, f in zip(vals, f_) if f]
        b = [v for v, f in zip(vals, f_) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real = stat(fl)
    null = []
    for _ in range(reps):
        rng.shuffle(fl)
        null.append(stat(fl))
    fl = [flag(x) for x in items]
    a = [v for v, f in zip(vals, fl) if f]
    b = [v for v, f in zip(vals, fl) if not f]
    return real, (pv_lo(null, real) if lower else pv_hi(null, real)), (round(sum(a) / max(1, len(a)), 4), len(a)), (round(sum(b) / max(1, len(b)), 4), len(b))


def chi2(pairs):
    return X.chi2(pairs)


def assoc(pairs, reps=REPS):
    """chi-square association of (a, b) pairs, shuffling b."""
    a = [x for x, _ in pairs]
    b = [y for _, y in pairs]
    real = chi2(pairs)
    null = []
    for _ in range(reps):
        rng.shuffle(b)
        null.append(chi2(list(zip(a, b))))
    return real, pv_hi(null, real), sum(null) / len(null)


def run(name, title, doc, tests):
    rows, details = [], {}
    for fn in tests:
        try:
            p, pred, prim, rob = fn()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            p, pred, prim, rob = None, fn.__doc__ or fn.__name__, {'error': str(ex)}, {}
        details[fn.__name__] = {'prediction': pred, 'primary': prim, 'robustness': rob, 'p': p}
        rows.append((fn.__name__, pred, p, prim))
        print(f"== {fn.__name__}: {pred}\n   primary {prim}\n   robustness {str(rob)[:700]}")
    tested = sorted([(p, k) for k, _, p, _ in rows if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = {k for _, k in tested[:cut]}
    res = {'title': title, 'method': doc.strip(), 'primary_p': {k: p for k, _, p, _ in rows}, 'bh_supported': sorted(supported), 'details': details}
    (ROOT / f'reading/{name}_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: (round(p, 4) if p is not None else None) for k, _, p, _ in rows})
    print('survive BH at 5%:', sorted(supported))
    return rows, supported


def fmt(prim):
    return ', '.join(f'{k} {v}' for k, v in prim.items() if k != 'p')[:160]


def report(round_no, name, title, intro, rows, supported, verdicts, adds, notes_lines):
    """verdicts: {test: verdict text}; adds: markdown paragraph(s); notes_lines: list of short lines for NOTES.md."""
    lines = [f'\n# {round_no} round: {title}, 24 September 2026\n',
             f'`reading/{name}.py`, results in `reading/{name}_results.json` and `reading/{name}_output.txt`.\n', intro + '\n',
             '| # | Hypothesis | primary p | BH 5% | verdict |', '|---|---|---|---|---|']
    for k, pred, p, prim in rows:
        pv = 'error' if p is None else f'{p:.4f}'.rstrip('0').rstrip('.')
        lines.append(f"| {k} | {pred} | {pv} ({fmt(prim)}) | {'yes' if k in supported else 'no'} | {verdicts.get(k, 'not supported')} |")
    lines.append('\n**What the round adds.**\n\n' + adds.strip() + '\n')
    rep = ROOT / 'LEADS_REPORT.md'
    rep.write_text(rep.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(lines), encoding='utf-8')
    notes = ROOT / 'NOTES.md'
    s = notes.read_text(encoding='utf-8')
    entry = f'\n## {round_no} round ({name}.py), 2026-09-24\n\n' + '\n'.join(f'- {x}' for x in notes_lines) + '\n'
    s = s.replace('\n## Remaining gaps\n', entry + '\n## Remaining gaps\n', 1)
    notes.write_text(s, encoding='utf-8')


def finish(round_no, label, name, title, intro, verdicts, adds, notes_lines, new_learnings):
    """Report a saturation-loop round and update reading/loop_ledger.json. Returns the consecutive-zero count."""
    d = json.loads((ROOT / f'reading/{name}_results.json').read_text(encoding='utf-8'))
    rows = [(k, v['prediction'], v['p'], v['primary']) for k, v in d['details'].items()]
    report(label, name, title, intro, rows, set(d['bh_supported']), verdicts, adds, notes_lines)
    path = ROOT / 'reading/loop_ledger.json'
    L = json.loads(path.read_text(encoding='utf-8'))
    prev = L['rounds'][-1]['consecutive_zero'] if L['rounds'] else 0
    zero = 0 if new_learnings else prev + 1
    L['rounds'].append({'round': round_no, 'tested': len(rows), 'bh_survivors': len(d['bh_supported']),
                        'new_learnings': new_learnings, 'consecutive_zero': zero})
    path.write_text(json.dumps(L, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return zero
