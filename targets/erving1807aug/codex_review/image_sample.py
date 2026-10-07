#!/usr/bin/env python3
"""Human visual readings recorded 2026-10-04; compare to source, not OCR.
Purposive, legible runs from four frames plus Hanover spellings; not random.
The visual transcription is hard-coded so the comparison is reproducible.
"""
from pathlib import Path
import csv,re,json,hashlib
R=Path(__file__).resolve().parent;P=R.parent
# (crop, transcription line, distinctive literal cipher run, hand-read digits)
runs=[
('p362_03.jpg','0362.1','69.1651.32.424^.500.1290','69 1651 32 424^ 500 1290'),
('p363R_01.jpg','0363R.1','1514.916.244.579','1514 916 244 579'),
('p363R_01.jpg','0363R.1','1578.1481.1250.1203.957.1481.525.580^','1578 1481 1250 1203 957 1481 525 580^'),
('p365L_02.jpg','0365L.1','244.1372.383.1651.1219.359.97','244 1372 383 1651 1219 359 97'),
('p365L_02.jpg','0365L.1','1578.1651.1219.359.97.1680.553.1027','1578 1651 1219 359 97 1680 553 1027'),
('p367L_03.jpg','0367L.1','230.525.125.755.1635.1651.580^.133.1210','230 525 125 755 1635 1651 580^ 133 1210'),
('z362_han.jpg','0362.3','724.549.{9}43','724 549 943'),
('z363_han.jpg','0363L.1','724.549.943','724 549 943'),
('z364_han.jpg','0364L.1','244.724.549.934.1343','244 724 549 934 1343'),
]
lines={l.split('|')[0].strip():l.split('|')[1] for l in (P/'transcription.txt').read_text().splitlines() if '|' in l and not l.startswith('#')}
rows=[]
for crop,ref,s,read in runs:
    assert s in lines[ref],(ref,s)
    tokens=re.sub('[{}]','',s).split('.')
    assert len(tokens)==len(read.split())
    for i,(old,new) in enumerate(zip(tokens,read.split()),1):
        rows.append([crop,ref,s,i,old,new,re.sub(r'\D','',old)==re.sub(r'\D','',new)])
with (R/'image_sample.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['crop','source_ref','source_run','position_in_run','transcribed','visual','digit_match']);w.writerows(rows)
n=len(rows);errors=sum(not x[-1] for x in rows)
summary={'sampled_groups':n,'digit_errors':errors,'error_percent':100*errors/n,'sampling':'purposive legible runs; not blinded or random; no population error estimate', 'images':{x[0]:hashlib.sha256((P/'crops'/x[0]).read_bytes()).hexdigest() for x in runs}}
(R/'image_metrics.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
