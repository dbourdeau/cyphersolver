# c7r_apply.py : sign-first pass on c. 7r, third round. One reader read every sign on full-resolution strips (recut.py). This reader had seen the
# earlier transcription and knew the key, so the pass is not blind. Only the places below changed. Writes the transcription, the decryption and a log.
import re
K={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('# ') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); K[p[0]]=p[2]
K['+']='u'
E=[('c. 7r l. 4:','D N 9 9 T g g 2 N T g 4','D N 9 9 T g 2 N T g 4','one g sign on the page; l. 5 has two. The earlier doubled g was a repair'),
('c. 7r l. 8:','x 3 9 2 V g T','x 3 9 2 g V T','signs are g then V, "strigne"; the earlier order was a silent swap'),
('c. 7r l. 14:','T 4 A x + A','T 4 A x + [A]','last sign at the tear: only its left stroke remains'),
('c. 7r l. 15:','T 9 A 9 T V N x 3 9 2','T 9 A 9 T A V N x 3 9 2','an A stands before the word-division stroke and had been dropped: "cooperare a nostri"'),
('c. 7r l. 15:','2 V 3 T 9 T x x','2 V 3 T 9 T x [x]','second x runs into a hole at the edge; left loop and crossing remain')]
F='transcription_cc07r_1630-02-07.txt'; G='decryption_cc07r_1630-02-07.txt'
L=open(F,encoding='utf8').read().split('\n'); log=['line\tearlier signs\tsigns now\treason']
for pl,a,b,r in E:
    for i,l in enumerate(L):
        if l.startswith(pl) and a in l:
            L[i]=l.replace(a,b); log.append(f'{pl[:-1]}\t{a}\t{b}\t{r}'); break
    else:
        raise SystemExit(('not found',pl,a))
open(F,'w',encoding='utf8').write('\n'.join(L))
def dec(b):
    return ''.join('['+K[t[1:-1]]+']' if t.startswith('[') else K[t] for t in b.split())
D=['# Letter-for-letter decryption, same lines as the transcription. Writer\'s spelling kept; u and v share one sign.']
for l in L:
    if l.startswith('c. '):
        h,b=l.split(':',1); D.append(f'{h}: {dec(b)}')
open(G,'w',encoding='utf8').write('\n'.join(D)+'\n')
open('retranscription_log_c7r.tsv','w',encoding='utf8').write('\n'.join(log)+'\n')
print('\n'.join(D)); print(sum(len(l.split(':',1)[1].split()) for l in L if l.startswith('c. ')),'signs')
