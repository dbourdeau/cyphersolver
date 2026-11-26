"""barlow1812: the Paris legation code of 1811-1813 ("the" = 1700) applied to two passages that carry no decipherment.

    python decode.py            re-derive decryption_*.txt from transcription_*.txt and key.tsv and compare (exit 1 on a difference)
    python decode.py --write    write the decryption files afresh
    python decode.py 1114 703   decode numbers given on the command line

key.tsv holds only values written or implied by decipherers of the time (grades P, C, D, W, L: see key.md).
proposals.tsv holds OUR values for the numbers that have none there; they are shown with grade ? and are doubtful.
Standard library only.
"""
import csv, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
DOCS = ('1812-09-25', '1812-10-25_A', '1812-10-25_B')
NUM = re.compile(r"(?<![\w'])(~?\^?)(\d{2,4})(\??)(\^?~?)(?![\w'])")


def load():
    key, prop = {}, {}
    for r in csv.DictReader((HERE / 'key.tsv').open(encoding='utf-8'), delimiter='\t'):
        if r['value']:
            key[int(r['number'])] = (r['value'], r['grade'])
    p = HERE / 'proposals.tsv'
    if p.exists():
        for r in csv.DictReader(p.open(encoding='utf-8'), delimiter='\t'):
            prop[int(r['number'])] = r['value']
    return key, prop


def decode_number(n, key, prop):
    if n in key:
        v, g = key[n]
        return f'{n}={v}/{g}'
    if n in prop:
        return f'{n}={prop[n]}/?'
    return f'{n}=?'


def decode_line(text, key, prop):
    """One manuscript line: numbers become number=value/grade; words in clear are kept in double quotes."""
    out, pos = [], 0
    for m in NUM.finditer(text):
        clear = text[pos:m.start()].strip(' ,-')
        if re.search(r'[A-Za-z&]', clear):
            out.append('"' + re.sub(r'\s+', '_', clear.strip()) + '"')
        n = int(m.group(2)); tok = decode_number(n, key, prop)
        if '~' in m.group(1): tok = '~' + tok + '~'          # struck out in the manuscript
        if '^' in m.group(1): tok = '^' + tok                # written above the line
        if m.group(3): tok += ' (digit doubtful)'
        out.append(tok); pos = m.end()
    clear = text[pos:].strip(' ,-')
    if re.search(r'[A-Za-z&]', clear):
        out.append('"' + re.sub(r'\s+', '_', clear.strip()) + '"')
    return '  '.join(out)


def derive(doc, key, prop):
    lines = []
    for ln in (HERE / f'transcription_{doc}.txt').read_text(encoding='utf-8').splitlines():
        if not ln.strip() or ln.startswith('#'): continue
        label, _, text = ln.partition(':')
        if label.endswith('*'):                       # a starred label marks a line that carries code numbers
            lines.append(f'{label.strip().rstrip("*"):<8}{decode_line(text, key, prop)}')
    return lines


def header(doc):
    return [f'# barlow1812: group-by-group decryption of transcription_{doc}.txt with key.tsv, line by line. Output of: python decode.py --write',
            '# number=value/grade. Grades (key.md): P, C, D, W = values written or implied by decipherers of 1811-1813; L = doubtful occurrence only;',
            '# ? after the slash = OUR proposal from the sense (proposals.tsv), not in the key; number=? = no value at all.',
            '# "words" = written in clear in the manuscript; ^ = written above the line; ~...~ = struck out. Only lines that carry numbers are listed.']


def main(argv):
    key, prop = load()
    if argv and argv[0] not in ('--write',):
        print('  '.join(decode_number(int(a), key, prop) for a in argv)); return 0
    bad = 0
    for doc in DOCS:
        want = header(doc) + derive(doc, key, prop)
        path = HERE / f'decryption_{doc}.txt'
        if argv == ['--write']:
            path.write_text('\n'.join(want) + '\n', encoding='utf-8'); print(f'wrote {path.name}: {len(want) - 4} lines'); continue
        have = path.read_text(encoding='utf-8').splitlines()
        n = sum(len(NUM.findall(l.partition(':')[2])) for l in (HERE / f'transcription_{doc}.txt').read_text(encoding='utf-8').splitlines()
                if l.strip() and not l.startswith('#') and l.partition(':')[0].endswith('*'))
        ok = have == want; bad += not ok
        print(f'{doc}: {len(want) - 4} coded lines, {n} numbers: {"ok" if ok else "DIFFERS"}')
    print('result: ok' if not bad else 'result: FAIL')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
