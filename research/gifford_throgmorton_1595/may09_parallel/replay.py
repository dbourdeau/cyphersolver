"""Replay fixed May predictions and scores from published ciphertext and witness slots."""
import argparse
from collections import Counter
import csv
from hashlib import sha256
import io
from pathlib import Path
import random
import re

HERE = Path(__file__).resolve().parent
INPUTS = {
    'may09/boxes.tsv': 'f8c1af095ed07186fe78fcba7a064e9642f9cbd5cc247e2318632d9f420a6557',
    'may09/reader_a.tsv': '1fca674af9734431769658aa959dcb2a505a39b5b98df281c64fe5ec770e4af6',
    'may09/reader_b.tsv': '5660bd337eebc5a43092abdf3e44cace5c8e26742b8bb49c2b69407d7c900f99',
    'june/alphabet.tsv': 'c4a4667d47849f48dc1c7635e234534c4c42317628af60e1d1139df3b27aff96',
}
EXCLUSIONS = {'T08', 'T09', 'T10', 'M10', 'M15'}
SLOTS_SHA = '8cc838391607827ffdc5121e76fb3e2ee0072c91cf94f3a7bf2690d0584c6d01'
OUTCOME_SHA = '9f829bfc012ce17035746b8a4bf473c9dec242101424661f0b8770926cda06e2'
CONTROLS_SHA = '7daa826ccdad6f01d4c561df64e2b1fa6301b43954ac115976a7c08734250fce'


def read_rows(path, digest):
    data = path.read_bytes().replace(b'\r\n', b'\n')
    if sha256(data).hexdigest() != digest:
        raise ValueError(f'Unexpected file contents in {path.name}')
    return list(csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t'))


def fold(value):
    return value.upper().replace('J', 'I').replace('U', 'V')


def tsv(header, rows):
    stream = io.StringIO()
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(header)
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--research', type=Path, default=HERE.parent,
                        help='directory containing the may09 and june folders')
    parser.add_argument('--output', type=Path, help='new directory for the two replayed TSV files')
    args = parser.parse_args()
    data = {name: read_rows(args.research / name, h) for name, h in INPUTS.items()}
    order = [r['group'] for r in data['may09/boxes.tsv']]
    readings = [{r['group']: fold(r['reading']) for r in data['may09/' + f]}
                for f in ('reader_a.tsv', 'reader_b.tsv')]
    assert len(order) == len(set(order)) == 34
    assert all(set(table) == set(order) for table in readings)
    key, = [r for r in data['june/alphabet.tsv'] if r['marker'] == '2']
    alphabet = key['header']
    decode = str.maketrans(key['shift_row'], alphabet)
    slots = {r['group']: r for r in read_rows(HERE / 'witness_slots.tsv', SLOTS_SHA)}
    words = []
    outcomes = []
    for group in order:
        a, b = [r[group] for r in readings]
        if group in EXCLUSIONS or a != b or not re.fullmatch('[' + alphabet + ']+2', a):
            continue
        prediction = a[:-1].translate(decode)
        r = slots[group]
        reference = r['reference']
        status = 'unmapped'
        if reference:
            words.append((prediction, fold(reference)))
            status = 'exact' if prediction == fold(reference) else 'mismatch'
        outcomes.append((group, a, prediction, reference, r['folio'], r['line'], r['token'], status))
    assert set(r[0] for r in outcomes) == set(slots)
    exact = {pred for pred, ref in words if pred == ref}
    letters = sum(map(len, exact))
    rng = random.Random(15950509)
    counts = []
    for _ in range(1000):
        permutation = list(alphabet)
        rng.shuffle(permutation)
        remap = str.maketrans(alphabet, ''.join(permutation))
        counts.append(len({ref for pred, ref in words if pred.translate(remap) == ref}))
    status = 'pass' if len(exact) >= 3 and letters >= 12 and len(exact) > max(counts) else 'miss'
    outputs = {
        'outcome.tsv': (tsv(['group','cipher','prediction','reference','folio','line','token','status'],
                            outcomes), OUTCOME_SHA),
        'controls.tsv': (tsv(['replicate','distinct_exact'], enumerate(counts, 1)), CONTROLS_SHA),
    }
    for filename, (data_bytes, digest) in outputs.items():
        if sha256(data_bytes).hexdigest() != digest:
            raise ValueError(f'Replay differs from {filename}')
    if args.output:
        args.output.mkdir(parents=True, exist_ok=False)
        for filename, (data_bytes, _) in outputs.items():
            (args.output / filename).write_bytes(data_bytes)
    print(outputs['outcome.tsv'][0].decode(), end='')
    print(f'{status}: {len(exact)} distinct whole words, {letters} letters, '
          f'{len(words)} mapped. Controls: {dict(sorted(Counter(counts).items()))}.')


if __name__ == '__main__':
    main()
