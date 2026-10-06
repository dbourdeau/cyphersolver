"""Show every context of a nomenclator code across Lasry's four letters (gold.json) and R75/R84."""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cipher
def render(t):
    if t == '6': return ' '
    if t.startswith('#'): t = t[1:]
    if t in cipher.NOMEN: return cipher.NOMEN[t].upper()
    if len(t) == 3: return '<%s>' % t
    if t.startswith('?') or t in cipher.NULLS: return ''
    return cipher.KEY.get(t, '!')
def streams():
    for name, pairs in json.load(open(os.path.join(HERE, 'gold.json'))):
        yield name, [p[0] for p in pairs]
    for f in ('r75', 'r84'):
        yield f, [t for l in json.load(open(os.path.join(HERE, f + '.tokens.json'))) for t in l]
if __name__ == '__main__':
    for code in sys.argv[1:]:
        print('==', code)
        for name, toks in streams():
            for i, t in enumerate(toks):
                if t.lstrip('#') == code:
                    a = ''.join(render(x) for x in toks[max(0, i-14):i])
                    b = ''.join(render(x) for x in toks[i+1:i+15])
                    print('  %-26s %30s [%s] %s' % (name[-12:], a[-30:], code, b[:30]))
