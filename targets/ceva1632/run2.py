"""Second pass (Oct 2026): decode each letter as ONE stream, not line by line.

Codes run across manuscript line ends (R75 l.28/29 '5|1' = f), so the
line-by-line pass of run.py produced spurious '?' noise digits there.  Uses
the re-transcribed digit files when present (r75.retrans.txt / r84.retrans.txt),
else the DECODE ones, and the extended NOMEN of cipher.py.
Writes r75.tokens2.json / r84.tokens2.json and r75.read2.txt / r84.read2.txt.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import decode as D, indomain, cipher

D.P_NOMEN_KNOWN, D.P_NOMEN_NEW, D.P_NULL = -1.5, -20.0, 0.0
for a in sys.argv:
    if a.startswith('--unvalued='): D.P_NOMEN_UNVALUED = float(a.split('=')[1])

def lines_of(tag):
    p = os.path.join(HERE, tag + '.retrans.txt')
    if not os.path.exists(p) or '--decode' in sys.argv:
        p = os.path.join(HERE, tag + '.digits')
    return [''.join(c for c in l if c.isdigit()) for l in open(p, encoding='utf-8') if any(c.isdigit() for c in l)], p

def main():
    model, n = indomain.build(w=0.6)
    nomen = D.load_nomen() | set(cipher.NOMEN)
    for tag in ('r75', 'r84'):
        lines, src = lines_of(tag)
        s = ''.join(lines)
        _, text, toks = D.decode(s, model, nomen, beam=600, w_lm=0.4)
        # re-split into manuscript lines by digit count, for display
        out, cur, k, bounds = [], [], 0, []
        acc = 0
        for l in lines:
            acc += len(l); bounds.append(acc)
        b = 0
        for t in toks:
            cur.append(t); k += len(t.lstrip('#?'))
            if b < len(bounds) and k >= bounds[b]:
                out.append(cur); cur = []; b += 1
        if cur: out.append(cur)
        json.dump(out, open(os.path.join(HERE, tag + '.tokens2.json'), 'w'), indent=0)
        def r(t):
            if t == '6': return ' '
            if t.startswith('#'):
                return cipher.NOMEN[t[1:]].upper() if t[1:] in cipher.NOMEN else '<%s>' % t[1:]
            if t.startswith('?'): return '{%s}' % t[1:]
            if t in cipher.NULLS: return ''
            return cipher.KEY[t]
        open(os.path.join(HERE, tag + '.read2.txt'), 'w', encoding='utf-8').write(
            '\n'.join(''.join(r(t) for t in l) for l in out) + '\n')
        sys.stderr.write('%s from %s\n' % (tag, os.path.basename(src)))

main()
