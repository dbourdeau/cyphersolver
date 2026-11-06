"""Western Diplomatica + Stedingk digitised volumes, with image-series id and image count -> units.json.
Input: enum.json (nad_enum.py). Image-series ids from sweep D's rik_vols.json where known, else the APE EAD <dao>.
Skips volumes sheeted by earlier sweeps (SKIP) and, in the Stedingk fonds, the Pomeranian family papers, accounts,
rolls and print (only Curt von Stedingk's diplomatic papers and correspondence are kept)."""
import json
import re
import sys
import time

from rik_common import count, dao

sys.stdout.reconfigure(encoding='utf-8')
SKIP = {
    'SE/RA/2105/I/A/11/14': 'Courtin 1657-60, sheeted 2 Nov (sweep_2026-11_riksarkivet_volumes)',
    'SE/RA/2113/2113.2/2': 'Orlik, Cosacica: viewed by sweep D (lead 2239)',
    'SE/RA/2113/2113.2/1a': 'Cosacica 1654-1721: viewed by sweep D (image 224 short postscript)',
    'SE/RA/2113/2113.2/1b': 'single Ottoman diploma for Orlik',
}
# Stedingk volume numbers (E-numbers) kept: drafts of despatches, royal letters, correspondence 1788-1812, state papers
STED_KEEP = set(range(6584, 6608)) | {6608, 6609, 6617} | set(range(6620, 6648)) | {6653, 6658, 6659} | \
    {6679, 6680, 6697, 6701, 6702, 6703, 6704, 6705, 6707, 6709, 6710, 6735}

e = json.load(open('enum.json', encoding='utf-8'))
known = {x['ref']: x for x in json.load(open('../sweep_2026-11_D_east_north/rik_vols.json', encoding='utf-8'))}
try:
    done = {u['ref']: u for u in json.load(open('units.json', encoding='utf-8'))}
except FileNotFoundError:
    done = {}
for x in e:
    ref = x['ref']
    if ref in SKIP or ref in done:
        continue
    if x['series'] == 'Stedingkska arkivet':
        m = re.search(r'E (\d{4})', ref.split('/')[-1])
        if not m or int(m.group(1)) not in STED_KEEP:
            continue
    u = dict(ref=ref, id=x['id'], series=x['series'], date=x.get('date'), caption=x.get('caption'), note=x.get('note'),
             path=x.get('path'), man=(known.get(ref) or {}).get('man'), n=(known.get(ref) or {}).get('n'))
    try:
        if not u['man']:
            u['man'] = dao(ref)
            time.sleep(1.2)
        if u['man'] and not u['n']:
            u['n'] = count(u['man'])
            time.sleep(1.2)
    except Exception as ex:
        u['err'] = str(ex)[:80]
    done[ref] = u
    print(ref.replace('SE/RA/', ''), u['man'], u['n'], flush=True)
    json.dump(list(done.values()), open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(list(done.values()), open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('units', len(done))
