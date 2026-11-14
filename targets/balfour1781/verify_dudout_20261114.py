"""balfour1781: independent decoder (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Reads only the key constants of the key file decode.py (RING, TABLES['C'], read as literals with ast, the
script is not run or imported) and the transcription pages transcription/p7xx.txt (L lines; N lines only for
the decipherer's "should be 13" on p. 718). Own rules, written from NOTES.md / Saberton:
 - A, B: dash groups run across line ends, except next to a 5-number indicator group at a line edge; numbers >= 30 are fillers; a group of fillers holding exactly one
   number < 30 (at least two fillers) is an indicator: that number is the new 'a'. The setting carries from
   one sheet to the next (No. 1 -> No. 2 -> No. 3). A group of one lone number is a numeral in clear.
 - C: one fixed table, numbers >= 40 are fillers.
No language model. Output compared letter by letter (letters only) with decryption_A/B/C.txt, then with the
interlinear (I lines) as a second check.
Run: python3 verify_dudout_20261114.py <path to targets/balfour1781>
"""
import ast, re, sys, os, difflib, glob
T = sys.argv[1] if len(sys.argv) > 1 else '.'
src = open(os.path.join(T, 'decode.py'), encoding='utf-8').read()
def const(name):
    m = re.search(r'^' + name + r'\s*=\s*', src, re.M); i = m.end()
    # take the literal up to its balanced end
    depth = 0
    for j in range(i, len(src)):
        c = src[j]
        if c in '[{(': depth += 1
        elif c in ']})':
            depth -= 1
            if depth == 0: return ast.literal_eval(src[i:j + 1])
RING = const('RING'); TABLE_C = const('TABLES')['C']
A = 'abcdefghiklmnopqrstuvwxyz'; POS = {n: i for i, n in enumerate(RING)}
def ring_letter(n, a): return A[(POS[n] - POS[a]) % 25]

def page(p):
    L, I, N = {}, {}, {}
    for l in open(os.path.join(T, 'transcription', f'p{p}.txt'), encoding='utf-8'):
        m = re.match(r'([LINC])(\d+)\s*\|\s?(.*)', l.rstrip('\n'))
        if m: {'L': L, 'I': I, 'N': N}.get(m.group(1), {})[int(m.group(2))] = m.group(3)
    return L, I, N

def num(t):
    if t == '?': return None, True
    if t.endswith('x'): return 99, False          # fillers cut at the page edge
    return int(t.rstrip('?')), t.endswith('?')

def is_ind(ns):
    """fillers (>= 30) holding exactly one real number; at least two fillers; at most one illegible."""
    real = [n for n in ns if n is not None and n < 30]; fill = [n for n in ns if n is not None and n >= 30]
    return len(real) == 1 and len(fill) >= 2 and ns.count(None) <= 1

def decode_ring(pages, a=None):
    stream = []
    for p in pages:
        L, I, N = page(p)
        for li in sorted(L):
            toks = L[li].split()
            # NOTES.md: indicator groups split at line ends -> a line end next to a full indicator group
            # (5 numbers or more: shorter edge groups are word ends padded with fillers) is a break
            head = toks[:toks.index('-')] if '-' in toks else toks
            tail = toks[len(toks) - toks[::-1].index('-'):] if '-' in toks else []
            if len(head) >= 5 and is_ind([num(t)[0] for t in head]) and stream and stream[-1][2] != '-': stream.append((p, li, '-'))
            for t in toks: stream.append((p, li, t))
            if len(tail) >= 5 and is_ind([num(t)[0] for t in tail]): stream.append((p, li, '-'))
    groups, cur = [], []
    for p, li, t in stream:
        if t == '-':
            if cur: groups.append(cur); cur = []
        else: cur.append((p, li, t))
    if cur: groups.append(cur)
    out = {}; inds = []
    for g in groups:
        ns = [num(t)[0] for _, _, t in g]
        real = [n for n in ns if n is not None and n < 30]
        fill = [n for n in ns if n is not None and n >= 30]
        if is_ind(ns):
            a = real[0]
            p, li = g[0][0], g[0][1]
            Np = page(p)[2]
            for k in (li, li + 1):
                if 'should be 13' in Np.get(k, '') and a == 25: a = 13
            inds.append((p, li, a)); continue
        if len(g) == 1 and ns[0] is not None and (ns[0] >= 30 or ns[0] not in POS or a is None or ring_letter(ns[0], a) != "a"):
            out.setdefault((g[0][0], g[0][1]), []).append('#'); continue
        for p, li, t in g:
            n, _ = num(t)
            if n is None: ch = '?'
            elif n >= 30: continue
            elif a is None or n not in POS: ch = '?'
            else: ch = ring_letter(n, a)
            out.setdefault((p, li), []).append(ch)
    return out, inds, a

def decode_table(pages):
    out = {}
    for p in pages:
        L, _, _ = page(p)
        for li in sorted(L):
            for t in L[li].split():
                if t == '-': continue
                n, _ = num(t)
                if n is not None and n >= 40: continue
                out.setdefault((p, li), []).append('?' if n is None else TABLE_C.get(n, '?'))
    return out

def theirs(doc):
    d = {}
    for l in open(os.path.join(T, f'decryption_{doc}.txt'), encoding='utf-8'):
        m = re.match(r'p(\d+) L(\d+)\s+(.*)', l.rstrip('\n'))
        if m:
            s = re.sub(r'<\d+>', '#', m.group(3)); s = re.sub(r'\[\d+\]', '?', s)
            d[(m.group(1), int(m.group(2)))] = re.sub(r'[^a-z?#]', '', s.replace('?', '') if False else s)
    return d

def compare(doc, mine):
    th = theirs(doc); agree = tot = 0; diffs = []
    for k in sorted(set(mine) | set(th)):
        a = re.sub(r'[^a-z]', '', ''.join(mine.get(k, []))); b = re.sub(r'[^a-z]', '', th.get(k, ''))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        agree += sum(x.size for x in sm.get_matching_blocks()); tot += max(len(a), len(b))
        if a != b: diffs.append((k, a, b))
    return agree, tot, diffs

docs = {'A': [str(p) for p in range(717, 726)], 'B': [str(p) for p in range(729, 733)], 'C': [str(p) for p in range(733, 737)]}
a = None
for doc, pages in docs.items():
    if doc == 'A':
        mine, inds, a = decode_ring(pages)
    elif doc == 'B':
        mine, inds, _ = decode_ring(pages)
    else:
        mine, inds = decode_table(pages), []
    ag, tot, diffs = compare(doc, mine)
    print(f'{doc}: {ag}/{tot} letters agree with decryption_{doc}.txt ({100 * ag / tot:.2f}%); indicators {len(inds)}: '
          + ' '.join(str(x[2]) for x in inds))
    for k, x, y in diffs: print(f'   p{k[0]} L{k[1]:02d}  mine {x}\n             pub. {y}')
