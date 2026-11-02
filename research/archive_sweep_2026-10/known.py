"""Is this item already known here? Greps the repo's ledgers, targets, sweeps and the DECODE / Cryptoole dumps.

    python research/archive_sweep_2026-10/known.py "Add MS 32305" "R1579" "Esterházy"

Case-insensitive substring match; each hit prints the file and a snippet. An "R1234" term also matches the DECODE
record id 1234 in the list/view dumps.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILES = ['catalogue.json', 'research/leads.json', 'CATALOGUE.md', 'SOLVED_CATALOGUE.md', 'SOLVED_RANKING.md', 'README.md',
         'decode_updates/queue.json', 'research/cryptoole/snapshot.json',
         'research/catalogue_harvest/decode/views.jsonl', 'research/catalogue_harvest/decode/views_b.jsonl',
         'research/catalogue_harvest/decode/views_c.jsonl', 'research/catalogue_harvest/hcportal/index.json']
GLOBS = ['targets/*/NOTES.md', 'research/*/*.md', 'research/*/*/*.md', 'research/*/candidates.json',
         'research/vetting_2026-10/removed_*.json']


def texts():
    seen = set()
    paths = [os.path.join(ROOT, f) for f in FILES]
    for g in GLOBS:
        paths += sorted(glob.glob(os.path.join(ROOT, g)))
    for p in paths:
        if p in seen or not os.path.exists(p):
            continue
        seen.add(p)
        with open(p, encoding='utf-8', errors='replace') as fh:
            yield os.path.relpath(p, ROOT), fh.read()


def main(terms):
    corpus = list(texts())
    for term in terms:
        pats = [re.escape(term)]
        m = re.fullmatch(r'[Rr](\d+)', term)
        if m:
            pats = [rf'\bR{m.group(1)}\b', rf'"id": "{m.group(1)}"', rf'RecordsView/{m.group(1)}\b']
        rx = re.compile('|'.join(pats), re.I)
        hits = 0
        print(f'== {term}')
        for name, txt in corpus:
            for mm in rx.finditer(txt):
                a, b = max(0, mm.start() - 90), min(len(txt), mm.end() + 90)
                print(f'  {name}: ...{txt[a:b]}...'.replace('\n', ' '))
                hits += 1
                if hits >= 12:
                    break
            if hits >= 12:
                print('  (more hits not shown)')
                break
        if not hits:
            print('  no hits')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(sys.argv[1:])
