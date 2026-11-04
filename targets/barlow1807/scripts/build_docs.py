"""Build the per-document files from trans_final/, key_final.txt and reading/rNN.txt.
Letter 1 (Barlow to Grenville, 12 Feb 1807, cipher) runs over images 15-18, 1-14, 19-20 in that order (catchwords and
sense; see NOTES.md); image 21 is blank, image 22 the docket. Letter 2 (Barlow to Tierney, 15 June 1807) is in clear:
images 23-25, docket image 26.   usage: build_docs.py"""
import sys,re
sys.path.insert(0,'scripts'); from parse import words
key=dict(l.split('=') for l in open('key_final.txt').read().split())
CODE={'4990':'India','5650':'British'}          # values that fit every occurrence (NOTES.md, code groups)
NULL={'1100','2200','1000'}
G=[15,16,17,18]+list(range(1,15))+[19,20]; GX=[21,22]; TI=[23,24,25]; TX=[26]
def raw(n): return open(f'trans_final/p{n:02d}.txt',encoding='utf8').read().strip()
def dec_word(v):
    if all(len(t)>3 for t in v): return '['+','.join(v)+']'
    return ''.join(key.get(t,'?') if len(t)<=3 else '['+t+']' for t in v)
def plain_tok(r):
    m=re.fullmatch(r'\[(\d{4})\]',r)
    if m: return None if m.group(1) in NULL else ('['+CODE[m.group(1)]+']' if m.group(1) in CODE else '[code '+m.group(1)+']')
    if r.startswith('[?'): return r
    s=re.sub(r'\{[a-z?]*>([a-z]*)\}',r'\1',r); return re.sub(r'\[([a-z]+)\]',r'\1',s).replace('_',' ')
T=['Sir George Barlow to Thomas Grenville, Fort William, 12 February 1807 ("Private and Confidential", "Quadruplicate").',
   'Cleveland Public Library, Zamboni note 159. Sign-first transcription, numbers as written; clear words as written.',
   'Pages in reading order. [..] = editorial note; {date:..} = clear date kept out of the cipher parse. Settled readings: patches.tsv, disagreements.tsv.','']
D=['Decryption with the frozen key (key_final.txt), letter by letter, no repair. Cipher words in <..>; ? = sign not in the key;',
   '[NNNN] = four-digit group. Clear words as written. Pages in reading order.','']
R=['# Barlow to Grenville, Fort William, 12 February 1807: reading','',
   'Marks: `[abc]` letters the clerk left out, supplied (normalisation, not a repair); `{x>y}` the sign decodes x, read as y '
   '(repair); `{x>}` sign dropped as superfluous (repair); `{?>y}` sign not in the frozen key, read as y (repair); `[?word]` '
   'doubtful, counted as not read; `[NNNN]` four-digit group; `_` two words written as one. `scripts/check_marks.py` rebuilds '
   'the decryption from transcription and key and fails on any unmarked departure.','',
   'Each page: the marked cipher words in <..> among the clear words, then a plain running text (marks resolved; 4990 shown as '
   '[India], 5650 as [British], other groups as [code NNNN], nulls 1100/2200/1000 left out). The letter is in English.','']
P=[]
for k,n in enumerate(G,1):
    t=raw(n); T.append(f'== image {n} (letter page {k})\n'+t); D.append(f'== image {n} (letter page {k})')
    for line in t.splitlines(): D.append(' '.join(v if kk=='P' else '<'+dec_word(v)+'>' for kk,v in words(line)))
    rd=open(f'reading/r{n:02d}.txt',encoding='utf8').read().split() if n<20 else []
    it=iter(rd); mk=[]; pl=[]
    for kk,v in words(t):
        if kk=='P': mk.append(v); pl.append(v); continue
        r=next(it); mk.append('<'+r+'>'); s=plain_tok(r)
        if s: pl.append(s)
    R+=[f'## Image {n} (letter page {k})','',' '.join(mk),'','> '+' '.join(pl),'']; P+=pl
for n in GX: T.append(f'== image {n}\n'+raw(n))
R+=['## Plain text, whole letter','',' '.join(P).replace('= =','').replace('- -',''),'']
open('transcription_12feb1807.txt','w',encoding='utf8').write('\n'.join(T)+'\n')
open('decryption_12feb1807.txt','w',encoding='utf8').write('\n'.join(D)+'\n')
open('reading_12feb1807.md','w',encoding='utf8').write('\n'.join(R)+'\n')
T2=['Sir George Barlow to George Tierney, Fort William, 15 June 1807. Written in clear; no cipher.','']
for k,n in enumerate(TI,1): T2.append(f'== image {n} (letter page {k})\n'+raw(n))
for n in TX: T2.append(f'== image {n} (docket)\n'+raw(n))
open('transcription_15jun1807.txt','w',encoding='utf8').write('\n'.join(T2)+'\n')
open('decryption_15jun1807.txt','w',encoding='utf8').write('No cipher. This letter is written in clear; the text is in transcription_15jun1807.txt and reading_15jun1807.md.\n')
txt=' '.join(re.sub(r'\[[^\]]*\]','',raw(n)) for n in TI); txt=re.sub(r'[=-]\s*\n\s*[=-]?','',txt); txt=re.sub(r'\s+',' ',txt)
ADDR='The Right Honorable George Tierney &c. &c. &c.'; assert ADDR in txt; txt=re.sub(' +',' ',txt.replace(ADDR,''))
open('reading_15jun1807.md','w',encoding='utf8').write('# Barlow to Tierney, Fort William, 15 June 1807: reading\n\nThe letter is in clear English. Running text from the transcription, line-end hyphens joined; the catchword at the foot of the first page is left out.\n\n'+txt.strip()+'\n\nAddressed at the foot of the first page: '+ADDR+'\n')
cw=lambda ns: sum(1 for n in ns for kk,v in words(raw(n)) if kk=='P')
print('clear words: letter page 20 (subscription):',cw([20]),' Tierney letter:',cw(TI))
