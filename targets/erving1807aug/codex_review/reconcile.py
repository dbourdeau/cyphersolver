#!/usr/bin/env python3
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent;P=R.parent
m=json.loads((R/'metrics.json').read_text());t=json.loads((R/'transcription_differences.json').read_text());fo=re.sub(r'\s+',' ',(P/'fo_99-01-02-1993.txt').read_text())
gaps=[{'gap':i,'context':fo[max(0,x.start()-70):x.end()+70]} for i,x in enumerate(re.finditer(r'⟨\s*⟩',fo),1)]
n=t['transcription_positions_after_duplicate_removed']
s={'literal_blank_gaps':len(gaps),'all_angle_spans':len(re.findall('⟨.*?⟩',fo)),
'reading_gap_variant_rows':sum('->' in x for x in (P/'reading.txt').read_text().split('=== Founders gaps/variants resolved by the code (group numbers) ===')[1].splitlines()),
'99pct_exact':100*m['99pct_non_X']/m['tokens'],
'claimed_recurrence_exact':100*m['claimed_recurrence_or_Wagner_any_value']/m['tokens'],
'nominal_with_all_transcription_positions':100*m['nominal_read']['tokens']/n,
'conservative_with_all_transcription_positions':100*m['unemended_image_secure']['tokens']/n,
'external_overlap_ceiling_percent':100*m['external_overlap_upper_tokens']/m['tokens'],
'no_external_group_overlap_tokens':m['tokens']-m['external_overlap_upper_tokens'],
'verdict_whitespace_words':len((R/'review.md').read_text().split()),'gaps':gaps}
assert s['verdict_whitespace_words']<400
assert s['literal_blank_gaps']==10
(R/'reconciliation.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps({k:v for k,v in s.items() if k!='gaps'},indent=2))
