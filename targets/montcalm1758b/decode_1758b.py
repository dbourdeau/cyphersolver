"""Decode Montcalm's letter to Bougainville of 21 Nov 1758 (AN 155AP/2, piece 25) with code B, group by group.

Reads transcriptions/figures_reconciled.txt and key/code_B_table.tsv (build_key_table.py) and writes
results/decode_line_by_line.txt. Every value that the printed letters do not show (status "inferred" in the table)
is printed as [?value]; a place where the two readings of the figures differ is printed as value1|value2.
Deterministic, standard library only:  python decode_1758b.py
"""
import csv, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def table():
    with open(HERE / 'key' / 'code_B_table.tsv', encoding='utf-8') as f:
        rows = csv.DictReader([l for l in f if not l.startswith('#')], delimiter='\t')
        return {r['group']: r for r in rows}


def show(g, tab):
    r = tab.get(g.replace('+', '*'))
    if r is None:
        return f'[{g}: not in the table]', 'missing'
    v = r['value']
    return (f'[?{v}]', 'inferred') if r['status'] == 'inferred' else (v, 'attested')


def main():
    tab = table()
    out, n, n_inf, n_alt = [], 0, 0, 0
    out.append('# Montcalm to Bougainville, 21 Nov 1758: decode with code B (key/code_B_table.tsv), made by decode_1758b.py.')
    out.append('# Each line: label, then group=value; [?x] = value inferred from the code\'s order (not shown by the printed')
    out.append('# letters); a|b = the two readings of the figures differ (34 first reading, 35 blind reading). Then the line run together.')
    for line in open(HERE / 'transcriptions' / 'figures_reconciled.txt', encoding='utf-8'):
        m = re.match(r'(P\dL\d):\s*(.*)', line.strip())
        if not m:
            continue
        pairs, run = [], []
        for g in m.group(2).split():
            n += 1
            alts = g.split('|')
            vals = [show(a, tab) for a in alts]
            if len(alts) > 1:
                n_alt += 1
            if any(k == 'inferred' for _, k in vals):
                n_inf += 1
            v = '|'.join(x for x, _ in vals)
            pairs.append(f'{g}={v}')
            run.append(v)
        out.append('')
        out.append(f'{m.group(1)}: ' + '  '.join(pairs))
        out.append(f'{m.group(1)} run: ' + ' '.join(run))
    out.append('')
    out.append(f'# {n} groups; {n_inf} with an inferred value; {n_alt} where the two readings of the figures differ.')
    (HERE / 'results').mkdir(exist_ok=True)
    (HERE / 'results' / 'decode_line_by_line.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
