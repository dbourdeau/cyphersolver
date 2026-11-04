"""Rebuild the decryption of a page from the final transcription + frozen key, and compare it word by word with the
marked reading. Fails (exit 1) on any unmarked departure.
Reading marks:  [abc] letters the clerk left out, supplied (normalisation, not a repair)
                {x>y} sign decodes x, reading has y (a repair, listed)   {x>} superfluous sign dropped (repair, listed)
                [?word] doubtful word, not checked, counted as not read     [NNNN] code group / null, not counted
                _ joins two words the clerk wrote as one.  u/v and i/j count as one letter.
                A sign not in the frozen key decodes as ?, so {?>m} reads it as m and {?>} drops it (both repairs).
                A four-digit group inside a run (1100, 2200) is dropped as a null and counted as a code group.
usage: check_marks.py <page> [<page> ...]   (files trans_final/pNN.txt, key_final.txt, reading/rNN.txt)"""
import sys,re
sys.path.insert(0,'scripts'); from parse import words
key=dict(l.split('=') for l in open('key_final.txt').read().split())
norm=lambda s:s.lower().replace('v','u').replace('j','i')
fail=0; T={'clear':0,'cipher':0,'read':0,'doubt':0,'repairs':0,'codes':0,'drops':0}
for p in sys.argv[1:]:
    items=words(open(f'trans_final/p{p}.txt',encoding='utf8').read())
    dec=[]; inner=0
    for k,v in items:
        if k!='C': continue
        if all(len(t)>3 for t in v): dec.append('['+','.join(v)+']'); continue
        inner+=sum(1 for t in v if len(t)>3)
        dec.append(''.join(key.get(t,'?') if len(t)<=3 else '' for t in v))
    clear=sum(1 for k,v in items if k=='P')
    rd=open(f'reading/r{p}.txt',encoding='utf8').read().split()
    if len(dec)!=len(rd):
        print(p,'LENGTH MISMATCH',len(dec),len(rd)); 
        for i,(d,r) in enumerate(zip(dec,rd)): print('  ',i,d,r)
        fail=1; continue
    c={'clear':clear,'cipher':0,'read':0,'doubt':0,'repairs':0,'codes':inner,'drops':0}; reps=[]
    for d,r in zip(dec,rd):
        if re.fullmatch(r'\[\d{4}(,\d{4})*\]',r):
            c['codes']+=1
            if d!=r: print(p,'CODE MISMATCH',d,r); fail=1
            continue
        c['cipher']+=1
        if r.startswith('[?'): c['doubt']+=1; continue
        n=len(re.findall(r'\{[a-z?]*>[a-z]*\}',r)); c['repairs']+=n; c['drops']+=len(re.findall(r'\{[a-z?]+>\}',r))
        if n: reps.append(f'{d}->{r}')
        base=re.sub(r'\{([a-z?]*)>[a-z]*\}',r'\1',r); base=re.sub(r'\[[a-z]+\]','',base).replace('_','')
        if norm(base)!=norm(d): print(p,'UNMARKED DEPARTURE: decryption',d,'reading',r); fail=1
        else: c['read']+=1
    words_total=c['clear']+c['cipher']; words_read=c['clear']+c['read']
    print(f"p{p}: clear {c['clear']}, cipher words {c['cipher']} (read {c['read']}, doubtful {c['doubt']}), repairs {c['repairs']} ({c['drops']} signs dropped), code groups {c['codes']}; words read {words_read}/{words_total} = {100*words_read/words_total:.1f}%")
    if reps: print('   repairs:',' '.join(reps))
    for k in T: T[k]+=c[k]
tot=T['clear']+T['cipher']; rd_=T['clear']+T['read']
print(f"TOTAL: words read {rd_}/{tot} = {100*rd_/tot:.1f}%; cipher words read {T['read']}/{T['cipher']} = {100*T['read']/T['cipher']:.1f}%; repairs {T['repairs']} ({T['drops']} signs dropped, {T['repairs']-T['drops']} letters changed); code groups {T['codes']}")
sys.exit(fail)
