#!/usr/bin/env python3
"""Graham to Madison, New Orleans, 2 Jan 1806: is the letter in Weber's code WE023?

Reads transcription_2jan1806.txt (the code groups with Jacob Wagner's interlinear words) and writes results.json and
key_direct.tsv. Standard library only.

    python3 verify.py                      # the parts that need no published table
    python3 verify.py --weber TABLE.tsv    # also the table test

Weber's tables are not in this repository (Ralph E. Weber, United States Diplomatic Codes and Ciphers, 1775-1938,
Chicago 1979; WE023 is the code printed on pp. 419-30). To run the table test, transcribe the tables you want to try
from a library copy into one tab-separated file with a header line and the columns code, number, element
(e.g. "WE023<TAB>28<TAB>people"). Elements such as "I. J." stand for either letter. Nothing from the table is written
to the output files: results.json gives counts only, key_direct.tsv gives Wagner's words only.

Seeds are fixed per section and per table, so the figures do not depend on which other tables the file holds.
"""
import argparse, collections, hashlib, itertools, json, pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
NULL_MIN = 1594          # WE023 runs 1-1593; Graham's 1590-1700 groups carry no interlinear word
SUFFIX = ['', 's', 'es', 'ed', 'd', 'e', 'n', 'en']   # what Graham's caret may add
NOV22 = [10, 19, 30, 33, 35, 36, 39, 41, 51, 61, 65, 77, 18, 46, 54, 67, 71, 73]   # 12 open + 6 conjectured
N_CTRL = 200


def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())


def parse():
    runs = []
    for line in (HERE / 'transcription_2jan1806.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        frame, rid, rest = line.split(' ', 2)
        spans = []
        for m in re.finditer(r'\{([^}]*)\}(\S*)', rest):
            toks = [{'g': None if t == 'X' else int(re.sub(r'\D', '', t)), 'caret': '^' in t,
                     'doubt': '?' in t or t == 'X'} for t in m.group(1).split()]
            spans.append({'toks': toks, 'word': m.group(2)})
        runs.append({'frame': frame, 'run': rid, 'spans': spans})
    return runs


def usable(span):
    return bool(span['word']) and all(not t['doubt'] for t in span['toks']) and all(t['g'] < NULL_MIN for t in span['toks'])


def load_tables(path):
    t = collections.defaultdict(dict)
    for i, line in enumerate(pathlib.Path(path).read_text().splitlines()):
        if i == 0 or not line.strip():
            continue
        code, num, el = line.split('\t')[:3]
        if num.isdigit():
            t[code][int(num)] = el
    return t


def cands(el):
    if el is None or norm(el) == '':
        return None
    parts = [norm(p) for p in re.split(r'[.,]\s*', el) if norm(p)]
    if len(parts) > 1 and all(len(p) == 1 for p in parts):
        return set(parts)
    return {norm(el)}


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def span_score(span, table):
    """(strict, lenient): the table's elements at the span's numbers spell Wagner's word (lenient: within one letter)"""
    w = norm(span['word'])
    sets = []
    for t in span['toks']:
        c = cands(table.get(t['g']))
        if c is None:
            return False, False
        sets.append(c)
    caret = any(t['caret'] for t in span['toks'])
    best = 99
    for combo in itertools.product(*sets):
        s = ''.join(combo)
        if any(s + suf == w for suf in (SUFFIX if caret else [''])):
            return True, True
        best = min(best, lev(s, w))
    return False, best <= 1


def table_score(spans, table):
    st = le = 0
    for s in spans:
        a, b = span_score(s, table)
        st += a
        le += b
    return st, le


def direct_key(runs):
    votes = collections.defaultdict(collections.Counter)
    for r in runs:
        for s in r['spans']:
            if usable(s) and len(s['toks']) == 1:
                votes[s['toks'][0]['g']][norm(s['word'])] += 1
    return {g: c.most_common(1)[0][0] for g, c in votes.items()}, votes


def heldout(train, test, rng):
    key, _ = direct_key(train)
    pairs = [(s['toks'][0]['g'], norm(s['word'])) for r in test for s in r['spans'] if usable(s) and len(s['toks']) == 1]
    covered = [(g, w) for g, w in pairs if g in key]
    hit = sum(key[g] == w for g, w in covered)
    gs = list(key)
    ctrl = []
    for _ in range(N_CTRL):
        vals = [key[g] for g in gs]
        rng.shuffle(vals)
        k2 = dict(zip(gs, vals))
        ctrl.append(sum(k2[g] == w for g, w in covered))
    return {'test_tokens': len(pairs), 'covered': len(covered), 'correct': hit, 'control_mean': round(sum(ctrl) / N_CTRL, 2),
            'control_max': max(ctrl), 'controls_at_or_above': sum(c >= hit for c in ctrl), 'n_controls': N_CTRL}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--weber', help='tab-separated file code/number/element transcribed from Weber 1979 (not in this repository)')
    a = ap.parse_args()

    runs = parse()
    spans = [s for r in runs for s in r['spans'] if usable(s)]
    toks = [t for r in runs for s in r['spans'] for t in s['toks']]
    out = {'transcription_sha256': hashlib.sha256((HERE / 'transcription_2jan1806.txt').read_bytes()).hexdigest(),
           'runs': len(runs), 'groups': len(toks),
           'groups_1594_up': sum(1 for t in toks if t['g'] and t['g'] >= NULL_MIN),
           'groups_doubtful_or_unreadable': sum(t['doubt'] for t in toks),
           'distinct_groups': len({t['g'] for t in toks if t['g']}),
           'usable_words': len(spans)}

    # 1. crib key from Wagner's words alone: built on frames 0006-0008, tested on 0009-0011 and the reverse
    A = [r for r in runs if r['frame'] in ('0006', '0007', '0008')]
    B = [r for r in runs if r['frame'] in ('0009', '0010', '0011')]
    out['heldout_A_to_B'] = heldout(A, B, random.Random('heldout-AB-18060102'))
    out['heldout_B_to_A'] = heldout(B, A, random.Random('heldout-BA-18060102'))

    key, votes = direct_key(runs)
    lines = ['group\twagner_word\tn']
    lines += [f'{g}\t{key[g]}\t{sum(votes[g].values())}' for g in sorted(key)]
    kt = '\n'.join(lines) + '\n'
    (HERE / 'key_direct.tsv').write_text(kt)
    out['key_direct'] = {'file': 'key_direct.tsv', 'sha256': hashlib.sha256(kt.encode()).hexdigest(), 'values': len(key),
                         'conflicts': {str(g): dict(c) for g, c in votes.items() if len(c) > 1}}

    # 2. the [22 Nov] 1806 numbers: does the January crib key give any of them?
    out['nov22_numbers_in_crib_key'] = [g for g in NOV22 if g in key]
    low = [t['g'] for t in toks if t['g'] and t['g'] <= 77]
    out['jan_groups_le_77'] = {'count': len(low), 'of': sum(1 for t in toks if t['g']), 'values': sorted(set(low))}
    out['p_18_distinct_all_le_77_if_uniform_1_1593'] = (77 / 1593) ** 18

    # 3. table test (needs Weber's tables, supplied by the reader)
    if a.weber:
        tables = load_tables(a.weber)
        out['weber_file_sha256'] = hashlib.sha256(pathlib.Path(a.weber).read_bytes()).hexdigest()
        res = {}
        for code in sorted(tables):
            rng = random.Random('table-' + code + '-18060102')
            st, le = table_score(spans, tables[code])
            ctrl = []
            for _ in range(N_CTRL):
                vals = list(tables[code].values())
                rng.shuffle(vals)
                ctrl.append(table_score(spans, dict(zip(tables[code], vals))))
            res[code] = {'size': len(tables[code]), 'strict': st, 'lenient': le, 'of': len(spans),
                         'ctrl_strict_max': max(c[0] for c in ctrl), 'ctrl_lenient_max': max(c[1] for c in ctrl),
                         'ctrl_lenient_mean': round(sum(c[1] for c in ctrl) / N_CTRL, 2)}
        out['table_test'] = res
        if 'WE023' in tables:
            we = tables['WE023']
            sa = [s for r in A for s in r['spans'] if usable(s)]
            sb = [s for r in B for s in r['spans'] if usable(s)]
            best = sorted(tables, key=lambda c: -table_score(sa, tables[c])[1])[0]
            out['table_chosen_on_0006_0008'] = best
            out['its_score_on_0009_0011'] = dict(zip(['strict', 'lenient'], table_score(sb, tables[best])), of=len(sb))
            out['crib_key_values_agreeing_with_WE023'] = sum(1 for g, v in key.items() if cands(we.get(g)) and v in cands(we.get(g)))
            out['nov22_numbers_with_a_WE023_element'] = sum(1 for g in NOV22 if g in we)
    else:
        out['table_test'] = 'not run: no --weber file (Weber 1979 is not in this repository; see the docstring)'

    (HERE / 'results.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'key_direct'}, indent=1)[:3000])


if __name__ == '__main__':
    main()
