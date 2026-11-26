"""Write the group-by-group decryptions of the 14 and 15 October 1913 telegrams.

Each cipher run of the frozen transcription is printed with the unedited output of its frozen table underneath.
'?' is an illegible group or a group the table does not give. Nothing is fitted or corrected here.

    python3 -I targets/tellez1913/make_texts.py      (from the repository root)
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
# the seven values added to the table from the 14 October telegram; their separate test missed
OCT14_ADDITIONS = {'20', '53', '108', '113', '132', '140', '147'}


def key(path):
    k = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'): continue
        p = line.split('\t')
        if p[0].strip().isdigit() and len(p) > 1 and p[1].strip():
            k[str(int(p[0]))] = p[1].strip()
    return k


def write(out, runs, keyfile, head, mark=frozenset()):
    k = key(keyfile)
    lines = [f'# Group-by-group decryption. {head}.',
             '# One cipher run per pair of lines; clear Spanish between runs is not shown. ? = illegible or not in the table.',
             '']
    for i, line in enumerate(runs.read_text(encoding='utf-8').split('\n'), 1):
        g = line.split()
        if not g: continue
        dec = [(k.get(x, '?') + ('*' if x in mark else '')) if x != '?' else '?' for x in g]
        lines += [f'<< run {i} >>', ' '.join(g), ' '.join(dec)]
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(out.name, 'written')


if __name__ == '__main__':
    write(HERE / 'decryption_oct14.txt', HERE / 'oct14.runs', HERE / 'candidate.tsv',
          'CEHM DLXXIII.1.32.5-41, Rubio to Téllez, 14 Oct 1913; table candidate.tsv (71 entries, frozen before the test)')
    write(HERE / 'decryption_oct15.txt', HERE / 'oct15.runs', HERE / 'candidate15.tsv',
          'CEHM DLXXIII.1.32.6-41, Rubio to [Téllez], 15 Oct 1913; table candidate15.tsv (78 entries, frozen before the '
          'test). Output from the seven values added after 14 Oct (20 53 108 113 132 140 147, separate test missed) is '
          'marked with *', OCT14_ADDITIONS)
