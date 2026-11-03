# apply_retranscription.py : apply the sign corrections settled on the images to the single-pass transcriptions, regenerate the
# decryptions, write retranscription_log.tsv. Run on the single-pass files kept in scans/old_singlepass/.
import re,glob,os
OLD='scans/old_singlepass/'
K={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('# ') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); K[p[0]]=p[2]
K['+']='u'
HEAD=("# Sign codes per key.tsv. Folio, line counted on the page image. Signs as they stand on the page.\n"
      "# Second pass, 2 Nov 2026: a reader with no key and no language copied every sign from the images; disagreements were settled on enlarged crops (retranscription_log.tsv).\n"
      "# [x] sign damaged or lost, restored from traces or sense; (x) sign written above the line; [deleted signs] ink struck out by the writer; {..} words in clear on the same line.\n")
DHEAD=("# Letter-for-letter decryption of the signs as they stand, same lines as the transcription. Writer's spelling and slips kept; u and v share one sign.\n"
       "# Departures made for sense are shown in the reading file, as editorial notes.\n")
# place, old fragment, new fragment, basis, note
E=[
('c. 9r l. 3','{...}','{sono stati carissimi:}','clear','clear text read'),
('c. 9r l. 6','V T g N 3 2 N c T 4','V T g N [7] 2 N c T 4','image','sign torn; top bar favours z, t not excluded; the word is negozio or negotio either way'),
('c. 9r l. 9','x 3 T D N V g 2 +','x 3 T A N V g 2 +','both reads, image','A-shaped sign, no base stroke; reading [c]ongiunture'),
('c. 9r l. 12','7 7 A D v T','7 7 (A) D v T','image','A written above the line over the next sign; the key-free reader missed it'),
('c. 9r l. 14','N D + 4 A','N A + 4 A','both reads, image','A-shaped sign with a blot at its foot; reading o[c]ulato'),
('c. 9r l. 15','+ T c T V c N V T','+ T g V T V c N V T','both reads, image','vegnendone, not vedendone; the earlier text was a sense repair'),
('c. 9r l. 17','A T c T 4 2 D A','A T c 2 4 2 D A','image','dilicata; the sign is 2 under a blot, not T'),
('c. 9r l. 22','3 9 2 c A r A + N','3 9 2 c 2 r A + N','both reads, image','di favorir, not da favorir'),
('c. 9v l. 6','o T 9 T 3 T + V o T 9 2','o T 9 T 3 T c + V o T 9 2','both reads, image',"colmerete d'un merito; the d sign had been dropped"),
('c. 9v l. 8','A 4 4 T D N x T c T 4','A 4 4 T [deleted signs] D N x T c T 4','both reads, image','solid black block, about 2 signs'),
('c. 11r l. 5','D v T t + 2 x 2 A','D v T + 2 x 2 A','both reads, image','che vi sia, not che qui sia; no q sign on the page'),
('c. 11r l. 6','# 9 N T x x 2','# 9 N A T x x 2','both reads, image','A-shaped sign in the gap; reading pro[c]essi'),
('c. 11r l. 8','4 N V N x D T','4 N N x D T','both reads, image','diminuirlo o scemarlo; no n sign, the supposed slip disappears'),
('c. 16r l. 4','{... sentito.}','{due nostre diffusam. vi habbiamo scritto.}','clear','clear text read'),
('c. 16r l. 5','4 T g g T 2 9 N','4 T g g 2 T 9 N','image','leggiero; the earlier order of i and e was wrong'),
('c. 16r l. 5','3 A [4] [2] A','3 A [4] [2] [A]','image','last three signs stained, tops visible'),
('c. 16r l. 6','V 2 x 3 9 2 r','V 2 [x] 3 9 2 r','image','sign under a blot'),
('c. 16r l. 6','+ T 9 # T 9','+ T 9','image','"per" is not on the page; blank paper after r'),
('c. 16r l. 7','o + V 2 7 2 N V 2','o + V 2 3 2 N V 2','both reads, image','munitioni: the sign is t, not z'),
('c. 16r l. 7','4 A 9 g 2 x x 2','4 A 9 g v 2 x x 2','both reads, image','larghissime; the h sign had been dropped'),
('c. 16r l. 9','c 2 2 V + 2 3 N','c 2 V + 2 3 N','both reads, image',"d'invito; one i only"),
('c. 16r l. 14','o o 2 V 2 x 3 9 A 9 T A c A','o 2 V 2 x 3 9 A 9 V T A c A','both reads, image','soministrarne ad: one m, and the n had been dropped'),
('c. 16r l. 15','A 9 T A V N 2 o T c T x 2 o 2 c A 4 3 9 A','A 9 V T A V N 2 o T c T x 2 o 2 c A A 4 3 9 A','both reads, image','procurarne; da altra parte, heavy A sign'),
('c. 16r l. 16','T 4 N x 3 A 3 N c T 4','T 4 A V g + x 3 2 A c T 4','both reads, image',"l'angustia, not lo stato; the earlier text was a sense repair"),
('c. 16r l. 18','x 2 o T 9 D 2 A 4 4 A','x 2 o T 9 D 2 D A 4 4','both reads, image','a D stands before all; the first A of alloggio belongs to l. 19'),
('c. 16r l. 19','4 4 N g g 2 N T # N x x 2','A 4 4 N g g 2 N # N x x 2','both reads, image','line opens with A; no e before possiamo'),
('c. 16r l. 21','t + A 3 3 9 N D T V','t + A [3] [3] 9 N D T V','image','two signs under a stain, tails visible'),
('c. 16v l. 1','x N V N x 3 A 3 2','x N V N 9 T x 3 A 3 2','both reads, image','sono restati, not sono stati; the signs r e had been dropped'),
('c. 16v l. 3','2 o # 2 T 3 A A g g 9 A','2 o # 2 T 3 A 4 A g g 9 A','both reads, image',"impieta l'aggravarli; the l sign had been dropped"),
('c. 16v l. 4','{In evento che ne ...}','{In evento che ve ne sia fatto alcun motivo, servitevi delle}','clear','clear text read'),
('c. 16v l. 7','{... forse anche opportuno che}','{se non ricercato, e per necessita. Sara forse anche opportuno che}','clear','clear text read'),
('c. 16v l. 11','D N 9 9 T g g 2 N o A','D N 9 9 T g 2 N o A','both reads, image','one g: the writer spelled Corregio here'),
('c. 16v l. 11','r A D 2 4 2 3 A 9 T A V D v T','r A D 2 4 2 3 A 9 A V D v T','both reads, image','facilitar anche; no e'),
('c. 20r l. 12','t + A 4 2 r 2 D A','t + D 4 2 r 2 D A','both reads, image','the writer wrote the D sign: quclificati; reading qu[a]lificati'),
('c. 20r l. 12','x x 2 o T D','x x 2 [o] T D','image','blot over one sign'),
('c. 20r l. 12','D 2 9 D N x 3 A V 7 T #','D 2 9 D N V 3 A V 7 T #','both reads, image','the writer wrote the V sign: circontanze; reading circo[s]tanze'),
('c. 20r l. 13','# 2 7 2 N V 2','# 2 [7] 2 N V 2','image','blot over one sign'),
('c. 20r l. 16','{...}','{stesso procuriate quelli de gli altri:}','clear','clear text read'),
('c. 20v l. 1','D 9 T # A V 3 2 c A 2 V N x 3 9 2 T D 2 A x D + V N','D 9 T # D V 3 2 c D V N x 3 9 2 D 2 D x D + V N','both reads, image',"three a are written with the closed D sign on this line; no i after da, no e before ciascuno"),
]
log=['place\tearlier signs\tsigns now\tbasis\tnote']
used=set()
def letters(body):
    def tr(m):
        t=m.group(0)
        if t.startswith('{') or t=='[deleted signs]': return ' '+t+' '
        if t.startswith('['): return '['+K[t[1:-1]]+']'
        if t.startswith('('): return '('+K[t[1:-1]]+')'
        return K[t]
    d=re.sub(r'\{.*?\}|\[deleted signs\]|\[[^\] ]\]|\([^) ]\)|\S',tr,body)
    parts=re.split(r'(\{.*?\}|\[deleted signs\])',d)
    return ' '.join(x for x in (p if p.startswith(('{','[deleted')) else p.replace(' ','') for p in parts) if x)
for f in sorted(glob.glob(OLD+'transcription_cc*.txt')):
    b=os.path.basename(f); out=[]; dec=[]
    for l in open(f,encoding='utf8').read().split('\n'):
        if l.startswith('#') or not l.strip(): continue
        pl,body=l.split(':',1); body=body.strip()
        for n,e in enumerate(E):
            if e[0]==pl and e[1] in body:
                assert body.count(e[1])==1,(pl,e[1])
                body=body.replace(e[1],e[2]); log.append('\t'.join(e)); used.add(n)
        out.append(f'{pl}: {body}')
        dec.append(f'{pl}: {letters(body)}')
    open(b,'w',encoding='utf8').write(HEAD+'\n'.join(out)+'\n')
    open(b.replace('transcription','decryption'),'w',encoding='utf8').write(DHEAD+'\n'.join(dec)+'\n')
print('applied',len(used),'of',len(E),'missing',[E[n][:2] for n in range(len(E)) if n not in used])
open('retranscription_log.tsv','w',encoding='utf8').write('\n'.join(log)+'\n')
