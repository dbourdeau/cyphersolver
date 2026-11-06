"""Decode R91 with Meister 1906 key no. 2 ("Cifra ultima con Mons. Poggio mandata per il Montepulciano", 1538-42).

Read polyphonically from the print: a3 e5 i7 o9 u0, b/c 8, d/f/g 01, l/p 2, n/m 4, r/t 6, et 1 (s/z has no value
printed). Dots are not in the DECODE transcript, so each dotted syllable is offered as an alternative of its
undotted code (80 na|ta ... 89 re|non, 08 ri|ns, 00 ro|smta).
"""
import sys
from key1 import beam_decode, lm, lines

K2 = {'3': ['a'], '5': ['e'], '7': ['i'], '9': ['o'], '0': ['u'], '8': ['b', 'c'], '01': ['d', 'f', 'g'],
      '2': ['l', 'p'], '4': ['n', 'm'], '6': ['r', 't'], '1': ['et'], '11': [''],
      '21': ['ca'], '22': ['ce'], '23': ['ci'], '24': ['co'], '88': ['ra', 'chi'], '89': ['re', 'non'],
      '08': ['ri', 'ns'], '00': ['ro', 'smta'],
      '12': ['da'], '14': ['de'], '16': ['di'], '18': ['do'], '84': ['sa', 'qua'], '85': ['se', 'que'],
      '86': ['si', 'qui'], '87': ['so', 'che'],
      '62': ['la'], '64': ['le'], '61': ['li'], '66': ['lo'], '04': ['ma'], '06': ['me'], '03': ['mi'], '05': ['mo'],
      '80': ['na', 'ta'], '81': ['ne', 'te'], '82': ['ni', 'ti'], '83': ['no', 'to']}

if __name__ == '__main__':
    m = lm.load('it-cinquecento', order=5, spaces=False)
    d = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
    s, path = beam_decode(d, K2, m, int(sys.argv[1]) if len(sys.argv) > 1 else 64)
    text = ''.join(o for _, o in path)
    print(f'score {s:.1f} per char {s / len(text):.3f} chars {len(text)}')
    print(text)
    print(' '.join(f'{c}={o}' for c, o in path[:120]))
