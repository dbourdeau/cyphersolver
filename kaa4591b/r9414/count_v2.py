"""Strict count for reading_v2.txt: words outside <..>; [..N] = N unread; a word with ? = unread; a split word (ends '-') joined to the next line."""
import re, sys
f = sys.argv[1] if len(sys.argv) > 1 else 'reading_v2.txt'
text = ' '.join(re.sub(r'^P\d\.\d\d ', '', l.strip()) for l in open(f, encoding='utf8') if l[:1] == 'P')
text = re.sub(r'<[^>]*>', ' ', text)
text = re.sub(r'-\s+', '', text)            # rejoin hyphenated words
read = unread = 0; per = {}
for tok in text.split():
    m = re.fullmatch(r'\[\.\.(\d+)\]', tok)
    if m: unread += int(m.group(1)); continue
    w = tok.strip('.,;:')
    if not w: continue
    if '?' in w: unread += 1
    else: read += 1
tot = read + unread
print(f'words {tot}  read {read}  unread {unread}  read% {100*read/tot:.1f}')
