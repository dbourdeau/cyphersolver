"""Adapter for docs/_replay.py: key.txt applied to transcription_item109.txt, against reading.md.

The key is Dana's table as key.txt holds it: three alphabets used in turn in the order of his sheet (N, W, I in
key.txt's naming; his columns W, a, r) and a list of word numbers. His rule: a number above 27 starts the key word
again. The transcription used is the clerk's copy (PCC item 109), because it has all 215 numbers; the triplicate
(transcription.txt) has the same 208 numbers and lacks seven at the frame edge.

Two places where the key columns do not follow the rule are written in here, because without them nothing after
them decodes. Both are marked in the reading, so the replay shows them:
  PHASE_29   29 is not in the table. It is taken to stand in a letter place and to use one key column (the first).
             The replay gives it no value; the reading has [I].
  SKIP_AFTER one key column is passed over after the 134th number (the 7 that is the b of "irresistab"). The reading
             marks the two letters that follow, irresistab[le].
No letter is corrected here: where Dana used the wrong column (three places) the key's own letter stands (r, g, s)
and the reading's letter is in brackets. A unit is named by key letter and number (W23 = 23 in the W row of key.txt).
The cipher runs on without word division, so words are counted over the reading.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = False
SOURCES = {'key': 'key.txt', 'transcription': 'transcription_item109.txt', 'reading': 'reading.md'}
POLYPHONY = {}
LABEL = 'no23'
ALPHA = 'abcdefghijklmnopqrstuvwxyz&'
ORDER = 'NWI'            # the order of the columns on Dana's sheet
SKIP_AFTER = 134         # 1-based position in the 215 numbers


def load_key():
    rows, words = {}, {}
    for line in open(os.path.join(HERE, 'key.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        m = re.match(r'^([WIN])\s*:(.*)$', line)
        if m:
            nums = [int(x) for x in m.group(2).split()]
            assert len(nums) == 27, line
            rows[m.group(1)] = {n: ALPHA[i] for i, n in enumerate(nums)}
            continue
        m = re.match(r'^(.*?)\s{2,}(\d+)\s+(\d+)\s+(\d+)\s*$', line.rstrip())
        if m:
            name = re.sub(r'\s*\(.*?\)', '', m.group(1)).strip()      # "Osterman (Count)" -> Osterman
            for n in m.group(2, 3, 4):
                words[int(n)] = name
    assert set(rows) == set('WIN') and len(words) == 78 * 3, (sorted(rows), len(words))
    return rows, words


def numbers():
    out = []
    for line in open(os.path.join(HERE, 'transcription_item109.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        out += [int(t.rstrip('.')) for t in line.split()]
    assert len(out) == 215 and out[SKIP_AFTER - 2:SKIP_AFTER + 1] == [15, 7, 26], out[SKIP_AFTER - 2:SKIP_AFTER + 1]
    return out


def mechanical():
    rows, words = load_key()
    word, pos = [], 0
    for i, n in enumerate(numbers(), 1):
        if n == 29:                                  # PHASE_29: no value, one key column used
            word.append(('29', None)); pos += 1
        elif n > 27:                                 # a word number: the key word starts again
            word.append((str(n), words.get(n))); pos = 0
        else:
            k = ORDER[pos % 3]
            word.append((k + str(n), rows[k][n])); pos += 1
        if i == SKIP_AFTER:
            pos += 1
    return [(LABEL, [word])]


def reading():
    txt = ''.join(l for l in open(os.path.join(HERE, 'reading.md'), encoding='utf-8') if not l.startswith('#'))
    return {LABEL: txt}


if __name__ == '__main__':
    # python replay.py > decryption_item109.txt : the key's output line by line, nothing corrected
    units = mechanical()[0][1][0]
    print('# Dana to Livingston, St Petersburg, 6 Apr 1783 (O.S.), No. 23: key.txt applied to transcription_item109.txt,')
    print('# number by number, with nothing corrected. Output of python replay.py. Lines as in the clerk\'s copy.')
    print('# Key columns in the order of Dana\'s sheet (N, W, I in key.txt; his W, a, r); a number above 27 starts the key')
    print('# word again. [29] has no value in the table. Two key-column events are written in (replay.py): 29 uses one')
    print('# column, and one column is passed over after the 134th number (the b of irresistab).')
    print('# Where Dana used the wrong column the key\'s own letter stands: whichrs (is), ang (any), influsnce (influence).')
    i = 0
    for n, line in enumerate((l for l in open(os.path.join(HERE, 'transcription_item109.txt'), encoding='utf-8')
                              if l.strip() and not l.startswith('#')), 1):
        toks = [t.rstrip('.') for t in line.split()]
        out = ''
        for _ in toks:
            unit, value = units[i]; i += 1
            out += value if value is not None and len(value) == 1 else '[%s]' % (value or unit)
        print('L%-2d %s' % (n, ' '.join(toks)))
        print('    ' + out)
