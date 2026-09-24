"""Recover SigLA word positions and compare editions without assigning meanings."""
from collections import Counter, defaultdict
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import re
import unicodedata as ud
from urllib.parse import quote
import urllib.request
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent

def canonical(char):
    name=ud.name(char,'')
    m=re.fullmatch(r'LINEAR A SIGN (AB|A)(\d+)([A-Z]*)',name)
    if not m:
        return None
    # Variant letters are kept separately by the source. Basic sign identity
    # comparison here does not establish identity of function or sound.
    return f'{m[1]}{int(m[2]):03d}'

def doc_key(name):
    return name.replace(' ','')

def groups(document):
    byword=defaultdict(list)
    roles=Counter()
    for a in document['attestations']:
        role,flag=a['function_or_bounds_raw']['fields']
        if isinstance(role,dict):
            offset,word_number=role['fields']
            byword[word_number].append((offset,a))
            roles['syllabogram']+=1
        else:
            roles[{0:'logogram',1:'fraction',2:'transaction',3:'unknown'}[role]]+=1
    out=[]
    for number,entries in sorted(byword.items()):
        entries.sort(key=lambda pair:pair[0])
        assert [p for p,a in entries]==list(range(len(entries)))
        atts=[a for p,a in entries]
        out.append({'word_index':number,'ids':[a['sign_id'] for a in atts],
            'attestations':[a['n'] for a in atts],
            'confident_signs':all(a['confidence_raw']==1 for a in atts),
            'unmarked':all(a['erasure_raw']==0 and a['ghost_raw']==0 for a in atts),
            'confidence_raw':[a['confidence_raw'] for a in atts]})
    return out,roles

def rendered_checks():
    cases=[('HT 13','index-word-0.html','ka-u-de-ta'),
           ('HT 13','index-word-7.html','ku-ro'),
           ('HT 13','index-5.html','Logogram'),
           ('HT 13','index-6.html','Transaction sign'),
           ('HT 13','index-9.html','Fraction'),
           ('HT 37','index-17.html','unsure-reading')]
    result=[]
    for name,page,expected in cases:
        url='https://sigla.phis.me/document/'+quote(name,safe='')+'/'+page
        cache=ROOT/'data'/('sigla_'+name.replace(' ','_')+'_'+page)
        if not cache.exists():
            cache.write_bytes(urllib.request.urlopen(url,timeout=25).read())
        raw=cache.read_bytes(); soup=BeautifulSoup(raw,'html.parser')
        if 'word-' in page:
            element=soup.select_one('.info-title')
            panel=soup.select_one('[id^=word-]')
            assert panel is not None
            shown=''.join(panel.get_text('',strip=True).split())
            ok=expected in shown
        elif expected=='unsure-reading':
            panel=soup.select_one('#occ-17 .unsure-reading')
            shown=panel.get_text('',strip=True) if panel else ''
            ok=shown=='na'
        else:
            shown=soup.select_one('.role').get_text(' ',strip=True)
            ok=shown==expected
        assert ok,(url,shown,expected)
        result.append({'url':url,'expected':expected,'observed':shown,'passed':ok,
            'sha256':hashlib.sha256(raw).hexdigest()})
    return result

def main():
    sigla=json.loads((ROOT/'data/sigla_decoded.json').read_text(encoding='utf8'))
    corpus=json.loads((ROOT/'data/corpus.json').read_text(encoding='utf8'))
    source=defaultdict(list)
    for r in corpus:source[doc_key(r['name'])].append(r)
    totals=Counter();roles=Counter();collected=[];unmatched=[];collated=[]
    for d in sigla:
        words,localroles=groups(d)
        roles.update(localroles)
        totals['word_groups']+=len(words)
        totals['confident_unmarked_groups']+=sum(w['confident_signs'] and w['unmarked'] for w in words)
        multi=[w for w in words if len(w['ids'])>=2]
        totals['multi_sign_groups']+=len(multi)
        totals['confident_unmarked_multi_sign_groups']+=sum(w['confident_signs'] and w['unmarked'] for w in multi)
        collected.append({'name':d['name'],'site':d['site'],'words':words})
        matches=source.get(doc_key(d['name']),[])
        if len(matches)!=1:
            continue
        r=matches[0]
        totals['shared_unique_document_names']+=1
        srcwords=[]
        for idx,raw in enumerate(r['words']):
            ids=[canonical(c) for c in raw if canonical(c)]
            if len(ids)>=2:
                srcwords.append({'index':idx,'ids':ids,'raw':raw,
                    'clear':all(canonical(c) is not None for c in raw)})
        seq1=[tuple(w['ids']) for w in multi]
        seq2=[tuple(w['ids']) for w in srcwords]
        matching=set()
        for block in SequenceMatcher(None,seq1,seq2,autojunk=False).get_matching_blocks():
            for k in range(block.size):
                a,b=multi[block.a+k],srcwords[block.b+k]
                matching.add(block.a+k)
                strong=a['confident_signs'] and a['unmarked'] and b['clear']
                totals['matched_multi_sign_tokens']+=1
                totals['matched_confident_clear_tokens']+=int(strong)
                collated.append({'document':d['name'],'site':d['site'], 'support':r['support'],
                    'scribe':r['scribe'],'word_index':a['word_index'],'ids':a['ids'],
                    'sigla_confidence':a['confidence_raw'],'source_clear':b['clear'],
                    'eligible_for_conservative_test':strong,
                    'source_index':b['index'],'sigla_attestations':a['attestations']})
        for i,w in enumerate(multi):
            if i not in matching:
                unmatched.append({'document':d['name'],**w})
    (ROOT/'data/sigla_words.json').write_text(json.dumps(collected,ensure_ascii=False,indent=2),encoding='utf8')
    (ROOT/'data/collated_words.json').write_text(json.dumps(collated,ensure_ascii=False,indent=2),encoding='utf8')
    (ROOT/'data/sigla_unmatched_words.json').write_text(json.dumps(unmatched,ensure_ascii=False,indent=2),encoding='utf8')
    result={'counts':dict(totals),'roles':dict(roles),'rendered_checks':rendered_checks(),
        'field_interpretation':'Nested pair is (zero-based sign position within word, zero-based word index), NOT start/end boundary states. Verified against rendered HT13 word pages and all-group contiguous offsets.',
        'limitations':['SigLA sign confidence is not phonetic certainty or word completeness.',
            'Integer quantity strokes are not included in this SigLA sign inventory; arithmetic still needs numerical source collation.',
            'Both editions largely derive from GORILA, so their agreement is transcription corroboration, not independent linguistic evidence.',
            'Exact-name matching omits aliases such as HT123+124a versus HT123a.',
            'An unmatched sequence is not automatically a source error. Ligatures, variants, function and segmentation can differ.'],
        'data_license':'SigLA and derivative word records: CC BY-NC-SA 4.0, Salgarella & Castellan; derived datasets are local in ignored data/.'}
    (ROOT/'sigla_collation_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'counts':dict(totals),'roles':dict(roles),'rendered_checks_passed':len(result['rendered_checks'])},indent=2))

if __name__=='__main__':main()
