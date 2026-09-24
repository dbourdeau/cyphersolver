"""Exploratory, sign-ID-only tests of one-sign word extensions.

Positive results concern ordered word-form structure, not affix meaning or
language identification. The null deliberately preserves sign frequencies by
position within each length class. A second null preserves each word's bag of
signs but destroys their order. Neither is a complete model of natural language.
"""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import random
import statistics

ROOT=Path(__file__).resolve().parent
REPLICATES=5000
SEED=20260923

def score(types):
    counts=[]
    for minimum in [2,3]:
        suffix=sum(len(w)>minimum and w[:-1] in types for w in types)
        prefix=sum(len(w)>minimum and w[1:] in types for w in types)
        counts.extend([suffix,prefix,suffix+prefix,suffix-prefix])
    return counts

NAMES=[f'{stat}_base_ge_{n}' for n in [2,3] for stat in ['suffix','prefix','either','suffix_minus_prefix']]

def shuffled(bylength,mode,rng):
    out=[]
    attempts=0
    for length,words in sorted(bylength.items()):
        # Rejection within independent length strata conditions each null on
        # the same number of distinct forms; collisions cannot shrink it.
        for attempt in range(10000):
            attempts+=1
            if mode=='within_word':
                proposed=[]
                for word in words:
                    w=list(word);rng.shuffle(w);proposed.append(tuple(w))
            else:
                cols=[list(col) for col in zip(*words)]
                for col in cols:rng.shuffle(col)
                proposed=list(zip(*cols))
            if len(set(proposed))==len(words):
                out.extend(proposed)
                break
        else:
            raise RuntimeError('Could not draw a unique-type conditional surrogate')
    return set(out),attempts

def run_null(types,mode):
    rng=random.Random(SEED)
    observed=score(set(types))
    bylength=defaultdict(list)
    for word in types:bylength[len(word)].append(word)
    samples=[];sizes=[];attempts=[]
    for _ in range(REPLICATES):
        null,draws=shuffled(bylength,mode,rng)
        assert len(null)==len(types)
        samples.append(score(null));sizes.append(len(null))
        attempts.append(draws)
    out={}
    for index,name in enumerate(NAMES):
        values=[s[index] for s in samples]
        obs=observed[index]
        if 'minus' in name:
            # Assess deviation from the null's centre in either direction.
            centre=statistics.mean(values)
            extreme=sum(abs(v-centre)>=abs(obs-centre) for v in values)
            tail='two-sided, absolute deviation from simulated mean'
        else:
            extreme=sum(v>=obs for v in values)
            tail='upper'
        out[name]={'observed':obs,'null_mean':statistics.mean(values),
            'null_sd':statistics.pstdev(values),'p_monte_carlo':(extreme+1)/(REPLICATES+1),
            'tail':tail,'null_min':min(values),'null_max':max(values)}
    return {'statistics':out,'unique_types_after_shuffle':{'min':min(sizes),'max':max(sizes),'mean':statistics.mean(sizes)},
            'length_stratum_draw_attempts':{'mean':statistics.mean(attempts),'max':max(attempts)},
            'uniqueness_control':'Reject collisions separately within each length class. All surrogates have the observed number of distinct types at every length.'}

def main():
    input_path=ROOT/'data/collated_words.json'
    rows=json.loads(input_path.read_text(encoding='utf8'))
    rows=[r for r in rows if r['eligible_for_conservative_test']]
    scenarios={'all_collated':rows,
       'haghia_triada_tablets':[r for r in rows if r['site']=='Haghia Triada' and r['support']=='Tablet'],
       'without_HT104':[r for r in rows if r['document']!='HT 104']}
    result={'seed':SEED,'replicates':REPLICATES,'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
       'design':'Exploratory. The candidate word families were inspected before these tests. No semantic labels enter scoring.',
       'interpretation_limits':['Relations can reflect morphology, related proper names, compound formation, spelling variation or segmentation.',
           'Sign confidence does not prove the word is complete.',
           'Same-object faces and same scribes are not independent observations; distinct types, not token frequencies, are scored.',
           'All 48 p-values (3 subsets x 2 nulls x 8 statistics) are reported; no isolated unadjusted p-value is a discovery.'],
       'scenarios':{}}
    for name,subset in scenarios.items():
        types=sorted({tuple(r['ids']) for r in subset})
        result['scenarios'][name]={'tokens':len(subset),'types':len(types),
            'position_by_length':run_null(types,'position_by_length'),
            'within_word':run_null(types,'within_word')}
    # Family-wise conservative adjustment across every statistic produced here.
    comparisons=len(scenarios)*2*len(NAMES)
    for scenario in result['scenarios'].values():
        for mode in ['position_by_length','within_word']:
            for v in scenario[mode]['statistics'].values():
                v['p_bonferroni_all_tests']=min(1,comparisons*v['p_monte_carlo'])
    bytype=defaultdict(list)
    for r in rows:bytype[tuple(r['ids'])].append({k:r[k] for k in ['document','site','scribe','word_index']})
    edges=[]
    for longer in sorted(bytype):
        for direction,base,extra in [('suffix',longer[:-1],longer[-1]),('prefix',longer[1:],longer[0])]:
            if len(base)>=2 and base in bytype:
                edges.append({'direction':direction,'base':base,'extended':longer,'extra_sign':extra,
                    'base_witnesses':bytype[base],'extended_witnesses':bytype[longer]})
    result['families']=edges
    (ROOT/'word_extension_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    for name,s in result['scenarios'].items():
        print(name,s['tokens'],'tokens',s['types'],'types')
        for mode in ['position_by_length','within_word']:
            print(mode,'surrogate type counts',s[mode]['unique_types_after_shuffle'])
            for stat in ['either_base_ge_2','either_base_ge_3','suffix_minus_prefix_base_ge_2']:
                x=s[mode]['statistics'][stat]
                print(stat,'observed',x['observed'],'null',round(x['null_mean'],2),'p',round(x['p_monte_carlo'],5),'adjusted',round(x['p_bonferroni_all_tests'],5))

if __name__=='__main__':main()
