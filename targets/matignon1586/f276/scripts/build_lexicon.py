"""Build the period-French word list used by measure.py --lex: Berger de Xivrey, Recueil des lettres missives de
Henri IV, t. I-V (the repo's lang/ corpus fr-henri4), Internet Archive OCR. Accents stripped; counts per word.
    python build_lexicon.py            -> xivrey_words.tsv (downloads ~10 MB once)
"""
import os, re, unicodedata, collections, urllib.request, time
IDS = ['recueildeslettre01henr', 'recueildeslettr02henr', 'recueildeslettre03henr', 'recueildeslettre04henr',
       'recueildeslettre05henr']
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
c = collections.Counter()
for i in IDS:
    f = os.path.join(HERE, i + '.txt')
    if not os.path.exists(f):
        req = urllib.request.Request(f'https://archive.org/download/{i}/{i}_djvu.txt', headers={'User-Agent': 'Mozilla/5.0'})
        open(f, 'wb').write(urllib.request.urlopen(req, timeout=300).read()); time.sleep(3)
    t = unicodedata.normalize('NFD', open(f, errors='replace').read())
    t = ''.join(ch for ch in t if unicodedata.category(ch) != 'Mn').lower().replace('-\n', '')
    c.update(re.findall(r'[a-z]+', t))
with open(os.path.join(HERE, 'xivrey_words.tsv'), 'w') as o:
    o.write('# Berger de Xivrey, Lettres missives de Henri IV t. I-V (IA OCR; lang/ corpus fr-henri4), accents stripped\n')
    for w, n in c.most_common(): o.write(f'{w}\t{n}\n')
print(len(c), 'types,', sum(c.values()), 'tokens')
