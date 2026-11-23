#!/usr/bin/env python3
"""Independent held-out scorer for Delacroix 1797 (reviewer's own code; see REVIEW_PLAN_heldout.md).
usage: my_heldout.py CIPHER TESTTEXT FROZEN_TABLE.json MANUAL_ALIGNMENT [BOUNDARY]"""
import json, random, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))

def groups(path):
    out = []
    for l in open(path):
        l = l.strip()
        if l and not l.startswith('#') and not l.startswith('frame'):
            out += [int(x) for x in l.split()]
    return out

def best_fits(cip, text, table, maxlen=15):
    n, m = len(cip), len(text)
    NEG = -10**9
    f = [[NEG] * (m + 1) for _ in range(n + 1)]
    f[0][0] = 0
    for i in range(n):
        ch = table.get(cip[i])
        row, nxt = f[i], f[i + 1]
        for j in range(m + 1):
            v = row[j]
            if v == NEG: continue
            for k in range(0, min(maxlen, m - j) + 1):
                if nxt[j + k] < v: nxt[j + k] = v
            if ch and text.startswith(ch, j):
                if nxt[j + len(ch)] < v + 1: nxt[j + len(ch)] = v + 1
    return f[n][m]

def main():
    cip_p, txt_p, tab_p, man_p = sys.argv[1:5]
    cip = groups(cip_p)
    text = ''.join(norm(l) for l in open(txt_p, encoding='utf-8') if l.strip() and not l.startswith('#'))
    tab = {int(g): v['chunk'] for g, v in json.load(open(tab_p))['table'].items()}
    # hand alignment: letters per group
    man = []
    for l in open(man_p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        for t in l.split():
            if t.startswith('~'): continue
            g, val = t.split('=', 1)
            man.append((int(g), val.split('!')[0]))
    assert [g for g, _ in man] == cip, 'hand alignment groups differ from cipher'
    man_letters = lambda v: '' if v in ('0', '.', '?') else v
    b_hand = sum(len(man_letters(v)) for _, v in man[:568])
    b = int(sys.argv[5]) if len(sys.argv) > 5 else 1928
    held_c, held_t = cip[568:], text[b:]
    pred = sum(1 for g in held_c if g in tab)
    fits = best_fits(held_c, held_t, tab)
    rng = random.Random(22112026)
    gs, cs = list(tab), list(tab.values())
    ctrl = []
    for _ in range(1000):
        sh = cs[:]; rng.shuffle(sh)
        ctrl.append(best_fits(held_c, held_t, dict(zip(gs, sh))))
    ctrl.sort()
    # simple check against the hand alignment
    agree = [(g, tab[g], v) for g, v in man[568:] if g in tab]
    same = sum(1 for g, t, v in agree if t == man_letters(v))
    out = dict(total_letters=len(text), boundary_used=b, boundary_from_hand_alignment=b_hand,
               held_letters=len(held_t), table_entries=len(tab), predictions=pred, fits=fits,
               fit_share=fits / pred, ctrl_mean=sum(ctrl) / len(ctrl), ctrl_p99=ctrl[989], ctrl_max=ctrl[-1],
               hand_alignment_predictions=len(agree), hand_alignment_agree=same,
               hand_alignment_disagreements=[(g, t, v) for g, t, v in agree if t != man_letters(v)])
    out['pass'] = pred >= 40 and fits / pred >= 0.70 and fits > out['ctrl_p99']
    print(json.dumps(out, indent=1))

main()
