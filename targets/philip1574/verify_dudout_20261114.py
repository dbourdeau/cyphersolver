"""philip1574: README word recount of clear_version.md (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

Counts the Spanish body only (from '## Paragraph 1'), drops the editorial note '(cipher: ...)', treats
abbreviation expansions written in brackets (r[elaci]on, q[ue]) as read words and '[?]' as a hole.
Also prints what research/reading_audit/v10_relabel.share gives on the same file, for comparison.
Usage: python3 verify_dudout_20261114.py <path to cyphersolver checkout>
"""
import re, sys, os, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
f = root / 'targets' / 'philip1574' / 'clear_version.md'
t = f.read_text(encoding='utf8')
body = t.split('## Paragraph 1', 1)[1]
body = re.sub(r'\(cipher:[^)]*\)', '', body)
body = '\n'.join(l for l in body.split('\n') if not l.startswith('##') and 'scan 2 right' not in l)
expansions = re.findall(r'\w*\[[^\]?]+\]\w*', body)
holes = re.findall(r'\[\?\]\w*', body)
words = re.findall(r'[^\W\d_]+', re.sub(r'[\[\]?]', '', body))
print('words', len(words), 'expansions', len(expansions), 'holes', holes,
      'share', round(1 - len(holes) / len(words), 3))
sys.path.insert(0, str(root / 'research' / 'reading_audit')); sys.path.insert(0, str(root / 'docs'))
os.chdir(root)
try:
    import v10_relabel as v
    print('v10_relabel.share (words, holes, doubtful):', v.share(t))
except Exception as e:
    print('v10 not run:', e)
