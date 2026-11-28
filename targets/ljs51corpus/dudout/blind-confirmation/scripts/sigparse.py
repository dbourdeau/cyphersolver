"""Lecture d'une transcription en signes -> (tokens entiers, K). '|' = separateur ; fin de ligne = pas de separateur."""
def parse_lines(lines):
    toks=[]
    for l in lines:
        for t in l.split():
            if t=='|':
                if toks and toks[-1]!='|': toks.append('|')
            else: toks.append(t)
    while toks and toks[0]=='|': toks.pop(0)
    while toks and toks[-1]=='|': toks.pop()
    labels=sorted(set(t for t in toks if t!='|'), key=lambda x:(len(x),x))
    m={s:i for i,s in enumerate(labels)}
    return [-1 if t=='|' else m[t] for t in toks], len(labels), labels
def read_sig(path):
    return parse_lines([l for l in open(path,encoding='utf8').read().split('\n') if l.strip()])
