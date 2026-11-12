"""decode_lot3.py SIGNS_TXT KEY_CODES_TSV : raw decode of a shape-label transcription for reading by sense (lot 3: lot-2 table + Daniel's own labels 9/OO/U/⊥/3f/x, PREREG_lot3 §1).
Key unchanged: code groups -> key_codes.tsv (Daniel, origin/main 62b62c5b5); letter signs -> the fixed table below, from
alpha.py / measure.py SIGNS (lot 1) with the declared look-alike alternatives of PREREG_lot2.md. Output per line:
codes in CAPS-free plain separated by '.', letters run together, alternatives as (x|y), unknown groups as <grp>."""
import sys, re
SIGN = {'n':'a','Z':'(a|s|c)','b':'b','z':'c','4':'e','y':'e','3':'(d|e)','oo':'d','P':'(f|s)','L':'g','X':'h','x':'h',
        'mo':'h','ai':'i','9':'l','B':'(m|r)','&':'n','t4':'n','#':'o','ao':'p','tt':'(p|n)','g':'(r|y)','Q':'s','q':'(s|t)',
        'Yo':'(s|t)','Lo':'t','m':'v','o':'x','xo':'s','A':'z',
        'OO':'g','U':'(u|v)','⊥':'r','3f':'a'}
NULLS = {'ll','#t','#o'}
def load_key(p):
    K = {}
    for line in open(p, encoding='utf-8').read().splitlines()[1:]:
        if '\t' not in line: continue
        c, v = line.split('\t', 1); K[c.rstrip('?')] = v
    return K
def main():
    K = load_key(sys.argv[2]); unk = {}
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        if line.startswith('##'): print(line.strip()); continue
        f = line.split(); ref, toks = f[0], f[1:]; out = []; prev_letter = False
        for t in toks:
            t0 = t.rstrip('?').lstrip('^')
            if t0 == '|': continue
            if t0 in NULLS: continue
            if t0.startswith('='): out.append(' ['+t0[1:]+'] '); prev_letter = False; continue
            if t0.startswith('['): out.append(' … '); prev_letter = False; continue
            if t0 in SIGN: out.append(SIGN[t0]); prev_letter = True; continue
            if t0 in K: out.append(' '+K[t0]+' '); prev_letter = False; continue
            out.append(' <'+t0+'> '); unk[t0] = unk.get(t0, 0) + 1; prev_letter = False
        print(ref, re.sub(' +', ' ', ''.join(out)).strip())
    print('# unknown groups:', ' '.join('%s×%d' % kv for kv in sorted(unk.items(), key=lambda kv: -kv[1])))
if __name__ == '__main__': main()
