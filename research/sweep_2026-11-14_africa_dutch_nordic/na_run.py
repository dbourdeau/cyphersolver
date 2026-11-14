"""item-level cipher-term search in Africa-related NA archives. writes na_items_all.json + log"""
import json,re,sys
from na import *
EADS=['1.05.14','1.05.01.01','1.05.01.02','1.05.03','1.05.06','1.05.13.01','1.11.06.14','2.01.28.01','2.01.28.02','2.01.28.03','1.02.19','1.02.21.01','1.02.21.02','1.02.00','1.03.01','2.05.15.15','2.05.15.17','2.05.15.05','2.05.22','2.05.14.11','2.05.30','1.10.62','1.10.72','1.01.46','1.01.47.15','1.01.47.16','2.19.190','2.21.479','1.10.69','1.10.30','1.10.56','1.10.59','1.11.06.18','1.05.11.11','2.10.01','2.10.03','2.01.27.02','2.01.27.05','1.02.20','1.02.22','1.02.16','1.02.18']
TERMS=['cijfer','cijfers','cijferschrift','chiffre','chiffres','gecijferd','ontcijferd','ontcijfering','geheimschrift','cijfferschrift','cijffer','sleutel','cifra','cijferbrief','chiffré','dechiffrement','gechiffreerd','cypher','cipher']
res={}
for e in EADS:
    for t in TERMS:
        r=items(e,t)
        res[f'{e}|{t}']=r
        if r:
            print(e,t,len(r),flush=True)
            for x in r[:25]: print('    ',x.get('id'),'|',re.sub('<[^>]+>','',x.get('title') or '')[:170],'|',x.get('period'),flush=True)
    json.dump(res,open('na_items_all.json','w'),ensure_ascii=False)
