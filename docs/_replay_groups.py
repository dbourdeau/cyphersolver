"""Shared adapter parts for docs/_replay.py: numeric code groups, a key.tsv and an "Established text" reading.md.

The layout of bouille1778, damas1787, blathwayt1729, partyet1721 and their like (tried on those four on 16 Nov 2026;
no adapter is committed in their folders: they are a contributor's readings, and marking them is his to agree):

    key.tsv            group<TAB>value[<TAB>...]; '#' lines are comments. A value may carry a count ("a×34"), several
                       values ("a×34 | à×2", "u/ou/v") or a query ("arme(?)"); the first is taken. A value with no
                       letter in it (".", "—", "[nom non glosé]") is a group the key does not read.
    transcription.txt  groups separated by dots or spaces, one manuscript line per line, an optional "label<TAB>" in
                       front; '#' lines are comments. Anything that is not a group (clear words, "/", "|") is skipped.
    reading.md         "# Established text ..." then prose. {x} = probable and [x] = restored by the sense (both are
                       marks: not what the key gives); ‹n› or ‹…› = unresolved; ‹clear: ...› and <...> = clear text of
                       the original, left out here because the transcription does not repeat it. ⟦x⟧ = what the key
                       gives for a group that the text leaves out (written in by docs/_replay_mark.py). A line that
                       begins "Conventions" is not text.

A target's replay.py is then:

    from _replay_groups import make
    DIVIDED, POLYPHONY, SOURCES, mechanical, reading = make(__file__)

with keyword arguments where the folder differs (see make()).
"""
import os, re

STOP = ('State of the reading', 'Justifications', 'Tables', 'Modern', 'Probable words', 'Conventions', 'English', 'Translation')
EOL = chr(13) + chr(10)


def load_key(path, nulls=()):
    key = {}
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or '\t' not in line:
            continue
        code, val = [x.strip() for x in line.rstrip(EOL).split('\t')[:2]]
        if not code:
            continue
        val = re.split(r'\s*\|\s*', val)[0]
        val = re.sub(r'×\d+$', '', val).strip()
        val = re.sub(r'\(\?\)$', '', val).strip()
        val = val.split('/')[0].strip() if re.fullmatch(r"[^\W\d_]+(/[^\W\d_]+)+", val) else val
        if val.lower().strip('()') in ('null', 'nul', 'nulle'):
            key[code] = ''
        elif val.startswith('[') or not re.search(r'[^\W\d_]', val):
            key[code] = None
        else:
            key[code] = val
    for n in nulls:
        key[str(n)] = ''
    return key


def groups(path):
    """-> [(section heading or '', [group, ...])]; a '## ' comment line opens a section."""
    out = [('', [])]
    for line in open(path, encoding='utf8'):
        line = line.rstrip(EOL)
        if line.startswith('## '):
            out.append((line[3:].strip(), [])); continue
        if line.startswith('#') or not line.strip():
            continue
        if '\t' in line:
            line = line.split('\t', 1)[1]
        line = re.sub(r'\([^)]*\)|\[[^\]]*\]|<[^>]*>', ' ', line)          # clear words written into the line
        for t in re.split(r'[.\s]+', line):
            t = t.strip('_,;:')
            if re.fullmatch(r'\d+\??', t):
                out[-1][1].append(t)
    return [(h, g) for h, g in out if g]


def established(path, drop=('Clear opening',), stop=STOP, keep=None):
    """The prose of reading.md in the engine's conventions ([x] marked, # unread), as a string of the same length as
    the file: whatever is not compared (headings, dropped sections, clear text) is blanked, so that a position in the
    string is a position in the file (docs/_replay_mark.py writes marks back by position)."""
    txt = open(path, encoding='utf8', newline='').read()
    out = list(txt)

    def blank(a, b, first=None):
        for i in range(a, b):
            if out[i] not in EOL:
                out[i] = ' '
        if first is not None and b > a:
            out[a] = first

    def each(pattern, first=None, flags=0):
        for m in re.finditer(pattern, ''.join(out), flags):
            blank(m.start(), m.end(), first)
    start = txt.find('# Established text')
    start = txt.find(chr(10), start) + 1 if start >= 0 else 0
    blank(0, start)
    heads = [(m.start(), m.end(), m.group(1).strip()) for m in re.finditer(r'^## (.*)$', txt, re.M) if m.start() >= start]
    bounds = [(start, start, '')] + heads + [(len(txt), len(txt), None)]
    stopped = False
    for (a, e, name), (na, _, _) in zip(bounds, bounds[1:]):
        blank(a, e)
        stopped = stopped or any(name.startswith(x) for x in stop)
        if stopped or any(name.startswith(d) for d in drop) or (keep and name and not any(name.startswith(k) for k in keep)):
            blank(e, na)
    each(r'^Conventions.*$', flags=re.M)
    each(r'‹clear:[^›]*›')
    each(r'‹[^›]*›', first='#')
    each(r'<[^>\r\n]*>')
    each(r'\*\*|__')
    return ''.join(out).replace('{', '[').replace('}', ']').replace('⟦', '[').replace('⟧', ']')


def make(file, key='key.tsv', transcription='transcription.txt', reading_file='reading.md', nulls=(), polyphony=None,
         label='text', **kw):
    here = os.path.dirname(os.path.abspath(file))

    def mechanical():
        k = load_key(os.path.join(here, key), nulls)
        word = [(g, None if g.endswith('?') else k.get(g)) for _, gs in groups(os.path.join(here, transcription)) for g in gs]
        return [(label, [word])]

    def reading():
        return {label: established(os.path.join(here, reading_file), **kw)}
    reading.path = os.path.join(here, reading_file)          # position-faithful: see established()
    return False, dict(polyphony or {}), {'key': key, 'transcription': transcription, 'reading': reading_file}, mechanical, reading
