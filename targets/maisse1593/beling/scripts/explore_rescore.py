"""Exploratory, after the one test run (not part of the test, no pass/fail): the test score with single key changes
suggested by explore_signs.py, and with unknown sign names left out of the denominator. Run from beling/."""
import importlib.util
spec = importlib.util.spec_from_file_location('t', 'scripts/test_key.py'); t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
key = t.load_key()
def run(k, drop_unknown=False):
    m = n = 0
    for L, files in t.CIPHER.items():
        toks = [x for f in files for (p, ln, line, tk, note) in t.load_lines(f) if t.is_test(p, ln, line, note) for x in tk]
        rows = [r for r in (t.HERE / t.COPY[L]).read_text(encoding='utf-8').splitlines() if not r.startswith('#')]
        T = t.norm(' '.join(rows)); d = t.decode(toks, k)
        if drop_unknown: d = d.replace('?', '')
        m += t.matched(d.replace('?', '\x00'), T); n += len(d)
    return round(m / n, 4)
print('frozen key                         ', run(key))
print('frozen key, unknown signs left out ', run(key, True))
k2 = dict(key, pi='o'); print('pi = o                             ', run(k2))
print('pi = o, unknown signs left out     ', run(k2, True))
