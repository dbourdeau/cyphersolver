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
def tsv_b(srcs, dst):
    """sysB/R93xx_pN.tsv: line_no, cipher_words (signs '.'-joined, words by space), gloss_words."""
    out = []
    for src in srcs:
        for l in io.open(src, encoding='utf8'):
            c = l.rstrip('\n').split('\t')
            if len(c) < 2 or not c[0].strip().isdigit(): continue
            s = re.sub(r'\[(?!ins:)[^\]]*\]', '', c[1])
            s = re.sub(r'\[ins:([^\]]*)\]', r'\1', s)
            out.append(' '.join(t.rstrip('?') for w in s.split() for t in w.split('.') if t.rstrip('?') and t != "''"))
    io.open(dst, 'w', encoding='utf8').write('\n'.join(out) + '\n')
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tsv('r9403/transcription.tsv', 'r9403/signs.txt')
tsv_b(['sysB/R9322_p1.tsv', 'sysB/R9322_p2.tsv'], 'sysB/R9322_signs.txt')
tsv_b(['sysB/R9323_p1.tsv'], 'sysB/R9323_signs.txt')
tsv_b(['sysB/R9417_p1.tsv', 'sysB/R9417_p2.tsv'], 'sysB/R9417_signs.txt')
