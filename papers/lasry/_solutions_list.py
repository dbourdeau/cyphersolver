"""The list of LLM solutions for George Lasry to edit and circulate (email 26 Sept 2026), as a Word file.

  python papers/lasry/_solutions_list.py      writes papers/lasry/llm-cipher-solutions.docx

Sections: keys recovered from ciphertext only; keys rebuilt from a plaintext found outside the collection; existing
keys found outside the collection; borderline cases found elsewhere in the same collection. Items, sources and
summaries are hand-kept in ct_sources.json; method, extent and the unpublished-prior note come from each profile.json.
Items are in date order within each section. Needs node with the docx package (npm install docx).
This script resolves the text into runs (plain, bold, link) in a payload that _solutions_doc.js lays out with docx-js.
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'docs'))
import _methods as M

SITE = 'https://dbourdeau.github.io/cyphersolver/'
DECODE = 'https://de-crypt.org/decrypt-web/RecordsView/'

SECTIONS = [
    ('ct', 'Keys recovered from ciphertext only',
     'The key was rebuilt from the ciphertext alone, with no plaintext and no existing key. Three items had also been '
     'solved earlier by George Lasry but never published; the LLMs solved them independently, and his unpublished '
     'solution is noted.'),
    ('extpt', 'Keys rebuilt from a plaintext found outside the collection',
     'The key was rebuilt by aligning the ciphertext with a plaintext found elsewhere: another archive, a printed '
     'edition or calendar, a website or article, or the decipherment of an unrelated record.'),
    ('extkey', 'Existing keys found outside the collection',
     'A key already existed but had not been connected with the document; it was found in another archive, volume, '
     'database record or publication and matched to the ciphertext.'),
    ('borderline', 'Borderline: key or plaintext found elsewhere in the same collection',
     'The key or plaintext came from the same collection (another volume or fonds, no link recorded before), not from '
     'a neighbouring record of the same file. Listed for a decision on whether they belong above.'),
]


def runs(text, links=(), decode=False):
    """Text as runs: DECODE record numbers become links, then ' · label' links are appended."""
    out, pos = [], 0
    if decode:
        for m in re.finditer(r'\bR(\d{2,5})\b', text):
            out.append({'t': text[pos:m.start()]})
            out.append({'t': m.group(0), 'url': DECODE + m.group(1)})
            pos = m.end()
    out.append({'t': text[pos:]})
    for label, url in links or ():
        out += [{'t': ' · '}, {'t': label, 'url': url}]
    return [r for r in out if r['t']]


def prior_note(prof):
    o, ps = prof['outcome'], prof['conditions'].get('prior_solution') or {}
    if o.get('first_break') != 'unpublished prior':
        return None
    where = ps.get('where', '')
    yr = next((w for w in ('2021', '2023', '2024') if f'in {w}' in where), '?')
    extra = ' (improved in February 2026)' if 'Feb 2026' in where else ''
    return [{'t': 'Solved independently by the LLMs', 'b': True},
            {'t': f', from the ciphertext alone and without knowledge of any earlier solution. In private '
                  f'communications, Lasry wrote that he had also solved it in {yr}{extra}, but his solution has '
                  'not been published.'}]


def item(it):
    prof = json.loads((ROOT / it['profile'] / 'profile.json').read_text(encoding='utf-8'))
    o = prof['outcome']
    method, ext = o.get('method', 'unknown'), M.extent(prof)
    if it.get('part'):
        part = next(x for x in o['parts'] if x['label'] == it['part'])
        method, ext = part['method'], part['extent']
    if it['section'] == 'ct':
        assert method == M.CT and o.get('first_break') is not False, it['slug']
    label = M.LABEL.get(method, method) + ' · ' + ext + (f' · split entry: {it["part"]} only' if it.get('part') else '')
    rows = [('Method', [{'t': label}]),
            ('Primary source', runs(it['primary'], it.get('primary_links'))),
            ('Secondary source', runs(it['secondary'], it.get('secondary_links'), decode=True))]
    if it.get('found'):
        rows.append(('Key or plaintext from', runs(it['found'], it.get('found_links'), decode=True)))
    if it.get('why'):
        rows.append(('Why borderline', [{'t': it['why']}]))
    note = prior_note(prof)
    if note:
        rows.append(('Independent solution', note))
    if it.get('cipherbrain'):
        rows.append(('Note', [{'t': 'also a Cipherbrain challenge (Klaus Schmeh)'}]))
    url = SITE + it['slug'] + '.html'
    rows.append(('Write-up', [{'t': url, 'url': url}]))
    return {'title': it['title'], 'date': it['date'], 'summary': it['summary'], 'rows': rows}


def year(it):
    m = re.search(r'\d{4}', it['date'])
    return int(m.group(0)) if m else 9999


def main():
    data = json.loads((HERE / 'ct_sources.json').read_text(encoding='utf-8'))
    secs = []
    for key, head, intro in SECTIONS:
        sec = sorted((i for i in data['items'] if i['section'] == key), key=year)
        items = [item(i) for i in sec]
        secs.append({'head': head, 'intro': intro, 'items': items})
    counts = {k: sum(1 for i in data['items'] if i['section'] == k) for k, _, _ in SECTIONS}
    payload = {
        'title': 'Historical ciphers solved with LLMs',
        'subtitle': (f'{counts["ct"]} keys recovered from ciphertext only; {counts["extpt"] + counts["extkey"]} keys or '
                     f'plaintexts found outside the collection; {counts["borderline"]} borderline cases. '
                     'List of 26 September 2026.'),
        'intro': ('The ciphers below were worked by large language models (Claude) in the cyphersolver project '
                  '(Daniel Bourdeau, with George Lasry). Each entry gives a short '
                  'summary, the primary source (the original document), the secondary source (where the item was '
                  'found: DECODE, Tomokiyo\'s cryptiana, Cipherbrain, a library catalogue), and a link to the full '
                  'write-up with transcription, key and reading. Cases where the key or a decipherment sat next to the '
                  'ciphertext in the same file are not listed.'),
        'site': SITE,
        'sections': secs,
        'excluded': [{'slug': x['slug'], 'why': x['why']} for x in data['excluded']],
    }
    pay = HERE / 'generated' / 'solutions_payload.json'
    pay.parent.mkdir(exist_ok=True)
    pay.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    out = HERE / 'llm-cipher-solutions.docx'
    subprocess.run(['node', str(HERE / '_solutions_doc.js'), str(pay), str(out)], check=True)
    print(', '.join(f'{k} {v}' for k, v in counts.items()), '->', out.name)


if __name__ == '__main__':
    main()
