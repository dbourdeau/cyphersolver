# Builds the marked reading of letter 1: each cipher word's mechanical output is aligned (Needleman-Wunsch on letters)
# to the clear copy; where they differ the word is written {mechanical/clear}. So every repair is a value taken from
# the clear copy and is marked. usage: python scripts/reading.py
import sys,re; sys.path.insert(0,'scripts'); from common import *; from em import nw, paras, clear as CL
T=load_trans('transcription_ind737_letter1.txt'); K=load_key('key_frozen.tsv')
raw={}
for ln in open('clear_panama29_R6_N23.txt',encoding='utf-8'):
    if ln[:1]=='P': k,v=ln.split(':',1); raw[k]=re.sub(r'\[|\]','',v.strip().lower())
out=open('reading_ind737_letter1.md','w',encoding='utf-8'); stats={'verbatim':0,'repaired':0,'clear_letters_only':0}
out.write('# Reading, letter 1 (AGI Indiferente 737 N.171, images 1-2): Alvaro de Sosa to the officials at Seville, Nombre de Dios, 4 July 1554\n\n')
out.write('Spanish. Each word is the mechanical decryption of one cipher word (scripts/decrypt.py, key_frozen.tsv). Where it\n')
out.write('departs from the clear copy in AGI Panama 29 R.6 N.23 it is written {mechanical/clear}: the clear form is a repair\n')
out.write('taken from that copy, not read from the signs. P1-P2 built the key; P3-P4 are held out. Paragraph 4 is scored\n')
out.write('against the copy with its numerals written out (P4n). A marked word is a gloss-only word: its form comes from the\n')
out.write('copy, and the signs do not give it. The marks hide the holes: every miss is filled from the copy.\n\n')
for pk in ['P1','P2','P3','P4n']:
    ck='P4' if pk=='P4n' else pk
    lines=paras[pk] if pk!='P4n' else paras['P4n']
    spaced=raw[pk]; letters=[(i,ch) for i,ch in enumerate(spaced) if re.match(r'[a-zñç]',ch)]
    c=''.join(ch for _,ch in letters)
    cw=[(l,[''.join(dec_tok(t,K) for t in w) for w in words(T[l])]) for l in lines]
    s=''.join(m for _,ws in cw for m in ws); amap=nw(s,c)
    pos=0; cut=0; out.write('## %s\n\n'%ck)
    for l,ws in cw:
        parts=[]
        for m in ws:
            idx=[amap[k] for k in range(pos,pos+len(m)) if amap[k] is not None]; pos+=len(m)
            end=max(idx)+1 if idx else cut
            if end<cut: end=cut
            seg=''.join(ch for _,ch in letters[cut:end]); cut=end
            if m==seg: parts.append(m); stats['verbatim']+=1
            else: parts.append('{%s/%s}'%(m,seg)); stats['repaired']+=1
        out.write('%s: %s\n'%(l,' '.join(parts)))
    if cut<len(letters): stats['clear_letters_only']+=len(letters)-cut; out.write('(copy continues: %s)\n'%''.join(ch for _,ch in letters[cut:]))
    out.write('\nClear copy of this paragraph, for sense: %s.\n\n'%spaced)
out.close(); print(stats)
