"""Count words of the coded runs of a reading: verbatim (no mark), repaired ({x/y} or {+a}),
guessed ([?w:G] inside the word; counted as holes), from gloss only (none here)."""
import sys, re
t = open(sys.argv[1], encoding='utf8').read().split('## Coded runs')[1]
v = r = h = 0
for ln in t.splitlines():
    m = re.match(r'^[SFCM]\d\d \| (.*)$', ln)
    if not m: continue
    for w in m.group(1).split():
        if '[?' in w or '[...' in w: h += 1
        elif '{' in w: r += 1
        else: v += 1
n = v + r + h
print(f'{sys.argv[1]}: {n} coded words; verbatim {v}, repaired {r}, guessed/hole {h}, gloss-only 0; read share {(v+r)/n:.3f}, verbatim share {v/n:.3f}')
