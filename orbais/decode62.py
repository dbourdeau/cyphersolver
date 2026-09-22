"""Decode the cipher groups of BnF fr. 3413 no. 62 (no62_cipher.txt) with the Nevers-Piles key as far as it is
known, print the reading, and measure the fraction read.

Sources of each value (grade in brackets, README Conventions):
  T  = Tomokiyo's partial Nevers-Piles table (cryptiana nevers.htm, from fr. 3612 f. 9)
  S  = fr. 4715 f. 2 (Guise to Nevers, 6 Oct 1586, same cipher, interlinear decipherment), fr4715_f2_aligned.txt
  K  = crib from the clear context of no. 62 itself
A token counts as read only when its group reads as French sense; letter values that give no sense (group C,
the tail of V) and code signs with no value are counted unread.

python decode62.py          -> reading + measured fraction
"""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
# sign -> (value, source)
KEY = {
    '1': ('de', 'T S'), '3': ('d', 'T'), '4': ('h', 'T S'), '6': ('p', 'K (depeschera, protection); T p = o-with-stroke'),
    '7': ('d', 'S'), '8': ('t', 'K (protection); in fr. 4715 8 = c'), '9': ('i', 'T S'),
    'W': ('c', 'T S'), 'V': ('a', 'T'), '÷': ('s', 'T S'), '◻': ('n', 'T S'), '⊡': ('r', 'T S'),
    'θ': ('e', 'T S'), 'æ': ('e', 'T S'), 'tt': ('o', 'T (o row 2), K'), 'm': ('o', 'T (tailed m), S (qui monstrent)'),
    'ooo': ('t', 'T S'), 'ɔ': ('u', 'T S'), 'φ': ('u', 'T S'), 'ɸ': ('i', 'K (protection, advis)'),
    'b': ('u', 'T (u row 3), S; K advis'), 'η': ('g', 'T S'), '−': ('a', 'T S'), 'q': ('s', 'S'),
    '∇': ('m', 'T S'), 'x': ('m', 'S (madame, qui monstrent), K mon, confirme'), 'ħ': ('i', 'T (i row 2)'),
    'Ⱥ': ('f', 'T (f)'), '⋕': ('o', 'K (mon, confirme)'), '2': ('b', 'T'), 'Ħ': ('n', 'S (H = n)'),
    'a': ('f', 'S (ferons)'), 'n': ('et', 'T (code et), S (et a mon avis, responces et)'),
    '⌘': ('Mr', 'T (code Mr)'), 'Ƒ': ('le', 'S (ʃ-with-bar = le: pour le bien, le monde); K le doyen'),
    'ʃ': ('jay', 'S (line 1: ʃ receu = Jay receu); K jay veu'),
}
PER_GROUP = {('P1', 'ꝥ'): ('l', 'T (l row 2), K la protection')}
# group -> (reading, grade) ; None = no sense reading.  Unread code signs are listed in UNREAD.
READ = {
    'S1a': ('[Ƃ] de-pes', 'C'), 'S1b': ('chera [ʃ]', 'C'), 'S2': ('le doien', 'C'),
    'C': (None, None), 'P1': ('la protect', 'H'), 'P2': ('ion', 'H'), 'Cas': ('Cassin', 'H'),
    'V1': ('vostre', 'H'), 'V2': (None, None), 'G1': ('Mr le [τ] mon mai', 'C'), 'G2': ('stre', 'H'),
    'H': ("j'ay veu ung advis", 'C'), 'I': ('confirme', 'C'), 'Sig': ('Baron', 'H'),
}
UNREAD = {('S1a', 'Ƃ'), ('S1b', 'ʃ'), ('G1', 'τ')}   # code signs with no value (the ʃ at the end of S1 is not 'jay')


def main():
    rows = []
    for line in (HERE / 'no62_cipher.txt').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'): continue
        g, *toks = line.split()
        rows.append((g, toks))
    total = read = 0
    for g, toks in rows:
        vals = []
        for t in toks:
            v = PER_GROUP.get((g, t)) or KEY.get(t)
            vals.append('?' if (g, t) in UNREAD or v is None else v[0])
        reading, grade = READ[g]
        n_read = 0 if reading is None else sum(1 for t in toks if (g, t) not in UNREAD)
        total += len(toks); read += n_read
        print(f'{g:4} {" ".join(toks):28} -> {"".join(vals):22} | {reading or "(no sense)":22} {grade or "-"}  {n_read}/{len(toks)}')
    print(f'\ncipher tokens {total}, read as sense {read}, fraction {read/total:.3f}')


if __name__ == '__main__':
    main()
