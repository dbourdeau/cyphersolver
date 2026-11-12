"""Context for the report's open groups: table neighbours (three valued groups each side), the report tokens
around each occurrence decoded with the frozen table, and the numeral groups of the table.

    python3 -I scripts/open_groups.py [--target ..] > results/open_groups_context.txt
"""
import argparse
import os

OPEN = [805, 6, 1210, 689, 460, 285, 214, 711, 1118, 1052, 726, 836, 585, 1152, 222]
NUMERALS = {'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze',
            'treize', 'quatorze', 'quinze', 'seize', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante',
            'cent', 'mille'}


def read_table(target):
    table = {}
    for line in open(os.path.join(target, 'codetable.tsv'), encoding='utf-8'):
        if line.startswith('#'):
            continue
        f = line.rstrip('\n').split('\t')
        table[int(f[0])] = (f[1], f[2], int(f[4]))
    return table


def read_report(target):
    toks = []
    for line in open(os.path.join(target, 'transcription', 'report_61005.txt'), encoding='utf-8'):
        if line.startswith('L'):
            label, rest = line.split(None, 1)
            toks += [(label, int(t.rstrip('?'))) for t in rest.strip().split('.') if t.strip()]
    return toks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', default='..')
    args = ap.parse_args()
    table = read_table(args.target)
    report = read_report(args.target)
    keys = sorted(table)

    def show(g):
        if g in table:
            v, grade, n = table[g]
            return f'{g}={v}' + ('?' if grade == 'M' else '')
        return f'[{g}]'

    print('# open groups of the report: table neighbours and report context (frozen codetable.tsv)')
    for g in OPEN:
        lo = [k for k in keys if k < g][-3:]
        hi = [k for k in keys if k > g][:3]
        print(f'\n{g}: below {" ".join(show(k) for k in lo) or "-"} | above {" ".join(show(k) for k in hi) or "-"}')
        for i, (label, t) in enumerate(report):
            if t == g:
                ctx = [show(x) for _, x in report[max(0, i - 5):i]] + [f'<<{g}>>'] + [show(x) for _, x in report[i + 1:i + 6]]
                print(f'  {label}: ' + ' '.join(ctx))
    print('\n# numeral groups in the table (value a number word), with the gaps between them')
    nums = [k for k in keys if table[k][0].lower() in NUMERALS]
    for k in nums:
        print(f'  {show(k)} (count {table[k][2]})')
    print('  groups below 18 with any value: ' + ' '.join(show(k) for k in keys if k < 18))


if __name__ == '__main__':
    main()
