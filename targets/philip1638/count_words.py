"""Count the words of reading.md by the README read rule (only sure words count as read).

A word is one whitespace-separated item of the text lines (L01-02 ... L69); a word cut at a line end with '-' is
joined to the first item of the next line and counted once. One class per word, the weakest:
‹...› unresolved, [..] restored or corrected, {..} probable; a word with none of them is sure.
"""
import re, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
lines = [l for l in (HERE / 'reading.md').read_text(encoding='utf-8').splitlines() if re.match(r'^L\d', l)]
words, carry = [], ''
for l in lines:
    body = l.split(' ', 1)[1].strip().split()
    if carry and body:
        body[0] = carry + body[0]; carry = ''
    if body and body[-1].endswith('-'):
        carry = body.pop()[:-1]
    words += body
if carry:
    words.append(carry)
words = [w for w in words if re.search(r'\w', w)]
def cls(w):
    if '‹' in w: return 'unresolved'
    if '[' in w: return 'restored'
    if '{' in w: return 'probable'
    return 'sure'
c = collections.Counter(cls(w) for w in words)
n = len(words)
print(f"{n} words: {c['sure']} sure, {c['probable']} probable, {c['restored']} restored, {c['unresolved']} unresolved;"
      f" holes {n - c['sure']}; sure share {c['sure'] / n:.3f}")
