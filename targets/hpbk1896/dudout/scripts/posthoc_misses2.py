# Post-hoc (after the single measurement): list held-out tokens where key and glosses disagree.
import csv,json,collections,os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(D+'/scripts/score.py').read().split('key=json.load')[0]
exec(src); D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key=json.load(open(D+'/key/key_systemB_v2.json'))
miss=collections.Counter()
for sid in ('644','652','675'):
    for r in csv.DictReader(open(f'{D}/transcription/merged_{sid}.tsv',encoding='utf-8'),delimiter='\t'):
        if r['type']!='num2' or not r['numA'] or r['numA']!=r['numB']: continue
        refs={sk(g) for g in (r['glossA'],r['glossB']) if g.strip() not in ('','-','?','ـ')}; refs.discard(None)
        if not refs: continue
        n=r['numA']
        if not (n in key and sk(key[n]) in refs): miss[(n,key.get(n),r['glossA'],r['glossB'])]+=1
for k,v in miss.most_common(): print(v,k)
