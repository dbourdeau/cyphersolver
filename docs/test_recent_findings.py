"""Regression checks for the homepage's editorial findings and folding."""
import re
import unittest
from pathlib import Path
from unittest.mock import patch

import _build_site as site


class RecentFindingsTests(unittest.TestCase):
    def test_rejects_accidentally_copied_navigation(self):
        page = ('<h2 id="recent">Recent findings</h2>\n<ul class="findings">'
                '<li><a href="writeups.html#kind=solved"><span class="st solved">77</span>'
                '<b>Solved or read</b></a></li></ul>\n<h2>Next section</h2>')
        with self.assertRaisesRegex(ValueError, 'navigation'):
            site.fold_findings(page)

    def test_preserves_entries_and_leaves_other_lists_alone(self):
        before = '<nav><ul><li>Navigation</li></ul></nav>\n'
        after = '\n<h2>Next section</h2>\n<ul><li>Unrelated</li></ul>'
        items = [f'<li><b>Finding {i}</b> — <span class="fnd">Result</span></li>' for i in range(8)]
        page = before + '<h2 id="recent">Recent findings</h2>\n<ul class="findings">' + ''.join(items) + '</ul>' + after
        with patch.object(site, 'stamp_finding', side_effect=lambda li: li):
            folded = site.fold_findings(page)
            self.assertEqual(site.fold_findings(folded), folded)
        self.assertTrue(folded.startswith(before))
        self.assertTrue(folded.endswith(after))
        visible = folded.split('<ul class="findings">', 1)[1].split('</ul>', 1)[0]
        self.assertEqual(visible.count('<li>'), 5)
        self.assertIn('Show 3 earlier findings', folded)
        for item in items:
            self.assertEqual(folded.count(item), 1)

    def test_published_homepage_contains_only_editorial_findings(self):
        page = (Path(__file__).parent / 'index.html').read_text(encoding='utf-8')
        section = site.FINDINGS_REGION.search(page).group()
        self.assertNotRegex(section, r'<span class="st [^"]+">')
        self.assertIn('segura1596.html', section)
        self.assertIn('joachim1530.html', section)
        items = re.findall(r'<li>.*?</li>', section, re.S)
        self.assertGreater(len(items), 200)
        with patch.object(site, 'stamp_finding', side_effect=lambda li: li):
            self.assertEqual(site.fold_findings(page), page)


if __name__ == '__main__':
    unittest.main()
