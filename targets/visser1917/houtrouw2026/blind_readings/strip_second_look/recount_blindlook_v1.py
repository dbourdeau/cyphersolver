# recount_blindlook_v1.py -- Project Ciphers, catalogue 698, 18 Nov 2026 (model-written, claude-opus-5-5, session eea13873).
# A second count, made apart from the desk's script, of the blind second look at the key strip against this chat's
# strip letters. It parses the table on its own rules and prints the counts the desk gives in its message of 22:24Z.
# Decides nothing. Run:  python3 -I recount_blindlook_v1.py TABLE.txt STRIPLETTERS_v1.json OUT.json
import sys, json, re, hashlib

TABLE, LETTERS, OUT = sys.argv[1:4]

def parse_letter(cell):
    """'R? (A?)' -> ('r', ['a'], False); 'L + V?' -> ('lv', [], two letters); 'not read' -> (None, [], ...)."""
    cell = cell.strip()
    if cell == 'not read':
        return None, []
    if '+' in cell:
        return ''.join(p.strip().rstrip('?').lower() for p in cell.split('+')), []
    m = re.fullmatch(r'(\S+?)\??(?:\s*\(([^)]*)\))?', cell)
    first = m.group(1).rstrip('?').lower()
    alts = [a.strip().rstrip('?').lower() for a in re.split(r',|\bor\b', m.group(2) or '') if a.strip()]
    return first, alts

raw = open(TABLE, 'rb').read()
lines = raw.decode('utf-8').split('\n')
assert lines[0].split('\t') == ['Place', 'Letter', 'Sure', 'What the shape looks like'], lines[0]
blind = {}
for l in lines[1:]:
    if not l.strip():
        break
    place, letter, sure, shape = l.split('\t')
    first, alts = parse_letter(letter)
    blind[int(place)] = dict(cell=letter, first=first, alts=alts, sure_cell=sure,
                             sure=(sure.strip() == 'yes'), read=(first is not None))
assert sorted(blind) == list(range(1, 28)), sorted(blind)

sl = {s['place']: s for s in json.load(open(LETTERS, encoding='utf-8'))['signs']}
def grade(s):
    if s['letter'] is None:
        return 'not read'
    if s['sure']:
        return 'sure'
    return 'by order' if s['by_order'] else 'doubtful'

rows = []
for p in range(1, 28):
    s, b = sl[p], blind[p]
    rows.append(dict(place=p, chat_letter=s['letter'], chat_grade=grade(s),
                     blind_cell=b['cell'], blind_first=b['first'], blind_alts=b['alts'], blind_sure=b['sure_cell'],
                     first_agrees=(s['letter'] is not None and b['first'] == s['letter']),
                     chat_letter_among_alts=(s['letter'] is not None and s['letter'] in b['alts'])))

def places(f):
    return [r['place'] for r in rows if f(r)]

sure = [r for r in rows if r['chat_grade'] == 'sure']
order = [r for r in rows if r['chat_grade'] == 'by order']
unread = [r for r in rows if r['chat_grade'] == 'not read']
counts = {
    'chat sure': len(sure), 'chat by order': len(order), 'chat not read': len(unread),
    'chat sure: blind same first letter, marked sure': [r['place'] for r in sure if r['first_agrees'] and blind[r['place']]['sure']],
    'chat sure: blind same first letter, not marked sure': [r['place'] for r in sure if r['first_agrees'] and not blind[r['place']]['sure']],
    'chat sure: blind differs': [r['place'] for r in sure if not r['first_agrees']],
    'chat by order: blind read': [r['place'] for r in order if blind[r['place']]['read']],
    'chat by order: blind not read': [r['place'] for r in order if not blind[r['place']]['read']],
    'chat by order: blind same first letter': [r['place'] for r in order if r['first_agrees']],
    'chat by order: chat letter among blind alternates only': [r['place'] for r in order if r['chat_letter_among_alts'] and not r['first_agrees']],
    'chat by order: blind read, differs, chat letter not among its letters': [r['place'] for r in order if blind[r['place']]['read'] and not r['first_agrees'] and not r['chat_letter_among_alts']],
    'chat not read: blind not read either': [r['place'] for r in unread if not blind[r['place']]['read']],
    'chat not read: blind read': [r['place'] for r in unread if blind[r['place']]['read']],
    'blind marked sure (any part)': places(lambda r: 'yes' in blind[r['place']]['sure_cell']),
}
out = dict(what='a second count of the blind look against STRIPLETTERS_v1; decides nothing',
           table_sha256=hashlib.sha256(raw).hexdigest(),
           letters_sha256=hashlib.sha256(open(LETTERS, 'rb').read()).hexdigest(),
           counts=counts, rows=rows)
open(OUT, 'x', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
for k, v in counts.items():
    print(f'{k}: {v}')
