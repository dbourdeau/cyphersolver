"""Smoke tests for the code every target shares: lang/, the docs/ checkers, the catalogue and the profiles.

Offline and quick (no corpus is fetched, the site is not built). Run from the repository root:

    python -m unittest discover tests
"""
import gzip
import importlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'docs'))

from lang import lm  # noqa: E402


def run(*args):
    env = dict(os.environ, PYTHONUTF8='1')
    return subprocess.run([sys.executable, *args], cwd=ROOT, env=env, capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


class Lang(unittest.TestCase):
    def test_norm_schemes(self):
        self.assertEqual(lm.norm('Jé vous Écris, Kyrie', 'early'), 'ie uous ecris kyrie')
        self.assertEqual(lm.norm('Jé vous Kyrie w', 'latin'), 'ie uous cirie u')
        self.assertEqual(lm.norm('Jé Vous', 'modern', spaces=False), 'jevous')

    def test_alphabet(self):
        self.assertEqual(len(lm.alphabet('modern', False)), 26)
        self.assertEqual(len(lm.alphabet('modern', True)), 27)

    def test_registry_sources_exist(self):
        models = json.loads((ROOT / 'lang' / 'models.json').read_text(encoding='utf-8'))
        sources = json.loads((ROOT / 'lang' / 'sources.json').read_text(encoding='utf-8'))
        self.assertTrue(models)
        for mid, m in models.items():
            for s in m['sources']:
                self.assertIn(s, sources, f'model {mid} names an unknown source')

    def test_dense_model_prefers_its_own_language(self):
        alpha = lm.alphabet('modern', True)
        text = lm.norm('le roi a escrit a son ambassadeur que la paix estoit faite avec le duc ' * 40)
        m = lm.DenseLM.build(text, 3, alpha)
        self.assertGreater(m.per_char(lm.norm('le duc a escrit au roi')), m.per_char('xqzj kwvx zzqj xkqw'))

    def test_lexicons_load(self):
        files = sorted((ROOT / 'lang' / 'lexicons').glob('*.json.gz'))
        self.assertTrue(files)
        for f in files:
            with gzip.open(f, 'rt', encoding='utf-8') as fh:
                self.assertTrue(json.load(fh), f.name)

    def test_cache_follows_the_recipe(self):
        # a model cached from one recipe is rebuilt when models.json names other sources or another norm
        from lang import corpora
        texts = {'a': 'le roi a escrit a son ambassadeur ' * 30, 'b': 'the king has written to his ambassador ' * 30}
        spec = {'norm': 'modern', 'order': 3, 'sources': ['a']}
        old = lm.CACHE, lm.registry, corpora.text
        with tempfile.TemporaryDirectory() as tmp:
            lm.CACHE, lm.registry = tmp, lambda: ({'t': spec}, {})
            corpora.text = lambda sids: ' '.join(texts[s] for s in sids)
            try:
                first = lm.load('t')
                self.assertEqual(lm.load('t').meta['chars'], first.meta['chars'])
                corpora.text = None                                  # an unchanged recipe is served from the cache
                self.assertEqual(lm.load('t').meta['sources'], ['a'])
                corpora.text = lambda sids: ' '.join(texts[s] for s in sids)
                spec['sources'] = ['b']
                self.assertEqual(lm.load('t').meta['sources'], ['b'])
                spec['norm'] = 'early'
                m = lm.load('t')
                self.assertEqual((m.meta['norm'], m.alpha), ('early', lm.alphabet('early', True)))
            finally:
                lm.CACHE, lm.registry, corpora.text = old


class Ledgers(unittest.TestCase):
    def test_json_ledgers_parse(self):
        for name in ('catalogue.json', 'contributors.json', 'repositories.json', 'profile.schema.json',
                     'research/leads.json', 'decode_updates/queue.json'):
            json.loads((ROOT / name).read_text(encoding='utf-8'))

    def test_every_profile_parses(self):
        bad = []
        for p in sorted((ROOT / 'targets').glob('*/profile.json')):
            try:
                json.loads(p.read_text(encoding='utf-8'))
            except ValueError as e:
                bad.append(f'{p.parent.name}: {e}')
        self.assertEqual(bad, [])

    def test_catalogue_gate(self):
        r = run('docs/_check_catalogue.py')
        self.assertIn('result: valid', r.stdout, r.stdout[-2000:] + r.stderr[-2000:])

    def test_profile_audit(self):
        r = run('docs/_check_profile.py', '--audit')
        self.assertEqual(r.returncode, 0, r.stderr[-2000:])
        self.assertIn(' 0 invalid', r.stdout)


class DocsModules(unittest.TestCase):
    def test_imports(self):
        for name in ('_methods', '_texts', '_check_reading', '_check_writeup', '_check_profile', '_check_catalogue'):
            importlib.import_module(name)


if __name__ == '__main__':
    unittest.main()
