"""ONE decode of the held-out leaves with the frozen key (KEY.tsv, see FREEZE_KEY.txt). No emendation, no re-run with
changes. Unknown tokens print as '?'. Writes DECODE.txt and work/decode_counts.txt."""
import sys, os, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from common import read_tx, split_sign

D = '/home/claude/keyless/round40c/basel_anv9/'
frozen = open(D + 'FREEZE_KEY.txt').read()
h = hashlib.sha256(open(D + 'KEY.tsv', 'rb').read()).hexdigest()
assert h in frozen, 'KEY.tsv does not match FREEZE_KEY.txt'

key, rules = {}, {}
for ln in open(D + 'KEY.tsv'):
    p = ln.rstrip('\n').split('\t')
    if ln.startswith('token'):
        continue
    if p[0] == '#RULE':
        rules[p[1]] = p[2]
        continue
    key[p[0]] = '' if p[1] == '-' else p[1]
R_D2 = rules.get('D2', '').startswith('nearest')
R_DBL = rules.get('+"', '').startswith('repeat')
VOW = 'aeiou'


def decode_word(signs):
    toks = []
    for s in signs:
        if s in ('Eq', 'Fill'):
            continue
        toks += split_sign(s)
    out, prev, unk = '', '', 0
    for t in toks:
        if t == 'D2' and R_D2:
            v = [c for c in out if c in VOW]
            s = v[-1] if v else key.get('D2', '?')
        elif t == '+"' and R_DBL:
            s = prev
        elif t in key:
            s = key[t]
        else:
            s = '?'; unk += 1
        out += s
        prev = s
    return out, len(toks), unk


FILES = [('H1', 'tx/f015r.txt'), ('H2', 'tx/f159r.txt'), ('H3', 'tx/f034r_p34.txt')]
lines_out, counts = [], []
for hid, f in FILES:
    ntok = nunk = nlet = 0
    lines_out.append('## %s %s' % (hid, f))
    for lid, words in read_tx(D + f):
        dec = []
        for w in words:
            d, n, u = decode_word(w)
            ntok += n; nunk += u; nlet += sum(1 for c in d if c.isalpha())
            if w and w[-1] == 'Eq':
                d += '='
            dec.append(d)
        lines_out.append('%s %s\t%s' % (hid, lid, ' '.join(dec)))
    counts.append('%s %s: tokens %d, tokens with no key value %d, decoded letters %d' % (hid, f, ntok, nunk, nlet))
open(D + 'DECODE.txt', 'w').write('# ONE decode with frozen KEY.tsv (sha256 %s). "=" marks a word broken at a line end.\n' % h
                                  + '\n'.join(lines_out) + '\n')
open(D + 'work/decode_counts.txt', 'w').write('\n'.join(counts) + '\n')
print('\n'.join(lines_out))
print('\n'.join(counts))
