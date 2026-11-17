#!/usr/bin/env python3
"""Print cipher/cypher contexts from a Durham XTF finding-aid record. usage: durham_ctx.py docId(ark/....xml) [term-regex]"""
import sys, re, html, subprocess, urllib.parse
doc = sys.argv[1]; pat = re.compile(sys.argv[2] if len(sys.argv) > 2 else r'ciph|cyph|crypt|in code|code-?word|secret writing', re.I)
url = 'https://reed.dur.ac.uk/xtf/view?docId=%s;doc.view=entire_text' % doc
t = subprocess.run(['curl', '-s', '-m', '60', '-A', 'Mozilla/5.0 (research sweep)', url], capture_output=True).stdout.decode('utf8', 'replace')
title = re.search(r'<title>(.*?)</title>', t, re.S)
print('##', doc, title.group(1).strip()[:100] if title else '', len(t))
txt = re.sub(r'<[^>]+>', ' ', t); txt = html.unescape(re.sub(r'\s+', ' ', txt))
last = -999
for m in pat.finditer(txt):
    if m.start() - last < 250: continue
    last = m.start(); print('   ...', txt[max(0, m.start()-220):m.start()+280])
