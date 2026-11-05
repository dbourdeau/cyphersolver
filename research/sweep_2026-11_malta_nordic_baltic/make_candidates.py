# Builds candidates.json for the Malta / Nordic / Baltic sweep (Nov 2026). No source yielded a qualifying row, so it is empty.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = []
json.dump(R, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'rows')
