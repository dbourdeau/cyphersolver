"""Replay the January and September comparisons using manuscript-derived text records."""
import argparse
import hashlib
import json
import math
import re
import runpy
import struct
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = HERE.parent
CORPUS = HERE.parents[3] / 'targets/edmondes1594/corpus/unton_cu31924027964471_djvu.txt'
CORPUS_HASH = '7529df2723f85388bb5c1e3073557a0d7641b2c59b094283521a53d95769c9bc'
M = runpy.run_path(str(HERE / 'matching.py'))
load = M['load']
normalize = M['normalized']


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def table97():
    return {r['tile']: (r['kind'], r['value']) for r in load(KEYS/'values.tsv') if r['key']=='97a'}


def direct(name):
    area = HERE/name
    if name == 'short':
        area = KEYS/'january_control'
        tables = [table97(), table97()]
        names = ['pass_a.tsv','pass_b.tsv']
    else:
        tables = [{r['tile']:(r['kind'],r['value']) for r in load(area/f'lookup_{k}.tsv')} for k in 'AB']
        names = ['pass_A.tsv','pass_B.tsv']
    a,b = [M['read_positions'](area/n, t) for n,t in zip(names,tables)]
    seq = []
    for _,x,y in M['align'](a,b):
        va,ca = a.get(x,('?', 'low'))
        vb,cb = b.get(y,('?', 'low'))
        left = tables[0].get(va)
        right = tables[1].get(vb)
        accepted = left is not None and left==right and ca!='low' and cb!='low' and left[0]!='special'
        seq.append(left if accepted else None)
    return seq, set(tables[0].values())


def model(path):
    if hashlib.sha256(path.read_bytes()).hexdigest()!=CORPUS_HASH:
        raise ValueError('Unexpected Unton corpus')
    counts = [Counter() for _ in range(5)]
    common = set('the and of to in that for his with he be it you my our this which was from have shall here hath your as by not unto they is'.split())
    for para in re.split(r'\n\s*\n',path.read_text(encoding='utf-8',errors='replace')):
        words = re.findall('[a-z]+',para.lower())
        if len(words)<12 or sum(w in common for w in words)<max(3,len(words)*.12):
            continue
        letters = normalize(''.join(words))
        for size in range(1,5):
            counts[size].update(letters[i:i+size] for i in range(len(letters)-size+1))
    total = sum(counts[1].values())
    assert total==735081
    alphabet_size = 24
    @lru_cache(None)
    def prob(gram):
        if len(gram)==1:
            return (counts[1][gram]+.1)/(total+.1*alphabet_size)
        n=len(gram)
        return (counts[n][gram]+10*prob(gram[1:]))/(counts[n-1][gram[:-1]]+10)
    @lru_cache(None)
    def logprob(gram):
        # The frozen experiment stored log probabilities in binary32.
        return struct.unpack('f',struct.pack('f',math.log(max(prob(gram),1e-14))))[0]
    return logprob


def check_language(name,lines,values,expected,logprob,is_control=False):
    pairs=[(a,b) for seq in lines for a,b in zip(seq,seq[1:]) if a and b]
    slots=sum(map(len,lines))
    used=sum(v is not None for seq in lines for v in seq)
    eligible=used>=.4*slots and len(pairs)>=10 and len(set(pairs))>=6
    def score(mapping):
        logs=[]
        for seq in lines:
            recent=''
            for unit in seq:
                if unit is None:
                    recent=''
                    continue
                text=mapping[unit]
                if recent:
                    logs.append(logprob(recent+text[0]))
                recent=(recent+text)[-3:]
        return math.fsum(logs)/len(logs) if logs else 0.
    actual=score({v:normalize(v[1]) for v in values if v[0]!='special'})
    controls=[score(m) for m in M['permutations'](values,15890911)]
    rank=sum(v>=actual for v in controls)
    status='insufficient coverage or pairs' if not eligible else 'pass' if rank<=(9 if is_control else 0) else 'miss'
    assert (slots,used,len(pairs),len(set(pairs)),rank,status)==tuple(expected[k] for k in ('slots','covered','pairs','distinct_pairs','equal_or_better','status'))
    assert abs(actual-expected['observed'])<1e-12 and abs(max(controls)-expected['best_shuffle'])<1e-12
    print(f'{name}: {used}/{slots}, {len(pairs)} pairs, {rank}/1000 equal or better; {status}.')


def compare_reference(seq,values):
    ref,_ = M['reference']((HERE/'january/reference.txt').read_text())
    toks = [normalize(v[1]) if v else None for v in seq]
    score,hits = M['match'](toks,ref)
    controls = [M['match']([m[v] if v else None for v in seq], ref)[0]
                for m in M['permutations'](values,15850105)]
    trace = load(HERE/'january/excerpts.tsv')
    assert list(hits)==[tuple(int(r[k]) for k in ('slot_start','ref_start','slot_end','ref_end')) for r in trace]
    assert all(r['normalized_match']==ref[int(r['ref_start'])-1:int(r['ref_end'])] for r in trace)
    saved = read_json(HERE/'january/reference_results.json')
    expected = saved['comparisons'][0]
    assert (score,max(controls),sum(n>=score for n in controls))==tuple(expected[k] for k in ('observed_characters','maximum_of_1000','equal_or_better'))
    criteria = {'coverage':sum(v is not None for v in seq)>=.4*len(seq),
                'pairs':sum(bool(a and b) for a,b in zip(seq,seq[1:]))>=5,
                'beats_shuffles':score>max(controls),'long_match':M['has_long_match'](seq,ref)}
    assert criteria==saved['criteria'] and all(criteria.values()) and saved['status']=='pass'
    print(f'January Chartley reference: {len(hits)} fragments, {score} characters, shuffled maximum {max(controls)}; pass.')


def legacy():
    values=table97()
    direct_lines=defaultdict(list)
    for r in load(HERE/'september/short_direct.tsv'):
        def choice(who):
            if r['tile_conf_'+who] not in ('high','medium') or r['shape_conf_'+who] not in ('high','medium'):
                return None
            if re.search(r'unclear|uncertain|possib|segment|boundar',r['shape_'+who],re.I):
                return None
            return values.get(r['tile_'+who])
        a,b=choice('a'),choice('b')
        direct_lines[r['line']].append(a if a==b else None)
    maps=[]
    for who in 'ab':
        maps.append({r['shape']:values.get(r['tile']) for r in load(KEYS/f'map_{who}.tsv')
                     if r['key']=='97a' and r['confidence'] in ('high','medium')})
    agreed={s:v for s,v in maps[0].items() if v and v==maps[1].get(s)}
    atlas=defaultdict(list)
    for r in load(KEYS.parent/'transcription/consensus.tsv'):
        if r['line'] not in ('U02','L08','U08'):
            atlas[r['line']].append(agreed.get(r['agreed']))
    return direct_lines,atlas


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus',type=Path,default=CORPUS)
    probability=model(parser.parse_args().corpus)
    jan=read_json(HERE/'january/language_results.json')
    seq,short=direct('short')
    check_language('January short table',[seq],short,jan['short'],probability,True)
    seq,full=direct('january')
    compare_reference(seq,full)
    check_language('January Chartley',[seq],full,jan['full'],probability,True)
    expected=read_json(HERE/'september/legacy_results.json')
    strips,atlas=legacy()
    check_language('September original strips',strips.values(),short,expected['direct_short'],probability)
    check_language('September atlas',atlas.values(),short,expected['atlas_short'],probability)
    seq,full=direct('september')
    check_language('September lower row four',[seq],full,read_json(HERE/'september/result.json'),probability)

if __name__=='__main__':
    main()
