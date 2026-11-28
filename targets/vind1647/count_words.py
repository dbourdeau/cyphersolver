"""Strict counts for vind1647 (standard library only). Every cipher word of transcription.txt (words broken at line end
joined), its decryption with key.tsv, and its status from the reading (reading.md): read, or a hole. A word whose
reading needs any changed or supplied letter is a hole, and so is a word whose sign was re-read after the solve on the sense
alone. Also the reciprocity of the key: how many signs X with
value Y have sign Y with value X, against 100,000 random one-to-one keys over the same signs (seed 20261126).
usage: python3 -I targets/vind1647/count_words.py"""
import random
from pathlib import Path
HERE = Path(__file__).resolve().parent
HOLE = {37: 'hmlu -> dikt: third sign doubtful (l or z); "dict" (= dit, your)? not settled',
        61: 'nqpghp -> grende: "trende" (three) wanted; the first sign is clearly n (= g)',
        65: 'fzh -> ocd: "och" wanted; d and h are a cipher pair, so a slip h for d',
        68: 'Wuxootpd -> staffueh: "staffued" (stavet) wanted; the same d/h slip',
        74: 'mgofqh -> inford: "indført"? not settled',
        22: 'papqzpq -> exercer: "exercere" wants a supplied final e',
        73: 'yfnWuxeotpq -> bogstapfuer: "bogstaffuer" wants f for the e-like sign (cipher e = p) that both readers saw',
        2: 'yqfhpq -> broder: the second sign was re-read y -> q after the solve, on the sense alone (frozen reader y, blind reader g or q)',
        72: 'xkkp -> alle: the second sign was re-read d -> k after the solve, on the sense alone (frozen reader d or k, blind reader h, k or d)'}
DOUBT = {45: 'thm (udi): first sign t in the first transcription, l in the blind one (then "kdi", a hole); counted read'}

def key():
    k = {}
    for line in open(HERE / 'key.tsv', encoding='utf-8'):
        if line.startswith('sign') or not line.strip(): continue
        s, p = line.rstrip('\n').split('\t')[:2]; k[s] = p
    return k

def words():
    out = []; carry = None
    for line in open(HERE / 'transcription.txt', encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        num, rest = line.split('#')[0].split(None, 1)
        ws = rest.split()
        for i, w in enumerate(ws):
            if carry is not None: w = carry + w; carry = None
            if w.endswith('=') and i == len(ws) - 1: carry = w[:-1]; continue
            out.append((num, w))
    return out

def main():
    k = key(); ws = words(); read = 0
    print('n\tline\tcipher\tdecryption\tstatus\tnote')
    for i, (ln, w) in enumerate(ws, 1):
        st = 'hole' if i in HOLE else 'read'
        read += st == 'read'
        print('%d\t%s\t%s\t%s\t%s\t%s' % (i, ln, w, ''.join(k[c] for c in w), st, HOLE.get(i, DOUBT.get(i, ''))))
    n = len(ws)
    print('# cipher words %d; read %d; holes %d; read share %d/%d = %.1f%%' % (n, read, len(HOLE), read, n, 100.0 * read / n))
    # Signs a, c, e and r occur once each and were given their values BY the pairing, so they are left out:
    # only signs whose value and whose partner's value were both read from the text count.
    signs = [s for s in k if len(s) == 1 and s.islower() and s != 'w' and s not in 'acer']
    test = [s for s in signs if k[s] in signs]
    rec = sum(1 for s in test if k[k[s]] == s)
    rng = random.Random(20261126); vals = [k[s] for s in signs]; mx = 0; ge = 0
    for _ in range(100000):
        rng.shuffle(vals); k2 = dict(zip(signs, vals))
        r = sum(1 for s in signs if k2[s] in k2 and k2[k2[s]] == s); mx = max(mx, r); ge += r >= rec
    print('# reciprocal signs %d of %d testable (signs a, c, e, r left out: fixed by the pairing; y has no partner sign in the text); '
          'random one-to-one keys over the same %d signs: max %d, at or above %d of 100000' % (rec, len(test), len(signs), mx, ge))

if __name__ == '__main__':
    main()
