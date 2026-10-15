# Regrade of R1139 and R1136 (pass 3, 2 Oct 2026) with the values fixed on V1921 (lone o = h/u, oo = b, z+/x+/xp = q,
# EL/AMP = f, K = et). Proposals: beam21.py (output saved in beam21_out.txt); every phrase below was checked against the
# sign crops seg21/<SRC>_Lnn_k.png. The share is (letters inside claimed phrases) / (letters the line decodes to,
# nulls excluded); letters in [..] are not counted, supplied letters [x] are counted as grade M.
# Run: python regrade21.py
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

CLAIMS = {
 'R1139': {   # pass 4: r1139_pass4.txt, beam output beam21_r1139_pass4.txt
  'L01': ["il custode qando a buda come i scrisi e tornato gubernator de"],
  'L02': ["decime", "ogni cosa per", "si e tenuto agria in oficio"],
  'L03': ["credo dia ogni ato e qualche cosa a le ma di o custode per ancora si n'e in"],
  'L04': ["trato", "in castelo et cosi la venuta sua in Italia", "che vi scrivi qual"],
  'L05': ["li teneva per ferma e andata in vero il che vedendo io", "li go fato"],
  'L06': ["moto deli danari del suo debito come mi dise messer alfonso"],
  'L07': ["lui m'ha resposto dice te voler andar in Italia quando al dare"],
  'L08': ["mi per Milan", "andiate parlaremo a longo sopra ciò"],
  'L09': ["danari in [p]resto per andar", "ve ne daro vedro quel mi dara e il tuo repo"],
  'L10': ["rtaro a v[ostra] ex"],
 },
 'R1136': {   # pass 4: second transcription r1136_pass4.txt, beam output beam21_r1136_pass4.txt
  'L01': ["transferse a Buda il custode"],
  'L02': ["in oficio questo episcopato et a epso custode"],
  'L03': ["guernator", "lactantio ho inteso qual"],
  'L04': ["in gran presia", "dicono esser conclusi"],
  'L05': ["congregati", "bachiensis", "che ogni episcopa"],
  'L06': ["il manco", "cosi", "tenir"],
  'L07': ["l'altro in titolo", "et a questo modo excludera"],
  'L08': ["li daran poco", "vostra excelentia quel si"],
  'L09': ["potra far al custode", "questa via de ungaria sopra il suo"],
  'L10': ["debi", "secondo", "patrone", "in questo loco niente"],
  'L11': ["tornato el sia", "e vedro intendere il"],
  'L12': ["spensier suo", "supra tal debito"],
 },
}

def letters(s):
    s = re.sub(r'\[\.\.\]', '', s)
    return len(re.findall(r'[a-zàèìòù]', s.lower()))

def main():
    out = {}
    FILES = {'R1139': 'beam21_r1139_pass4.txt', 'R1136': 'beam21_r1136_pass4.txt'}
    for src0, fn in FILES.items():
      if not os.path.exists(os.path.join(HERE, fn)): fn = 'beam21_out.txt'
      for line in open(os.path.join(HERE, fn), encoding='utf8'):
        src, lab = line.split()[:2]; lab = lab.rstrip('*')
        if src != src0: continue
        txt = line.rsplit(']', 1)[1].strip()
        out[(src, lab)] = len([c for c in txt if c.isalpha()])
    for src, lines in CLAIMS.items():
        tot = sum(n for (s, _), n in out.items() if s == src)
        got = sum(min(sum(letters(p) for p in ph), out[(src, lab)]) for lab, ph in lines.items())
        print(f'{src}: {got} of {tot} decoded letters inside claimed phrases ({100*got/tot:.1f} %)')

if __name__ == '__main__':
    main()
