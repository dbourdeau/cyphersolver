"""Write one-sign-per-token streams (signs.txt) from the transcriptions, for python docs/_check_profile.py --measure.
Clear text [..], glosses (g:), headers and line numbers are dropped; '?' (blot) is kept as a sign."""
import re, io
def onechar(src, dst):
    out = []
    for l in io.open(src, encoding='utf8'):
        if l.startswith(('#', '==', 'g:')) or not l.strip(): continue
        s = re.sub(r'^\s*\d+\s', '', l.rstrip('\n'))
        s = re.sub(r'\[[^\]]*\]', '', s).replace('{-}', '')
        out.append(' '.join(ch for ch in s if not ch.isspace()))
    io.open(dst, 'w', encoding='utf8').write('\n'.join(out) + '\n')
def tsv(src, dst):
    out = []
    for l in io.open(src, encoding='utf8'):
        if l.startswith(('#', 'g:')): continue
        c = l.rstrip('\n').split('\t')
        if len(c) < 3: continue
        out.append(' '.join(t for w in c[2].split() for t in w.split('.') if t))
    io.open(dst, 'w', encoding='utf8').write('\n'.join(out) + '\n')
tsv('r9403/transcription.tsv', 'r9403/signs.txt')
onechar('r9415/transcription.txt', 'r9415/signs.txt')
onechar('r9414/transcription_v2.txt', 'r9414/signs.txt')
