"""Write the public DECODE decryption bodies (decode_updates/decryptions/R<id>.txt) from a decoder output file.

Follows decode_updates/CLEANING_BRIEF.md: one [IMG ...] line per page, the run-on letter stream split into words
with the spaced it-cinquecento model (same beam as ../bergamo1585/split_words.py), nomenclator words in lower case,
unread dotted codes as <nnn>, unknown figures as [?], lines of at most ~110 characters. No letters are changed.

usage: python make_decryptions.py [decoder output] [--skip-existing]
       default input: decrypt_raw.txt here; for the F22b records: ../morosini1589/decrypt_raw.txt
"""
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
from lang import lm  # noqa: E402

M = lm.load('it-cinquecento', spaces=True)


def split(run, B=40):
    beam = [(0.0, ' ')]
    for ch in run:
        nb = []
        for sc, s in beam:
            nb.append((sc + M.score(s[-5:] + ch) - M.score(s[-5:]), s + ch))
            if s[-1] != ' ':
                nb.append((sc + M.score(s[-5:] + ' ' + ch) - M.score(s[-5:]), s + ' ' + ch))
        beam = sorted(nb, reverse=True)[:B]
    return beam[0][1].strip()


def clean_line(line):
    out = []
    for p in re.split(r'(\[[^\]]*\])', line):
        if not p.strip():
            continue
        if p.startswith('['):
            code = p[1:-1]
            out.append('<' + code[:-1] + '>' if code.endswith('?') else code.lower())
        else:
            words = split(p.lower().replace('?', '#'))
            out.append(words.replace('#', '[?]'))
    return ' '.join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    src = args[0] if args else os.path.join(HERE, 'decrypt_raw.txt')
    skip = '--skip-existing' in sys.argv
    pages = {}
    rec = img = None
    for line in open(src, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'== (R\d+) (\S+)', line)
        if m:
            rec, img = m.group(1), m.group(2)
            continue
        if line.strip() and rec:
            pages.setdefault(rec, []).append((img, line))
    for rec, pl in pages.items():
        path = os.path.join(ROOT, 'decode_updates', 'decryptions', f'{rec}.txt')
        if skip and os.path.exists(path):
            continue
        body = []
        for img, line in pl:
            body.append(f'[IMG {img.rsplit(".", 1)[0]}]')
            body += textwrap.wrap(clean_line(line), 108, break_on_hyphens=False)
            body.append('')
        open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(body).rstrip('\n') + '\n')
        print(rec, len(pl), 'pages ->', path)


if __name__ == '__main__':
    main()
