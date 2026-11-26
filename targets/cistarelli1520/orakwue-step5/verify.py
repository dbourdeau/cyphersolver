from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
key = dict(line.split('\t') for line in (HERE / 'key.tsv').read_text(encoding='utf-8').splitlines()[1:])


def replay(text):
    output = []
    total = unresolved = 0
    for part in re.split(r'(\[[^\]]+\])', text):
        if part.startswith('['):
            output.append(part)
            continue
        values = [key.get(token.rstrip('?'), '?') for token in part.split()]
        total += len(values)
        unresolved += values.count('?')
        if values:
            output.append(''.join(values).upper())
    return ' '.join(output), total, unresolved


def main():
    output = []
    total = unresolved = 0
    for name in ('r1137_transcription.txt', 'v1908_transcription.txt'):
        for line in (HERE.parent / name).read_text(encoding='utf-8').splitlines():
            if not re.match(r'^(P2|V) L', line):
                continue
            label, text = line.split(': ', 1)
            decoded, positions, holes = replay(text)
            output.append(f'{label}: {decoded}')
            total += positions
            unresolved += holes
    literal = (HERE / 'literal.txt').read_text(encoding='utf-8').splitlines()
    if output != [line for line in literal if line]:
        raise SystemExit('The replay differs from the filed literal output.')
    print(f'{len(output)} rows, {total - unresolved}/{total} assigned, {unresolved} unassigned')


if __name__ == '__main__':
    main()
