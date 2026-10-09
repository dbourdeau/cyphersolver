# mechanical key-A decoder: one output line per MS line, token-by-token (cipher -> plain)
import sys,re,io
K={'9':'a','p':'a','a':'o','q':'o','z':'e','Z':'e','g':'e','S':'e','e':'s','n':'s','c':'n','T':'t','2':'l','3':'u',
   '7':'i','P':'g','O':'c','Q':'c','o':'r','L':'r','d':'m','b':'p','f':'y','m':'x','V':'q','R':'f','Y':'rr','H':'','U':'?','D':'d','W':'ç'}
CODES={'cap':'que','lod':'de','luc':'duque','lih':'Milan','cip':'Venecia','mos':'infanteria','lim':'mil','leh':'en',
 'sig':'Rey','saq':'Francia','rap':'Italia','mul':'porque','q':'que','f':'y'}
def dec(w):
    if w in CODES: return '<'+CODES[w]+'>'
    v=w.replace('cT','D').replace('Lo','W')
    return ''.join(K.get(c,'_'+c) for c in v if c not in '?{}')
def toks(s):
    s=re.sub(r'\{[^}]*\}','',s); return s.split()
if __name__=='__main__':
  sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
  for l in open(sys.argv[1],encoding='utf-8'):
      m=re.match(r'\s*(L\d+):(.*)',l)
      if not m: continue
      t=toks(m.group(2)); print(m.group(1),' | '.join(f'{w}={dec(w)}' for w in t))
