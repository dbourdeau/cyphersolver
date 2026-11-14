"""Reproduce explicit-hole body counts with the repository's unchanged v10 metric."""
from pathlib import Path
import sys,json
H=Path(__file__).resolve().parent; R=H.parents[2]
sys.path.insert(0,str(R/'research/reading_audit'))
import v10_relabel as v
record=json.loads((H/'reading_metrics.json').read_text())
for r in record['results']:
    w,h,d=v.share((H/'reading'/f"{r['message']}.md").read_text())
    share=round(1-(h+d)/(w+h),3)
    assert (w,h,d,w+h,share)==(r['words'],r['holes'],r['doubtful'],r['denominator'],r['read_share']),r['message']
    print(r['message'], 'words',w,'holes',h,'doubtful',d,'denominator',w+h,'read_share',share)
