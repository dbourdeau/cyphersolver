#!/usr/bin/env python3
"""Mark check for 2393 (Pandolfini 1515). Standard library only.
    python scripts/check_marks.py
1. Rebuilds decryption_666.txt from transcription_666.txt and key.tsv with decrypt.py; fails if it differs.
2. For every reading line (label: text) in reading_666.md, resolves the marks to their mechanical side
   ({x/y} -> x, {+a} -> nothing, a bare [...] -> nothing) and compares the letters (accents, case, spaces and
   punctuation ignored) with the decryption line of the same label (r18b continues r18). Fails on any difference.
3. Prints word counts: verbatim words, words with a marked repair, conjectures, holes."""
import pathlib, re, subprocess, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
out = subprocess.run([sys.executable, str(HERE / 'decrypt.py'), str(ROOT / 'transcription_666.txt'), str(ROOT / 'key.tsv')],
                     capture_output=True, text=True, encoding='utf-8')
have = (ROOT / 'decryption_666.txt').read_text(encoding='utf-8')
if out.returncode or out.stdout.replace('\r\n', '\n') != have.replace('\r\n', '\n'):
    print('FAIL decryption_666.txt is not what decrypt.py gives'); sys.exit(1)
print('decryption_666.txt: rebuilt, identical')
mech = {}
for l in have.splitlines():
    lab, _, t = l.partition('\t'); mech[lab] = t.replace('|', '')
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z0-9?]', '', ''.join(c for c in s if not unicodedata.combining(c)))
MARK = re.compile(r'\{([^{}/]*)/([^{}]*)\}|\{\+([^{}]*)\}|(\[\.\.\.\])')
def mech_side(t):
    return MARK.sub(lambda m: m.group(1) if m.group(1) is not None else '', t)
rd = {}
for l in (ROOT / 'reading_666.md').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^((?:r|v|b|bv)\d+\w*): (.*)$', l)
    if not m: continue
    lab = 'r18' if m.group(1) == 'r18b' else m.group(1)
    rd[lab] = rd.get(lab, '') + ' ' + m.group(2)
bad = 0
for lab, t in mech.items():
    if lab not in rd: print('FAIL no reading for', lab); bad += 1; continue
    a, b = norm(mech_side(rd[lab])), norm(t)
    if a != b:
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        print(f'FAIL {lab}: reading gives ...{a[max(0,i-12):i+12]}... decryption ...{b[max(0,i-12):i+12]}...'); bad += 1
if bad: sys.exit(1)
print(f'reading_666.md: {len(mech)} lines, every departure marked')
# word counts on the read side
verb = rep = conj = hole = 0
for lab, t in rd.items():
    t2 = re.sub(r'\{[^{}/]*/\[\.\.\.\]\}|\[\.\.\.\]', ' HOLE ', t)
    t2 = re.sub(r'\{[^{}/]*/\[\?([^\]]*)\]\}', lambda m: ' ' + ' '.join('CONJ' for _ in m.group(1).split()) + ' ', t2)
    t2 = re.sub(r'\{[^{}/]*/\[Cristianissimo\]\}', ' REPAIR ', t2)
    for w in re.findall(r"[^\s,.;:«»()]+", t2):
        if w == 'HOLE': hole += 1
        elif w == 'CONJ': conj += 1
        elif '{' in w or '}' in w or w == 'REPAIR': rep += 1
        elif re.search(r'[A-Za-zÀ-ÿ]', w): verb += 1
tot = verb + rep + conj + hole
print(f'words: {tot} = {verb} verbatim + {rep} with a marked repair + {conj} conjectural + {hole} holes '
      f'(read as sense: {(verb + rep) / tot:.1%}; verbatim: {verb / tot:.1%})')
