"""Decode every transcription file in transcription/ with the frozen key.txt, for reading (not a test).

    python3 -I scripts/decode_all.py          (run from beling/; writes results/decode_all.txt)

Per line: the decrypt with the writer's word gaps kept as spaces; code groups as [n], numbers below 60 the key
lacks as <n>, unread signs as ?, clear words as {..}; '*' marks a letter from a doubtful reading.
Files in page order; the build lines (key/transcription_build.txt) are included so each page reads in order.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location('t1', os.path.join(HERE, 'scripts', 'test_m0271.py'))
t1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(t1)
FILES = [('build', os.path.join('key', 'transcription_build.txt'))] + [
    (f, os.path.join('transcription', f)) for f in
    ['m0265_rest.txt', 'm0266_rest.txt', 'm0267.txt', 'm0269_rest.txt', 'm0271.txt', 'm0271_r2.txt', 'm0272.txt',
     'm0273_top.txt']]


def decode_body(body, key):
    words = []
    for w in body.split('|'):
        w = w.strip()
        out = ''
        for part in re.split(r'(\{[^}]*\})', w):
            if part.startswith('{'):
                out += part
                continue
            for t in part.split('.'):
                t = t.strip()
                if not t:
                    continue
                star = t.endswith('*')
                n = t.rstrip('*')
                if not n.isdigit():
                    out += '?'
                    continue
                v = int(n)
                if v >= 60:
                    s = '[%d]' % v
                elif v in key:
                    s = key[v]
                else:
                    s = '<%d>' % v
                out += s + ('*' if star else '')
        words.append(out)
    return ' '.join(words)


def main():
    key = t1.load_key(os.path.join(HERE, 'key', 'key.txt'))
    lines = []
    for name, rel in FILES:
        page_lines = []
        with open(os.path.join(HERE, rel), encoding='utf-8') as fh:
            for raw in fh:
                if raw.startswith('@'):
                    tag, body = raw.rstrip('\n').split(' ', 1)
                    page_lines.append((tag, name, decode_body(body, key)))
        lines.extend(page_lines)

    def order(item):
        tag, name, _ = item
        m = re.match(r'@m(\d+)\.(e?)(\d+|dk|end)', tag)
        page, e, num = m.group(1), m.group(2), m.group(3)
        n = {'dk': 0, 'end': 999}.get(num, None)
        if n is None:
            n = int(num) + (900 if e else 0)
        return (page, name == 'm0271_r2.txt', n)
    lines.sort(key=order)
    with open(os.path.join(HERE, 'results', 'decode_all.txt'), 'w', encoding='utf-8') as fh:
        fh.write('# All transcribed cipher A lines decoded with key.txt (reading aid; not a test). [n] code group, '
                 '<n> number the key lacks, ? unread, * doubtful. m0273.eNN = the last 12 lines of m0273.\n')
        for tag, name, text in lines:
            fh.write('%-11s %-15s %s\n' % (tag, name, text))
    print('lines', len(lines))


if __name__ == '__main__':
    sys.exit(main())
