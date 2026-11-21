"""Count exact, bounded reading.md words against the archived Revenga evidence."""
from pathlib import Path
import ast
import csv
from collections import Counter, defaultdict
import hashlib
import json
import re
import runpy

OUT = Path(__file__).resolve().parent
SRC = OUT.parent.parent
SECOND = SRC/'second_pass'
def table(path):
    return list(csv.DictReader((l for l in path.read_text().splitlines() if not l.startswith('#')), delimiter='\t'))

def dump(path, rows):
    with path.open('w') as handle:
        w = csv.DictWriter(handle, rows[0], delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def distances(x, y):
    d = [[0]*(len(y)+1) for _ in range(len(x)+1)]
    for i in range(len(x)+1): d[i][0] = i
    for j in range(len(y)+1): d[0][j] = j
    for i, a in enumerate(x, 1):
        for j, b in enumerate(y, 1):
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+(a!=b))
    return d

def forced_map(x, y):
    """Return matched locations shared by every minimum unit-cost edit path."""
    d, back = distances(x,y), distances(x[::-1], y[::-1])
    n,m=len(x),len(y)
    total=d[n][m]
    matched = {}
    for i,a in enumerate(x):
        candidates=set()
        for j in range(m+1):
            if d[i][j]+1+back[n-i-1][m-j]==total:
                candidates.add(None)
            if j<m and d[i][j]+(a!=y[j])+back[n-i-1][m-j-1]==total:
                candidates.add(j if a==y[j] else None)
        if len(candidates)==1 and None not in candidates:
            matched[i]=candidates.pop()
    return matched

def orthographic(s):
    return s.lower().translate(str.maketrans('áéíóú','aeiou'))
def reading_tokens(q):
    # Brackets are tracked across spaces. an[...] / [...]rados constitute fragments.
    out = []
    for part in re.findall(r'\[\?[^\]]+\]|(?:[^\W\d_]*\[\.\.\.\][^\W\d_]*|[^\W\d_]+)',q):
        if part.startswith('[?'):
            out += [(w,'bracketed') for w in re.findall(r'[^\W\d_]+',part)]
        else:
            out.append((part,'gap' if part=='[...]' else 'fragment' if '[' in part else ''))
    return out

def span_confirms(start,end,first,other,mapping):
    # Compare the delimiting signs as well as the word and reject an intervening insertion.
    indices=list(range(max(0,start-1), min(len(first),end+1)))
    loc=[mapping.get(i) for i in indices]
    if any(i is None for i in loc) or any(y!=x+1 for x,y in zip(loc,loc[1:])):
        return False
    return not (start==0 and loc[0]!=0 or end==len(first) and loc[-1]!=len(other)-1)

def spans(raw, key):
    parts=[]
    def add(lo,hi):
        if lo==hi: return
        s=''.join(raw[lo:hi]); plain=mechanical(s,key)
        parts.append((lo,hi,plain,s))
    start=0
    for i,t in enumerate(raw):
        if t in ('a',','):
            add(start,i);start=i+1
    add(start,len(raw))
    return parts

def mechanical(s,key):
    return ''.join(key.get(t,'[?]') for t in re.findall(r'\[[^\]]*\]|ll|.',s))

def main():
    inputs = [SRC/'reading.md', SRC/'key.txt', SRC/'transcription.txt', SRC/'decryption.txt',
              SRC/'decrypt.py', SECOND/'agreement_recount.py', SECOND/'agreement_positions.tsv',
              SECOND/'blind/transcription_blind.tsv',SECOND/'decryption_settled.tsv',
              SECOND/'transcription_settled.tsv',SECOND/'collation.tsv',SECOND/'corrections_check.tsv']
    key = next(ast.literal_eval(n.value) for n in ast.parse((SRC/'decrypt.py').read_text()).body
               if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='KEY')
    key['ll']=key.pop('S')
    firm = {l.split()[0] for l in (SRC/'key.txt').read_text().splitlines()
            if not l.startswith('#') and re.search(r'\bfirm\b', l)}
    first = {l.split('\t')[0]:l.split('\t')[2] for l in (SRC/'transcription.txt').read_text().splitlines() if re.match(r'C\d\d\t',l)}
    blind = {r['id']:r['cipher'] for r in table(SECOND/'blind/transcription_blind.tsv')}
    settled = {r['id']:r['cipher_settled'] for r in table(SECOND/'transcription_settled.tsv')}
    decode = {r['id']:r for r in table(SECOND/'decryption_settled.tsv')}
    published = re.findall(r'^(C\d+) [^\n]+\n  cipher: ([^\n]+)\n  plain:  ([^\n]+)',(SRC/'decryption.txt').read_text(),re.M)
    assert len(published)==len(first)==len(blind)==len(settled)==len(decode)==56
    for gid,raw,plain in published:
        assert first[gid]==raw and mechanical(raw,key)==plain, gid
    for gid, row in decode.items():
        assert row['cipher_settled']==settled[gid]
        # The settled output marks c -> plain ll with a capital L, and bare unknowns as ?.
        actual=''.join('[?]' if t.startswith('[') else 'L' if t=='c' else key.get(t,'?')
                       for t in re.findall(r'\[[^\]]*\]|ll|.',settled[gid]))
        assert actual==row['plain_mechanical'], (gid,actual,row['plain_mechanical'])
    tokens = runpy.run_path(str(SECOND/'agreement_recount.py'))['tokens']
    groups = defaultdict(list)
    for r in table(SECOND/'agreement_positions.tsv'):
        groups[(r['first_groups'],r['second_groups'])].append(r)
    prose=(SRC/'reading.md').read_text().split('## Fragment 1',1)[1]
    quotes=re.findall('«([^»]+)»',prose)
    # Group-to-quotation concordance from the surrounding clear text, checked against both passes.
    qi={i:[i] for i in range(1,8)} | {8:[8,9],9:[10],10:[11,12],11:[13],12:[14,15],13:[16],14:[17],15:[18],16:[19],17:[20],18:[21],19:[],20:[22],21:[23],22:[24],23:[25,26]}
    qi.update({i:[i+3] for i in range(24,55)})
    qi.update({55:[58],56:[]})
    assert [q for v in qi.values() for q in v] == list(range(1,len(quotes)+1))
    ledger=[]; group_ledger=[]
    for (cs,bs), rows in groups.items():
        cids=cs.split('+');bids=bs.split('+')
        qids=[idx for c in cids for idx in qi[int(c[1:])]]
        edited=[(q,i+1,t,flag) for q in qids for i,(t,flag) in enumerate(reading_tokens(quotes[q-1]))]
        a=[x[2] for x in tokens(''.join(first[g] for g in cids))]
        b=tokens(''.join(blind[g] for g in bids))
        z=[x[2] for x in tokens(''.join(settled[g] for g in bids))]
        certainty={int(r['first_pos'])-1:int(r['second_pos'])-1 for r in rows if r['sure_agree']=='1'}
        unique_b=forced_map(a,[x[2] for x in b])
        # Intersect the published blind alignment with placements forced even under alternative optimal paths.
        certainty={x:y for x,y in certainty.items() if unique_b.get(x)==y}
        sm=forced_map(a,z)
        words=spans(a,key)
        # A bracketed word is never an exact target. It may anchor sequence order by its displayed spelling.
        em=forced_map([orthographic(t) for _,_,t,_ in edited],[orthographic(w[2]) for w in words])
        group_ledger.append(dict(first=cs,second=bs,quotes=','.join(map(str,qids)),mechanical_slots=len(words),edited_items=len(edited)))
        for e,(q,i,t,flag) in enumerate(edited):
            state=flag or 'no_forced_exact_word'; start=end=cipher=plain=keys=''
            bstart=bend=zstart=zend=''
            if e in em:
                lo,hi,plain,cipher=words[em[e]];start,end=lo+1,hi
                glyphs=re.findall(r'\[[^\]]*\]|ll|.',cipher)
                keys=','.join(sorted(set(glyphs)-firm))
                if span_confirms(lo,hi,a,b,certainty): bstart,bend=certainty[lo]+1,certainty[hi-1]+1
                if span_confirms(lo,hi,a,z,sm): zstart,zend=sm[lo]+1,sm[hi-1]+1
                if not flag:
                    if not span_confirms(lo,hi,a,b,certainty):state='blind_sign_or_boundary'
                    elif not span_confirms(lo,hi,a,z,sm):state='settled_sign_or_boundary'
                    elif (cs=='C39' and lo==0) or (cs=='C55+C56' and hi==len(a)):state='fragment_edge'
                    elif t.lower()!=plain:state='editorial_accent'
                    elif keys:state='key_not_marked_firm'
                    else:state='sure'
            ledger.append(dict(first=cs,second=bs,quotation=q,word_in_quote=i,reading=t,disposition=state,first_start=start,first_end=end,blind_start=bstart,blind_end=bend,settled_start=zstart,settled_end=zend,cipher=cipher,mechanical=plain,values_without_firm_label=keys))
    for r in table(SECOND/'collation.tsv'):
        if r['method'] not in {'open','sense'} or not r['pos_C'].isdigit(): continue
        for w in ledger:
            if w['disposition']=='sure' and r['groups_C']==w['first']:
                assert not w['first_start']-1<=int(r['pos_C'])<=w['first_end']+1, (r['n'],w)
    dump(OUT/'words.tsv',ledger);dump(OUT/'groups.tsv',group_ledger)
    report=dict(counts=dict(Counter(r['disposition'] for r in ledger)), quotations=len(quotes),
                inputs={str(f.relative_to(SRC)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs})
    (OUT/'result.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['counts'])
if __name__=='__main__':main()
