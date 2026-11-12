"""check_marks.py <reading.md> <decryption.txt>: rebuilds the mechanical letter stream from the marked reading and
compares it with the decryption. Fails on any unmarked departure."""
import re, sys
def mech_from_reading(t):
    t = t.split('## Marked reading', 1)[1].split('## Plain', 1)[0]
    t = re.sub(r'<[^>]*>', ' ', t)
    t = re.sub(r'\{\+[^}]*\}', '', t)
    t = re.sub(r'\{([^/}]*)/[^}]*\}', r'\1', t)
    t = re.sub(r'\[\?[^|\]]*\|((?:[^\[\]]|\[\d+\])*)\]', lambda m: m.group(1), t)
    t = re.sub(r'\[\.\.\.\|((?:[^\[\]]|\[\d+\])*)\]', lambda m: m.group(1), t)
    return norm(t)
def norm(t):
    t = re.sub(r'\[\?(\d+)\]', r'[\1]', t)
    return re.sub(r'[^a-zø\[\]0-9]', '', t.lower())
r = mech_from_reading(open(sys.argv[1], encoding='utf8').read())
d = norm(open(sys.argv[2], encoding='utf8').read())
if r == d: print('OK', sys.argv[1], len(d), 'signs'); sys.exit(0)
i = next((k for k in range(min(len(r), len(d))) if r[k] != d[k]), min(len(r), len(d)))
print('FAIL', sys.argv[1], 'at', i, '\n reading:', r[max(0, i-20):i+30], '\n decrypt:', d[max(0, i-20):i+30]); sys.exit(1)
