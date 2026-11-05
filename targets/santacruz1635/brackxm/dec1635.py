"""Apply the 1635 working key to the transcribed cipher blocks (```...```) of a file."""
import re, sys

K = {}
def add(s):
    for pair in s.split(','):
        k, v = pair.strip().split('=')
        K[k.strip()] = v.strip()

# syllables: vowel kept, consonant replaced
for v in 'aeiou':
    K['x'+v] = 'l'+v; K['n'+v] = 'd'+v; K['l'+v] = 'p'+v; K['Z'+v] = 'v'+v
    K[v+'r'] = 's'+v; K[v+'t'] = 'g'+v
for base, c in [(28,'c'),(33,'f'),(43,'m'),(48,'r'),(53,'t')]:
    for i, v in enumerate('aeiou'):
        K[str(base+i)] = c+v
add("""29=ce, 30=ci, 31=co, 32=cu, 36=fo, 38=ya, 41=yo, 44=me, 45=mi, 46=mo, 47=mu, 49=re, 50=ri, 51=ro,
54=te, 55=ti, 56=to, 57=tu, 58=cha, 60=cho, 10=bi, 11=que, 12=p, 14=i, 17=t, 20=veinte, 22=xe,
13=y, 15=y, 68=que, 69=que, 70=que, 71=de, 72=de, 75=aunque, 77=avisa, 78=año, 80=assi, 83=fue,
85=armada, 86=aquel, 88=all-, 97=bie(n), 98=bue, 101=Duque, 109=Duque, 110=Dios, 111=diligencia,
113=daño, 116=despacho, 117=despues, 118=qui, 120=discurso, 122=dicho, 133=efecto, 134=ere,
136=enemigo, 139=ello, 144=español, 146=estado, 148=ju, 150=for, 151=fuerte, 156=frances,
157=Francia, 160=fortificacion, 163=D.FcoMelo, 176=General, 178=gente, 186=galera, 187=galeon,
190=hombre, 195=hazi, 196=hecho, 197=hazer, 198=haviendo, 205=lugar, 206=liga, 209=luego,
217=Marques, 218=Milan, 219=mucho, 220=muy, 228=navio, 229=Villanueva, 232=necesidad,
233=Napoles, 235=vuestro, 243=orden, 244=otro, 252=obra, 255=principe, 260=para, 261=puerto,
274=particular, 275=pues, h=s, d=s, g=e, x=e, r=a, p=a, v=a, f=a, e=l, C=l, L=n, l=n, y=o, m=o, b=o,
6=r, 1=r, 7=b, 3=d, 8=u, B=h, Δ=g, D=ç, an=al, en=el, Jel=resolucion, Jos=Republica, Ney=Señor,
der=como, sel=vos, noy=sobre, flo=cuidado, nal=tanto, nil=tiempo, pax=tambien, pex=tregua, pux=Turco,
men=socorro, mun=Saboya, ilt=CondeMonterrey, ult=CardenalAlbornoz, ban=Cardenal, alt=CondeDuque,
bis=carta, hoc=quan, hac=quanto, pin=villa, fen=conveniente, tard=vasallos, pan=tengo, huc=quenta,
mah=Sicilia, Z=n, n=h, 1u=pu, ff=m, sol=vuestro, 229=nueva, 230=sin, 231=necesari-, 63=xa, 168=ca, 165=frances, 191=hermano, 212=MarquesSantaCruz, lec=razon, mach=seguridad, tic=visto, Q=justo, 26=o, 9=a, 1c=no, Lc=no, ch=os, Ch=os, 19=u, Le=me, o=e, c=o, 7L=de, Lo=ne, &=, I=, T=, S=""")

def dec(tok):
    t = tok.strip('.,')
    if t in K: return K[t]
    return '[' + t + ']'

f = sys.argv[1]
for blk in re.findall(r'```(.*?)```', open(f).read(), re.S):
    for line in blk.strip('\n').split('\n'):
        out = []
        for part in re.split(r'(\(clear:\)[^0-9]*)', line):
            if part.startswith('(clear:)'):
                out.append('«' + part[8:].strip() + '»')
            else:
                out.append(' '.join(dec(t) for t in part.split()))
        print(' '.join(out))
    print()
