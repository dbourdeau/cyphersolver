import json, sys
e = json.load(open('ctts/hand_edits.json'))
for k, v in json.loads(sys.argv[1]).items(): e[k] = v
json.dump(e, open('ctts/hand_edits.json', 'w'), indent=0); print(len(e), 'lines with edits')
