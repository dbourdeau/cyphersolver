"""Replay the unchanged registered scorer with repository inputs in an isolated directory."""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import json
import shutil
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    here = Path(__file__).resolve().parent
    scorer = here / 'registered_scorer.py'
    key = here.parents[2] / 'figueroa1534/validation/K4.tsv'
    shapes = here.parent / 'shape_index.tsv'
    reference = here / 'reference.txt'
    expected = json.loads((here / 'result.json').read_text())
    freeze = dict(line.split(maxsplit=1)[::-1] for line in (here / 'FREEZE.txt').read_text().splitlines()[1:])
    for source in [here / 'PLAN.md', key, shapes, reference]:
        assert digest(source) == freeze[source.name], source.name
    assert digest(scorer) == (here / 'SCORER.sha256').read_text().split()[0]
    for name, expected_hash in expected['inputs'].items():
        assert digest(here / name) == expected_hash, name

    # The original program reads two project-relative paths, then writes its products beside itself.
    with TemporaryDirectory(dir=here, prefix='replay-') as path:
        root = Path(path)
        staged = root / 'study/interior'
        files = {
            key: root / 'crawford_rebase/targets/figueroa1534/validation/K4.tsv',
            shapes: root / 'priority_review/modena_shape_reference/shape_index.tsv',
            reference: staged / 'reference.txt',
            scorer: staged / 'check.py',
        }
        for name in expected['inputs']:
            files[here / name] = staged / name
        for source, output in files.items():
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, output)
        subprocess.run([sys.executable, '-I', '-B', str(staged / 'check.py')], check=True, capture_output=True)
        # TSV uses native CSV line endings in the registered scorer and LF in the portable packet.
        for name in ('positions.tsv', 'control_scores.txt', 'result.json'):
            assert (here / name).read_text() == (staged / name).read_text(), name
    print(f"{expected['covered']}/{expected['union']} positions, {expected['known']} known characters. "
          f"Ordered matches {expected['pieces']}, score {expected['score']}. "
          f"Of 1,000 controls, {expected['control_greater']} beat, {expected['control_tie']} tied; "
          f"maximum {expected['control_max']}. Pass: {expected['pass']}.")


if __name__ == '__main__':
    verify()
