"""The open CISI digitisation (mayig/indus-valley-script-corpus, MIT licence; Parpola et al., Corpus of Indus Seals
and Inscriptions, Parpola's own sign numbers P000-P2xx) as a second, independent transcription of the objects it covers
(Mohenjo-daro M-1 to M-184, 179 texts, mostly unicorn seals).

build(repo) writes data/cisi_mayig.tsv from a clone of the repository: one row per side and line, signs in reading
order (the repository lists the sealing left to right; the script reads right to left, so the list is reversed), with
per-sign damage and uncertainty. load() reads it back. p2icit() maps Parpola signs to ICIT glyphs through the
repository's own Mahadevan equivalents and data/icit_m77_map.tsv (no alignment on the texts).

Usage: python cisi.py path/to/indus-valley-script-corpus
"""
import glob
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, 'data', 'cisi_mayig.tsv')
HEADER = ('# Source: https://github.com/mayig/indus-valley-script-corpus (MIT licence, commit ad2f1e2), a digitisation\n'
          '# of Parpola et al., Corpus of Indus Seals and Inscriptions. Signs are Parpola numbers in reading order.\n')


def build(repo):
    rows = []
    for f in sorted(glob.glob(os.path.join(repo, 'corpus', '*', '*.json'))):
        for side in json.load(open(f, encoding='utf-8')):
            lines = defaultdict(list)
            for g in side['graphemes']:
                ft = g.get('features') or [0, 1, 0]
                lines[ft[1]].append((g['id'], ft[0], ft[2]))
            for ln in sorted(lines):
                gs = lines[ln][::-1]
                rows.append((side['id'], side.get('description', '').replace('\t', ' '), str(ln),
                             ' '.join(g for g, d, u in gs), ' '.join(str(d) for g, d, u in gs), ' '.join(str(u) for g, d, u in gs)))
    feats = {}
    for f in sorted(glob.glob(os.path.join(repo, 'features', '*.json'))):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except (OSError, ValueError):
            continue
        feats[d['id']] = (d.get('description', '').replace('\t', ' '), ','.join(d.get('mahadevan_graphemes', [])))
    with open(TSV, 'w', encoding='utf-8', newline='\n') as out:
        out.write(HEADER)
        out.write('side\tdescription\tline\tsigns\tdamage\tuncertainty\n')
        for r in rows:
            out.write('\t'.join(r) + '\n')
    with open(os.path.join(HERE, 'data', 'cisi_signs.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        out.write(HEADER)
        out.write('parpola\tdescription\tmahadevan\n')
        for k in sorted(feats):
            out.write('%s\t%s\t%s\n' % (k, feats[k][0], feats[k][1]))
    print('rows %d, sides %d, signs described %d' % (len(rows), len({r[0] for r in rows}), len(feats)))


def _read(path):
    out = []
    with open(path, encoding='utf-8') as f:
        hdr = None
        for ln in f:
            if ln.startswith('#'):
                continue
            p = ln.rstrip('\n').split('\t')
            if hdr is None:
                hdr = p
                continue
            out.append(dict(zip(hdr, p)))
    return out


def load():
    """{side id: {'description', 'seq': [[P signs] per line], 'damage': [[..]], 'unc': [[..]]}}"""
    objs = {}
    for r in _read(TSV):
        o = objs.setdefault(r['side'], {'description': r['description'], 'seq': [], 'damage': [], 'unc': []})
        o['seq'].append(r['signs'].split())
        o['damage'].append([int(x) for x in r['damage'].split()])
        o['unc'].append([int(x) for x in r['uncertainty'].split()])
    return objs


def signs():
    return {r['parpola']: (r['description'], r['mahadevan'].split(',') if r['mahadevan'] else []) for r in
            _read(os.path.join(HERE, 'data', 'cisi_signs.tsv'))}


def p2icit():
    """Parpola sign -> set of ICIT glyphs, through the Mahadevan numbers."""
    m2i = defaultdict(set)
    for r in _read(os.path.join(HERE, 'data', 'icit_m77_map.tsv')):
        m2i[r['m77'].replace('MSg', 'M').lstrip('M').lstrip('0')].add(r['icit'])
    out = {}
    for p, (d, ms) in signs().items():
        out[p] = set().union(*[m2i.get(m.lstrip('M').lstrip('0'), set()) for m in ms]) if ms else set()
    return out


def cisi_no(side):
    """'M-1A' -> 'M-1' (the CISI object number used in ICIT field 1)."""
    return side.rstrip('ABCDEFGH') if side[-1:].isalpha() else side


if __name__ == '__main__':
    build(sys.argv[1])
