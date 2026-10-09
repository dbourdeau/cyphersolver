#!/usr/bin/env python3
"""Reproduce this review from read-only inputs. Writes only beside this script."""
from pathlib import Path
from collections import Counter,defaultdict
import re,csv,json,hashlib
R=Path(__file__).resolve().parent; P=R.parent
M=P.parent/'erving1807'/'erving_groups.txt'
def norm(g,v):
    v=v.lower().replace('’',"'").rstrip("'")
    v=re.sub(r'\(.*?\)','',v).replace('?','')
    if ('^' in g or 'Δ' in g) and v.endswith('s'):v=v[:-1]
    return v
def base(g):return g.replace('^','').replace('Δ','').replace('#','')
def usable(v):return v!='X' and '?' not in v
A=[]
for ln,l in enumerate((P/'aligned.txt').read_text().splitlines(),1):
    if l.startswith('#') or '|' not in l:continue
    ref,s=l.split('|',1)
    for j,(g,v) in enumerate(re.findall(r'(\S+)=(\S+)',s),1):
        A.append(dict(id=len(A)+1,ref=ref.strip(),position=j,line=ln,group=g,base=base(g),value=v,norm=norm(g,v)))
K={r[0]:r for r in csv.reader((P/'key_pinckney.tsv').read_text().splitlines(),delimiter='\t') if r and not r[0].startswith('#')}
W=defaultdict(set); Wraw=defaultdict(list)
for g,v in re.findall(r'(\d+[Δ?]?)=(\S*)','\n'.join(l for l in (P/'wagner_pairs.txt').read_text().splitlines() if not l.startswith('#'))):
    Wraw[base(g)].append(v)
    if v and '?' not in g+v:
        for variant in v.split('/'):W[base(g)].add(norm(g,variant))
E=defaultdict(set);external_rows=[]
ml=M.read_text().splitlines()
for l in (R/'march_segments.tsv').read_text().splitlines():
    if not l or l.startswith('#'):continue
    seq,vs=l.split('\t');gs=seq.split('.');vs=vs.split()
    assert len(gs)==len(vs),(seq,vs)
    hits=[(i,x) for i,x in enumerate(ml,1) if not x.startswith('#') and seq in x.split('|')[0]]
    assert hits,seq
    ln,source=hits[0]
    for g,v in zip(gs,vs):
        E[g].add(norm(g,v));external_rows.append([g,v,ln,source])
# Explicit scalar mapping in March notes, kept separate from word segmentation.
E['38'].add('ly')
external_rows.append(['38','ly',next(i for i,l in enumerate(ml,1) if '38=ly' in l),'explicit note: 38=ly'])
for g,values in W.items():
    for v in values:external_rows.append([g,v,'Wagner','wagner_pairs.txt'])
EX={g:E[g]|W[g] for g in set(E)|set(W)}
counts=Counter(a['base'] for a in A)
vc=Counter((a['base'],a['norm']) for a in A if a['base'].isdigit() and usable(a['value']))
shared=sorted(set(counts)&set(Wraw),key=lambda x:int(x) if x.isdigit() else 99999)
# Known alternate values from the file or a clear word in March; do not call these a fixed-key decoding.
# These occurrences remain intelligible only by contextual emendation or a new segmentation.
# Only clear collisions: 66 in/West vs ing; 310 ceiv vs liev; 665 change vs were;
# 943 er vs ly; 870 they vs their. Others are catalogued but not adjudicated as errors.
emend={(a['ref'],a['group'],a['value']) for a in A if
    (a['base']=='66' and a['value']!='ing') or
    (a['base']=='310' and a['value']=='ceiv') or
    (a['base']=='665' and a['value'].startswith('change')) or
    (a['base']=='943' and a['value'].startswith('er')) or
    (a['base']=='870' and a['value'].startswith('they'))}
for a in A:
    g,v=a['base'],a['norm'];ok=usable(a['value']) and g.isdigit()
    a['external']=ok and v in EX.get(g,set())
    a['repeat_same_value']=ok and vc[g,v]>=2
    a['loo']=a['external'] or a['repeat_same_value']
    a['nominal_read']=usable(a['value'])
    a['image_secure']=a['nominal_read'] and '#' not in a['group']
    a['unemended_image_secure']=a['image_secure'] and (a['ref'],a['group'],a['value']) not in emend
n=len(A)
def stat(k):
    c=sum(a[k] for a in A);return dict(tokens=c,percent=round(100*c/n,4))
# Overlap is an upper bound for external identity, not proof of its proposed value.
marchgroups=set(re.findall(r'\d+', '\n'.join(l.split('|')[0] for l in ml if not l.startswith('#'))))
summary={'tokens':n,'key_rows':len(K),'numeric_types_in_alignment':len({a['base'] for a in A if a['base'].isdigit()}),
'unknown_values':sum(a['value']=='X' for a in A),'conjecture_values':sum('?' in a['value'] for a in A),
'hidden_marked':sum('#' in a['group'] for a in A),
'99pct_non_X':sum(a['value']!='X' for a in A),
'claimed_recurrence_or_Wagner_any_value':sum(counts[a['base']]>=2 or a['base'] in shared for a in A),
'external':stat('external'),'repeat_same_value':stat('repeat_same_value'),'leave_one_out':stat('loo'),
'nominal_read':stat('nominal_read'),'image_secure':stat('image_secure'),'unemended_image_secure':stat('unemended_image_secure'),
'external_supported_types':len({a['base'] for a in A if a['external']}),
'external_overlap_upper_tokens':sum(a['base'] in marchgroups or a['base'] in Wraw for a in A),
'wagner_shared_types':len(shared),'wagner_shared_tokens':sum(counts[g] for g in shared),
'wagner_agree_value_tokens':sum(usable(a['value']) and a['norm'] in W.get(a['base'],set()) for a in A),
'emendations':[(a['id'],a['group'],a['value']) for a in A if (a['ref'],a['group'],a['value']) in emend]}
# Compatible type check permits any listed alternative, but no guesses. 584 is 'nation' in alignment,
# 'na' in key and 'nations?' in Wagner: exclude it, along with unvalued 943.
ks={g:{norm('',x) for x in K[g][1].split('/')} for g in shared}
ks['248'].add('tion');ks['424'].add('ion')
compatible={g for g in shared if ks[g]&W[g]}
summary['wagner_definite_compatible_types']=len(compatible)
summary['wagner_indeterminate_types']={g:dict(key=K[g][1],wagner=Wraw[g]) for g in shared if g not in compatible}
# Toy chance model: permute the definite Wagner value sets among their labels, preserving marginal values.
# Not a contextual null or p-value: no record of withheld labels/context exists.
scorable=[g for g in shared if W[g]]
summary['toy_permutation_expected_matches']=sum(bool(ks[g]&W[h]) for g in scorable for h in scorable)/len(scorable)
summary['toy_permutation_n']=len(scorable)
with (R/'token_audit.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(A[0]),delimiter='\t');w.writeheader();w.writerows(A)
with (R/'external_evidence.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['group','value','source_line','source']);w.writerows(external_rows)
with (R/'wagner_audit.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['group','key_value','aligned_values','Wagner_values','definite_compatible','tokens'])
    for g in shared:w.writerow([g,K[g][1],'/'.join(sorted({a['value'] for a in A if a['base']==g})),Wraw[g],g in compatible,counts[g]])
with (R/'value_recurrence.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['group','value','occurrences','external_supported','LOO','refs'])
    for (g,v),c in sorted(vc.items(),key=lambda x:(int(x[0][0]),x[0][1])):
        w.writerow([g,v,c,v in EX.get(g,set()),c>=2 or v in EX.get(g,set()),','.join(a['ref'] for a in A if a['base']==g and a['norm']==v)])
summary['input_hashes']={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [P/'aligned.txt',P/'transcription.txt',P/'key_pinckney.tsv',P/'wagner_pairs.txt',P/'reading.txt',P/'fo_99-01-02-1993.txt',M]}
(R/'metrics.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='input_hashes'},indent=2))
