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

    def test_authors_agent(self):
        self.assertTrue(MP.authors_agent("Author's agents (Andrew Beling, with AI agents)", []))
        self.assertTrue(MP.authors_agent('Claude Opus 5.5 (for Brice Dudout)', ['Brice Dudout']))
        self.assertFalse(MP.authors_agent('Claude Opus 5.5 (for Brice Dudout)', ['Andrew Beling']))
        self.assertFalse(MP.authors_agent('Claude Opus 5.5 (PR review on merge)', ['Brice Dudout']))


class Format(unittest.TestCase):
    def test_fr_typo(self):
        self.assertEqual(MP.fr_typo('ceci : cela ; « mot »'), 'ceci&nbsp;: cela&nbsp;; «&nbsp;mot&nbsp;»')
        self.assertEqual(MP.fr_typo('<a href="https://x">x</a>'), '<a href="https://x">x</a>')

    def test_table(self):
        t = MP.table(['a', 'b'], [['1', '2']], total=['All', ''])
        self.assertIn('<th>a</th><th>b</th>', t)
        self.assertIn('<td><b>All</b></td><td></td>', t)


class Counts(unittest.TestCase):
    def test_counts(self):
        rr = lambda by, note='': {'grade': 'A', 'by': by, 'date': '2026-11-16', 'note': note}
        tree = {
            'a': profile([{'reading_review': rr('Claude Opus 5.5', 'not independent (same session)'), 'read_share': 0.97},
                          {'state': 'read in part', 'reading_review': rr('Brice Dudout (with Claude)')},
                          {'state': 'read', 'doc': 'd1'}, {'state': 'read', 'doc': 'd2'}],
                         method='key recovered from ciphertext-only', **{'class': 'read'},
                         validation={'date': 'x', 'verdict': 'pass'},
                         human_check={'date': 'x', 'by': 'p', 'passage': 'l. 1', 'result': 'confirmed'}),
            'b': profile([{'reading_review': rr('Someone Else')}, {'reading_review': rr('Claude (for Xavier Y)')},
                          {'state': 'read in part'}],
                         method='key recovered from ciphertext-only',
                         provenance='contributed', credits=[{'who': 'x', 'role': 'solution'}], **{'class': 'read in part'}),
            'c': profile([], method='not solved', verification=['matched control'], **{'class': 'not read'}),
            'd': profile([], method='not solved', **{'class': 'not read'}),
        }
        tree['a']['conditions']['prior_solution'] = {'exists': 'in print', 'found': 'after reading'}
        tree['a']['outcome']['credits'] = [{'who': 'ed', 'role': 'prior solution'}]
        tree['b']['conditions']['prior_solution'] = {'exists': 'online'}
        audit = {'a': {'grade': 'C', 'docs': {'d1': {'grade': 'A'}}}}
        with tempfile.TemporaryDirectory() as d:
            for folder, prof in tree.items():
                (pathlib.Path(d) / 'targets' / folder).mkdir(parents=True)
                (pathlib.Path(d) / 'targets' / folder / 'profile.json').write_text(json.dumps(prof), encoding='utf-8')
            # a copy one level deeper is not a target and is not counted
            (pathlib.Path(d) / 'targets' / 'a' / 'old').mkdir()
            (pathlib.Path(d) / 'targets' / 'a' / 'old' / 'profile.json').write_text(json.dumps(tree['a']), encoding='utf-8')
            (pathlib.Path(d) / 'targets' / 'b' / 'timestamps').mkdir()
            c = MP.review_counts(d, audit=audit, names={'x': 'Xavier Y'})
        self.assertEqual(c['profiles'], 4)
        self.assertEqual(c['rr'], 4)
        self.assertEqual(c['rr_profiles'], 2)
        self.assertEqual(dict(c['kinds']), {'model': 2, 'person+model': 1, 'person': 1})
        self.assertEqual(c['rr_not_independent'], 1)
        self.assertEqual(c['rr_authors_agent'], 1)
        self.assertEqual(c['read_no_rr'], 2)
        self.assertEqual(c['read_no_share'], 4)
        # no grade of its own: d1 takes the audit's per-document A, d2 the target's C, b's entry has none
        self.assertEqual((c['graded_no_rr'], c['no_rr_audit_ab'], c['no_rr_audit_other'], c['no_rr_none']), (3, 1, 1, 1))
        self.assertEqual((c['m_notsolved'], c['notsolved_control']), (2, 1))
        self.assertEqual((c['to_credit'], c['credited']), (2, 1))
        self.assertEqual(c['found']['after reading'], 1)
        self.assertEqual((c['timestamped'], dict(c['ts_prov'])), (1, {'contributed': 1}))
        self.assertEqual(c['hc'], 1)
        self.assertEqual((c['crypt_read'], c['crypt_val'], c['crypt_unval']), (2, 1, 1))
        self.assertEqual(dict(c['unval_who']), {'x': 1})

    def test_pages_render(self):
        c = MP.review_counts(ROOT)
        for page in (MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})):
            self.assertIn('<!-- site:nav -->', page)
            main = page.split('<main>')[1]
            self.assertNotIn('{', main.replace('{+...}', ''))
            self.assertEqual(main.count('<table>'), main.count('</table>'))
            self.assertEqual(main.count('<table>'), 8)
            self.assertIn('callout glance', main)
            # "human review" appears only to say that the model's grade is not one
            self.assertEqual(main.count('human review'), main.count('not a human review'))
            self.assertEqual(main.count('relecture humaine'), main.count('pas une relecture humaine'))


if __name__ == '__main__':
    unittest.main()
