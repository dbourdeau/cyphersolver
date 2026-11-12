"""Rebuild the decryption from transcription + frozen key and check that the reading departs from it only where marked.

Marks allowed in the reading: {CODE=meaning} (resolved code word, must equal the decryption's), |WORD| (unidentified
code word, must equal the decryption's), {x/y} (x as decrypted, y as read). Case, accents and punctuation are ignored
(the teleprinter has no accents and PT is the full stop). Exit 1 on any unmarked departure.

    python scripts/check_marks.py
"""
import sys, re, pathlib, subprocess, unicodedata

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / 'scripts'))
import decrypt  # noqa: E402


def norm(w):
    w = ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^\w=|{}/. ]', '', w).upper()


def tokens_reading(text):
    out = []
    for m in re.finditer(r'\{[^}]*\}|\|[^|]*\||[^\s{|]+', text):
        t = m.group(0)
        if t.startswith('{') and '/' in t and '=' not in t:
            x, y = t[1:-1].split('/', 1)
            out.append(('repair', norm(x)))
        elif t.startswith('{') or t.startswith('|'):
            out.append(('mark', norm(t.rstrip('.,;:'))))
        else:
            w = norm(re.sub(r'[.,;:!?]+$', '', t))
            if w:
                out.append(('plain', w))
    return out


def main():
    key = decrypt.load_key(HERE / 'key_frozen.tsv')
    dec = []
    for lab, words in decrypt.text_lines(HERE / 'transcription_goulart1946.txt'):
        dec += [norm(x) for x in decrypt.decode(words, key) if x not in ('.', '=')]
    # the published decryption file must equal the rebuild
    pub = []
    for line in (HERE / 'decryption_goulart1946.txt').read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('L'):
            pub += [norm(x) for x in re.findall(r'\{[^}]*\}|\|[^|]*\||\S+', line.split(' ', 1)[1]) if x not in ('.', '=')]
    ok = True
    if pub != dec:
        print('FAIL: decryption_goulart1946.txt differs from the rebuild'); ok = False
    rd = []
    rpath = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'reading_goulart1946.md'
    for line in rpath.read_text(encoding='utf-8-sig').splitlines():
        if re.match(r'L\d\d ', line):
            rd += tokens_reading(line.split(' ', 1)[1])
    if len(rd) != len(dec):
        print('FAIL: reading has %d words, decryption %d' % (len(rd), len(dec))); ok = False
    n_rep = 0
    for i, ((kind, w), d) in enumerate(zip(rd, dec)):
        if kind == 'repair':
            n_rep += 1
            if w != d:
                print('FAIL word %d: repair source %r is not the decrypted %r' % (i + 1, w, d)); ok = False
        elif w != d:
            print('FAIL word %d: %r read, %r decrypted, not marked' % (i + 1, w, d)); ok = False
    print('words %d, marked repairs %d, result %s' % (len(dec), n_rep, 'PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
