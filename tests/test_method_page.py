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
        # one classifier: docs/_reader_kind.py, called through kind_of(review)
        by = lambda b, **kw: dict({'grade': 'A', 'by': b, 'date': '2026-11-16'}, **kw)
        self.assertEqual(MP.kind_of(by('Claude Opus 5.5 (for Brice Dudout)')), 'model')
        self.assertEqual(MP.kind_of(by('Brice Dudout (with Claude)')), 'person+model')
        self.assertEqual(MP.kind_of(by('Andrew Beling')), 'person')
        self.assertEqual(MP.kind_of(by("project (the project's verification pass)")), 'unclear')
        self.assertEqual(MP.kind_of(by('integration pass (a model session, not a person)')), 'model')
        # a reader_kind written in the record wins over the rule
        self.assertEqual(MP.kind_of(by('Andrew Beling', reader_kind='person assisted by model')), 'person+model')

    def test_same_classifier_as_reader_kind(self):
        import _reader_kind as RK
        for b in ('Claude Opus 5.5', 'Brice Dudout (with Claude)', 'Andrew Beling', 'project (x)', "Rundata (Uppsala University)"):
            r = {'by': b}
            self.assertEqual(MP.kind_of(r), MP.KIND[RK.kind_of(r)])

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
                         human_check={'date': 'x', 'by': 'p', 'passage': 'l. 1', 'result': 'confirmed'},
                         sign_check=[{'date': 'x', 'checker': 'p', 'checker_kind': 'project', 'model_roles': ['sheet'],
                                      'signs_checked': 9, 'controls': 2, 'controls_passed': 2, 'rule': 'NOTES', 'rule_hash': 'b' * 64},
                                     {'date': 'y', 'checker': 'q', 'checker_kind': 'external', 'model_roles': [],
                                      'signs_checked': 8, 'controls': 2, 'controls_passed': 1, 'rule': 'NOTES'}]),
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
        # sign checks: one record, two sheets; the second misses a control, so it does not meet the level
        self.assertEqual((c['sc_profiles'], c['sc'], c['sc_level']), (1, 2, 1))
        self.assertEqual((c['sc_signs'], c['sc_external'], c['sc_model']), (17, 1, 1))
        self.assertEqual((c['crypt_read'], c['crypt_val'], c['crypt_unval']), (2, 1, 1))
        self.assertEqual(dict(c['unval_who']), {'x': 1})

    def test_pages_render(self):
        c = MP.review_counts(ROOT)
        for page in (MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})):
            self.assertIn('<!-- site:nav -->', page)
            main = page.split('<main>')[1]
            self.assertNotIn('{', main.replace('{+...}', ''))
            self.assertEqual(main.count('<table>'), main.count('</table>'))
            self.assertEqual(main.count('<table>'), 7)  # the model-family table went (review of #789, point 2)
            self.assertIn('callout glance', main)
            # "human review" appears only to say that the model's grade is not one
            self.assertEqual(main.count('human review'), main.count('not a human review'))
            self.assertEqual(main.count('relecture humaine'), main.count('pas une relecture humaine'))
        # the sign-check level: named for what it is, never "validated"
        en, fr = MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})
        self.assertIn('AI decipherment, human-checked on a sample of signs', en)
        self.assertIn('Déchiffrement par IA, vérifié par une personne sur un échantillon de signes', fr)
        self.assertIn('id="sign-check"', en)
        self.assertIn('id="signes"', fr)
        # the first readings: the checker is the contributor (not independent), said on the page
        self.assertIn('the checker is the contributor', en)
        self.assertIn('le vérificateur est le contributeur', fr)
        for page in (en, fr):
            sec = page.split('<h3 id="sign')[1].split('<h2')[0]
            self.assertNotRegex(sec.lower(), r'\bvalidated?\b|\bvalidée?\b')
            self.assertIn('<code>sign_check</code>', sec)


class ReducedTree(unittest.TestCase):
    def test_no_timestamps_folder(self):
        # a tree where no target has timestamps/ (review of #718, point 7): figures() and both pages still build
        with tempfile.TemporaryDirectory() as d:
            (pathlib.Path(d) / 'targets' / 'a').mkdir(parents=True)
            (pathlib.Path(d) / 'targets' / 'a' / 'profile.json').write_text(json.dumps(profile(
                [{'reading_review': {'grade': 'A', 'by': 'Claude Opus 5.5', 'date': 'x'}}],
                method='key recovered from ciphertext-only', **{'class': 'read'})), encoding='utf-8')
            c = MP.review_counts(d, audit={}, names={})
        self.assertNotIn('timestamped', c)
        self.assertFalse(MP.figures(c, 'en')['ts_all_contrib'])
        for page in (MP.page_en(c, 0, {}), MP.page_fr(c, 0, {})):
            self.assertIn('<!-- site:nav -->', page)

    def test_tool_pages(self):
        import _check_writeup as CW
        self.assertTrue({'method', 'method-fr'} <= CW.TOOL_PAGES)


class SignLevel(unittest.TestCase):
    def test_meets_level(self):
        ok = {'signs_checked': 8, 'controls': 2, 'controls_passed': 2, 'checker': 'Named reader',
              'rule': 'Frozen before answers', 'rule_hash': 'a' * 64}
        self.assertTrue(MP.sign_level(ok))
        for field in ('checker', 'rule', 'rule_hash'):
            incomplete = ok.copy()
            del incomplete[field]
            self.assertFalse(MP.sign_level(incomplete))
        self.assertFalse(MP.sign_level(dict(ok, rule_hash='invalid')))
        self.assertFalse(MP.sign_level(dict(ok, controls_passed=1)))
        self.assertFalse(MP.sign_level(dict(ok, signs_checked=7)))
        self.assertFalse(MP.sign_level(dict(ok, controls=1, controls_passed=1)))
        self.assertFalse(MP.sign_level({'signs_checked': 'unknown', 'controls': 2, 'controls_passed': 2}))


class Wording(unittest.TestCase):
    def test_review_of_19_nov(self):
        c = MP.review_counts(ROOT)
        en, fr = MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})
        # point 4: the read share is counted by a script where the reading declares its markup
        self.assertIn('counted by a script where the reading declares its markup', en)
        self.assertNotIn('By the README, a script counts it', en)
        self.assertNotIn('Selon le README, un script la compte', fr)
        # point 3: corrections.html is on main; the citation carries the commit; no "version number yet"
        self.assertNotIn('not yet a public list of corrections', en)
        self.assertNotIn('pas encore de liste publique des corrections', fr)
        self.assertIn('href="corrections.html"', en)
        self.assertIn('href="corrections.html"', fr)
        self.assertNotIn('version number yet', en)
        self.assertNotIn('numéro de version', fr)
        self.assertIn('repository commit', en)
        # the unedited-decryption rule, the ruleset bypass and the sign-check rules as the project's own
        self.assertIn('nothing edited', en)
        self.assertIn('deploy key', en)
        self.assertIn('clé de déploiement', fr)
        self.assertIn('These are the project&rsquo;s rules', en)

    def test_first_batch_sentence_and_no_below_level(self):
        c = MP.review_counts(ROOT)
        en, fr = MP.page_en(c, 7, {}), MP.page_fr(c, 7, {})
        for page in (en, fr):
            for slug in ('ridolfi1646', 'lopehurtado1520', 'genes1638'):
                self.assertIn('<code>%s</code>' % slug, page)
        self.assertIn('was not part of the first batch', en)
        self.assertIn('ne faisait pas partie du premier lot', fr)
        # below_level is not a rule of the level: gone from the README, the schema and the code
        for f in ('README.md', 'profile.schema.json', 'docs/_method_page.py'):
            self.assertNotIn('below_level', (ROOT / f).read_text(encoding='utf-8'))

    def test_one_french_file_name(self):
        import _check_writeup as CW
        self.assertNotIn('methode', CW.TOOL_PAGES)


if __name__ == '__main__':
    unittest.main()
