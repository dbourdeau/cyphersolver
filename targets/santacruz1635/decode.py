"""Apply the Sept-Dec 1635 Santa Cruz key (issue #183, key_1635.md) to a transcription.

Built here from the prose key, not from the contributor's dec1635.py.
Usage: python decode.py FILE   (decodes the ``` blocks; reports token coverage)
"""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")

K = {}
V = 'aeiou'
# consonant+vowel: vowel kept, consonant replaced
for v in V:
    K['x' + v] = 'l' + v      # l
    K['n' + v] = 'd' + v      # d
    K['l' + v] = 'p' + v      # p
    K['Z' + v] = 'v' + v      # v/b
    K[v + 'r'] = 's' + v      # vowel-first s
    K[v + 't'] = 'g' + v      # vowel-first g
# number blocks of five
for base, c in [(28, 'c'), (33, 'f'), (43, 'm'), (48, 'r'), (53, 't')]:
    for i, v in enumerate(V):
        K[str(base + i)] = c + v
K.update({'50': 'ri', '51': 'ro', '38': 'ya', '41': 'yo', '58': 'cha', '60': 'cho', '63': 'ja',
          '168': 'ca', '148': 'ju', '150': 'for', '10': 'bi', '12': 'p', '14': 'i', '17': 't',
          '22': 'xo', '20': 'veinte', '13': 'y', '15': 'y', '68': 'que', '69': 'que', '70': 'que',
          '11': 'que', '71': 'de', '72': 'de', '260': 'para', 'en': 'el', 'an': 'al'})
# single letters
K.update({'h': 's', 'd': 's', 'g': 'e', 'f': 'a', 'v': 'a', 'p': 'a', 'e': 'i', 'C': 'l',
          'L': 'n', 'y': 'o', 'b': 'o', 'm': 'o', '6': 'r', '1': 'r', '7': 'b', '3': 'd',
          'n': 'h', 'B': 'h', 'D': 'c', 'x': 'e', 'r': 'a', 'o': 'e', 'c': 'o', '8': 'u',
          '19': 'u', '26': 'o', '9': 'a'})
# nomenclator and word signs
K.update({'85': 'armada', '86': 'aquel', '88': 'all-', '97': 'bien', '98': 'bue', '101': 'Duque',
          '109': 'Duque', '110': 'Dios', '111': 'diligencia', '113': 'dano', '116': 'despacho',
          '117': 'despues', '118': 'qui', '120': 'discurso', '122': 'dicho', '133': 'efectos',
          '134': 'ere', '136': 'enemigos', '139': 'ellos', '144': 'espanoles', '146': 'estado',
          '151': 'fuerte', '156': 'franceses', '157': 'Francia', '160': 'fortificacion',
          '163': 'D.Francisco de Melo', '165': 'frances', '176': 'General', '178': 'gente',
          '186': 'galeras', '187': 'galeones', '190': 'hombres', '191': 'hermano', '195': 'hazi-',
          '196': 'hecho', '197': 'hazer', '198': 'haviendo', '205': 'lugar', '206': 'liga',
          '209': 'luego', '212': 'Marques de Santa Cruz', '217': 'Marques', '218': 'Milan',
          '219': 'mucho', '220': 'muy', '228': 'navios', '229': 'nueva', '230': 'sin',
          '231': 'necesario', '232': 'necesidad', '233': 'Napoles', '235': 'vuestro',
          '243': 'orden', '244': 'otro', '252': 'obra', '255': 'principe', '261': 'puerto',
          '274': 'particular', '275': 'pues', '75': 'aunque', '77': 'avisa', '78': 'ano',
          '80': 'assi', '83': 'fue', '81': 'asistencia',
          'Jel': 'resolucion', 'Jeil': 'Reyno', 'Jos': 'Republica', 'Ney': 'Senor', 'der': 'como',
          'sel': 'vos', 'sol': 'vuestro', 'noy': 'sobre', 'flo': 'cuidado', 'nal': 'tanto',
          'nil': 'tiempo', 'pax': 'tambien', 'pex': 'tregua', 'pux': 'Turco', 'men': 'socorro',
          'mun': 'Saboya', 'ilt': 'Conde de Monterrey', 'ult': 'Cardenal Albornoz',
          'ban': 'Cardenal', 'alt': 'Conde Duque', 'bis': 'carta', 'hoc': 'quando',
          'hac': 'quanto', 'pin': 'villa', 'fen': 'conveniente', 'tard': 'vasallos',
          'pan': 'tengo', 'huc': 'quenta', 'mah': 'Sicilia', 'lec': 'razon', 'mach': 'seguridad',
          'tic': 'visto', 'Q': 'justo', 'J': 'Italia'})

# D.179 transcription signs (brackxm/signs_d179.md, issue #183, 31 Oct 2026): conventions of the earlier
# transcription passes, written here from that list, not copied from dec1635.py. I, T, S are marks (no value).
K.update({'ff': 'm', '1u': 'pu', '1c': 'no', 'Lc': 'no', 'ch': 'os', 'Ch': 'os', 'Le': 'me', '7L': 'de',
          'Lo': 'ne', 'Z': 'n', 'l': 'n', 'I': '', 'T': '', 'S': ''})


def decode_line(line):
    """Return (text, n_tokens, n_unknown). '(clear:)' tails are kept as-is."""
    out, n, u = [], 0, 0
    parts = re.split(r'(\(clear:\)[^0-9]*)', line)
    for part in parts:
        if part.startswith('(clear:)'):
            out.append('<' + part[8:].strip() + '>')
            continue
        for t in part.replace('|', ' ').split():
            if t in '.,&':
                continue
            n += 1
            if t in K:
                out.append(K[t])
            else:
                u += 1
                out.append('[' + t + ']')
    return ' '.join(out), n, u


if __name__ == '__main__':
    text = open(sys.argv[1], encoding='utf-8').read()
    N = U = 0
    for blk in re.findall(r'```(.*?)```', text, re.S):
        for line in blk.strip('\n').split('\n'):
            s, n, u = decode_line(line)
            N += n; U += u
            print(s)
        print()
    print(f'# tokens {N}, without value {U} ({100 * (N - U) / max(N, 1):.1f}% valued)')
