"""R955 (the 1757 table): the "watch it decipher" file for docs/swieten1757.html (written 14 Oct 2026, entry split).

  python targets/swieten1757/build_reveal955.py

Reads the 89 groups of runs955.txt and the 1757 values that NOTES.md lists from aligning the groups with the
decipherment written under them on f. 141 ("Aligning it gives an alphabetical syllabary ..."). Groups that the
NOTES list does not value are shown as unknown. Writes docs/reveal/swieten1757.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
notes = (HERE / 'NOTES.md').read_text(encoding='utf-8')
seg = notes.split('homophones: ', 1)[1].split('## R956', 1)[0]
key = {}
for val, nums in re.findall(r'([a-zç]+) (\d+(?:/\d+)?)', seg):
    for n in nums.split('/'):
        key[n] = val
groups = (HERE / 'runs955.txt').read_text(encoding='utf-8').split(':', 1)[1].split()
tokens = [{'g': g, 'p': key[g]} if g in key else {'g': g, 'p': '?', 'cls': 'unk'} for g in groups]
data = {
    'slug': 'swieten1757',
    'anchor': 'r955',
    'title': 'R955, f. 141: the Hanau sentence',
    'caption': 'Van Swieten to Cobenzl, undated (1757-58), ARA Brussels SEG 1236 f. 141, DECODE R955: the 89 dotted groups of the ciphered sentence.',
    'unit': 'code groups',
    'key_note': 'Values of the 1757 table as aligned with the decipherment written under the numbers on the same page (targets/swieten1757/NOTES.md). The last groups, 400, 297 and 586, fall in "conclure même" and are not valued in that list.',
    'tokens': tokens,
}
(ROOT / 'docs' / 'reveal' / 'swieten1757.json').write_text(json.dumps(data, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(groups), 'groups,', sum(1 for t in tokens if t.get('cls') != 'unk'), 'valued')
