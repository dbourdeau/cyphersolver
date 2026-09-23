"""Lead 5 (sixth pass): a fourth language family, and the world base rate of the fish = star pun.

Every fish reading rests on one word meaning both 'fish' and 'star' (Dravidian *min). CLICS4
(github.com/clics/clics4, CC BY) has FISH and STAR in 3,447 languages. For each language: are the
two words identical (colexified), or nearly so (normalised edit similarity >= 0.75)? Which families
have it, and in particular the families of South Asia: Dravidian, Indo-Aryan, Munda
(Austroasiatic), Burushaski, Sino-Tibetan of the Himalaya. The same for the numeral that most
often precedes the fish in the Indus texts (3) against STAR, as a control for chance similarity.

Usage: python fish_star_world.py path/to/clics4/cldf
Writes results/fish_star_world.md.
"""
import csv
import io
import os
import re
import sys
import unicodedata
import zipfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def plain(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', w)


def ed(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[len(b)]


def sim(a, b):
    return 1 - ed(a, b) / max(len(a), len(b)) if a and b else 0


def main(cldf):
    langs = {l['ID']: l for l in csv.DictReader(open(os.path.join(cldf, 'languages.csv'), encoding='utf-8'))}
    z = zipfile.ZipFile(os.path.join(cldf, 'concepts.csv.zip'))
    concepts = list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding='utf-8')))
    want = {}
    for c in concepts:
        g = (c.get('Concepticon_Gloss') or c.get('Name') or '').upper()
        if g in ('FISH', 'STAR', 'THREE'):
            want[c['ID']] = g
    forms = defaultdict(lambda: defaultdict(set))
    z = zipfile.ZipFile(os.path.join(cldf, 'forms.csv.zip'))
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding='utf-8')):
        g = want.get(r['Parameter_ID'])
        if g:
            forms[r['Language_ID']][g].add(plain(r['Form'] or r['Value']))
    both = {k: v for k, v in forms.items() if v['FISH'] and v['STAR']}
    say('# The fish = star pun across the world\'s languages (CLICS4)')
    say()
    say('Languages with words for both FISH and STAR: %d (of %d).' % (len(both), len(langs)))
    say()
    same, near, near3 = [], [], 0
    fam = Counter()
    for lid, v in both.items():
        best = max((sim(a, b), a, b) for a in v['FISH'] for b in v['STAR'])
        if best[0] == 1:
            same.append((lid, best))
        elif best[0] >= 0.75:
            near.append((lid, best))
        fam[langs[lid]['Family_Name'] or langs[lid]['Name']] += 1
        if v['THREE']:
            b3 = max(sim(a, b) for a in v['THREE'] for b in v['STAR'])
            near3 += b3 >= 0.75
    nb3 = sum(1 for v in both.values() if v['THREE'])
    say('- identical word for fish and star: %d languages (%.1f%%); near-identical (similarity >= 0.75): %d '
        '(%.1f%%). Control: the word for "three" near-identical with "star" in %d of %d (%.1f%%).' % (
            len(same), 100 * len(same) / len(both), len(near), 100 * len(near) / len(both), near3, nb3,
            100 * near3 / nb3 if nb3 else 0))
    say()
    say('| language | family | fish | star |')
    say('|---|---|---|---|')
    for lid, (s, a, b) in sorted(same + near, key=lambda x: (-x[1][0], langs[x[0]]['Family_Name'])):
        say('| %s | %s | %s | %s |' % (langs[lid]['Name'], langs[lid]['Family_Name'], a, b))
    say()
    say('## South Asia')
    say()
    say('| language | family | fish | star | similarity |')
    say('|---|---|---|---|---|')
    sa = [(lid, l) for lid, l in langs.items() if lid in both and (
        l['Family_Name'] in ('Dravidian', 'Burushaski') or re.search(r'Munda|Santali|Mundari|Ho\b|Sora|Kharia|Korku|Juang|Gutob|Remo|Bondo', l['Name'])
        or (l['Family_Name'] == 'Indo-European' and float(l['Longitude'] or 0) > 66 and 5 < float(l['Latitude'] or 0) < 36))]
    for lid, l in sorted(sa, key=lambda x: (x[1]['Family_Name'], x[1]['Name'])):
        v = both[lid]
        s, a, b = max((sim(a, b), a, b) for a in v['FISH'] for b in v['STAR'])
        say('| %s | %s | %s | %s | %.2f |' % (l['Name'], l['Family_Name'], ', '.join(sorted(v['FISH'])),
                                             ', '.join(sorted(v['STAR'])), s))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'fish_star_world.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
