"""The short-text floor in docs/_texts.reading_problems (README Conventions, 19 Nov 2026)."""
import pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'docs'))
import _texts


def profile(**entry):
    base = {'doc': 'a', 'state': 'read', 'translation': 't.md', 'language': 'fr',
            'reading_review': {'grade': 'A', 'by': 'x', 'date': '2026-11-19', 'note': 'n'}}
    base.update(entry)
    return {'outcome': {'class': 'read', 'texts': [base]}}


def hard(**entry):
    with tempfile.TemporaryDirectory() as d:
        return _texts.reading_problems(pathlib.Path(d), profile(**entry), score=False)[0]


class Floor(unittest.TestCase):
    def test_over_bar_needs_nothing(self):
        self.assertEqual(hard(read_share=0.96), [])

    def test_under_bar_without_floor_is_refused(self):
        h = hard(read_share=0.89)
        self.assertEqual(len(h), 1)
        self.assertIn('floor_used', h[0])

    def test_nine_codes_two_holes(self):
        self.assertEqual(hard(read_share=7 / 9, floor_used=True, cipher_words=9, holes=2), [])

    def test_five_percent_beats_two_holes_only_from_forty_words(self):
        # 39 words: at most max(2, 1.95) = 2 holes
        self.assertEqual(hard(read_share=37 / 39, floor_used=True, cipher_words=39, holes=2), [])
        self.assertEqual(len(hard(read_share=36 / 39, floor_used=True, cipher_words=39, holes=3)), 1)

    def test_forty_words_never_get_the_floor(self):
        h = hard(read_share=37 / 40, floor_used=True, cipher_words=40, holes=3)
        self.assertEqual(len(h), 1)
        self.assertIn('40 or more', h[0])

    def test_share_must_match_the_counts(self):
        h = hard(read_share=0.8, floor_used=True, cipher_words=9, holes=2)
        self.assertEqual(len(h), 1)
        self.assertIn('does not match', h[0])

    def test_counts_must_be_whole_numbers(self):
        self.assertEqual(len(hard(read_share=0.8, floor_used=True, cipher_words=9.0, holes=2)), 1)


if __name__ == '__main__':
    unittest.main()
