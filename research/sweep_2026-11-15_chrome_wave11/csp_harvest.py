"""Wave 11: harvest British History Online, Calendar of State Papers Spain (vols 2-4, 1520s), node pages in order.
For every entry citing 'Salazar, A. N, f. M' record the entry text's cipher/deciphering remarks.  curl with 1.5 s pacing."""
import re, html, json, subprocess, time, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = []; titles = {}
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for n in range(lo, hi):
    r = subprocess.run(['curl', '-s', '-L', '-m', '40', '-A', 'Mozilla/5.0', f'https://www.british-history.ac.uk/node/{n}'], capture_output=True)
    t = r.stdout.decode('utf8', 'replace')
    m = re.search(r'<title>([^<|]*)', t); title = html.unescape(m.group(1)).strip() if m else ''
    titles[n] = title
    body = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
    ms = list(re.finditer(r'Salazar\s*[,.]?\s*A\.\s*(\d+)\s*[,.]?\s*f{1,2}\.\s*([\d,\- and\.]+?)(?=[\.;]\s|\s*<|\s*$|\s+[A-Z])', body))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        ent = body[m.end():end]      # the header (sender, date, ref) comes first, then the body and its notes
        hdr = body[max(0, m.start() - 160):m.end()]
        out.append(dict(node=n, page=title, vol=int(m.group(1)), fol=m.group(2).strip(), cipher=bool(re.search(r'cipher|cypher', ent[:-170] if i + 1 < len(ms) else ent, re.I)),
                        deciph=bool(re.search(r'deciphe', ent[:-170] if i + 1 < len(ms) else ent, re.I)), hdr=hdr, tail=ent[-500:]))
    print(n, title, len(body), file=sys.stderr); time.sleep(1.5)
json.dump(dict(titles=titles, entries=out), open(os.path.join(HERE, f'csp2_{lo}_{hi}.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
