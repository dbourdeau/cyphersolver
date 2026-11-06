"""Apply key.tsv to transcription.txt and compare with reading.tsv.

python decipher.py            raw decipherment, line by line
python decipher.py --measure  per-word status from reading.tsv and the share of cipher signs read as sense
"""
import os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
SIGN = re.compile(r'(t0|\+0|10|[1-9][\^/]?|t|\+|D)')


def key():
    k = {}
    for l in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8').read().splitlines()[1:]:
        s, v = l.split('\t')[:2]
        k[s] = v.split(',')[0].strip() if s != 'D' else 'X.'
    return k


def lines():
    out = []
    for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        if not l.startswith('f'):
            continue
        ref, rest = l.split(' ', 1)
        rest = rest.split('[clear')[0]
        out.append((ref, rest.split()))
    return out


def signs(word):
    w = word.replace('?', '').replace('[..]', '').replace(':', '').strip('-,().')
    return [s for s in SIGN.findall(w)]


def raw(word, k):
    return ''.join(k.get(s, '?') for s in signs(word))


def main():
    k = key()
    if '--measure' not in sys.argv:
        for ref, ws in lines():
            print(ref, ' '.join(raw(w, k) for w in ws))
        return
    rd = {}
    for l in open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8').read().splitlines()[1:]:
        f = l.split('\t')
        rd[(f[0], int(f[1]))] = f
    tot = collections.Counter()
    for ref, ws in lines():
        for i, w in enumerate(ws, 1):
            n = len(signs(w))
            st = rd[(ref, i)][4] if (ref, i) in rd else 'missing'
            tot[st] += n
            tot['all'] += n
    print(dict(tot))
    print('signs read as sense: %d / %d = %.1f%%' % (tot['read'], tot['all'], 100 * tot['read'] / tot['all']))
    print('read or read with one doubtful sign: %.1f%%' % (100 * (tot['read'] + tot['doubt']) / tot['all']))


if __name__ == '__main__':
    main()
