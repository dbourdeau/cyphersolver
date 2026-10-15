# -*- coding: utf-8 -*-
# Decode Mascon's cipher (Lasry/Tomokiyo key) from ASCII aliases. Spaces ignored; [..] copied; {nn} code group.
import sys,re
K={
 '3':'a','8':'a','+':'a',
 'z':'b',
 '4':'c','c':'c',
 '5':'d',
 '9':'e','o':'e','b':'e',
 'F':'f',
 'g':'g',
 'h':'h',
 'A':'i','L':'i','H':'i',
 'l':'l','X':'l',
 'W':'ll',
 '1':'m','M':'m',
 '7':'n','N':'n',
 'f':'o','D':'o','j':'o',
 '=':'p','P':'p',
 'w':'pp',
 'q':'q',
 'R':'r','r':'r',
 'E':'rr',
 '6':'s','s':'s','C':'s',
 'S':'ss',
 'G':'t','T':'t',
 'U':'u','m':'u','V':'u',
 'x':'x',
 '&':'&',
 'n':'','~':'','_':'','|':'',
 '?':'?',
}
CODES={'30':'<PAPE>','40':'<ROY>'}
def dec(s):
    out=[]
    for part in re.split(r'(\[[^\]]*\]|\{[^}]*\})',s):
        if part.startswith('['): out.append(part); continue
        if part.startswith('{'): out.append(CODES.get(part[1:-1],'<'+part[1:-1]+'>')); continue
        for ch in part:
            if ch.isspace(): continue
            out.append(K.get(ch,'('+ch+')'))
    return ''.join(out)
if __name__=='__main__':
    src=sys.argv[1:] and [' '.join(sys.argv[1:])] or sys.stdin.read().splitlines()
    for l in src: print(dec(l))
