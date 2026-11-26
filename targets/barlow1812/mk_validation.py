"""Build validation.tsv for docs/_validate.py from the two decryption files that decode.py writes.

    python mk_validation.py

One code number per line with the value key.tsv gives it. A number whose value is only our proposal (grade ?, from
proposals.tsv) or that has no value is written '?' (unread, left out of the score). Numbers struck out in the manuscript
(~...~) and the words in clear are left out. Copy B of the note to Bassano repeats copy A and is not added.
Standard library only.
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
DOCS = ('1812-09-25', '1812-10-25_A')
TOK = re.compile(r'(~?)\^?(\d{2,4})=([^/\s"]*(?: [^/\s"]+)*?)(?:/(\S))?(~?)(?=\s|$)')

out = ['# model: en-modern',
       '# source: decryption_1812-09-25.txt + decryption_1812-10-25_A.txt (python decode.py), values of key.tsv only',
       '# note: a code of words and syllables; most numbers occur once or twice here, so the permutation tests have little to work with']
n = 0
for doc in DOCS:
    for line in (HERE / f'decryption_{doc}.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip():
            continue
        for part in re.split(r'\s{2,}', line.split(None, 1)[1] if ' ' in line else ''):
            part = part.replace(' (digit doubtful)', '').strip()
            m = re.fullmatch(r'(~?)\^?(\d{2,4})=(.*?)(~?)', part)
            if not m:
                continue                                   # a word in clear
            if m.group(1) or m.group(4):
                continue                                   # struck out
            val = m.group(3)
            v, _, g = val.rpartition('/')
            if not v or g == '?' or val == '?':
                v = '?'
            out.append(f'{m.group(2)}\t{v}')
            n += 1
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(n, 'numbers;', sum(1 for l in out[3:] if l.endswith('\t?')), 'unread')
