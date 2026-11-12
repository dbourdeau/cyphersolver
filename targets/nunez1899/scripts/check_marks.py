"""Rebuild the decryption from reading_9926.md by undoing the marks and compare it, line by line, with the mechanical
decryption from transcription + key (decrypt.py). Fails (exit 1) on any unmarked departure.
Marks: {+x} added, {-x} dropped, {a/b} changed, [?x] guess for a [...] hole."""
import re, sys
from common import HERE, read_lines, read_key, decrypt_tokens, strip_acc
key = read_key(HERE / 'key.tsv')
mech = {}
for lab, toks in read_lines(HERE / 'transcription_9926.txt'):
    ws = []
    for code, val in decrypt_tokens(toks, key):
        ws += (code if val is None else val).split()
    mech[lab] = ws
def norm(ws):
    out = []
    for w in ws:
        w = strip_acc(w.lower()).strip(',;:')
        w = w.rstrip('.')
        if w:
            out.append(w)
    return out
bad = 0; n = 0
for ln in open(HERE / 'reading_9926.md', encoding='utf-8'):
    m = re.match(r'^(L\d\d) \| (.*)$', ln.rstrip('\n'))
    if not m:
        continue
    lab, txt = m.groups(); n += 1
    txt = re.sub(r'\{\+[^}]*\}', ' ', txt)
    txt = re.sub(r'\{-([^}]*)\}', r' \1 ', txt)
    txt = re.sub(r'\{([^}/]*)/[^}]*\}', r' \1 ', txt)
    txt = re.sub(r'\[\?[^\]]*\]', ' [...] ', txt)
    a, b = norm(txt.split()), norm(mech[lab])
    if a != b:
        bad += 1; print('MISMATCH', lab, '\n  reading :', a, '\n  mechanic:', b)
print(f'{n} lines checked, {bad} mismatches')
sys.exit(1 if bad or n != len(mech) else 0)
