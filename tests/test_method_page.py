"""The method page's review figures (docs/_method_page.py): the signer classes and the counts, on a synthetic tree.

    python -m unittest tests.test_method_page
"""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'docs'))

import _method_page as MP  # noqa: E402


def profile(texts=(), **outcome):
    return {'outcome': dict(texts=list(texts), **outcome), 'conditions': {'models': ['claude-opus-5-5']}}


class Kinds(unittest.TestCase):
    def test_classes(self):
        self.assertEqual(MP.kind_of('Claude Opus 5.5 (for Brice Dudout)'), 'model')
        self.assertEqual(MP.kind_of('Brice Dudout (with Claude)'), 'person+model')
        self.assertEqual(MP.kind_of('Andrew Beling'), 'person')
        self.assertEqual(MP.kind_of("project (the project's verification pass)"), 'unclear')
        self.assertEqual(MP.kind_of('integration pass (a model session, not a person)'), 'model')

    def test_edition(self):
        self.assertTrue(MP.EDITION.search('Rundata (Uppsala University)'))
        self.assertFalse(MP.EDITION.search('Andrew Beling'))


class Counts(unittest.TestCase):
    def test_counts(self):
        rr = lambda by, note='': {'grade': 'A', 'by': by, 'date': '2026-11-16', 'note': note}
        tree = {
            'a': profile([{'reading_review': rr('Claude Opus 5.5', 'not independent (same session)')},
                          {'state': 'read in part', 'reading_review': rr('Brice Dudout (with Claude)')},
                          {'state': 'read'}],
                         method='key recovered from ciphertext-only', **{'class': 'read'},
                         validation={'date': 'x', 'verdict': 'pass'},
                         human_check={'date': 'x', 'by': 'p', 'passage': 'l. 1', 'result': 'confirmed'}),
            'b': profile([{'reading_review': rr('Someone Else')}], method='key recovered from ciphertext-only',
                         provenance='contributed', credits=[{'who': 'x', 'role': 'solution'}], **{'class': 'read in part'}),
        }
        with tempfile.TemporaryDirectory() as d:
            for folder, prof in tree.items():
                (pathlib.Path(d) / 'targets' / folder).mkdir(parents=True)
                (pathlib.Path(d) / 'targets' / folder / 'profile.json').write_text(json.dumps(prof), encoding='utf-8')
            # a copy one level deeper is not a target and is not counted
            (pathlib.Path(d) / 'targets' / 'a' / 'old').mkdir()
            (pathlib.Path(d) / 'targets' / 'a' / 'old' / 'profile.json').write_text(json.dumps(tree['a']), encoding='utf-8')
            c = MP.review_counts(d)
        self.assertEqual(c['profiles'], 2)
        self.assertEqual(c['rr'], 3)
        self.assertEqual(dict(c['kinds']), {'model': 1, 'person+model': 1, 'person': 1})
        self.assertEqual(c['rr_not_independent'], 1)
        self.assertEqual(c['read_no_rr'], 1)
        self.assertEqual(c['hc'], 1)
        self.assertEqual((c['crypt_read'], c['crypt_val'], c['crypt_unval']), (2, 1, 1))
        self.assertEqual(dict(c['unval_who']), {'x': 1})

    def test_pages_render(self):
        c = MP.review_counts(ROOT)
        for page in (MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})):
            self.assertIn('<!-- site:nav -->', page)
            self.assertNotIn('{', page.split('<main>')[1].replace('{+...}', ''))


if __name__ == '__main__':
    unittest.main()
