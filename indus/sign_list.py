"""A structural sign list: every sign with 5+ tokens in the ICIT-derived corpus plus the M77 additions,
with what can be said of it without sound values.

Columns: ICIT id; tokens (ICIT-derived / M77 additions); share of its tokens text-initial, medial, final;
commonest left and right neighbours; the ending its names take when it is the last sign before 740 / 520
(lines with each); its numeral value and stroke series if a numeral; Fairservis 1992's identification of the
drawing (sure / likely matches, keys/fairservis1992_raw.tsv); anchors (copper-tablet equations, the
provisional anchors of anchors.py); a role, from these facts only:
  opener   - one of the heading signs 817 / 820 / 861 or the stroke that follows them
  ending   - 740 / 520, or 400 / 90 / 151 after them
  numeral  - a stroke numeral (short, long or tiered series)
  520-name - the last sign of names that take 520 in 20%+ of lines (5+ lines)
  740-name - the last sign of names that take 740 in 90%+ of lines (5+ lines)
  other    - the rest

Writes results/sign_list.tsv and results/sign_list.md (a summary).
"""
import csv
import os
from collections import Counter, defaultdict

from numerals import NUMS
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
FIRM = {'341': 'rhinoceros (copper tablets)', '749': 'markhor goat (copper tablets)', '753': 'hare (copper tablets)',
        '777': 'goat / archer (copper tablets)', '778': 'goat (copper tablets)'}
PROV = {'347': 'multi-headed animal (moulded tablets, provisional)', '460': 'tree / plant (moulded tablets, provisional)',
        '645': 'cross motif (weak)', '318': 'gharial (weak)'}


def split_end(t):
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        return tuple(t[:-2]), t[-2]
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return tuple(t[:-1]), t[-1]
    return None, None


def main():
    ident = {}
    for r in csv.DictReader((ln for ln in open(os.path.join(HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8')
                             if not ln.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            ident.setdefault(r['icit'].split('|')[0], '%s %s' % (r['fcode'], r['gloss'].split('=>')[0].strip()))
    a, b = load(), load(only_m77=True)
    tok = Counter()
    ta, tb = Counter(), Counter()
    pos = defaultdict(Counter)
    left, right = defaultdict(Counter), defaultdict(Counter)
    ends = defaultdict(Counter)
    for rows, tc in ((a, ta), (b, tb)):
        for r in rows:
            for ln in r['seq']:
                ln = [g for g in ln if g != '?']
                for i, g in enumerate(ln):
                    tok[g] += 1
                    tc[g] += 1
                    pos[g]['i' if i == 0 else ('f' if i == len(ln) - 1 else 'm')] += 1
                    left[g][ln[i - 1] if i else '^'] += 1
                    right[g][ln[i + 1] if i < len(ln) - 1 else '$'] += 1
                s, e = split_end(ln)
                if s:
                    ends[s[-1]][e] += 1
    rows_out = []
    for g, n in tok.most_common():
        if n < 5:
            break
        e = ends[g]
        ne = sum(e.values())
        if g in ('817', '820', '861'):
            role = 'opener'
        elif g in ('740', '520', '400', '90', '151'):
            role = 'ending'
        elif g in NUMS:
            role = 'numeral'
        elif ne >= 5 and e['520'] / ne >= 0.2:
            role = '520-name'
        elif ne >= 5 and e['740'] / ne >= 0.9:
            role = '740-name'
        else:
            role = 'other'
        p = pos[g]
        rows_out.append({
            'sign': g, 'tokens': n, 'icit': ta[g], 'm77_added': tb[g],
            'initial': '%.0f%%' % (100 * p['i'] / n), 'medial': '%.0f%%' % (100 * p['m'] / n),
            'final': '%.0f%%' % (100 * p['f'] / n),
            'left': ' '.join('%s:%d' % kv for kv in left[g].most_common(3)),
            'right': ' '.join('%s:%d' % kv for kv in right[g].most_common(3)),
            'as_name_end_740': e['740'], 'as_name_end_520': e['520'],
            'numeral': ('%d %s' % (NUMS[g][0], NUMS[g][1])) if g in NUMS else '',
            'fish_series': 'yes' if g in FISH else '',
            'fairservis': ident.get(g, ''),
            'anchor': FIRM.get(g) or PROV.get(g, ''),
            'role': role})
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'sign_list.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows_out[0]), delimiter='\t')
        w.writeheader()
        w.writerows(rows_out)
    roles = Counter(r['role'] for r in rows_out)
    cover = Counter()
    for r in rows_out:
        cover[r['role']] += r['tokens']
    total = sum(tok.values())
    lines = ['# A structural sign list', '',
             '%d sign types with 5+ tokens (of %d types, %d tokens, ICIT-derived + M77 additions); they hold %.1f%% of all '
             'tokens. Full table: results/sign_list.tsv.' % (len(rows_out), len(tok), total,
                                                               100 * sum(r['tokens'] for r in rows_out) / total), '',
             '| role | signs | share of all tokens |', '|---|---|---|']
    for k in ('opener', 'ending', 'numeral', '520-name', '740-name', 'other'):
        lines.append('| %s | %d | %.1f%% |' % (k, roles[k], 100 * cover[k] / total))
    lines += ['', 'Signs with a firm meaning (copper-tablet equations): %s. Provisional: %s.' % (
        ', '.join('%s = %s' % kv for kv in FIRM.items()), ', '.join('%s = %s' % kv for kv in PROV.items())), '']
    with open(os.path.join(HERE, 'results', 'sign_list.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
