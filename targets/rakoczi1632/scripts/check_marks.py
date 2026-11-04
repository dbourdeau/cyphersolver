#!/usr/bin/env python3
"""Rebuild the decryption of one page from its transcription, word table and key.tsv; check every mark; count words.
    python scripts/check_marks.py f491r        writes decryption_<doc>.txt (in the target folder), prints counts, exit 1 on any failure
Rules (each a failure):
  - the cipher words of transcription_<doc>.txt, in order, must be exactly those of words_<doc>.tsv;
  - a plain reading must be produced by the frozen key (letters; groups with two values may take either);
  - <word> (cipher departs from key, reading from the contemporary gloss) needs a gloss equal to the word (or its
    abbreviation) AND a key decode that does NOT give the word;
  - [?word] needs a real doubt: no gloss, a key value of status 'context', a decode that differs, or a sign doubt in the note;
  - a group not in the key may only stand in a marked word.
Counts: clear words ([?..] = not read), cipher words (plain and <..> read; [?..], [...] not read), total. Standard library only."""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parent.parent
doc = sys.argv[1]; D = ROOT if (ROOT / f'words_{doc}.tsv').exists() else ROOT / doc

def rows(p):
    for l in p.read_text(encoding='utf8').splitlines():
        if l and not l.startswith('#') and not l.startswith(('seq\t', 'group\t')):
            yield l.split('\t')

def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s.lower().replace('v', 'u').replace('j', 'i')).replace('qu', 'q')

key = {}
for f in rows(ROOT / 'key.tsv'):
    key[f[0]] = (f[1], f[2])
words = list(rows(D / f'words_{doc}.tsv'))
TOK = re.compile(r'^(\{[A-Za-z]+\}|\d+)(\.(\{[A-Za-z]+\}|\d+))*\.?$')
found = []
for l in (D / f'transcription_{doc}.txt').read_text(encoding='utf8').splitlines():
    m = re.match(r'^(\d\d) ?(.*)$', l)
    if not m: continue
    for t in m.group(2).split():
        t2 = t.replace('|', '.').rstrip('.')
        if TOK.match(t2) and re.search(r'\d|\{', t2):
            found.append(t2)
clear = []
for l in (D / f'transcription_{doc}.txt').read_text(encoding='utf8').splitlines():
    m = re.match(r'^(\d\d) ?(.*)$', l)
    if not m: continue
    for t in m.group(2).split():
        t2 = t.replace('|', '.').rstrip('.')
        if not (TOK.match(t2) and re.search(r'\d|\{', t2)) and re.search(r'[A-Za-z]', t):
            clear.append(t)
fail = []
exp = [w[2] for w in words]
if found != exp:
    i = next((i for i, (a, b) in enumerate(zip(found, exp)) if a != b), min(len(found), len(exp)))
    fail.append(f'cipher words: transcription {len(found)} vs table {len(exp)}; first difference at {i}: '
                f'{found[i] if i < len(found) else None} / {exp[i] if i < len(exp) else None}')

def decodes(c):
    """set of possible plaintexts (normalised) and flags"""
    if c in key and key[c][1] != 'context' and len(key[c][0]) > 2:
        return {norm(key[c][0])}, False, False
    outs = ['']; ctx = False; miss = False
    for g in c.split('.'):
        if g not in key: miss = True; outs = [o + '?' for o in outs]; continue
        v, st = key[g]; ctx |= st == 'context'
        vals = v.split('/')
        outs = [o + x for o in outs for x in vals]
    return {norm(o) if '?' not in o else o for o in outs}, ctx, miss

out = []; rd_c = 0; listed = []
for w in words:
    seq, line, c, p1, gloss, r, note = (w + [''] * 7)[:7]
    dec, ctx, miss = decodes(c)
    shown = '/'.join(sorted(dec))
    if r.startswith('[?'):
        word = r[2:-1]
        if not (gloss.strip() in ('-', '') or ctx or miss or norm(word) not in dec or 'doubt' in note or 'sign' in note):
            fail.append(f'{seq}: mark [?{word}] without a doubt under it')
    elif r == '[...]':
        pass
    elif r.startswith('<'):
        word = r[1:-1]; g = norm(gloss)
        if not g or not (norm(word).startswith(g.rstrip('.')) or g.startswith(norm(word))):
            fail.append(f'{seq}: <{word}> but gloss "{gloss}" differs')
        if norm(word) in dec:
            fail.append(f'{seq}: <{word}> marked as departure but the key gives it')
        rd_c += 1; listed.append(f'{seq} {c} key:{shown} gloss:{gloss}')
    else:
        if miss or ctx:
            fail.append(f'{seq}: {c} has groups missing from the key or from context only; reading unmarked')
        elif norm(r) not in dec:
            fail.append(f'{seq}: reading "{r}" not given by the key ({shown})')
        rd_c += 1
    out.append(f'{line:>2}  {c:<52} key: {shown:<22} gloss: {gloss:<18} reading: {r}')
(D / f'decryption_{doc}.txt').write_text('# rebuilt by scripts/check_marks.py from transcription, words table and key.tsv\n'
                                       + '\n'.join(out) + '\n', encoding='utf8')
cl_unread = sum(1 for t in clear if t.startswith('[?') or t == '[...]')
nc, nw = len(clear), len(words)
tot = nc + nw; rd = nc - cl_unread + rd_c
print(f'clear words {nc}, not read {cl_unread}; cipher words {nw}, read {rd_c} (of which {len(listed)} read from the gloss over a cipher departure)')
print(f'all words {tot}, read {rd} = {100*rd/tot:.1f}%')
strict = rd - len(listed)
print(f'strict count (departures counted as not read): {strict} = {100*strict/tot:.1f}%')
for x in listed: print('  departure', x)
for f in fail: print('FAIL', f)
print('result:', 'FAIL' if fail else 'ok'); sys.exit(1 if fail else 0)
