"""Re-score the two declared replacement tests (Pinckney 1795 "Cypher 2d", Eaton 25 May 1801) with the frozen key.

Self-contained: reads only files in this bundle. The measure is the one declared in PREREGISTRATION_eaton_1802-10-22.md
(replacement tests): over interlined groups that the frozen key covers and whose interlinear placement the transcriber
marked clear, the share where the key value equals the interlinear word (or the word begins with it, for a group with an
inflection mark) or, for a word written over several groups, is contained in that word (letters only). A word and the
dash rows after it are one unit, as in key/scripts/code16_merge_v3_2026_11_10.py. Baseline: the key's values dealt at
random to its groups, 200 shuffles.

The original scoring runs of 10 Nov 2026 were not kept as a script; this is a re-implementation written for the
bundle. Its numbers are printed next to the recorded ones (tests/*_frozen_key_v1_result.json) so any difference shows.

    python3 tests/rescore_frozen_key.py        (from targets/legation1788/beling)
"""
import csv, json, random, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.parent
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())


def tok(t):
    m = re.fullmatch(r'(\d+)(\+\+|\+|\^)?', t.strip())
    return (int(m.group(1)), m.group(2) or '') if m else None


def units(path):
    """(word letters, [(group, mark)]) for clear interlined units; dash rows join the unit before them."""
    out, cur = [], None
    def flush():
        nonlocal cur
        if cur and cur['ok'] and cur['w']:
            out.append((cur['w'], cur['gs']))
        cur = None
    for r in csv.DictReader(open(path), delimiter='\t'):
        if r['kind'].strip() != 'interlinear':
            flush(); continue
        w = r['interlinear'].strip()
        gs = [tok(x) for x in r['groups'].split()]
        good = r['placement'].strip() == 'clear' and gs and all(gs)
        if re.fullmatch(r'[—–\-\s.]+', w):
            if cur:
                if good: cur['gs'] += gs
                else: cur['ok'] = False
            continue
        flush()
        if ' ' in w.strip():                    # several words drifting over a run: not a word-to-group unit
            continue
        cur = dict(w=norm(re.sub(r'\[.*?\]', '', w)), gs=gs if good else [], ok=good)
    flush()
    return out


def score(us, key):
    tested = fit = 0; miss = []
    for w, gs in us:
        for g, mark in gs:
            if g not in key: continue
            v = norm(key[g])
            if not v: continue
            tested += 1
            ok = bool((w == v or (mark and w.startswith(v))) if len(gs) == 1 else (v in w))
            fit += ok
            if not ok: miss.append((g, key[g], w))
    return tested, fit, miss


def main():
    key = {int(r['group']): r['value'] for r in csv.DictReader(open(HERE / 'frozen_key_v1.tsv'), delimiter='\t')}
    tests = [('Pinckney 1795, M31 roll 7 frames 0018-0021', B / 'witnesses/pinckney_1795_madrid/spans.tsv', HERE / 'pinckney1795_frozen_key_v1_result.json'),
             ('Eaton 25 May 1801, T303 roll 2 frame 0049', B / 'witnesses/eaton_1801-05-25/spans.tsv', HERE / 'eaton1801_frozen_key_v1_result.json')]
    res = {}
    for name, sp, rec in tests:
        us = units(sp)
        t, f, miss = score(us, key)
        rng = random.Random(20261110); gl = sorted(key); vl = [key[g] for g in gl]; base = []
        for _ in range(200):
            sh = vl[:]; rng.shuffle(sh)
            tt, ff, _ = score(us, dict(zip(gl, sh))); base.append(ff / tt if tt else 0)
        r0 = json.load(open(rec))
        res[name] = dict(tested=t, fit=f, share=round(f / t, 3), shuffled_mean=round(sum(base) / len(base), 3), shuffled_max=round(max(base), 3),
                         pass_rule=f / t >= 0.85 and f / t - max(base) >= 0.30, misfits=miss,
                         recorded=dict(tested=r0['tested'], fit=r0['fit'], share=r0['share'], shuffled_max=r0['shuffled_max'], pass_rule=r0['pass_rule']))
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
