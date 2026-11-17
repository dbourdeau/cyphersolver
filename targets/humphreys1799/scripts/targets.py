"""Read the target transcriptions (../transcriptions/no214_*.txt, no188_*.txt): code lines are lines of numbers,
optionally with [?] marks. Prints coverage against a table (../pairs.tsv majority values, or a frozen table given
as argv[1]) and a decode with [group] for unknowns. Usage: python3 -I targets.py [table.tsv] [passfile ...]"""
import os, re, sys, collections, csv
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def load_table(p=None):
    t = {}
    if p:
        for r in csv.reader(open(p), delimiter='\t'):
            if r and not r[0].startswith('#') and r[0] != 'group': t[r[0]] = r[1]
        return t
    d = collections.defaultdict(collections.Counter)
    for r in csv.DictReader(open(BASE + '/key/pairs_build_v1.tsv'), delimiter='\t'):
        if r['uncertain'] == 'g' or r['value'] in ('?', ''): continue
        d[r['group']][r['value']] += 1
    return {g: c.most_common(1)[0][0] for g, c in d.items()}
def read_target(p):
    seq = []  # (passage, token)
    cur = '?'
    for line in open(p):
        s = line.strip()
        if not s or s.startswith('#'): continue
        m = re.match(r'^([a-z])\s', s)
        if m: cur = m.group(1); continue
        if s.startswith('{'): seq.append((cur, '|')); continue
        toks = s.split()
        if all(re.fullmatch(r'[\d\[\]?]+', t) for t in toks):
            for t in toks: seq.append((cur, t))
    return seq
if __name__ == '__main__':
    args = sys.argv[1:]
    tab = load_table(args[0]) if args and args[0].endswith('.tsv') else load_table()
    files = [a for a in args if not a.endswith('.tsv')] or [BASE + '/transcriptions/no214_pass1.txt', BASE + '/transcriptions/no188_pass1.txt']
    for f in files:
        seq = read_target(f)
        groups = [t for _, t in seq if t != '|']
        known = [t for t in groups if t in tab]
        print(f'== {os.path.basename(f)}: {len(groups)} groups, {len(known)} in table ({len(known)/max(1,len(groups)):.0%}); distinct {len(set(groups))}, known distinct {len(set(known))}')
        out, last = [], None
        for p, t in seq:
            if p != last: out.append(f'\n[{p}] '); last = p
            if t == '|': out.append(' // '); continue
            out.append(tab[t] if t in tab else f'[{t}]')
            out.append(' ')
        print(''.join(out))
