"""extract_decode_o5.py (PREREG-O5 §6, 25/11/2026) - extrait de MESURE-O5.txt les seules lignes de décodage
('6v L01: lettres') vers lecture-input/DECODE-O5.txt, sans M, sans témoins, sans verdict, sans noms de signes : c'est le
SEUL texte que voient les lecteurs par le sens (§7). '?' = signe sans valeur de clé (nom t..., tS-..., NIL, barré).
Lancer depuis o5-2511/ : python3 -I tools/extract_decode_o5.py"""
import re, os
rows = []
for l in open('MESURE-O5.txt', encoding='utf-8'):
    m = re.match(r'^(\d[rv] L\d\d): ([a-z?]*)$', l.rstrip('\n'))
    if m: rows.append((m.group(1), m.group(2)))
assert rows, 'aucune ligne de décodage'
assert len({r for r, _ in rows}) == len(rows), 'ligne en double'
os.makedirs('lecture-input', exist_ok=True)
hdr = ('# DECODE-O5.txt - décodage mécanique (clé figée, aucune correction) de la portion Q, lettre du 12 mars 1548.\n'
       '# Une ligne par ligne chiffrée, dans l\'ordre ; le texte est continu : un mot peut se poursuivre d\'une ligne (et d\'une page) à la suivante.\n'
       '# Lettres a-z (i/j et u/v confondus, sans accents) ; ? = signe sans valeur dans la clé. %d lignes, %d caractères, dont %d ?.\n'
       % (len(rows), sum(len(s) for _, s in rows), sum(s.count('?') for _, s in rows)))
open('lecture-input/DECODE-O5.txt', 'w', encoding='utf-8').write(hdr + ''.join('%s: %s\n' % r for r in rows))
print(len(rows), 'lignes écrites dans lecture-input/DECODE-O5.txt')
