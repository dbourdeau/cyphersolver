# Balkans / Greece sweep, 2 Nov 2026. No row survived the checks (see README.md), so candidates.json is empty.
# Rows would use the format of research/chrome_pass_2026-11/make_candidates.py.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = []
with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)
print(len(R))
