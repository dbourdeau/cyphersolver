rows='1357902468'; cols='1234567890'
T='''a able accion ado al an ando ante ar as
b ble c cia cien cion con ch d da
dad de di do e el em en encia endo
ente er es esta f g i ido im in
ir j l la las les lo los m ma
mente mi n na ne ni no ñ o on
or os osa oso p pa pe por pra pre
pro pues que qui r ra re rr s sa
se señor si sin su sus t ta te tras
tu u un usted w x y ya yo z'''.split('\n')
RC={};CR={}
for r,line in zip(rows,T):
  for c,v in zip(cols,line.split()): RC[r+c]=v; CR[c+r]=v
import sys as _s
for s in _s.argv[1:] if __name__=="__main__" else []:
  g=s.replace(' ','-').split('-'); g=[x for x in g if x]
  print('RC:', ' '.join(RC.get(x,'['+x+']') for x in g))
  print('CR:', ' '.join(CR.get(x,'['+x+']') for x in g))
