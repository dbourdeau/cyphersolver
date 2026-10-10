"""Generate correction HYPOTHESES for visual checking, never a verified reading.

The shared substitution is fixed. Only frequent manual transcription confusions
are allowed, with a log-score penalty. Output must be checked against source.
"""
import pathlib,sys,json,re
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
from lang import lm
root=pathlib.Path(__file__).resolve().parent
key=json.loads((root/'shared-key-hypothesis.json').read_text())
m=lm.load('hu-modern',order=5,spaces=False)
conf=['qg','cp','in','uv','hr']
def decode(s):
 x=''.join(c for c in s if c in key)
 beam=[(0.0,'','')]
 for c in x:
  opts=[(c,0.0)]+[(z,3.5) for group in conf if c in group for z in group if z!=c]
  expanded=[]
  for score,plain,cipher in beam:
   for z,pen in opts:
    p=key[z]; text=plain+p
    add=0.0
    if len(text)>=5:
     ix=0
     for ch in text[-5:]: ix=ix*26+ord(ch)-97
     add=float(m.lp[ix])
    expanded.append((score+add-pen,text,cipher+z))
  expanded.sort(reverse=True)
  # Prune equivalent contexts, retaining highest-scoring history.
  seen=set(); beam=[]
  for item in expanded:
   if item[1][-4:] not in seen:
    beam.append(item); seen.add(item[1][-4:])
   if len(beam)==100: break
 return {'input':x,'plaintext_hypothesis':beam[0][1],'cipher_hypothesis':beam[0][2],
         'corrections':sum(a!=b for a,b in zip(x,beam[0][2]))}
raw=(root/'R4936-transcription.txt').read_text()
segments=[]
for section in re.split(r'(\{[^}]*\}|#[^\n]*)',raw):
 if section.startswith(('{','#')): segments.append({'clear_or_heading':section})
 elif section.strip(): segments.append(decode(section))
(root/'R4936-correction-hypotheses.json').write_text(json.dumps(segments,indent=2))
for s in segments:
 print(s.get('plaintext_hypothesis',s.get('clear_or_heading')))
