"""Build validation.tsv: every figure of the runs in transcription.txt (no. 247) and transcription_249.txt (no. 249),
found with decode.py's run pattern and read with its KEY (and the two no. 249 signs). Unreadable figures ('?' or an
odd digit left over) are '?'; the date 1565 is clear text and left out."""
import re, os
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, 'decode.py'), encoding='utf-8').read()
ns = {}
exec(src.split('pat = re.compile')[0], ns)          # KEY, SIGNS
pat = re.compile(r'(?<![\w])(?:\d{2,}|θ|μ)(?: (?:\d+|θ|μ))*')   # as in decode.py; clear dates skipped below
out = ['# model: es-golden-age', '# source: transcription.txt + transcription_249.txt with decode.py KEY/SIGNS; mk_validation.py',
       '# note: nos. 247 and 249, same key']
for fn in ('transcription.txt', 'transcription_249.txt'):
    for line in open(os.path.join(H, fn), encoding='utf-8'):
        if line.startswith('#') or line.startswith('=='): continue
        line = line.rstrip('\n')
        for m in pat.finditer(line):
            if m.group(0).strip() == '16' and line[m.end():m.end() + 8] == '. de Jul': continue   # the day of 'a 16. de Jullio'
            for run in m.group(0).split():
                if run == '1565': continue
                if run in ns['SIGNS']: out.append(f"{run}\t{ns['SIGNS'][run]}"); continue
                for i in range(0, len(run) - 1, 2):
                    g = run[i:i+2]; v = ns['KEY'].get(int(g), '?') if g.isdigit() else '?'
                    out.append(f'{g}\t{v}')
                if len(run) % 2: out.append(f'{run[-1]}\t?')
open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n'); print(len(out) - 3)
