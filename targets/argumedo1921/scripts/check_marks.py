"""Mark check: python scripts/check_marks.py   (standard library only)
1. Re-runs decrypt.py and checks that the decryption files are unchanged.
2. For every run of each marked reading, undoes the marks ({x/y} -> x, {x} -> x) and compares the letters with the
   mechanical decryption (word division ignored); fails on any unmarked departure.
3. Prints word counts per letter: cipher words, read as given, marked (holes)."""
import os, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
DOCS = ['DCXXI.3.244.1', 'DCXXI.3.250.2']
before = {d: open(os.path.join(ROOT, 'decryption_%s.txt' % d), encoding='utf-8').read() for d in DOCS}
subprocess.run([sys.executable, os.path.join(HERE, 'decrypt.py')], check=True, capture_output=True)
bad = False
for d in DOCS:
    if open(os.path.join(ROOT, 'decryption_%s.txt' % d), encoding='utf-8').read() != before[d]:
        print('FAIL: decryption_%s.txt is not what decrypt.py gives' % d); bad = True
    mech = {}
    for line in before[d].splitlines():
        if line.startswith('#'): continue
        rid, fol, role, dec = line.split('\t'); mech[rid] = (role, dec)
    md = open(os.path.join(ROOT, 'reading_%s.md' % d), encoding='utf-8').read()
    block = re.search(r'```marked\n(.*?)```', md, re.S).group(1).strip().splitlines()
    norm = lambda s: re.sub(r'[^A-ZÑ?]', '', s.replace('<0?>', '?'))
    words = read = marked = 0; new_w = new_r = 0
    for line in block:
        rid, m = line.split(': ', 1)
        undone = re.sub(r'\{([^/{}]*)/[^{}]*\}', r'\1', m); undone = re.sub(r'\{([^{}]*)\}', r'\1', undone)
        if norm(undone) != norm(mech[rid][1]):
            print('FAIL %s: %s does not undo to %s' % (rid, m, mech[rid][1])); bad = True
        for w in m.split():
            words += 1; ok = '{' not in w; read += ok; marked += not ok
            if mech[rid][0] == 'new': new_w += 1; new_r += ok
    if set(mech) - {l.split(': ')[0] for l in block}: print('FAIL runs missing in', d); bad = True
    print('%s: %d cipher words, %d read as given, %d marked (share %.3f); new runs: %d words, %d read'
          % (d, words, read, marked, read / words, new_w, new_r))
sys.exit(1 if bad else 0)
