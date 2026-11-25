"""Adapter for docs/_replay.py: key.tsv applied to transcription.txt (first reading of every [a/b]), against the
marked text in reading.md (between the <!-- replay --> comments). Each cipher letter is a unit; the groups do not mark
word division, so words are counted over the words of the reading."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key.tsv', 'transcription': 'transcription.txt', 'reading': 'reading.md'}
POLYPHONY = {}


def _key():
    k = {}
    for line in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if line.startswith('#') or line.startswith('cipher\t') or not line.strip():
            continue
        c, p = line.split('\t')[:2]
        k[c] = p
    return k


def mechanical():
    k = _key(); words = []
    for line in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        groups = re.sub(r'\[(\w)/\w\]', r'\1', line.rstrip('\n').split('\t')[1]).replace('/', '')
        for g in groups.split():
            words.append([(ch, k.get(ch)) for ch in g])
    return [('telegram', words)]


def reading():
    s = open(os.path.join(HERE, 'reading.md'), encoding='utf-8').read()
    t = s.split('<!-- replay -->')[1].split('<!-- /replay -->')[0]
    return {'telegram': ' '.join(t.split())}
