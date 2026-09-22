"""Apply corrections by whole-word match: (line id, old token run, new token run)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FIX = [
 ('P1.21','20 54 48 32 16 12 18 40 10 72 40','20 54 48 32 10 12 18 40 16 72 40'),  # furhabenden
 ('P2.11','54 18 48 16 40 10 18 48 40','54 18 48 10 40 16 18 48 40'),              # verandern
 ('P2.21','42 48 10 40 54 40 30','42 48 16 40 54 40 30'),                          # ordnung
 ('P2.21','44 10 48 42 34 14 68 36 10 48','44 10 48 52 34 14 68 36 10 48'),        # particular
 ('P1.08','30 48 10 20 50 14 32 60 20 42','30 48 10 20 50 14 32 60 20 52'),        # grafschaft
 ('P1.26','30 48 10 20 40 14 32 60 20 52','30 48 10 20 50 14 32 60 20 52'),        # grafschaft
 ('P2.25','20 42 48 52 58 58 30','20 42 48 52 58 54 30'),                          # fortzug
 ('P3.08','18 34 40 30 42 30 64 48 58 40 30','18 34 40 36 42 30 64 48 54 40 30'),  # einlogirung
 ('P3.14','58 08 18 34','58 78 18 34'),                                            # zwei
 ('P3.14','74 66 44 50 52 54 14 74 32','74 66 44 20 50 52 54 14 74 32'),           # kopfstuckh
 ('P4.31','16 18 50 78 30 62 40','16 18 50 78 18 30 62 40'),                       # deswegen
 ('P6.04','54 66 36 14 74 32','54 66 36 14 74 52'),                                # volckht? -> volckh
 ('P6.06','58 54 30 64 18 14 52','58 54 30 36 18 34 14 32'),                       # zugleich
 ('P6.09','50 64 64 40 62 40','50 62 64 40 62 40'),                                # seinen
 ('P8.02','58 54 10 48','58 78 10 48'),                                            # zwar
 ('P8.06','58 08 62 50 10 52 58','58 68 62 50 10 52 58'),                          # zuesatz
 ('P8.25','72 54 50 18 48 34 50 54','72 54 50 18 48 34 50 52'),                    # eusserist
 ('P8.26','52 10 30 34 14 32 50','52 10 30 36 34 14 32 50'),                       # taglichs
 ('P9.01','78 18 48 12 58 40 30 18 40','78 18 48 12 54 40 30 18 40'),              # werbungen
 ('P9.14','14 10 54 42 36 34 50 14 32 18 40','14 10 52 42 36 34 50 14 32 18 40'),  # catolischen
 ('P1.10','58 54 40 14 14 42 38 38 60 10 34 18 48 40','58 54 60 14 14 42 38 38 42 16 34 18 48 40'),  # zuaccommodiern
 ('P9.05','30 48 60 76 52','30 48 60 20 52'),                                      # graft/graf
 ('P9.12','20 42 48 54','20 42 48 52'),                                            # fort
 ('P5.20','18 48 38 62 36 52 72 52 40 38 18 34 40 18 40','18 48 38 62 36 52 72 40 38 18 34 40 18 40'),  # ermelten meinen
 ('P8.03','10 18 44 48 34 38 64 48 52','50 54 44 44 48 34 38 64 48 52'),           # supprimirt
]
path = os.path.join(HERE, 'transcription.txt')
txt = open(path, encoding='utf8').read().split('\n')
by = {ln.split(' ', 1)[0]: i for i, ln in enumerate(txt) if ln[:1] == 'P'}
n = 0
for lid, old, new in FIX:
    i = by.get(lid)
    if i is None: print('no line', lid); continue
    if old not in txt[i]: print('no match', lid, old); continue
    txt[i] = txt[i].replace(old, new, 1); n += 1
open(path, 'w', encoding='utf8').write('\n'.join(txt))
print(n, 'of', len(FIX), 'applied')
