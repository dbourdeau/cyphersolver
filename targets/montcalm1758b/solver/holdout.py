"""Hold-out test (rule fixed before running; no tuning afterwards).

RULE
 1. For each letter L of a code, run solve.py on the OTHER letters of that code only
    (seed 1, 600 sweeps, KMAX=20, all other settings as in the main runs).
 2. Table = for each group, its most frequent aligned value in that run (ties: the
    longer value, then alphabetical). Nulls count as values ("").
 3. Decode L group by group with that table. Words printed in clear inside the figure
    stream are copied as printed. A group absent from the table decodes to nothing
    and is counted as unknown.
 4. Score = characters of the printed clear text (letters/digits only, accents removed)
    matched by the decoded string, using difflib.SequenceMatcher (autojunk off),
    divided by the length of the printed clear text.
    Also reported: share of groups known to the table; and a chance baseline = the same
    score after randomly permuting the table values among the table's groups (mean of
    20 permutations, fixed seed 0).

usage: python3 -I holdout.py OUTDIR code_letter_files...
"""
import sys, os, json, random, difflib
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('KMAX', '20')
import solve
from common import parse

def table_from(res):
    c = defaultdict(Counter)
    for u in res:
        for kind, g, page, v, j in (u['align'] or []):
            if kind == 'g':
                c[g][v] += 1
    tab = {}
    for g, cnt in c.items():
        tab[g] = sorted(cnt.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))[0][0]
    return tab

def decode(path, tab):
    d = parse(path)
    out = []; known = 0; total = 0; clear = ''
    for u in d['units']:
        clear += u['text']
        for kind, g, page, line in u['groups']:
            if kind == 'w':
                out.append(g); continue
            total += 1
            if g in tab:
                known += 1; out.append(tab[g])
    return ''.join(out), clear, known, total

def score(dec, clear):
    sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / max(1, len(clear))

if __name__ == '__main__':
    outdir = sys.argv[1]; files = sys.argv[2:]
    os.makedirs(outdir, exist_ok=True)
    lines = []
    for f in files:
        name = os.path.basename(f).split('.')[0]
        train = [x for x in files if x != f]
        res = solve.run(train, 1, 600)
        json.dump(res, open(os.path.join(outdir, f'holdout_train_without_{name}.json'), 'w'), ensure_ascii=False)
        tab = table_from(res)
        dec, clear, known, total = decode(f, tab)
        s = score(dec, clear)
        rng = random.Random(0)
        keys = list(tab); base = []
        for _ in range(20):
            vals = [tab[k] for k in keys]; rng.shuffle(vals)
            ptab = dict(zip(keys, vals))
            d2, c2, _, _ = decode(f, ptab)
            base.append(score(d2, c2))
        line = (f'{name}: trained on {",".join(os.path.basename(x).split(".")[0] for x in train)}; '
                f'groups known {known}/{total} ({known/max(1,total):.1%}); '
                f'clear-text chars matched {s:.1%}; chance baseline {sum(base)/len(base):.1%}')
        print(line, flush=True)
        lines.append(line)
        open(os.path.join(outdir, f'holdout_decode_{name}.txt'), 'w').write(dec + '\n\nPRINTED:\n' + clear + '\n')
    open(os.path.join(outdir, 'holdout_lines.txt'), 'w').write('\n'.join(lines) + '\n')
