"""Parse DECODE's R91 transcription (Spain IA-1, Dec 1541) into cipher lines.

Writes r91_cipher.txt: one line per manuscript line, "<page>.<line>\t<digits with ? marks>\t<gap-groups>".
Gaps of two or more spaces in the DECODE file are kept as '|' in the third column (the wide gaps on the page).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'decode', 'DOC_R91_D2341_2341.txt')
PAGES = {'682': '64r', '683': '64v', '684': '65r', '685': '65v', '686': '66r'}


def lines():
    page, n = None, 0
    for raw in open(SRC, encoding='utf-8'):
        raw = raw.rstrip('\n')
        m = re.match(r'#IMAGE NAME: (\d+)\.jpeg$', raw)
        if m:
            page, n = PAGES[m.group(1)], 0
            continue
        if raw.startswith('#') or not raw.strip():
            continue
        n += 1
        body = re.sub(r'<CLEARTEXT[^>]*>', ' ', raw.replace('<IL>', '_'))
        toks = re.findall(r'\d\??', body)
        if toks:
            groups = re.split(r'\s{2,}', body.strip())
            yield page, n, toks, ['|'.join(g.split()) for g in groups]


def digits(keep_unsure=True):
    out = []
    for _, _, toks, _ in lines():
        out += [t[0] for t in toks if keep_unsure or '?' not in t]
    return ''.join(out)


if __name__ == '__main__':
    with open(os.path.join(HERE, 'r91_cipher.txt'), 'w', encoding='utf-8') as f:
        for page, n, toks, groups in lines():
            f.write(f'{page}.{n}\t{" ".join(toks)}\t{"  ".join(groups)}\n')
    d = digits()
    print(len(d), 'digits;', sum(1 for _, _, t, _ in lines() for x in t if '?' in x), 'uncertain')
