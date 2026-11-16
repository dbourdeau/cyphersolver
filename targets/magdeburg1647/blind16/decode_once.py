"""decode_once.py FOLDER : one mechanical decode of FOLDER/BLIND.tsv with the frozen magdeburg1647 key.
Key: FREEZE/key_upstream.tsv (upstream targets/magdeburg1647/key.tsv, commit 89e25ef), columns cipher -> plain.
Decoder logic = upstream scripts/decode.py dec_word(), unchanged: lower-case each cipher letter, look it up,
a letter not in the key -> '?' (hole).
Adapter for the blind-sheet notation (no token edited, only notation parsed):
  [a|b]              alternative reading: first option decoded, second noted as alt=...
  {S:name}           drawn symbol: looked up in the key's symbol/name rows; key.tsv has none -> '[S]' (hole)
  {mark:...}         diacritic/underline on the token: not a letter, dropped, noted
  {blot}             signs hidden by a blot: '[blot]' (hole, count unknown)
  {struck:...}       deleted: not decoded, counted
Note: key.tsv row m (plain x) is marked in the key as 'not in the frozen file (decodes ?)'; no m occurs in these texts.
"""
import sys, os, re, hashlib, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
KF = os.path.join(HERE, 'FREEZE', 'key_upstream.tsv')
KEY_SHA = 'c734821ef7ae8d062d63873fee0642e42db9fc4eebcd9a8d7355afb8e2aea2fe'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def load_key(kf):
    k = {}; sym = {}
    for l in open(kf, encoding='utf-8'):
        if l.startswith('#') or l.startswith('cipher\t') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        if len(f[0]) == 1: k[f[0]] = f[1]
        else: sym[f[0]] = f[1]
    return k, sym
# ---- upstream decode.py dec_word, unchanged ----
def dec_word(w, k): return ''.join(k.get(c, '?') for c in w.lower())
# ----
def main(folder):
    if sha(KF) != KEY_SHA: sys.exit('HASH MISMATCH key')
    bl = os.path.join(folder, 'BLIND.tsv')
    if sha(bl) != open(os.path.join(folder, 'FREEZE_blind.txt')).read().split()[0]: sys.exit('HASH MISMATCH BLIND.tsv')
    k, sym = load_key(KF)
    rows = [l.rstrip('\n').split('\t') for l in open(bl, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]
    out = ['image\tline\tclear_word_before\tcipher\tdecode\tnote']
    words = letters = val = hole = syms = blots = struck = alts = 0
    for img, ln, tok, cw in rows:
        notes = []
        if tok.startswith('{struck:'):
            struck += 1; out.append(f'{img}\t{ln}\t{cw}\t{tok}\t<struck>\tnot decoded'); continue
        m = re.fullmatch(r'\{S:([^}]*)\}', tok)
        if m:
            syms += 1; hole += 1; d = sym.get(m.group(1), '[S]')
            out.append(f'{img}\t{ln}\t{cw}\t{tok}\t{d}\tsymbol {m.group(1)}: no symbol row in key'); continue
        words += 1; dec = []; alt_dec = []; t = tok; i = 0
        while i < len(t):
            if t[i] == '{':
                j = t.index('}', i); inner = t[i+1:j]; i = j + 1
                if inner == 'blot': blots += 1; hole += 1; dec.append('[blot]'); alt_dec.append('[blot]')
                else: notes.append(inner)
                continue
            if t[i] == '[':
                j = t.index(']', i); a, b = t[i+1:j].split('|'); i = j + 1; alts += 1
                da = dec_word(a, k); dec.append(da); alt_dec.append(dec_word(b, k))
                notes.append(f'[{a}|{b}]={da}|{dec_word(b, k)}')
            else:
                c = t[i]; i += 1; dec.append(dec_word(c, k)); alt_dec.append(dec[-1])
                a = c
            letters += 1
            if dec[-1] == '?': hole += 1
            else: val += 1
        out.append(f'{img}\t{ln}\t{cw}\t{tok}\t{"".join(dec)}\t{"; ".join(notes)}')
    open(os.path.join(folder, 'decode_once.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    run = [f'time_utc: {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}',
           'run: once, decode_once.py (upstream decode.py dec_word unchanged), key = FREEZE/key_upstream.tsv (upstream 89e25ef)',
           f'BLIND.tsv sha256 {sha(bl)} (matches FREEZE_blind.txt)', f'key_upstream.tsv sha256 {sha(KF)} (matches FREEZE.txt)',
           f'decode_once.py sha256 {sha(os.path.abspath(__file__))}',
           f'cipher words {words}; cipher letters {letters}; letters valued {val}; holes {hole} '
           f'(= {letters - val} letter holes + {syms} symbols + {blots} blots); alternatives [a|b] {alts} (first option decoded); struck tokens {struck}']
    open(os.path.join(folder, 'DECODE_RUN.txt'), 'w').write('\n'.join(run) + '\n')
    print('\n'.join(run)); print('\n'.join(out[:4]))
if __name__ == '__main__': main(sys.argv[1])
