#!/usr/bin/env python3
"""Independently reconstruct scores and report search-adjusted shuffle controls."""
import csv, json, math, pathlib, re, itertools, collections
import numpy as np
D=pathlib.Path(__file__).resolve().parent
meta=json.loads((D/'model_metadata.json').read_text()); tables=json.loads((D/'normalized_tables.json').read_text())
data=(D/'search_input.txt').read_text().split(); pos=0
n=int(data[pos]);pos+=1;ct=list(map(int,data[pos:pos+n]));pos+=n
uni=np.array(list(map(float,data[pos:pos+27])));pos+=27
lp=np.array(list(map(float,data[pos:pos+729]))).reshape(27,27);pos+=729
values=sorted(set(ct)); sm=[x for x in values if x<100];lg=[x for x in values if x>=100]
perms=list(itertools.permutations(range(4)))
def transform(f,id,N):
    wrap=lambda x:x%N+1
    if f=='direct_shift':
        k=id-1899; return [x+k for x in values],{'k':k}
    if f=='modular_shift':return [wrap(x-1+id) for x in values],{'k':id}
    if f=='reverse_digits':return [int(str(x)[::-1]) for x in values],{}
    if f=='digit_permutation':
        perm=perms[id];return [int(''.join(f'{x:04d}'[j] for j in perm)) for x in values],{'permutation':perm}
    if f=='decimal_offsets':
        ds=f'{id:04d}';return [int(''.join(str((int(a)+int(b))%10) for a,b in zip(f'{x:04d}',ds))) for x in values],{'offsets_thousands_to_units':ds}
    if f=='split_modular_shift':
        a,b=divmod(id,N);return [wrap(x-1+(a if x<100 else b)) for x in values],{'k_small':a,'k_large':b}
    if f=='affine_modular':
        aa=[a for a in range(1,N) if math.gcd(a,N)==1];a,b=aa[id//N],id%N
        return [wrap(a*(x-1)+b) for x in values],{'a':a,'b':b}
    lo=1-max(lg); width=N-min(lg)-lo+1
    a,b=1-max(sm)+id//width,lo+id%width
    return [x+(a if x<100 else b) for x in values],{'k_small':a,'k_large':b}

def norm(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFKD',s.lower()) if 'a'<=c<='z')

def score(mapping,key,seq):
    stream=''.join(norm(key.get(str(mapping[i]),'')) or '?????' for i in seq)
    codes=np.array([ord(c)-97 if c!='?' else 26 for c in stream])
    return float((uni[codes[0]]+lp[codes[:-1],codes[1:]].sum())/len(codes))
report={'metadata':meta,'families':{},'best_per_code':{},'function_word_checks':{},'top3':[]};zs=[];observedz=[];all_candidates=[];maxerr=0
for name,t in tables.items():
    N=t['modulus'];key=t['entries'];seq=np.loadtxt(D/f'shuffle_indices_{name}.txt',dtype=int)
    families=collections.defaultdict(list)
    for r in csv.DictReader((D/f'raw_results_{name}.tsv').open(),delimiter='\t'):families[r['family']].append(r)
    arr=[]
    for f,rows in families.items():
        assert len(rows)==201
        scores=np.array([float(r['score']) for r in rows]); mu=float(scores[1:].mean());sd=float(scores[1:].std(ddof=1));z=(scores[0]-mu)/sd
        for r in rows:
            mapping,params=transform(f,int(r['id']),N)
            maxerr=max(maxerr,abs(score(mapping,key,seq[int(r['control'])])-float(r['score'])))
        mapping,params=transform(f,int(rows[0]['id']),N)
        dec=[key.get(str(mapping[i]),'?') for i in seq[0]]
        known=sum(bool(norm(x)) for x in dec)/len(dec)
        rec={'score':float(scores[0]),'shuffle_mean':mu,'shuffle_sd':sd,'z':z,'empirical_p':float((1+sum(scores[1:]>=scores[0]))/201),'parameters':params,'coverage':known,'sample':' | '.join(dec[:30]),'full_decode':dec,'small_group_mapping':{str(x):key.get(str(mapping[values.index(x)]),'?') for x in [17,18,38,1,14]}}
        report['families'][name+'/'+f]=rec;arr.append(scores);zs.append((scores[1:]-mu)/sd);observedz.append(z)
    arr=np.array(arr);bestf=list(families)[int(arr[:,0].argmax())];mx=arr.max(axis=0);mu=mx[1:].mean();sd=mx[1:].std(ddof=1)
    report['best_per_code'][name]={**report['families'][name+'/'+bestf],'family':bestf,'all_families_shuffle_mean':float(mu),'all_families_shuffle_sd':float(sd),'all_families_z':float((mx[0]-mu)/sd),'all_families_p':float((1+sum(mx[1:]>=mx[0]))/201)}
    report['function_word_checks'][name]=[]
    for r in csv.DictReader((D/f'function_hits_{name}.tsv').open(),delimiter='\t'):
        mapping,params=transform(r['family'],int(r['id']),N)
        report['function_word_checks'][name].append({**r,'parameters':params,'example':{str(x):key.get(str(mapping[values.index(x)]),'?') for x in [17,18,38,1,14]}})
    for r in csv.DictReader((D/f'top_candidates_{name}.tsv').open(),delimiter='\t'):
        mapping,params=transform(r['family'],int(r['id']),N)
        dec=[key.get(str(mapping[i]),'?') for i in seq[0]]
        all_candidates.append({'code':name,'family':r['family'],'score':float(r['score']),'parameters':params,'sample':' | '.join(dec[:18]),'stream_sample':''.join(norm(x) or '?????' for x in dec)[:160],'full_decode':dec})
assert maxerr<1e-9,maxerr
unique={}
for r in sorted(all_candidates,key=lambda r:-r['score']):
    signature=tuple(r['full_decode'])
    if signature not in unique:unique[signature]=r
report['top3']=list(unique.values())[:3]
for candidate in report['top3']:
    null=report['best_per_code'][candidate['code']]
    candidate['z_against_full_search_controls']=(candidate['score']-null['all_families_shuffle_mean'])/null['all_families_shuffle_sd']
nullmax=np.array(zs).max(axis=0);obs=max(observedz)
report['across_16_family_max_z']={'observed':obs,'empirical_p':float((1+sum(nullmax>=obs))/201),'null_max_z':nullmax.tolist(),'note':'Exploratory empirical max of family-standardized scores, using the same 200 permutations across both tables.'}
report['validation']={'independent_score_max_abs_error':maxerr,'reconstructed_winners':201*len(zs)}
(D/'results.json').write_text(json.dumps(report,indent=2))
with (D/'family_summary.tsv').open('w') as f:
    f.write('code_family\tscore\tshuffle_mean\tshuffle_sd\tz\tempirical_p\tparameters\n')
    for k,r in report['families'].items():f.write('\t'.join(map(str,[k,r['score'],r['shuffle_mean'],r['shuffle_sd'],r['z'],r['empirical_p'],r['parameters']]))+'\n')
print(json.dumps({k:v for k,v in report.items() if k in ['best_per_code','top3','validation']},indent=2)[:9000])
print('Across 16 families max-z empirical p:',report['across_16_family_max_z']['empirical_p'])
