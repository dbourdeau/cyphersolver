"""Table T (n° 2530 petkum-1665), apprise des gloses des feuillets A seulement :
img 338 L/R, 377 R, 401 L/R, 421 R, 429 L/R, 461 R (relations au roi et lettres à Biermann, déc. 1664 - juin 1665).
Aucun feuillet H (561, 553, 541, 638, 505, 501) n'a été regardé avant le gel de T.
Structure inférée de A : lettres 14-37 (ordre alphabétique a..z sans j/k/w ? ; ancrées : 14a 16c 17d 18e 19f 22i 24l 26n 28p 30r 31s 32t 33u 36y),
syllabes consonne+voyelle par blocs de 5 (a e i o u) placées alphabétiquement dans un répertoire 170-389 mêlé de mots,
mots (nomenclateur) 37-169 et 390+ ; signes = homophones de lettres.
Clés 'obs' = vues glosées dans A ; 'int' = interpolées dans un bloc dont au moins 2 valeurs sont vues."""
OBS = {}
INT = {}
# lettres
for k,v in {14:'a',16:'c',17:'d',18:'e',19:'f',22:'i',24:'l',26:'n',28:'p',30:'r',31:'s',32:'t',33:'u',36:'y'}.items(): OBS[str(k)]=v
for k,v in {15:'b',20:'g',21:'h',23:'j',25:'m',27:'o',29:'q',34:'v',35:'x'}.items(): INT[str(k)]=v
# signes (homophones)
for k,v in {'g':'p','9':'t','x':'l','beta':'r','lambda':'u','ll':'e','4':'n','m7':'s','6':'i','d':'g','ct':'a','theta':'m','y':'c','T':'y','#':'o','2':'t','f':'f'}.items(): OBS[k]=v
# blocs syllabiques : (consonne, premier numéro)
BLOCS = [('b',170),('c',182),('d',200),('f',217),('g',229),('h',241),('j',252),('l',266),('m',276),('n',298),('p',316),('r',339),('s',352),('t',364),('v',380)]
SEEN = {172,173,182,183,184,185,186,200,201,202,204,217,219,220,229,230,231,232,241,244,252,253,266,267,268,269,270,276,277,278,279,298,299,300,301,316,317,318,319,320,339,340,341,342,352,353,354,355,356,364,365,366,367,380,381,382}
for c,b in BLOCS:
    for i,vw in enumerate('aeiou'):
        n=b+i; val=c+vw
        (OBS if n in SEEN else INT)[str(n)]=val
for n,v in {334:'qua',335:'que',336:'qui'}.items(): OBS[str(n)]=v
INT['337']='quo'
# mots
W = {38:'et',51:'votremajeste',61:'roytreschrestien',92:'roydangleterre',96:'lechancelier',100:'et',107:'messieurslesestats',
     114:'dannemarck',115:'norvegue',116:'lafrance',119:'langleterre',120:'lasuede',130:'lahollande',133:'coppenhague',134:'stockholm',
     145:'lahaye',157:'hollandois',161:'affaires',162:'affection',166:'argent',169:'avantage',192:'commerce',196:'contre',
     215:'executer',222:'faire',225:'fomenter',227:'fort',236:'garentye',240:'guerre',288:'majeste',313:'on',373:'traitte',376:'traffic',
     389:'votre',395:'sund'}
for k,v in W.items(): OBS[str(k)]=v
T = dict(INT); T.update(OBS)
if __name__=='__main__':
    import json,sys
    json.dump({'T':T,'obs':sorted(OBS),'int':sorted(INT)},sys.stdout,ensure_ascii=False,indent=0,sort_keys=True)
