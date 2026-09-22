"""Read bar: share of words in a fit output that came out as lexicon words.

A word in <> is one the fit could not match (emitted raw, sign by sign); a clear
passage in [] counts as read, since it stands in clear in the document. One-letter
matches are counted as unread too: a stray 'a' or 'e' is not a reading.
"""
import re
import sys

tot = bad = 0
for fn in sys.argv[1:]:
    for ln in open(fn, encoding='utf-8'):
        m = re.match(r'\S+ \S+ (.*)', ln.rstrip('\n'))
        if not m:
            continue
        for w in re.findall(r'\[[^\]]*\]|<[^>]*>|\S+', m.group(1)):
            tot += 1
            if w.startswith('<') or (len(w) == 1 and w.isalpha()):
                bad += 1
print('words %d  unread %d  read %.1f%%' % (tot, tot - bad, 100.0 * (tot - bad) / tot))
