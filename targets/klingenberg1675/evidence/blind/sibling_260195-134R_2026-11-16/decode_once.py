"""decode_once.py FOLDER : one mechanical decode of FOLDER/BLIND.tsv with the frozen klingenberg1675 key.
Decoder logic = upstream targets/klingenberg1675/scripts/count.py (commit 89e25ef), copied unchanged:
SIGN table, dec1() (number -> table_M3, else words_v4, else '[n]' hole; letter sign -> SIGN, else '?' hole),
token normalisation (strip '"' and '?').
Adapter for the blind-sheet notation (no token edited, only notation parsed):
  [struck] / [struck: ...]      deleted text: not decoded, counted separately
  [insert: X]                   token X written above the line: decoded in place
  [insert-mark above: ...], [edge]   marks: not tokens
  [margin: ...]                 margin run: its tokens decoded in order
  {...}                         drawn sign description: kept as {..}, not a token (upstream treats {} as non-cipher)
  X~                            '~' = blind reader's doubt flag, stripped like upstream '?' doubt flag; counted
  token containing '?' other than a trailing doubt flag on a full figure (e.g. ?24, 3??, 41? at [edge], lone ?):
                                unread character(s) in the blind sheet -> hole '[?raw]'
"""
import sys, os, re, json, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, '_key_frozen')
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

def main(folder):
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
            n += 1; t = raw
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
           'run: once, decode_once.py (upstream count.py dec1/SIGN unchanged), key = _key_frozen (upstream 89e25ef)',
           f'BLIND.tsv sha256 {sha(bl)} (matches FREEZE_blind.txt)'] + \
          [f'{f} sha256 {sha(os.path.join(KEY, f))} (matches FREEZE.txt)' for f in EXPECT] + \
          [f'decode_once.py sha256 {sha(os.path.abspath(__file__))}',
           f'tokens {n}; valued {val}; hole {hole} (= {val}+{hole}); doubt-flagged (~) tokens {doubt}; struck groups not decoded {struck}']
    open(os.path.join(folder, 'DECODE_RUN.txt'), 'w').write('\n'.join(run) + '\n')
    print('\n'.join(run)); print('\n'.join(out[:4]))
if __name__ == '__main__': main(sys.argv[1])
