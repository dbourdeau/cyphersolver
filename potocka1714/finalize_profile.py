from pathlib import Path
import sys,json,re,csv,collections
P=Path(__file__).parent;root=P.parent
sys.path.insert(0,str(root/'docs'))
import _check_profile as check
p=json.loads((P/'profile.json').read_text());cov=json.loads((P/'coverage.json').read_text())
for d in p['documents']:
    rid=d['id'];c=cov['documents'][rid[1:]];f=P/(rid+'-cipher.txt');m=check.measure(f,digits=True)
    d['length']=dict(tokens=m['tokens'],distinct=m['distinct'],unit='code groups',measured=True,file=f.name)
    d['language']='Polish and Latin' if rid=='R7524' else 'French and Polish' if rid=='R7526' else 'French (with Polish names and clear passages)'
    d['cleartext_in_document']='interspersed' if rid=='R7524' else 'mostly clear'
    d['plaintext']={'location':['none'],'source':'No contemporary decipherment visible in the available images; no independent edition located.'}
    d['transcription']=dict(by='llm from images',source='DECODE full-resolution images; image suffixes and anchors in reading.md',image_quality='fair',notes='Counts include isolated nomenclator figures and exclude clear text, dates and amounts. Literal values and editorial interpretations are separated.')
    d['read']='not read' if rid=='R7524' else 'read' if c['conservative_coherent']/c['tokens']>=.95 else 'read in part'
    if rid=='R7536':d.update(date='31 December 1716',year=1716,route='Vilna -> Warsaw')
    if rid=='R7535':d.update(date='18 January 1716',year=1716)
    if rid=='R7527':d.update(date='7 March 1716')
p['system']=dict(types=['homophonic','nomenclator','undetermined'],summary='Potocka uses a partly ordered numerical alphabet with doubled homophones and person codes; Mniszech uses a separate numerical system that remains undetermined.',symbol_kind='digits',digit_groups={'width':'2-3','separation':'mixed'},distinct_symbols='unknown',diacritics={'used':'unknown','note':'Small curves often distinguish figure 5; no established independent cipher function.'},homophones={'used':True},nomenclator={'present':True,'entries':4,'kinds':['names'],'unread_groups':4},nulls={'present':'unknown'},key_order='partly alphabetical',word_division='partial',notes='Counts and recovered structure describe Potocka; no key recovered for R7524. Do not double low values mechanically: e.g. 14=x but 28=b. Only listed key values are accepted.')
p['conditions']['tools']+=['Polish quintgram homophonic trials, tentative crib/null trials, regularized trial, synthetic control','prepare_reading.py; image re-reading']
for kind,what,result in [
('access','R7526 image manager supplied the missing spread; final image set is 29 across ten records.','worked'),
('verification','Full all-page audit added 22 R7527 reverse segments, corrected figures, and counted 23 standalone codes; final numeric transcription has 1119 tokens.','worked'),
('control','A 232-token synthetic Polish homophonic control with 75 observed symbols recovered only 49 positions (21.1%). Mniszech search failures are inconclusive, not evidence of impossibility.','failed'),
('reading','Recovered Potocka alphabet values 863/887 tokens across nine letters; literal readings retain doubtful spellings and unresolved names. R7524 remains unread.','partial')]:p['solution'].append(dict(date='2026-09-23',kind=kind,what=what,result=result))
gaps=[]
notes=(P/'NOTES.md').read_text(encoding='utf8').replace('ASang_teka_421/8','ASang_teka_422/6').replace('ASang_teka_421/9','ASang_teka_422/7').replace('The shelfmarks in this table must be checked against the saved metadata; `profile.json` retains the catalogue spellings.','The shelfmarks in this table have been checked against the saved metadata.')
(P/'NOTES.md').write_text(notes,encoding='utf8')
for line in notes.split('## Remaining gaps\n')[1].split('## Escalation')[0].splitlines():
    if line.startswith('- '):
        a,b=line[2:].split(' — blocker: ');block,detail=b.split(';',1);gaps.append(dict(item=a,blocker=block,detail=detail.strip()))
ts=list(csv.DictReader((P/'reading-tokens.tsv').open(),delimiter='\t'));grades=collections.Counter(t['grade'] for t in ts if t['grade'])
p['outcome']={'class':'read in part','key':'partial','fraction_read':cov['fraction_read'],'fraction_coherent':cov['conservative_coherent']/cov['total'],'fraction_read_method':'measured','fraction_read_source':'potocka1714/reading-tokens.tsv: 1119 cipher tokens, plain=? unread; fraction_coherent is a conservative lower bound excluding entire doubtful segments and two Polish names.','codes_open':cov['codes_open'],'grades':dict(grades),'verification':['key confirms','historical consistency'],'gaps':gaps,'notes':'863/887 Potocka tokens valued (97.3%), not equivalent to verified prose; 232/232 Mniszech tokens unvalued. No independent plaintext. Failed control limits the negative search inference.'}
(P/'profile.json').write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for d in p['documents']:print(d['id'],d['length']['tokens'],d['read'])
