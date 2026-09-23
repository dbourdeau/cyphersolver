from pathlib import Path
import json,csv,re
R=Path(__file__).resolve().parent.parent;D=R/'docs';P=R/'potocka1714';slug='potocka1714'
def load(f):return json.loads(f.read_text(encoding='utf8'))
def save(f,v):f.write_text(json.dumps(v,indent=1,ensure_ascii=False)+'\n',encoding='utf8')
manifest=D/'_build_site.py';s=manifest.read_text(encoding='utf8')
entry="""    dict(slug='potocka1714', label='Potocka and Mniszech to Dunin', year='1714&ndash;16 / undated', y=1715, place='Vilna and Dukla &rarr; Jakub Dunin', st='partial', stt='solved in part',
         title='Potocka and Mniszech to Dunin &mdash; a Polish postscript unlocks the French cipher',
         blurb='Polish monoalphabetic annealing recovered the Potocka alphabet; doubled homophones extend it across nine letters. 863/887 Potocka tokens have values, with uncertain names and four open person codes. Mniszech uses a separate unread system; the full group remains read in part.',
         quote='pan starosta &hellip; iest tu pytalam sie',
         rights='Archiwum Narodowe w Krakowie, Archiwum Sanguszk&oacute;w, via DECODE'),
"""
if "slug='potocka1714'" not in s:s=s.replace("    dict(slug='anne1711'",entry+"    dict(slug='anne1711'",1)
if "'potocka1714':" not in s:s=s.replace('IMAGES = {',"IMAGES = {'potocka1714': ('potocka1714_lead.jpg', 'R7526: the Polish postscript that yielded the alphabet.', 'Archiwum Narodowe w Krakowie, Archiwum Sanguszk&oacute;w, ASang_teka_343/12, DECODE R7526'), ",1)
manifest.write_text(s,encoding='utf8')
skip=load(D/'_explore_skip.json');skip.setdefault('portrait',{})[slug]='Commons searches found namesakes, not a verified public-domain portrait of Barbara Dunin Potocka or Jakub Antoni Dunin.';save(D/'_explore_skip.json',skip)
kw=load(D/'keys.json');kw.setdefault('unlinked',{})[slug]='Key recovered here from R7526 and transferred to eight other Potocka letters; no external named key used. Mniszech remains unkeyed.';save(D/'keys.json',kw)
atlas=load(D/'atlas.json');atlas['places'].setdefault('Vilna',[54.687,25.279]);atlas['letters']=[x for x in atlas['letters'] if x['slug']!=slug];atlas['letters'].append(dict(slug=slug,doc='R7536',year=1716.99,date='31 December 1716',**{'from':'Vilna','to':'Warsaw'},st='partial',label='Potocka to Dunin: security of correspondence'));save(D/'atlas.json',atlas)
result='**Read in part.** Potocka alphabet broken from the Polish R7526 postscript and transferred to eight French letters, including doubled homophones. 863/887 Potocka tokens valued (97.3%, not verified-prose coverage); 863/1,119 across all ten. Property, court influence and correspondence security. Four person codes, figure 73 and doubtful spellings remain open; Mniszech R7524 is unread and solver failure is inconclusive. No prior reading found; existence unknown.'
where='[`potocka1714/`](potocka1714/) · [write-up](https://dbourdeau.github.io/cyphersolver/potocka1714.html)'
target='Potocka and Mniszech → Jakub Dunin, Archiwum Sanguszków, DECODE R7524–7530 and R7534–7536 (catalogue 280, C; formerly N/A, placeholder dates on some records)'
f=R/'README.md';s=f.read_text(encoding='utf8');row=f'| {target} | 1714–16 and undated | 23 Sept 2026 | {result} | {where} |\n'
if 'potocka1714/' not in s:
    start=s.index('### Partly solved: key broken here, read in part');i=s.index('\n|---',start);i=s.index('\n',i+1)+1;s=s[:i]+row+s[i:]
f.write_text(s,encoding='utf8')
f=R/'SOLVED_CATALOGUE.md';s=f.read_text(encoding='utf8')
if 'potocka1714/' not in s:
    n=max(map(int,re.findall(r'^\| (\d+) \|',s,re.M)))+1
    i=s.index('\n|---',s.index('## 2. Partly read'));i=s.index('\n',i+1)+1
    row=f'| {n} | **{target}** | 1714–16 / undated | 23 Sept 2026 | **Read in part** | Polish R7526 postscript and cross-letter inference; 863/887 Potocka tokens valued, Mniszech unread. | Image transcription, language identification and key recovery; no independent clear copy. {where} |\n'
    s=s[:i]+row+s[i:]
f.write_text(s,encoding='utf8')
f=R/'SOLVED_RANKING.md';s=f.read_text(encoding='utf8')
if 'potocka1714.html' not in s:
    n=max(map(int,re.findall(r'\bp(\d+)\b',s)))+1
    s=s.replace('## Axes and weights',f'The **Potocka and Mniszech letters** are provisionally p{n} at **2.85**: an independently recovered bilingual alphabet, but one separate cipher remains unread and there is no independent plaintext.\n\n## Axes and weights',1)
    i=s.index('\n|---',s.index('## Composite ranking'));i=s.index('\n',i+1)+1
    s=s[:i]+f'| p{n} | **Potocka and Mniszech to Dunin** | 1714–16 / undated | 3 | 3 | 4 | 3 | 1 | 2 | **2.85** | Nine letters share the recovered alphabet; person codes and Mniszech remain open. [potocka1714](https://dbourdeau.github.io/cyphersolver/potocka1714.html) |\n'+s[i:]
    s+=f'\nPotocka and Mniszech provisional score (p{n}): 0.25×3 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×2 = **2.90**. Novelty remains provisional.\n'
    s=s.replace(f'p{n} at **2.85**',f'p{n} at **2.90**').replace('| 3 | 3 | 4 | 3 | 1 | 2 | **2.85**','| 3 | 3 | 4 | 3 | 1 | 2 | **2.90**')
f.write_text(s,encoding='utf8')
f=R/'TARGETS.md';s=f.read_text(encoding='utf8')
if 'potocka1714/' not in s:s=s.replace('## Done elsewhere in this repo','## Done elsewhere in this repo\n\nPotocka and Mniszech to Dunin (catalogue 280): Potocka alphabet recovered, group read in part; Mniszech R7524 remains open. '+where+'\n',1)
f.write_text(s,encoding='utf8')
cat=load(R/'catalogue.json');e=next(x for x in cat['entries'] if x['id']==280)
e.update(title='Mniszech to Jakub Dunin, Crown regent',correspondents='Józef Mniszech → Jakub Dunin',year=1714,date='1714',place='Dukla → Poland',language='Polish',shelfmark='Archiwum Narodowe Kraków, Archiwum Sanguszków, ASang_teka_290/6',decode_ids=[7524],links=[x for x in e['links'] if '7524' in x['href']],status='R7524 remains unread: 232 cipher tokens transcribed, separate numerical system. No matching key or decipherment found; solver failed its synthetic control, so the negative result is inconclusive. Nine Potocka siblings transferred to potocka1714, alphabet recovered (863/887 tokens valued), person codes and uncertain readings open.',outcome='attempted, open',seen='image',verify='Stronger Polish homophonic or syllabic attack, or additional same-key correspondence; see potocka1714/NOTES.md.')
save(R/'catalogue.json',cat)
f=R/'CATALOGUE.md';s=f.read_text(encoding='utf8');needle='## Read or resolved here, and removed'
if 'potocka1714' not in s:s=s.replace(needle,needle+'\n\nItem **280** narrowed to Mniszech R7524; nine Potocka letters removed to [potocka1714](https://dbourdeau.github.io/cyphersolver/potocka1714.html), alphabet recovered, readings with explicit gaps.\n',1)
f.write_text(s,encoding='utf8')
f=D/'index.html';s=f.read_text(encoding='utf8')
if '<b>Potocka and Mniszech to Dunin, 1714–16 and undated</b>' not in s:s=s.replace('<ul class="findings">','<ul class="findings">\n<li><b>Potocka and Mniszech to Dunin, 1714–16 and undated</b> — <span class="fnd">A Polish postscript unlocks nine letters’ alphabet.</span> Four person codes and Mniszech’s separate cipher remain open. <a href="potocka1714.html">write-up</a></li>',1)
f.write_text(s,encoding='utf8')
# Queue public extracts. Clear prose not transcribed is represented by gaps.
q=load(R/'decode_updates/queue.json');t=q['targets'][slug];t['key']={'file':'potocka1714/key-potocka.json','lang':'PL/FR','how':'Recovered here from R7526 by Polish monoalphabetic annealing and cross-letter inference.'};t['cite']=None;t['fields']={}
rows=list(csv.DictReader((P/'potocka-segments.tsv').open(encoding='utf8'),delimiter='\t'));key=load(P/'key-potocka.json')
for rid,d in t['records'].items():
    if rid=='R7524':
        d.update(proposed='Non-decrypted',note='Separate numerical cipher, 232 tokens transcribed; no coherent decipherment. Search failure is inconclusive because the synthetic control also failed.',reading=None,reading_not_needed=True,key={'none':'No matching key recovered.'},transcription=['potocka1714/r7524-cipher.txt']);continue
    content=[]
    if rid=='R7526':
        content=['[spread, right page]','Pan starosta serecki? iest tu. Pytalam sie iezeli ma co postanowionego.','Ni ma nic. Iedzie dzie? do Lublina. To tesz prawda ze byl u dominikanow','wtenczas iak estancowal z nia w polu. Powiedal mi p. Tabrowski?','[...]']
    else:
        last=None
        for r in sorted([x for x in rows if x['record']==rid[1:]],key=lambda x:x['page']):
            if last!=r['page']:content.append('[p. '+r['page']+']');last=r['page']
            raw=''.join(key.get(n,'<'+n+'>') for n in r['cipher'].split());proposal=re.split(r'[(:;]',r['reading_note'])[0].strip()
            words=proposal if re.sub('[^a-z]','',proposal.lower())==re.sub('[^a-z]','',raw.lower()) else raw+'?'
            anchor=r['context'].replace('...','[...]');anchor=re.sub(r'\[(\d+)\]',r'<\1>',anchor)
            if anchor=='title continued':anchor='[...]'
            content+=['[clear: '+anchor+']',words,'[...]']
    f=R/'decode_updates/decryptions'/f'{rid}.txt';f.write_text('\n'.join(content)+'\n',encoding='utf8')
    d.update(proposed='Partially decrypted',note='Numerical alphabet recovered; reading file supplies cipher-passage extracts only. Standalone person codes, doubtful spellings and names remain open; 97.3% valued is group key coverage, not verified-prose coverage.',reading=[{'file':str(f.relative_to(R)).replace('\\','/')}],fields={'cipher type':'Numerical homophonic substitution with person codes','plaintext language':'Polish' if rid=='R7526' else 'French with Polish names'})
save(R/'decode_updates/queue.json',q)
# Prevent local source images or authenticated pages being staged by later sessions.
(P/'.gitignore').write_text('*.html\n*.jpg\n*.png\nTH_*\n')
