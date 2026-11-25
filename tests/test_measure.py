"""Unit tests for the read-share measure (research/reading_audit/v10_relabel.py with v2_score.py).

The read share counts cipher words only (README Conventions, 16 Nov 2026) and holes by words (14 Nov 2026). These
tests pin the rules from the R23 scan: declared cipher or clear markup, blockquoted readings, files with no
"## Reading" heading, read code values, markers and comments. Offline; nothing in the repository is written.
Run from the repository root:

    python -m unittest discover tests
"""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'docs'))
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))

import _check_profile as CP   # noqa: E402
import v2_score as V2         # noqa: E402
import v10_relabel as V10     # noqa: E402


def m(text, **decl):
    return V10.measure_text(text, decl)


class CipherOnly(unittest.TestCase):
    TEXT = ('# A letter: reading\n\n## Reading\n\n'
            'Monsieur, je vous escris ceste lettre [...] en clair, et **le roy veult la paix** [...] avec vous, '
            '**et [?mande] que vous veniez**. Je prie Dieu.\n')

    def test_undeclared_is_whole_body_and_says_not_split(self):
        r = m(self.TEXT)
        self.assertEqual(r['split'], 'not split')
        self.assertIn('**', r['marks'])
        self.assertEqual(r['holes'], 3)

    def test_cipher_markup_counts_the_marked_words_only(self):
        r = m(self.TEXT, cipher_markup='**')
        self.assertTrue(r['split'].startswith('cipher only'))
        self.assertEqual(r['words'], 9)        # le roy veult la paix / et que vous veniez
        self.assertEqual(r['holes'], 2)        # [?mande] inside, [...] touching the first run; not the clear [...]

    def test_hole_among_clear_words_does_not_count(self):
        r = m('## Reading\n\nIl dit [...] que **le roy veult la paix et la guerre** demain.\n', cipher_markup='**')
        self.assertEqual((r['words'], r['holes']), (8, 0))

    def test_hole_between_two_cipher_runs_counts(self):
        r = m('## Reading\n\nIl dit **le roy** [...] **la paix** demain.\n', cipher_markup='**')
        self.assertEqual((r['words'], r['holes']), (4, 1))

    def test_clear_markup_drops_clear_words_and_their_holes(self):
        r = m('## Reading\n\n⟨Monsieur, je vous [...] escris⟩ le roy veult [?la] paix ⟨Je prie Dieu(?)⟩\n',
              clear_markup='⟨⟩')
        self.assertEqual((r['words'], r['holes'], r['doubtful']), (4, 1, 0))

    def test_double_brackets_as_cipher(self):
        r = m('## Reading\n\nEr schreibt ⟦der Kaiser kommt [...]⟧ morgen.\n', cipher_markup='⟦⟧')
        self.assertEqual((r['words'], r['holes']), (3, 1))

    def test_guillemets_as_cipher(self):
        r = m('## Reading\n\nHe writes «the fleet sails» on Monday.\n', cipher_markup='«»')
        self.assertEqual(r['words'], 3)

    def test_italics_as_cipher_not_bold(self):
        r = m('## Reading\n\nClear **bold** and *cipher words here* and ***also cipher***.\n', cipher_markup='*')
        self.assertEqual(r['words'], 5)

    def test_braces_as_clear_leave_hole_marks_alone(self):
        r = m('## Reading\n\n{Sire, j\'ay receu} le roy {?} veult la paix.\n', clear_markup='{}')
        self.assertEqual((r['words'], r['holes']), (5, 1))

    def test_caps_as_cipher(self):
        r = m('## Reading\n\nEnterado de su mensaje. ESTOY REFORZANDO TODA LA VIA. Saludos.\n', cipher_markup='CAPS')
        self.assertEqual(r['words'], 5)

    def test_file_declaration_overrides_the_entry(self):
        text = '<!-- measure: clear_markup=⟨⟩ -->\n## Reading\n\n⟨Monsieur⟩ le roy veult\n'
        d = V10.declaration(text, {'cipher_markup': '**'})
        self.assertEqual(d, {'clear_markup': '⟨⟩'})
        self.assertEqual(m(text, **d)['words'], 3)

    def test_entry_declaration(self):
        d = V10.declaration('## Reading\n\nx\n', {'cipher_markup': '⟦⟧', 'doc': 'A'})
        self.assertEqual(d, {'cipher_markup': '⟦⟧'})


class Body(unittest.TestCase):
    def test_blockquoted_reading_is_measured_not_the_commentary(self):
        text = ('# R674: reading\n\nCipher runs in bold. The writer [slipped] once; [?] marks a doubt here and [...] there.\n\n'
                '> Si Dominus **Generalis [60]** regimenta coniungeret, possent ad minimum tria millia\n'
                '> hominum constituere, quibus si adiungerentur adhuc duo millia peditum.\n')
        r = m(text)
        self.assertTrue(r['quoted'])
        self.assertEqual(r['holes'], 1)                     # [60] only: the commentary's marks are not the reading
        self.assertGreaterEqual(r['words'], 18)

    def test_interleaved_quotes_are_not_taken_as_the_reading(self):
        # klingenberg1675: '>' lines carry the clear text between the cipher runs
        text = '## Reading\n\n' + ''.join(f'> clear words of the letter number {i}\n\ncipher [?word] read\n\n' for i in range(6))
        r = m(text)
        self.assertFalse(r['quoted'])
        self.assertIn('>', r['marks'])
        self.assertEqual((r['words'], r['holes']), (12, 6))

    def test_declared_quote_markup(self):
        text = '## Reading\n\nclear words here and more clear [...] words\n\n> the cipher passage [...] read\n'
        r = m(text, cipher_markup='>')
        self.assertEqual((r['words'], r['holes'], r['quoted']), (4, 1, True))
        self.assertTrue(r['split'].startswith('cipher only'))
        r = m('## Reading\n\n' + 'cipher [?x] words\n\n> clear words [...] here and here and here\n', clear_markup='>')
        self.assertEqual((r['words'], r['holes']), (2, 1))

    def test_short_quotation_in_commentary_is_dropped(self):
        text = ('## Reading\n\n' + 'le roy veult la paix et la guerre avec vous ' * 4 + '\n\n> [?] a quoted line\n')
        r = m(text)
        self.assertFalse(r['quoted'])
        self.assertEqual(r['holes'], 0)

    def test_no_reading_heading_stops_at_notes_and_translation(self):
        text = ('# Letter of 3 May: reading\n\n## f. 12r\n\nle roy veult [?la] paix\n\n'
                '## Translation\n\nthe king wants [?the] peace and many more English words here\n\n'
                '## Notes\n\n[...] [...] notes words\n\n### a subsection of the notes [...]\n\n'
                '## f. 12v\n\net la guerre\n')
        r = m(text)
        self.assertEqual((r['words'], r['holes']), (7, 1))

    def test_level_one_apparatus_lines_do_not_stop(self):
        text = '# Reading of no. 24\n# context and the bracket, not from the key\nle roy veult la paix\n'
        self.assertEqual(m(text)['words'], 5)

    def test_label_paragraph_and_comments_are_not_reading(self):
        text = ('<!-- built from [the] decode: [?] [...] many words in a comment -->\n'
                '# Letter: reading\n\nConventions: [x] supplied; [?x] guessed; [...] unread.\n\n'
                'le roy veult la paix\n')
        r = m(text)
        self.assertEqual((r['words'], r['holes']), (5, 0))

    def test_reading_section(self):
        text = '## f. 233\n\nle roy [...]\n\n## f. 288v\n\nla paix et la guerre\n'
        r = m(text, reading_section='f. 288v')
        self.assertEqual((r['words'], r['holes']), (5, 0))

    def test_reading_notes_heading_is_not_the_reading(self):
        text = '## Reading notes\n\n[...] [...]\n\n## Reading\n\nle roy veult\n'
        self.assertEqual(m(text)['holes'], 0)


class Holes(unittest.TestCase):
    def count(self, s):
        return V2.holes(s).count('[?]')

    def test_read_sign_with_value_is_not_a_hole(self):
        self.assertEqual(self.count('per terras [sign = Venetorum], veremur'), 0)
        self.assertIn('Venetorum', V2.holes('[sign = Venetorum]'))
        self.assertEqual(self.count('[94=ce] [2 = che] [= October]'), 0)

    def test_doubtful_or_missing_value_stays_a_hole(self):
        self.assertGreaterEqual(self.count('[= colcothar, one sign missing]'), 1)
        self.assertGreaterEqual(self.count('[=..]'), 1)
        self.assertGreaterEqual(self.count('[?sign = rex]'), 1)

    def test_bold_code_value_is_read(self):
        out = V2.holes('en ce temps **94,** [le marquis] y arriva')
        self.assertEqual(out.count('[?]'), 0)
        self.assertIn('**94, le marquis**', out)

    def test_bracket_after_plain_number_is_not_taken_as_a_code_value(self):
        self.assertEqual(self.count('le 30 [aprilis]'), 1)

    def test_markers_are_not_holes(self):
        for mk in ('[v006r]', '[12r]', '[106v]', '[image 3]', '[img 4]', '[view 6]', '[frame 0099]', '[f. 79v]',
                   '[l. 12]', '[col. 2]', '[f. 6r = P3]', '[img374 = f° 208r]'):
            self.assertEqual(self.count(f'le roy {mk} veult'), 0, mk)

    def test_unvalued_code_is_a_hole(self):
        self.assertEqual(self.count('le [202] veult'), 1)

    def test_supplied_letters_stay_holes(self):
        self.assertEqual(m('## Reading\n\nactu[al] le roy\n')['holes'], 1)

    def test_declared_expansions_are_read(self):
        text = '## Reading\n\nIp[sis] Literis R[everendi]ssimam D[omi]nationem [que]\n'
        self.assertEqual(m(text)['holes'], 4)
        r = m(text, bracket_expansions=True)
        self.assertEqual((r['holes'], r['words']), (1, 4))   # the free-standing supplied [que] stays a hole

    def test_holes_by_words_unchanged(self):
        self.assertEqual(self.count('[... 4]'), 4)
        self.assertEqual(self.count('[?]'), 1)


class Schema(unittest.TestCase):
    def errors(self, entry):
        s = CP.SCHEMA['properties']['outcome']['properties']['texts']
        errs, gaps = [], []
        CP.validate([entry], s, 'outcome.texts', errs, gaps)
        return errs

    def test_declarations_are_in_the_schema(self):
        self.assertEqual(self.errors({'doc': 'A', 'cipher_markup': '⟦⟧', 'bracket_expansions': True,
                                      'reading_section': 'f. 233'}), [])
        self.assertEqual(self.errors({'doc': 'A', 'clear_markup': '{}'}), [])

    def test_unknown_markup_is_refused(self):
        self.assertTrue(self.errors({'doc': 'A', 'cipher_markup': '[[]]'}))

    def test_every_schema_markup_is_measured(self):
        s = CP.SCHEMA['properties']['outcome']['properties']['texts']['items']['properties']
        self.assertEqual(set(s['cipher_markup']['enum']), set(V10.MARKUP) | {'>'})
        self.assertEqual(set(s['clear_markup']['enum']), set(V10.MARKUP) | {'>'})


class Entry(unittest.TestCase):
    def test_measure_detail_reads_the_entry_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp) / 'targets' / 'x'
            base.mkdir(parents=True)
            (base / 'r.md').write_text('## Reading\n\nIl dit [...] que **le roy veult la paix** demain.\n', encoding='utf-8')
            old, V10.ROOT = V10.ROOT, pathlib.Path(tmp)
            try:
                t = {'doc': 'A', 'reading': 'r.md', 'cipher_markup': '**'}
                r = V10.measure_detail('x', t)
                self.assertEqual((r['words'], r['holes'], r['share'], r['file']), (5, 0, 1.0, 'r.md'))
                self.assertEqual(V10.measure('x', t), ('r.md', 1.0, 5))
                self.assertEqual(V10.measure_detail('x', {'doc': 'A', 'reading': 'r.md'})['split'], 'not split')
            finally:
                V10.ROOT = old


if __name__ == '__main__':
    unittest.main()
