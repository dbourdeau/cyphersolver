# Write H2 in H1's sign names using reconcile's map (signs H2 has that map to nothing keep a '#' prefix).
import sys, re
mp = {l.split('\t')[0]: l.split('\t')[1] for l in open(sys.argv[2]) if l.strip()}
for l in open(sys.argv[1], encoding='utf-8'):
    if '\t' not in l: continue
    a, b = l.rstrip('\n').split('\t', 1); b = re.sub(r'\{[^}]*\}', ' {clear} ', b)
    out = [t if t == '{clear}' else mp.get(t.rstrip('?'), '#' + t.rstrip('?')) + ('?' if t.endswith('?') else '') for t in b.split()]
    print(a + '\t' + ' '.join(out))
