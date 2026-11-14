#!/usr/bin/env python3
"""Durham University Library Archives & Special Collections (XTF, reed.dur.ac.uk) keyword search; plain curl works.
usage: durham.py TERM ... ; prints total, collections and hit counts (2 pages max). Includes Sudan Archive / Middle East Documentation Unit."""
import sys, re, html, time, subprocess, urllib.parse
for q in sys.argv[1:]:
    for p in (1, 2, 3):
        url = 'https://reed.dur.ac.uk/xtf/search?keyword=%s&startDoc=%d' % (urllib.parse.quote(q), (p-1)*10+1)
        t = subprocess.run(['curl', '-s', '-m', '30', '-A', 'Mozilla/5.0 (research sweep)', url], capture_output=True).stdout.decode('utf8', 'replace')
        m = re.search(r'Results:\s*(?:<[^>]*>\s*)*([\d,]+)\s*Items', t)
        if p == 1: print('###', q, m.group(1) if m else '0')
        rows = re.findall(r'(\d+) hits?\s*</?[^>]*>?\s*.*?<a href="(view\?docId=[^"]+)"[^>]*>(.*?)</a>', t, re.S)
        for n, h, tit in re.findall(r'(\d+)\s+hits?.*?<a href="(view\?docId=[^";]+)[^"]*"[^>]*>(.*?)</a>', t, re.S):
            print('  ', n, h, '|', re.sub(r'<[^>]+>', '', html.unescape(tit)).strip()[:90])
        time.sleep(2.5)
        if 'Next' not in t: break
