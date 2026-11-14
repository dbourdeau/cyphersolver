"""Shared helpers for the Kerlérec 1759 work: parse transcription files, normalise French, align code groups
with the clerk's interlinear plaintext."""
import re
import unicodedata


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]', '', s)


def parse(path):
    """Return list of pages: {'page','folio','lines':[{'n','gloss','codes':[tok..]}]}.
    tok = dict(code=int|None, top=int|None, kind='code'|'lost'|'num'|'clear', text=...)"""
    pages = []
    cur = None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        m = re.match(r'@page (\S+) (\S+)', line)
        if m:
            cur = {'page': m.group(1), 'folio': m.group(2), 'lines': {}}
            pages.append(cur)
            continue
        m = re.match(r'L(\d+)\s+(GLOSS|CODE):\s*(.*)$', line)
        if not m:
            continue
        n, kind, rest = int(m.group(1)), m.group(2), m.group(3)
        L = cur['lines'].setdefault(n, {'n': n, 'gloss': '', 'codes': []})
        if kind == 'GLOSS':
            L['gloss'] = rest
        else:
            for t in rest.split():
                if t == '??':
                    L['codes'].append({'kind': 'lost', 'code': None, 'top': None, 'raw': t})
                elif t.startswith('#num:'):
                    L['codes'].append({'kind': 'num', 'code': None, 'top': None, 'raw': t, 'text': t[5:]})
                elif t.startswith('#clear:'):
                    L['codes'].append({'kind': 'clear', 'code': None, 'top': None, 'raw': t, 'text': t[7:]})
                else:
                    unc = t.endswith('?')
                    t2 = t.rstrip('?')
                    if '/' in t2:
                        a, b = t2.split('/')
                        L['codes'].append({'kind': 'code', 'code': int(b), 'top': int(a), 'raw': t, 'unc': unc})
                    else:
                        L['codes'].append({'kind': 'code', 'code': int(t2), 'top': None, 'raw': t, 'unc': unc})
    for p in pages:
        p['lines'] = [p['lines'][k] for k in sorted(p['lines'])]
    return pages


def load_table(path):
    """code -> list of normalised candidate strings (tsv code<TAB>value[, value])"""
    t = {}
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('#'):
            continue
        c, v = l.rstrip('\n').split('\t')[:2]
        vals = []
        for x in re.split(r',\s*', v):
            # the OCR of Pusch's table prints accented letters as '?': expand to the likely base letters
            opts = ['']
            for ch in x:
                if ch == '?':
                    opts = [o + r for o in opts for r in 'eca']
                else:
                    opts = [o + ch for o in opts]
            vals += [norm(o) for o in opts]
        t[int(c)] = [x for x in vals if x] or ['']
    return t


def align(groups, text, table, free_cost=3.0, skip_cost=1.6, empty_cost=3.5, maxlen=12):
    """groups: list of token dicts (stream); text: normalised gloss stream.
    Returns list of (group_index, plaintext_slice or None, how) and the text chars skipped.
    how = 'match' (slice equals a table candidate), 'free' (unknown/lost group, slice assigned by context),
          'conflict' (known group took a slice different from the table), 'empty' (no plaintext)."""
    n, m = len(groups), len(text)
    INF = 1e18
    # dp[i][j] = min cost having consumed i groups and j chars
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    for i in range(n + 1):
        row = dp[i]
        for j in range(m + 1):
            c = row[j]
            if c >= INF:
                continue
            # skip a text char (plaintext the clerk wrote that has no group, e.g. a word added for sense)
            if j < m and c + skip_cost < dp[i][j + 1]:
                dp[i][j + 1] = c + skip_cost
                bk[i][j + 1] = ('skip', i, j)
            if i == n:
                continue
            g = groups[i]
            cands = []
            if g['kind'] == 'code' and g['code'] in table:
                for v in table[g['code']]:
                    if text.startswith(v, j):
                        cands.append((len(v), 0.0, 'match'))
                # conflict: known code, other slice
                for L in range(1, min(maxlen, m - j) + 1):
                    cands.append((L, free_cost + 2.0 + 0.15 * L, 'conflict'))
            elif g['kind'] == 'num':
                v = norm(g['text'])
                if text.startswith(v, j):
                    cands.append((len(v), 0.0, 'match'))
            elif g['kind'] == 'clear':
                v = norm(g['text'])
                if text.startswith(v, j):
                    cands.append((len(v), 0.0, 'match'))
                cands.append((0, 0.5, 'empty'))
            else:
                for L in range(1, min(maxlen, m - j) + 1):
                    cands.append((L, free_cost + 0.15 * L, 'free'))
            cands.append((0, empty_cost, 'empty'))
            for L, cost, how in cands:
                if c + cost < dp[i + 1][j + L]:
                    dp[i + 1][j + L] = c + cost
                    bk[i + 1][j + L] = (how, i, j)
    # backtrack from best end (allow trailing text skipped already via skip moves)
    i, j = n, m
    out = []
    skipped = []
    while (i, j) != (0, 0):
        how, pi, pj = bk[i][j]
        if how == 'skip':
            skipped.append(pj)
        else:
            out.append((pi, text[pj:j] if j > pj else None, how))
        i, j = pi, pj
    out.reverse()
    return out, sorted(skipped), dp[n][m]
