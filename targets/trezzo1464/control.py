"""Control for align.py: encipher a clear text in a synthetic syllabic code and measure what the aligner recovers.

usage: python3 control.py <clear.txt> <noise> <seed> <out_cipher.txt>

The clear is cut into units: a consonant followed by a vowel becomes one unit (probability 0.6), otherwise a single
letter. Each distinct unit gets one sign (s0, s1, ...), most frequent first; units beyond the 70th share the sign of a
random earlier unit, so the code has about 70 signs as the real transcription does. Then a share `noise` of the
tokens is replaced by a random sign, to imitate misread signs. Writes the cipher in the c283.txt line format.
"""
import random, re, sys, collections

sys.path.insert(0, '.')
import align  # noqa: E402

VOW = set('aeiou')


def main():
    s = align.load_clear(sys.argv[1])
    noise, seed = float(sys.argv[2]), int(sys.argv[3])
    rnd = random.Random(seed)
    units, i = [], 0
    while i < len(s):
        if i + 1 < len(s) and s[i] not in VOW and s[i + 1] in VOW and rnd.random() < 0.6:
            units.append(s[i:i + 2]); i += 2
        else:
            units.append(s[i]); i += 1
    freq = collections.Counter(units)
    sign = {}
    for n, (u, _) in enumerate(freq.most_common()):
        sign[u] = 's%d' % n if n < 70 else sign[rnd.choice(list(sign))]
    toks = [sign[u] for u in units]
    toks = [('s%d' % rnd.randrange(70)) if rnd.random() < noise else t for t in toks]
    with open(sys.argv[4], 'w') as f:
        for k in range(0, len(toks), 30):
            f.write('C.%02d %s\n' % (k // 30 + 1, ' '.join(toks[k:k + 30])))
    print('units', len(units), 'signs', len(set(toks)), 'letters/token', round(len(s) / len(toks), 2))


if __name__ == '__main__':
    main()
