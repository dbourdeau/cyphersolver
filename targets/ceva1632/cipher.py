"""The Barberini-Ceva cipher of ASV SdS Francia 346 (1632-34).

System, as reconstructed by George Lasry (DECODE, 24 Oct 2020) and checked
here against his aligned decipherments of 346:1, 346/4, 346/5 and 346/9:

  6         word separator
  2x        null (no 2x pair is used for plaintext)
  XY        homophone / syllable, from KEY below
  pXY       nomenclator element: one prefix digit + a 2-digit code.
            Lasry's note names prefix 4; in his own readings the prefix is
            also 0, 1, 3, 5, 7, 8 or 9. None of the 95 he marked was solved.
"""

KEY = {}
for codes, val in [
    ('19|38|47', 'a'), ('73', 'al'), ('08|79', 'b'), ('10|71', 'c'),
    ('44', 'che'), ('55', 'chi'), ('00', 'con'), ('09|48', 'd'),
    ('74', 'da'), ('77', 'de'), ('84', 'di'), ('18|37|45', 'e'),
    ('97', 'et'), ('51|80', 'f'), ('91', 'g'), ('07', 'h'),
    ('17|35|41', 'i'), ('53', 'il'), ('34', 'in'), ('54', 'io'),
    ('57|90', 'l'), ('83', 'la'), ('01|78', 'm'), ('93', 'ma'),
    ('14', 'mi'), ('30|81', 'n'), ('11', 'no'), ('15|31|39', 'o'),
    ('04|58', 'p'), ('13', 'per'), ('89', 'qu'), ('88', 'quel'),
    ('59|70', 'r'), ('03|87', 's'), ('94', 'se'), ('95', 'si'),
    ('43', 'st'), ('40|85', 't'), ('49|75|98', 'v'), ('50', 'z'),
]:
    for c in codes.split('|'):
        KEY[c] = val

SEP = '6'
NULLS = {'2%d' % d for d in range(10)}

def is_null(t):
    return t in NULLS

def units(t):
    """Plaintext of a token, or None if it is not a plain 2-digit code."""
    return KEY.get(t)


# Nomenclator elements read here off the 1632 interlinear decipherment of R75
# and confirmed against Lasry's four letters.  He left all 95 unsolved.
NOMEN = {
    '474': 'mente',    # piena~, principal~, non sola~, malacomoda~
    '495': 'quanto',   # "e ~ al proporre arbitrare"; pairs with 498
    '498': 'tanto',    # "che ~ in <347> quanto in <857> si sappia la cagione"
    '830': 'francia',  # always after a feminine article: "render la ~ piu poderosa"
    '854': 'guerra',   # R75 interlinear, twice
    '149': 'piazza',   # R75 interlinear, "acquisto d'una ~"
}

# Second pass, Oct 2026: read off the R75 interlinear at full image resolution
# (I589/I590), or fixed by pooling every context in Lasry's four letters + R75/R84.
NOMEN.update({
    '315': 's.e.',      # Sua Eminenza (Richelieu): R75 interlinear 'S.E.' (l.12 'che S.E. cominci'), l.27 'gia S.E. e arrivata', l.32 'alla gloria di S.E.'
    '411': 'v.s.',      # 'ricordando a ~', 'risposto ~ adequatamente', 'di ~ de ventitre', 'non so dir a ~ d'avantaggio'
    '481': 'pero',      # R75 interlinear 'pero' (l.25); 'non si poteva ~ negare', 'non lascierà ~ di andar'
    '470': 'hor',       # R75 interlinear 'hor mai' (l.14)
    '439': 'ancora',    # R75 interlinear 'consideri ancora' (l.19), 'ancora che' (l.21)
    '493': 'questa',    # R75 interlinear 'questa sola parte' (l.32); 'entrar in ~ cose' (R84)
    '938': 'monsieur',  # R75 margin 'Monsieur S.A.' (l.21/22); 'la fuga di ~', 'accomodamento di ~ col fratello'
    '988': 'negotio',   # 'il principal ~ commesso a V.S.', 'il ~ dell'accomodamento', 'quel ~ et indrizzato'
    '338': 'stato',     # 'la Francia in ~ di dar legge', 'non so quanto sia ~ a proposito', 'e ~ supposto'
    '441': 'bene',      # 'se ~ si agiustano' (interlinear 'bin'), 'al publico ~ et alla quiete', 'stimarà ~ e gradirà'
    '857': 'germania',  # R75 interlinear 'Germa' (l.21): 'alla Francia quanto alla ~'
    '334': 'sueco',     # R75 interlinear 'del Sueco' (l.20): 'la vittoria del ~'
    '104': 'svedesi',   # R75 interlinear (l.13): 'la potenza de' ~ che cominciano'
    '129': 'regno',     # R75 interlinear 'del Regno' (l.23)
    '454': 'grandi',    # R75 interlinear 'cose grandi' (l.14)
    '488': 'quale',     # R75 interlinear 'alla quale' (l.18); 'le cose sue, le quali in tempo di guerra'
    '127': 'imperiali', # R75 interlinear 'a gli Imperiali' (l.15)
})
