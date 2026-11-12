"""sande1660 cipher B (m0063): build a letter table from the glosses of the time ("full construction") and say how
much it reads.

    python3 -I scripts/cipherB_glosses.py     (run from beling/; writes results/cipherB_m0063.txt)

Rule: a gloss is aligned one group to one letter only when, after doubled letters are made single and spaces
removed (v written as u, as the cipher does), it has exactly as many letters as the run has groups (9xx end marks and '#' left out). Each aligned run adds
group -> letter pairs; a group given two different letters is reported as a conflict.
Checks: (0) six glossed runs on m0062, read after the table was built, decoded with it; (1) leave-one-out: for each aligned run, the table built from the other aligned runs decodes it, and the
share of its groups given the right letter is counted; (2) the runs that cannot be aligned (no gloss, or lengths
differ) are decoded with the full table.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    runs = []
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            if not raw.startswith('@'):
                continue
            rid, rest = raw.split(None, 1)
            groups, _end, gloss = [p.strip() for p in rest.split('|')]
            gloss = re.sub(r'\s*\(.*$', '', gloss.split(':', 1)[1]).strip()
            toks = [g.rstrip('*') for g in groups.split('.') if g.strip() and g.strip() != '#']
            runs.append((rid[1:], [int(t) for t in toks], None if gloss == 'none' else gloss))
    return runs


def letters(gloss):
    s = re.sub(r'[^a-z]', '', gloss.lower()).replace('v', 'u')
    return re.sub(r'(.)\1+', r'\1', s)


def build(aligned):
    table, conflicts = {}, []
    for rid, toks, lets in aligned:
        for g, c in zip(toks, lets):
            if g in table and c not in table[g]:
                conflicts.append((g, sorted(table[g]), c, rid))
            table.setdefault(g, set()).add(c)
    return table, conflicts


def decode(toks, table):
    return ''.join('/'.join(sorted(table[g])) if g in table else '?' for g in toks)


def main():
    runs = load(os.path.join(HERE, 'cipherB', 'm0063_runs.txt'))
    aligned, other = [], []
    for rid, toks, gloss in runs:
        if gloss and len(letters(gloss)) == len(toks):
            aligned.append((rid, toks, letters(gloss)))
        else:
            other.append((rid, toks, gloss))
    table, conflicts = build(aligned)
    out = ['# Cipher B, m0063: letter table from the glosses (see scripts/cipherB_glosses.py)', '']
    out.append('Aligned runs (gloss letters = groups): ' + ', '.join(r for r, _, _ in aligned))
    out.append('Not aligned: ' + ', '.join('%s (%s)' % (r, g or 'no gloss') for r, _, g in other))
    out.append('')
    by_letter = {}
    for g, cs in table.items():
        for c in cs:
            by_letter.setdefault(c, []).append(g)
    out.append('Table, letter: groups')
    for c in sorted(by_letter):
        out.append('  %s: %s' % (c, ', '.join(str(g) for g in sorted(by_letter[c]))))
    out.append('Groups: %d; conflicts (one group, two letters): %s' % (
        len(table), '; '.join('%d %s vs %s (%s)' % c for c in conflicts) or 'none'))
    out.append('')
    out.append('Leave-one-out (table from the other aligned runs):')
    tot = right = known = 0
    for i, (rid, toks, lets) in enumerate(aligned):
        t2, _ = build(aligned[:i] + aligned[i + 1:])
        d = decode(toks, t2)
        r = sum(1 for g, c in zip(toks, lets) if g in t2 and c in t2[g])
        k = sum(1 for g in toks if g in t2)
        tot += len(toks)
        right += r
        known += k
        out.append('  %-4s %-28s -> %-20s %d/%d groups known, %d right' % (rid, lets, d, k, len(toks), r))
    out.append('  total: %d groups, %d known from the other runs, %d of those right (%.2f of all groups)'
               % (tot, known, right, right / tot))
    out.append('')
    out.append('Runs not aligned, decoded with the full table:')
    for rid, toks, gloss in other:
        out.append('  %-4s %-40s -> %s   (gloss: %s)' % (rid, '.'.join(map(str, toks)), decode(toks, table), gloss))
    out.append('')
    out.append('Check on m0062 (cipherB/m0062_runs.txt; glossed runs read after the table was built; not used to build it):')
    tot = right = known = 0
    for rid, toks, gloss in load(os.path.join(HERE, 'cipherB', 'm0062_runs.txt')):
        lets = letters(gloss)
        d = decode(toks, table)
        same_len = len(lets) == len(toks)
        r = sum(1 for g, c in zip(toks, lets) if g in table and c in table[g]) if same_len else 0
        k = sum(1 for g in toks if g in table)
        tot += len(toks)
        right += r
        known += k
        out.append('  %-4s %-40s -> %-12s gloss %-12s %d/%d groups known, %d agree with the gloss' % (
            rid, '.'.join(map(str, toks)), d, lets, k, len(toks), r))
    out.append('  total: %d groups, %d in the m0063 table, %d agree with the m0062 glosses (%.2f of all groups)'
               % (tot, known, right, right / tot))
    with open(os.path.join(HERE, 'results', 'cipherB_m0063.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    sys.exit(main())
