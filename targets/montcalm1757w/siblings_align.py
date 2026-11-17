"""Align the figures of the sibling code W letters with their period decipherment, using the 1757 attestation index.

Siblings (transcribed 12 Nov 2026, files in support/):
  W1756-11-03  Montcalm to d'Argenson, 3 Nov 1756, cipher postscript (C-12577 frame 0934)
  W1758-05-09  Montcalm to Belle-Isle, 9 May 1758, pieces 80 and 80bis (C-12578 frames 1022-1027)
  W1758-09-09  Montcalm to Belle-Isle, 9 Sep 1758, cipher end (C-12579 frame 0172)
  W1759-11-10  Levis to the Marine minister, 10 Nov 1759, page 307 only (C-10523 frame 0345)

The decipherment in these copies is written word by word, not split per group, so each letter is aligned as a whole:
dynamic programming over (group, position in the normalised clear text). A group in the 1757 index
(key/W_1757_attestations.tsv) costs nothing when the text matches one of its 1757 values and 1.2 per edit otherwise;
a group not in the index may take any 1-12 letter stretch at 0.8 + 0.1 per letter (or nothing at 1.5); skipping a
letter of the text costs 1.0. Digits marked ? or + in the transcription are kept but flagged.

Writes results/siblings_alignment.tsv (every group with the stretch aligned to it) and prints a summary.
The values for groups not in the 1757 index are read from the period decipherment; they are not a decipherment of ours.

Run from the repository root:  python targets/montcalm1757w/siblings_align.py
"""
import csv, json, pathlib, re, unicodedata
from functools import lru_cache

HERE = pathlib.Path(__file__).resolve().parent
SIBS = [('W1756-11-03', 'support/W1756-11-03_A1_3417_duplicata.txt'),
        ('W1758-05-09', 'support/W1758-05-09_A1_3498_p80-80bis.txt'),
        ('W1758-09-09', 'support/W1758-09-09_A1_3499_p65.txt'),
        ('W1759-11-10', 'support/W1759-11-10_Levis_F3_sample_p307.txt')]
MAXLEN = 12


def norm(s):
    s = s.replace('œ', 'oe').replace('&', 'et')
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s)


@lru_cache(maxsize=None)
def ed(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def load_index():
    idx = {}
    with open(HERE / 'key' / 'W_1757_attestations.tsv', encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            vals = []
            for part in row['values_counts'].split(';'):
                v = re.sub(r'\(\d+\)\s*$', '', part.strip())
                v = re.sub(r'\[[^\]]*\]', '', v).strip()
                if norm(v):
                    vals.append(norm(v))
            idx[int(row['group'])] = sorted(set(vals))
    return idx


def load_sibling(path):
    text, groups = [], []
    for ln in open(HERE / path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('C '):
            text.append(ln[2:].replace('|', ' '))
        elif ln.startswith('W '):
            text.append(ln[2:])
        elif ln.startswith('F '):
            for tok in ln[2:].split():
                m = re.fullmatch(r'(\d*)(\?)?(\d*)([?+]*)', tok)
                if not m or not (m.group(1) + m.group(3)):
                    continue
                flag = '?' if ('?' in tok) else ('+' if '+' in tok else '')
                digits = m.group(1) + m.group(3)
                # a group with an uncertain digit keeps its number only for the lookup when the ? is trailing
                # (whole group doubtful); with a ? in place of a digit it has no number
                num = int(digits) if (m.group(2) is None or not m.group(3)) and digits else None
                if m.group(2) and not m.group(3) and not tok.endswith('?'):
                    num = None
                groups.append((tok, num, flag))
    return norm(' '.join(text)), groups


def align(groups, ref, idx):
    n, m = len(groups), len(ref)
    INF = float('inf')

    def fn(g):
        tok, num, flag = g
        if num is not None and num in idx:
            vals = idx[num]
            return lambda s: min(1.2 * ed(v, s) for v in vals) if s else 1.2 * min(len(v) for v in vals)
        return lambda s: (0.8 + 0.1 * len(s)) if s else 1.5

    fns = [fn(g) for g in groups]
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for j in range(1, m + 1):
        D[0][j], B[0][j] = D[0][j - 1] + 1.0, ('skip',)
    for i in range(1, n + 1):
        f, Di, Dp, Bi = fns[i - 1], D[i], D[i - 1], B[i]
        for j in range(m + 1):
            best, bk = INF, None
            if j and Di[j - 1] + 1.0 < best:
                best, bk = Di[j - 1] + 1.0, ('skip',)
            for k in range(min(MAXLEN, j) + 1):
                c = Dp[j - k]
                if c >= best:
                    continue
                c += f(ref[j - k:j])
                if c < best:
                    best, bk = c, ('tok', k)
            Di[j], Bi[j] = best, bk
    out, i, j = [], n, m
    while i or j:
        b = B[i][j]
        if b[0] == 'skip':
            j -= 1
        else:
            out.append((groups[i - 1], j - b[1], j))
            i, j = i - 1, j - b[1]
    return out[::-1]


def one_pass(idx):
    out = {}
    for name, path in SIBS:
        ref, groups = load_sibling(path)
        out[name] = (ref, align(groups, ref, idx))
    return out


def accept_new(passes, idx):
    """New values: groups not in the 1757 index whose every occurrence aligns with the same stretch and which either
    occur twice or more, or occur once between two neighbours that agree with their 1757 values."""
    occ = {}
    for name, (ref, spans) in passes.items():
        for i, ((tok, num, flag), a, b) in enumerate(spans):
            if num is None or flag or num in idx:
                continue
            def ok(k):
                if not 0 <= k < len(spans):
                    return True
                (t2, n2, f2), a2, b2 = spans[k]
                return n2 is not None and not f2 and n2 in idx and ref[a2:b2] in idx[n2]
            occ.setdefault(num, []).append((name, i + 1, ref[a:b], ok(i - 1) and ok(i + 1)))
    acc = {}
    for num, os_ in occ.items():
        vals = {v for _, _, v, _ in os_}
        if len(vals) != 1 or not next(iter(vals)):
            continue
        if len(os_) >= 2 or os_[0][3]:
            acc[num] = (next(iter(vals)), os_)
    return acc


def main():
    base = load_index()
    idx = {k: list(v) for k, v in base.items()}
    accepted = {}
    for it in range(4):
        passes = one_pass(idx)
        acc = accept_new(passes, idx)
        if not acc:
            break
        for num, (v, os_) in acc.items():
            idx[num] = [v]
            accepted[num] = (v, os_, it + 1)
        print('pass', it + 1, 'accepted', len(acc))
    passes = one_pass(idx)
    rows, summary = [], {}
    for name, (ref, spans) in passes.items():
        s = {'groups': len(spans), 'in_1757_index': 0, 'agree_1757': 0, 'differ_1757': 0, 'new_value_accepted': 0,
             'new_unsettled': 0, 'uncertain_digit': 0}
        for pos, ((tok, num, flag), a, b) in enumerate(spans, 1):
            val = ref[a:b]
            if num is None or flag:
                kind = 'uncertain digit'; s['uncertain_digit'] += 1
            elif num in base:
                s['in_1757_index'] += 1
                if val in base[num]:
                    kind = 'agrees with 1757'; s['agree_1757'] += 1
                else:
                    kind = 'differs from 1757'; s['differ_1757'] += 1
            elif num in accepted:
                kind = 'new value (accepted)' if val == accepted[num][0] else 'new value (other occurrence differs)'
                s['new_value_accepted'] += 1
            else:
                kind = 'new, unsettled'; s['new_unsettled'] += 1
            ctx = ref[max(0, a - 10):a] + '[' + val + ']' + ref[b:b + 10]
            rows.append((name, pos, tok, '|'.join(base.get(num, [])) if num else '', val, kind, ctx))
        summary[name] = s
        print(name, s)
    with open(HERE / 'results' / 'siblings_alignment.tsv', 'w', encoding='utf-8') as f:
        f.write('# Sibling code W texts aligned with their period decipherment (siblings_align.py). value_1757 = the values\n'
                '# the 1757 index gives the group; aligned = normalised stretch of the period decipherment aligned with it.\n')
        f.write('letter\tposition\tgroup\tvalue_1757\taligned\tkind\tcontext\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(HERE / 'key' / 'W_sibling_values.tsv', 'w', encoding='utf-8') as f:
        f.write('# SEPARATE TABLE (14 Nov 2026): code W groups NOT in key/W_1757_attestations.tsv, with the value the period\n'
                '# decipherment of the sibling letters gives them (siblings_align.py). Accepted only when every occurrence aligns\n'
                '# with the same stretch and the group occurs twice or more, or once between two neighbours that agree with\n'
                '# their 1757 values. Read from the clerks\' decipherment (word by word in these copies), not deciphered by us.\n'
                '# occurrences = letter:position; pass = alignment pass in which it was accepted (later passes lean on earlier ones).\n')
        f.write('group\tvalue\tn\toccurrences\tpass\n')
        for num in sorted(accepted):
            v, os_, it = accepted[num]
            f.write('%d\t%s\t%d\t%s\t%d\n' % (num, v, len(os_), ' '.join('%s:%d' % (a, b) for a, b, _, _ in os_), it))
    (HERE / 'results' / 'siblings_summary.json').write_text(json.dumps(summary, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
