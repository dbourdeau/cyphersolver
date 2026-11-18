#!/usr/bin/env python3
"""Regenerate every decryption file from key.tsv and the transcriptions. Standard library only.

    python scripts/decrypt.py          writes decryption_*.txt next to the transcriptions

Rules: a token with a trailing _ is a sign cancelled by dots under it and prints as a dot; # is an ink blot and prints
nothing; {word} is a word-like group written in plain letters; a token with no value prints as [token]. Blind passes
use the reader's own sign names, mapped to the names of key.tsv by scripts/blind_name_map.json (from the alignment of
14 Nov), so their decodings keep that reader's errors.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SIGNS = {
    'ch1549_1114': 'Charles V, 14 Nov 1549.',
    '1547_c09': 'Philip, 23 May 1547, cc. 9r-9v.',
    '1548_c10r': 'Philip, 4 Aug 1548, c. 10r.',
    '1549_c12r': 'Philip, 8 Mar 1549, c. 12r.',
    '1551_c26r': 'Philip, 24 Nov 1551, c. 26r.',
    '1551_c28r': 'Philip, 24 Nov 1551, c. 28r.',
    'ch1549_c30r': 'Charles V, 13 May 1549, c. 30r.',
}
BLIND = {
    'ch1549_0930_1120_blind': 'Blind pass decoded with key.tsv, unrepaired. Sign names mapped automatically, so errors remain. Group T overlaps the 14 Nov letter.',
    'philip_1546_1553_x_blind': 'Blind rough pass decoded with key.tsv, unrepaired. Decoded, not read. Group C is unreliable (bleed-through).',
}


def load_key():
    k = {}
    for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        p = l.split('\t')
        k[p[0]] = p[1]
    return k


def sign_lines(key, path):
    out, miss = [], {}
    for l in path.read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        t = l.split()
        o = []
        for s in t[1:]:
            w = s.strip('{}')
            if s == '#':
                continue
            if s.endswith('_'):
                o.append('.')
            elif w in key:
                o.append(key[w])
            else:
                o.append('[' + w + ']')
                miss[w] = miss.get(w, 0) + 1
        out.append(t[0] + ' ' + ''.join(o))
    return out, miss


def blind_lines(key, names, path):
    out = []
    for l in path.read_text(encoding='utf8').splitlines():
        if l.startswith('#'):
            out.append(l.strip())
        if l.startswith('#') or not l.strip():
            continue
        t = l.split()
        o = []
        for s in t[1:]:
            s = s.rstrip('?').strip('{}')
            s2 = names.get(s, s)
            if s2.endswith('_'):
                continue
            o.append(key.get(s2, key.get(s, '[' + s + ']')))
        out.append(t[0] + ' ' + ''.join(o))
    return out


def main():
    key = load_key()
    for name, head in SIGNS.items():
        lines, miss = sign_lines(key, ROOT / f'transcription_{name}.txt')
        text = [f'# {head} Sign-by-sign decryption with key.tsv, unrepaired.', '# Dot = sign cancelled by dots beneath. [x] = no value.'] + lines
        if miss:
            text.append('# tokens without a value: ' + ', '.join(f'{a} ({b})' for a, b in sorted(miss.items())))
        (ROOT / f'decryption_{name}.txt').write_text('\n'.join(text) + '\n', encoding='utf8', newline='\n')
    names = json.loads((ROOT / 'scripts' / 'blind_name_map.json').read_text(encoding='utf8'))
    for name, head in BLIND.items():
        lines = blind_lines(key, names, ROOT / f'transcription_{name}.txt')
        (ROOT / f'decryption_{name}.txt').write_text('\n'.join(['# ' + head] + lines) + '\n', encoding='utf8', newline='\n')


if __name__ == '__main__':
    main()
