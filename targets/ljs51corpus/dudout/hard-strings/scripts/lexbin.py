"""lex.tsv -> lex.bin (uint64 code base 32, float32 compte), formes de 1 a 12 lettres, compte >= 2."""
import sys, struct
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
from common import IDX
with open(sys.argv[2], 'wb') as g:
    m = 0
    for l in open(sys.argv[1]):
        w, c = l.rstrip('\n').split('\t'); c = int(c)
        if c < 2 or len(w) > 12: continue
        code = 1
        for ch in w: code = code * 32 + IDX[ch]
        g.write(struct.pack('<Qf', code, float(c))); m += 1
print(m, 'formes')
