"""Word pass over all rolls of NARA M1194 (RG 165 MID name index, series naId 2824985), 11 Nov 2026.

Usage: python3 m1194_scan.py <scratch dir>
Needs <scratch>/nara/rolls.json ({naId: title}, from /proxy/records/parentNaId/2824985?limit=100&page=N).
Reads each roll's OCR from /proxy/extractedText/<naId>?limit=1000&page=N (2 s apart) and writes every frame whose
OCR matches WORD to <scratch>/nara/hits.jsonl, with a 'fail' flag when a failure phrase is near. Resumable.
"""
import json, os, re, sys, time, urllib.request

S = sys.argv[1]
WORD = re.compile(r'\b(ciphers?|cyphers?|ciphered|decipher\w*|decypher\w*|undecipher\w*|cryptogra\w*|'
                  r'code (?:message|letter|telegram)s?|in code|secret writing)\b', re.I)
FAIL = re.compile(r'undecipher|undecypher|not (?:been )?(?:able to )?(?:be )?(?:decipher|decod|solv|read)|unable to|'
                  r'could not|cannot|can not|impossible|no key|unsolved|without (?:result|success)|failed', re.I)
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'}
rolls = json.load(open(os.path.join(S, 'nara', 'rolls.json')))
donef = os.path.join(S, 'nara', 'done.txt')
done = set(open(donef).read().split()) if os.path.exists(donef) else set()
out = open(os.path.join(S, 'nara', 'hits.jsonl'), 'a')
for naid, title in rolls.items():
    if naid in done:
        continue
    page, ok = 1, True
    while True:
        url = f'https://catalog.archives.gov/proxy/extractedText/{naid}?limit=1000&page={page}'
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read())
        except Exception as e:
            print('ERR', naid, page, e, flush=True)
            ok = False
            break
        objs = d.get('digitalObjects') or []
        for i, o in enumerate(objs):
            t = o.get('extractedText') or ''
            for m in WORD.finditer(t):
                ctx = ' '.join(t[max(0, m.start() - 300):m.end() + 300].split())
                out.write(json.dumps({'naId': naid, 'roll': title, 'objectId': o.get('objectId'),
                                      'frame': (page - 1) * 1000 + i + 1, 'word': m.group(0),
                                      'fail': bool(FAIL.search(ctx)), 'ctx': ctx}) + '\n')
        out.flush()
        time.sleep(2)
        if page * 1000 >= int(d.get('total') or 0) or not objs:
            break
        page += 1
    if ok:
        open(donef, 'a').write(naid + '\n')
        print('done', naid, title, flush=True)
