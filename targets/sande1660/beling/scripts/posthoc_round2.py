"""sande1660 round 2, POST-HOC (not pre-registered): the same score on all new lines.

The pre-registered exclusion rule (a run of 6+ tokens shared with a build line) was meant to catch lines that are
physically the same as build lines. It caught 72 of 168 lines, nearly all because the letter text repeats common
phrases (que, porque, Sua [72] ...). Only one is a physical overlap: m0269.12 (18 tokens in a row equal to build
m0269.12). This script scores all new lines but that one, and the 71 lines the rule left out on their own, with the
same key, lexicon, rule and null (200 shuffles, seed 1660). It does not replace the pre-registered result.

    python3 -I scripts/posthoc_round2.py      (run from beling/; writes results/posthoc_round2.json and
                                              results/posthoc_round2_maxrun.txt)
"""
import importlib.util
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location('t2', os.path.join(HERE, 'scripts', 'test_round2.py'))
t2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t2)
t1 = t2.t1
PHYSICAL_OVERLAP = {'@m0269.12'}


def longest_run(a, b):
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] is not None and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best


def null_scores(lines, key, lex):
    rng = random.Random(t2.SEED)
    syms = sorted(key)
    vals = [key[s] for s in syms]
    out = []
    for _ in range(t2.N_SHUFFLED):
        v = vals[:]
        rng.shuffle(v)
        out.append(t1.score(lines, dict(zip(syms, v)), lex)[0])
    return out


def main():
    key = t1.load_key(os.path.join(HERE, 'key', 'key.txt'))
    lex = t1.load_lexicon(os.path.join(HERE, 'lexicon', 'pt.json.gz'))
    build = t1.load_lines(os.path.join(HERE, 'key', 'transcription_build.txt'))
    s_build = t1.score(build, key, lex)[0]
    build_runs = set()
    for _, toks in build:
        build_runs |= t2.runs(toks)
    allnew, ruled_out, rows = [], [], []
    for f in t2.NEW_FILES:
        for tag, toks, _, _ in t2.load_lines(os.path.join(HERE, 'transcription', f)):
            m, mt = max((longest_run(toks, bt), btag) for btag, bt in build)
            rows.append('%s %s longest run shared with build: %d (%s)' % (f, tag, m, mt))
            if tag in PHYSICAL_OVERLAP:
                continue
            allnew.append((tag, toks))
            if t2.runs(toks) & build_runs:
                ruled_out.append((tag, toks))
    res = {'S_build': round(s_build, 4), 'threshold_0.85xS_build': round(0.85 * s_build, 4)}
    for name, lines in (('all_new_but_m0269.12', allnew), ('only_the_lines_the_rule_left_out', ruled_out)):
        s, n, _ = t1.score(lines, key, lex)
        null = null_scores(lines, key, lex)
        res[name] = {'lines': len(lines), 'letters': n, 'S': round(s, 4),
                     'mean_shuffled': round(sum(null) / len(null), 4), 'best_shuffled': round(max(null), 4),
                     'margin': round(s - max(null), 4)}
    with open(os.path.join(HERE, 'results', 'posthoc_round2.json'), 'w', encoding='utf-8') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    with open(os.path.join(HERE, 'results', 'posthoc_round2_maxrun.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(rows) + '\n')
    print(json.dumps(res))


if __name__ == '__main__':
    sys.exit(main())
