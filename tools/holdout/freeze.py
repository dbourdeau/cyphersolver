#!/usr/bin/env python3
"""freeze.py - freeze the files of a held-out test (protocol, transcription, key, held-out passage) before measuring.

    python tools/holdout/freeze.py freeze targets/<t>/verification/MANIFEST_v1.sha256 PROTOCOL_v1.json key.tsv ...
    python tools/holdout/freeze.py verify targets/<t>/verification/MANIFEST_v1.sha256

`freeze` writes one line per file, "<sha256>  <path>", under a header with the UTC time. Paths are stored relative to
the manifest's folder. A file may sit above that folder (`../transcription.txt`) as long as it stays inside the git
repository, or inside the manifest's folder when there is no repository. An existing manifest is never overwritten:
a new freeze takes a new name (MANIFEST_v2.sha256 ...), so the history stays visible.

Hashes are taken with CRLF line ends turned into LF, so a file gives the same hash on a Windows checkout
(core.autocrlf) and on a Linux one. For a file that has no CRLF this is the plain SHA-256 of the file.

What the hashes show: that the files did not change after the manifest was written. They do not show WHEN it was
written. That comes from outside the folder: the manifest committed and pushed to GitHub before the measurement, or
its hash posted in an issue comment (see tools/holdout/README.md). measure.py refuses to run without one of the two.

Adapted from Brice Dudout's method kit (26 Nov 2026), code under the MIT licence, Copyright (c) 2026 Brice Dudout.
"""
import datetime
import hashlib
import os
import subprocess
import sys


def sha256_bytes(data):
    """SHA-256 with CRLF turned into LF (identical to the plain hash when there is no CRLF)."""
    return hashlib.sha256(data.replace(b'\r\n', b'\n')).hexdigest()


def sha256(path):
    return sha256_bytes(open(path, 'rb').read())


def repo_root(start):
    try:
        out = subprocess.run(['git', '-C', start, 'rev-parse', '--show-toplevel'], capture_output=True, text=True)
    except OSError:
        return None
    return os.path.abspath(out.stdout.strip()) if out.returncode == 0 and out.stdout.strip() else None


def _inside(path, folder):
    try:
        return os.path.commonpath([os.path.abspath(path), os.path.abspath(folder)]) == os.path.abspath(folder)
    except ValueError:  # another drive on Windows
        return False


def freeze(manifest, paths):
    if os.path.exists(manifest):
        sys.exit(f'{manifest} already exists: use a new manifest name (e.g. MANIFEST_v2.sha256).')
    base = os.path.dirname(os.path.abspath(manifest))
    limit = repo_root(base) or base
    rows = []
    for p in paths:
        if not os.path.isfile(p):
            sys.exit(f'{p}: not a file.')
        if not _inside(p, limit):
            sys.exit(f'{p} is outside {limit}: move it there first.')
        rel = os.path.relpath(os.path.abspath(p), base).replace(os.sep, '/')
        rows.append((p, rel))
    if len({r for _, r in rows}) != len(rows):
        sys.exit('A file is named twice.')
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    with open(manifest, 'w', encoding='utf-8', newline='\n') as out:
        out.write(f'# frozen {now} (UTC)\n')
        for p, r in rows:
            out.write(f'{sha256(p)}  {r}\n')
    print(f'{manifest}: {len(rows)} files frozen at {now}. Manifest hash: {sha256(manifest)}')
    print('Next: commit the manifest and the files it names, and get that commit onto GitHub (or post the manifest '
          'hash in an issue comment) BEFORE running measure.py.')


def entries(manifest):
    """(digest, path relative to the manifest folder) for each line of a manifest."""
    out = []
    for line in open(manifest, encoding='utf-8'):
        line = line.rstrip('\r\n')
        if line.startswith('#') or not line.strip():
            continue
        digest, path = line.split('  ', 1)
        out.append((digest, path))
    return out


def listed(manifest):
    """Absolute, normalised paths of the files a manifest names."""
    base = os.path.dirname(os.path.abspath(manifest))
    return {os.path.normcase(os.path.normpath(os.path.join(base, p))) for _, p in entries(manifest)}


def verify(manifest, quiet=False):
    base = os.path.dirname(os.path.abspath(manifest))
    bad = []
    for digest, path in entries(manifest):
        full = os.path.join(base, path)
        if not os.path.isfile(full):
            bad.append(f'missing: {path}')
        elif sha256(full) != digest:
            bad.append(f'changed: {path}')
    if bad:
        print('\n'.join(bad))
        return False
    if not quiet:
        print(f'{manifest}: all files match.')
    return True


if __name__ == '__main__':
    if len(sys.argv) >= 4 and sys.argv[1] == 'freeze':
        freeze(sys.argv[2], sys.argv[3:])
    elif len(sys.argv) == 3 and sys.argv[1] == 'verify':
        sys.exit(0 if verify(sys.argv[2]) else 1)
    else:
        sys.exit(__doc__)
