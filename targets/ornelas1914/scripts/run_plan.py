"""Run PLAN.md once: key tests for T1 (with the period clear copy), T1-R, T2, T2-P, T4, T5, T6.
AI-written (Claude Opus 5.5), 25 Nov 2026. PLAN.md is plan/PLAN_2026-11-25.md here; T2 is this telegram,
CMXV.35.3492.2-3. T1 and T4-T6 are other telegrams of catalogue 1462: they are part of the frozen run and are kept so
that the run can be repeated whole, but they are not part of this entry.

Copied on 27 Nov 2026 from the contributor's work folder. Two changes, neither touching a test: the inputs are read
from plan/frozen_run/ (see common.py), and the output is printed only, or written to a file given with --write
(the work folder wrote decodes/plan_run.txt). The filed output of the frozen run is plan/plan_run_2026-11-25.txt.

Usage, from the repository root:
  ALLEN_JSON=<path to Ashton Allen's decode-result.json> python3 -I targets/ornelas1914/scripts/run_plan.py
(see common.py for ALLEN_JSON and CYPHERSOLVER_REPO)"""
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def dec(key, g):
    return key.get(g, '?')


def permuted(key, rng):
    ks, vs = list(key), list(key.values())
    rng.shuffle(vs)
    return dict(zip(ks, vs))


def all_keys():
    g = C.grid_keys()
    words = C.clave0_words()
    k = {}
    k['K-ALLEN'] = C.allen_key()
    k['K-ALLEN-X'] = C.allen_x()
    for o in ('RC', 'CR'):
        c0 = dict(g[f'K-C0-{o}'])
        c0.update(words)
        k[f'K-C0-{o}'] = c0
        k[f'K-A1-{o}'] = g[f'K-A1-{o}']
        k[f'K-A2-{o}'] = g[f'K-A2-{o}']
        k[f'K-REY-{o}'] = g[f'K-REY-{o}']
    k21i, k21ii = C.alfabeto21()
    k['K-21I'], k['K-21II'] = k21i, k21ii
    k.update(C.syl_keys())
    return k


def ddn_layer(key, direction):
    p2c = C.ddn()
    m = p2c if direction == 'enc' else {c: p for p, c in p2c.items()}
    return {g: ''.join(m.get(ch, '?') for ch in v) for g, v in key.items()}


# ---------------- T1 ----------------

def t1_alignment():
    text = (C.INPUTS / 'transcription' / 'T1_3433-2-2_clearcopy.txt').read_text(encoding='utf-8').splitlines()[1]
    body = text.split('|', 1)[1]
    body = body.split('[image 2]')[0] + body.split('[image 2]')[1].split('|')[0]
    words = [C.norm(w) for w in body.replace('-|', '').replace('|', ' ').split()]
    words = [w for w in words if w]
    aligned, report, pos = [], [], 0
    for i, r in enumerate(C.runs('T1_3433')):
        lw = [C.norm(x) for x in r['left'].split()] if r['left'] else []
        rw = [C.norm(x) for x in r['right'].split()] if r['right'] else []
        # find left anchor (sequence of words) at or after pos
        def find(seq, start):
            for j in range(start, len(words) - len(seq) + 1):
                if words[j:j + len(seq)] == seq:
                    return j
            return None
        a = find(lw, pos) if lw else 0
        if a is None:
            report.append((i, r, 'left anchor not in copy', None))
            continue
        s = a + len(lw)
        b = find(rw, s) if rw else len(words)
        if b is None:
            report.append((i, r, 'right anchor not in copy', None))
            continue
        stretch = ''.join(words[s:b])
        n = len(r['groups'])
        ph = {'ch': '1', 'll': '2', 'rr': '3'}
        back = {v: k for k, v in ph.items()}
        variants = {stretch}
        for dg in ('ch', 'll', 'rr'):
            if dg in stretch:
                variants.add(stretch.replace(dg, ph[dg]))
        if len([d for d in ph if d in stretch]) > 1:
            v_all = stretch
            for dg in ph:
                v_all = v_all.replace(dg, ph[dg])
            variants.add(v_all)
        ok = sorted(v for v in variants if len(v) == n)
        if ok:
            v = ok[0]
            letters = [back.get(ch, ch) for ch in v]
            aligned.append((i, r['groups'], letters))
            report.append((i, r, 'aligned', ''.join(c if c not in back else back[c].upper() for c in v)))
            pos = b
        else:
            report.append((i, r, f'counts differ: {n} groups, {len(stretch)} letters', stretch))
            pos = b
    return aligned, report


def t1_tests(keys):
    say('== T1 CMXV.35.3433.1-2 (Dieguez), key tests against the clear copy 3433.2-2')
    aligned, report = t1_alignment()
    for i, r, status, st in report:
        say(f'  run {i}: {len(r["groups"])} groups, "{r["left"]}" .. "{r["right"]}": {status}' + (f' [{st}]' if st else ''))
    pairs = [(g, l) for _, gs, ls in aligned for g, l in zip(gs, ls)]
    say(f'  aligned groups: {len(pairs)}')
    order = ['K-ALLEN', 'K-ALLEN-X', 'K-C0-RC', 'K-C0-CR', 'K-A1-RC', 'K-A1-CR', 'K-A2-RC', 'K-A2-CR', 'K-REY-RC',
             'K-REY-CR', 'K-21I', 'K-21II', 'K-SYL-RC', 'K-SYL-CR']
    rng = random.Random(1462)
    for name in order:
        key = keys[name]
        A = sum(dec(key, g) == l for g, l in pairs) / len(pairs)
        ctrl = []
        for _ in range(1000):
            pk = permuted(key, rng)
            ctrl.append(sum(dec(pk, g) == l for g, l in pairs) / len(pairs))
        fit = A >= 0.80 and A > max(ctrl)
        say(f'  {name:10s} A={A:.3f} ctrl_max={max(ctrl):.3f} -> {"FITS" if fit else "miss"}')
    return pairs


def t1_recover(pairs):
    say('== T1-R key from the clear copy (aligned runs only)')
    tab = defaultdict(set)
    for g, l in pairs:
        tab[g].add(l)
    conflicts = {g: v for g, v in tab.items() if len(v) > 1}
    say(f'  distinct groups {len(tab)}, conflicts {len(conflicts)}: {sorted(conflicts.items())}')
    single = {g: next(iter(v)) for g, v in tab.items() if len(v) == 1 and len(g) == 2}
    # row families: merge tens digits whose shared units digits agree
    rows = defaultdict(dict)
    for g, l in single.items():
        rows[g[0]][g[1]] = l
    fam = {t: {t} for t in rows}
    contra = []
    ts = sorted(rows)
    for a in ts:
        for b in ts:
            if a >= b:
                continue
            shared = set(rows[a]) & set(rows[b])
            same = [u for u in shared if rows[a][u] == rows[b][u]]
            diff = [u for u in shared if rows[a][u] != rows[b][u]]
            if same and not diff:
                merged = fam[a] | fam[b]
                for t in merged:
                    fam[t] = merged
            if same and diff:
                contra.append((a, b, same, diff))
    fams = sorted({tuple(sorted(f)) for f in fam.values()})
    say(f'  tens-digit rows: {ts}; families from shared units: {fams}; contradictions {contra}')
    # letter -> units digit consistency
    lu = defaultdict(set)
    for g, l in single.items():
        lu[l].add(g[1])
    multi = {l: u for l, u in lu.items() if len(u) > 1}
    say(f'  letters seen with more than one units digit: {multi}')
    # family check: within each family the units digit must fix the letter
    bad = []
    for f in fams:
        cols = defaultdict(set)
        for t in f:
            for u, l in rows[t].items():
                cols[u].add(l)
        bad += [(f, u, v) for u, v in cols.items() if len(v) > 1]
    form = not conflicts and not bad and not contra
    say(f'  form structure (no conflict, families consistent): {form}; family conflicts: {bad}')
    proj = {}
    for f in fams:
        cols = {}
        for t in f:
            cols.update(rows[t])
        for t in f:
            for u, l in cols.items():
                proj[t + u] = l
    for g, v in tab.items():
        if len(g) == 3 and len(v) == 1:
            proj[g] = next(iter(v))
    say('  table (projected over families): ' + ' '.join(f'{g}={proj[g]}' for g in sorted(proj, key=lambda x: (len(x), x))))
    return proj if form else None


# ---------------- language-measured tests ----------------

def w_test(label, groups, keys, order, lex, require_all=False):
    rng = random.Random(1462)
    results = []
    for name in order:
        key = keys[name]
        text = ''.join(dec(key, g) for g in groups)
        W, seg = C.coverage(text, lex)
        undefined = sum(dec(key, g) == '?' for g in groups)
        ctrl = []
        for _ in range(1000):
            pk = permuted(key, rng)
            ctrl.append(C.coverage(''.join(dec(pk, g) for g in groups), lex)[0])
        fit = W >= 0.80 and W > max(ctrl) and (undefined == 0 or not require_all)
        say(f'  {name:16s} W={W:.3f} ctrl_max={max(ctrl):.3f} undefined={undefined}/{len(groups)} '
            f'-> {"FITS" if fit else "miss"} | {" ".join(seg)[:160]}')
        results.append((name, W, fit))
    return results


def main():
    keys = all_keys()
    lex = C.lexicon()
    say(f'lexicon words: {len(lex)}')
    pairs = t1_tests(keys)
    kdieg = t1_recover(pairs)

    say('== T2 CMXV.35.3492.2-3 (Ornelas)')
    g2 = [v for _, kind, v, _ in C.tokens('T2_3492') if kind == 'group']
    say(f'  groups {len(g2)}')
    keys['K-ALLEN-X+DDN-dec'] = ddn_layer(keys['K-ALLEN-X'], 'dec')
    keys['K-ALLEN-X+DDN-enc'] = ddn_layer(keys['K-ALLEN-X'], 'enc')
    order = ['K-ALLEN', 'K-ALLEN-X', 'K-ALLEN-X+DDN-dec', 'K-ALLEN-X+DDN-enc']
    if kdieg:
        keys['K-DIEG'] = kdieg
        order.append('K-DIEG')
    else:
        say('  K-DIEG not formed (T1-R table lacks the form structure)')
    order += ['K-C0-RC', 'K-C0-CR', 'K-A1-RC', 'K-A1-CR', 'K-A2-RC', 'K-A2-CR', 'K-REY-RC', 'K-REY-CR', 'K-21I',
              'K-21II', 'K-SYL-RC', 'K-SYL-CR']
    w_test('T2', g2, keys, order, lex)

    say('== T2-P pencil line as a crib')
    for crib in ('esciertoquevieneestamigeneralavila', 'ezciertoquevieneestamigeneralavila'):
        ok = []
        for p in range(len(g2) - len(crib) + 1):
            m, rev, bad = {}, {}, False
            for g, l in zip(g2[p:p + len(crib)], crib):
                if m.setdefault(g, l) != l:
                    bad = True
                    break
            if not bad:
                ok.append(p)
        say(f'  crib {crib}: consistent positions (no group with two letters): {ok}')

    say('== T4 CMXV.18.1770.1-4 (to Bonilla), ten-digit runs as five two-digit groups')
    runs4 = [v for _, kind, v, _ in C.tokens('T4_1770') if kind == 'group']
    g4 = [r[i:i + 2] for r in runs4 for i in range(0, len(r), 2)]
    say(f'  groups {g4}')
    w_test('T4', g4, keys, ['K-A2-RC', 'K-A2-CR', 'K-A1-RC', 'K-A1-CR', 'K-REY-RC', 'K-REY-CR', 'K-21I', 'K-21II',
                            'K-C0-RC', 'K-C0-CR', 'K-SYL-RC', 'K-SYL-CR', 'K-ALLEN-X'], lex, require_all=True)

    say('== T5 CMXV.14.1354.1 (Luque)')
    g5 = [v for _, kind, v, _ in C.tokens('T5_1354') if kind == 'group']
    for name in ['K-C0-RC', 'K-C0-CR', 'K-SYL-RC', 'K-SYL-CR']:
        key = keys[name]
        vals = [dec(key, g) for g in g5]
        have = sum(v != '?' for v in vals)
        say(f'  {name}: {have}/{len(g5)} numbers have a value ({have / len(g5):.2f})')
        frame = []
        for line, kind, v, _ in C.tokens('T5_1354'):
            frame.append(v.upper() if kind == 'clear' else f'[{v}={dec(key, v)}]')
        say('    ' + ' '.join(frame))

    say('== T6 CMXV.17.1648.2-3 (Gabriel)')
    toks = C.tokens('T6_1648')
    lk = C.letter_keys()
    clear = {'hijo', 'urgele', 'hablar', 'con', 'preguntele', 'si', 'va', 'aqui'}
    cipher_runs, cur = [], []
    for _, kind, v, _ in toks:
        if v in clear:
            if cur:
                cipher_runs.append(''.join(cur))
                cur = []
        else:
            cur.append(v)
    if cur:
        cipher_runs.append(''.join(cur))
    say(f'  coded runs (typed groups joined between clear words): {cipher_runs}')
    rng = random.Random(1462)
    for name, (kind, key) in lk.items():
        def apply(k, run):
            if kind == 'di':
                return ''.join(k.get(run[i:i + 2], '?') for i in range(0, len(run) - 1, 2)) + ('?' if len(run) % 2 else '')
            return ''.join(k.get(ch, ch if kind == 'swap' else '?') for ch in run)
        text = ''.join(apply(key, r) for r in cipher_runs)
        W, seg = C.coverage(text, lex)
        ctrl = [C.coverage(''.join(apply(permuted(key, rng), r) for r in cipher_runs), lex)[0] for _ in range(1000)]
        fit = W >= 0.80 and W > max(ctrl)
        say(f'  {name:10s} W={W:.3f} ctrl_max={max(ctrl):.3f} -> {"FITS" if fit else "miss"} | {" ".join(seg)[:150]}')

    if '--write' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--write') + 1])
        with open(out, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
