"""Mechanical decryption of the sibling telegrams of catalogue 1462 with the archive's own cards.

Hernandez card (CEHM CMXV.16.1557.1 scans 15-16, '../../hernandez1911/key.tsv'): l-a n-e r-i s-o t-u swap.
Clave G.A. card (scans 12-13, '../../mccarty1911/key.tsv'): digraphic, row letter + column letter.
Run: python3 decode.py > decryption.txt
"""
SW = dict(zip('alenirostu', 'lanerisout'))
def swap(w): return ''.join(SW.get(c, c) for c in w.lower())

COLS = 'blrafqenhdxyosj'
R1 = 'r i y m s o ñ u a q b l t e k'.split()
R2 = 'e f v n p w a d g x h c j z o'.split()
def ga(s):
    out = []
    for i in range(0, len(s) - 1, 2):
        a, b = s[i], s[i + 1]
        if b in COLS and a in 'wzctg': out.append(R1[COLS.index(b)])
        elif b in COLS and a in 'mvpki': out.append(R2[COLS.index(b)])
        else: out.append('[' + a + b + ']')
    if len(s) % 2: out.append('[' + s[-1] + ']')
    return ''.join(out)

HERN = {
 'CMXV.15.1420.5-6': 'Flech nzurn lndrn eschn eulhs mdino bnegl braal inlab snopj neuny unegl arous dle dlese olags psina mlele lrnndr sdrl',
 'CMXV.15.1420.6-6': 'Efola gshsy mle nled nledn cliul atqtn tidsn cuino rotln cuili liing asocl pruta',
 'CMXV.15.1430.3-3': 'Usula crnu sonon eulhs mbino drglo rvrne ninst nizsy clese',
 'CMXV.15.1432.3-4 (coded words only)': 'osasnom usula aiamodon atqtn eloru irtan dedile neuin vroul dscse umons dtmen ouna anes',
 'CMXV.15.1447.1-3 (coded words only)': 'revru Lorur Lichrh Kttns chule edsase Orgtn esaan elltc Mrule',
 'CMXV.17.1648.2-3 Gabriel (control: card does not read)': 'Hdylq gbfvl sgyln pvdhr egblht dn vdble gbgyrsl aghle pqpbl qgebyl brhth lnfyr btvrh rerbl',
}
GA = {
 'CMXV.17.1695.1-2': 'kopjg Ftskf Tlkap Lvnme',
 'CMXV.17.1695.2-2': 'ykego ijkabji Gydyn birbh kukjg nkygf kbpap apgtf',
}
print('# Hernandez swap card, applied group by group (cipher -> plain). Unedited output of the key.')
for k, t in HERN.items():
    print('\n==', k)
    for w in t.split(): print(f'{w}\t{swap(w)}')
    print('joined:', ''.join(swap(w) for w in t.split()))
print('\n# Clave G.A. card, coded words joined and read in pairs; [xy] = pair not on the card.')
for k, t in GA.items():
    s = ''.join(t.lower().split())
    print('\n==', k); print('offset 0:', ga(s)); print('offset 1:', ga(s[1:]))
