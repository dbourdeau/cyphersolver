"""Parse the image re-read of R91 (reread/<folio>.txt) into token lines.

Token forms in the re-read: 8, 8? (uncertain), 8^ (dot above), 8^^, 8^? (possible dot), '.' / '.?' (baseline mark),
'/' (heavy stroke), '[ ... ]' (struck by the scribe: dropped), '?' alone (a digit lost to a corrosion hole).

lines() yields (folio, line, tokens), each token a dict(d=<digit or None for lost>, dot=0/1/2, unsure=bool, mark=str).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
RR = os.path.join(HERE, 'reread')
FOLIOS = ['64r', '64v', '65r']


def parse_line(s):
    s = re.sub(r'\[[^\]]*\]', ' ', s)          # struck digits out
    toks = []
    for t in s.split():
        if t in ('.', '.?', '/', ':'):
            toks.append(dict(d=None, dot=0, unsure=False, mark=t)); continue
        m = re.fullmatch(r'(\d)(\^*)(\??)(\^*)(\??)', t)
        if m:
            dots = len(m.group(2)) + len(m.group(4))
            unsure_dot = bool(m.group(3)) and dots and m.group(2) or bool(m.group(5))
            toks.append(dict(d=int(m.group(1)), dot=dots, unsure=bool(m.group(3) and not m.group(2)),
                             dotq=bool(dots and (m.group(3) or m.group(5))), mark=''))
        elif re.fullmatch(r'\?+', t):
            toks.append(dict(d=None, dot=0, unsure=True, mark='lost'))
        else:
            toks.append(dict(d=None, dot=0, unsure=True, mark='odd:' + t))
    return toks


def lines():
    for f in FOLIOS:
        p = os.path.join(RR, f + '.txt')
        if not os.path.exists(p):
            continue
        for raw in open(p, encoding='utf-8'):
            m = re.match(r'(\d+):\s(.*)$', raw.rstrip('\n'))
            if m:
                yield f, int(m.group(1)), parse_line(m.group(2))


if __name__ == '__main__':
    from collections import Counter
    dots, n, lost = Counter(), 0, 0
    for f, l, toks in lines():
        for t in toks:
            if t['d'] is not None:
                n += 1
                if t['dot']:
                    dots[t['d']] += 1
            elif t['mark'] == 'lost':
                lost += 1
    print('digits', n, 'lost', lost, 'dots by digit', sorted(dots.items()))
