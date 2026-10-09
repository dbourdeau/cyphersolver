import re,sys
T="""A27 A114 A161 affaires389 ance473 app186 ar540 as487 au67 B246 bi541 bien453 bo160 bre377 C204 C388 ca293 ce43 ces183 cha200 che50 cho115 ci452 co140 con249 connois306 cu230
D552 dans526 de56 de221 des126 des149 dif318 dispose321 dra439 du66 dui486 E4 E304 est35 ec451 el344 en116 encores51 ent391 er89 ers250 es424 esse264 et489 et563 eur197 ev408 ex267
F144 fa12 fait516 fe415 fi132 fo308 ger356 gouverne243 grande2 he201 honneur365 I49 J49 I297 J297 il410 im317 ir22 L101 L554 la224 le40 les118 li446 lo288 lon437 lu343 M353
main476 mais252 mande269 me3 me414 ment86 ment382 mi459 moins124 N347 N495 N549 na92 ne558 O52 O203 oit258 on1 P123 pa85 paix532 pas315 pe564 pendant513 peut501 pli272 plus521
po538 pour508 pouvoir290 pr357 pr535 pre411 que32 qui461 quil467 quon209 R78 ra122 raison480 re83 ren362 ri394 roit531 S25 S111 S231 S477 sa493 sans506 se64 si512 so313 soit448
solu57 su153 sure69 T33 T166 T170 ta113 table247 te29 te212 temps463 ten174 ter402 ti429 tion62 toute256 traite120 tre206 U119 V119 U262 V262 un350 ur373 ut324 ve8 ven334 ver136 veu219 vi261
vo479 voie128 voir276 vous385 vous505 vu151 X568 Y61 Y560 Z301"""
K={}
for w in T.split():
    m=re.match(r'([A-Za-z]+)(\d+)$',w); K.setdefault(int(m[2]),m[1].lower())
toks=[];
for l in open(__import__('os').path.join(__import__('os').path.dirname(__file__),'transcription.txt'),encoding='utf-8'):
    if l[:3] in('C |','U |'):
        toks+= [int(x) for x in l[3:].split() if x.isdigit()]
print(len(toks),'groups; missing from table:',sorted(set(t for t in toks if t not in K)))
print(sum(t in K for t in toks)/len(toks))
s=''.join(K.get(t,'[%d]'%t) for t in toks)
print(s)
if len(sys.argv)>1:
    miss={t for t in toks if t not in K}
    for i,t in enumerate(toks):
        if t in miss:
            print(t,'|',' '.join(K.get(x,'[%d]'%x) for x in toks[max(0,i-5):i]),'<<',t,'>>',' '.join(K.get(x,'[%d]'%x) for x in toks[i+1:i+6]))
