#!/usr/bin/env python3
"""Test against a clerk's decipherment on another copy: mechanical decode (key only, no mark rules, no context)
against the clerk's words.

Usage: python3 score_interlinear.py TRANSCRIPTION CLERKTEXT LINE_PREFIXES(comma-separated) [N=200]
  No. 24: python3 score_interlinear.py ../letters/1814-12-30_No24/transcription.txt \
              ../letters/1814-12-30_No24/clerk_decipherment_0196.txt 220,S
  No. 25: python3 score_interlinear.py ../letters/1815-01-06_No25/transcription.txt \
              ../letters/1815-01-06_No25/clerk_decipherment_0174.txt 220,221,S

Score = characters of the clerk's text (letters and digits; [[ ]] stretches the reader could not make out are dropped)
matched in order by the decode (difflib matching blocks, autojunk off), divided by the length of the clerk's text.
Control: the 1,600 key readings shuffled among the code numbers N times (seed 650), same transcription, same scoring.
Python standard library only."""
import difflib, hashlib, random, re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode650 as D

tr, ct, pref = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
N = int(sys.argv[4]) if len(sys.argv) > 4 else 200
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
clerk = ' '.join(l for l in open(ct, encoding='utf-8') if not l.startswith('#'))
clerk = norm(re.sub(r'\[\[.*?\]\]', ' ', clerk, flags=re.S))
groups = [t[1] for lab, toks in D.load(tr) if any(lab.startswith(p) for p in pref) for t in toks if t[0] == 'code']


def score(vals):
    s = norm(''.join(vals.get(D.tj(m)) or '' for m in groups if 1 <= m <= 1600))
    sm = difflib.SequenceMatcher(None, s, clerk, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / len(clerk)


real = dict(D.KEY)
r = score(real)
codes = sorted(real)
vals = [real[c] for c in codes]
rng = random.Random(650)
ctl = []
for _ in range(N):
    rng.shuffle(vals)
    ctl.append(score(dict(zip(codes, vals))))
ctl.sort()
print(f"key {D.KEY_PATH.name} sha256 {hashlib.sha256(D.raw).hexdigest()}")
print(f"groups {len(groups)}  clerk chars {len(clerk)}")
print(f"real key: {r:.3f}   shuffled ({N}): best {ctl[-1]:.3f}  median {ctl[N//2]:.3f}  real beats {sum(c < r for c in ctl)}/{N}")
