"""Rebuild the mechanical decryption from transcription + key and check that the reading departs from it only where
marked. Marks: {x/y} mechanical x changed to y; {+a} added letter; [?word] guess; [...] hole; [N] unidentified code.
u/v, i/j and case are not distinctions; spaces, hyphens and punctuation are ignored.
Usage: python -I check_marks.py <transcription> <key> <reading.md>"""
import sys, re, os
sys.path.insert(0, os.path.dirname(__file__))
from decrypt import decrypt_lines
def norm(s): return re.sub(r'[^a-z?\[\]°]', '', s.lower().replace('v', 'u').replace('j', 'i'))
mech = {lab: norm(''.join(ws)) for lab, ws in decrypt_lines(sys.argv[1], sys.argv[2])}
bad = n = 0
for ln in open(sys.argv[3], encoding='utf8'):
    m = re.match(r'\s*(L\d\d): (.*)', ln)
    if not m: continue
    lab, txt = m.groups(); n += 1
    pat = ''
    for tok in re.split(r'(\{[^}]*\}|\[[^\]]*\])', txt):
        if not tok: continue
        if tok.startswith('{+'): continue
        if tok.startswith('{'): pat += re.escape(norm(tok[1:-1].split('/')[0])); continue
        if tok.startswith('['): pat += '.+?'; continue
        pat += re.escape(norm(tok))
    if not re.fullmatch(pat, mech.get(lab, '')):
        bad += 1; print('UNMARKED DEPARTURE', lab, '\n  mech:', mech.get(lab), '\n  read:', txt)
print(f'{n} lines checked, {bad} with unmarked departures')
sys.exit(1 if bad or not n else 0)
