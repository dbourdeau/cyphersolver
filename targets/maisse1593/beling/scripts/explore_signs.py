"""Exploratory, after the one test run (not part of the test): which signs decode against the copy and which do not.
Aligns each letter's decryption to its copy (same alignment as test_key.py), attributes each decrypted character to the
sign it came from, and for each sign counts matched characters and, where a one-to-one replacement occurs, the copy
letter it lines up with. Run from beling/: python3 -I scripts/explore_signs.py"""
import collections, difflib, importlib.util
spec = importlib.util.spec_from_file_location('t', 'scripts/test_key.py'); t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
key = t.load_key()
stat = collections.defaultdict(lambda: [0, 0, collections.Counter()])
for L, files in t.CIPHER.items():
    toks = []
    for f in files:
        for page, n, line, tk, note in t.load_lines(f):
            if t.is_test(page, n, line, note):
                toks.extend(tk)
    rows = [r for r in (t.HERE / t.COPY[L]).read_text(encoding='utf-8').splitlines() if not r.startswith('#')]
    T = t.norm(' '.join(rows))
    d, owner = [], []
    for x in toks:
        s = t.token_sign(x); v = key.get(s) if s is not None else None
        out = '?' if v is None else t.norm(v) if v else ''
        for ch in out:
            d.append(ch); owner.append(s if s is not None else '[?]')
    d = ''.join(d).replace('?', '\x00')
    sm = difflib.SequenceMatcher(None, d, T, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        for k in range(i1, i2):
            st = stat[owner[k]]; st[1] += 1
            if tag == 'equal': st[0] += 1
            elif tag == 'replace' and i2 - i1 == j2 - j1: st[2][T[j1 + k - i1]] += 1
print('sign\tvalue\tchars\tmatched\tshare\tcopy letters where replaced')
for s, (m, n, c) in sorted(stat.items(), key=lambda kv: kv[1][0] / kv[1][1]):
    if n >= 4 and m / n < 0.8:
        print(f'{s}\t{key.get(s, "-")}\t{n}\t{m}\t{m/n:.2f}\t{dict(c.most_common(4))}')
