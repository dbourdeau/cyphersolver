"""Fetch CalmView records and print description text. CALM_BASE=... python calm_record.py <id> ... (id as in result list, e.g. 'XJC%2f1%2f1%2f8%2f57' or JC/1/1/8/57)"""
import html, os, re, subprocess, sys, time, urllib.parse
BASE = os.environ.get('CALM_BASE', 'https://calmview.bham.ac.uk/')
for rid in sys.argv[1:]:
    rid = urllib.parse.unquote(rid)
    u = BASE + 'Record.aspx?src=CalmView.Catalog&id=' + urllib.parse.quote(rid, safe='')
    t = subprocess.run(['curl','-s','-m','60','-L','-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf8','replace')
    m = re.search(r'<table class="DetailsTable".*?</table>', t, re.S) or re.search(r'<div[^>]*id="[^"]*Details[^"]*".*', t, re.S)
    body = m.group(0) if m else t
    txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body))).strip()
    pat = os.environ.get('GREP')
    if pat:
        print('==', rid)
        for m in re.finditer(pat, txt, re.I):
            print('   ...', txt[max(0, m.start()-250):m.end()+250], '...')
    else:
        print('==', rid, '\n', txt[:int(os.environ.get('N','1800'))], '\n')
    time.sleep(3)
