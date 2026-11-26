"""Adapter for docs/_replay.py: key.tsv (Narváez's table) applied to the two transcriptions, against the ```marked
blocks of the two reading files. Each two-digit pair is a unit; the writer divides the runs into words ("|"), so words
are counted over cipher words. In the reading, {x/y} (the signs give x, read y) becomes the marked emendation [y], and
{x} (the key gives x, sense uncertain) becomes [x]. The overstruck pair "0?" has no key value (an open unit)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = True
DOCS = ('DCXXI.3.244.1', 'DCXXI.3.250.2')
SOURCES = {'key': 'key.tsv',
           'transcription': 'transcription_DCXXI.3.244.1.txt, transcription_DCXXI.3.250.2.txt',
           'reading': 'reading_DCXXI.3.244.1.md, reading_DCXXI.3.250.2.md'}
POLYPHONY = {}


def _key():
    k = {}
    for line in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if line.startswith('#') or line.startswith('code\t') or not line.strip():
            continue
        c, p = line.rstrip('\n').split('\t')[:2]
        k[c] = p
    return k


def mechanical():
    k = _key(); out = []
    for doc in DOCS:
        words = []
        for line in open(os.path.join(HERE, f'transcription_{doc}.txt'), encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            groups = line.rstrip('\n').split('\t')[3]
            for w in groups.split('|'):
                words.append([(p, k.get(p)) for p in w.split('-')])
        out.append((doc, words))
    return out


def reading():
    out = {}
    for doc in DOCS:
        s = open(os.path.join(HERE, f'reading_{doc}.md'), encoding='utf-8').read()
        block = s.split('```marked')[1].split('```')[0]
        runs = []
        for line in block.splitlines():
            if ':' not in line:
                continue
            t = line.split(':', 1)[1]
            t = re.sub(r'\{[^}/]*/([^}]*)\}', r'[\1]', t)
            t = re.sub(r'\{([^}]*)\}', r'[\1]', t)
            runs.append(t.strip())
        out[doc] = ' '.join(runs)
    return out
