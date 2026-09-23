"""Reproduce literal readings and counts; no guessed nomenclator values."""
from pathlib import Path
import csv, json, re, collections
P=Path(__file__).parent
key=json.loads((P/'key-potocka.json').read_text())
rows=list(csv.DictReader((P/'potocka-segments.tsv').open(encoding='utf8'),delimiter='\t'))
rows.append(dict(record='7526',page='spread-right',context='Postscript',cipher=(P/'r7526-trial.txt').read_text(),reading_note='Pan starosta serecki? iest tu. Pytalam sie iezeli ma co postanowionego. Ni ma nic. Iedzie dzie? do Lublina. To tesz prawda ze byl u dominikanow wtenczas iak estancowal z nia w polu. Powiedal mi p. Tabrowski?'))
codes=json.loads((P/'standalone-codes.json').read_text())
records=sorted(set(r['record'] for r in rows)|{'7524'})
tokens=[]; summaries={};md=['# Literal cipher readings','', 'These are the encrypted passages, with short clear-text anchors, not a full diplomatic transcription of the mostly clear letters. Page numbers refer to DECODE image suffixes; left/right identifies a spread. Numeric readings preserve irregular spelling. Editorial interpretations are separate. All recovered values are grade I (inferred here), with doubtful segments marked M. No archive key or independent plaintext was used. Standalone codes remain unvalued.','']
for rec in records:
    md+=['## R'+rec,'']
    own=[]
    if rec=='7524':
        ct=re.findall(r'\d+', (P/'r7524-cipher.txt').read_text())
        for i,n in enumerate(ct):own.append(dict(record=rec,segment='unread',position=i+1,cipher=n,plain='?',grade='',coherent=False))
        md+=['Mniszech: not read. The clear Polish and Latin anchors in `r7524-cipher.txt` are not decipherments. Every one of the cipher tokens remains open. The solver candidates are failed trials, not readings.','']
    for idx,r in enumerate(rows):
        if r['record']!=rec:continue
        ct=r['cipher'].split(); raw=''.join(key.get(n,'<'+n+'>') for n in ct)
        doubtful=any(s in r['reading_note'].lower() for s in ['unclear','verify','possible','probably','likely','some surplus','substitution errors','irregular surname','could be','?']) or rec=='7526'
        grade='M' if doubtful else 'I'
        # Conservative coherence count: exclude entire doubtful segments, not just unkeyed figures.
        for i,n in enumerate(ct):
            uncertain=doubtful
            if rec=='7526': uncertain=(11<=i<18 or i>=len(ct)-9)
            own.append(dict(record=rec,segment=str(idx),position=i+1,cipher=n,plain=key.get(n,'?'),grade=('M' if uncertain else 'I') if n in key else '',coherent=not uncertain and n in key))
        md += [f"### Image {r['page']}, segment {idx}",f"Clear anchor: {r['context']}",'',f"Cipher: `{r['cipher'].strip()}`",'',f"Literal ({grade}): **{raw}**",'',f"Interpretation: {r['reading_note']}",'']
    for r in codes:
        if r['record']!=rec:continue
        md += [f"Standalone codes, image {r['page']}: "+' '.join('<'+str(n)+'>' for n in r['tokens'])+'. Unidentified; listed separately from the passage order.','']
        for i,n in enumerate(r['tokens']):own.append(dict(record=rec,segment='codes-'+r['page'],position=i+1,cipher=str(n),plain='?',grade='',coherent=False))
    (P/(f'R{rec}-tokens.txt' if rec=='7524' else f'R{rec}-cipher.txt')).write_text(' '.join(t['cipher'] for t in own)+'\n')
    tokens+=own
    summaries[rec]=dict(tokens=len(own),valued=sum(t['plain']!='?' for t in own),conservative_coherent=sum(t['coherent'] for t in own))
(P/'reading.md').write_text('\n'.join(md),encoding='utf8')
with (P/'reading-tokens.tsv').open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(tokens[0]),delimiter='\t');w.writeheader();w.writerows(tokens)
tot=len(tokens);val=sum(t['plain']!='?' for t in tokens)
summary=dict(documents=summaries,total=tot,valued=val,fraction_read=val/tot,conservative_coherent=sum(t['coherent'] for t in tokens),codes_open={'open':4,'total':4,'tokens_open':sum(len(r['tokens']) for r in codes)})
(P/'coverage.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
