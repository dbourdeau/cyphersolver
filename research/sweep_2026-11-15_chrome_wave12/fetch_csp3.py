"""Wave 12: save the full body text of BHO Calendar of State Papers Spain vol. 3 pages for 1525-29 (nodes 74485-74700), 1.5 s pacing."""
import re, html, subprocess, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
for n in range(74485, 74701):
    p = os.path.join(HERE, 'csp3_pages', f'{n}.txt')
    if os.path.exists(p): continue
    t = subprocess.run(['curl', '-s', '-L', '-m', '40', '-A', 'Mozilla/5.0', f'https://www.british-history.ac.uk/node/{n}'], capture_output=True).stdout.decode('utf8', 'replace')
    b = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
    i = b.find('Keyword Highlight Search')
    open(p, 'w', encoding='utf8').write(b[i:] if i >= 0 else b)
    time.sleep(1.5)
