import re
m=dict(q='a',v='w',V='m',T='c',C='s',D='·',J='f',o='g',g='g',H='k',w='i',X='u',Y='m',O='d?',u='o',P='p',Q='(c)',A='r',y='s',e='t',E='ch',W='·',K='z',R='[R]',L='f',z='z',B='[B]',U='[U]')
m['#']='[#]';m['+']='d';m['6']='e';m['3']='n';m['4']='h';m['8']='l';m[')']=')';m['&']='?';m['?']='?'
for l in open('transcription.txt',encoding='utf8'):
  if not re.match(r'(L\d\d|P\d) ',l):continue
  tag,rest=l.split(' ',1);rest=rest.split('   (')[0].split('    (')[0]
  out=[];i=0
  for part in re.split(r'(\[[^\]]*\])',rest.rstrip()):
    if part.startswith('['):out.append('|'+part[1:-1]+'|');continue
    out.append('{'+' '.join(''.join(m.get(c,'_') for c in w) for w in part.split())+'}' if part.strip() else '')
  print(tag,' '.join(o for o in out if o and o!='{}'))
