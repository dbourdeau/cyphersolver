"""gitstate.py - the git facts measure.py and check.py rely on, in one place.

The order "frozen, then measured" is shown by history that left this machine:
  * the commit that added the manifest is on a remote-tracking branch (pushed to GitHub) when the measurement runs,
    and is an ancestor of the commit that adds the result; or
  * the manifest's hash was posted in a GitHub issue comment before the result was committed (checked online).
"""
import os
import subprocess


def git(root, *args):
    out = subprocess.run(['git', '-C', root, *args], capture_output=True, text=True, encoding='utf-8')
    return out.returncode, out.stdout.strip()


def rel(root, path):
    return os.path.relpath(os.path.abspath(path), root).replace(os.sep, '/')


def adding_commit(root, path):
    """The commit that first added `path` (oldest), or None if it was never committed."""
    code, out = git(root, 'log', '--diff-filter=A', '--format=%H', '--', rel(root, path))
    lines = out.splitlines() if code == 0 else []
    return lines[-1] if lines else None


def is_tracked_clean(root, path):
    r = rel(root, path)
    code, out = git(root, 'ls-files', '--error-unmatch', '--', r)
    if code != 0:
        return False
    code, out = git(root, 'status', '--porcelain', '--', r)
    return code == 0 and out == ''


def remote_refs_containing(root, commit):
    code, out = git(root, 'branch', '-r', '--contains', commit)
    return [l.strip() for l in out.splitlines() if l.strip() and '->' not in l] if code == 0 else []


def is_ancestor(root, a, b):
    return git(root, 'merge-base', '--is-ancestor', a, b)[0] == 0


def commit_exists(root, c):
    return git(root, 'cat-file', '-e', f'{c}^{{commit}}')[0] == 0


def commit_time(root, c):
    code, out = git(root, 'show', '-s', '--format=%cI', c)
    return out if code == 0 else None


def blob_at(root, commit, path):
    """Bytes of `path` at `commit`, or None."""
    out = subprocess.run(['git', '-C', root, 'show', f'{commit}:{rel(root, path)}'], capture_output=True)
    return out.stdout if out.returncode == 0 else None


def head(root):
    return git(root, 'rev-parse', 'HEAD')[1] or None


def tsr_info(path):
    """(imprint hex, UTC time ISO string) of an RFC 3161 reply, read with `openssl ts -reply -text`; None if unreadable.
    The certificate chain is not verified here (`openssl ts -verify -CAfile ...` does that)."""
    import datetime
    import re
    try:
        out = subprocess.run(['openssl', 'ts', '-reply', '-in', path, '-text'], capture_output=True, text=True)
    except OSError:
        return None
    if out.returncode != 0 or 'Time stamp:' not in out.stdout:
        return None
    lines = out.stdout.splitlines()
    i = next(n for n, l in enumerate(lines) if l.strip() == 'Message data:')
    hexpart = ''
    for l in lines[i + 1:]:
        m = re.match(r'\s+[0-9a-f]{4} - ([0-9a-f -]+)', l)
        if not m:
            break
        hexpart += re.sub(r'[^0-9a-f]', '', m.group(1)[:48])
    stamp = next(l for l in lines if l.startswith('Time stamp:')).split(':', 1)[1].strip()
    t = datetime.datetime.strptime(re.sub(r'\.\d+', '', stamp).replace(' GMT', ''), '%b %d %H:%M:%S %Y')
    return hexpart, t.strftime('%Y-%m-%dT%H:%M:%SZ')
