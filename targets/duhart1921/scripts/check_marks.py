"""Mark check: python scripts/check_marks.py   (standard library only)
1. Rebuilds decryption_DCXXI.3.231.1.txt from the transcription and key_frozen.tsv; fails if the file differs.
2. For every run of the marked reading, undoes the marks ({x/y} -> x, {+a} -> nothing) and compares the letters
   (spaces and apostrophes ignored) with the mechanical decryption; fails on any unmarked departure.
3. Prints word counts: verbatim, repaired, holes."""
import os, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
DOC = 'DCXXI.3.231.1'
out = subprocess.run([sys.executable, os.path.join(HERE, 'decrypt.py'), os.path.join(ROOT, f'transcription_{DOC}.txt'),
                      os.path.join(ROOT, 'key_frozen.tsv')], capture_output=True, text=True, encoding='utf-8').stdout
have = open(os.path.join(ROOT, f'decryption_{DOC}.txt'), encoding='utf-8').read()
bad = False
if out.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
    print('FAIL: decryption file is not what decrypt.py gives'); sys.exit(1)
print('decryption file: rebuilt, identical')
mech = {}
for line in out.splitlines():
    if line.startswith('#'): continue
    rid, page, d = line.split('\t'); mech[rid] = d
md = open(os.path.join(ROOT, f'reading_{DOC}.md'), encoding='utf-8').read()
block = re.search(r'```marked\n(.*?)```', md, re.S).group(1)
letters = lambda s: re.sub(r"[^A-Z]", '', s)
words = verb = rep = holes = 0
for line in block.strip().splitlines():
    rid, marked = line.split(': ', 1)
    undone = re.sub(r'\{\+[A-Z]+\}', '', marked)
    undone = re.sub(r'\{([A-Z]*)/[A-Z]*\}', r'\1', undone)
    if letters(undone) != letters(mech[rid]):
        print(f'FAIL {rid}: marked reading does not undo to the decryption'); bad = True
    for w in marked.split():
        words += 1
        if '[' in w: holes += 1
        elif '{' in w: rep += 1
        else: verb += 1
missing = set(mech) - {l.split(': ')[0] for l in block.strip().splitlines()}
if missing: print('FAIL runs missing from reading:', sorted(missing)); bad = True
print(f'cipher words {words}: verbatim {verb} ({100*verb/words:.1f}%), repaired {rep}, from gloss 0, holes {holes}')
sys.exit(1 if bad else 0)
