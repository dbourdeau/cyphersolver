"""Check the frozen 9 May comparison and rerun its registered scorer once.

FREEZE.sha256 names files by their paths in the working folders of 20 November 2026.
This script finds each one in this repository, checks its hash, then runs the frozen
score.py unchanged on the Cotton reference in a temporary copy of the old layout and
compares result.json and controls.tsv with the saved files byte for byte.
The two lines for manuscript images are reported, not checked: the images are not here.
Usage: python3 -I -B replay_registered.py
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOP = HERE.parents[1]
WHERE = {
    'PLAN.md': HERE.parent / 'registered_plan.md',
    'score.py': HERE / 'score.py',
    'predictions.tsv': HERE / 'predictions.tsv',
    'eligibility.tsv': HERE / 'eligibility.tsv',
    '../nov20_william_transfer/alphabet.tsv': TOP / 'june' / 'alphabet.tsv',
    '../nov20_william_may_fresh/boxes.tsv': TOP / 'may09' / 'boxes.tsv',
    '../nov20_william_may_fresh/reader_a.tsv': TOP / 'may09' / 'reader_a.tsv',
    '../nov20_william_may_fresh/reader_b.tsv': TOP / 'may09' / 'reader_b.tsv',
    '../nov20_william_may_fresh/gloss.tsv': TOP / 'may09' / 'gloss.tsv',
    '../nov20_william_may_fresh/result.json': TOP / 'may09' / 'result.json',
}
IMAGES = {'../nov20_william_may_fresh/19r_top.png', '../nov20_william_may_fresh/19r_middle.png'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    kept = []
    for line in (HERE / 'FREEZE.sha256').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        if name in IMAGES:
            print(f'not checked (manuscript image, not included): {name}')
            continue
        if sha(WHERE[name]) != digest:
            raise SystemExit(f'hash mismatch: {name}')
        kept.append(line)
    print(f'{len(kept)} frozen files match FREEZE.sha256')
    cotton = HERE / 'cotton'
    combined = (cotton / 'reference_329r.tsv').read_bytes() + b''.join(
        (cotton / 'reference_329v.tsv').read_bytes().splitlines(keepends=True)[1:])
    if combined != (cotton / 'reference_combined.tsv').read_bytes():
        raise SystemExit('reference_combined.tsv is not the two folio tables joined')
    with tempfile.TemporaryDirectory(prefix='may09-registered-') as tmp:
        d = Path(tmp) / 'nov20_may_parallel'
        d.mkdir()
        for name, path in WHERE.items():
            target = d / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        with (d / 'FREEZE.sha256').open('w', encoding='utf-8', newline='') as stream:
            stream.write(''.join(line + '\n' for line in kept))
        run = subprocess.run([sys.executable, '-I', '-B', str(d / 'score.py'),
                              str(cotton / 'reference_combined.tsv')], cwd=tmp, capture_output=True, text=True)
        if run.returncode:
            raise SystemExit(run.stderr)
        for name in ('result.json', 'controls.tsv'):
            if (d / name).read_bytes() != (HERE / name).read_bytes():
                raise SystemExit(f'replay differs: {name}')
    print('Registered scorer rerun: result.json and all 1,000 controls reproduced byte for byte.')


if __name__ == '__main__':
    main()
