"""Mechanical decryption of transcription_44r.txt with a key file (default key.tsv).
Unknown signs print as [sign]; points print as nothing."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import read_transcription, read_key, HERE

def decrypt_tokens(toks, key):
    out = []
    for t in toks:
        v = key.get(t)
        if v is None: out.append(f'[{t}]')
        elif v == '_': continue
        else: out.append(v)
    return out

if __name__ == '__main__':
    keyp = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'key.tsv')
    key = read_key(keyp); tr = read_transcription()
    lines = [f"{lab}: {'-'.join(decrypt_tokens(tr[lab], key))}" for lab in sorted(tr)]
    outp = sys.argv[2] if len(sys.argv) > 2 else None
    txt = "# Mechanical decryption of c. 44r with " + os.path.basename(keyp) + " (syllables joined by '-', points dropped; no word division)\n" + "\n".join(lines) + "\n"
    if outp: open(outp, 'w', encoding='utf-8').write(txt)
    else: print(txt)
