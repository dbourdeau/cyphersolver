"""The one run of TEST_PLAN_2857.md: George Lasry's Esp. 318 no. 95 key applied unchanged to catalogue 2857.

  python3 -I test2857.py <transcription_reconciled.txt> <signsheet_K_private_map.json> <claver_tsv> <pulgar_txt> <outdir>

Values: each K tile was cut from Lasry's key image (esp318_1497_key.png); an alphabet tile's value is the letter of
the column it was cut from. Specials and code groups take Lasry's labels. N03, [bnm] and '#' have no value.
Measure: wl2857.sandwich_measure (LMIN 3) with the word list wl2857.build_claver_pulgar_long(..., 4, 5), U = 10.
Control: 1,000 tables with the letter values permuted among the 44 alphabet tiles (random.Random(2857)).
"""
import sys, os, json, random, re
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wl2857

rec, pmap, ctsv, ptxt, out = sys.argv[1:6]
priv = json.load(open(pmap))
CODES = {'bac': 'ciudad', 'bcd': 'cardenal', 'bnh': 'rey', 'bon': 'gente', 'dae': 'papa', 'dif': 'rey de romanos?',
         'boo': 'Name5?', 'dah': 'Name2?', 'dal': 'Name3?', 'dcl': 'Name1?', 'dnl': 'Name4?', 'aunque': 'aunque?'}
key = {}
for k, lab in priv.items():
    if re.fullmatch(r'[A-Z]\d', lab):
        key[k] = lab[0].lower()
    elif lab == 'nine_dot':
        key[k] = 'y'            # Lasry "[y?]"
    elif lab == 'D_null':
        key[k] = ''             # Lasry "[null?]"
    else:
        key[k] = '<' + CODES[lab] + '>'
alpha_tiles = sorted(k for k, v in key.items() if len(v) == 1)
lines = []
for l in open(rec, encoding='utf8'):
    m = re.match(r'(L\d): (.*)', l)
    if m:
        lines.append((m.group(1), m.group(2).split()))


def decode(k):
    segs, cur, per_line = [], '', []
    pos = []   # (sign, segment index, char index) for letters
    for ln, toks in lines:
        txt = ''
        for t in toks:
            v = k.get(t)
            if v is None:                          # N03, [bnm], '#': no value
                if t.startswith('['):
                    segs.append(cur); cur = ''; txt += ' <unassigned group ' + t + '> '
                else:
                    pos.append((t, len(segs), len(cur))); cur += '?'; txt += '?'
            elif v == '':
                continue
            elif len(v) == 1:
                pos.append((t, len(segs), len(cur))); cur += v; txt += v
            else:
                segs.append(cur); cur = ''; txt += ' ' + v + ' '
        per_line.append((ln, txt))
    segs.append(cur)
    return segs, per_line, pos


wl = wl2857.build_claver_pulgar_long(ctsv, ptxt, 4, 5)
seg = wl2857.Seg(wl)
segs, per_line, pos = decode(key)
real, toks = wl2857.sandwich_measure(seg, segs, 3)
rng = random.Random(2857)
ctrl = []
for _ in range(1000):
    vals = [key[t] for t in alpha_tiles]; rng.shuffle(vals)
    k2 = dict(key); k2.update(zip(alpha_tiles, vals))
    ctrl.append(wl2857.sandwich_measure(seg, decode(k2)[0], 3)[0])
cs = sorted(ctrl)
p95 = cs[949]
if p95 >= 0.20:
    verdict = 'TEST NOT VALID (control 95th percentile not under 20%)'
elif real >= 0.70:
    verdict = 'PASS (read under Lasry key)'
elif real >= 0.30:
    verdict = 'MIDDLE BAND (same family, different key?)'
else:
    verdict = 'MISS'
# per-sign agreement: share of each sign's occurrences that fall inside counted words (needs character coverage map)
cover = []
for sgm in segs:
    s = wl2857.norm_string(sgm)
    covered = [False] * len(s)
    # recompute coverage exactly as sandwich_measure does
    tk = seg.segment(s); longw = [isw and len(w) >= 3 for w, isw in tk]; i0 = 0
    for i, (w, isw) in enumerate(tk):
        ok = longw[i]
        if isw and not ok:
            ok = ((i == 0) or longw[i - 1]) and ((i == len(tk) - 1) or longw[i + 1]) and not (i == 0 and i == len(tk) - 1)
        for j in range(i0, i0 + len(w)):
            covered[j] = ok
        i0 += len(w)
    cover.append((sgm, s, covered))
stat = defaultdict(lambda: [0, 0])
for t, si, ci in pos:
    sgm, s, covered = cover[si]
    # raw -> normalised index: normalisation maps letters one to one and only collapses doubled letters (not l)
    mapped = wl2857.norm_string(sgm[:ci + 1])
    j = len(mapped) - 1 if mapped else 0
    j = min(j, len(covered) - 1) if covered else 0
    stat[t][1] += 1
    stat[t][0] += 1 if (covered and covered[j]) else 0
with open(os.path.join(out, 'test2857_output.txt'), 'w', encoding='utf8') as f:
    f.write(f'measure (sandwich, LMIN 3, list Claver + Pulgar 4+ letters seen 5+ times, U {wl2857.U}): {real:.4f}\n')
    f.write(f'control 1000 permuted tables: mean {sum(cs)/1000:.4f}, 95th percentile {p95:.4f}, max {cs[-1]:.4f}, '
            f'number >= real {sum(1 for c in cs if c >= real)}\n')
    f.write(f'VERDICT: {verdict}\n\n# mechanical decode per line (? = no value)\n')
    for ln, txt in per_line:
        f.write(f'{ln}: {txt}\n')
    f.write('\n# segmentation used by the measure (counted words lower case; uncounted dictionary words with *; '
            'unknown letters upper case)\n' + ' '.join(toks) + '\n\n# per-sign: occurrences inside counted words / all\n')
    for t in sorted(stat, key=lambda x: -stat[x][1]):
        f.write(f'{t}\t{priv.get(t, t)}\t{key.get(t, "-")}\t{stat[t][0]}/{stat[t][1]}\n')
print(open(os.path.join(out, 'test2857_output.txt'), encoding='utf8').read())
