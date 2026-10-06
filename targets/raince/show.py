"""show.py PAGE LINE: numbered machine labels (pred.json) and existing hand labels for one line,
to correct against img/idx/<page>_<NN>.png."""
import json,sys
p=json.load(open('pred.json')); d=json.load(open('raince_tokens.json'))
page,ln=sys.argv[1],int(sys.argv[2])
row=sorted([t for t in d['tokens'] if t['page']==page and t['line']==ln-1],key=lambda t:t['x0'])
pr=''.join(p.get(f"{page}|{ln-1}|{t['x0']}",'#') for t in row)
g={}
for f in ('gold/labels.txt','gold/labels_v3.txt'):
    try:
        for l in open(f,encoding='utf8'):
            if l.strip() and not l.startswith('#'):
                a,b,c=l.split(); g[(a,int(b))]=c
    except FileNotFoundError: pass
print(len(row),'tokens'); print('pred', pr); print('gold', g.get((page,ln),'-'))
for i in range(0,len(row),10): print(f'{i+1:>3}:', ' '.join(pr[i:i+10]))
