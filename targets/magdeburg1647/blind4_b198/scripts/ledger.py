import sys
sys.path.insert(0,'/home/claude/en/trackB/b198_magdeburg_blind/scripts')
from decode import words,dec
B='/home/claude/en/trackB/b198_magdeburg_blind/'
# Judgements made once on the first decode. S = German/Latin word as it stands (listed spellings u/v, i/j, dt, th; names; run-together words).
# SP = counted S only by a common 17th-c. spelling outside the four listed (ey, tz, single for double consonant in wolte/solte, no umlaut, aw). Everything else E.
S={'f102':"ihre nachmals mit wesenbecio wegen gebraucht grosglogaw nebst confirmation wie bremen minden selbst undt cum spiritu uertiginis oder uel explorandi causa".split(),
   'f104':"einer legatis auf uier streitigen zu seiner ein haben auch inhohem berichtet erheut uoneinem ihnen unter uerbleiben weilaber selbst mir alsauch aus nach uermuthlich post repulsam pro sua also bissich eine aneinem in".split(),
   'f204':"auch tagen mich inhohem et pro certo berichten selbst sich consilia lieber undt undtauch zur hingeben nur noch bleiben aber".split()}
SP={'f102':"deputirte bey zuschertzen wolte umb groszuthun were wansie newer cantzlar getriben".split(),
    'f104':"sieihme seltzame beywelcher erihme uertrawen furgeschlagen were solte sowol alsscheinet etwan fugliche munsterischen burger ereugnete".split(),
    'f204':"uertrawen lasen ertz solte".split()}
SYM={}
tot={}
for f in ('f102','f104','f204'):
    ws=words(B+'tx/%s.txt'%f)
    nsym=sum(line.count('{S:') for line in open(B+'tx/%s.txt'%f,encoding='utf-8') if not line.startswith('#'))
    s=sp=e=0
    with open(B+'dec/%s.ledger.tsv'%f,'w') as o:
        o.write('line\tcipher_as_frozen\tdecoded\tjudgement\n')
        for ln,tok,c in ws:
            p=dec(c)
            j='S' if p in S[f] else 'SP' if p in SP[f] else 'E'
            s+=j=='S'; sp+=j=='SP'; e+=j=='E'
            o.write('%s\t%s\t%s\t%s\n'%(ln,tok,p,j))
        n=len(ws)
        o.write('# words=%d S=%d SP=%d E=%d N=0\n'%(n,s,sp,e))
        o.write('# strict figure of record (S+SP)/(S+SP+E+N) = %d/%d = %.2f%%\n'%(s+sp,n,100*(s+sp)/n))
        o.write('# hard figure (listed spellings only) S/(S+SP+E+N) = %d/%d = %.2f%%\n'%(s,n,100*s/n))
        o.write('# supplementary, symbols as N: %d/(%d+%d) = %d/%d = %.2f%%\n'%(s+sp,n,nsym,s+sp,n+nsym,100*(s+sp)/(n+nsym)))
    print(open(B+'dec/%s.ledger.tsv'%f).read().split('# words')[1].join(['# words','']) if False else '')
    print(f, ''.join(l for l in open(B+'dec/%s.ledger.tsv'%f) if l.startswith('#')))
    miss=[x for x in S[f]+SP[f] if x not in [dec(c) for _,_,c in ws]]
    print('unmatched judgement keys:',miss)
