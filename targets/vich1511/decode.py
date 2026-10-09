"""Decode a transcription of the Ferdinand-Vich cipher (AHN Estado 8715, 1511-12 key).

Values come from aligning N.46 (5 Jul 1511) and N.52BIS (1 Mar 1512) with their contemporary
decipherments. Unknown tokens print in [brackets]."""
import sys, re

LET = {  # single symbols -> letters (homophones)
    '40': 'r', '4h': 'e', '3': 'e', 'ah': 'o', 'T': 'o', 'to': 'a', 'q': 'm', '7': 'a', 'b': 'a',
    'ch': 'c', 'c': 'l', 'oo': 'd', '11': 'n', 'X': 't', 'g': 't', 'P': 'p', 'SS': 'p', 'e': 'i',
    'Z': 'i', '8': 'y', 'B': 'b', 'd': 's', 'eh': 's', 'V': 'v', '3t': 'u', 'gh': 'f', '7o': 'll',
    '9': 't', 'p': 'z', 'q1': 'a', '11h': 'l', '6h': 'u', 'xt': 'e', 'A': 'd', 'bh': 'a', 'qto': 'l', 'B8': 'b', 'pi': 'm', 'W': 'n', 'mt': 'p', 'tt': 'r', 'o': 'g', 'O': 'h', 'E': 'r',
}
CODE = {  # code groups -> words / syllables
    'pef': 'que', 'diz': 'de', 'dih': 'con', 'fak': 'el', 'fem': 'es', 'fan': 'en', 'has': 'lo',
    'hor': 'la', 'raf': 'por', 'rif': 'porque', 'mik': 'no', 'flart': 'me', 'seh': 'se', 'pob': 'si',
    'soy': 'io', 'suy': 'ia', 'pax': 'su', 'mix': 'papa', 'moe': 'mucho', 'mee': 'muy', 'mem': 'nro',
    'fug': 'señor', 'fiq': 'victoria', 'sod': 'sera', 'gik': 'agora', 'go': 'aunque', 'doh': 'contra',
    'fid': 'despues', 'sal': 'todo', 'sel': 'todo', 'sub': 'vras', 'par': 'recebido', 'hap': 'havemos',
    'hag': 'havemos', 'hib': 'guerra', 'hub': 'gente', 'gos': 'ciudad', 'pip': 'razon', 'fub': 'daño',
    'fuj': 'exercito', 'dai': 'como', 'mok': 'nos', 'fol': 'ellas', 'goy': 'cartas', 'fis': 'febrero',
    'fib': 'febrero', 'hat': 'luego', 'fac': 'dichas', 'heh': 'ha', 'hig': 'haver', 'day': 'direys',
    'gak': 'aquella', 'hel': 'ingalaterra', 'hep': 'julio', 'gik': 'agora', 'pag': 'quales',
    'moe': 'mucho', 'die': 'cosa', 'huf': 'he', 'fun': 'esta', 'sus': 'um', 'miq': 'orden',
    'plart': 'mi', 'soy': 'yo', 'mah': 'dezir', 'fim': 'esta', 'fit': 'capitan', 'dee': 'general',
    'gab': 'assi', 'plort': 'al', 'fef': 'emperador', 'sap': 'venecianos', 'ref': 'para', 'suk': 'tiene',
    'roc': 'parece', 'gor': 'venir', 'seg': 'viene', 'hob': 'largo', 'fir': 'del', 'rof': 'paraque', 'keg': 'pero',
    'huz': 'mas', 'fud': 'dicho', 'hik': 'italia', 'myk': 'no', 'rie': 'pued', 'fat': 'forma', 'dieb': 'cosas', 'fic': 'del',
    'soq': 'verdad', 'daz': 'dize', 'gup': 'batalla', 'fur': 'dela', 'guo': 'bien', 'dij': 'cierto', 'diy': 'cierto',
    'hih': 'ha', 'fue': 'saber', 'far': 'dar', 'pid': 'presa', 'gaf': 'aqui', 'guj': 'esto', 'meq': 'otra',
    # from N.45 (Apr 1511), agent alignment
    'plut': 'ni', 'fen': 'esto', 'fio': 'ferrara', 'dur': 'duque', 'poj': 'rey', 'rug': 'parte',
    'mag': 'otro', 'peh': 'quiere', 'mef': 'manera', 'heg': 'haveys', 'dex': 'deve', 'fae': 'dicha',
    'mac': 'mil', 'guz': 'consejo', 'fep': 'hazer', 'mul': 'negocio', 'mak': 'napoles', 'fop': 'hecho', 'dez': 'dezir', 'hah': 'he', 'foo': 'ducados', 'dot': 'dos',
    'gol': 'alguna', '&': 'y',
    # from N.45 pp.10-15 (second-half alignment)
    'fos': 'deseo', 'mef': 'manera', 'mum': 'ninguna', 'feh': 'estado', 'ob': 'ga', 'sod': 'ser',
    'heg': 'haveys', 'hes': 'lugar', 'pic': 'potencia', 'gno': 'bien', 'mye': 'papa', 'dox': 'duque',
    'dux': 'duque', 'dur': 'duque', 'fax': 'franceses', 'fuq': 'francia', 'gub': 'armas', 'sat': 'uno',
    'set': 'una', 'ged': 'amistad', 'di': 'cardenal', 'plu': 'ni', 'far': 'dar',
    # from N.41 (22 May 1510), aligned with its clerk decipherment (n41_align.tsv)
    'poi': 'rey de francia', 'pum': 'roma', 'feo': 'florentines', 'hey': 'mantua', 'fof': 'embaxador',
    'sno': 'venecianos', 'med': 'moros', 'gux': 'capitanes', 'hoh': 'hombre', 'haj': 'hombres de armas',
    'may': 'mayo', 'pep': 'remedio', 'poy': 'secreto', 'fil': 'ellos', 'hio': 'junto', 'sim': 'tratado',
    'seq': 'conviene', 'maf': 'mucha', 'sul': 'tambien', 'guy': 'aquellos', 'gil': 'algun', 'pif': 'quando',
    'fon': 'estas', 'hol': 'justa', 'goo': 'brevemente', 'gug': 'autoridad', 'io': 'prudencia',
    'man': 'necessidad', 'myr': 'mayor', 'sne': 'saber', 'oto': 'qu', 'Vh': 'ss', 'muk': 'no',
    # from 8714 N.39 (13 May 1510) and N.12 (30 Sep 1508), aligned with their clerk decipherments
    'plirt': 'ni', 'sol': 'todos', 'feb': 'hasta', 'mox': 'principes', 'gue': 'alla', 'gey': 'christianos',
    'gem': 'avisad', 'mym': 'nuestra', 'gip': 'buena', 'gep': 'buen', 'pey': 'secreto', 'mom': 'ningun',
    'rig': 'persona', 'sug': 'verdadero', 'sax': 'verdadera', 'moh': 'mandamiento', 'my': 'mal',
    'mup': 'officio', 'pare': 'su', 'dof': 'creo', 'hin': 'infieles', 'hue': 'general', 'fns': 'fines',
    'pyy': 'secretario', 'pak': 'aquella', 'mon': 'nuestro', 'dub': 'cardenal santa cruz', 'syg': 'suya',
    'gu': 'assimismo', 'N': '.', '/': '.', '9to': '.',
    # from the N.60 v2 re-transcription (5 Oct 2026), context forced over many occurrences (n60_v2_groups.tsv)
    '&2': 'x', 'flort': 'liga', 'fiy': 'favor', 'fuy': 'exercito', 'mat': 'obligado',
    # from N.60 (1 Sep 1512)
    'mar': 'mil', 'das': 'ducado', 'gib': 'franceses', 'maq': 'otro', 'pio': 'rey', 'fer': 'dio',
    'sok': 'fiar', 'sum': 'tierra', 'hiz': 'mar', 'gih': 'dexar', 'fex': 'fe', 'mac': 'mil',
}

def decode(tokens):
    out = []
    for t in tokens:
        if t in CODE: out.append(' ' + CODE[t] + ' ')
        elif t in LET: out.append(LET[t])
        else: out.append(' [' + t + '] ')
    return re.sub(r' +', ' ', ''.join(out)).strip()

if __name__ == '__main__':
    for line in open(sys.argv[1], encoding='utf-8'):
        if not line.startswith('L'): continue
        tag, body = line.split(':', 1)
        print(tag, decode(body.split()))
