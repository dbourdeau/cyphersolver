"""Parse key/key25.md (repo copy, unchanged) into figure -> letter. Nulls and barred entries are not letters."""
import re
def load(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'\|\s*([a-z]{1,2})\s*\|\s*([\d ]+)\|', line)
        if m:
            for f in m.group(2).split():
                key[f] = m.group(1)
    return key
if __name__ == '__main__':
    import sys, json; print(json.dumps(load(sys.argv[1]), sort_keys=True))
