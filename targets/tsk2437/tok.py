"""Convert a positioned pass file (pass1.txt, pass2.txt, final.txt) to a line transcription and token file.
Usage: python tok.py <passfile> <out transcription> [--tokens <cipher_tokens out>]
Pass file rows: L<n>|x|code|grade|note.  code '|' = gap/hole/tear (written '|'), '-' dash, '.' dot."""
import re
import sys

ROW = re.compile(r'^(L\d)\|(\d+)\|(.*?)\|(firm|likely|doubtful|gap|hole|tear|rubbed)\|(.*)$')


def parse(path):
    rows = []
    for l in open(path, encoding='utf-8'):
        m = ROW.match(l.rstrip('\n'))
        if m:
            rows.append((m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5)))
    return rows


def lines(rows):
    out = {}
    for ln, x, code, grade, note in rows:
        out.setdefault(ln, []).append((x, code, grade))
    return out


if __name__ == '__main__':
    rows = parse(sys.argv[1])
    L = lines(rows)
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write('# T-S K24.37 recto, positioned transcription (%s), page order left to right, shape-true classes (legend.txt).\n' % sys.argv[1])
        f.write("# '-' dash, '.' dot, '|' hole/tear/rubbed gap, '?' unreadable sign. Reading direction not assumed.\n")
        for ln in sorted(L, key=lambda s: int(s[1:])):
            f.write('%s: %s\n' % (ln, ' '.join(c for x, c, g in L[ln])))
    if '--tokens' in sys.argv:
        t = sys.argv[sys.argv.index('--tokens') + 1]
        with open(t, 'w', encoding='utf-8') as f:
            for ln in sorted(L, key=lambda s: int(s[1:])):
                f.write(' '.join(c for x, c, g in L[ln] if c not in ('-', '.', '|')) + '\n')
    n = sum(1 for r in rows if r[2] not in ('-', '.', '|'))
    print('signs (incl ?):', n, 'rows', len(rows))
