"""Own decoder (integration of issue #556, 14 Nov 2026), not the contributor's verify.py: apply aaymeloglu/key.json to
aaymeloglu/transcription.txt and compare with the 'printed' lines of aaymeloglu/reading.txt. Standard library only.
    python3 own_decode.py"""
import json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aaymeloglu')
key = {k: v['value'] for k, v in json.load(open(os.path.join(H, 'key.json'))).items() if not k.startswith('_')}
runs = {}
for line in open(os.path.join(H, 'transcription.txt')):
    if line.startswith('P'):
        tag, body = line.split(':', 1)
        runs[tag] = body.split()
theirs, cur = {}, None
for line in open(os.path.join(H, 'reading.txt')):
    if line.startswith('P'):
        cur = line.strip()
    elif 'printed:' in line:
        theirs[cur] = line.split('printed:')[1].strip()
same = 0
for tag, groups in runs.items():
    mine = ''.join(key.get(g, '?') for g in groups)
    same += mine == theirs.get(tag)
    print(tag, mine)
print(same, 'of', len(runs), 'runs identical to reading.txt;', sum(map(len, runs.values())), 'groups')
