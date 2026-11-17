"""Apply the rebuilt Guaras key to the 20-line blind sample and print each line beside Lettenhove's printed words.

  python research/vetting_2026-11-17_ajbeling/1001/decode_sample.py

Standard library only; deterministic. Reads key.json, sample_20_lines_blind.txt and lettenhove_1888_sample_lines.tsv
from this folder. Notation of the sample: one sign per token; '|' is a comma or dot of the manuscript, '~' a doubtful
boundary; '?' a sign the two readers did not agree on; 'P' the sign l with a raised p (abbreviation ending);
'^2' a raised abbreviation mark. In the output '?' stays '?', an abbreviation mark is shown as "'", and boundaries are
dropped (the cipher has no word division).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    with open(os.path.join(HERE, 'key.json'), encoding='utf-8') as fh:
        key = {s: v['plain'] for s, v in json.load(fh)['key'].items()}
    with open(os.path.join(HERE, 'sample_20_lines_blind.txt'), encoding='utf-8') as fh:
        sample = [ln.rstrip('\n') for ln in fh if ln.strip()]
    printed = {}
    with open(os.path.join(HERE, 'lettenhove_1888_sample_lines.tsv'), encoding='utf-8') as fh:
        next(fh)
        for ln in fh:
            if ln.strip():
                line, words = ln.rstrip('\n').split('\t', 1)
                printed[line] = words
    return key, sample, printed


def decode(tokens, key):
    out = []
    for tk in tokens:
        if tk in ('|', '~', ',', '.'):
            continue
        if tk == 'P':          # l + raised p: abbreviation ending, no letter value
            out.append("'")
        elif tk.startswith('^'):
            out.append("'")
        elif tk == '?':
            out.append('?')
        else:
            out.append(key.get(tk, '#'))
    return ''.join(out)


def main():
    key, sample, printed = load()
    for ln in sample:
        label, body = ln.split(':', 1)
        print(f'{label}  decode : {decode(body.split(), key)}')
        print(f'{"":5}printed: {printed.get(label, "(none)")}')


if __name__ == '__main__':
    main()
