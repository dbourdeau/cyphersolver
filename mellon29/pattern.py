import itertools
Z={'Ariete':'srconpggy','Taurus':'lrqrlrpnqsr7g','Gemini':'qrqrsipqsop3g','Cancer':'irqpshkscel','Leo':'rqlpsonspyhB',
'Virgo':'pqyqpqsqst','Libra':'9qsgqxqkb3','Scorpio':'prksyqs7qp','Sagit':'xinak7sqol','Capri':'7nqqpypt7r','Aquario':'qksqrongya','Pissis':'7tbyhqphyv'}
names='''sale armoniaco|sal armoniaco|salarmoniaco|argento vivo|argentovivo|mercurio|solfere|solfo|zolfo|solfore|arsenico|arsenicho|orpimento|oropimento|salnitro|sal nitro|sal gemma|sale gemma|sale commune|sal comune|sal alkali|sale alkali|sale alcali|alume de rocha|alume de roccha|alume|allume|alume zucharino|alume scagliola|alume de piuma|vetriolo|vitriolo|vitriolo romano|borace|borax|tutia|tuzia|marchasita|marcasita|magnesia|antimonio|verderame|verde rame|cinabrio|cinabro|litargirio|calcina|calcina viva|sale tartaro|tartaro|gripola|grippola|gomma|dragante|draganti|sale alembrot|sale de vetro|sal de vetro|fiel de vetro|lume de feccia|sapone|minio|biacca|cerusa|ceruse|piombo|stagno|rame|ferro|oro|argento|acqua forte|aqua forte|acqua vita|aceto|aceto forte|urina|sangue|sale|sal|tinchar|tincar|atincar|cristallo|calamina|pietra calaminare|squama de ferro|croco de ferro|crocus martis|feccia de vino|sal de orina|sale de urina|lume|allume de rocha|sale ammoniaco|salammoniaco|sale armeniaco|aqua de vita|olio de tartaro|oglio de tartaro|oglio de vitriolo|tartaro de vino|vitriolo cipro|sublimato|solimato|argento sublimato|mercurio sublimato|zinabrio|realgar|risigallo|risagallo|arsenico cristallino|arsenico bianco|arsenico citrino'''.split('|')
def pat(s):
    d={};return tuple(d.setdefault(c,len(d)) for c in s)
for k,c in Z.items():
    hits=[n for n in names if len(n.replace(' ',''))==len(c) and pat(n.replace(' ',''))==pat(c)]
    near=[n for n in names if len(n.replace(' ',''))==len(c)]
    print(k,c,'MATCH:',hits,'| samelen:',len(near))
