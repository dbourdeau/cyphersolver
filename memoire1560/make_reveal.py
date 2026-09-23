"""Build docs/reveal/memoire1560.json: ff. 152v.09-14 (the Clairac assembly), decoded sign by sign with key.txt.

A cipher word whose mechanical decrypt differs from the reading (reading_152r-154r.txt) is marked 'unc'.
"""
import os, re, json, sys, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decrypt

LINES = [f'152v.{n:02d}' for n in range(9, 15)]


def plain(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s).replace('j', 'i').replace('v', 'u')


key = decrypt.load_key()
units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
reading = {}
for l in open(os.path.join(HERE, 'reading_152r-154r.txt'), encoding='utf8'):
    if '\t' in l and not l.startswith('#'):
        k, t = l.rstrip('\n').split('\t')
        reading[k] = t
cipher = {f'{fol}.{n:02d}': line for fol, n, line in decrypt.lines()}

tokens = []
for ln in LINES:
    words = re.sub(r'\[[^\]]*\]', ' ', cipher[ln]).split()
    rwords = [plain(w) for w in re.sub(r'\[\.\.\]', ' ', reading[ln]).replace("'", ' ').split()]
    rtext = ''.join(rwords)
    for w in words:
        if '=' + w in key:
            tokens.append({'g': w, 'p': key['=' + w], 'cls': 'code'})
        else:
            dec = decrypt.dec_word(w, key, units)
            # polyphonic delta (u/v/b/g) and i/y/j are not errors; otherwise a word must match a reading word closely
            norm = lambda t: t.translate(str.maketrans('bgy', 'uui'))
            best = max((difflib.SequenceMatcher(None, norm(plain(dec)), norm(r)).ratio() for r in rwords), default=0)
            cls = '' if best >= 0.99 else 'unc'
            i = 0
            while i < len(w):
                for u in units:
                    if w.startswith(u, i):
                        v = key[u]
                        tokens.append({'g': u, 'p': v, 'cls': cls} if cls else {'g': u, 'p': v})
                        i += len(u)
                        break
                else:
                    tokens.append({'g': w[i], 'p': '?', 'cls': 'unk'}); i += 1
        tokens.append({'g': '', 'p': ' ', 'cls': 'plain'})
    tokens.append({'g': '', 'p': ' / ', 'cls': 'plain'})

out = {
    'slug': 'memoire1560',
    'anchor': 'reading',
    'title': 'Clairac, December 1560: two thousand rebels in arms',
    'caption': 'BnF fr. 3157 f. 152v, lines 9-14, decoded sign by sign with the key rebuilt here. '
               'Each two-stroke unit (zo, pp, io, s3, lz) is one letter; Z, 4 and c+ are whole-word codes.',
    'unit': 'signs',
    'key_note': 'Homophonic key rebuilt ciphertext-only (memoire1560/key.txt); signs in words whose decrypt needs an emendation are marked uncertain.',
    'tokens': tokens,
}
json.dump(out, open(os.path.join(HERE, '..', 'docs', 'reveal', 'memoire1560.json'), 'w', encoding='utf8'),
          indent=1, ensure_ascii=False)
print(len([t for t in tokens if t['g']]), 'groups;', sum(t.get('cls') == 'unc' for t in tokens), 'unc')
