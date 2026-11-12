# Mechanical decryption: transcription (SIGN_CONVENTIONS.md) + key_frozen.tsv -> decryption file. Unknown tokens -> '?'.
# usage: python scripts/decrypt.py transcription.txt key_frozen.tsv out.txt
import sys; sys.path.insert(0,'scripts'); from common import *
T=load_trans(sys.argv[1]); K=load_key(sys.argv[2])
with open(sys.argv[3],'w',encoding='utf-8') as f:
    f.write('# Mechanical decryption of %s with %s (no repairs). One output word per cipher word; ? = sign with no value.\n'%(sys.argv[1],sys.argv[2]))
    for k,v in T.items(): f.write('%s: %s\n'%(k,dec_line(v,K)))
