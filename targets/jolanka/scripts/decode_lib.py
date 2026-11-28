import re
def toks(field):
    return re.findall(r'\{[^}]*\}|\[[^\]]*\]|\S+', field)
def dec_line(field, key):
    out=[]
    for t in toks(field):
        if t[0]=='{': out.append(' '+t+' '); continue
        if t[0]=='[': out.append('_' if t=='[.]' else ' ... '); continue
        if t in ',.': out.append(t); continue
        out.append(key.get(t.rstrip('?'),'#'))
    return ''.join(out)
