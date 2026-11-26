"""decode_once.py : one mechanical decode of kling72/BLIND.tsv with the frozen klingenberg1675 key.
Copied from /home/claude/siblings/klingenberg1675/decode_once.py (16 Nov 2026; used for 41R, 134R, 253R). Changes, and
nothing else: (1) KEY = ./key_frozen (byte copies from upstream main 8b75e65ac, same sha256 as the 16 Nov freeze);
(2) the blind sheet now uses neutral labels S01..S31: each S-label token is first translated to its key sign name
through ./sheet_to_key.tsv (sha256 checked against FREEZE.txt), keeping its ~ and " flags; numbers are untouched;
(3) main() takes no argument: folder = this script's folder. Decoder logic (upstream count.py SIGN/dec1, unchanged):
number -> table_M3, else words_v4, else '[n]' hole; letter sign -> SIGN, else '?' hole.
Adapter for the blind-sheet notation (as before):
  [struck] / [struck: ...]      deleted text: not decoded, counted separately
  [insert: X]                   token X written above the line: decoded in place
  [insert-mark above: ...], [edge], [gloss]   marks: not tokens
  [margin: ...]                 margin run: its tokens decoded in order
  {...}                         drawn sign description: kept as {..}, not a token
  X~                            doubt flag, stripped; counted
  token containing '?' (other than a trailing doubt flag): unread character(s) -> hole '[?raw]'
Refuses to run if decode_once.txt exists (first pass is the figure of record).
"""
import sys, os, re, json, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, 'key_frozen')
MAP = os.path.join(HERE, 'sheet_to_key.tsv')
LAB = {}
for _l in open(MAP, encoding='utf-8'):
    _f = _l.rstrip('\n').split('\t')
    if len(_f) == 2 and not _l.startswith('#') and _f[0] != 'label': LAB[_f[0]] = _f[1]
def relabel(raw):
    t = raw; tail = ''
    while t and t[-1] in '~"': tail = t[-1] + tail; t = t[:-1]
    return (LAB[t] + tail) if t in LAB else raw
# ---- upstream count.py, unchanged ----
SIGN = {"E":"e","y":"n","A":"r","F":"h","Q":"h","D":"u","G":"i","B":"i","X":"o","K":"s","L":"t","Z":"t","#":"c",
        "I":"l","x":"m","O":"a","o":"a","w":"d","H":"g","C":"f","V":"f","PP":"q","⊐":"k","T":"z","J":"k","P":"p","-":"b","U":"k","⊥":"z"}
def load(path): return {k: v for k, v in json.load(open(path, encoding='utf-8')).items() if not k.startswith('_')}
def dec1(k, t, table, words):
    if k == 'N': return table[t] if t in table else (words[t] if t in words else '[' + t + ']')
    return SIGN.get(t, '?')
# ---- end upstream ----
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
EXPECT = {'key.tsv': '160c5c5faf58956b14bc5aab23f2883d524082fb3ae04e8c09669d73d23d9b05',
          'maps_words_v4.json': '9ac253c22179babd427969909008cae61265f57c07210c66ad1d423591cf5784',
          'maps_table_M3.json': '7f2112e36372248c2ba4d30089f1906881d112a57de98aacb211891ed72542e2'}

def parse(s):
    """split a tokens cell into items: ('T', raw) token, ('S', raw) struck, ('C', raw) sign/mark."""
    out = []; i = 0
    while i < len(s):
        c = s[i]
        if c.isspace(): i += 1; continue
        if c == '[':
            d = 0; j = i
            while True:
                if s[j] == '[': d += 1
                elif s[j] == ']':
                    d -= 1
                    if d == 0: break
                j += 1
            inner = s[i+1:j]; i = j + 1
            if inner.startswith('struck'): out.append(('S', inner))
            elif inner.startswith('insert:'): out += parse(inner[len('insert:'):])
            elif inner.startswith('margin:'): out += parse(inner[len('margin:'):])
            else: out.append(('C', '[' + inner + ']'))
            continue
        if c == '{':
            j = s.index('}', i); out.append(('C', s[i:j+1])); i = j + 1
            if i < len(s) and s[i] == '~': i += 1
            continue
        j = i
        while j < len(s) and not s[j].isspace() and s[j] not in '[{': j += 1
        out.append(('T', s[i:j])); i = j
    return out

def main(folder=HERE):
    if os.path.exists(os.path.join(folder, 'decode_once.txt')): sys.exit('decode_once.txt exists: runs once')
    fz = open(os.path.join(folder, 'FREEZE.txt'), encoding='utf-8').read()
    if sha(MAP) not in fz: sys.exit('HASH MISMATCH sheet_to_key.tsv')
    for f, h in EXPECT.items():
        if sha(os.path.join(KEY, f)) != h: sys.exit(f'HASH MISMATCH {f}')
    bl = os.path.join(folder, 'BLIND.tsv')
    want = open(os.path.join(folder, 'FREEZE_blind.txt')).read().split()[0]
    if sha(bl) != want: sys.exit('HASH MISMATCH BLIND.tsv')
    table = load(os.path.join(KEY, 'maps_table_M3.json')); words = load(os.path.join(KEY, 'maps_words_v4.json'))
    rows = [l.rstrip('\n').split('\t') for l in open(bl, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]
    out = ['image\tline\tclear_word_before\tdecode']; n = val = hole = struck = doubt = 0
    for img, ln, toks, cw in rows:
        parts = []
        for kind, raw in parse(toks):
            if kind == 'S': struck += 1; parts.append('<struck>'); continue
            if kind == 'C': parts.append(raw); continue
            n += 1; raw = relabel(raw); t = raw
            if t.endswith('~'): doubt += 1; t = t[:-1]
            core = t.replace('"', '')
            if '?' in core:
                d = '[?' + raw + ']'
            else:
                k = 'N' if core.isdigit() else 'L'
                d = dec1(k, core, table, words)
            if d == '?' or d.startswith('['): hole += 1; d = d if d.startswith('[') else '<?' + raw + '>'
            else: val += 1
            parts.append(d)
        out.append(f'{img}\t{ln}\t{cw}\t' + ' '.join(parts))
    open(os.path.join(folder, 'decode_once.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    run = [f'time_utc: {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}',
           'run: once, decode_once.py (upstream count.py dec1/SIGN unchanged), key = key_frozen (upstream 8b75e65ac, = 89e25ef bytes), labels via sheet_to_key.tsv',
           f'BLIND.tsv sha256 {sha(bl)} (matches FREEZE_blind.txt)'] + \
          [f'{f} sha256 {sha(os.path.join(KEY, f))} (matches FREEZE.txt)' for f in EXPECT] + \
          [f'decode_once.py sha256 {sha(os.path.abspath(__file__))}',
           f'tokens {n}; valued {val}; hole {hole} (= {val}+{hole}); doubt-flagged (~) tokens {doubt}; struck groups not decoded {struck}']
    open(os.path.join(folder, 'DECODE_RUN.txt'), 'w').write('\n'.join(run) + '\n')
    print('\n'.join(run)); print('\n'.join(out[:4]))
if __name__ == '__main__': main()
