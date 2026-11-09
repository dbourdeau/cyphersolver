#!/usr/bin/env python3
"""Décodeur v6 (pandolfini-francia-1514-15). usage: python3 -I decode_v6.py CLE.json TRANSCRIPTION.txt [--tokens]
Applique tokens/base/vowels (comme mesure/measure_p03.dec_token) PUIS les règles de contexte machine de la clé
(_contexte_machine ; une règle ne s'applique que si sa clé y figure) : « 0 + 8 » (0 devant 8 = t, v5b ; ABSENTE de v6) ;
« O + r nu » (= c) ; « 2^5 y 3… » (bande = ba) ; .4. = maesta après « a » ou après « S^4 6 8 » (questa abrégé), toujours appliquée. Aucune retouche : la sortie est le décodé brut, syllabe par jeton."""
import json, re, sys

def dec_token(tok, key):
    t = tok.rstrip('?') or tok
    m = re.fullmatch(r'\.(\w+)\.', t)
    if m:
        v = key['codes'].get(m.group(1))
        if v is None:
            return '[%s]' % m.group(1) if re.fullmatch(r'[ivxlcdm]+', m.group(1)) else '‹.%s.›' % m.group(1)
        return v
    if t in key['tokens']:
        return key['tokens'][t]
    base, _, exp = t.partition('^')
    if base not in key['base']:
        return '?'
    out = key['base'][base]
    for ch in exp:
        if ch in key['vowels']:
            out += key['vowels'][ch]
        elif ch in 'nm':
            out += ch
        else:
            out += '?'
    return out

def decode_line(toks, key):
    R = key.get('_contexte_machine', {})
    outs = []
    for i, t in enumerate(toks):
        tt = t.rstrip('?') or t
        nx = (toks[i+1].rstrip('?') or toks[i+1]) if i + 1 < len(toks) else ''
        nx2 = toks[i+2] if i + 2 < len(toks) else ''
        if tt == '.4.':
            prev = re.sub(r'[^a-z]', '', ''.join(outs))
            q = [x.rstrip('?') for x in toks[max(0, i-3):i]] == ['S^4', '6', '8'] or [x.rstrip('?') for x in toks[max(0, i-3):i]] == ['S^4', '6', '8^5']
            d = 'maesta' if (prev.endswith('a') or q) else key['codes']['4']
        elif '0 + 8' in R and tt == '0' and nx.startswith('8'):
            d = 't'
        elif 'O + r nu' in R and tt == 'O' and nx == 'r':
            d = 'c'
        elif '2^5 y 3…' in R and tt == '2^5' and nx == 'y' and nx2.startswith('3'):
            d = 'ba'
        else:
            d = dec_token(t, key)
        outs.append(d)
    return outs

def main():
    key = json.load(open(sys.argv[1], encoding='utf-8'))
    show = '--tokens' in sys.argv
    for line in open(sys.argv[2], encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        lab, _, rest = line.partition(':')
        toks = rest.split()
        outs = decode_line(toks, key)
        print('    %s %s' % (lab.strip(), ' '.join(outs)))
        if show:
            print('       ' + ' '.join(toks))

if __name__ == '__main__':
    main()
