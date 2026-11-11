#!/bin/sh
# DECODE RecordsList keyword search: prints the result count line and record rows. Usage: decode_q.sh "<term>"
curl -s -A 'Mozilla/5.0' -G 'https://de-crypt.org/decrypt-web/RecordsList' --data-urlencode "search=$1" --data 'cmd=search&searchtype=' | python3 -c "
import sys,re,html
t=sys.stdin.read()
m=re.search(r'Records? \d+ to \d+ of \d+|No records found',t); print(m.group(0) if m else 'no count')
for r in re.findall(r'<tr[^>]*data-rowindex.*?</tr>',t,flags=re.S)[:12]:
    print(' ',re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',r)))[:230])
"
sleep 2
