"""End-to-end tests of freeze.py, measure.py and check.py in a throwaway git repository with a local "remote".

    python tools/holdout/test_holdout.py
"""
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
TEXT = ("the ambassador writes that the king will not sign the treaty before the fleet returns from the islands "
        "and that the money promised for the army has not arrived he asks that the letters be sent by the usual "
        "road and that nothing be said to the council until the answer of the queen is known")


def run(*args, cwd=None):
    return subprocess.run(list(args), cwd=cwd, capture_output=True, text=True, encoding='utf-8')


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def tool(name, *args, cwd=None):
    return run(PY, os.path.join(HERE, name), *args, cwd=cwd)


def nomenclator():
    """Every word its own three-digit code: the case where the char metric's controls stay high."""
    words = TEXT.split()
    vocab = sorted(set(words))
    codes = [str(n) for n in random.Random(7).sample(range(100, 1000), len(vocab))]
    key = dict(zip(codes, vocab))
    inv = {w: c for c, w in key.items()}
    return key, [inv[w] for w in words], words


class Repo:
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix='holdout-test-')
        self.remote = os.path.join(self.tmp, 'remote.git')
        self.root = os.path.join(self.tmp, 'work')
        run('git', 'init', '-q', '--bare', self.remote)
        run('git', 'init', '-q', self.root)
        for k, v in (('user.name', 'test'), ('user.email', 'test@example.invalid'), ('core.autocrlf', 'false')):
            run('git', 'config', k, v, cwd=self.root)
        run('git', 'remote', 'add', 'origin', self.remote, cwd=self.root)
        self.ver = os.path.join(self.root, 'targets', 'demo', 'verification')
        os.makedirs(self.ver)

    def write(self, name, text):
        with open(os.path.join(self.ver, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)

    def commit(self, msg, *paths):
        run('git', 'add', '--', *paths, cwd=self.root)
        return run('git', 'commit', '-q', '-m', msg, cwd=self.root)

    def push(self):
        run('git', 'push', '-q', 'origin', 'HEAD:main', cwd=self.root)
        run('git', 'fetch', '-q', 'origin', cwd=self.root)

    def setup_passage(self, key, groups, ref, v='v1', metric='group', extra=None):
        self.write(f'key_{v}.tsv', ''.join(f'{c}\t{w}\n' for c, w in sorted(key.items())))
        self.write(f'holdout_{v}.txt', ' '.join(groups) + '\n')
        self.write(f'reference_{v}.txt', ' '.join(ref) + '\n' if metric == 'group' else TEXT + '\n')
        proto = {'name': f'demo {v}', 'manifest': f'MANIFEST_{v}.sha256', 'key': f'key_{v}.tsv',
                 'holdout': f'holdout_{v}.txt', 'reference': f'reference_{v}.txt', 'metric': metric,
                 'threshold': 0.85, 'margin': 0.30, 'controls': 200, 'seed': 2026, 'result': f'RESULT_{v}.json'}
        proto.update(extra or {})
        self.write(f'PROTOCOL_{v}.json', json.dumps(proto, indent=1) + '\n')
        files = [f'PROTOCOL_{v}.json', f'key_{v}.tsv', f'holdout_{v}.txt', f'reference_{v}.txt']
        r = tool('freeze.py', 'freeze', f'MANIFEST_{v}.sha256', *files, cwd=self.ver)
        assert r.returncode == 0, r.stdout + r.stderr
        return [os.path.join('targets', 'demo', 'verification', f) for f in files + [f'MANIFEST_{v}.sha256']]

    def measure(self, v='v1', *extra):
        return tool('measure.py', os.path.join(self.ver, f'PROTOCOL_{v}.json'), *extra)

    def check(self):
        return tool('check.py', f'--root={self.root}')

    def close(self):
        shutil.rmtree(self.tmp, ignore_errors=True)


class HoldoutTests(unittest.TestCase):
    def setUp(self):
        self.r = Repo()
        self.key, self.groups, self.words = nomenclator()

    def tearDown(self):
        self.r.close()

    def test_full_cycle(self):
        paths = self.r.setup_passage(self.key, self.groups, self.words)
        out = self.r.measure()
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('Not committed', out.stderr)

        self.r.commit('freeze v1', *paths)
        out = self.r.measure()
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('no remote-tracking branch', out.stderr)

        self.r.push()
        out = self.r.measure()
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn('VALIDATED', out.stdout)
        res = load(os.path.join(self.r.ver, 'RESULT_v1.json'))
        self.assertEqual(res['score'], 1.0)
        self.assertLess(res['controls']['mean'], 0.1)        # group metric: controls near zero on average
        self.assertTrue(res['git']['manifest_commit_on_remote'])

        again = self.r.measure()
        self.assertIn('burnt', again.stderr)

        out = self.r.check()
        self.assertIn('not committed yet', out.stdout)
        self.r.commit('result v1', 'targets/demo/verification/RESULT_v1.json')
        out = self.r.check()
        self.assertEqual(out.returncode, 0, out.stdout)
        self.assertIn('order shown by git', out.stdout)
        self.assertIn('result: valid', out.stdout)

        # a frozen file edited after the measurement
        with open(os.path.join(self.r.ver, 'key_v1.tsv'), 'a', encoding='utf-8') as f:
            f.write('999\tx\n')
        out = self.r.check()
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('no longer matches', out.stdout)

    def test_changed_file_refused_before_run(self):
        paths = self.r.setup_passage(self.key, self.groups, self.words)
        self.r.commit('freeze', *paths)
        self.r.push()
        with open(os.path.join(self.r.ver, 'holdout_v1.txt'), 'a', encoding='utf-8') as f:
            f.write('123\n')
        out = self.r.measure()
        self.assertIn('changed', out.stdout + out.stderr)
        self.assertFalse(os.path.exists(os.path.join(self.r.ver, 'RESULT_v1.json')))

    def test_dry_run_is_not_evidence(self):
        paths = self.r.setup_passage(self.key, self.groups, self.words)
        out = self.r.measure('v1', '--dry-run')
        self.assertEqual(out.returncode, 0, out.stderr)
        self.r.commit('dry', *paths, 'targets/demo/verification/RESULT_v1.json')
        out = self.r.check()
        self.assertIn('dry run: not evidence', out.stdout)
        self.assertNotEqual(out.returncode, 0)

    def test_wrong_key_fails_and_char_floor(self):
        wrong = dict(self.key)
        codes = sorted(wrong)[:12]
        vals = [wrong[c] for c in codes][::-1]
        wrong.update(zip(codes, vals))
        self.r.setup_passage(wrong, self.groups, self.words)
        out = self.r.measure('v1', '--dry-run')
        self.assertIn('NOT VALIDATED', out.stdout)
        # same key, same passage, same seed: the char metric's controls sit well above the group metric's
        self.r.setup_passage(self.key, self.groups, self.words, v='v2', metric='group')
        self.r.setup_passage(self.key, self.groups, self.words, v='v3', metric='char')
        self.r.measure('v2', '--dry-run')
        self.r.measure('v3', '--dry-run')
        g = load(os.path.join(self.r.ver, 'RESULT_v2.json'))
        c = load(os.path.join(self.r.ver, 'RESULT_v3.json'))
        self.assertGreater(c['controls']['best'], g['controls']['best'] + 0.1)
        self.assertGreater(c['controls']['mean'], g['controls']['mean'] + 0.2)

    def test_forged_manifest_commit_fails(self):
        run('git', 'commit', '-q', '--allow-empty', '-m', 'unrelated', cwd=self.r.root)
        unrelated = run('git', 'rev-parse', 'HEAD', cwd=self.r.root).stdout.strip()
        paths = self.r.setup_passage(self.key, self.groups, self.words)
        self.r.commit('freeze', *paths)
        self.r.push()
        self.assertEqual(self.r.measure().returncode, 0)
        res_path = os.path.join(self.r.ver, 'RESULT_v1.json')
        res = load(res_path)
        res['git']['manifest_commit'] = unrelated
        with open(res_path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(res, f)
        self.r.commit('result', 'targets/demo/verification/RESULT_v1.json')
        out = self.r.check()
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('order not shown', out.stdout)

    @unittest.skipIf(shutil.which('openssl') is None, 'openssl not installed')
    def test_rfc3161_timestamp(self):
        """A throwaway local TSA stamps the manifest; measure accepts it without a push, check accepts the order."""
        d = os.path.join(self.r.tmp, 'tsa')
        os.makedirs(d)
        cnf = os.path.join(d, 'tsa.cnf')
        with open(cnf, 'w') as f:
            f.write('[req]\ndistinguished_name=dn\nprompt=no\n[dn]\nCN=test tsa\n'
                    '[ext]\nextendedKeyUsage=critical,timeStamping\n'
                    '[tsa]\ndefault_tsa=t\n[t]\nserial=' + os.path.join(d, 'serial').replace('\\', '/') +
                    '\nsigner_digest=sha256\ndefault_policy=1.2.3.4\ndigests=sha256\naccuracy=secs:1\n'
                    'ess_cert_id_alg=sha256\n')
        with open(os.path.join(d, 'serial'), 'w') as f:
            f.write('01\n')
        key, crt = os.path.join(d, 'k.pem'), os.path.join(d, 'c.pem')
        r = run('openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-keyout', key, '-out', crt, '-days', '2',
                '-config', cnf, '-extensions', 'ext')
        self.assertEqual(r.returncode, 0, r.stderr)

        paths = self.r.setup_passage(self.key, self.groups, self.words, v='v2',
                                     extra={'timestamp': {'rfc3161': 'MANIFEST_v2.sha256.tsr'}})
        man = os.path.join(self.r.ver, 'MANIFEST_v2.sha256')
        tsq, tsr = man + '.tsq', man + '.tsr'
        self.assertEqual(run('openssl', 'ts', '-query', '-data', man, '-sha256', '-cert', '-out', tsq).returncode, 0)
        r = run('openssl', 'ts', '-reply', '-config', cnf, '-section', 't', '-queryfile', tsq, '-signer', crt,
                '-inkey', key, '-out', tsr)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.r.commit('freeze v2 + stamp', *paths, 'targets/demo/verification/MANIFEST_v2.sha256.tsr')
        out = self.r.measure('v2')                       # not pushed: the stamp is the outside clock
        self.assertEqual(out.returncode, 0, out.stderr)
        import time
        time.sleep(1.1)                                  # the result commit must come after the stamp's second
        res_path = os.path.join(self.r.ver, 'RESULT_v2.json')
        res = load(res_path)
        self.assertEqual(res['git']['manifest_commit_on_remote'], [])
        res['git']['manifest_commit'] = '0' * 40         # as if the freeze commit was squashed away
        with open(res_path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(res, f)
        self.r.commit('result v2', 'targets/demo/verification/RESULT_v2.json')
        out = self.r.check()
        self.assertEqual(out.returncode, 0, out.stdout)
        self.assertIn('order shown by RFC 3161 token', out.stdout)

    def test_crlf_gives_same_hash(self):
        sys.path.insert(0, HERE)
        import freeze
        self.assertEqual(freeze.sha256_bytes(b'a\r\nb\r\n'), freeze.sha256_bytes(b'a\nb\n'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
