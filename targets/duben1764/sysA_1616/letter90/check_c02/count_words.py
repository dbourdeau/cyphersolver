"""Word count of a tagged reading: plain = sure, {x} = probable, ‹n› = n unresolved words; elided forms (j'ai) count as two words; a line-end hyphen joins the word."""
import re,sys
txt=[]
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split(' ',1); txt.append(p[1] if len(p)>1 else '')
s=' '.join(txt)
s=re.sub(r'-\s+','',s)            # line-break hyphen joins
s=re.sub(r"(\w)'(?=\w|\{)",r"\1' ",s)  # elision = separate word (j'ai -> j' ai)
sure=prob=unr=0
for t in re.findall(r'‹\d+›|\{[^}]*\}|[^\s{‹]+',s):
    if t.startswith('‹'): unr+=int(t[1:-1])
    elif t.startswith('{'): prob+=1
    elif re.search(r'\w',t): sure+=1
tot=sure+prob+unr
print(f'sure {sure}  probable {prob}  unresolved {unr}  total {tot}  strict(sure) {sure/tot:.3f}  sure+probable {(sure+prob)/tot:.3f}')
