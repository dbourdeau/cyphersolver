"""Mark check: rebuilds decryption_DCXXI.3.323.1.txt (key 313) and checks that the marked reading undoes to it.
{x/y} -> x, {+a} -> '', [?x] -> x. Prints word counts. Exit 1 on any mismatch."""
import os, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); DOC = 'DCXXI.3.323.1'
out = subprocess.run([sys.executable, os.path.join(HERE, 'decrypt.py'), os.path.join(ROOT, f'transcription_{DOC}.txt'), '313'],
                     capture_output=True, text=True, encoding='utf-8').stdout
have = open(os.path.join(ROOT, f'decryption_{DOC}.txt'), encoding='utf-8').read()
if out.replace('\r\n', '\n').strip() != have.replace('\r\n', '\n').strip():
    print('FAIL: decryption file is not what decrypt.py gives'); sys.exit(1)
print('decryption file: rebuilt, identical')
mech = {l.split('\t')[0]: l.split('\t')[2] for l in out.splitlines() if not l.startswith('#')}
block = re.search(r'```marked\n(.*?)```', open(os.path.join(ROOT, f'reading_{DOC}.md'), encoding='utf-8').read(), re.S).group(1)
L = lambda s: re.sub(r'[^A-ZÑ]', '', s)
bad = False; words = verb = rep = holes = 0
for line in block.strip().splitlines():
    rid, marked = line.split(': ', 1)
    u = re.sub(r'\{\+[A-ZÑ]+\}', '', marked); u = re.sub(r'\{([A-ZÑ]*)/[A-ZÑ]*\}', r'\1', u); u = re.sub(r'\[\?([A-ZÑ]*)\]', r'\1', u)
    if L(u) != L(mech[rid]): print('FAIL', rid); bad = True
    for w in re.findall(r'[^\s,.#]+', marked):
        if not re.search('[A-ZÑ]', w): continue
        words += 1
        if w.startswith('[?'): holes += 1
        elif '{' in w: rep += 1
        else: verb += 1
print(f'cipher words {words}: verbatim {verb} ({100*verb/words:.1f}%), repaired {rep}, holes {holes}')
sys.exit(1 if bad else 0)
