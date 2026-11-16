"""item-level cipher-term search in Africa-related NA archives. writes na_items_all2.json + log"""
import json,re,sys
from na import *
EADS=['2.21.105','2.05.121','2.05.70','2.05.128','2.05.123','2.05.124','2.05.125','2.05.119','2.05.122','2.05.12','2.18.18.02','2.21.167','2.21.174','2.21.011','2.05.14.12','2.05.15.06','2.05.30','1.10.07','1.04.02']
TERMS=['cijferschrift','chiffre','chiffres','gecijferd','ontcijferd','ontcijfering','geheimschrift','cijfferschrift','cijffer','cifra','cijferbrief','dechiffrement','cijfertelegram','cijfertelegrammen','cijfer','cijfers','sleutel','cypher','cipher']
res={}
for e in EADS:
    for t in TERMS:
        r=items(e,t)
        res[f'{e}|{t}']=r
        if r:
            print(e,t,len(r),flush=True)
            for x in r[:25]: print('    ',x.get('id'),'|',re.sub('<[^>]+>','',x.get('title') or '')[:170],'|',x.get('period'),flush=True)
    json.dump(res,open('na_items_all2.json','w'),ensure_ascii=False)
