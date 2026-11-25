"""Align the two blind helpers' transcriptions line by line and keep only the positions where both agree.

Usage: python3 align.py <helperA.txt> <helperB.txt> <hidden_mapping.json> <out_agreed.json> <out_table.tsv>

Helper file format, one line per drawn line (parts joined in order):
    L2_f6r_l07: S12 S03 / S44 ? [dal] S09 ...
Tokens: a sheet id (S01..), '?' (unreadable), '[letters]' (a group written in ordinary letters), 'X:desc' (a sign not on
the sheet), '{clear}' (ordinary handwriting), '/' (word gap, ignored here).
A position counts as agreed only when both helpers give the same token and it is a sheet id or a [letters] group with
no '?' inside. Everything else is a hole '#'. Needleman-Wunsch: match +2, mismatch -1, gap -1.
"""
import sys, json, re


def parse(path):
    out = {}
    for line in open(path, encoding='utf8'):
        line = line.strip()
        if not line or line.startswith('#') or ':' not in line.split()[0]:
            continue
        key, rest = line.split(':', 1)
        key = re.sub(r'_[ab]$', '', key.strip())  # parts a and b of a line are joined in file order
        toks = [t for t in rest.split() if t != '/' and t != '{clear}']
        out.setdefault(key, []).extend(toks)
    return out


def nw(a, b):
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i
    for j in range(1, m + 1): S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i-1][j-1] + (2 if a[i-1] == b[j-1] else -1), S[i-1][j] - 1, S[i][j-1] - 1)
    i, j, al = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i][j] == S[i-1][j-1] + (2 if a[i-1] == b[j-1] else -1):
            al.append((a[i-1], b[j-1])); i -= 1; j -= 1
        elif i > 0 and S[i][j] == S[i-1][j] - 1:
            al.append((a[i-1], None)); i -= 1
        else:
            al.append((None, b[j-1])); j -= 1
    return al[::-1]


def good(t):
    return t is not None and (re.fullmatch(r'S\d\d', t) is not None or (t.startswith('[') and '?' not in t))


if __name__ == '__main__':
    A, B = parse(sys.argv[1]), parse(sys.argv[2])
    mp = json.load(open(sys.argv[3]))['id_to_lasry']
    agreed = {'letter2': [], 'letter1': []}
    rows = ['line\tcolumns\tagreed\tA_tokens\tB_tokens']
    lines_out = {}
    tot_c = tot_a = 0
    for key in sorted(set(A) | set(B)):
        al = nw(A.get(key, []), B.get(key, []))
        seq = []
        for x, y in al:
            if x == y and good(x):
                seq.append(x if x.startswith('[') else mp[x])
            else:
                seq.append('#')
        nag = sum(1 for t in seq if t != '#')
        rows.append(f'{key}\t{len(al)}\t{nag}\t{len(A.get(key, []))}\t{len(B.get(key, []))}')
        tot_c += len(al); tot_a += nag
        agreed['letter2' if key.startswith('L2') else 'letter1'].append(seq)
        lines_out[key] = {'alignment': al, 'agreed_lasry': seq}
    rows.append(f'TOTAL\t{tot_c}\t{tot_a}\t\t')
    json.dump(agreed, open(sys.argv[4], 'w'), ensure_ascii=False)
    json.dump(lines_out, open(sys.argv[4].replace('.json', '_lines.json'), 'w'), ensure_ascii=False)
    open(sys.argv[5], 'w').write('\n'.join(rows) + '\n')
    print('\n'.join(rows))
