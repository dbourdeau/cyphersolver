"""dieguez1914: apply key.tsv to the settled transcription of CMXV.35.3433.1-2, write the unedited decryption, and
count the cipher words read.

A cipher word is read when the key's output for its groups, unedited, spells the word: the copy's word where the
clear copy of the time CMXV.35.3433.2-2 has it ("read: key output matches the copy"), or the Spanish word the groups
spell where the copy has nothing there. Everything else is a hole: one wrong group, a group with no value, or a
three-figure code whose value comes only from the copy (121). A word that needs group 49 or 59 is also a hole: the key
has rr there and the blind reader had r, and the copy does not settle it (it spells Corrua with rr, but
contrarevolución with one r where the cipher has 49). Spelling is compared without accents.

Run from the repository root:  python targets/dieguez1914/scripts/decrypt.py [--key49 r]
  --key49 r   the blind reader's value for 49/59 (r instead of rr), to show that the count is the same.
Writes targets/dieguez1914/decryption_CMXV.35.3433.1-2.txt and words_CMXV.35.3433.1-2.tsv (default key only).
"""
import csv, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TSV = HERE / 'transcription' / 'groups_CMXV.35.3433.1-2.tsv'
DISPUTED = {'49', '59'}   # rr in key.tsv, r to the blind reader; the copy does not settle it

# (groups, the copy's word here or None, the Spanish word the groups are compared with, note)
WORDS = [
    ('87 94 58 88 46 99 71 82 74 48 86', 'descubriose', 'descubriose', ''),
    ('63 79 80 66', 'plan', 'plan', ''),
    ('95 61 90 84 50 80 97 74', 'Irapuato', 'fraguado', 'copy: Irapuato; the groups spell f r a g ? a d o'),
    ('88 79 86 71 64', 'clero', 'clero', ''),
    ('96 76', 'en', 'en', ''),
    ('98 74 66 97 61 80 10 88 55 64 79 46 121', 'contrarevolución', 'contrarrevolución', ''),
    ('89 90 81 64', 'bajo', 'bajo', ''),
    ('69 96 47 81', 'lema', 'lema', ''),
    ('61 86 79 82 94 92 74 46', 'Religion', 'religion', ''),
    ('85 46', 'y', 'y', 'the cipher has f u where the copy has y'),
    ('85 46 96 61 74 48', 'Fueros', 'fueros', ''),
    ('63 61 74 98 16 87 82 87 64', 'procedido', 'procedido', ''),
    ('90', None, 'a', 'not in the copy: procedido a aprehender'),
    ('80 43 71 86 83 96 66 87 96 71', 'aprehender', 'aprehender', ''),
    ('80', 'a', 'a', ''),
    ('79 64 48', 'los', 'los', ''),
    ('88 46 61 90 48', 'curas', 'curas', ''),
    ('87 64 88 46 67 86 66 47 74 48', 'documentos', 'documentos', ''),
    ('87 98 66 56 76 88 92 80 66', None, 'denuncian', 'not in the copy (copy: con)'),
    ('69 74 48', None, 'los', 'not in the copy'),
    ('69 74 58', 'los', 'los', ''),
    ('63 61 64 77 74 47 64 61 86 48', 'promotores', 'promotores', ''),
    ('98 74 66 47 61 80 49 86 55 64 79 46 121', 'contrarevolución', 'contrarrevolución', ''),
    ('87 96 79', 'del', 'del', ''),
    ('67 74 41 82 77 87 86 47 64', 'movimiento', 'movimiento', ''),
    ('88 46 61 80', 'Cura', 'cura', ''),
    ('90 66 47 84 66 82 74', 'Antonio', 'antonio', ''),
    ('98 64 49 56 90', 'Corrua', 'corrua', ''),
    ('80', None, None, 'stray group after Corrua; not a word'),
    ('90 63 71 86 83 96 66 87 82 97 64', 'aprehendido', 'aprehendido', ''),
    ('88 90 48 57 82 94 80 61 96', 'Castigaré', 'castigare', ''),
    ('67 90 76 64', 'mano', 'mano', ''),
    ('69 74 48', 'los', 'los', ''),
    ('41 86 63 74 66 48 90 99 80 66 58', 'responsables', 'responsables', ''),
]


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def load_key(key49):
    key = {}
    for line in open(HERE / 'key.tsv', encoding='utf-8'):
        if line.startswith('#') or line.startswith('group\t'):
            continue
        p = line.rstrip('\n').split('\t')
        key[p[0]] = p[1]
    if key49:
        key['49'] = key['59'] = key49
    return key


def tokens():
    rows = list(csv.DictReader((l for l in open(TSV, encoding='utf-8') if not l.startswith('#')), delimiter='\t'))
    return [(r['line'], r['kind'], r['value']) for r in rows]


def main():
    key49 = sys.argv[sys.argv.index('--key49') + 1] if '--key49' in sys.argv else None
    key = load_key(key49)
    toks = tokens()
    groups = [v for _, k, v in toks if k == 'group']
    assert [g for gs, *_ in WORDS for g in gs.split()] == groups, 'word division does not cover the groups'
    dec_lines, cur = [], None
    for line, kind, v in toks:
        if line != cur:
            dec_lines.append([line]); cur = line
        dec_lines[-1].append(v.upper() if kind == 'clear' else key.get(v, '[%s]' % v) if key.get(v, '?') != '?' else '[%s]' % v)
    n = ok = 0
    rows = []
    for gs, copy, word, note in WORDS:
        dec = ''.join(key.get(g, '?') if key.get(g, '?') != '?' else '[%s]' % g for g in gs.split())
        if word is None:
            rows.append((gs, '', '', dec, 'not a word', note)); continue
        n += 1
        good = dec == norm(word) and '121' not in gs.split()
        if good and DISPUTED & set(gs.split()):
            good = False
            note = (note + '; ' if note else '') + 'spelt only with 49 = rr, which the copy does not settle: a hole'
        if good:
            ok += 1
            how = 'read: key output matches the copy' if copy else 'read: key output; the copy has no word here'
        else:
            how = 'hole'
        rows.append((gs, copy or '', word, dec, how, note))
    print('key 49/59 =', key['49'])
    for r in rows:
        print('%-46s %-17s %-18s %-20s %s%s' % (r[0], r[1], r[2], r[3], r[4], ('  (' + r[5] + ')') if r[5] else ''))
    print('cipher words %d, read %d, holes %d, read share %.3f' % (n, ok, n - ok, ok / n))
    if key49 is None:
        with open(HERE / 'decryption_CMXV.35.3433.1-2.txt', 'w', encoding='utf-8', newline='\n') as f:
            f.write('# Decryption of CMXV.35.3433.1-2: key.tsv applied to transcription/groups_CMXV.35.3433.1-2.tsv, group by group, '
                    'nothing edited (scripts/decrypt.py). Clear words of the telegram in capitals; a group with no value in brackets.\n')
            for l in dec_lines:
                f.write(l[0] + ': ' + ' '.join(l[1:]) + '\n')
        with open(HERE / 'words_CMXV.35.3433.1-2.tsv', 'w', encoding='utf-8', newline='\n') as f:
            f.write('# Cipher words of CMXV.35.3433.1-2 and how each is counted (scripts/decrypt.py). %d cipher words, %d read, %d holes.\n' % (n, ok, n - ok))
            f.write('groups\tcopy_word\tcompared_with\tkey_output\tcount\tnote\n')
            for r in rows:
                f.write('\t'.join(r) + '\n')
        with open(HERE / 'validation.tsv', 'w', encoding='utf-8', newline='\n') as f:
            f.write('# model: es-modern\n# source: transcription/groups_CMXV.35.3433.1-2.tsv, reading = key.tsv (scripts/decrypt.py)\n'
                    '# note: one group per line, the key output as decrypted (wrong groups keep their key value); 10, 16, 40 and 50 have no value and are left unread; 121 carries cion\n')
            for g in groups:
                v = key.get(g, '?')
                f.write('%s\t%s\n' % (g, '?' if v == '?' else norm(v)))


if __name__ == '__main__':
    main()
