# show a transcription line by line with key_M + H/M inferred values (measure_sense's lookup)
import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import measure_sense as m
for line in open(sys.argv[1],encoding='utf8'):
    if line.startswith('#'): print(line.rstrip()); continue
    out=[]
    for t in line.split():
        alts=t.split('|'); v=[m.val(a) for a in alts]
        out.append('/'.join(f'{x}' if y is None else f'{y}' for x,y in zip(alts,v)) if len(alts)>1 else (f'[{t}]' if v[0] is None else v[0]))
    print(' '.join(out))
