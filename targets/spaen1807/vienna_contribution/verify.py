"""Verify the portable Vienna evidence draft. Requires only Python's standard library."""
import csv
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

BUNDLE = Path(__file__).resolve().parent
DIGEST_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")

# The frozen scripts must stay byte for byte as hashed on 19 November 2026, so they cannot be edited
# to pass encoding='utf-8' and newline=''. They are run through this wrapper instead, which gives
# every text-mode open() in them those two defaults. On macOS and Linux it changes nothing.
RUNNER = """import builtins, io, runpy, sys
_open = io.open
def _utf8_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if 'b' not in mode:
        if encoding in (None, 'locale'):
            encoding = 'utf-8'
        if newline is None:
            newline = ''
    return _open(file, mode, buffering, encoding, errors, newline, closefd, opener)
io.open = builtins.open = _utf8_open
script = sys.argv[1]
sys.argv = sys.argv[1:]
runpy.run_path(script, run_name='__main__')
"""


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(name):
    path = Path(name)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError(f"Unsafe relative path: {name}")
    return path


def digest_lines(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        match = DIGEST_LINE.fullmatch(line)
        if match:
            yield match[1], str(relative(match[2]))


def verify_archive():
    entries = dict((name, value) for value, name in digest_lines(BUNDLE / 'SHA256SUMS'))
    present = {str(p.relative_to(BUNDLE)) for p in BUNDLE.rglob('*') if p.is_file()}
    if present != set(entries) | {'SHA256SUMS'}:
        raise ValueError('Bundle file inventory differs from SHA256SUMS')
    for name, wanted in entries.items():
        if digest(BUNDLE / name) != wanted:
            raise ValueError(f'Bundle digest mismatch: {name}')

    with (BUNDLE / 'PATH_MAP.tsv').open(encoding='utf-8', newline='') as stream:
        mapping = {r['original_path']:r for r in csv.DictReader(stream, delimiter='\t')}
    commits = ('january/VIENNA_FREEZE.txt', 'march/PLAN_FREEZE.txt',
               'march/PREDICTION_FREEZE.txt', 'march14/PLAN_FREEZE.txt',
               'march14/PREDICTION_FREEZE.txt')
    omitted = set()
    verified = 0
    for manifest in commits:
        for wanted, original in digest_lines(BUNDLE / manifest):
            item = mapping[original]
            if item['status'] == 'image checksum only':
                if item['bundle_path'] or Path(original).suffix != '.jpg':
                    raise ValueError(f'Invalid image exclusion: {original}')
                omitted.add(original)
                continue
            if digest(BUNDLE / relative(item['bundle_path'])) != wanted:
                raise ValueError(f'Historical commitment mismatch: {original}')
            verified += 1
    if len(omitted) != 3:
        raise ValueError('Expected exactly three unbundled source-image commitments')
    for manifest in ('REFERENCE_FREEZE.txt', 'SEAL21.txt'):
        records = list(digest_lines(BUNDLE / 'references' / manifest))
        if len(records) != 1:
            raise ValueError(f'Missing held-out reference commitment in {manifest}')
        wanted, name = records[0]
        if digest(BUNDLE / 'references' / name) != wanted:
            raise ValueError(f'Held-out reference digest mismatch: {name}')
    print(f'Archive: {len(entries)} file hashes; {verified} frozen file entries; '
          '2 sealed references. Three original training-image hashes are preserved without images.')
    return {r['bundle_path']:relative(original) for original,r in mapping.items() if r['bundle_path']}


def replay(scratch, locations):
    def copy(name):
        target = scratch / locations[name]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BUNDLE / name, target)
        return target

    def run(name, *args):
        completed = subprocess.run([sys.executable, '-I', '-B', str(runner), str(scratch / locations[name]),
                                    *map(str,args)], cwd=scratch, text=True, capture_output=True)
        if completed.returncode:
            raise RuntimeError(f'{name} failed:\n{completed.stderr}')

    def compare(*names):
        for name in names:
            if (scratch / locations[name]).read_bytes() != (BUNDLE / name).read_bytes():
                raise ValueError(f'Replay mismatch: {name}')

    runner = scratch / '_utf8_runner.py'
    with runner.open('w', encoding='utf-8', newline='') as stream:
        stream.write(RUNNER)

    # Stage source and fixed inputs only, so no saved result can masquerade as regenerated output.
    for name in locations:
        if name.startswith('readers/') or name.endswith('.py'):
            copy(name)
    for name in ('january/vienna_clear_copy.txt', 'march/train23.txt', 'march/labels.txt',
                 'march/path_1.5.tsv', 'march/path_3.tsv'):
        copy(name)
    ref26 = copy('references/reference26.txt')
    ref21 = copy('references/heldout21.txt')
    run('january/vienna_reconcile.py')
    run('march/reconcile.py')
    run('march14/reconcile21.py')
    compare('january/vienna_groups.tsv', 'march/groups23.tsv', 'march/groups26.tsv',
            'march14/groups21.tsv')

    run('january/vienna_test.py')
    compare(*('january/'+name for name in ('vienna_fitted.tsv', 'vienna_controls.tsv',
                                          'vienna_predictions.tsv', 'vienna_result.json')))
    print('January: 330 slots; 2/5 matched (one distinct word); 226/1,000 controls tied or beat the score. MISS.')

    # Re-select the key from the archived two training paths. Do not refit the alignment.
    run('march/predict.py')
    compare(*('march/'+name for name in ('candidate_audit.tsv', 'training_segments.tsv',
                                         'key.tsv','predictions26.tsv','label_coverage26.tsv',
                                         'pre_score.json','shared_sequences.tsv','overlap_controls.tsv')))
    run('march14/predict21.py',digest(ref21))
    compare('march14/predictions21.tsv','march14/label_coverage21.tsv','march14/pre_score.json')
    for folder,doc,reference in [('march',26,ref26),('march14',21,ref21)]:
        run(folder+'/score_heldout.py',reference)
        compare(*(folder+'/'+name for name in ('transfer_controls.tsv','transfer_matches.tsv',
                                               'transfer_result.json')))
        res = json.loads((BUNDLE / folder / 'transfer_result.json').read_text(encoding='utf-8'))
        print(f"No. {doc}: {res['exact_matches']}/{res['predictions']} exact window matches, "
              f"{res['distinct_matched_words']} distinct; best of 1,000 controls {res['control_max']}. "
              f"{'PASS' if res['passed'] else 'MISS'}.")
    run('march/summarize_matches.py')
    run('march14/compare_support.py')
    compare('march/held_support_by_code.tsv','march14/cross_letter_support.tsv')
    print('Reconciliations, 93-entry key, prospective predictions, matched rows, all control '
          'rows and cross-letter support tables reproduced byte-for-byte.')


def dusseldorf():
    """Check the 19 November bare-number screen on Düsseldorf No. 6 and rerun it."""
    folder = BUNDLE / 'dusseldorf'
    repo_annex = BUNDLE.parents[1] / 'spaen1808' / 'annex_groups.txt'
    where = {
        'output/codex_2026-11-17b/nov19_late/spaen1808_projection/PLAN.md': folder / 'PLAN.md',
        'output/codex_2026-11-17b/nov19_late/shortlist/march/key.tsv': BUNDLE / 'march' / 'key.tsv',
        'sources/research-repo/targets/spaen1808/annex_groups.txt': repo_annex,
        'output/spaen1808_2026-11-14/transcription/annex_pass2.txt': folder / 'annex_pass2.txt',
    }
    records = list(digest_lines(folder / 'FREEZE.txt'))
    if sorted(name for _, name in records) != sorted(where):
        raise ValueError('Unexpected entries in dusseldorf/FREEZE.txt')
    for wanted, name in records:
        if digest(where[name]) != wanted:
            raise ValueError(f'Düsseldorf commitment mismatch: {name}')
    with tempfile.TemporaryDirectory(prefix='vienna-dusseldorf-') as tmp:
        root = Path(tmp) / 'targets'
        work = root / 'spaen1807' / 'vienna_contribution'
        (work / 'dusseldorf').mkdir(parents=True)
        (work / 'march').mkdir()
        (root / 'spaen1808').mkdir()
        for name in ('screen.py', 'annex_pass2.txt'):
            shutil.copyfile(folder / name, work / 'dusseldorf' / name)
        shutil.copyfile(BUNDLE / 'march' / 'key.tsv', work / 'march' / 'key.tsv')
        shutil.copyfile(repo_annex, root / 'spaen1808' / 'annex_groups.txt')
        completed = subprocess.run([sys.executable, '-I', '-B', str(work / 'dusseldorf' / 'screen.py')],
                                   cwd=tmp, text=True, capture_output=True)
        if completed.returncode:
            raise RuntimeError(f'dusseldorf/screen.py failed:\n{completed.stderr}')
        for name in ('bare_numbers.tsv', 'slots.tsv', 'predictions.tsv', 'result.json'):
            if (work / 'dusseldorf' / name).read_bytes() != (folder / name).read_bytes():
                raise ValueError(f'Replay mismatch: dusseldorf/{name}')
    res = json.loads((folder / 'result.json').read_text(encoding='utf-8'))
    print(f"Düsseldorf No. 6: 4 frozen inputs match; {res['covered_slots']} eligible placements over "
          f"{res['strict_comparable']} agreed positions (minimum 8). Outputs reproduced byte-for-byte; not scored.")


if __name__ == '__main__':
    locations = verify_archive()
    with tempfile.TemporaryDirectory(prefix='vienna-evidence-') as tmp:
        replay(Path(tmp), locations)
    dusseldorf()
