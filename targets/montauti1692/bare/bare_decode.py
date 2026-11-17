"""bare_decode.py -- decode the round-4 bare System B transcriptions with frozen key v2 (unchanged).
Notation in the transcription: groups separated by spaces; w = the w-shaped sign;
'a+b' = two groups written with one shared sign (e.g. 5w+w4 written '5w4');
'?xy' = group read with doubt; '##' = illegible group. Unknown groups print as [xy]."""
import json, hashlib, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kp = os.path.join(os.path.dirname(R), 'systemB', 'key_v2.json')
raw = open(kp, 'rb').read(); assert hashlib.sha256(raw).hexdigest().startswith('64783ab8')
KEY = {k: v for k, v in json.loads(raw).items() if not k.startswith('_')}
KEY['91'] = 'u'  # 'also seen once: 91 = u' (given in the brief, not in the file)

P = [  # passage, folio, line, clear before, groups, clear after
('P1','534 f.114r',1,'riguardo i Negoziati','w2 44 ww 6w 21',''),
('P1','534 f.114r',2,'','66 6w+w2 ?11 44 41 64 6w w4 46 21 55 w2 42 11 6w 21 50 64 31 56 w2 5w ## ## ## 40','e precisare'),
('P1','534 f.114r',3,'il disegno che vi suppone avere il','110 46 31 66 11 51 41 31 w2',''),
('P1','534 f.114r',4,'','46 w6 ?w2 44 w2 66 11 64 21 44 41 55 ?15 55 55 11 ?10 w6 66 51 w2 4w 31 50 55 w6 w2','e quanto andava promovendo il pred.o Ministro'),
('P1','534 f.114r',5,'Ministro','66 31 5w 41 64 46 31 5w 21 11 55 w2 60',''),
('P1','534 f.114r',6,'','11 44 21 44 41 56 21 11 55','la sollecitazione degli intenzionati soccorsi'),
('P1','534 f.114r',7,'a cui miravano le','31 5w 44 51 56 42 21 5w 76 w4 46 21 55 11 42 w2 6w 21','sud.o'),
('P1','534 f.114r',8,'Servono di','64 41 50 w2 44 52 w4 60 21 64 60 ?11 64 6w 21 46 w4 13','sia stato fatto insinuare al'),
('P1','534 f.114r',9,'insinuare al','22 44 52 21','non venisse approvato da'),
('P1','534 f.114r',10,'approvato da','106 31 55 56 11 6w 64 31 56 41 5w 31 ww','di med.o'),
('P1','534 f.114r',11,'di med.o','110 44 41 5w 55 w2 21 ?0w 46 31 60 41 55 ww ww 5w 31 w2','ed è similmente non piaciuta a'),
('P1','534 f.114r',12,'non piaciuta a','106 44 52 21','concorresse al'),
('P1','534 f.114r',13,'concorresse al','91 w4 ?66 44 41 51 w2 ?6w ww 46 31 55 31 21 50 w4 55 21 55 w4 6w 41 64 46 31 44 41 55 ww 5w 31 w2','e che pure è vero che siano corse tali ambasciate, vedendosi che non ostante il'),
('P1','534 f.114r',14,'non ostante il','22 52 11 66 6w w2 44 ?w2 31 55 w6 66 6w 21 55 w4 66 ?31 ?22 5w 41 76 21','per quanto si dice'),
('P1','534 f.114r',15,'si dice','44 ww 5w 55 11 46 21 6w w2 21 ?0w','e che non desiste di proseguire le sue pratiche'),
('P1','534 f.114r',16,'sue pratiche','31 5w 55 w6 21 50 w4 55 21 55 w4 6w 41 64 46 31 44 ww 55 41 5w 31 w2','può dubitarsi che'),
('P1','534 f.114r-v',17,'può dubitarsi che','4w 64 11 55 w2 51 50 91 66 6w 31 66 w6 56 21 44 11 44 w2 66 21 ?11 21 55 w4 55 21 6w 41 64 11 55 21 46 31 42 11 91 31 w4 64 11','nascano delle amarezze'),
('P2','534 f.115r',1,'le notizie della','21 66 31 42 w6 76 31 ww 5w+w4','che si supponeva fatta'),
('P2','534 f.115r',2,'fatta','w2 44 41 6w 21 66 6w+w2 44+41 64 6w 21 46 11 55 110 46 w6+66 w2 91 41 31 11','della sua di Lei'),
('P2','534 f.115r',3,'di Lei','4w 31 50 55 w6 w2','per il'),
('P2','534 f.115r',4,'per il','64 21 46 w4 64 41 56 11 5w+w6','onde mi nasce motivo di ringraziarne'),
('P2','534 f.115r',5,'costà progettarsi','90 46 11 55 11 42 w2 6w+w4 50 64 w6 56 11 5w 31','durante la'),
('P2','534 f.115r',6,'durante la','46 w6 55+51 31 60 21 64 56 11 5w+w4 5w 76 11 31 5w','coteste'),
('P2','534 f.115r',7,'coteste','60 11 64 6w 31 46 41 51 21','se bene le'),
('P2','534 f.115r',8,'se bene le','w0 46 31 55 51 w6','negoziazioni passavano molto'),
('P2','534 f.115r',9,'passavano molto','30 40 66 21 50 64 w4 6w 21 44 ww 55 104','non sono però a lungo andare'),
('P2','534 f.115r',10,'a lungo andare','31 56+60 21 5w+w4 6w 64 11 42 31 55 w6','le cose per la naturale'),
('P2','534 f.115r',11,'per la naturale','11 60 21 64 6w 51 64 11','e poca'),
('P2','534 f.115r',12,'e poca','44 31 64 44+41 66+60 21 76 ?6w ww 5w+w4 6 21 39','In conto dell\'Amb.re di Venezia'),
('P3','534 f.116r',1,'perché il Sig.r','27 66 31 ww 60 41 5w 50 11 60 64 41 50 21 6w 31 46 w6 116 44 ww 5w 6w 11 5w 6w w2 4w ?ww 64 76 11 56 21 5w 6w 64 21','sono manifesti gli utili, che'),
('P3','534 f.116r',2,'utili, che','11 6w 51 6w 31','deriverebbero dallo stabilimento di'),
('P3','534 f.116v',3,'stabilimento di','51 5w 66 31 50 64 11 5w 42 w4 5w+w4','Del resto mi saranno molto care'),
('P4','531 f.4r',1,"de' negoziati de",'55 10 44+41 55 11 42 w2 6w 21 50 64 31 56 w2 5w 31','potendo importar molto'),
]
def groups(s):
    out = []
    for t in s.split():
        for g in t.split('+'):
            out.append(g)
    return out
def dec(g):
    q = g.lstrip('?')
    if q == '##': return '#'
    return KEY.get(q, '[%s]' % q)
if __name__ == '__main__':
    tot = {}
    with open(os.path.join(R, 'bare_transcriptions.tsv'), 'w') as f:
        f.write('passage\tfolio\tline\tclear_before\tgroups_as_written\tdecoded_key_v2\tclear_after\n')
        for p, fo, ln, cb, gs, ca in P:
            d = ''.join(dec(g) for g in groups(gs))
            f.write('\t'.join([p, fo, str(ln), cb, gs, d, ca]) + '\n')
            n = len(groups(gs)); k = sum(1 for g in groups(gs) if not dec(g).startswith('[') and dec(g) != '#')
            t = tot.setdefault(p, [0, 0, set()]); t[0] += n; t[1] += k
            t[2].update(g.lstrip('?') for g in groups(gs) if dec(g).startswith('['))
            print(p, fo, ln, d)
    for p, (n, k, u) in tot.items(): print(p, 'groups', n, 'decoded', k, '%.0f%%' % (100*k/n), 'unknown', sorted(u))
    a = sum(v[0] for v in tot.values()); b = sum(v[1] for v in tot.values()); print('ALL', a, b, '%.1f%%' % (100*b/a))
