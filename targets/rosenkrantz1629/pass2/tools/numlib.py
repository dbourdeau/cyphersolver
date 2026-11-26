import re,collections
def load(path):
    """rows: (letter,image,line,[items]); item = ('n',int,flag) | ('c',text) | ('d',text)"""
    rows=[]
    for l in open(path,encoding='utf-8').read().splitlines()[1:]:
        if not l.strip(): continue
        let,img,ln,tk=l.split('\t'); items=[]
        for part in re.split(r'(\{[^}]*\}|\[[^\]]*\])',tk):
            part=part.strip()
            if not part: continue
            if part.startswith('{'): items.append(('c',part[1:-1]))
            elif part.startswith('['): items.append(('d',part[1:-1]))
            else:
                for t in part.split():
                    q=t.endswith('?'); t=t.rstrip('?')
                    if t.isdigit(): items.append(('n',int(t),q))
                    else: items.append(('n',t,True))
        rows.append((let,img,ln,items))
    return rows
def stream(rows):
    """flat list of tokens with clear-word boundary markers: ints, or '|' for clear text/line gaps (line ends are NOT boundaries unless clear text intervenes)"""
    out=[]
    for let,img,ln,items in rows:
        for it in items:
            if it[0]=='n': out.append(it[1])
            elif it[0]=='c': out.append('|'+it[1])
    return out
