import struct,sys
f=open(sys.argv[1],'rb').read()
off=struct.unpack('<I',f[10:14])[0]; w,h=struct.unpack('<ii',f[18:26]); bpp=struct.unpack('<H',f[28:30])[0]
bp=bpp//8; row=(w*bp+3)&~3; flip=h>0; h=abs(h)
OX,OY=int(sys.argv[2]),int(sys.argv[3])
red=[]
for y in range(h):
    ry=(h-1-y) if flip else y
    b=off+ry*row
    for x in range(w):
        B,G,R=f[b+x*bp],f[b+x*bp+1],f[b+x*bp+2]
        if R>150 and R-G>55 and R-B>70: red.append((x,y))
# cluster
S=set(red);seen=set();cl=[]
for p in red:
    if p in seen: continue
    st=[p];seen.add(p);pts=[]
    while st:
        q=st.pop();pts.append(q)
        for dx in(-2,-1,0,1,2):
            for dy in(-2,-1,0,1,2):
                r=(q[0]+dx,q[1]+dy)
                if r in S and r not in seen: seen.add(r);st.append(r)
    if len(pts)>=6:
        xs=[a for a,_ in pts];ys=[b for _,b in pts]
        cl.append((len(pts),OX+sum(xs)//len(xs),OY+sum(ys)//len(ys)))
for c in sorted(cl,key=lambda c:(c[2],-c[1])): print(c)
