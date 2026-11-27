"""Pass 5, T2 (python3 -I): apply the looped-sign re-look (DL_CHECK_P5.tsv rows marked 'changed') to copies of the
pass-4 transcriptions. Each change names text, line, the old word and the new word; the script asserts the old word is
there exactly once on that line. The checks were done with AI tools and no person checked each record by hand."""
import sys
P4, OUT = sys.argv[1].rstrip('/') + '/', sys.argv[2].rstrip('/') + '/'
CH = {
 'f004r.txt': [('L15', 'Hk X 6_ Ds D1 Dl@', 'Hk X 6_ Ds D1 X@'),
               ('L17', 'Ds^ Pe Bx Tk X Dl@', 'Ds^ Pe Bx Tk X@'),
               ('L18', 'Oe^m Cs Dl@', 'Oe^m Cs X@')],
 'f004v.txt': [('L08', 'Oc Lm 1 Dl 6r X Dl@', 'Oc Lm 1 Dl 6r X@'),
               ('L09', '2 6 X Dl@', '2 6 X@'),
               ('L10', 'Lm 7 X 6_ Dl@', 'Lm 7 X 6_ X@'),
               ('L10', ' 6 X Dl@ ', ' 6 X@ '),
               ('L13', '6r X Dl@', '6r X@'),
               ('L16', '9 Dl 6r X Dl@', '9 Dl 6r X@')],
 'f159r.txt': [('L02', '6s Cd Dl@', '6s Cd X@'),
               ('L02', '4 Dl D1 6r Dl@', '4 Dl D1 6r X@'),
               ('L03', '8 6 Dl" Dl 7 X Dl@', '8 6 Dl" Dl 7 X@'),
               ('L06', '6s Lm_ 1 8 6r 3 Bx Ds D2 7 X Dl@', '6s Lm_ 1 8 6r 3 Bx Ds D2 7 X@'),
               ('L10', 'X Bx Cs X Dl@', 'X Bx Cs X@')],
 'f034r_p34.txt': [('P4', 'Lm Tk^ Dl@', 'Lm Tk^ X@')],
}
n = 0
for f, rows in CH.items():
    L = open(P4 + f, encoding='utf-8').read().split('\n')
    L.insert(0, '# PASS 5 (27 Nov 2026): pass-4 file with the looped-sign words re-looked on the image (DL_CHECK_P5.tsv); %d words changed from Dl@ (us) to X@ (is); nothing else changed. The checks were done with AI tools and no person checked each record by hand.' % len(rows))
    for lid, old, new in rows:
        idx = [i for i, l in enumerate(L) if l.startswith(lid + '\t')]
        assert len(idx) == 1, (f, lid)
        line = L[idx[0]] + ' '
        assert line.count(old) == 1, (f, lid, old, line.count(old))
        L[idx[0]] = line.replace(old, new).rstrip(' ')
        n += 1
    open(OUT + f, 'w', encoding='utf-8').write('\n'.join(L))
print('changed words', n)
