"""Adapter for docs/_replay.py: key_v4.json applied to ct_233/239/288.txt, against the French of reading.md.

The decode rule is decode.py's (letters; syllable blocks of five from 54, fourteen rows; names), with one addition
stated here and in NOTES.md: the q row is read qua que qui quo qu (decode.py prints qa qe qi qo qu). Word-signs whose
value in the key is a guess in [ ] or unknown in { } count as open codes. Only the cipher is compared: the cipher
runs of a leaf, in order, against the bold passages of its section of reading.md, in order. The clear text is left out
(reading.md abridges it). The cipher runs on without word division, so words are counted over the reading.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key_v4.json', 'transcription': 'ct_233.txt, ct_239.txt, ct_288.txt', 'reading': 'reading.md (French sections, bold passages)'}
POLYPHONY = {}
BLOCK0, NBLK, VOW = 54, 14, 'aeiou'
LEAVES = (('f233', 'ct_233.txt', '## f. 233'), ('f239', 'ct_239.txt', '## f. 239'), ('f288v', 'ct_288.txt', '## f. 288v'))


def mechanical():
    key = json.load(open(os.path.join(HERE, 'key_v4.json'), encoding='utf8'))
    L = {int(k): v for k, v in key['letters'].items()}
    B = {int(k): v for k, v in key['blocks'].items()}
    N = key.get('names', {})

    def dec(t):
        if t.isdigit():
            n = int(t)
            if n in L:
                v = L[n]
                return None if v.startswith('{') else v
            if BLOCK0 <= n < BLOCK0 + 5 * NBLK:
                c = B.get(BLOCK0 + 5 * ((n - BLOCK0) // 5))
                if c is None:
                    return None
                v = VOW[(n - BLOCK0) % 5]
                return ('qu' if v == 'u' else 'qu' + v) if c == 'q' else c + v
            return None
        v = N.get(t)
        return None if v is None or v[:1] in '[{' else v
    out = []
    for label, fn, _ in LEAVES:
        word = []
        for line in open(os.path.join(HERE, fn), encoding='utf8'):
            if line.startswith('#'):
                continue
            line = line.replace('/INS', ' ').replace('INS', ' ')
            for part in re.split(r'(\[[^\]]*\])', line.strip()):
                if part.startswith('['):
                    continue
                for t in part.split():
                    t = t.rstrip('?.')
                    word.append((t, dec(t)))
        out.append((label, [word]))
    return out


def reading():
    txt = open(os.path.join(HERE, 'reading.md'), encoding='utf8').read().split('## English translation')[0]
    R = {}
    for label, _, head in LEAVES:
        sec = txt.split(head, 1)[1].split('\n## ', 1)[0]
        sec = re.split(r'\n(?:Token-level notes|Notes):', sec)[0]
        bold = ' '.join(re.findall(r'\*\*(.+?)\*\*', sec, re.S))
        bold = re.sub(r'\{[^}]*\}', ' # ', bold)          # word-signs and numbers left as signs
        bold = bold.replace('…', ' # ')                   # passages not read
        R[label] = bold
    return R
