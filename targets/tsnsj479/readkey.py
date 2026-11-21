"""Render the shape transcriptions of T-S NS J479 in Hebrew letters under a key. Words are reversed (the scribe writes
left to right; the transcribers listed signs right to left). Usage: readkey.py [rows-prefix] [extra L=heb,...]"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
ORDER = 'I U E A N 4 c B d - < p P q w O 6 S X 9 C 7'.split()
KEY = dict(zip(ORDER, 'אבגדהוזחטיכלמנסעפצקרשת'))
pref = sys.argv[1] if len(sys.argv) > 1 else 'S'
for a in sys.argv[2:]:
    for kv in a.split(','):
        k, v = kv.split('='); KEY[k] = v
for f in ('tr_side1.md', 'tr_side2.md'):
    try: L = open(f, encoding='utf-8').read().splitlines()
    except FileNotFoundError: continue
    for l in L:
        m = re.match(r'\s*(S\d\w+\d\d):\s*(.*)', l)
        if not m or not m.group(1).startswith(pref): continue
        out = []
        for w in m.group(2).split('|'):
            t = [x.rstrip('.').rstrip('?').rstrip('.') for x in w.split()]
            out.append(''.join(KEY.get(x, '{%s}' % x) for x in reversed(t)))
        print(m.group(1), ' '.join(out))
