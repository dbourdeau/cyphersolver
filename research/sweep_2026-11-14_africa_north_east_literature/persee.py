#!/usr/bin/env python3
"""Persee full-text search (HTML) -> titles of hits. usage: persee.py "query" ... ; prints total and first page titles."""
import sys, re, time, subprocess, urllib.parse, html
for q in sys.argv[1:]:
    url = 'https://www.persee.fr/search?ta=article&q=' + urllib.parse.quote(q)
    r = subprocess.run(['curl', '-s', '-m', '40', '-A', 'Mozilla/5.0 (research sweep)', url], capture_output=True)
    t = r.stdout.decode('utf8', 'replace')
    m = re.search(r'([\d\s  ]+)\s*(?:résultats?|document)', t)
    tot = re.findall(r'class="[^"]*(?:count|total|nb)[^"]*"[^>]*>\s*([^<]{1,40})<', t)[:2]
    print('##', q, '| total?', tot, m.group(0).strip() if m else '')
    seen = set()
    for href, title in re.findall(r'<a href="https://www\.persee\.fr(/doc/[^"?]+)[^"]*" class="title[^"]*">(.*?)</a>', t, re.S):
        title = re.sub(r'<[^>]+>', '', html.unescape(title)).strip()
        if title and href not in seen:
            seen.add(href); print('  ', href, '|', title[:120])
    time.sleep(2.5)
