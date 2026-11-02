"""Normalise clear text: clear_letters.json (expanded, from clear_running.txt) and clear_abbr.txt (unexpanded, from clear.txt)."""
import re,json
def norm(s):
    s=s.lower().replace('j','i').replace('v','u')
    return s
t=open('clear194/clear_running.txt').read()
t=t.split('\n',1)[1]  # drop date line (not enciphered)
t=t.replace('[?]',' ').replace('[...]',' ')
t=re.sub(r'\[\?(\w+)\]',r'\1',t)
words=re.findall(r'[A-Za-z]+',t)
words=[norm(w) for w in words]
json.dump(words,open('ext/clear_words.json','w'))
# unexpanded
out=[]
for l in open('clear194/clear.txt'):
    if not re.match(r'f\d[rv] [LM]',l): continue
    b=l.split(':',1)[1]
    b=re.sub(r'\[del:[^\]]*\]','',b); b=re.sub(r'\{ins: ([^},]*)[^}]*\}',r'\1',b)
    b=re.sub(r'\{marg: \([^)]*\)','',b).replace('}','')
    b=re.sub(r'\([^)]*\)','.',b)  # abbreviation marks kept as '.'
    out.append(norm(b.strip()))
open('ext/clear_abbr.txt','w').write('\n'.join(out)+'\n')
print(len(words),sum(map(len,words)))
