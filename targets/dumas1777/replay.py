"""Adapter for docs/_replay.py: key/key_positions.json applied to transcriptions/reconciled/*.txt (the principal
copies), against the cipher passages of letters/*_text.txt.

One number is one character of the key text (a letter, or a stop, comma, apostrophe, hyphen, & or the reference
mark). The cipher runs on without word division, so words are counted over the reading. Only the words between
the cipher marks of the reading files are compared; the clear words around them are not in the transcription.

Marks of the reading files, as the replay sees them: {+x} (a letter from another cipher copy or from the decipherer's
letter over the number), a {-y}{+x} pair and [x] are all marked emendations; a blotted number (#) and a number out
of range have no key value. The guessed "&" of 20 Sept 1779 is passed as an unread hole. A {-x} sign that the
reading drops with nothing in its place (the b of "d b espagne", the stray z after "Congress") is shown to the
replay by bracketing the letter next to it, so that the word is classed as a marked emendation. The copy-only
phrase of 30 April 1776 and the second copy of the 17 Aug 1778 heading are left out: the replay covers the 4,503
number places of the principal copies.
"""
import os, re, json, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key/key_positions.json', 'transcription': 'transcriptions/reconciled/<id>.txt',
           'reading': 'letters/<id>_text.txt'}
POLYPHONY = {'28': ['k']}    # the key text has no k: Dumas writes c ("cing of Prussia")

# reading file stem -> reconciled files, in the order of the reading
DOCS = [
    ('1776-04-30_letter-and-extrait', ['1776-04-30']),
    ('1776-05-14_B', ['1776-05-14']),
    ('1776-08-10_C-extract', ['1776-08-10']),
    ('1776-09-01_D-and-suite-1776-10-10', ['1776-09-01']),
    ('1777-04-12_E-extract', ['1777-04-12']),
    ('1777-08-02_N', ['1777-08-02']),
    ('1777-08-14_to-Franklin-extract', ['1777-08-14']),
    ('1777-09-25_R_and_1777-10-14_S', ['1777-09-25', '1777-10-14']),
    ('1777-11-04_T', ['1777-11-04']),
    ('1777-11-28_V_2d-extraits', ['1777-11-28']),
    ('1778-02-24_B2-C2', ['1778-02-24']),
    ('1778-04-27_H2-D2', ['1778-04-27']),
    ('1778-06-14_N2-M2', ['1778-06-14']),
    ('1778-07-31_names-left-blank', ['1778-07-31']),
    ('1778-08-17_to-Van-Berckel', ['1778-08-17']),
    ('1779-05_Q3-R3_and-S3', ['1779-05', '1779-05-after17', '1779-06-21']),
    ('1779-09-20_N4-Z3', ['1779-09-20']),
    ('1781-09-02_F6-PS', ['1781-09-02']),
]


def _key():
    pos = json.load(open(os.path.join(HERE, 'key', 'key_positions.json'), encoding='utf8'))['positions']
    return {k: unicodedata.normalize('NFD', v)[0].lower() for k, v in pos.items()}


def mechanical():
    key = _key()
    out = []
    for stem, files in DOCS:
        word = []
        for f in files:
            for line in open(os.path.join(HERE, 'transcriptions', 'reconciled', f + '.txt'), encoding='utf8'):
                m = re.match(r"\s*[A-Za-z0-9']+:\s*(.*)$", line)
                if line.startswith('#') or not m:
                    continue
                body = re.sub(r'\{[^}]*\}|\[[^\]]*\]', ' ', m.group(1))   # plain signs in a run, struck numbers
                for t in body.split():
                    t = t.rstrip('*')
                    if t == '#':
                        word.append(('#', None))                           # a blotted number
                    elif t.isdigit():
                        word.append((t, key.get(t)))                       # None when out of range (698)
        out.append((stem, [word]))
    return out


def reading():
    out = {}
    for stem, files in DOCS:
        txt = open(os.path.join(HERE, 'letters', stem + '_text.txt'), encoding='utf8').read()
        txt = txt.split('## Reading', 1)[1].split('## Notes', 1)[0]
        txt = '\n\n'.join(p for p in txt.split('\n\n') if not p.lstrip().startswith('Copy only'))
        spans = re.findall(r'⟦([^⟧]*)⟧', txt)
        if stem.startswith('1778-08-17'):
            spans = spans[:1]                          # the second copy of the heading (image 201) is not replayed
        if stem.startswith('1779-05'):
            spans.append(spans[-1])                    # the same 17 numbers in the letters of [after 17 May] and 21 June
        s = ' '.join(spans)
        s = s.replace('[&]', ' # ')                                        # the guessed sign: unread
        s = re.sub(r'\{-[^}]*\}\{\+([^}]*)\}', r'[\1]', s)                 # a letter replaced
        s = re.sub(r'\{\+([^}]*)\}\{-[^}]*\}', r'[\1]', s)
        s = re.sub(r'\{\+([^}]*)\}', r'[\1]', s)                           # a letter from another copy or the gloss
        s = re.sub(r'(\w)\s+\{-[^}]*\}', lambda m: '[' + m.group(1) + ']', s)   # a stray sign after a word
        s = re.sub(r"\{-[^}]*\}(\W*)(\w)", lambda m: m.group(1) + '[' + m.group(2) + ']', s)   # a stray sign in a word
        out[stem] = s
    return out
