"""Decode a system A cipher transcription with key_c01 and place each line in a clear text.

usage: python3 -I sysA_place.py <key.json> <cipher.txt> <clear.txt>

Groups below 100 and keyless groups decode to nothing (unknown groups show as <nnn>). Each decoded line is
placed in the normalised clear (letters a-z only) by the matching blocks of 3 letters or more that
difflib finds between the line and the clear; the line's place is the median clear position of the matched
letters, and the clear word nearest it is printed with the share of the line's letters matched.
"""
import json, re, sys, difflib, unicodedata, statistics


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', s)


def read_clear(path):
    """Clear lines -> (normalised string, list of (pos, label, word)) with struck text removed."""
    text, words = '', []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.rstrip('\n').partition(' ')
        if '[archivist note]' in body:
            continue
        body = re.sub(r'\[del:[^\]]*\](\[\?\])?', '', body)
        body = re.sub(r'\{ins:([^}]*)\}', r'\1', body)
        for w in body.split():
            n = norm(w)
            if n:
                words.append((len(text), lab, w))
                text += n
    return text, words


def read_cipher(path):
    lines = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab, _, body = line.rstrip('\n').partition(' ')
        if lab.endswith('G') or lab.endswith('T'):
            continue
        body = re.sub(r'\[del:[^\]]*\]', '', body)
        toks = [t for t in re.split(r'[\s.|]+', body) if re.search(r'\d', t)]
        lines.append((lab, toks))
    return lines


def main():
    key = {k: (v[0] if v else '') for k, v in json.load(open(sys.argv[1])).items()}
    clear, words = read_clear(sys.argv[3])
    for lab, toks in read_cipher(sys.argv[2]):
        out, dec = [], ''
        for t in toks:
            g = re.sub(r'[^0-9]', '', t)
            if not g:
                continue
            g = str(int(g))
            if int(g) < 100 or g in ('400', '508') or key.get(g) == '' and g in key:
                continue
            if g in key:
                out.append(key[g])
                dec += norm(key[g])
            else:
                out.append('<%s>' % g)
        sm = difflib.SequenceMatcher(None, dec, clear, autojunk=False)
        pos = [b.b + i for b in sm.get_matching_blocks() if b.size >= 3 for i in range(b.size)]
        if pos:
            med = statistics.median(pos)
            near = min(words, key=lambda w: abs(w[0] - med))
            place = '%s "%s" %.2f' % (near[1], near[2], len(pos) / max(1, len(dec)))
        else:
            place = '-'
        print('%-9s %-34s %s' % (lab, place, ' '.join(out)))


if __name__ == '__main__':
    main()
