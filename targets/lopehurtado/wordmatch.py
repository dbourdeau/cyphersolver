# -*- coding: utf-8 -*-
"""Candidate words for an unread spelled run (2026-10-03).
Each sign maps to the SET of letters it has been read as anywhere in the 1522 hand (glyph confusions at DECODE
resolution included); every expansion is looked up in a Spanish word list (Quijote, Vasto memorias, Gutenberg
Spanish, and the clear text of the Hurtado letters), normalised early (j->i, v->u, accents off, ç->c, y->i).
A hit is a candidate only: it is accepted in a reading when it also fits the sentence.
  python wordmatch.py "ϑ α 8 ɋ 7"        # one run
  python wordmatch.py --all r9634        # every {..} run in r9634_reading.tsv"""
import sys, io, os, re, itertools, collections, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
S0 = {'7':'a','ß':'a','Ho':'a','℔':'a','ʃʃ':'a','8':'et','H':'e','oo':'e','ɣ̊':'r','ʇʇ':'r','ρρ':'r','ϑ':'tdnc','b':'tc',
     '∠':'u','α':'i','ω':'inc','∞':'i','4':'n','&':'os','x':'d','9':'dnlc','σ':'d','c':'s','r':'s','∂':'sptdo','ɣ':'cng',
     'y':'oc','ϯ':'mx','ʇ':'m','ʋ':'m','ɭb':'p','⊃':'p','∂̶':'p','ε':'lg','Ɛ':'lgi','#':'f','m̶':'f','(':'f','ɡ':'g','ɣ̶':'g',
     'ɋ':'rcp','ϙ':'rcp','z':'ns','m':'o','ʙ':'b','ʇʇʇ':'b','δ':'st','3':'h','ɷ':'il','ʒ':'pcrs','ɲ':'q','v':'g','⊤':'us',
     'ɩ':'il','ɀ':'n','ɸ':'uf','t':'m','f':'c','q':'l','L':'r','♀':'xz','⅋':'x','ϭ':'s','6':'d','φ':'u','ʑ':'i','⁝':'z',
     'e':'e','ɕ':'s','∆':'d','ʆ':'s','ʄ':'i'}
S = {k: list(v) for k, v in S0.items()}
for k in ('ʇʇ', 'ɋ', 'ϙ', 'ɣ̊'): S[k] = S[k] + ['rr']
S['ɷ'] = ['i', 'll']
C = {'zar':['de'],'zarε':['del'],'ton':['que'],'xul':['lo'],'xug':['la'],'xuɡ':['la'],'ʃu':['se','so'],'ʃop':['bi'],
     'xor':['mu'],'zil':['con'],'yuc':['en'],'xu':['ha'],'ʃed':['su'],'tef':['nec'],'zuc':['assi'],'zar∂':['des'],
     'xur':['na'],'zun':['da'],'xod':['fe','he'],'xic':['ha'],'ye':['dizi'],'xar':['mo'],'ʃad':['so'],'ʃan':['ba'],
     'ʃil':['toma'],'ʃal':['esta'],'yof':['esta'],'yaf':['es'],'sub':['si'],'ʃub':['si'],'tu':['no'],'yo':['dicho'],'xi':['ha']}
def norm(w):
    w = unicodedata.normalize('NFD', w.lower()); w = ''.join(ch for ch in w if unicodedata.category(ch) != 'Mn')
    return w.replace('j','i').replace('v','u').replace('y','i').replace('ç','c')
def lexicon():
    cnt = collections.Counter()
    files = [os.path.join(ROOT,'lang','corpora',f) for f in ('es-quijote.txt','es-vasto-memorias.txt','es-gutenberg.txt')]
    for f in files:
        if os.path.exists(f):
            cnt.update(re.findall(r'[a-zñ]+', norm(io.open(f, encoding='utf-8', errors='ignore').read())))
    for f in os.listdir(HERE):  # clear text quoted in the reading files of this target and lopehurtado1523
        pass
    return cnt
def cands(toks, lex, maxn=200000):
    sets = []
    for t in toks:
        if t in C: sets.append(C[t])
        elif t in S: sets.append(S[t])
        else: return None
    out = []
    n = 1
    for s in sets: n *= len(s)
    if n > maxn: return 'too many'
    for combo in itertools.product(*sets):
        w = norm(''.join(combo))
        if lex.get(w, 0) >= 2: out.append((lex[w], w))
    return sorted(set(out), reverse=True)[:8]
if __name__ == '__main__':
    lex = lexicon()
    if sys.argv[1] == '--all':
        for l in io.open(os.path.join(HERE, sys.argv[2] + '_reading.tsv'), encoding='utf-8'):
            if l.startswith(('#','ref')) or not l.strip(): continue
            ref, _, rd = l.rstrip('\n').split('\t', 2)
            for run in re.findall(r'\{([^}]*)\}', rd):
                for word in run.split():
                    toks = re.findall('|'.join(sorted(map(re.escape, list(S) + list(C)), key=len, reverse=True)) + '|.', word)
                    if len(toks) < 2: continue
                    print(ref, word, '->', cands(toks, lex))
    else:
        print(cands(sys.argv[1].split(), lex))
