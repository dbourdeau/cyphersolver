"""Collate the two readings of m0271 (transcription/m0271.txt, first reader; transcription/m0271_r2.txt, blind
second reader) token by token, line by line (difflib alignment on the number tokens; word gaps ignored).

    python3 -I scripts/collate_m0271.py       (run from beling/; writes results/collation_m0271.txt)

Each disagreement gets an id (Lnn.k), the position in each reading (1-based token index), the two readings, and
the decrypt of each side under key.txt for orientation (the decrypt is not used to settle anything here; settling
is done on the image and recorded in results/collation_m0271_settled.md).
"""
import difflib
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location('t1', os.path.join(HERE, 'scripts', 'test_m0271.py'))
t1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t1)


def raw_tokens(path):
    """{tag: [token strings, '*' kept]}"""
    out = {}
    import re
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            if raw.startswith('@'):
                tag, body = raw.rstrip('\n').split(' ', 1)
                out[tag] = [t.strip() for t in re.split(r'[.|]', body) if t.strip()]
    return out


def main():
    key = t1.load_key(os.path.join(HERE, 'key', 'key.txt'))
    a = raw_tokens(os.path.join(HERE, 'transcription', 'm0271.txt'))
    b = raw_tokens(os.path.join(HERE, 'transcription', 'm0271_r2.txt'))

    def dec(toks):
        s = []
        for t in toks:
            n = t.rstrip('*')
            s.append(key.get(int(n), '#') if n.isdigit() and int(n) < 60 else '[%s]' % n)
        return ''.join(s)

    out = ['# m0271 collation: A = first reading (m0271.txt), B = blind second reading (m0271_r2.txt)',
           '# id  A-pos  B-pos  A-tokens  ->  B-tokens   (decrypt A / decrypt B)']
    n_tok_a = n_tok_b = n_same = n_diff = 0
    for tag in sorted(set(a) | set(b)):
        ta, tb = a.get(tag, []), b.get(tag, [])
        na = [t.rstrip('*') for t in ta]
        nb = [t.rstrip('*') for t in tb]
        n_tok_a += len(ta)
        n_tok_b += len(tb)
        sm = difflib.SequenceMatcher(None, na, nb, autojunk=False)
        k = 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                n_same += i2 - i1
                continue
            k += 1
            n_diff += 1
            out.append('%s.%d  A%d-%d  B%d-%d  %s  ->  %s   (%s / %s)' % (
                tag[1:], k, i1 + 1, i2, j1 + 1, j2, '.'.join(ta[i1:i2]) or '-', '.'.join(tb[j1:j2]) or '-',
                dec(ta[max(0, i1 - 3):i2 + 3]), dec(tb[max(0, j1 - 3):j2 + 3])))
    summary = ('A tokens %d, B tokens %d, tokens identical and aligned %d (%.3f of A), disagreements %d'
               % (n_tok_a, n_tok_b, n_same, n_same / n_tok_a, n_diff))
    out.insert(2, '# ' + summary)
    with open(os.path.join(HERE, 'results', 'collation_m0271.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    print(summary)


if __name__ == '__main__':
    sys.exit(main())
