#!/usr/bin/env python3
"""Parse helper transcription files (C:/G:/F:/CW: lines) into a list of despatches.
Each despatch: list of blocks in page order: ('G', text) / ('F', [tokens]) / ('C', text) / page markers."""
import re, sys, glob, os, json
def parse(path):
    d = {'file': path, 'head': '', 'items': []}
    page = ''
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if line.startswith('# despatch:'): d['head'] = line[11:].strip(); continue
        if line.startswith('## '): page = line[3:].strip(); d['items'].append(('P', page)); continue
        if line.startswith('G:'):
            d['items'].append(('G', line[2:].strip()))
        elif line.startswith('F:'):
            toks = []
            for t in line[2:].split():
                m = re.match(r'^(\d+)(\{[^}]*\})?(_)?[.:,;]*(_)?[.:,;—-]*$', t)
                if m:
                    toks.append({'n': int(m.group(1)), 'alt': (m.group(2) or '').strip('{}'), 'ul': bool(m.group(3) or m.group(4)), 'raw': t})
                else:
                    toks.append({'w': t})
            d['items'].append(('F', toks))
        elif line.startswith('C:'):
            d['items'].append(('C', line[2:].strip()))
        elif line.startswith('CW:'):
            d['items'].append(('CW', line[3:].strip()))
    return d
if __name__ == '__main__':
    files = sorted(glob.glob('h?/*.txt')) + sorted(glob.glob('mine/n3[67]_mine.txt'))
    tot = 0; allg = []
    for f in files:
        d = parse(f)
        nums = [t for k, v in d['items'] if k == 'F' for t in v if 'n' in t]
        odd = [t['w'] for k, v in d['items'] if k == 'F' for t in v if 'w' in t]
        gl = [v for k, v in d['items'] if k == 'G' and v != '(none)']
        words = sum(len(re.findall(r"[A-Za-z][A-Za-z'’.:]*", g)) for g in gl)
        print(f, '|', d['head'][:60], '| nums', len(nums), 'ul', sum(t['ul'] for t in nums), 'alt', sum(bool(t['alt']) for t in nums), 'words', words, '| nonnum:', ' '.join(odd)[:150])
        tot += len(nums); allg += [t['n'] for t in nums]
    from collections import Counter
    c = Counter(allg)
    print('total', tot, 'distinct', len(c), 'max', max(allg), 'min', min(allg))
    print('most common', c.most_common(40))
    print('freq of freq', sorted(Counter(c.values()).items()))
