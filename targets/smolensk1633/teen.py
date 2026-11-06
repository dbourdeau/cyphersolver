"""Teen-number tokenisation test: a cross attached to 3,4,5,7,8 makes 1d; a free cross binds to the next digit."""
import collections, sys
ATT = set('34578')
def tok(w):
    w = w.replace(',', '').replace('?', '')
    out = []; i = 0
    while i < len(w):
        c = w[i]
        if c == '+':
            j = i + 1
            if j < len(w) and w[j].isdigit():
                # free cross + digit; skip an attached cross on that digit
                out.append('1' + w[j]); i = j + 1
                if i < len(w) and w[i] == '+' and w[j] in ATT: i += 1
                continue
            out.append('1'); i += 1; continue
        if c == '1' and i + 1 < len(w) and w[i+1].isdigit():
            out.append('1' + w[i+1]); i += 2; continue
        if c in ATT and i + 1 < len(w) and w[i+1] == '+':
            out.append('1' + c); i += 2; continue
        out.append(c); i += 1
    return out
if __name__ == '__main__':
    ws = [tok(w) for l in open(sys.argv[1], encoding='utf-8') if l.startswith('L') for w in l.split()[1:]]
    c = collections.Counter(t for w in ws for t in w)
    print(sum(c.values()), len(c), c.most_common())
    for w in ws[:40]: print('.'.join(w), end='  ')
