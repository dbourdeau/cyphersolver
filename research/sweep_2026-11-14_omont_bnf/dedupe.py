"""Which fr. numbers from summary.json already appear in the repo's ledgers/targets/sweeps (as 'fr. N', 'Français N', 'ms fr N' ...)?
usage: python dedupe.py summary.json known.json   (run from the repo root)"""
import json, re, sys, glob, os, collections
sm = json.load(open(sys.argv[1], encoding='utf8'))
frs = sorted({d['fr'] for d in sm})
files = ['catalogue.json', 'research/leads.json', 'CATALOGUE.md', 'SOLVED_CATALOGUE.md', 'README.md', 'decode_updates/queue.json']
for g in ['targets/*/NOTES.md', 'targets/*/profile.json', 'research/*/*.md', 'research/*/candidates.json', 'research/gallica_sweep/src/*.txt',
          'research/gallica_sweep/*.txt', 'research/gallica_sweep/ark_shelfmarks.json', 'research/gallica_siblings/*', 'research/sweep_2026-11*/*.json']:
    files += glob.glob(g)
rx = re.compile(r'(?:fr(?:an[cç]ais|an[cç]\.?)?\.?|ms\.?\s*fr\.?|B\.?n\.?F\.?(?:,)?\s*fr\.?|Dupuy|Colbert|Cinq|Baluze|Fonds fran[cç]ais)[^0-9\n]{0,12}((?:\d{3,5}(?:[,;/ ]+(?:and|et|&)?\s*)?)+)', re.I)
hit = collections.defaultdict(set)
for f in files:
    if not os.path.isfile(f) or os.path.getsize(f) > 60e6: continue
    t = open(f, encoding='utf8', errors='ignore').read()
    for m in rx.finditer(t):
        for n in re.findall(r'\d{3,5}', m.group(1)):
            n = int(n)
            if n in frs: hit[n].add(f)
# ranges "3484-3490"
json.dump({k: sorted(v) for k, v in hit.items()}, open(sys.argv[2], 'w'), indent=0)
print(len(frs), 'volumes;', len(hit), 'with a hit')
for n in frs:
    print(n, ' | '.join(sorted(os.path.basename(os.path.dirname(x)) + '/' + os.path.basename(x) for x in hit.get(n, []))[:4]))
