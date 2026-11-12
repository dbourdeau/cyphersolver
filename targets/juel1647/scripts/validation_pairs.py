"""validation_pairs.py: writes validation.tsv (cipher token TAB reading) for Dan's docs/_validate.py, for the 8-64 table
only (king and chancellor passages, p. 5). The reading per token is the frozen key's letter, '-' for a null, and '?'
for codes, open numbers (11, 12, 13), doubtful groups and every letter of a word the reading marks as a hole or a guess.
The vibe passage (p. 115) is left out: Vibe's old cipher shifts per word, so one token has no fixed value."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import load_key, tokens
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
K = load_key()
# letter stretches of the mechanical decryption (nulls left out) that the readings mark as a hole or a guess
# ('trgese' is split at its doubtful group 33|53)
UNREAD = {'chancellor': ['kbags', 'tay', 'taysign', 'trg', 'se', 'quartg', 'bb', 'fyle', 'forlagrditaggrop'], 'king': []}
def rows(doc):
    src = os.path.join(D, 'transcription_%s.txt' % doc)
    toks = []
    for l in open(src, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        for t in tokens(l):
            if t == '|' or t.startswith('#'): continue
            doubt = '|' in t; n = int(t.split('|')[0]); v = K.get(n)
            r = '?' if n > 64 or v in (None, '?') or doubt else '-' if v == '(null)' else v
            toks.append([t, r])
    # letters in order, with their token index (nulls and codes skipped)
    idx = [i for i, (t, r) in enumerate(toks) if r not in ('-', '?')]
    s = ''.join(toks[i][1] for i in idx)
    for w in UNREAD[doc]:
        # an unread stretch is the letters after an open number or a code, or a whole word; mark every occurrence
        # that lies next to a '?' token or stands alone between nulls
        for m in re.finditer(w, s):
            a, b = idx[m.start()], idx[m.end() - 1]
            near = any(toks[j][1] == '?' for j in (a - 1, b + 1) if 0 <= j < len(toks)) or \
                all(0 <= j < len(toks) and toks[j][1] == '-' for j in (a - 1, b + 1))
            if near or w in ('fyle', 'forlagrditaggrop', 'quartg'):
                for j in range(a, b + 1):
                    if toks[j][1] != '-': toks[j][1] = '?'
    # giern{[11]c/e}: 11 (open) and 35 (= c) stand for one letter e; both left out
    if doc == 'chancellor':
        for j in range(len(toks) - 1):
            if toks[j][0] == '11' and toks[j + 1][0] == '35': toks[j + 1][1] = '?'
        # haf{o/u}e: 24 frozen o, read u
        for j in range(len(toks) - 2):
            if [t for t, _ in toks[j:j + 3]] == ['32', '24', '33']: toks[j + 1][1] = 'u'
    return toks
if __name__ == '__main__':
    out = ['# model: da-modern', '# source: transcription_king.txt, transcription_chancellor.txt, key_frozen.tsv, '
           'reading_king.md, reading_chancellor.md',
           '# note: 8-64 table only (p. 5); holes, guesses, codes, open numbers and doubtful groups are ?, nulls are -']
    for doc in ('king', 'chancellor'):
        for t, r in rows(doc): out.append('%s\t%s' % (t.split('|')[0], r))
    open(os.path.join(D, 'validation.tsv'), 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
    print(len(out) - 3, 'tokens;', sum(1 for l in out[3:] if l.split('\t')[1] not in ('?', '-')), 'read')
