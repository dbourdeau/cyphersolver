"""The 'contributed' provenance rule in docs/_credits.py: it needs a credit that says the contributor made the result."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'docs'))
import _credits as C  # noqa: E402

REG = {'someone': {'kind': 'person'}}


def prof(role, provenance='contributed'):
    return {'outcome': {'provenance': provenance, 'credits': [{'who': 'someone', 'role': role}]}}


class ContributedRule(unittest.TestCase):
    def test_roles_that_satisfy_it(self):
        for role in ('solution', 'new cipher', 'new cipher with solution'):
            with self.subTest(role=role):
                self.assertEqual(C.check(prof(role), REG), [])

    def test_a_pointer_does_not(self):
        errs = C.check(prof('pointer'), REG)
        self.assertEqual(len(errs), 1)
        self.assertIn('"new cipher"', errs[0])


if __name__ == '__main__':
    unittest.main()
