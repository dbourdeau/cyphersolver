"""Write tx/plain.txt: the decipherment as running text, clear passages in {braces}, unknown groups as [group]."""
from decode import lines, render
with open('tx/plain.txt','w',encoding='utf8') as f:
    f.write("# R1862 decipherment (working text). {..} = passages written in clear; [nnnn] = group with no key value.\n")
    for lab,it in lines():
        f.write(f'{lab}\t{render(it)}\n')
