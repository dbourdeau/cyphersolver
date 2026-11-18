"""AtoM browse-search (plain curl): python atom.py <base> <term> [<term> ...]
Prints result count and, for each result row, its text (reference, level, title, snippet). Rows saved to atom_<host>.jsonl"""
import re, subprocess, sys, html, time, urllib.parse, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def fetch(url):
    return subprocess.run(["curl","-s","-m","45","-L",url],capture_output=True).stdout.decode("utf8","replace")
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def search(base, term, page=1):
    url = f"{base}/index.php/informationobject/browse?topLod=0&sort=relevance&query={urllib.parse.quote(term)}&page={page}"
    t = fetch(url)
    m = re.search(r'([\d,]+) results', t)
    n = int(m.group(1).replace(',','')) if m else 0
    rows = []
    for blk in re.split(r'<article', t)[1:]:
        blk = blk.split('</article>')[0]
        hrefs = re.findall(r'href="([^"#]+)"', blk)
        rows.append({"href": next((h for h in hrefs if '/index.php/' in h or h.count('-')>=1), ''), "text": clean(blk)[:400]})
    return n, rows, t
if __name__ == "__main__":
    base = sys.argv[1]; host = base.split('//')[1].split('/')[0]
    out = open(os.path.join(HERE, f"atom_{host}.jsonl"), "a", encoding="utf8")
    for term in sys.argv[2:]:
        n, rows, t = search(base, term)
        tot = rows[:]
        pg = 1
        while len(tot) < n and pg < 15 and rows:
            pg += 1; time.sleep(2.5)
            n2, rows, _ = search(base, term, pg); tot += rows
        print(f"{term!r} | {n} results | parsed {len(tot)}", flush=True)
        for r in tot:
            r["term"] = term; out.write(json.dumps(r, ensure_ascii=False) + "\n")
            print('   ', r['text'][:230])
        time.sleep(2.5)
