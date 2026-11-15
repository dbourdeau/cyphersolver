"""Build the key table, the marked decryption and validation.tsv from the transcription and the hand reading.

Inputs:  ../transcription/pass1.txt (printed cipher letters), ../reading/reading_words.tsv (the hand reading divided
         into words; checked letter for letter against ../reading/reading_hand.tsv).
Outputs: ../keys/key_table.tsv, ../reading/decryption.txt, ../validation.tsv

Marks in decryption.txt:
  °  the word rests on at least one letter whose value was chosen by sense: the printed letter carries more than one
     value in this reading, and here it takes either a value other than its commonest one, or its commonest one when
     that covers under 70% of its uses (printed s, r, o, v, c, which have no dominant value).
  †  weak: the word needs a printed letter read against the print (a misprint assumed) or a value found nowhere
     else: "by" (printed g read as q), "gouuernor" (printed q read as g), "relligion" in A10 (printed r = r),
     "some" in A7 (printed c = m), and "he will", which takes the printed roman "to" as cipher.
  ?  a printed cipher letter not read.
Usage: python3 -I make_reading.py
"""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import poly
A = 'abcdefghiklmnopqrstuwxyz'
ROOT = os.path.join(HERE, '..')
segs, labels = poly.read_ct(os.path.join(ROOT, 'transcription', 'pass1.txt'))
hand = dict(l.split('\t') for l in open(os.path.join(ROOT, 'reading', 'reading_hand.tsv')).read().splitlines()[1:])
words = dict(l.split('\t') for l in open(os.path.join(ROOT, 'reading', 'reading_words.tsv')).read().splitlines()[1:])
for k in labels:
    assert words[k].replace(' ', '') == hand[k].lower(), k

def cipher_of(c):            # printed u is cipher n, printed v is cipher u (pass2.txt, note 8)
    return {'u': 'n', 'v': 'u'}.get(c, c)

PREF = (7, 8, 10, 11, 20)
def shift(c, p):             # printed u may also be cipher u (B2 "comandinge"); take the reading in the usual shifts
    cands = [(A.index(p) - A.index(cc)) % 24 for cc in ({'u': ['n', 'u']}.get(c) or [cipher_of(c)])]
    return sorted(cands, key=lambda k: (k not in PREF, k))[0]

vals = collections.defaultdict(collections.Counter)
for lab, s in zip(labels, segs):
    for c, p in zip(s, words[lab].replace(' ', '')):
        if p != '?': vals[c][p] += 1

def by_sense(c, p):
    v = vals[c]
    if len(v) < 2: return False
    top, n = v.most_common(1)[0]
    return p != top or n < 0.7 * sum(v.values())

WEAK = {('A9.0', 'by'), ('A9.0', 'gouuernor'), ('A10.1', 'relligion'), ('A7.0', 'some')}

# key table
with open(os.path.join(ROOT, 'keys', 'key_table.tsv'), 'w') as f:
    f.write('# Printed cipher letter -> plain values in the reading, with the shift each needs on the 24-letter alphabet\n'
            '# (a b c d e f g h i k l m n o p q r s t u w x y z). Base shift 7: cipher a = plain h. Printed u is taken\n'
            '# as cipher n and printed v as cipher u (letters confused in reading a secretary hand). Counts are over the\n'
            '# 636 read letters (the printed "to" in A10 is not included). "multi" = more than one value in the reading.\n')
    f.write('printed\tbase_value(shift7)\tvalues_in_reading (plain:count:shift)\tmulti\n')
    for c in sorted(vals):
        base = A[(A.index(cipher_of(c)) + 7) % 24]
        vs = ', '.join(f'{p}:{n}:{shift(c, p)}' for p, n in vals[c].most_common())
        f.write(f'{c}\t{base}\t{vs}\t{"yes" if len(vals[c]) > 1 else ""}\n')

# marked decryption
out = ['# Decryption of the printed cipher, segment by segment (labels as in transcription/pass1.txt).',
       '# Line 1 the printed letters, line 2 the plain letter each is read as, line 3 the words.',
       '# Marks: ° value chosen by sense among the values the printed letter carries in this reading;',
       '#        † weak (a misprint assumed, or a single value found nowhere else); ? not read.',
       '# The roman "to" printed between A10.0 and A10.1 is read as cipher e w ("that he will"); see NOTES.', '']
nsense = nweak = nread = nunread = 0
for lab, s in zip(labels, segs):
    plain = words[lab].replace(' ', '')
    out.append(f'{lab}  ' + ' '.join(s))
    out.append(' ' * (len(lab) + 2) + ' '.join(plain))
    i = 0; ws = []
    for w in words[lab].split():
        cs = s[i:i + len(w)]; i += len(w)
        if '?' in w:
            nunread += 1; ws.append(w); continue
        nread += 1
        m = ''
        if any(by_sense(c, p) for c, p in zip(cs, w)): m += '°'; nsense += 1
        if (lab, w) in WEAK: m += '†'; nweak += 1
        ws.append(w + m)
    out.append(' ' * (len(lab) + 2) + ' '.join(ws))
    out.append('')
out.append(f'# words read {nread}, unread runs {nunread}; words marked ° {nsense}, marked † {nweak} '
           f'(plus "he will" across the printed "to", counted in A10.0 "that h" and A10.1 "ill")')
open(os.path.join(ROOT, 'reading', 'decryption.txt'), 'w').write('\n'.join(out) + '\n')

# validation.tsv for docs/_validate.py
with open(os.path.join(ROOT, 'validation.tsv'), 'w') as f:
    f.write('# model: en-1640s\n# source: transcription/pass1.txt paired with reading/reading_words.tsv (scripts/make_reading.py)\n'
            '# note: printed letters as tokens (printed u and v kept as printed); unread letters ?; the printed "to" and the person signs left out\n')
    for lab, s in zip(labels, segs):
        for c, p in zip(s, words[lab].replace(' ', '')):
            f.write(f'{c}\t{p}\n')
print('words read', nread, 'unread runs', nunread, 'sense', nsense, 'weak', nweak)
