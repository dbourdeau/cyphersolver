import os
d=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(d,'parse.py')).read().split('for k,v in segs')[0])
exec(open(os.path.join(d,'key.py')).read())
for k,v in segs:
    print(('   '+v) if k=='C' else ('>> '+''.join(KEY.get(x,'#') for x in v)+'    ['+' '.join(v)+']'))
