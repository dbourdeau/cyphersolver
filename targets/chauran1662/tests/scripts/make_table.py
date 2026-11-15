#!/usr/bin/env python3
"""Build table v1 from the alignment of ff.189 and 260 (key/alignment_auto.txt) plus my line-by-line corrections."""
import json, re, collections, hashlib
occ=collections.defaultdict(list)
for ln in open('key/alignment_auto.txt'):
    p=ln.split()
    if len(p)<3: continue
    tag=p[0]+' '+p[1]
    for t in p[2:]:
        g,v=t.rsplit('=',1); occ[g].append((v,tag))
patch=dict(x.split('=') for x in """208:S2=no 228:S2=medio 205:D3=s 178:S1=recevido 45:B1=negocio 64:D3=vu 197:O=ve 221:P=in 139:B2=razo 72=ro 182:B1=l 147:P=nes 24:O=conuenien 155=tes 160:S1=hauiendo 8:D3=des 192:O=to 113:B1=u 65=l 110:M=ho 165=m 171:M=bo 49:M=u 87:S2=r 36:B1=g 226:S1=mente 94:M=passa 19:D3=da 62:D3=ajustamient 156=ru 208:S1=tan 68:D3=he 81:M=quenta 154:P=f 59:D3=y 27:O=executa 225:S1=confirm 90:P=cion 114:S2=fuere 125:S2=yor 31:B3=mu 200:B1=mucho 105:D3=procurando 52:P=sino 149:B1=materia 191=esta 61:P=ros 118:B1=ad 134:B1=cri 126:S2=y 198:D3=conveniencia 50:P=del 18=pero 229:S2=menester 202:P=muy 136:M=particular 180:S1=atencion 91=punto 44:D3=occasiones 141:S2=puedan 51:D3=differentes 184:P=dieta 195:S1=futura 36:B2=donde 72:S1=considerar 59:S1=mostrado 112:D3=experiencia 136:D3=ven 139:D3=ge 34:B1=bles 27:M=trattado 113:M=pues 221:S1=diuertir 39:B2=por 148:S1=te 111:M=ellas 124:B2=occasion 182:D3=re 182:O=hu 187:P=pri 2:S2=audiencia 153=aora 145:B1=dezir 171:B1=os 168:M=mas 97:D3=persis 225:P=tir 120:B1=fo 45:S2=satisfaccion 68:B2=yo 210:B1=22 48:B2=ocho 160:O=muger 131:B1=hi 71:B1=zi 203:O=y 38:B2=ju 206:D3=z 21:S1=ga 127=visto 27:D3=hauiendo 95:S1=corriente 29:B2=del 173:M=bra 164:M=ze 177:M=san 124:D3=assigura 130:P=pla 214:S2=sas 83:B2=ti 195:S2=za 216:O=fuesse 180:M=ha 209:B2=e 195:M=otra 22:S1=me 207:S2=no 172:B1=fre 200:O=r 5:B1=of 53:M=dri 3:O=nos 129:S1=arbitros 53:P=pro 165:B1=caso 134:M=ministro 183:D3=del 25:S1=ja 97:B2=puede 66:B2=xo 92:B2=gente 12:O=algunas 82:S1=otras 158:D3=regimientos 234:S2=seran 7:O=quinze 67:S2=mil 152:B2=hombres 74:B2=acom 65:P=na 199:B1=mad 199:S1=bien 12:P=operacion 198=cinco 108:M=gro 43:D3=personas 190:M=grande 43:B2=por 104=gusto 210:O=calidad 153:S1=cauallos 99:B2=mad 15:M=dignidad 145:S1=jo 25:S2=manda 215:S2=una 100:B2=relacion 91:B2=estara 209=poder 135:D3=sin 20=vien 110:D3=dios 16=ni 121:B1=los 112:P=semana 228:S2=medio 13:D3=tas 78:S1=principe 70:B1=do 115=le 1:B1=as 63:S2=todas 19:B2=los 181:P=neu 113:O=entrado 17=ie 35:B1=d 190:P=ro 157=mi 71:B1=zi 83:S1=mo""".split())
drop={'126:?','33:?','163:?','130:?','152:?','93','65:S1','84:O','113:D3','105','8:B2','66','62:M','178:B1','9:O','191:D3','79:S1','158','154:P' ,'178:P','203:P','19:B1','69:B1','34:P','192:D3','17:D3','114:M','133:B2','126','6:B1','180:D3','217:S1','76:M','31:B1','131:B1x','12','67:B2','47:S2','64:S1','174:M','116:O x'}
# groups in `drop` are those whose value I could not settle from the gloss; 66 is kept below as r (firm by count)
drop.discard('66'); drop.discard('154:P')
rows=[]
for g,lst in occ.items():
    c=collections.Counter(v for v,_ in lst); n=len(lst)
    top,k=c.most_common(1)[0]
    val=patch.get(g,top)
    kk=c.get(val,0)
    if g in drop or val=='_' : tier='unsettled'
    elif n>=2 and kk>=2 and kk/n>=0.6: tier='firm'
    elif n>=2: tier='mixed'
    else: tier='single'
    rows.append((g,val,tier,n,kk,' '.join('%s×%d'%(a,b) for a,b in c.most_common(4))))
def sk(r):
    m=re.match(r'(\d+)(?::(.*))?',r[0]); return (int(m.group(1)),m.group(2) or '')
rows.sort(key=sk)
with open('key/table_v1.tsv','w') as o:
    o.write('group\tvalue\ttier\toccurrences\tagreeing\taligned_values\n')
    for r in rows: o.write('\t'.join(str(x) for x in r)+'\n')
h=hashlib.sha256(open('key/table_v1.tsv','rb').read()).hexdigest()
open('key/table_v1.sha256','w').write(h+'  table_v1.tsv\n')
t=collections.Counter(r[2] for r in rows)
print(len(rows),'groups',dict(t),h)
tok=collections.Counter()
for r in rows: tok[r[2]]+=r[3]
print('tokens by tier',dict(tok))
