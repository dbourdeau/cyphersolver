# V1921 (ASMo Ungheria b. 4, Caprili 1520-21 no. 12, Esztergom 25 Feb 1521): reading of the cipher runs.
# Signs re-checked on img/v/v1921_2.jpg, 2 Oct 2026. Each token is "SIGN=value"; value '' = null, '?' = unread.
# Values are key21.json except where marked (* = value from the key21_counts minority or a new ligature, forced here
# by context and confirmed elsewhere). Run: python read_v1921.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

RUNS = [
 ('L01', 'e scarico di chi ne ha colpa.', None,
  "8=e z=m ss=e PSI=d B=i PHI=c L=i Z=x 8=e | o=h* T=a | LAM=u DIV=n | oSLo=o HH=m CE=o | z+=q* o=u* RC=i",
  'qual oltra che fa mille pacie & da poca riputation ale cose del patron'),
 ('L02', None, None,
  "r=d B=i TH=c y=e | QB=o w=g p=n L=i | PHI=c CE=o MT=s q=a | y'=e | y=e x=r a=u ss=e n=l f=t UT=a",
  'e ha ditto haver scritto al suo mazo che'),
 ('L02-03', None, None,
  "L=i ff=l | PHI=c LAM=u NT=s h=t CE=o r=d y=e | ss=e | MT=s f=t q=a h=t QB=o | x+=q* a=u y=e ff=l | "
  "TH=c o=h* T=a | EL=p ss=e x=r NT=s LAM=u T=a MT=s oSLo=o | 1=? 1=?",
  'a dire che'),
 ('L03-04', None, None,
  "QB=? | T=a w=g AST=r B=i q=a | ss=e x=r q=a | PSI=d UT=a h=t T=a | r=d q=a DIV=n h=t B=i | L=i ff=l | "
  "NT=s o=u* QB=o | UT=a PSI=d a=u y=e DIV=n h=t oSLo=o | K=e* PHI=c o=h* ss=e | n=l e=o | f=t QB=o U=g ff=l B=i q=a | "
  "RC=i p=n | oSLo=o EL=f* L=i TH=c B=i CE=o",
  'e molto sturbato le sue cose, e chi l\'ha messo in gran disgratia di'),
 ('L05', None, None,
  "NT=s LAM=u oSLo=o | MT=s B=i w=g p=n CE=o x=r y=e",
  'il che quando cossi sia como mi acerta alcuno ch\'à veduto le lettere a V. Ex.a sera poca fatica i cominciar a repeter il suo'),
 ('L06', None, None,
  "MT=s CE=o AMP=p AST=r q=a | NT=s QB=o B=i | oo=b* y=e DIV=n L=i | z+=q* LAM=u T=a p=n h=t o=u* DIV=n x=q* p= LAM=u y=e | "
  "MT=s B=i q=a p=n CE=o | B=i DIV=n | AST=r y=e w=g K=? PHI=?",
  'e S. V. Ex.a a questo modo ...'),
]

READING = [
 ('L01', "e me dicixe [= disse?] ha un omo qui", 'M (dicixe) / C'),
 ('L02', "dice ogni cosa e revelta", 'C (dice ogni cosa) / M (revelta)'),
 ('L02-03', "il custode è stato quel ch'à persuaso [..]", 'C'),
 ('L03-04', "[.] Agria era data d'anti il suo advento, e[t] che lo toglia in oficio", 'C / M (K = et)'),
 ('L05', "suo signore", 'C'),
 ('L06', "sopra soi beni, quantunque siano in reg[..]", 'C (quantunque: x p = q, as in R1136 L10 questo)'),
]

def tokens(s):
    for g in s.replace('|', ' ').split():
        sign, val = g.split('=')
        yield sign, val.rstrip('*')

def main():
    from lang import lm
    tot = sense = unread = 0
    plain = []
    for lab, _, _, toks, _ in RUNS:
        t = list(tokens(toks))
        tot += len(t)
        u = sum(1 for _, v in t if v == '?')
        unread += u
        plain.append(''.join(v for _, v in t if v != '?'))
        print(lab, ''.join(v if v != '?' else '.' for _, v in t))
    # signs that are unread: 1 1 (L03), QB before Agria, K PHI at the page edge; the p after x in quantunque is part of the xp ligature (= q)
    sense = tot - unread
    print(f'tokens {tot}, read as sense {sense} ({100*sense/tot:.1f} %), unread {unread}')
    txt = ' '.join(r for _, r, _ in READING)
    m = lm.load('it-cinquecento')
    print('it-cinquecento per_char', round(m.per_char(lm.norm(txt, 'early')), 2))
    import random
    random.seed(1)
    ctl = []
    for i in range(20):
        letters = [c for c in txt if c != ' ']
        random.shuffle(letters)
        it = iter(letters)
        ctl.append(m.per_char(lm.norm(''.join(c if c == ' ' else next(it) for c in txt), 'early')))
    print('control (letters shuffled, word breaks kept, 20 runs) mean per_char', round(sum(ctl) / len(ctl), 2))
    # grade-C share: 'dicixe' (6 signs) and 'e revelta' (8 signs) are grade M
    print(f'grade C only: {sense - 14} of {tot} ({100*(sense-14)/tot:.1f} %)')
    print('it-modern per_char', round(lm.load('it-modern').per_char(lm.norm(txt, 'modern')), 2),
          '| fr-1600-letters', round(lm.load('fr-1600-letters').per_char(lm.norm(txt, 'early')), 2),
          '| best_language', [r for r in lm.best_language(lm.norm(txt, 'early'))[:3]])

if __name__ == '__main__':
    main()
