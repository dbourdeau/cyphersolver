"""Second round (PLAN2.md): keep only the groups two blind readings agree on, write codes_1810_round2.txt.

python build_round2.py            -> codes_1810_round2.txt, reader_agreement.txt, no29_agreed.txt

Witness texts are taken unchanged from ../codes_1810.txt. Reading files: ../transcriptions_round2/ (X, Y, Z) and the
round-1 blind second readings in ../transcriptions/. A disagreeing or unreadable group becomes the hole token 0.
Python standard library only.
"""
import difflib, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(HERE)
T2 = os.path.join(B, 'transcriptions_round2')
T1 = os.path.join(B, 'transcriptions')

def tok(t):
    """raw token -> ('num', {values}, marks) | ('word', w) | ('hole', n) | None"""
    t = t.strip().rstrip('.,;')
    if not t or t in ('~', '-', '|', '--', '—'):
        return None
    m = re.fullmatch(r'\[unreadable run, about (\d+) numbers\]', t)
    if m:
        return ('hole', int(m.group(1)))
    if 'illegible' in t or 'clipped' in t or 'blotted' in t or '_' in re.sub(r'_[+vu^]', '', t) and re.search(r'\d_\d', t):
        return ('hole', 1)
    m = re.fullmatch(r'\[(\d+)/(\d+)\](.*)', t) or re.fullmatch(r'\[(\d+)/(\d+\^?)\](.*)', t)
    vals = None
    if m:
        vals = {int(m.group(1)), int(re.sub(r'\D', '', m.group(2)))}; rest = m.group(3)
    else:
        m = re.fullmatch(r'(\d*)\[(\d)/(\d)\](\d*)(.*)', t)           # 157[4/6]
        if m:
            vals = {int(m.group(1) + m.group(2) + m.group(4)), int(m.group(1) + m.group(3) + m.group(4))}; rest = m.group(5)
        else:
            m = re.fullmatch(r'(\d+)(.*)', t)
            if m:
                vals = {int(m.group(1))}; rest = m.group(2)
    if vals is not None:
        mk = ('^' if ('^' in rest or '°' in rest) else '') + ('+' if '_+' in rest else '')
        return ('num', vals, mk)
    w = re.sub(r'[^a-z]', '', t.lower())
    return ('word', w) if w else None

def read_file(path, nolabel=False):
    """-> list of (label, [tokens]) passages"""
    out = []; cur = None
    for line in open(path, encoding='utf8'):
        s = line.rstrip('\n')
        if s.startswith('=='):
            if 'remarks' in s.lower():
                cur = None; continue
            cur = (s[2:].strip(), []); out.append(cur); continue
        if cur is None:
            continue
        m = re.match(r'^\s*(\d{2})(?::|\s)\s*(.*)$', s)
        if not m:
            continue
        body = re.sub(r'\(.*?\)|\{.*?\}', ' ', m.group(2))
        body = re.sub(r'\s{3,}.*$', '', body) if re.search(r'\s{3,}\(', m.group(2)) else body
        body = body.replace('[unreadable run, about ', '[unreadable_run_about_').replace(' numbers]', '_numbers]')
        for raw in body.split():
            raw = raw.replace('[unreadable_run_about_', '[unreadable run, about ').replace('_numbers]', ' numbers]')
            x = tok(raw)
            if x is None:
                continue
            if x[0] == 'hole':
                cur[1].extend([('hole', 1)] * x[1])
            else:
                cur[1].append(x)
    return out

def pick(passages, *keys):
    """concatenate passages whose label starts with each key, in the order given"""
    toks = []
    for k in keys:
        if isinstance(k, list):           # literal tokens
            toks += k; continue
        hit = [p for p in passages if p[0].startswith(k)]
        assert len(hit) == 1, (k, [p[0][:30] for p in passages])
        toks += hit[0][1]
    return toks

def key(x):
    return ('n', min(x[1])) if x[0] == 'num' else ('w', x[1]) if x[0] == 'word' else ('h', id(x))

def agree(a, b):
    """-> agreed token strings, n_agreed_numbers, n_numbers_a, n_numbers_b"""
    ka = [('n', sorted(x[1])[0]) if x[0] == 'num' else ('w', x[1]) if x[0] == 'word' else ('h', i) for i, x in enumerate(a)]
    kb = [('n', sorted(x[1])[0]) if x[0] == 'num' else ('w', x[1]) if x[0] == 'word' else ('h', -i - 1) for i, x in enumerate(b)]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
    out = []; nag = 0
    def emit(x, y):
        nonlocal nag
        if x[0] == 'num' and y[0] == 'num' and x[1] & y[1]:
            v = min(x[1] & y[1]); out.append(f'{v}{x[2]}'); nag += 1
        elif x[0] == 'word' and y[0] == 'word' and x[1] == y[1]:
            out.append(x[1])
        else:
            out.append('0')
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
            for x, y in zip(a[i1:i2], b[j1:j2]):
                emit(x, y)
        else:
            n = max(i2 - i1, j2 - j1)
            out += ['0'] * sum(1 for x in (a[i1:i2] if i2 - i1 >= j2 - j1 else b[j1:j2]) if x[0] != 'word')
    na = sum(1 for x in a if x[0] in ('num', 'hole')); nb = sum(1 for x in b if x[0] in ('num', 'hole'))
    return out, nag, na, nb

# witness blocks of round 1, unchanged
wit = []
cur = None
for line in open(os.path.join(B, 'codes_1810.txt'), encoding='utf8'):
    if line.startswith('@'):
        cur = {'ref': line[1:].strip(), 'plain': ''}; wit.append(cur)
    elif line.startswith('=') and cur:
        cur['plain'] += line[1:].strip()

X23, Y23 = read_file(os.path.join(T2, 'X_no23.txt')), read_file(os.path.join(T2, 'Y_no23.txt'))
X25, Y25 = read_file(os.path.join(T2, 'X_no25.txt')), read_file(os.path.join(T2, 'Y_no25.txt'))
X27, Y27 = read_file(os.path.join(T2, 'X_no27_28.txt')), read_file(os.path.join(T2, 'Y_no27_28.txt'))
S24, Z24 = read_file(os.path.join(T1, 'no24_second.txt')), read_file(os.path.join(T2, 'Z_no24.txt'))
S29, Z29 = read_file(os.path.join(T1, 'no29_second.txt')), read_file(os.path.join(T2, 'Z_no29.txt'))
said = [('word', w) for w in 'i said i believed this opinion correct'.split()]

pairs = {
 'No. 23, 5 Sep 1810, passage A': (pick(X23, '143L'), pick(Y23, '143L')),
 'No. 23, 5 Sep 1810, passage B': (pick(X23, '145R'), pick(Y23, '145R')),
 'No. 23, 5 Sep 1810, passage C': (pick(X23, '145L passage 1'), pick(Y23, '145L passage 1')),
 'No. 23, 5 Sep 1810, passage D': (pick(X23, '145L passage 2', '143R'), pick(Y23, '145L passage 2', '143R')),
 'No. 23, 5 Sep 1810, passage E': (pick(X23, '144L passage 1'), pick(Y23, '144L passage 1')),
 'No. 23, 5 Sep 1810, passage F': (pick(X23, '144L passage 2', '150S passage 1'), pick(Y23, '144L passage 2', '150S passage 1')),
 'No. 23, 5 Sep 1810, passage G': (pick(X23, '150S passage 2'), pick(Y23, '150S passage 2')),
 'No. 24, 20 Sep 1810, passage A': (pick(S24, '154L passage 1', '154R passage 1'), pick(Z24, '154L passage 1')),
 'No. 24, 20 Sep 1810, passage B': (pick(S24, '154R passage 2'), pick(Z24, '154R passage 2')),
 'No. 24, 20 Sep 1810, passage C': (pick(S24, '155S passage 1'), pick(Z24, '155S passage 3')),
 'No. 25, 30 Sep 1810, passage A': (pick(X25, '167R passage 1'), pick(Y25, '167R passage A')),
 'No. 25, 30 Sep 1810, passage B': (pick(X25, '167R passage 2'), pick(Y25, '167R passage B')),
 'No. 25, 30 Sep 1810, passage C': (pick(X25, '168L passage 1'), pick(Y25, '168L passage C')),
 'No. 25, 30 Sep 1810, passage D': (pick(X25, '168L passage 2'), pick(Y25, '168L passage D')),
 'No. 25, 30 Sep 1810, passage E': (pick(X25, '168L passage 3', '168R passage 1'), pick(Y25, '168L passage E', '168R passage E')),
 'No. 25, 30 Sep 1810, passage F': (pick(X25, '168R passage 2'), pick(Y25, '168R passage F')),
 'No. 25, 30 Sep 1810, passage G': (pick(X25, '168R passage 3'), pick(Y25, '168R passage G')),
 'No. 27, 12 Oct 1810, passage A': (pick(X27, '176R'), pick(Y27, '176R')),
 'No. 27, 12 Oct 1810, passage B': (pick(X27, '177 passage 1') + said + pick(X27, '177 passage 2'), pick(Y27, '177 passage 1') + said + pick(Y27, '177 passage 2')),
 'No. 28, 10/22 Oct 1810, passage A': (pick(X27, '182'), pick(Y27, '182')),
 'No. 28, 10/22 Oct 1810, passage B': (pick(X27, '183'), pick(Y27, '183')),
}

lines = ['# Second round (PLAN2.md): groups two blind readings agree on; 0 = a group they do not agree on or could not read.',
         '# Witness texts unchanged from ../codes_1810.txt. Built by build_round2.py. Format of ../codes_ford.txt (align.py).']
rep = ['passage\tnumbers_reading1\tnumbers_reading2\tagreed\tagreed/longer']
per = {}
for w in wit:
    ref = w['ref']
    if ref.startswith('No. 21'):
        toks = None
        for l in open(os.path.join(B, 'codes_1810.txt'), encoding='utf8'):
            pass
        # No. 21: the two readings agree 33 of 33 (../transcriptions/compare_no21.txt): the round-1 text stands
        blk = open(os.path.join(B, 'codes_1810.txt'), encoding='utf8').read().split('@ ' + ref + '\n', 1)[1].split('\n@', 1)[0]
        body = [l for l in blk.split('\n')[1:] if l.strip() and not l.startswith('#')]
        agreed = ' '.join(body).split(); nag = na = nb = 33
    else:
        k = [p for p in pairs if ref.startswith(p)]
        assert len(k) == 1, ref
        agreed, nag, na, nb = agree(*pairs[k[0]])
    ref2 = re.sub(r'\(.*\)$', '', ref).strip() + ' (round 2: agreed blind readings)'
    lines += [f'@ {ref2}', f'= {w["plain"]}'] + [' '.join(agreed[i:i + 18]) for i in range(0, len(agreed), 18)]
    rep.append(f'{ref.split(" (")[0]}\t{na}\t{nb}\t{nag}\t{nag / max(na, nb):.3f}')
    d = ref.split(',')[0]
    a = per.setdefault(d, [0, 0, 0]); a[0] += na; a[1] += nb; a[2] += nag
open(os.path.join(HERE, 'codes_1810_round2.txt'), 'w', encoding='utf8').write('\n'.join(lines) + '\n')
rep += ['', 'despatch\tnumbers_reading1\tnumbers_reading2\tagreed\tagreed/longer']
for d, (na, nb, ag) in per.items():
    rep.append(f'{d}\t{na}\t{nb}\t{ag}\t{ag / max(na, nb):.3f}')

# No. 29: agreed groups only
s29, z29 = S29, Z29
def flat(ps):
    t = []
    for _, x in ps:
        t += x
    return t
ag29, nag29, na29, nb29 = agree(flat(S29), flat(Z29))
rep += ['', f'No. 29 (no witness)\t{na29}\t{nb29}\t{nag29}\t{nag29 / max(na29, nb29):.3f}']
open(os.path.join(HERE, 'no29_agreed.txt'), 'w', encoding='utf8').write(
    '# No. 29: the groups the two blind readings (../transcriptions/no29_second.txt, ../transcriptions_round2/Z_no29.txt) agree on, in order; 0 = not agreed. build_round2.py\n'
    + '\n'.join(' '.join(ag29[i:i + 18]) for i in range(0, len(ag29), 18)) + '\n')
open(os.path.join(HERE, 'reader_agreement.txt'), 'w', encoding='utf8').write('\n'.join(rep) + '\n')
print('\n'.join(rep))
