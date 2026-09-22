import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lang import lm
M=lm.load('it-modern',order=4,spaces=True)
OUT='ABCDEFGILMNOPQRSTVXZ1234'.lower()
INNERS={'alberti':'gklnprtuz&xysomqihfdbace'}
segs={'1v_pre':'osor','1v_R':'erpij leor sglgrz hshr hyor larohgt gsg yhzy solir tzs noyp',
'2r':'ylior lay gnotrh ghplr agksro','2r_b':'zshukss','2r_c':'gpr sgrghs hr hqihz yz set','2r_V':'z vs sn qrpt'}
Z={'Ariete':'srcon pggy','Taurus':'lrqrlrpnqsr&g','Gemini':'qrqrsipqsop zg','Cancer':'irqpshkscel','Leo':'rqlpsonspyh','Virgo':'pqyqpqs q st','Libra':'qsgqxqkbz','Scorpio':'prk syqs&qp','Sagit':'xin ak & sqol','Capri':'&n qqpypt&r','Aquario':'qk sqrongya','Pissis':'&t by hqph yv'}
segs.update(Z)
for nm,inner in INNERS.items():
  for direction in (1,-1):
    print('==',nm,direction)
    for k,s in segs.items():
        s=s.replace('j','i').replace('v','u')
        res=[]
        for off in range(24):
            p=''.join(OUT[(direction*inner.index(c)+off)%24] if c in inner else c for c in s)
            q=p.translate(str.maketrans('','','1234'))
            res.append((M.per_char(' '+q+' '),p,off))
        res.sort(reverse=True)
        print(k,s,'->',[(round(a,2),b,o) for a,b,o in res[:2]])
