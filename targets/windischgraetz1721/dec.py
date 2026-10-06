"""Apply Mirka's key to ct.txt. Codes in three tiers:
 A  value on Mirka's list, or confirmed by an interlinear gloss in the sibling letters R5025-R5028 (6 Oct 2026 pass)
 B  bracketed from the alphabetical code order and fitted to every context (proposal, NOT counted as read)
 open  no value"""
import re,sys
t=[("A",24,36),("B",12,48),("C",23,35),("D",11,47),("E",22,34),("F",10,46),("G",21,33),("H",9,45),("I",20,32),("K",8,44),("L",19,31),("M",7,43),("N",18,30),("O",6,42),("P",17,29),("Q",5,41),("R",16,28),("S",4,40),("T",15,27),("V",3,39),("W",14,26),("X",2,38),("Y",13,25),("Z",1,37)]
k={}
for c,a,b in t: k[a]=c;k[b]=c
A={52:"affaire",54:"Althann",85:"der/dem",86:"die",121:"geheim",128:"Graf",135:"hat",145:"ich",152:"Kayser",197:"Plan",198:"Prinz",
   # sibling glosses
   78:"Compagnie",      # R5026 p.4: '85 191 78 85 152' glossed 'der Ostend. Compagnie dem Kayser'
   99:"Engländer",      # R5026 p.4 and R5028 p.2: pencil gloss 'Engländer' over 99
   103:"Eugen",         # R5028 p.1 'P.E.', R5026 p.5 '103 contrair' glossed 'Eug.'
   167:"Miosch",        # R5025 p.3 '128.167' glossed 'Graf Miosch'
   191:"Ostendisch",213:"Starhemberg"}
B={111:"Franzosen",130:"gut",131:"haben",146:"ihm",149:"ihro",151:"Kaiserin",164:"mehr",168:"mir",172:"mit",182:"nicht",209:"seyn",205:"Rialp",139:"Hof"}
def decode(show_b=True):
  out_lines=[]
  for line in open('ct.txt',encoding='utf8'):
    if line.startswith('#') or '|' not in line:continue
    pg,body=line.split('|',1); out=[]
    for tok in re.split(r'(\[[^\]]*\])',body):
      if tok.startswith('['): out.append(tok[1:-1]); continue
      w=''
      for n in map(int,tok.split()):
        if n<=48: w+=k[n]
        else:
          if w: out.append(w); w=''
          if n in A: out.append('«%s»'%A[n])
          elif n in B and show_b: out.append('«%s?»'%B[n])
          else: out.append('«%d»'%n)
      if w: out.append(w)
    out_lines.append(pg.strip()+': '+' '.join(out))
  return out_lines
if __name__=='__main__':
  sys.stdout.reconfigure(encoding='utf-8')
  print('\n'.join(decode()))
