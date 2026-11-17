# Decode a sheet in pass-A reading order with a key; numerals agreed by A and B (else A's, marked).
# 3-digit codes print as [num:glossA]; clear words as «word»; unknown numerals as {num}.
import csv,json,sys,os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key=json.load(open(sys.argv[1],encoding='utf-8'))
for sid in sys.argv[2:]:
    rows=list(csv.DictReader(open(f'{D}/transcription/merged_{sid}.tsv',encoding='utf-8'),delimiter='\t'))
    rows=[r for r in rows if r['seqA']]; rows.sort(key=lambda r:int(r['seqA']))
    out=[]
    for r in rows:
        n=r['numA']; t=r['type']
        if t=='clear': out.append(' «'+r['glossA']+'» '); continue
        if t=='num2':
            l=key.get(n)
            g=r['glossA'] if r['glossA'] not in ('','-','ـ','?') else ''
            out.append(l if l else '{%s}'%n)
        elif t=='num3': out.append(' [%s:%s] '%(n,r['glossA']))
        else: out.append(' <%s %s> '%(n,r['glossA']))
        if r.get('noteA','').find('slash')>=0: pass
    print(sid+':',''.join(out)); print()
