"""Every attestation of Meluhha in the ORACC corpora (CC0), read for people and goods.

Input: the attestation table gathered from ORACC epsd2 (entries Meluhha[1]GN, Meluhha[0]PN,
Me.luh..., with the line, context and full text of each). Output: counts by period and genre, the
people described as 'son of Meluhha', 'man of Meluhha' or given oil and grain as Meluhhans, the
goods called 'of Meluhha', and the Irisagrig allotment texts that name Nanaza and Samar.

Usage: python meluhha_oracc.py path/to/meluhha_attestations_oracc.csv
Writes results/meluhha_oracc.md.
"""
import csv
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
GOODS = [('abba wood (furniture, weapons)', r'ab-?ba me-luḫ'), ('mes wood', r'\bmes me-luḫ'),
         ('boats', r'\bma₂ me-luḫ'), ('copper', r'uruda? me-luḫ|urudu'), ('carnelian', r'gug|na₄'),
         ('the dar bird', r'dar-?(re|ra)? me-luḫ|dar me-luḫ'), ('garden / date palm', r'kiri₆ me-luḫ|gešimmar'),
         ('Meluhha-style chair / table', r'gu-za|banšur'), ('ur-DAR animal', r'ur-DAR')]


def say(s=''):
    OUT.append(s)
    print(s)


def clean(t):
    return re.sub(r'\s*-\s*', '-', re.sub(r'[⸢⸣\[\]]', '', t))


def main(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    say('# Meluhha in the cuneiform record (ORACC)')
    say()
    texts = {r['text'] for r in rows}
    say('- %d attestations in %d texts. By period: %s. By genre: %s.' % (
        len(rows), len(texts), ', '.join('%s %d' % kv for kv in Counter(r['period'] or '?' for r in rows).most_common()),
        ', '.join('%s %d' % kv for kv in Counter(r['genre'] or '?' for r in rows).most_common())))
    say()
    say('## People')
    say()
    ppl = defaultdict(set)
    for r in rows:
        ln = clean(r['line'])
        m = re.search(r'((?:[\w₀-₉]+-)*(?:d\s)?[\w₀-₉]+(?:-[\w₀-₉]+)*)\s+dumu-?\s*me-luḫ', ln)
        if m and not re.fullmatch(r'[\d\s]+', m.group(1)):
            ppl['%s, son of Meluhha' % m.group(1).replace('d ', 'd')].add(r['designation'])
        elif re.search(r'dumu-?\s*me-luḫ', ln):
            ppl['(name broken or on another line), son of Meluhha'].add(r['designation'])
        if re.search(r'lu₂-?\s*me-luḫ', ln):
            ppl['"man/men of Meluhha" (%s)' % ln[-60:].strip()].add(r['designation'])
        if 'ugula' in ln and 'me-luḫ' in ln:
            ppl['overseer of Meluhha'].add(r['designation'])
        if re.search(r'e-lum-me-luḫ', ln):
            ppl['Elum-Meluh (a name)'].add(r['designation'])
        if 'illat' in ln and 'me-luḫ' in ln:
            ppl['the envoy Utu-illat, gone to Meluhha'].add(r['designation'])
    for p, d in sorted(ppl.items(), key=lambda x: -len(x[1])):
        say('- %s: %d text%s (%s).' % (p, len(d), '' if len(d) == 1 else 's', '; '.join(sorted(d)[:6])))
    say()
    say('## The Irisagrig allotments')
    say()
    seen = set()
    for r in rows:
        ft = clean(r['full_text'])
        if 'na-na-' in ft and 'ma-ar' in ft and r['designation'] not in seen:
            seen.add(r['designation'])
            nm = re.findall(r'(na-na-[\w₀-₉]+)', ft)
            say('- %s (%s, %s): %s; %s; "oil allotment of the men of Meluhha, royal donated slaves, shepherds of '
                'bezoars".' % (r['designation'], r['provenience'][:10], r['date'],
                               ', '.join(sorted(set(nm))), ', '.join(sorted(set(re.findall(r'(sa₆-ma-ar)', ft))))))
    say('- The two names recur on %d tablets of one year (Šu-Suen 6: month 3, and month 12 twice): a standing '
        'allotment, not a single mention. The first is spelt na-na-za twice and na-na-sa₃ once: an alternation of z '
        'and s that can point to a sound Sumerian writing lacked (an affricate), as foreign names often show.' % len(seen))
    say()
    say('## Goods "of Meluhha"')
    say()
    g = Counter()
    for r in rows:
        ln = clean(r['line'])
        for lab, pat in GOODS:
            if re.search(pat, ln):
                g[lab] += 1
    say('- ' + '; '.join('%s %d' % kv for kv in g.most_common()) + '.')
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'meluhha_oracc.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
