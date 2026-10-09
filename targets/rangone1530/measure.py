"""Measure how many cipher signs read as sense (rangone1530).

Each passage is given as a word-segmented reading aligned sign by sign with the key decrypt:
  ?      an unread sign (key value '?')
  {x}    a sign read as x against its key value (writer's slip, or a once-only sign set by the word)
  .      the null
A word counts as sense only if it has no '?' and occurs in the it-cinquecento corpora (>= MINC times)
or is listed in OK with a reason. Signs in any other word count as unread.
Run: python measure.py
"""
import json, os, re, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

MINC = 3
NOT = {'f'}  # corpus abbreviations that are not words here
OK = {  # word -> reason, for sense words missing from (or rare in) the corpus
 'esendo': 'essendo, writer drops double consonants (clear text: acaduto, satisfato)',
 'oferte': 'offerte, single consonant as above',
 'atenderui': 'attendervi, single consonant as above',
 'rouiare': 'rovi(n)are, the n is not enciphered (missing sign, sense forced by e hara ... da)',
 'olse': '(v)olse after piu: the u of piu is not repeated; one sign serves both words',
}

PASSAGES = {
 'A1-A5a': (['A1', 'A2', 'A3', 'A4', 'A5a'],
   "l fa instantia ?e de uen{i}re al serui cio loro ? le mie malissimo satisfato di lui ha mandato a dirlo "
   "al {s}ignore cesare {e} farli grande oferte"),
 'A5b-A6': (['A5b', 'A6'], "esendo seguito la ?icon puorano atenderui"),
 'B1': (['B1'], "il fre.goso"),
 'B2-B5': (['B2', 'B3', 'B4', 'B5'],
   "tolse fare la cosa de ?en mai piu olse r{u}i{n}a le cose ben disposte in casa e hara il f da rouiare "
   "e ho una pratica di lei mi dispiacera"),
}

def lines():
    key = json.load(open(os.path.join(HERE, 'key.json')))
    out = {}
    for l in open(os.path.join(HERE, 'cipher.txt'), encoding='utf8'):
        if l[:1] in 'AB' and l[1].isdigit():
            k, v = l.split(':', 1)
            parts = v.split('|')
            if len(parts) == 2:
                out[k + 'a'], out[k + 'b'] = parts[0].split(), parts[1].split()
            else:
                out[k] = v.split()
    return key, out

def lexicon():
    root = os.path.join(HERE, '..', '..', 'lang', 'corpora')
    c = Counter()
    for f in ('it-renaissance.txt', 'it-nunziature.txt'):
        c.update(lm.norm(open(os.path.join(root, f), encoding='utf8').read(), 'early', spaces=True).split())
    return c

def main():
    key, L = lines()
    lex = lexicon()
    tot_all = read_all = 0
    per_letter = Counter(); per_letter_read = Counter()
    for name, (ls, spec) in PASSAGES.items():
        toks = [t for l in ls for t in L[l]]
        dec = ''.join(key[t] for t in toks)
        words = spec.split()
        # align
        pos = 0; unread = []; slips = []
        for w in words:
            plain = re.sub(r'\{(.)\}', r'\1', w)
            units = re.findall(r'\{.\}|.', w)
            n = len(units)
            seg = dec[pos:pos + n]
            for u, d in zip(units, seg):
                if u.startswith('{'):
                    slips.append((w, d, u[1]))
                elif u != d:
                    raise SystemExit('%s: spec %r does not match decrypt %r at %d' % (name, w, seg, pos))
            pos += n
            word = plain.replace('.', '')
            ok = '?' not in word and (lex[word] >= MINC or word in OK) and word not in NOT
            if not ok:
                unread.append((w, n, lex[word] if '?' not in word else 0))
        assert pos == len(dec), (name, pos, len(dec))
        u = sum(n for _, n, _ in unread)
        letter = name[0]
        per_letter[letter] += len(dec); per_letter_read[letter] += len(dec) - u
        tot_all += len(dec); read_all += len(dec) - u
        print('%-7s %3d signs, %3d unread  %s' % (name, len(dec), u,
              ' '.join('%s(%d,lex=%d)' % x for x in unread)))
        if slips:
            print('        set against key: ' + ', '.join('%s %s->%s' % s for s in slips))
    for k in sorted(per_letter):
        print('letter %s: %d/%d = %.1f%%' % (k, per_letter_read[k], per_letter[k], 100 * per_letter_read[k] / per_letter[k]))
    print('overall: %d/%d = %.1f%% of signs read as sense' % (read_all, tot_all, 100 * read_all / tot_all))

if __name__ == '__main__':
    main()
