"""Measure the f. 130 reading: every token's reading letter is checked against the key.
read = letter allowed by the key (or null where the key says null); emended = reading differs from key; open = '?'."""
import decode, collections, sys
EQ = {'v': 'u', 'j': 'i', 'y': 'i', 'x': 's', 'z': 's'}
def eq(c): return EQ.get(c, c)
def tokens(path):
    return {n: s.split() for n, s in (l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('# ')) if not n.endswith('.clear')}
def readings(path):
    return {n: r.replace(' ', '') for n, r in (l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('# '))}
if __name__ == '__main__':
    T = tokens(sys.argv[1] if len(sys.argv) > 1 else '../f130_signs.txt'); R = readings(sys.argv[2] if len(sys.argv) > 2 else '../reading_f130.tsv')
    k = decode.key(sys.argv[3] if len(sys.argv) > 3 else '../key.tsv')
    tot = collections.Counter(); emend = []
    for n, S in T.items():
        r = R[n]; assert len(r) == len(S), (n, len(r), len(S))
        for i, (s, c) in enumerate(zip(S, r)):
            v = k.get(s, '?')
            allowed = {'-'} if v == '-' else {eq(x) for x in v.split('/')}
            if c == '?': tot['open'] += 1
            elif (c == '-' and v == '-') or eq(c) in allowed: tot['read'] += 1
            else: tot['emended'] += 1; emend.append(f'{n}#{i+1}: {s} key={v} read={c}')
    N = sum(tot.values())
    print(f"tokens {N}: read {tot['read']} ({tot['read']/N:.1%}), emended {tot['emended']}, open {tot['open']} ({tot['open']/N:.1%})")
    for e in emend: print('  emended', e)
