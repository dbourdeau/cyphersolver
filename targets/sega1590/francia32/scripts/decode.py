"""Decode the rows of this folder with Meister's key no. 65, as the record pages show it.

Usage: python3 scripts/decode.py transcription/R5612_f017r_digits.txt [...]
Prints one decode line for each row: its label, then the decode. Clear text (‖) stays ‖.
The rules are those of key/README.md, "How the decode reads a row". This is the decoder of
17 November 2026, cut down to the rows files; its known faults are listed in check.md.
"""
from __future__ import annotations

import re
import sys
import unicodedata

# Meister 1906, key no. 65, as targets/sega1590/key.tsv of this ledger gives it.
PAIRS = {'21': 'b', '22': 'c', '23': 'd', '24': 'e', '25': 'f', '26': 'g', '27': 'h', '28': 'i', '29': 'l',
         '31': 'n', '32': 'o', '33': 'p', '34': 'qu', '35': 'r', '36': 's', '37': 't', '38': 'u', '39': 'x',
         '41': 'et', '42': 'a', '52': 'm', '62': 'z'}
CODES = {'a': 'perche', 'b': 'che', 'c': 'per', 'd': 'onde', 'e': 'come', 'f': 'cosi', 'g': 'quando',
         'h': 'pero', 'k': 'siche', 'l': 'il', 'm': 'lo', 'n': 'la', 'o': 'quale', 'p': 'quello', 'q': 'ha',
         'r': 'ho', 't': 'hora', 'u': 'del', 'x': 'della', 'y': 'delli', 'z': 'non'}
# Vowel signs (combining marks); the last four are sign forms read as the key's signs (key/key.tsv).
SIGN = {'̈': 'a', '̂': 'e', '̄': 'i', '⁺': 'o', '̅': 'i', '̵': 'o',
        'ˢ': 'u', '²': 'u'}
DOT = {'̇', '·'}
SHAPES = {'ω': 'in', '∞': '<con?>', '#': '<sym>'}
NAMES = {'453': 'Villeroy'}
NOTE = re.compile(r'^(\s*\[[^\]]*(?:label|location|recto|verso|face|row|margin|strip|F\d)[^\]]*\])+')


def lex(row: str) -> list[tuple[str, str]]:
    """Tokens: d = digit with marks, w = lone letter, s = symbol, c = clear text, b = anything else."""
    s = unicodedata.normalize('NFD', NOTE.sub(' ', row))
    out: list[tuple[str, str]] = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '[':
            j = s.find(']', i)
            j = len(s) if j < 0 else j
            m = re.fullmatch(r'(\d[^\d|\s]*)(\|.*)?\?', s[i + 1:j])
            out.append(('d', m.group(1)) if m else ('b', s[i + 1:j]))
            i = j + 1
        elif ch == '⟨':
            j = s.find('⟩', i)
            j = len(s) if j < 0 else j
            inner = s[i + 1:j]
            if sum(c.isdigit() for c in re.sub(r'\[[^\]]*\]', '', inner)) >= 4:
                out.extend(lex(inner))
            else:
                out.append(('s', inner.strip()))
            i = j + 1
        elif ch.isdigit():
            j = i + 1
            while j < len(s) and (unicodedata.category(s[j]) == 'Mn' or s[j] in '⁺·ˢ²'):
                j += 1
            out.append(('d', s[i:j]))
            i = j
        elif ch.isalpha():
            j = i
            while j < len(s) and (s[j].isalpha() or unicodedata.category(s[j]) == 'Mn' or s[j] in "'’"):
                j += 1
            out.append(('w', s[i:j]) if j - i == 1 else ('c', s[i:j]))
            i = j
        elif ch == '‖':
            out.append(('c', ch))
            i += 1
        elif ch in ' \t':
            i += 1
        elif ch in 'ω∞#':
            out.append(('s', ch))
            i += 1
        else:
            out.append(('b', ch))
            i += 1
    return out


def decode(tokens: list[tuple[str, str]]) -> str:
    out: list[str] = []
    pend: str | None = None
    for kind, t in tokens:
        if kind == 'd':
            d, mk = t[0], t[1:]
            sign = next((SIGN[c] for c in mk if c in SIGN), None)
            dot = any(c in DOT for c in mk)
            if dot and pend is None and out and re.fullmatch(r'\{\d\d\}', out[-1]):
                code = out.pop()[1:3] + d
                out.append('{' + NAMES.get(code, code) + '}')
                continue
            if pend is not None:
                if mk and not dot:
                    out.append('?')
                    pend = None
                else:
                    p, pend = pend + d, None
                    out.append(('{' + p + '}' if dot else PAIRS[p]) if p in PAIRS else '{' + p + '}')
                    continue
            if mk and not dot:
                if d not in '7890':
                    out.append(sign or '?')
            elif d not in '78901':
                pend = d
        else:
            if pend is not None:
                out.append('?')
                pend = None
            if kind in ('w', 's') and len(t) == 1 and t.lower() in CODES:
                out.append('[' + CODES[t.lower()] + ']')
            elif kind == 's' and t in SHAPES:
                out.append('[' + SHAPES[t] + ']')
            elif kind == 's':
                out.append('<' + t[:12] + '>')
            elif kind == 'c':
                out.append(' ‖ ')
    if pend is not None:
        out.append('?')
    text = re.sub(r'\{(\d\d)\}', r'<\1>', ''.join(out))
    text = re.sub(r'‖(\s*‖)+', '‖', text)
    return re.sub(r'\s+', ' ', text).strip()


def main() -> None:
    for path in sys.argv[1:]:
        for line in open(path, encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            label, _, body = line.rstrip('\n').partition(' ')
            print(f'{label}: {decode(lex(body))}')


if __name__ == '__main__':
    main()
