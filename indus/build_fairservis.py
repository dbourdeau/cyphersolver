"""Build bench keys from the Fairservis 1992 transcription (keys/fairservis1992_raw.tsv).

The value is Fairservis's Dravidian equivalent: the first alternative before ' / ' or ';', the
'hom:' (homophone) column dropped, brackets removed but their letters kept (kavadi(y)an ->
kavadiyan). An ICIT id matched to two of his signs keeps the first.

keys/fairservis1992.tsv       signs matched 'sure' or 'likely' (the main key)
keys/fairservis1992_wide.tsv  also the 'unsure' ones, with the first candidate id

Usage: python build_fairservis.py
"""
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def value(v):
    v = v.split('hom:')[0]
    v = re.split(r'\s*/\s*|;', v)[0]
    v = v.replace('(', '').replace(')', '').replace('?', '').strip().strip(',').strip()
    return v.split()[0] if v.split() else ''


def main():
    raw = os.path.join(HERE, 'keys', 'fairservis1992_raw.tsv')
    rows = [r for r in csv.DictReader((ln for ln in open(raw, encoding='utf-8') if not ln.startswith('#')),
                                      delimiter='\t')]
    for name, ok in (('fairservis1992', ('sure', 'likely')), ('fairservis1992_wide', ('sure', 'likely', 'unsure'))):
        key = {}
        for r in rows:
            if r['confidence'] not in ok or not r['icit'].strip():
                continue
            g = r['icit'].split('|')[0].strip()
            v = value(r['value'])
            if g and v and g not in key:
                key[g] = (v, '%s %s' % (r['fcode'], r['gloss'][:80]))
        title = ('Fairservis 1992, The Harappan Civilization and its Writing, Appendix A' +
                 ('' if name == 'fairservis1992' else ' (with unsure matches)'))
        with open(os.path.join(HERE, 'keys', name + '.tsv'), 'w', encoding='utf-8') as f:
            f.write('# %s\n' % title)
            f.write('# language: dra. Built by build_fairservis.py from keys/fairservis1992_raw.tsv (%s matches); '
                    'value = his Dravidian equivalent, first alternative.\n' % '/'.join(ok))
            f.write('# sign\tvalue\tgloss\n')
            for g in sorted(key, key=int):
                f.write('%s\t%s\t%s\n' % (g, key[g][0], key[g][1]))
        print(name, len(key), 'signs')


if __name__ == '__main__':
    main()
