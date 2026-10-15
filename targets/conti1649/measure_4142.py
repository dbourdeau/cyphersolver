"""Measure nos. 41-42 (14 Oct 2026, one-key split): cipher signs in transcription.txt outside the [..] clear words,
and how many have a value under Lasry's key ('?' = illegible sign, unread). Every legible sign has a value: the
polyphonic signs get one letter each from decode.py's choice."""
import re
SIGNS = set('Jcstuvgrdolaemn' + 'Di')
total = unread = 0
for line in open('transcription.txt', encoding='utf-8'):
    if line.startswith('#') or line.startswith('=='):
        continue
    for ch in re.sub(r'\[[^\]]*\]', '', line):
        if ch.isspace():
            continue
        total += 1
        if ch == '?' or ch not in SIGNS:
            unread += 1
print(f'{total} cipher signs, {unread} unread; {total - unread} of {total} have a value ({(total - unread) / total:.1%})')
