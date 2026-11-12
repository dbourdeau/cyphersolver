"""sande1660 cipher A, round 2: the pre-registered test of key.txt on the rest of cipher A (see ../PREREG_round2.md).

    python3 -I scripts/test_round2.py          (run from beling/; writes results/test_round2_result.json and
                                               results/test_round2_output.txt)

Standard library only. The key parser, normaliser, lexicon, coverage and scoring functions are those of
scripts/test_m0271.py, loaded from that file unchanged. New here: clear words in braces {...} break a line like a
code group; lines sharing a run of 6+ tokens with a build line are left out; several files are scored together.
Inputs (frozen in results/frozen_inputs_round2.sha256).
"""
import importlib.util
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 1660
N_SHUFFLED = 200
MIN_LETTERS = 600
RUN = 6
NEW_FILES = ['m0272.txt', 'm0265_rest.txt', 'm0266_rest.txt', 'm0267.txt', 'm0269_rest.txt', 'm0273_top.txt']
SECONDARY = 'm0271_r2.txt'

_spec = importlib.util.spec_from_file_location('t1', os.path.join(HERE, 'scripts', 'test_m0271.py'))
t1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t1)


def load_lines(path):
    """[(tag, tokens, n_unread, n_clear)]. Tokens: int, or None for a break ('?', a blot mark, or clear words)."""
    out = []
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            if not raw.startswith('@'):
                continue
            tag, body = raw.rstrip('\n').split(' ', 1)
            n_clear = len(re.findall(r'\{[^}]*\}', body))
            body = re.sub(r'\{[^}]*\}', '|{}|', body)
            toks, n_unread = [], 0
            for t in re.split(r'[.|]', body):
                t = t.strip().rstrip('*')
                if not t:
                    continue
                if t.isdigit():
                    toks.append(int(t))
                else:
                    toks.append(None)
                    if t != '{}':
                        n_unread += 1
            out.append((tag, toks, n_unread, n_clear))
    return out


def runs(toks, n=RUN):
    s = set()
    for i in range(len(toks) - n + 1):
        w = toks[i:i + n]
        if None not in w:
            s.add(tuple(w))
    return s


def main():
    key = t1.load_key(os.path.join(HERE, 'key', 'key.txt'))
    assert len(key) == 26, len(key)
    lex = t1.load_lexicon(os.path.join(HERE, 'lexicon', 'pt.json.gz'))
    build = t1.load_lines(os.path.join(HERE, 'key', 'transcription_build.txt'))
    build_runs = set()
    for _, toks in build:
        build_runs |= runs(toks)
    s_build, n_build, _ = t1.score(build, key, lex)

    held, excluded, per_file, stats = [], [], {}, {}
    for f in NEW_FILES:
        lines = load_lines(os.path.join(HERE, 'transcription', f))
        keep = []
        for tag, toks, nu, nc in lines:
            if runs(toks) & build_runs:
                excluded.append(tag)
            else:
                keep.append((tag, toks))
        per_file[f] = keep
        tk = [t for _, ts in keep for t in ts]
        stats[f] = {'lines_kept': len(keep), 'lines_excluded': len(lines) - len(keep),
                    'tokens': sum(1 for t in tk if t is not None) + sum(nu for tg, _, nu, _ in lines
                                                                       if tg not in excluded),
                    'unread': sum(nu for tg, _, nu, _ in lines if tg not in excluded),
                    'clear_spans': sum(nc for tg, _, _, nc in lines if tg not in excluded)}
        held.extend(keep)

    s_new, n_new, rows = t1.score(held, key, lex, detail=True)
    for f in NEW_FILES:
        s, n, _ = t1.score(per_file[f], key, lex)
        stats[f].update({'letters': n, 'S': round(s, 4)})

    rng = random.Random(SEED)
    syms = sorted(key)
    vals = [key[s] for s in syms]
    null = []
    for _ in range(N_SHUFFLED):
        v = vals[:]
        rng.shuffle(v)
        null.append(t1.score(held, dict(zip(syms, v)), lex)[0])
    best_null = max(null)
    threshold = 0.85 * s_build
    margin = s_new - best_null
    too_small = n_new < MIN_LETTERS
    passed = (not too_small) and s_new >= threshold and margin >= 0.30

    sec = [(tg, ts) for tg, ts, _, _ in load_lines(os.path.join(HERE, 'transcription', SECONDARY))]
    s_sec, n_sec, sec_rows = t1.score(sec, key, lex, detail=True)

    toks = [t for _, ts in held for t in ts if t is not None]
    unkeyed = {}
    for t in toks:
        if t < 60 and t not in key:
            unkeyed[t] = unkeyed.get(t, 0) + 1
    groups = {}
    for t in toks:
        if t >= 60:
            groups[t] = groups.get(t, 0) + 1
    result = {
        'key_numbers': len(key), 'lexicon_skeletons': len(lex),
        'build_lines': len(build), 'build_letters': n_build, 'S_build': round(s_build, 4),
        'new_lines': len(held), 'new_lines_excluded': excluded, 'new_letters': n_new, 'S_new': round(s_new, 4),
        'threshold_0.85xS_build': round(threshold, 4),
        'shuffled_n': N_SHUFFLED, 'seed': SEED, 'mean_shuffled': round(sum(null) / len(null), 4),
        'best_shuffled': round(best_null, 4), 'margin': round(margin, 4),
        'too_small': too_small, 'pass': passed,
        'per_file': stats,
        'new_code_group_tokens': sum(groups.values()), 'new_code_groups': dict(sorted(groups.items())),
        'new_unkeyed_below_60': dict(sorted(unkeyed.items())),
        'secondary_m0271_r2': {'lines': len(sec), 'letters': n_sec, 'S': round(s_sec, 4)},
    }
    with open(os.path.join(HERE, 'results', 'test_round2_result.json'), 'w', encoding='utf-8') as fh:
        json.dump(result, fh, indent=1)
        fh.write('\n')
    with open(os.path.join(HERE, 'results', 'test_round2_output.txt'), 'w', encoding='utf-8') as fh:
        fh.write('# Round 2 under the frozen key, line by line. Segments: the raw decrypt (# = number the key '
                 'lacks), then the normalised parse (UPPER = lexicon word of 3+ letters, lower = not covered).\n'
                 '# Code groups, ? and clear words break the line and are not shown here; see the transcription.\n')
        fh.write('# Excluded (share a run of %d tokens with a build line): %s\n' % (RUN, ', '.join(excluded) or 'none'))
        for tag, segs, parses, lc, lt in rows + [('--- secondary: m0271_r2', [], [], 0, 0)] + sec_rows:
            if not segs and tag.startswith('---'):
                fh.write('\n%s\n' % tag)
                continue
            fh.write('%s  %d/%d\n  raw:   %s\n  parse: %s\n' % (tag, lc, lt, ' | '.join(segs), ' | '.join(parses)))
        fh.write('\nshuffled-key scores (sorted): %s\n' % ', '.join('%.3f' % x for x in sorted(null)))
    print(json.dumps(result))


if __name__ == '__main__':
    sys.exit(main())
