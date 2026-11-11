"""lee1813: William Lee's WINCHESTER cipher (Paris, February 1813). Re-derive the decryption files from the transcriptions.

    python decode.py              check every stretch of the three letters: the numerals in decryption_*.txt match
                                  transcription_*.txt, and the baseline and "used" mechanical texts follow from them
    python decode.py 5 1 22 13    decode numerals with the key restarted at W (offset 0)
    python decode.py --offset 3 5 1 22    the same with the key started at keyword position 3

The rule (key.md): plaintext = ALPHABET[(numeral - 1 + ALPHABET.index(KEY[(i + offset) % 10])) % 25], i = 0-based position
in the stretch. Offsets that change inside a stretch (Lee's slips) are given per run as "first-last:offset".
The language-model decoder that proposed those paths (letter 4-grams, 9.0 nats per offset change, 200 shuffled controls)
is described in NOTES.md; it needs a corpus that is not in this repository, so it is not included. Standard library only.
"""
import pathlib, re, sys

ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'        # 25 letters, I and J one letter
KEY = 'WINCHESTER'
HERE = pathlib.Path(__file__).resolve().parent
LETTERS = ('1813-02-01', '1813-02-02', '1813-02-06')


def decode(numerals, runs=None):
    """runs: [(first, last, offset)], 1-based inclusive; default offset 0 throughout."""
    runs = runs or [(1, len(numerals), 0)]
    out = []
    for i, n in enumerate(numerals):
        off = next(o for a, b, o in runs if a <= i + 1 <= b)
        out.append(ALPHABET[(n - 1 + ALPHABET.index(KEY[(i + off) % 10])) % 25])
    return ''.join(out)


def parse_runs(text):
    return [tuple(map(int, m)) for m in re.findall(r'(\d+)-(\d+):(\d+)', text)]


def transcription(date):
    """{stretch id: numerals} from transcription_<date>.txt (a numeral line is followed by '# <id>  frame ...')."""
    lines = (HERE / f'transcription_{date}.txt').read_text(encoding='utf-8').splitlines()
    out = {}
    for prev, line in zip(lines, lines[1:]):
        m = re.match(r'# (\S+)  frame ', line)
        if m: out[m.group(1)] = [int(t) for t in prev.split() if t.isdigit()]
    return out


def decryption(date):
    out, cur = {}, None
    for line in (HERE / f'decryption_{date}.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'(\S+)  frame ', line)
        if m: cur = out.setdefault(m.group(1), {}); continue
        m = re.match(r'  (\w+)\s+(.*)$', line)
        if cur is not None and m: cur[m.group(1)] = m.group(2)
    return out


def check():
    bad = total = 0
    for date in LETTERS:
        tr, de = transcription(date), decryption(date)
        for sid, ns in tr.items():
            total += 1
            d = de.get(sid, {})
            problems = []
            if [int(x) for x in d.get('numerals', '').split()] != ns: problems.append('numerals differ')
            if d.get('baseline') != decode(ns): problems.append('baseline differs')
            if d.get('used', '').startswith('none'):
                pass
            elif 'used' in d and d.get('mech') != decode(ns, parse_runs(d['used'])): problems.append('used text differs')
            if problems:
                bad += 1; print(date, sid, '; '.join(problems))
        print(f'{date}: {len(tr)} stretches, {sum(map(len, tr.values()))} numerals')
    print(f'result: {"ok" if not bad else f"{bad} problem(s)"} ({total} stretches checked)')
    return bad


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(1 if check() else 0)
    off = 0
    if a[0] == '--offset': off, a = int(a[1]), a[2:]
    print(decode([int(x) for x in a], [(1, len(a), off)]))
