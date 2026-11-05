# Run syl.py's `real` with wsa5: append GCLS lines so that 3-letter code groups sharing initial and final letter
# (Lannoy's rule) are pushed towards words with the same first letter. Usage: SOLVER=./wsa5 ... python3 real5.py TOKENS
import sys, collections, syl
_task2 = syl.task2
def task2(toks, signs, groups, ws, fix={}):
    t = _task2(toks, signs, groups, ws, fix)
    cls = collections.defaultdict(list)
    for i, g in enumerate(groups):
        if len(g) == 3: cls[(g[0], g[2])].append(i)
    cid = 0; extra = []
    for k, ids in sorted(cls.items()):
        if len(ids) < 2: continue
        extra += [f'GCLS {i} {cid}' for i in ids]; cid += 1
    print('classes with 2+ groups:', cid, 'groups in them:', len(extra), file=sys.stderr)
    return t + '\n'.join(extra) + '\n'
syl.task2 = task2
if __name__ == '__main__':
    syl.real(sys.argv[1])
