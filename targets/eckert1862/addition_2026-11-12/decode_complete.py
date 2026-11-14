"""Complete line-preserving edition of five selected telegrams; no route reversal.
Use python3 -I targets/eckert1862/addition_2026-11-12/decode_complete.py.
Only exact selected-key matches and the listed morphology are substituted.
The frozen source inputs must hash-match before any output is generated.
An unmatched word is not thereby certified clear. English readings are separate.
"""
from pathlib import Path
import csv, hashlib, json, re
HERE=Path(__file__).resolve().parent
for row in (HERE/'INPUT_SHA256SUMS').read_text().splitlines():
    digest,name=row.split('  ',1)
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest, f'Input changed: {name}'
keys={n:{r['code'].lower():r for r in csv.DictReader((HERE/f'key_book{n}_selected.tsv').open(),delimiter='\t')} for n in [1,2]}
derived={'patenting':('patent','advancing'),'quickened':('quicken','detached'),'rewarding':('reward','following'),'swindled':('swindle','moved'),'jaunts':('jaunt',"Lee's"),'javelins':('javelin',"Lee's"),'horaces':('horace',"Richmond's"),'saints':('saint','forces'),'pacifics':('pacific','batteries'),'wafers':('wafer','rivers'),'widows':('widow','troops'),'tobsy':('topsy','12:30 p.m.'),'abbott':('abbot','James')}
unknown3={'pauline','quarrel','ink','rodneyed','abel','viola'}
ledger=[]; stats={}
for name,book,tail in [('U1',2,'nasty day this'),('U2',1,'Nothing about Devereux'),('McPhail',2,None),('Grant',2,'How you make it go'),('U3',None,'How is George')]:
    lines=(HERE/'transcription'/f'{name}.txt').read_text().splitlines(); out=[]; before=len(ledger)
    for i,line in enumerate(lines,1):
        tail_start=line.find(tail) if tail else -1
        def sub(m):
            w=m.group(); k=w.lower()
            if i==1 or (tail_start>=0 and m.start()>=tail_start): return w
            if name=='U3': return '[?'+w+']' if k in unknown3 else w
            if name=='McPhail' and w=='Baldwin': return w
            key=keys[book]
            if book==2 and k in derived: base,meaning=derived[k]; row=key[base]; method='explicit morphology or spelling variant'
            elif k in key: row=key[k]; meaning=row['meaning']; method='selected key entry'
            else: return w
            ledger.append([name,i,w,meaning,book,row['page'],method,row['note']])
            return '['+meaning+']'
        literal=re.sub(r'[A-Za-z]+',sub,line)
        out.extend([f'L{i:02d} cipher: {line}',f'L{i:02d} literal: {literal}',''])
    (HERE/'decoded'/f'{name}.txt').write_text('\n'.join(out)+'\n')
    stats[name]={'source_lines':len(lines),'substitutions':len(ledger)-before}
with (HERE/'applied_complete.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['message','line','cipher_word','meaning','book','key_page','method','note']);w.writerows(ledger)
# Regression comparisons concern evidence-sensitive claims, not grammar guesses.
assert len(ledger)==180, len(ledger)
assert keys[2]['java']['meaning']=='Johnston'
assert keys[2]['ink']['meaning']=='Beauregard'
assert keys[2]['topsy']['meaning']=='12:30 p.m.'
assert keys[1]['emily']['meaning']=='10 a.m.'
assert 'For Grant [Period]' in (HERE/'decoded/Grant.txt').read_text()
assert 'Elliotts' in (HERE/'decoded/Grant.txt').read_text()
assert all(r[2].lower() not in ['nasty','elliotts','dusty','whims','unity'] for r in ledger)
assert stats['U2']['substitutions']==4 and stats['U3']['substitutions']==0
assert (HERE/'decoded/U3.txt').read_text().count('[?')==6
# Portable legacy run must agree with the 176 Book2 substitution tuples (175 originally, plus Allen = 1 after the 13 Nov key correction).
old=list(csv.DictReader((HERE/'applied_key_ledger.tsv').open(),delimiter='\t'))
triples=lambda rows:[(r[2],r[3],str(r[5])) for r in rows]
assert triples([r for r in ledger if r[0] in ['U1','McPhail','Grant']])==[(r['cipher_word'],r['meaning'],r['key_page']) for r in old]
result={'inputs_hash_checked':True,'messages':stats,'selected_book2_entries':len(keys[2]),'selected_book1_entries':len(keys[1]),'total_substitutions':len(ledger),'legacy_substitution_sequence_preserved':True,'U3_unresolved_tokens':sorted(unknown3),'limitations':'Full source lines and substitutions, not proof every unmatched token is ordinary English; contextual punctuation and readings are separate.'}
(HERE/'complete_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
