"""Decode f. 33 (BnF italien 1585) from the sign-by-sign transcription in texts/f33_cipher.txt.

The transcription already writes each cipher sign as the key letter it stands for (key: ASMi Carteggio
Sforzesco cart. 1597 no. 16, DECODE R5316, headed "Andreas Biragus"), so decoding is a lookup:
letters -> themselves, ET -> "et", FP -> "[Francesco Piccinino]". Writes texts/f33_decryption.txt and
prints token counts.
"""
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'texts' / 'f33_cipher.txt'
OUT = HERE / 'texts' / 'f33_decryption.txt'

# Signs on the key (k16v.jpg). b has no sign on the key.
KEY = {c: c for c in 'acdefghilmnopqrstuxz'}
KEY['ET'] = 'et'
KEY['FP'] = '[Francesco Piccinino]'


def main():
    out, signs, uncertain, offkey = [], [], [], []
    for raw in SRC.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('CLEAR:'):
            out.append(line)
            continue
        tag, body = line.split(':', 1)
        words = []
        for chunk in body.split('|'):
            w = []
            for tok in chunk.split():
                signs.append(tok.rstrip('?'))
                if tok.endswith('?'):
                    uncertain.append((tag, tok))
                    tok = tok[:-1]
                    w.append(KEY.get(tok, tok) + '(?)')
                elif tok in KEY:
                    w.append(KEY[tok])
                else:
                    offkey.append((tag, tok))
                    w.append(tok)
            if w:
                words.append(''.join(w))
        out.append(f'{tag}: ' + ' '.join(words))
    OUT.write_text('\n'.join(out) + '\n', encoding='utf-8')
    cnt = Counter(signs)
    print(f'total cipher signs: {len(signs)}')
    print(f'distinct signs: {len(cnt)}  ({" ".join(f"{k}:{v}" for k, v in sorted(cnt.items()))})')
    print(f'not on the key: {len(offkey)} {offkey}')
    print(f'uncertain: {len(uncertain)} {uncertain}')
    print(f'key signs never used: {sorted(set(KEY) - set(cnt))}')
    print(f'wrote {OUT}')


if __name__ == '__main__':
    main()
