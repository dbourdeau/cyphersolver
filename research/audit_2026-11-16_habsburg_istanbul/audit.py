"""Same-letter audit of 'no decipherment' cipher items in Hungaricana's Viennese-inventory regests (HHStA Türkei I and others).
For each item (a regest id): read the regest in full; list its Konvolut (search on the quoted shelfmark prefix, every page);
take every Konvolut regest whose date string shares a day with the item (range dates included) or carries no full date,
plus every regest found by a quoted date search for each of the item's days; read those regests in full.
Usage: python -I -X utf8 audit.py items.json out.jsonl
items.json: [{"group": "2237", "id": 49853, "konv": optional quoted-search string}, ...]
Caches: raw/regests.jsonl (own) and ../vetting_2026-11-16_w20_b12/raw/regests.jsonl (read only); raw/konv/*.jsonl; raw/dates/*.jsonl.
Polite: one request per 1.2 s."""
import base64, json, os, re, sys, time, html, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'raw')
os.makedirs(os.path.join(RAW, 'konv'), exist_ok=True)
os.makedirs(os.path.join(RAW, 'dates'), exist_ok=True)


def get(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                t = r.read().decode('utf8', 'replace')
            time.sleep(1.2)
            return t
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError('failed ' + url)


CACHE = {}
for p in [os.path.join(HERE, '..', 'vetting_2026-11-16_w20_b12', 'raw', 'regests.jsonl'), os.path.join(RAW, 'regests.jsonl')]:
    if os.path.exists(p):
        for l in open(p, encoding='utf8'):
            r = json.loads(l)
            if 'error' not in r and r.get('ref'):
                CACHE[r['id']] = r
OWN = open(os.path.join(RAW, 'regests.jsonl'), 'a', encoding='utf8')


def regest(i):
    if i in CACHE:
        return CACHE[i]
    t = get(f'https://archives.hungaricana.hu/en/lear/BecsSeg/{i}/')
    t = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', t))).split())
    k = t.find('Reference code')
    seg = t[k:t.find('Links Print metadata', k)] if k >= 0 else ''
    f = lambda a, b: (re.search(re.escape(a) + r'\s*(.*?)\s*(?:' + b + r'|$)', seg) or [None, ''])[1]
    r = {'id': i, 'ref': f('Reference code', 'Database'), 'date': f('Date of Creation', 'Description|Links'),
         'desc': f('Description', 'Links|$')}
    CACHE[i] = r
    OWN.write(json.dumps(r, ensure_ascii=False) + '\n'); OWN.flush()
    return r


def parse(t):
    out = []
    for blk in t.split('list-group-item bg-light mb-2 result')[1:]:
        m = re.search(r'lear/BecsSeg/(\d+)/[^>]*>\s*(.*?)\s*</a>', blk, re.S)
        if not m:
            continue
        d = re.search(r'Date of Creation</strong></td>\s*<td>(.*?)</td>', blk, re.S)
        clean = lambda x: ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', x)).split()) if x else ''
        out.append({'id': int(m.group(1)), 'ref': clean(m.group(2)), 'date': clean(d.group(1) if d else '')})
    return out


def search(q, cachefile, maxp=15):
    if os.path.exists(cachefile):
        return [json.loads(l) for l in open(cachefile, encoding='utf8')]
    lst = base64.b64encode(json.dumps({'query': q}).encode()).decode().rstrip('=')
    seen, rows = set(), []
    for p in range(1, maxp + 1):
        hits = parse(get(f'https://archives.hungaricana.hu/en/lear/search/results/?list={lst}&per_page=100&page={p}'))
        new = [h for h in hits if h['id'] not in seen]
        for h in new:
            seen.add(h['id']); rows.append(h)
        if len(hits) < 100 or not new:
            break
    with open(cachefile, 'w', encoding='utf8') as f:
        for h in rows:
            f.write(json.dumps(h, ensure_ascii=False) + '\n')
    return rows


def days(s):
    """Every yyyy.mm.dd named in a date string, ranges and abbreviated follow-ons included."""
    s = s.replace('0I', '01')
    out = set()
    for m in re.finditer(r'(\d{4})\.\s?(\d{1,2})\.\s?(\d{1,2})\b(?:\s*-\s*(\d{1,2})\b)?', s):
        y, mo, d = m.group(1), int(m.group(2)), int(m.group(3))
        if mo == 0 or d == 0:
            continue
        out.add(f'{y}.{mo:02d}.{d:02d}')
        if m.group(4):
            for dd in range(d + 1, int(m.group(4)) + 1):
                out.add(f'{y}.{mo:02d}.{dd:02d}')
        tail = s[m.end():]
        tail = re.split(r'\d{4}\.', tail)[0]
        for mm in re.finditer(r'(?<![\d.])(\d{2})\.(\d{2})\b', tail):
            out.add(f'{y}.{int(mm.group(1)):02d}.{int(mm.group(2)):02d}')
        for mm in re.finditer(r'(?:és|,|\.)\s+(\d{1,2})\.(?!\d)', tail):
            out.add(f'{y}.{mo:02d}.{int(mm.group(1)):02d}')
    return out


def konv_query(ref):
    r = ' '.join(ref.replace(' .', '.').split())
    m = re.search(r'Türkei I\.\s*(Karton|Kt\.)\s*(\d+)\.\s*Konv\.\s*(\d+)', r)
    if m:
        if m.group(1) == 'Karton':
            return f'"Türkei I. Karton {m.group(2)}. Konv. {m.group(3)}."'
        return f'"Türkei I. Kt. {m.group(2)}. Konv.{m.group(3)}"'
    m = re.search(r'(Fasc\. \d+\. Konv\. [A-Z]\.)', r)
    if m:
        return f'"{m.group(1)}"'
    return None


def same_konv(ref_a, ref_b):
    norm = lambda r: re.sub(r'\s+', '', r.replace('Karton', 'Kt.'))
    ka = re.search(r'(Kt\.\d+\.Konv\.?\d+|Fasc\.\d+\.Konv\.[A-Z])', norm(ref_a))
    kb = re.search(r'(Kt\.\d+\.Konv\.?\d+|Fasc\.\d+\.Konv\.[A-Z])', norm(ref_b))
    return bool(ka and kb and ka.group(1) == kb.group(1))


def main():
    items = json.load(open(sys.argv[1], encoding='utf8'))
    outp = sys.argv[2]
    done = set()
    if os.path.exists(outp):
        done = {(json.loads(l)['group'], json.loads(l)['id']) for l in open(outp, encoding='utf8')}
    with open(outp, 'a', encoding='utf8') as out:
        for it in items:
            if (it['group'], it['id']) in done:
                continue
            r = regest(it['id'])
            q = it.get('konv') or konv_query(r['ref'])
            ds = days(r['date'])
            cands = {}
            if q:
                kfile = os.path.join(RAW, 'konv', re.sub(r'\W+', '_', q).strip('_') + '.jsonl')
                for h in search(q, kfile):
                    if h['id'] == it['id'] or not same_konv(h['ref'], r['ref']):
                        continue
                    hd = days(h['date'])
                    if (hd & ds) or not hd:
                        cands[h['id']] = 'konv-' + ('date' if hd & ds else 'undated')
            for d in sorted(ds):
                for h in search(f'"{d}"', os.path.join(RAW, 'dates', d + '.jsonl'), maxp=3):
                    if h['id'] != it['id'] and ('Türkei' in h['ref'] or same_konv(h['ref'], r['ref'])):
                        cands.setdefault(h['id'], 'datesearch')
            rows = []
            for cid, how in sorted(cands.items()):
                c = regest(cid)
                rows.append(dict(c, how=how))
            out.write(json.dumps({'group': it['group'], 'id': it['id'], 'item': r, 'konv_query': q, 'days': sorted(ds),
                                  'cands': rows}, ensure_ascii=False) + '\n')
            out.flush()
            print(it['group'], it['id'], r['date'], len(rows), flush=True)


if __name__ == '__main__':
    main()
