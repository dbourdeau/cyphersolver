"""Decipher R8572 (BL Cotton Vesp. C IV ff.214-218, "el Gilino" to Francesco II Sforza, Paredes 15 Sept 1527)
with the key DECODE R5258 (ASMi Carteggio Sforzesco cart. 1591 no. 24, "Cum equite Bilie / extracta ex cifris").

One key dict, KEY[token] = (value, source); source is 'sheet' (read on the R5258 key sheet), 'context' (fixed by
the R8572 text only) or 'both' (on the sheet and confirmed by context). Value '' = null.
Transcription corrections are applied from transcription_corrections.txt (line id, old, new, reason).

  python decode_r8572.py            -> raw.txt (per MS line, undivided, with [unread] tokens)
  python decode_r8572.py --tsv      -> also key_r8572.tsv (token, value, source, count)
  python decode_r8572.py --measure  -> counts
Word division and doubtful marks are in reading_words.txt (hand-divided), merged by build_reading.py.
"""
import re, sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
TOK = os.path.join(HERE, '..', 'r8572_tokens.txt')

KEY = {}
def put(tok, val, src):
    KEY[tok.rstrip('?')] = (val, src)
def rng(base, start, sylls, src='both'):
    for i, s in enumerate(sylls.split()):
        put(f'{base}.{start+i}', s, src)

# ---- syllable rows (sheet, numbered in sequence; every row confirmed by the text) ----
rng('B', 31, 'ba be bi bo bu ca ce ci co cu da de di do du ga ge gi go gu')
rng('B', 51, 'fa fe fi fo fu')
rng('D', 51, 'la le li lo lu ma me mi mo mu na ne ni no nu')
rng('6', 56, 'pa pe pi po pu qua que qui quo quu ra re ri ro ru sa se si so su ta te ti to tu')
rng('o', 33, 'va ve vi vo vu xa xe xi xo xu za ze zi zo zu')
# ---- syllables and words outside the rows ----
put('A.42', 'al', 'sheet'); put('A.43', 'am', 'sheet'); put('A.44', 'an', 'sheet')
put('H.26', 'cosa', 'both'); put('H.27', 'che', 'both'); put('H.28', 'come', 'both')
put('R.28', 'ancora', 'both'); put('R.23', 'con', 'both'); put('D.40', 'i', 'both')   # letter column of the sheet (i: D.40); the word row's 'sara' does not fit: 'li scrive', 'restituirlo', 'diligentia'
put('6.2w', 'to', 'context')      # superscript loop-form; "questo", "obligato", "deliberato"
# ---- single letters ----
LET = {
 'a': [('ut','both'), ('th','both'), ('A.30','both'), ('iy','context')],
 'b': [('20','both'), ('lam','both'), ('A.31','both')],
 'c': [('oto','both'), ('A.32','both')],
 'd': [('A.33','sheet')],
 'e': [('+','both'), ('B.25','both'), ('SS','context')],
 'f': [('gf','both'), ('B.26','sheet')],
 'g': [('mp','both'), ('B.27','both')],
 'h': [('dots','both'), ('B.28','both')],
 'i': [('np','both'), ('pb','both')],
 'l': [('D.41','both'), ('bf','context')],
 'm': [('pi','both'), ('D.42','both')],
 'n': [('6','both'), ('36','both'), ('D.43','both')],
 'o': [('b+','both'), ('6.50','sheet')],
 'p': [('R','context'), ('6.51','sheet')],
 'r': [('S','both'), ('44','both'), ('6.53','sheet')],
 's': [('xo','both'), ('o.27','both')],
 't': [('m','both'), ('o.28','context')],
 'v': [('o.29','both'), ('xp','context')],
 'x': [('o.30','both')],
 'con': [('q','context')],
}
for v, lst in LET.items():
    for t, s in lst:
        put(t, v, s)
# ---- nulls (sheet row "Nulle" or behaviour) ----
for t, s in [('a++','sheet'), ('Hvv','context'), ('P.25','context'), ('vv','context'), ('x','sheet'), ('|','context')]:
    put(t, '', s)
# ---- nomenclator ----
put('B.55', '<Imperatore>', 'both')
put('B.56', '<Sua Maesta>', 'both')

# r8572 writes the D-base both as capital D and as a small round d; same values
def dcopy():
    for k in list(KEY):
        if k.startswith('D.') and 'd' + k[1:] not in KEY:
            KEY['d' + k[1:]] = KEY[k]
dcopy()

# extra entries added during the reading are appended by the EXTRA block below
EXTRA = os.path.join(HERE, 'key_extra.tsv')
if os.path.exists(EXTRA):
    for l in open(EXTRA, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        t, v, s = (l.rstrip('\n').split('\t') + ['', ''])[:3]
        put(t, '' if v == 'NULL' else v, s)
dcopy()


def load_lines():
    """Return [(line_id, [tokens or {clear}])] in MS order of the transcription file."""
    out = []; page = None
    corr = load_corrections()
    for l in open(TOK, encoding='utf-8'):
        m = re.match(r'## (P\d+)', l)
        if m: page = m.group(1); continue
        m = re.match(r'# (P\d+) lines? (\d+)', l)
        if m: lid = f'{m.group(1)}.{m.group(2)}'; continue
        if l.startswith('#') or not l.strip(): continue
        s = l.strip()
        if lid in corr:
            for old, new in corr[lid]:
                if old not in s:
                    print('WARN correction not found', lid, old, file=sys.stderr)
                s = s.replace(old, new, 1)
        s = re.sub(r'\bo t o\??', 'oto', s)
        out.append((lid, split_tokens(s)))
    return out

def split_tokens(s):
    toks = []
    for m in re.finditer(r'\{[^}]*\}|\[\[[^\]]*\]\]|\[del:[^\]]*\]|\[above:[^\]]*\]|\[del\]|\S+', s):
        toks.append(m.group(0))
    return toks

def load_corrections():
    p = os.path.join(HERE, 'transcription_corrections.txt'); c = collections.defaultdict(list)
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            if l.startswith('#') or not l.strip(): continue
            f = l.rstrip('\n').split('\t')
            if len(f) >= 3: c[f[0]].append((f[1], f[2]))
    return c

def norm_tok(t):
    return t.rstrip('?')

def decode_line(toks):
    s = ''
    for t in toks:
        if t.startswith('{'):
            s += ' ' + t + ' '; continue
        if t.startswith('[del'):           # writer's deletion: skipped
            continue
        if t.startswith('[above:'):        # writer's interlined replacement
            s += decode_line(t[7:-1].split()); continue
        u = norm_tok(t)
        if u in KEY: s += KEY[u][0]
        else: s += '[' + t + ']'
    return s

if __name__ == '__main__':
    L = load_lines()
    with open(os.path.join(HERE, 'raw.txt'), 'w', encoding='utf-8') as f:
        for lid, toks in L:
            f.write(f'{lid}\t{decode_line(toks)}\n')
    cnt = collections.Counter(); unk = collections.Counter()
    for lid, toks in L:
        for t in toks:
            if t.startswith('{') or t.startswith('[del') : continue
            if t.startswith('[above:'):
                for x in t[7:-1].split(): cnt[norm_tok(x)] += 1
                continue
            cnt[norm_tok(t)] += 1
            if norm_tok(t) not in KEY: unk[t] += 1
    if '--tsv' in sys.argv:
        with open(os.path.join(HERE, 'key_r8572.tsv'), 'w', encoding='utf-8') as f:
            NOTES = {}
            np_ = os.path.join(HERE, 'key_notes.tsv')
            if os.path.exists(np_):
                for l in open(np_, encoding='utf-8'):
                    a, b = l.rstrip('\n').split('\t', 1); NOTES[a] = b
            f.write('token\tvalue\tsource\tcount\tnote\n')
            for t, (v, s) in sorted(KEY.items(), key=lambda x: (-cnt[x[0]], x[0])):
                if cnt[t] == 0: continue
                f.write(f'{t}\t{v if v else "(null)"}\t{s}\t{cnt[t]}\t{NOTES.get(t, "")}\n')
    print('tokens', sum(cnt.values()), 'unread', sum(unk.values()))
    print(' '.join(f'{k}:{v}' for k, v in unk.most_common()))
