# Tabulate numeral -> gloss readings (pass A and B) on given sheets, num2 only, numeral agreed by both passes.
import csv,sys,os,collections
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T=collections.defaultdict(collections.Counter)
for sid in sys.argv[1:]:
    for r in csv.DictReader(open(f'{D}/transcription/merged_{sid}.tsv',encoding='utf-8'),delimiter='\t'):
        if r['type']!='num2' or r['numA']!=r['numB'] or not r['numA']: continue
        for g in (r['glossA'],r['glossB']):
            g=g.strip()
            if g in ('','-','?'): continue
            T[r['numA']][g]+=1
for k in sorted(T,key=int): print(k, sum(T[k].values()), dict(T[k].most_common()))
