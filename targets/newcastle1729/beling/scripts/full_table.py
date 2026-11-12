"""Full construction of the code table (PREREG_round2.md, section 2): one row per group with its value and every
attestation, by kind: interlinear gloss, clear copy (4 Aug 1729, 60903-60904), or context proposal only.

    python3 -I scripts/full_table.py [--target ..]
Writes results/full_table.tsv and prints a summary.
"""
import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_4aug import TOKEN, ALIAS, norm, sib_files, build_table, code_lines, units, align  # noqa: E402


def gloss_attestations(paths):
    att = collections.defaultdict(list)
    for path in paths:
        name = os.path.basename(path)[:-4]
        for line in open(path, encoding='utf-8'):
            if not line.startswith('L'):
                continue
            label, rest = line.split(None, 1)
            rest = re.sub(r'\{[^}]*\}(=\S+)?', ' ', rest)
            for m in TOKEN.finditer(rest):
                value = m.group(3)
                doubtful = bool(m.group(2)) or '?' in value
                att[int(m.group(1))].append((f'{name}:{label}', value.strip('[]').lstrip('?'), doubtful))
    return att


def value_of(occ):
    firm = [v for _, v, d in occ if not d] or [v for _, v, _ in occ]
    return collections.Counter(ALIAS.get(v, v) for v in firm).most_common(1)[0][0]


def proposals(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
        if m:
            out[int(m.group(1))] = f'{m.group(2)} ({m.group(3)})'
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', default='..')
    ap.add_argument('--out', default='results/full_table.tsv')
    args = ap.parse_args()
    repo = sib_files(args.target, lambda n: True)
    mine = [os.path.join('transcription', n) for n in sorted(os.listdir('transcription'))
            if n.startswith('sib194_') and n.endswith('.txt')]
    att = gloss_attestations(repo + mine)

    # clear copy: round-1 alignment with the repo's full table
    full = build_table(repo)
    lines = code_lines(args.target)
    clear = collections.defaultdict(list)
    for unit, names, page, text in units('transcription/clear_4aug_brackets.tsv'):
        toks = [t for n in names for t in lines[n]]
        _, _, flags = align(toks, text, full)
        for (g, struck), fl in zip(toks, flags or []):
            if struck or fl[0] != 'val':
                continue
            clear[g].append(f'{page} u{unit} ' + ('agrees' if fl[1] else f'differs:"{fl[2]}"'))

    ctx = proposals('results/open_group_values.md')
    groups = sorted(set(att) | set(clear) | set(ctx))
    rows, kinds, conflicts = [], collections.Counter(), 0
    for g in groups:
        occ = att.get(g, [])
        val = value_of(occ) if occ else ''
        firm_vals = {norm(ALIAS.get(v, v)) for _, v, d in occ if not d and v != '_'}
        differs = any('differs' in c for c in clear.get(g, []))
        conflict = []
        if len(firm_vals) > 1:
            conflict.append('glosses disagree')
        if differs:
            conflict.append('clear copy differs')
        if conflict:
            conflicts += 1
        if occ and clear.get(g):
            basis = 'gloss+clear'
        elif occ:
            basis = 'gloss'
        elif clear.get(g):
            basis = 'clear only'
        else:
            basis = 'context only'
        if val == '_':
            basis += ' (null)'
        kinds[basis] += 1
        glosses = ' '.join(f'{w}={v}{"?" if d else ""}' for w, v, d in occ)
        rows.append([str(g), val, basis, str(len(occ)), glosses, '; '.join(clear.get(g, [])),
                     ctx.get(g, ''), ', '.join(conflict)])
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write('# full_table.py: one row per code group. value = repo rule over all glosses (194 included); '
                'glosses: source:line=gloss (? doubtful); clear: 4 Aug clear copy, round-1 alignment with the '
                "repo's full table (differs = the letters the alignment gave, approximate); context: round-1 "
                'proposal, [I].\n')
        f.write('# group\tvalue\tbasis\tn_gloss\tglosses\tclear_copy\tcontext\tconflict\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print('groups:', len(rows), dict(sorted(kinds.items())), 'rows with a conflict:', conflicts)
    new = sorted(g for g in att if all(w.startswith('sib194_') for w, _, _ in att[g]))
    print('groups attested only in the 194 transcription:', new)
    print('open groups:', {g: (value_of(att[g]) if g in att else None) for g in sorted(ctx)})


if __name__ == '__main__':
    main()
