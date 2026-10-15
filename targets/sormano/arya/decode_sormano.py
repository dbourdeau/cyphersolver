"""Decode Sormano's cipher (BnF fr. 3096, 1529) with Lasry's key.

Glyph labels used in the ct/*.txt transcriptions, and their values from key_lasry.tsv:
  n1 clean pi = n        a1 pi+tick = a      V capital V = a     u1 round U = a    z3 figure 3 = a
  b1 tau = b             D triangle = c      cc crossed bars=cc  d1 e-with-tail = d
  e1 tall pi+tick = e    k1 k = e            r1 Gamma = e        s7 figure 7 = e
  ff double f = f        G capital S = g     H1 capital E = h
  Y capital Y = i        oo circle+dot = i   P capital P = i     f4 figure 4 = i
  LL square+dot = ll     n9 figure 9 = l     M g+crossed tail=m  n1 pi = n
  O1 U+stroke = o        O2 plain stroke = o O3 delta/8 = o      p6 figure 6 = p
  Q1 inverted triangle=q R capital Q = r     S1 T+2 bars = s     S2 reversed C = s
  T chi/x = t            V1 capital T = v    al alpha = v        Y2 Y+mark = v   H2 capital H = v
  X large X = x          NUL tall looped sign = null (claimed; unverified)
  ?  unidentified glyph
usage: python3 decode_sormano.py ct/FILE.txt
"""
import sys, re
K = {'n1':'n','a1':'a','V':'a','u1':'a','z3':'a','b1':'b','D':'c','cc':'cc','d1':'d',
     'e1':'e','k1':'e','r1':'e','s7':'e','ff':'f','G':'g','H1':'h','Y':'i','oo':'i','P':'i','f4':'i',
     'LL':'ll','n9':'l','M':'m','O1':'o','O2':'o','O3':'o','p6':'p','Q1':'q','R':'r','S1':'s','S2':'s',
     'T':'t','V1':'v','al':'v','Y2':'v','H2':'v','X':'x','NUL':'','?':'?'}
def decode(line):
    out=[]
    for tok in line.split():
        if tok.startswith('[['): out.append(' '+tok[2:-2]+' '); continue
        out.append(K.get(tok,'<'+tok+'>'))
    return ''.join(out)
if __name__=='__main__':
    for path in sys.argv[1:]:
        print('=====',path)
        for raw in open(path):
            raw=raw.strip()
            if not raw or raw.startswith('#'): continue
            if raw.startswith('[[') and raw.endswith(']]'): print(raw[2:-2]); continue
            print(decode(raw))
