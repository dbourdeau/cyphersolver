"""Fetch Lambeth CalmView records and print the sentences around cipher words.

    python research/sweep_2026-11-13_lambeth/calm_record.py <outdir> "<record id as in the URL>" [...]

One request every 3 s. Saves <outdir>/rec_<n>.html and prints the field table as text, cut to the cipher context.
"""
import html, os, re, subprocess, sys, time

URL = 'https://archives.lambethpalacelibrary.org.uk/CalmView/Record.aspx?src=CalmView.Catalog&id='
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
WORDS = re.compile(r'c[iy]pher|deciph|decyph|cifra|in code|characters', re.I)

outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)
for n, rid in enumerate(sys.argv[2:], 1):
    out = os.path.join(outdir, 'rec_' + re.sub(r'\W+', '_', rid) + '.html')
    r = subprocess.run(['curl', '-sS', '-A', UA, '-m', '60', '-L', '-o', out, '-w', '%{http_code}', URL + rid],
                       capture_output=True, text=True)
    time.sleep(3)
    page = open(out, encoding='utf-8', errors='replace').read()
    m = re.search(r'<table[^>]*summary="Record View".*?</table>', page, re.S) or re.search(r'<table.*</table>', page, re.S)
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', m.group(0) if m else page)))
    print(f'== {rid}  HTTP {r.stdout}  {len(text)} chars')
    print('   head:', text[:330])
    for mm in WORDS.finditer(text):
        print('   ...' + text[max(0, mm.start() - 380):mm.end() + 380] + '...')
