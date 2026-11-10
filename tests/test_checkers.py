"""Unit tests for the docs/ build and checkers: the rules every write-up passes through.

Offline and quick: small fixtures in a temporary folder, no site build, nothing in the repository is written.
Run from the repository root:

    python -m unittest discover tests
"""
import json
import pathlib
import struct
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'docs'))

import _check_catalogue as CC  # noqa: E402
import _check_profile as CP    # noqa: E402
import _check_terms as CT      # noqa: E402
import _check_writeup as CW    # noqa: E402
import _images as IMG          # noqa: E402
import _manifest as MF         # noqa: E402
import _texts as TX            # noqa: E402


def png(path, w, h):
    """A file with a PNG header of the given size (the size reader looks at the header alone)."""
    path.write_bytes(b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR' + struct.pack('>II', w, h) + b'\x08\x02\x00\x00\x00')


class Manifest(unittest.TestCase):
    """_manifest.py is imported by the build and read as text by the checkers: both views must agree."""

    def test_text_reader_sees_every_page(self):
        pages, images, _ = CW.manifest()
        self.assertEqual(set(pages), {p['slug'] for p in MF.PAGES})
        self.assertEqual({p['slug']: p['st'] for p in MF.PAGES}, pages)

    def test_text_reader_sees_every_image(self):
        _, images, _ = CW.manifest()
        self.assertEqual(set(images), set(MF.IMAGES))
        for slug, has in images.items():
            self.assertEqual(has, MF.IMAGES[slug] is not None, slug)

    def test_slugs_unique_and_complete(self):
        slugs = [p['slug'] for p in MF.PAGES]
        self.assertEqual(len(slugs), len(set(slugs)))
        for p in MF.PAGES:
            for k in ('slug', 'label', 'year', 'y', 'st', 'stt', 'title', 'blurb'):
                self.assertIn(k, p, f'{p.get("slug")}: PAGES entry without {k}')

    def test_lead_images_exist(self):
        for slug, im in MF.IMAGES.items():
            if im: self.assertTrue((ROOT / 'docs' / im[0]).exists(), f'{slug}: {im[0]} is not in docs/')

    def test_titles_reader(self):
        titles = CW.manifest_titles()
        self.assertEqual(set(titles), {p['slug'] for p in MF.PAGES})

    def test_uncommented_drops_unpublished_entries(self):
        s = "    dict(slug='a', st='solved'),\n    # dict(slug='b', st='solved'),\n"
        self.assertNotIn("'b'", CW.uncommented(s))
        self.assertIn("'a'", CW.uncommented(s))


class Notes(unittest.TestCase):
    def test_section(self):
        notes = '# T\n\n## Remaining gaps\nline one\n\n## Escalation\nstep\n'
        self.assertEqual(CW.section(notes, 'Remaining gaps').strip(), 'line one')
        self.assertEqual(CW.section(notes, 'escalation').strip(), 'step')
        self.assertIsNone(CW.section(notes, 'Sources'))


class Integrity(unittest.TestCase):
    def heads(self, body):
        return {'x': ('t', 'h', body)}

    def test_sound_page(self):
        self.assertEqual(CW.integrity_problems('x', self.heads('<main><p>the cipher&rsquo;s key</p></main>')), [])

    def test_unbalanced_tag(self):
        probs = CW.integrity_problems('x', self.heads('<main><table><tr><td>a</td></tr></main>'))
        self.assertTrue(any('unbalanced <table>' in p for p in probs), probs)

    def test_damaged_entity(self):
        probs = CW.integrity_problems('x', self.heads('<main><p>cipher&rsquo;srsquo;s key</p></main>'))
        self.assertTrue(any('damaged character entity' in p for p in probs), probs)

    def test_script_content_is_ignored(self):
        self.assertEqual(CW.integrity_problems('x', self.heads('<main><script>var s="<table>";</script><p>a</p></main>')), [])

    def test_unknown_slug(self):
        self.assertEqual(CW.integrity_problems('nosuchpage', self.heads('<p>a</p>')), [])


class Texts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)
        (self.dir / 'transcr.txt').write_text('12 34 56', encoding='utf-8')
        (self.dir / 'read.md').write_text('le roi', encoding='utf-8')
        self.profile = {'documents': [{'id': 'A'}],
                        'outcome': {'class': 'read', 'method': 'read with known key',
                                    'texts': [{'doc': 'A', 'transcription': 'transcr.txt', 'decryption': 'read.md'}]}}
        if not TX.needs_texts(self.profile): self.skipTest('fixture profile is not classed as a reading')

    def tearDown(self):
        self.tmp.cleanup()

    def problems(self):
        return TX.texts_problems(self.dir, self.profile)

    def test_complete(self):
        self.assertEqual(self.problems(), [])

    def test_no_texts(self):
        self.profile['outcome']['texts'] = []
        self.assertTrue(any('no outcome.texts' in p for p in self.problems()))

    def test_missing_transcription(self):
        del self.profile['outcome']['texts'][0]['transcription']
        self.assertEqual(self.problems(), ['A: no transcription file'])

    def test_transcription_missing_needs_a_reason_only_for_the_transcription(self):
        t = self.profile['outcome']['texts'][0]
        del t['transcription']; t['transcription_missing'] = 'the leaf is not online'
        self.assertEqual(self.problems(), [])
        del t['decryption']
        self.assertEqual(self.problems(), ['A: no decryption file'])

    def test_file_must_exist(self):
        self.profile['outcome']['texts'][0]['decryption'] = 'gone.md'
        self.assertTrue(any('gone.md does not exist' in p for p in self.problems()))

    def test_uncovered_document(self):
        self.profile['documents'].append({'id': 'B'})
        self.assertTrue(any('documents without texts: B' in p for p in self.problems()))
        self.profile['outcome']['texts'][0]['doc'] = ['A', 'B']
        self.assertEqual(self.problems(), [])

    def test_transcription_is_not_the_reading(self):
        t = self.profile['outcome']['texts'][0]
        t['transcription'] = 'read.md'; t['reading'] = 'read.md'
        self.assertTrue(any('is also the reading' in p for p in self.problems()))

    def test_key_file_when_key_recovered(self):
        self.profile['outcome']['contribution'] = [TX.KEY_WORK[0]]
        self.assertTrue(any('no outcome.key_file' in p for p in self.problems()))
        (self.dir / 'key.tsv').write_text('12\tle', encoding='utf-8')
        self.profile['outcome']['key_file'] = 'key.tsv'
        self.assertEqual(self.problems(), [])

    def test_withheld(self):
        self.profile['outcome']['texts'] = []
        self.profile['outcome']['texts_withheld'] = 'the owner asked'
        self.assertEqual(self.problems(), [])

    def test_not_solved_needs_no_texts(self):
        self.assertFalse(TX.needs_texts({'outcome': {'class': 'attempted, open', 'method': 'not solved'}}))


class Vetting(unittest.TestCase):
    def entry(self):
        long = 'x' * (CC.MIN_TEXT + 5)
        return {'access': 'online',
                'vetting': {'date': '2026-11-01', 'by': 'tester',
                            'seen': {'kind': CC.SEEN_KINDS[0], 'where': long, 'extent': long, 'cipher': long},
                            'prior_art': {k: long for k in CC.PRIOR_ART},
                            'key_check': long, 'duplicates': long, 'verdict': 'open'}}

    def test_passes(self):
        self.assertEqual(CC.vetting_problems(self.entry()), [])

    def test_no_block(self):
        self.assertEqual(CC.vetting_problems({}), ['no "vetting" block'])

    def test_bad_date(self):
        e = self.entry(); e['vetting']['date'] = 'last week'
        self.assertIn('vetting.date is not an ISO date', CC.vetting_problems(e))

    def test_prior_art_all_required(self):
        for k in CC.PRIOR_ART:
            e = self.entry(); e['vetting']['prior_art'][k] = ''
            self.assertIn(f'vetting.prior_art.{k} missing or too short', CC.vetting_problems(e))

    def test_only_open_leads_enter(self):
        for v in CC.VERDICTS:
            e = self.entry(); e['vetting']['verdict'] = v
            self.assertEqual(CC.vetting_problems(e) == [], v == 'open', v)

    def test_not_online_needs_archive_access(self):
        if 'not online' not in CC.SEEN_KINDS: self.skipTest('no "not online" kind')
        e = self.entry(); e['vetting']['seen']['kind'] = 'not online'
        self.assertTrue(CC.vetting_problems(e))
        e['access'] = 'archive'
        self.assertEqual(CC.vetting_problems(e), [])

    def test_key_notes_must_say_something(self):
        e = self.entry(); e['vetting']['key_in_volume'] = 'yes'
        self.assertTrue(any('key_in_volume' in p for p in CC.vetting_problems(e)))


class Measure(unittest.TestCase):
    def measure(self, text, **kw):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 't.txt'
            f.write_text(text, encoding='utf-8')
            return CP.measure(f, **kw)

    def test_tokens_and_comments(self):
        m = self.measure('# heading\n12 34 12\n== page 2\n56 12\n')
        self.assertEqual((m['tokens'], m['distinct']), (5, 3))
        self.assertEqual(m['separation'], 'spaces')

    def test_ic(self):
        self.assertEqual(self.measure('1 1 1 1')['ic'], 1.0)
        self.assertEqual(self.measure('1 2 3 4')['ic'], 0.0)

    def test_fixed_width_groups(self):
        m = self.measure('123456 78', width=2)
        self.assertEqual(m['tokens'], 4)

    def test_digits_only(self):
        self.assertEqual(self.measure('le 12 roi 34', digits=True)['tokens'], 2)

    def test_letters(self):
        self.assertEqual(self.measure('ab c', letters=True)['tokens'], 3)

    def test_dotted(self):
        self.assertEqual(self.measure('12.34.56 78.90')['separation'], 'dots')


class Images(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name)
        png(self.dir / 'a.png', 640, 480)

    def tearDown(self):
        self.tmp.cleanup()

    def test_size_from_header(self):
        self.assertEqual(tuple(IMG.size(self.dir / 'a.png')), (640, 480))
        self.assertIsNone(IMG.size(self.dir / 'missing.png'))

    def test_annotate_adds_size_once(self):
        once = IMG.annotate('<p><img src="a.png" alt="x"></p>', base=self.dir)
        self.assertIn('width="640" height="480" decoding="async"', once)
        self.assertEqual(IMG.annotate(once, base=self.dir), once)

    def test_annotate_is_undone_by_added(self):
        page = '<p><img src="a.png" alt="x"></p>'
        self.assertEqual(IMG.ADDED.sub('', IMG.annotate(page, base=self.dir)), page)

    def test_remote_and_missing_images_left_alone(self):
        for tag in ('<img src="https://example.org/a.png" alt="">', '<img src="nothere.png" alt="">'):
            self.assertEqual(IMG.annotate(tag, base=self.dir), tag)

    def test_thumb_index_points_at_real_files(self):
        for src, copies in IMG.COPIES.items():
            for w, path in copies.items():
                self.assertTrue((ROOT / 'docs' / path).exists(), f'{path} is listed in thumbs/index.json but missing')


class Terms(unittest.TestCase):
    def test_prose_keeps_line_numbers(self):
        s = '<p>one</p>\n<p>two &amp; three</p>\n<p>four</p>'
        lines = CT.prose(s)
        self.assertEqual(len(lines), 3)
        self.assertIn('two & three', lines[1])


class Ledgers(unittest.TestCase):
    def test_review_ledger_names_real_pages(self):
        ledger = json.loads((ROOT / 'docs' / '_page_sources.json').read_text(encoding='utf-8'))
        for slug, rec in ledger.items():
            self.assertIn('digest', rec, slug)
            self.assertTrue((ROOT / 'docs' / f'{slug}.html').exists(), f'{slug} is in the review ledger but has no page')

    def test_gate_baseline_parses(self):
        f = ROOT / 'docs' / '_audit_baseline.json'
        if f.exists(): json.loads(f.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
