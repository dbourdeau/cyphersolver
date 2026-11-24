"""Adapter for docs/_replay.py: key/we025_crawford1814.tsv applied to crawford1814_transcription.txt, against
crawford1814_reading.md.

The decode rule is decode.py's: each group gives its WE025 element with Crawford's marks applied (' adds s, ^ adds
ed or d, _r/_rr/_rrr and _y drop one to three final letters), and decode.py's SPECIAL table gives the letters where the
mark rule alone does not (read from decode.py's source, not run). The nine groups decode.py lists in GUESSED are given
their table value with the marks applied, so that the reading's bracketed word shows against it. Element 509 is printed
"u. V" in the table (one letter in its two forms) and is taken as u. The clear words written among the groups are
passed through as anchor text and are not counted; the clear text the transcription leaves out and the reading's [...]
(clear text not given there) are not compared. One clear word is passed as the reading has it, "very" (64R01) as
"every" (a silent mending listed in NOTES.md section 3): passed as written, the aligner charges the added e to the cipher
word before it, sa-cri-fice, which the key gives exactly; clear words are not counted either way. The groups run on without word division (a group is a word or a
syllable), so words are counted over the words of the reading that the groups carry.
"""
import ast, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key/we025_crawford1814.tsv', 'transcription': 'crawford1814_transcription.txt',
           'reading': 'crawford1814_reading.md'}
POLYPHONY = {}
SECTIONS = ('64R', '65R', '66L')
CLEAR_AS_READ = {('64R01', 'very'): 'every'}


def _decode_tables():
    """SPECIAL and GUESSED as decode.py defines them."""
    out = {}
    for node in ast.parse(open(os.path.join(HERE, 'decode.py'), encoding='utf-8').read()).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and getattr(node.targets[0], 'id', '') in ('SPECIAL', 'GUESSED'):
            out[node.targets[0].id] = ast.literal_eval(node.value)
    return out['SPECIAL'], out['GUESSED']


def _element(el, marks):
    m = re.search(r'_(r+|y)', marks)
    if m:
        el = el[:-len(m.group(1))]
    if "'" in marks:
        el += 's'
    if '^' in marks:
        el += 'd' if el.endswith('e') else 'ed'
    return el


def mechanical():
    T = {}
    for i, l in enumerate(open(os.path.join(HERE, 'key', 'we025_crawford1814.tsv'), encoding='utf-8')):
        if i:
            n, el, _ = l.rstrip('\n').split('\t')
            T[n] = 'u' if el == 'u. V' else el
    special, guessed = _decode_tables()
    words = {s: [] for s in SECTIONS}
    for line in open(os.path.join(HERE, 'crawford1814_transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or ':' not in line:
            continue
        lab, body = line.rstrip('\n').split(':', 1)
        body = re.sub(r'\[struck:[^\]]*\]', ' ', body)
        w = words[lab[:3]]
        for tok in re.findall(r'"[^"]*"|\d+[\'^+_ry?]*', body):
            if tok.startswith('"'):
                w.append((None, CLEAR_AS_READ.get((lab, tok.strip('"')), tok.strip('"'))))
                continue
            num = re.match(r'\d+', tok).group()
            marks = tok[len(num):].replace('?', '')
            if (lab, num) in special and (lab, num) not in guessed:
                v = special[(lab, num)]
            else:
                v = _element(T[num], marks)
            w.append((num + marks, v))
    return [(s, [words[s]]) for s in SECTIONS]


def reading():
    txt = open(os.path.join(HERE, 'crawford1814_reading.md'), encoding='utf-8').read()
    R = {}
    for s in SECTIONS:
        sec = txt.split('## 00' + s, 1)[1].split('\n## ', 1)[0]
        sec = sec.split('\n', 1)[1]                  # the heading line
        R[s] = sec.replace('[...]', ' ')
    return R
