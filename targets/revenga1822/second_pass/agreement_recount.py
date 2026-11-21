"""Count blind transcription agreement with an explicit deterministic alignment.
No cipher key or plaintext is read. Run with Python -I.
"""
import pathlib,csv,re,json
BASE=pathlib.Path(__file__).resolve().parent
import sys
FIRST=BASE.parent/'transcription.txt'
SECOND=BASE/'blind/transcription_blind.tsv'

def tokens(text):
 out=[];i=0
 while i<len(text):
  c=text[i]
  if c=='[':
   j=text.index(']',i);v=text[i+1:j];out.append((v[0] if re.fullmatch(r'[a-zñ]\?',v) else None,False,text[i:j+1]));i=j+1;continue
  if c=='?':
   if out:out[-1]=(out[-1][0],False,out[-1][2]+'?')
   else:out.append((None,False,'?'))
   i+=1;continue
  if c=='|':
   if out and i+1<len(text):out[-1]=(out[-1][0],False,out[-1][2]+'|'+text[i+1]);i+=2;continue
  if c.isalpha() or c==',':out.append((c.lower(),True,c))
  i+=1
 return out

def align(a,b):
 # Unit substitution/insertion/deletion costs. Equal first-choice letters cost zero.
 # Ties: diagonal, deletion from second, insertion into second, in that order.
 n,m=len(a),len(b);d=[[0]*(m+1) for _ in range(n+1)]
 for i in range(n+1):d[i][0]=i
 for j in range(m+1):d[0][j]=j
 def cost(i,j):return 0 if a[i][0] is not None and a[i][0]==b[j][0] else 1
 for i in range(1,n+1):
  for j in range(1,m+1):d[i][j]=min(d[i-1][j-1]+cost(i-1,j-1),d[i-1][j]+1,d[i][j-1]+1)
 out=[];i=n;j=m
 while i or j:
  if i and j and d[i][j]==d[i-1][j-1]+cost(i-1,j-1):out.append((i,j,a[i-1],b[j-1]));i-=1;j-=1
  elif i and d[i][j]==d[i-1][j]+1:out.append((i,'',a[i-1],None));i-=1
  else:out.append(('',j,None,b[j-1]));j-=1
 return list(reversed(out))

def main():
 a={l.split('\t')[0]:l.split('\t')[2] for l in FIRST.read_text().splitlines() if re.match(r'^C\d\d\t',l)}
 b={r['id']:r['cipher'] for r in csv.DictReader(SECOND.open(),delimiter='\t')}
 groups=[]
 for k in range(1,10):groups.append(([f'C{k:02}'],[f'B{k:02}']))
 groups.append((['C10'],['B10','B11']))
 for k in range(11,17):groups.append(([f'C{k:02}'],[f'B{k+1:02}']))
 groups.append((['C17','C18'],['B18']))
 for k in range(19,55):groups.append(([f'C{k:02}'],[f'B{k:02}']))
 groups.append((['C55','C56'],['B55','B56']))
 rows=[];sums=[]
 for cs,bs in groups:
  aa=tokens(''.join(a[k] for k in cs));bb=tokens(''.join(b[k] for k in bs));ar=align(aa,bb);n=0;first_choice=0
  for col,(i,j,x,y) in enumerate(ar,1):
   agree=bool(x and y and x[1] and y[1] and x[0]==y[0]);n+=agree;first_choice+=bool(x and y and x[0] is not None and x[0]==y[0])
   rows.append(['+'.join(cs),'+'.join(bs),col,i,j,x[2] if x else 'GAP',y[2] if y else 'GAP',int(agree)])
  sums.append({'first':cs,'second':bs,'first_positions':len(aa),'second_positions':len(bb),'columns':len(ar),'sure_agree':n,'first_choice_agree':first_choice})
 with (BASE/'agreement_positions.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['first_groups','second_groups','column','first_pos','second_pos','first','second','sure_agree']);w.writerows(rows)
 total=sum(r['columns'] for r in sums);sure=sum(r['sure_agree'] for r in sums)
 out={'first_choice_agree':sum(r['first_choice_agree'] for r in sums),'sure_agree':sure,'alignment_columns':total,'fraction':sure/total,'groups':sums,'warning':'Bracketed spans of unknown length each occupy one unresolved placeholder; total is an operational alignment denominator, not a certified manuscript sign count.'}
 (BASE/'agreement_recount.json').write_text(json.dumps(out,indent=2)+'\n');print(out['first_choice_agree'],sure,total,sure/total)
if __name__=='__main__':main()
