"""score8211.py: the pre-registered held-out test (HELDOUT-8211.md) on new ciphertext in Vat. lat. 8211.

Frozen key = ../key.json (sha256 f78de9d1...); units = lib6.DEFAULT_MERGE; word = one cipher segment of
heldout8211/transcription-8211.tsv; lexicon = cipherkit `it` corpus types with count >= 2 plus the clear text of
ff. 298r-v, 68r, 198r and of the 8211 pages; a segment with a code sign or an unkeyed sign is a miss;
null = permutation_z_key on the hit count, n=200, seed 0. Writes heldout8211/result.json."""
import sys, json, re, unicodedata, collections, csv, hashlib
sys.path.insert(0, '/Users/aaymeloglu/git/unsolved-ciphers')
sys.path.insert(0, '/Users/aaymeloglu/.claude-assistant/research/unsolved-ciphers/mantua-1524/solve')
import lib6 as L
from cipherkit import corpora
from cipherkit.controls import permutation_z_key

KEYF = L.HERE + 'key.json'
assert hashlib.sha256(open(KEYF, 'rb').read()).hexdigest().startswith('f78de9d123bf'), 'key changed'
key = L.load_key(KEYF)
TR = L.HERE + 'heldout8211/transcription-8211.tsv'
rows = list(csv.DictReader((l for l in open(TR) if not l.startswith('#')), delimiter='\t'))


def fold(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return t.replace('j', 'i').replace('v', 'u').replace('k', 'c').replace('y', 'i')


lex = collections.Counter(re.findall('[a-z]+', re.sub('[^a-z]+', ' ', fold(corpora.text('it')))))
lexicon = {w for w, c in lex.items() if c >= 2}
clear = ' '.join(r['text'] for r in L.rows(True) if r['kind'] == 'clear')
clear += ' ' + ' '.join(r['text'] for r in rows if r['kind'] == 'clear')
lexicon |= set(re.findall('[a-z]+', fold(re.sub(r'[\[\]{}?]', '', clear))))

segs = [L.units(r['text']) for r in rows if r['kind'] == 'cipher']
segs = [u for u in segs if u]


def word(m, u):
    if any(x in L.CODE or x not in m for x in u):
        return None
    return ''.join(m[x] for x in u)


def hits(m, long_only=False):
    n = 0
    for u in segs:
        w = word(m, u)
        if w is None or (long_only and len(w) < 4):
            continue
        n += w in lexicon
    return n


out = {'segments': len(segs), 'units': sum(map(len, segs)),
       'transcription_sha256': hashlib.sha256(open(TR, 'rb').read()).hexdigest()}
raw = [(L.dec(u, key, upper=False), (word(key, u) or '') in lexicon) for u in segs]
out['raw'] = raw
print('raw decode:', ' | '.join(w.upper() + ('*' if h else '') for w, h in raw))
n4 = sum(1 for u in segs if (word(key, u) or '') and len(word(key, u)) >= 4)
for lab, lo in (('all', False), ('4plus', True)):
    zz = permutation_z_key(lambda m: hits(m, lo), dict(key), None, n=200, seed=0)
    zz['segments'] = len(segs) if not lo else n4
    zz['share'] = zz.get('observed', hits(key, lo)) / zz['segments'] if zz['segments'] else 0
    out[lab] = zz
    print(lab, {k: round(v, 3) if isinstance(v, float) else v for k, v in zz.items()})
z = out['all'].get('z', 0)
out['pass'] = out['all']['share'] >= 0.40 and z >= 5
print('PASS' if out['pass'] else 'FAIL', '(bar: share >= 0.40 and z >= 5)')
json.dump(out, open(L.HERE + 'heldout8211/result.json', 'w'), indent=1)
