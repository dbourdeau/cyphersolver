#!/usr/bin/env python3
"""check.py - check that every held-out result was measured on files frozen, and published, before the measurement.

    python tools/holdout/check.py                 # every target
    python tools/holdout/check.py morier1808 ...  # some targets
    python tools/holdout/check.py --online        # also check issue-comment timestamps with `gh api`

For each result written by measure.py (a JSON file with "tool": "cyphersolver-holdout/...") under targets/:
  * it is not a dry run;
  * the manifest still has the hash the result records, and every frozen file still matches the manifest;
  * the recorded manifest commit exists and holds that same manifest;
  * the order is shown: the manifest commit is an ancestor of, and not the same as, the commit that added the result;
    or, when the manifest commit is no longer in history (a squashed pull request), an issue comment carrying the
    manifest hash was posted before the result commit (checked with --online; reported, not failed, without it).
  An RFC 3161 reply recorded by measure.py also shows the order when its time is before the result commit.
A manifest named by a PROTOCOL*.json with no result yet is listed as pending. Results written before this convention
(no "tool" field), and the separate `timestamps/` stamp folders, are not checked here; their order rests on the
contributor's record and the stamps they carry, and their pages say so.
Prints "result: valid" when nothing fails.
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import freeze    # noqa: E402
import gitstate  # noqa: E402


def iso_utc(s):
    """A git %cI time (with offset) as a UTC 'YYYY-MM-DDTHH:MM:SSZ' string, comparable with the other times."""
    import datetime
    return datetime.datetime.fromisoformat(s).astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def issue_comment_ok(url, digest, before):
    m = re.match(r'https://github\.com/([^/]+/[^/]+)/(?:issues|pull)/\d+#issuecomment-(\d+)$', url or '')
    if not m:
        return False, f'not an issue comment URL: {url}'
    out = subprocess.run(['gh', 'api', f'repos/{m.group(1)}/issues/comments/{m.group(2)}'],
                         capture_output=True, text=True, encoding='utf-8')
    if out.returncode != 0:
        return False, f'gh api failed for {url}'
    c = json.loads(out.stdout)
    if digest not in (c.get('body') or ''):
        return False, 'the issue comment does not carry the manifest hash'
    if c.get('created_at', '9999') > before:
        return False, f"the issue comment ({c.get('created_at')}) is later than the result commit ({before})"
    if c.get('updated_at') and c['updated_at'] != c['created_at']:
        return True, f"issue comment of {c['created_at']} carries the hash (edited {c['updated_at']}: check the edit history)"
    return True, f"issue comment of {c['created_at']} carries the hash"


def check_result(root, path, online):
    problems, notes = [], []
    R = json.load(open(path, encoding='utf-8'))
    base = os.path.dirname(path)
    manifest = os.path.join(base, R.get('manifest', ''))
    if R.get('dry_run'):
        problems.append('dry run: not evidence')
    if not os.path.isfile(manifest):
        return problems + [f"manifest {R.get('manifest')} missing"], notes
    if freeze.sha256(manifest) != R.get('manifest_sha256'):
        problems.append('the manifest changed after the measurement')
    if not freeze.verify(manifest, quiet=True):
        problems.append('a frozen file no longer matches the manifest')
    G = R.get('git') or {}
    mc = G.get('manifest_commit')
    if not mc:
        return problems + ['no manifest commit recorded'], notes
    rc = gitstate.adding_commit(root, path)
    if not rc:
        notes.append('result not committed yet: commit and push it')
        return problems, notes
    rtime = gitstate.commit_time(root, rc)
    failed = []   # why each proof of order that was tried did not hold; any one proof that holds is enough

    if gitstate.commit_exists(root, mc):
        blob = gitstate.blob_at(root, mc, manifest)
        if blob is None or freeze.sha256_bytes(blob) != R.get('manifest_sha256'):
            failed.append(f'commit {mc[:10]} does not hold the recorded manifest')
        elif mc == rc:
            failed.append('the manifest and the result were added in the same commit')
        elif gitstate.is_ancestor(root, mc, rc):
            notes.append(f'order shown by git: manifest {mc[:10]} before result {rc[:10]}'
                         + ('' if G.get('manifest_commit_on_remote') else ' (not recorded as pushed when measured)'))
            return problems, notes
        else:
            failed.append(f'manifest commit {mc[:10]} is not an ancestor of the result commit {rc[:10]}')
    else:
        failed.append(f'manifest commit {mc[:10]} is not in this history (squashed?)')

    tsr = G.get('rfc3161')
    if tsr:
        tpath = os.path.join(base, tsr['file'])
        info = gitstate.tsr_info(tpath) if os.path.isfile(tpath) else None
        raw = hashlib.sha256(open(manifest, 'rb').read()).hexdigest()
        if not os.path.isfile(tpath):
            failed.append(f"RFC 3161 reply {tsr['file']} missing")
        elif info is None:
            notes.append(f"RFC 3161 reply {tsr['file']} not read here (openssl missing?)")
        elif info[0] not in (raw, R.get('manifest_sha256')):
            failed.append(f"RFC 3161 reply {tsr['file']} does not stamp this manifest")
        elif info[1] >= iso_utc(rtime):
            failed.append(f'RFC 3161 time {info[1]} is not before the result commit ({rtime})')
        else:
            notes.append(f'order shown by RFC 3161 token: manifest stamped {info[1]}, result committed {rtime} '
                         '(TSA certificate chain not verified here)')
            return problems, notes

    issue = G.get('issue_comment')
    if issue and online:
        ok, msg = issue_comment_ok(issue, R.get('manifest_sha256', ''), iso_utc(rtime))
        if ok:
            notes.append('order shown by ' + msg)
            return problems, notes
        failed.append(msg)
    elif issue or (tsr and info is None):
        notes.extend(f'not shown: {x}' for x in failed)
        notes.append('order not checked offline: ' + (f'run with --online for {issue}' if issue else 'install openssl'))
        return problems, notes
    problems.append('order not shown: ' + '; '.join(failed))
    return problems, notes


def main(argv):
    online = '--online' in argv
    names = [a for a in argv if not a.startswith('--')]
    roots = [a.split('=', 1)[1] for a in argv if a.startswith('--root=')]
    root = os.path.abspath(roots[0]) if roots else freeze.repo_root(HERE)
    tdir = os.path.join(root, 'targets')
    folders = [os.path.join(tdir, n) for n in names] if names else sorted(glob.glob(os.path.join(tdir, '*')))
    bad = checked = 0
    for folder in folders:
        results, used = [], set()
        for p in sorted(glob.glob(os.path.join(folder, '**', '*.json'), recursive=True)):
            try:
                R = json.load(open(p, encoding='utf-8'))
            except (ValueError, OSError, UnicodeDecodeError):
                continue
            if isinstance(R, dict) and str(R.get('tool', '')).startswith('cyphersolver-holdout'):
                results.append(p)
                used.add(os.path.normcase(os.path.normpath(os.path.join(os.path.dirname(p), R.get('manifest', '')))))
        pending = []
        for p in sorted(glob.glob(os.path.join(folder, '**', 'PROTOCOL*.json'), recursive=True)):
            try:
                P = json.load(open(p, encoding='utf-8'))
            except (ValueError, OSError, UnicodeDecodeError):
                continue
            if not (isinstance(P, dict) and P.get('manifest') and P.get('result')):
                continue
            d = os.path.dirname(p)
            m = os.path.normcase(os.path.normpath(os.path.join(d, P['manifest'])))
            if m not in used and not os.path.exists(os.path.join(d, P['result'])) and os.path.isfile(m):
                pending.append(m)
        for p in results:
            checked += 1
            problems, notes = check_result(root, p, online)
            print(f"{'FAIL' if problems else 'ok  '} {gitstate.rel(root, p)}")
            for x in problems:
                print('     FAIL', x)
            for x in notes:
                print('     ', x)
            bad += bool(problems)
        for m in pending:
            print(f'pend {gitstate.rel(root, m)}: frozen, not measured yet'
                  + ('' if freeze.verify(m, quiet=True) else ' (FAIL: a frozen file changed)'))
            bad += not freeze.verify(m, quiet=True)
    print(f'{checked} result(s) checked.')
    print('result: ' + ('valid' if not bad else f'{bad} problem(s)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
