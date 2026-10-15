import re,sys
def groups(fn):
    out=[]
    for l in open(fn,encoding='utf8'):
        if l.startswith('#') or l.startswith('=='): continue
        for t in l.split():
            if t=='|': continue
            t=re.sub(r'\[.*?\]','',t); t=re.sub(r'\^.*','',t); t=t.strip('_?')
            if t.isdigit(): out.append(int(t))
    return out
L={k:groups(f'transcription_{k}.txt') for k in ('R2968','R2970','R2972')}
