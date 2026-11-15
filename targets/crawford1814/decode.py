"""Decode crawford1814_transcription.txt with WE025 (key/we025_crawford1814.tsv, the rows of Weber's table used here).

    python decode.py                 write crawford1814_decryption.txt and validation.tsv
    python decode.py --print         print the decryption only

Each group is written number=element; the encoder's marks are applied as in ../poinsett1813/beling (' plural -s,
^ -ed, _r/_rr/_rrr drop one to three final letters, _y drop the final letter, + a doubled letter) to give the letters
the group contributes.
Groups whose reading in crawford1814_reading.md is a guess against or beyond the table are listed in GUESSED and go
to validation.tsv as '?' (unread). Python standard library only."""
import hashlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, 'key', 'we025_crawford1814.tsv')
KEY_SHA = open(os.path.join(HERE, 'key', 'SHA256.txt'), encoding='utf-8').read().split()[0]
assert hashlib.sha256(open(KEY, 'rb').read()).hexdigest() == KEY_SHA, 'key file changed'
T = {}
for i, l in enumerate(open(KEY, encoding='utf-8')):
    if i:
        n, el, _ = l.rstrip('\n').split('\t')
        T[n] = el
# (line, group) -> letters, where the mark rule does not give the word used in the reading
SPECIAL = {('65R06', '720'): 'lost', ('66L06', '121'): 'parties', ('66L13', '121'): 'parties',
           ('65R11', '456'): 'them', ('65R05', '372'): 'ggle', ('65R07', '372'): 'ggle', ('66L01', '1115'): 'all',
           ('64R07', '1116'): 'oops'}
GUESSED = {('64R12', '1276'), ('65R02', '812'), ('66L12', '361'),
           ('64R14', '1512'), ('65R02', '1512'), ('65R07', '1512'), ('66L09', '1512'), ('66L09', '556'),
           ('66L15', '1474')}

def contribution(line, num, marks):
    if (line, num) in GUESSED:
        return '?'
    if (line, num) in SPECIAL:
        return SPECIAL[(line, num)]
    el = T[num]
    m = re.search(r'_(r+|y)', marks)
    if m:
        el = el[:-len(m.group(1))]
    if "'" in marks:
        el += 's'
    if '^' in marks:
        el += 'd' if el.endswith('e') else 'ed'
    return el

dec, pairs = [], []
for line in open(os.path.join(HERE, 'crawford1814_transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or ':' not in line:
        continue
    lab, body = line.rstrip('\n').split(':', 1)
    body = re.sub(r'\[struck:[^\]]*\]', ' ', body)
    out = []
    for tok in re.findall(r'"[^"]*"|\d+[\'^+_ry?]*', body):
        if tok.startswith('"'):
            out.append(tok)
            continue
        num = re.match(r'\d+', tok).group()
        marks = tok[len(num):]
        c = contribution(lab, num, marks)
        out.append(f'{num}{marks}={T[num]}' + ('' if c in (T[num], '?') else f'>{c}') + ('/guess' if c == '?' else ''))
        pairs.append(f'{num}{marks.replace("?", "")}\t{c}')
    dec.append(f'{lab}  ' + '  '.join(out))
head = ('# Crawford to Monroe, Paris, 5 Nov 1814 (No. 33-2, Private): group-by-group decryption with WE025\n'
        '# (key/we025_crawford1814.tsv), line by line against crawford1814_transcription.txt. Output of: python decode.py\n'
        '# number=element as Weber prints it; >letters = what the encoder\'s mark makes of it; /guess = the reading supplies\n'
        '# a word against or beyond the table (see crawford1814_reading.md); "words" = written in clear.\n')
if '--print' in sys.argv:
    print(head + '\n'.join(dec))
else:
    open(os.path.join(HERE, 'crawford1814_decryption.txt'), 'w', encoding='utf-8').write(head + '\n'.join(dec) + '\n')
    open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf-8').write(
        '# model: en-modern\n# source: crawford1814_transcription.txt decoded by decode.py (key/we025_crawford1814.tsv)\n'
        '# note: guessed groups are ? (unread); marks applied as in decode.py\n' + '\n'.join(pairs) + '\n')
    print(len(pairs), 'groups;', sum(1 for p in pairs if p.endswith('\t?')), 'unread in validation.tsv')
