"""Round 5 part 6: the 29 doubtful positions of 14 April 1497 (catalogue 2857), majority over all six readers
(A, B round 1; C, D round 2; N1, N2 round 5 with sheet v2), in Lasry sign names; then strict/working recount with
round 2/3's rule (words_round3.py logic). Run once. usage: python3 -I recount1497_r5.py OUTDIR"""
import sys, re, json, difflib, collections
out = sys.argv[1]
R2 = 'output/juanmanuel1497_round2_2026-11-17'; V = 'output/juanmanuel1497_verify_2026-11-16'
KP = 'output/repo_items_2026-11-16/upstream_files/esp318no95/lasry2021/ctts/key.txt'
key = {}; names = {}
for ln in open(KP):
    if ln.startswith('#') or ' - ' not in ln: continue
    s, v = ln.rstrip('\n').split(' - ', 1); key[s] = v
    for i, n in enumerate(s.split('|'), 1): names[(v, i)] = n
M = json.load(open(f'{V}/my_map_from_key_image.json'))
def kname(t):
    lab = M.get(t)
    if lab is None: return '?'
    m = re.fullmatch(r'([A-Z])(\d)', lab)
    if m: return names.get((m.group(1), int(m.group(2))), '?')
    if lab == 'D_null': return None
    if lab in ('nine_dot', 'aunque'): return '?'
    return '§' + lab
W = {l.split('\t')[0]: l.split('\t')[2] for l in open('output/juanmanuel_round5_2026-11-17/hidden/sheet_mapping_v2.tsv') if l.startswith('W')}

def wname(t):
    n = W.get(t)
    if n is None: return '?'
    if n == 'NONE': return '?'
    if n == 'D': return None
    return n
def tokname(t, kind):
    if t in ('#', '?', '-', '/'): return None if t in ('-', '/') else '?'
    if t.startswith('{'): return '§' + t.strip('{}').lower()
    if t.startswith('?'): return '?'
    return kname(t) if kind == 'K' else wname(t)
def load_reader(path, kind):
    L = collections.OrderedDict()
    for ln in open(path, encoding='utf-8'):
        if ln.lstrip().startswith('#') or ln.lstrip().startswith('!'): continue
        m = re.match(r'\s*(L\d[ab]?)_w\d+\s*:(.*)', ln)
        if not m: continue
        v = re.sub(r'\?\([^)]*\)', '?', m.group(2))
        for t in v.split():
            n = tokname(t, kind)
            if n is not None: L.setdefault(m.group(1), []).append(n)
    return L
readers = {'A': load_reader(f'{V}/helper/transcription_A.txt', 'K'), 'B': load_reader(f'{V}/helper/transcription_B.txt', 'K'),
           'C': load_reader(f'{R2}/helper_inputs/C/transcription_C.txt', 'K'), 'D': load_reader(f'{R2}/helper_inputs/D/transcription_D.txt', 'K'),
           'N1': load_reader('output/juanmanuel_round5_2026-11-17/transcriptions/transcription_N1.txt', 'W'),
           'N2': load_reader('output/juanmanuel_round5_2026-11-17/transcriptions/transcription_N2.txt', 'W')}
strict = collections.OrderedDict()
for ln in open(f'{R2}/transcription_strict_round3_ids.txt'):
    L, v = ln.split(':', 1)
    strict[L.strip()] = [x for x in ((kname(t) if t != '#' else '#') for t in v.split()) if x is not None]
NOVAL = {'?', '#'}
log = open(f'{out}/recount1497_stretches.tsv', 'w')
log.write('line\tstrict_from\tstrict_to\t' + '\t'.join(readers) + '\tresult\thow\n')
new = {}; nst = nclosed_pos = nopen = 0
for L, s in strict.items():
    res = list(s); i = 0; repl = []
    while i < len(s):
        if s[i] != '#': i += 1; continue
        j = i
        while j < len(s) and s[j] == '#': j += 1
        reads = {}
        for R, txt in readers.items():
            r = txt.get(L, [])
            sm = difflib.SequenceMatcher(a=s, b=r, autojunk=False); mp = {}
            for o, a1, a2, b1, b2 in sm.get_opcodes():
                if o == 'equal':
                    for k in range(a2 - a1): mp[a1 + k] = b1 + k
            lo = mp.get(i - 1, -1) if i > 0 else -1
            hi = mp.get(j, len(r)) if j < len(s) else len(r)
            if (i > 0 and (i - 1) not in mp) or (j < len(s) and j not in mp): reads[R] = None
            else: reads[R] = tuple(r[lo + 1:hi])
        valid = [v for v in reads.values() if v is not None]
        cnt = collections.Counter(valid); best, nb = (cnt.most_common(1)[0] if cnt else ((), 0))
        how = 'open'; out_seq = None
        if nb >= 4 and not any(t in NOVAL for t in best): out_seq = list(best); how = f'{nb} of 6 identical'
        else:
            lens = collections.Counter(len(v) for v in valid)
            ln_, nl = lens.most_common(1)[0] if lens else (0, 0)
            if nl >= 4 and ln_ > 0:
                same = [v for v in valid if len(v) == ln_]; seq = []
                for k in range(ln_):
                    c = collections.Counter(v[k] for v in same if v[k] not in NOVAL).most_common(1)
                    seq.append(c[0][0] if c and c[0][1] >= 4 else '#')
                if any(t != '#' for t in seq): out_seq = seq; how = 'per position (>=4 of 6)'
        nst += 1
        if out_seq is None: out_seq = ['#'] * (j - i); nopen += j - i
        else: nclosed_pos += sum(t != '#' for t in out_seq); nopen += sum(t == '#' for t in out_seq)
        repl.append((i, j, out_seq))
        log.write(f'{L}\t{i + 1}\t{j}\t' + '\t'.join('(unaligned)' if reads[R] is None else (' '.join(reads[R]) or '(none)') for R in readers) + f'\t{" ".join(out_seq) or "(none)"}\t{how}\n')
        i = j
    for i, j, seq in reversed(repl): res[i:j] = seq
    new[L] = res
print(f'stretches {nst}; positions closed {nclosed_pos}; still open {nopen}')
with open(f'{out}/strict_round5_names.txt', 'w') as f:
    for L, v in new.items(): f.write(f'{L}: ' + ' '.join(v) + '\n')
# recount, words_round3.py logic, on the package's words.tsv (working signs in Lasry names)
def letter(n):
    for s_, v in key.items():
        if n in s_.split('|'): return v.lower() if len(v) == 1 else '[' + v + ']'
    return '?'
order = ['L1','L2','L3','L4','L5','L6','L7','L8b','L8a']
S = [x for L in order for x in new.get(L, [])]
S3 = [x for L in order for x in strict.get(L, [])]
rows = [l.rstrip('\n').split('\t') for l in open('output/push_2026-11-17/wt-juanmanuel1497/targets/juanmanuel1497/words.tsv') if l[0].isdigit()]
r3 = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open(f'{R2}/words_round3.tsv') if l[0].isdigit()}
def score(strictseq):
    work = []; span = []
    for r in rows:
        t = r[3].split(); a = len(work); work += t; span.append((a, len(work)))
    sm = difflib.SequenceMatcher(a=work, b=strictseq, autojunk=False); amap = {}
    for o, i1, i2, j1, j2 in sm.get_opcodes():
        for k in range(i2 - i1):
            amap[i1 + k] = strictseq[j1 + k] if (o == 'equal' or (o == 'replace' and i2 - i1 == j2 - j1)) else '#'
    res = []
    for r, (a, b) in zip(rows, span):
        s_ = [amap.get(k, '#') for k in range(a, b)]
        dec = ''.join('?' if t in ('#', '?') else (letter(t) if not t.startswith('§') else '?') for t in s_)
        wdec = ''.join('?' if t.startswith('[') or t == '#' else (letter(t) if not t.startswith('§') else '?') for t in r[3].split())
        res.append((r, dec, r[5] == 'yes' and '?' not in dec and dec == wdec))
    return res
old = score(S3); now = score(S)
print(f'strict read, round-3 text through this script: {sum(x[2] for x in old)} of {len(rows)}; round 5: {sum(x[2] for x in now)} of {len(rows)}')
with open(f'{out}/words1497_round5.tsv', 'w') as f:
    f.write('n\tline\tword (working)\tstrict round-3 decode\tread strict r3\tstrict round-5 decode\tread strict r5\tread working\n')
    for (r, d3, k3), (_, d5, k5) in zip(old, now):
        f.write(f'{r[0]}\t{r[1]}\t{r[2]}\t{d3}\t{"yes" if k3 else "no"}\t{d5}\t{"yes" if k5 else "no"}\t{r[5]}\n')
