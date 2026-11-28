#!/usr/bin/env python3
"""measure.py - ONE measurement of a frozen key on a held-out passage, against shuffled-key controls.

    python tools/holdout/measure.py targets/<t>/verification/PROTOCOL_v1.json
    python tools/holdout/measure.py PROTOCOL.json --dry-run      # synthetic tests only; check.py never accepts it
    python tools/holdout/measure.py PROTOCOL.json --issue-comment=URL

PROTOCOL_vN.json, written and frozen with freeze.py before the run (paths relative to the protocol's folder):
{
  "name":       "morier1808 H3",            # free text
  "manifest":   "MANIFEST_v1.sha256",
  "key":        "key.tsv",                  # code <TAB> value per line ('#' comment); empty value = null; no duplicates
  "holdout":    "holdout.txt",              # groups separated by spaces; '|' = break (clear passage); '?' = illegible
  "reference":  "holdout_reference.txt",    # metric "char": independent plaintext of the same passage;
                                            # metric "group": one expected value per held-out token, aligned 1:1
                                            #   ('|' where the held-out has '|', '-' = null, '?' = not known: skipped)
  "lexicon":    "lexicon.txt",              # metric "lex": an independent word list, one word per line
  "metric":     "group" | "char" | "lex",
  "min_word":   4, "min_groups": 2,         # lex only
  "threshold":  0.85, "margin": 0.30,       # pass = score >= threshold AND score >= best control + margin
  "controls":   200, "seed": 12345,
  "result":     "RESULT_v1.json",           # written once; the run refuses to start if it exists
  "timestamp":  {"rfc3161": "MANIFEST_v1.sha256.tsr"}   # optional: an outside timestamp instead of a pushed
                                            # commit (the reply is named before freezing; it is not itself frozen)
}
An issue comment carrying the manifest hash can serve instead; since it is posted after the freeze, it is given on the
command line:  measure.py PROTOCOL_v1.json --issue-comment=https://github.com/OWNER/REPO/issues/N#issuecomment-ID

Before scoring, the run checks, and refuses if any fails:
  1. the result file does not exist (the passage is not burnt);
  2. every file in the manifest matches its hash, and the protocol and every file it names are in the manifest;
  3. (not with --dry-run) the manifest and the files it names are committed and unchanged in the working tree, and
     the commit that added the manifest is on a remote-tracking branch (run `git fetch` first) - or the protocol
     names an RFC 3161 reply whose imprint is the manifest's SHA-256, or an issue comment carrying that hash.
The result records the manifest's hash and commit, the hash of this script and the Python version, so a result can
be traced to the exact files and code that produced it. Commit and push it at once.

Metrics. "group": share of counted held-out groups whose key value equals the aligned reference value; shuffled
controls score near zero on it, so the margin means something for nomenclators. "char": letters matched by difflib
against an independent plaintext, over the longer of the two; shuffled controls keep real words and syllables, so on
nomenclators they reach about 0.70 (Brice Dudout's experience), which makes the 0.30 margin hard to reach.
"lex": share of decoded letters covered by lexicon words of at least min_word letters; even a perfect key stays
below 1. The metric and threshold are fixed in the protocol before the run.

Controls: the values of the codes that occur in the held-out passage are shuffled among those codes (seeded). A pass
shows that the assignment is far from random on this passage, not that every value is right; it means something only
if the key was built without seeing the passage. The result also gives the rank among controls (with 200 controls the
smallest p is 0.005) and z, the distance from the control mean in control standard deviations.

One run only: a measured passage is burnt. A corrected key is tested on a NEW passage with a NEW manifest.

Adapted from Brice Dudout's method kit (26 Nov 2026), code under the MIT licence, Copyright (c) 2026 Brice Dudout.
"""
import datetime
import difflib
import hashlib
import json
import os
import platform
import random
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import freeze      # noqa: E402
import gitstate    # noqa: E402

TOOL = 'cyphersolver-holdout/1'


def norm(s):
    s = unicodedata.normalize('NFD', s.lower().replace('œ', 'oe').replace('æ', 'ae'))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z]', '', s)


def load_key(path):
    key = {}
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        line = line.rstrip('\r\n')
        if line.startswith('#') or not line.strip():
            continue
        if '\t' not in line:
            sys.exit(f'{path}:{n}: no TAB between code and value.')
        code, value = line.split('\t')[:2]
        code = code.strip()
        if code in key:
            sys.exit(f'{path}:{n}: code {code!r} listed twice.')
        key[code] = norm(value)
    return key


def runs_of_values(groups, key):
    """Decoded values cut into runs at breaks, illegible groups and codes missing from the key; nulls skipped."""
    runs, cur = [], []
    for g in groups:
        if g not in ('|', '?') and key.get(g) == '':
            continue
        v = key.get(g) if g not in ('|', '?') else None
        if v:
            cur.append(v)
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs


def score_char(groups, key, reference):
    decoded = ''.join(''.join(r) for r in runs_of_values(groups, key))
    if not decoded or not reference:
        return 0.0
    m = difflib.SequenceMatcher(None, decoded, reference, autojunk=False)
    return sum(b.size for b in m.get_matching_blocks()) / max(len(decoded), len(reference))


def score_lex(groups, key, lexicon, min_word, min_groups, max_groups=8):
    total = covered = 0
    for r in runs_of_values(groups, key):
        n = len(r)
        best = [0] * (n + 1)
        for i in range(1, n + 1):
            best[i] = best[i - 1]
            for j in range(max(0, i - max_groups), i - min_groups + 1):
                w = ''.join(r[j:i])
                if len(w) >= min_word and w in lexicon and best[j] + len(w) > best[i]:
                    best[i] = best[j] + len(w)
        total += sum(len(x) for x in r)
        covered += best[n]
    return covered / total if total else 0.0


def load_aligned(path, groups):
    ref = open(path, encoding='utf-8').read().split()
    if len(ref) != len(groups):
        sys.exit(f'{path}: {len(ref)} reference tokens for {len(groups)} held-out tokens; they must align 1:1.')
    for i, (g, r) in enumerate(zip(groups, ref), 1):
        if (g == '|') != (r == '|'):
            sys.exit(f'{path}: token {i}: breaks do not line up ({g!r} against {r!r}).')
    return ref


def score_group(groups, key, ref):
    counted = right = 0
    for g, r in zip(groups, ref):
        if g in ('|', '?') or r == '?':
            continue
        counted += 1
        want = '' if r == '-' else norm(r)
        right += (g in key and key[g] == want)
    return right / counted if counted else 0.0


def git_gate(proto_path, P, manifest, must, issue=None):
    """Refuse unless the frozen state left this machine before the measurement. Returns the facts to record."""
    root = freeze.repo_root(os.path.dirname(os.path.abspath(proto_path)))
    if not root:
        sys.exit('Not in a git repository: commit the frozen files first (or use --dry-run on synthetic data).')
    unclean = [gitstate.rel(root, f) for f in [manifest] + must if not gitstate.is_tracked_clean(root, f)]
    if unclean:
        sys.exit('Not committed, or changed since the commit: ' + ', '.join(unclean) + ' -> measurement refused.')
    commit = gitstate.adding_commit(root, manifest)
    refs = gitstate.remote_refs_containing(root, commit)
    T = P.get('timestamp') or {}
    tsr = None
    if T.get('rfc3161'):
        tpath = os.path.join(os.path.dirname(os.path.abspath(proto_path)), T['rfc3161'])
        info = gitstate.tsr_info(tpath) if os.path.isfile(tpath) else None
        raw = hashlib.sha256(open(manifest, 'rb').read()).hexdigest()
        if not info:
            sys.exit(f"{T['rfc3161']}: missing, or not readable with `openssl ts -reply -text`. Measurement refused.")
        if info[0] not in (raw, freeze.sha256(manifest)):
            sys.exit(f"{T['rfc3161']}: its imprint is not the manifest's SHA-256. Measurement refused.")
        tsr = {'file': T['rfc3161'], 'time': info[1]}
    if not refs and not issue and not tsr:
        sys.exit(f'The commit that added the manifest ({commit[:10]}) is on no remote-tracking branch. Push it to '
                 'GitHub (then `git fetch`); or stamp the manifest (RFC 3161) and name the reply in the protocol as '
                 '"timestamp": {"rfc3161": "MANIFEST_vN.sha256.tsr"}; or post the manifest hash in an issue comment '
                 'and pass --issue-comment=URL. Measurement refused.')
    return root, {'manifest_commit': commit, 'manifest_commit_on_remote': refs, 'issue_comment': issue,
                  'rfc3161': tsr, 'head_at_measure': gitstate.head(root)}


def main(proto_path, dry_run=False, issue=None):
    P = json.load(open(proto_path, encoding='utf-8'))
    base = os.path.dirname(os.path.abspath(proto_path))
    at = lambda p: os.path.join(base, p)
    result_path = at(P['result'])
    if os.path.exists(result_path):
        sys.exit(f"{P['result']} exists: this passage is already measured (burnt). Use a new held-out passage.")
    manifest = at(P['manifest'])
    if not freeze.verify(manifest, quiet=True):
        sys.exit('Frozen files changed since the manifest: measurement refused.')
    metric = P['metric']
    needs = {'group': ['reference'], 'char': ['reference'], 'lex': ['lexicon']}
    if metric not in needs:
        sys.exit('metric must be "group", "char" or "lex".')
    for k in ['key', 'holdout'] + needs[metric]:
        if not P.get(k):
            sys.exit(f'The protocol names no "{k}" file, which metric "{metric}" needs.')
    must = [at(P[k]) for k in ('key', 'holdout', 'reference', 'lexicon') if P.get(k)]
    frozen = freeze.listed(manifest)
    missing = [os.path.basename(f) for f in [os.path.abspath(proto_path)] + must
               if os.path.normcase(os.path.normpath(os.path.abspath(f))) not in frozen]
    if missing:
        sys.exit('Not in the manifest: ' + ', '.join(missing) + ' -> measurement refused.')
    if int(P.get('controls', 0)) < 1:
        sys.exit('controls must be >= 1.')

    gitfacts = None
    if not dry_run:
        _, gitfacts = git_gate(proto_path, P, manifest, [os.path.abspath(proto_path)] + must, issue)

    key = load_key(at(P['key']))
    groups = open(at(P['holdout']), encoding='utf-8').read().split()
    if metric == 'char':
        ref = norm(open(at(P['reference']), encoding='utf-8').read())
        score = lambda k: score_char(groups, k, ref)
    elif metric == 'group':
        ref = load_aligned(at(P['reference']), groups)
        score = lambda k: score_group(groups, k, ref)
    else:
        lex = {norm(w) for w in open(at(P['lexicon']), encoding='utf-8') if norm(w)}
        score = lambda k: score_lex(groups, k, lex, P.get('min_word', 4), P.get('min_groups', 2))

    n_groups = sum(1 for g in groups if g != '|')
    codes = [g for g in groups if g not in ('|', '?')]
    coverage = sum(1 for g in codes if g in key) / n_groups if n_groups else 0.0
    real = score(key)
    used = sorted({g for g in codes if g in key})
    values = [key[c] for c in used]
    rng = random.Random(P['seed'])
    controls = []
    for _ in range(int(P['controls'])):
        shuffled = values[:]
        rng.shuffle(shuffled)
        k2 = dict(key)
        k2.update(zip(used, shuffled))
        controls.append(score(k2))
    controls.sort()
    best = controls[-1]
    mean = statistics.mean(controls)
    sd = statistics.pstdev(controls)
    ge = sum(1 for c in controls if c >= real)
    passed = real >= P['threshold'] and real >= best + P['margin']

    result = {
        'tool': TOOL,
        'dry_run': dry_run,
        'protocol': os.path.basename(proto_path),
        'name': P.get('name') or P.get('_name') or '',
        'measured_at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'manifest': P['manifest'],
        'manifest_sha256': freeze.sha256(manifest),
        'frozen_files': {p: d for d, p in freeze.entries(manifest)},
        'git': gitfacts,
        'script_sha256': {n: freeze.sha256(os.path.join(HERE, n)) for n in ('measure.py', 'freeze.py', 'gitstate.py')},
        'python': platform.python_version(),
        'metric': metric,
        'groups': n_groups,
        'coverage': round(coverage, 4),
        'score': round(real, 4),
        'controls': {'n': len(controls), 'seed': P['seed'], 'best': round(best, 4),
                     'p95': round(controls[int(0.95 * (len(controls) - 1))], 4), 'mean': round(mean, 4),
                     'sd': round(sd, 4), 'at_or_above_real': ge},
        'p_empirical': round((1 + ge) / (len(controls) + 1), 4),
        'z': round((real - mean) / sd, 2) if sd > 0 else None,
        'criterion': {'threshold': P['threshold'], 'margin': P['margin'], 'bar': round(max(P['threshold'], best + P['margin']), 4)},
        'verdict': 'VALIDATED' if passed else 'NOT VALIDATED',
    }
    with open(result_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(f"{result['name'] or proto_path}: {metric} score {real:.4f}; controls best {best:.4f}, mean {mean:.4f}"
          f" (z = {result['z']}); {ge}/{len(controls)} controls at or above; bar {result['criterion']['bar']}"
          f" -> {result['verdict']}")
    print(f"Written {P['result']}. Commit and push it now." + (' (dry run: not evidence)' if dry_run else ''))


if __name__ == '__main__':
    opts = [a for a in sys.argv[1:] if a.startswith('--')]
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    issues = [a.split('=', 1)[1] for a in opts if a.startswith('--issue-comment=')]
    unknown = [a for a in opts if a != '--dry-run' and not a.startswith('--issue-comment=')]
    if len(args) != 1 or unknown:
        sys.exit(__doc__)
    main(args[0], dry_run='--dry-run' in opts, issue=issues[0] if issues else None)
