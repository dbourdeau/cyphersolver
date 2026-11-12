# signnames.py R2_FILE > OUT: maps the blind reader's lower-case sign names (ll b x psi beta ms tq lam y g theta hash u4 hz q dx) to the sign names of key.tsv and drops the unsure mark ~. Copied unchanged from the contributor's b96 scripts/b94names.py (this comment line added).
import sys,re
M={'ll':'LL','b':'B','x':'X','psi':'PSI','beta':'BET','ms':'MT','tq':'QX','lam':'LAM','y':'Y','g':'G','theta':'TH','hash':'HSH','u4':'U4','hz':'HB','q':'Q','dx':'DB'}
for l in open(sys.argv[1],encoding='utf8'):
    if l.startswith('#') or '|' not in l: print(l,end=''); continue
    print(re.sub(r'<([^>]*)>',lambda m:'<'+'.'.join(M.get(t.strip().rstrip('~'),t.strip().rstrip('~')) for t in m.group(1).split('.'))+'>',l),end='')
