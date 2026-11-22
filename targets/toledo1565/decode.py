"""Decode the figure runs in transcription.txt with the 1565 Toledo key."""
import re, sys
KEY = {}
for letter, codes in [('a',[12,13,14]),('b',[15]),('c',[16]),('d',[17]),('e',[18,19,20]),('f',[21]),
                      ('g',[22]),('h',[23]),('i',[24,25,26]),('l',[27]),('m',[28]),('n',[29]),
                      ('o',[30,31,32]),('p',[33]),('q',[34]),('r',[35]),('s',[36]),('t',[37]),
                      ('u',[38,39,40]),('x',[41]),('y',[42]),('z',[43])]:
    for c in codes: KEY[c] = letter

SIGNS = {'θ': 'll', 'μ': 'r'}  # no. 249 only: barred theta = ll; M-like sign = r (in 'respuesta')

def dec(run):
    if run == '1565': return run  # the date, not cipher
    if run in SIGNS: return SIGNS[run].upper()
    d = run.replace(' ', '')
    out = []
    for i in range(0, len(d) - 1, 2):
        out.append(KEY.get(int(d[i:i+2]), '?'))
    if len(d) % 2: out.append('|odd')
    return ''.join(out).upper()

# A figure run is any run of two or more digits (or one of the two no. 249 signs). Only dates written in
# clear are skipped: the year 1565 and the day '16' of 'a 16. de Jullio' (no. 249).
pat = re.compile(r'(?<![\w])(?:\d{2,}|θ|μ)(?: (?:\d+|θ|μ))*')

def clear_date(line, m):
    run = m.group(0).strip()
    return run == '1565' or (run == '16' and line[m.end():m.end() + 8] == '. de Jul')

def sub(m, line):
    if clear_date(line, m): return m.group(0)
    return '<' + ' '.join(dec(t) for t in m.group(0).split()) + '>'
for line in open(sys.argv[1] if len(sys.argv) > 1 else 'transcription.txt', encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('#'): continue
    if line.startswith('=='): print(line); continue
    print(pat.sub(lambda m: sub(m, line), line))
