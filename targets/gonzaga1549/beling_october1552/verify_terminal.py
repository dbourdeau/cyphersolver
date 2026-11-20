"""Reproduce the registered terminal comparison and verify its full control ledger."""
import io
import csv
import difflib
import hashlib
import json
import random
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEY = HERE.parents[1] / 'figueroa1534/validation/K4.tsv'
PLATES = HERE / 'shape_index.tsv'
TARGET = 'y hasta saber particularmente todo lo del estado del negocio estaremos con el cuydado que es razon'


def rows(path):
    with path.open() as source:
        yield from csv.DictReader((s for s in source if not s.startswith('#')), delimiter='\t')


def normalized(raw):
    unaccented = unicodedata.normalize('NFD', raw.lower())
    return ''.join(c for c in unaccented if c.isalpha() or c == '#').translate(str.maketrans('vj', 'ui'))


def suffix_score(text, target):
    # Distances to every prefix of the reversed target = distances to its suffixes.
    line = list(range(len(target) + 1))
    for i, char in enumerate(reversed(text), 1):
        next_line = [i]
        for j, goal in enumerate(reversed(target), 1):
            next_line.append(min(line[j] + 1, next_line[-1] + 1, line[j-1] + (char != goal)))
        line = next_line
    return max((1 - d / max(len(text), j), j) for j, d in enumerate(line) if j)


def main():
    vals = defaultdict(set)
    for row in rows(KEY):
        vals[row['label']].update(row['valeur'].split('|'))
    labels = sorted(vals)
    visual = defaultdict(set)
    for r in rows(PLATES):
        for name in [r['visual_name'], r['number'], r['plate'] + r['number']]:
            visual[name].add(r['published_label'])
    readers = defaultdict(list)
    for r in rows(HERE / 'reader_inputs.tsv'):
        if r['status'] == 'terminal-punctuation':
            continue
        raw = r['label']
        valid = set(visual.get(raw, []))
        if raw in vals:
            valid.add(raw)
        label = next(iter(valid)) if r['status'] == 'certain' and len(valid) == 1 else None
        readers[r['reader']].append(label or ('hole', r['reader'], r['index']))
    a, b = readers.values()
    consensus = []
    matching = 0
    for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal':
            matching += j-i
            consensus.extend(a[i:j])
        else:
            consensus.extend([None] * max(j-i, l-k))
    target = normalized(TARGET)
    def evaluate(table):
        chars = []
        for label in consensus:
            options = table.get(label, set())
            val = next(iter(options)) if len(options) == 1 else '#'
            chars.append('' if val == 'NUL' else normalized(val))
        expansion = ''.join(chars)
        score, size = suffix_score(expansion, target)
        return expansion, score, target[-size:]
    expansion, score, suffix = evaluate(vals)
    rng = random.Random(1552100634)
    ledger = []
    for i in range(1000):
        sets = [vals[label] for label in labels]
        rng.shuffle(sets)
        control, sim, ending = evaluate(dict(zip(labels, sets)))
        ledger.append((i+1, control, sim, ending))
    with io.StringIO() as dest:
        writer = csv.writer(dest, delimiter='\t', lineterminator='\n')
        writer.writerow(['iteration', 'expansion', 'similarity', 'suffix'])
        writer.writerows(ledger)
        assert dest.getvalue() == (HERE/'controls.tsv').read_text()
    tie = sum(s == score for _, _, s, _ in ledger)
    beat = sum(s > score for _, _, s, _ in ledger)
    votes = matching / len(consensus) if consensus else 0
    known = len(expansion.replace('#', ''))
    result = dict(reader_lengths=[len(a), len(b)], matching=matching, total=len(consensus),
                  agreement=votes, consensus=consensus, expansion=expansion, score=score,
                  known=known, suffix=suffix, ties=tie, beat=beat, max_control=max(r[2] for r in ledger),
                  passed=votes >= .60 and score >= .75 and known >= 6 and tie+beat <= 9,
                  controls=len(ledger), key_sha256=hashlib.sha256(KEY.read_bytes()).hexdigest())
    assert result == json.loads((HERE/'terminal_result.json').read_text())
    print(f'{matching}/{len(consensus)} agree. {expansion}, similarity {score:.2f}. Of 1,000 controls, {beat} beat and {tie} tie. Pass: {result["passed"]}.')


if __name__ == '__main__':
    main()
