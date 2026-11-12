#!/usr/bin/env python3
"""Mechanical line-by-line decode of a catalogue 650 letter transcription (letters/<date>_No<n>/transcription.txt).

Usage: python3 decode650.py TRANSCRIPTION [OVERRIDE ...]
  OVERRIDE is LINE:OLD=NEW, a text replacement on one transcription line before decoding, e.g. 112.10:69<[?]=69^
  (used only where the collation of copies adopts another copy's reading; see each letter's line_by_line_decode.txt).

Key: ../key/codebook_M97_13_transcription.csv (WE028, the = 1385; its sha256 is printed). Morris's copy numbers the
16 blocks of 100 in reverse order: Morris m -> code 100*(15-i) + m - 100*i, with i = (m-1)//100.
Output: each group as m=value, marks in [] ([c] hook, [3]/[5] strokes, < angle, ^ triangle), ? for a doubtful group,
{...} for words Morris wrote in clear. No mark rules, no context: the reading is in reading.txt.
Python standard library only."""
import csv, hashlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
KEY_PATH = HERE.parent / 'key' / 'codebook_M97_13_transcription.csv'
raw = KEY_PATH.read_bytes()
KEY = {}
for r in csv.DictReader(raw.decode('utf-8').splitlines()):
    KEY[int(r['code_number'])] = r['reading'] or ''


def tj(m):
    """Morris number -> number in the State Department code (blocks of 100 reversed)."""
    i = (m - 1) // 100
    return 100 * (15 - i) + m - 100 * i


def val(m):
    if not 1 <= m <= 1600:
        return None
    return KEY[tj(m)] or None


def tokens(body):
    body = re.sub(r'\{[^}]*\}', '', body)          # drop variant notes {copy:reading}
    out = []
    for t in re.findall(r'\|[^|]*\||\S+', body):
        if t[0] == '|':
            out.append(('clear', t.strip('|')))
            continue
        for g in [x for x in t.split('.') if x]:
            d = re.sub(r'\[[^\]]*\]|[<^]', '', g)
            if re.fullmatch(r'\d+', d):
                marks = ''.join(re.findall(r'\[([c35]+)\]', g)) + ('<' if '<' in g else '') + ('^' if '^' in g else '')
                out.append(('code', int(d), marks, '[?]' in g))
            elif g.strip():
                out.append(('clear', g))
    return out


def load(path, overrides=()):
    lines = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or ':' not in l:
            continue
        lab, body = l.split(':', 1)
        for o in overrides:
            k, v = o.split('=', 1)
            ol, old = k.split(':', 1)
            if ol == lab.strip():
                body = body.replace(old, v)
        lines.append((lab.strip(), tokens(body)))
    return lines


if __name__ == '__main__':
    print('# key', KEY_PATH.name, 'sha256', hashlib.sha256(raw).hexdigest())
    if sys.argv[2:]:
        print('# overrides', ' '.join(sys.argv[2:]))
    for lab, toks in load(sys.argv[1], sys.argv[2:]):
        out = []
        for t in toks:
            if t[0] == 'clear':
                out.append('{' + t[1] + '}')
            else:
                v = val(t[1])
                out.append(f"{t[1]}={v if v is not None else '[blank]'}" + (f"[{t[2]}]" if t[2] else '') + ('?' if t[3] else ''))
        print(lab + ': ' + ' | '.join(out))
