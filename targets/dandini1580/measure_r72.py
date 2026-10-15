"""Measure R72 on its own key (14 Oct 2026, one-key split): share of parsed cipher tokens that get a value.
Run decrypt_r72.py first (it writes r72_parsed.json, the DP parse of SofPe's transcription in Lasry's frame).
Letter values: the R72 letter key in NOTES.md (C and M grades). Nomenclator: Lasry's ^ groups (D3190), which R72
shares, minus the groups NOTES lists as unread. Single-digit leftovers of the parse and code 32 (M, no letter
fixed) count as unread."""
import json, re, collections
R72 = {'a': '14 52 81', 'b': '16', 'c': '18 83', 'd': '20', 'e': '12 62', 'f': '41', 'g': '01 26', 'h': '42',
       'i': '30 72 24', 'l': '22', 'm': '34 96', 'n': '36', 'o': '38 82', 'p': '40 00', 'q': '90', 'r': '44',
       's': '46', 't': '28 48', 'u': '50 92', 'z': '11'}
letter = {c: l for l, cs in R72.items() for c in cs.split()}
nom = {}
for line in open('decode/DOC_R72_D3190_3190.txt', encoding='utf8'):
    m = re.match(r'^([\d|]+)(\+?)\s+- (.+)$', line.strip())
    if m and m.group(2):
        for c in m.group(1).split('|'):
            nom[c + '^'] = m.group(3)
UNREAD = {'766^', '866^', '030^', '448^'}
parsed = json.load(open('r72_parsed.json'))
n = collections.Counter()
for code, _ in parsed:
    if code.endswith('^'):
        n['nomenclator read' if code in nom and code not in UNREAD else 'nomenclator open'] += 1
    elif code in letter:
        n['letter read'] += 1
    else:
        n['unread (single digit, 32)'] += 1
total = len(parsed)
read = n['letter read'] + n['nomenclator read']
print(dict(n))
print(f'{read} of {total} tokens have a value ({read / total:.1%})')
