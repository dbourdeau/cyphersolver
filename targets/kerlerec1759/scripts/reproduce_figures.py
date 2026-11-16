"""Re-run every figure in NOTES.md from files in this folder.
Usage (from the repository root or anywhere): python3 -I targets/kerlerec1759/scripts/reproduce_figures.py [n_shuffles=200]

1. Held-out test (test/TEST_PLAN.md, test/TEST_PLAN_followup.md), no. 228 ff. 48v-49r, 253 groups, for:
   a. key/key_manuscript_frozen.tsv (clerks' key of the first test)                        -> 78.3%
   b. union of the two committed key files, key_manuscript.tsv + pusch_values_used.tsv     -> 91.7%
      (the first test's 96.0% used Pusch's full printed table, which is not in this folder)
   c. key/key_clerks_only_frozen.tsv, d. key/key_clerks_enlarged_frozen.tsv (follow-up)
2. sha256 of the frozen keys and plans against the recorded values.
3. Coverage of nos. 206, 207, 215 and the list of decoded changes (scripts/compare_decodes.py).
"""
import hashlib, os, subprocess, sys, tempfile

here = os.path.dirname(os.path.abspath(__file__))
td = os.path.dirname(here)
n = sys.argv[1] if len(sys.argv) > 1 else '200'
held = os.path.join(td, 'transcriptions/heldout_no228_1760-06-12.txt')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run(args):
    return subprocess.run([sys.executable, '-I'] + args, capture_output=True, text=True, check=True).stdout


print('== hashes')
for rec in ('test/TEST_PLAN.sha256', 'test/TEST_PLAN_followup.sha256', 'test/TEST_PLAN_followup.plan.sha256'):
    p = os.path.join(td, rec)
    if not os.path.exists(p):
        continue
    for l in open(p):
        if not l.strip():
            continue
        h, f = l.split()[:2]
        fp = os.path.join(td, f) if os.path.exists(os.path.join(td, f)) else os.path.join(td, 'test', os.path.basename(f))
        if os.path.exists(fp):
            print('%s %s %s' % ('OK  ' if sha(fp) == h else 'DIFF', h[:12], f))
        else:
            print('n/a  %s %s (file not in folder)' % (h[:12], f))

print('== held-out test,', n, 'shuffles')
with tempfile.TemporaryDirectory() as tmp:
    union = os.path.join(tmp, 'union_committed_keys.tsv')
    with open(union, 'w', encoding='utf-8') as f:
        seen = set()
        for kf in ('key/key_manuscript.tsv', 'key/pusch_values_used.tsv'):
            for l in open(os.path.join(td, kf), encoding='utf-8'):
                if l[0].isdigit():
                    c, v = l.split('\t')[:2]
                    if c not in seen:
                        seen.add(c); f.write('%s\t%s\n' % (c, v))
    for label, k in (('a. clerks key of the first test', os.path.join(td, 'key/key_manuscript_frozen.tsv')),
                     ('b. committed keys together', union),
                     ('c. follow-up clerks-only key', os.path.join(td, 'key/key_clerks_only_frozen.tsv')),
                     ('d. follow-up enlarged clerks key', os.path.join(td, 'key/key_clerks_enlarged_frozen.tsv'))):
        print(label)
        print('   ' + run([os.path.join(here, 'heldout_test.py'), k, held, n]).replace('\n', '\n   ').rstrip())

print('== nos. 206, 207, 215')
print(run([os.path.join(here, 'compare_decodes.py'), td]))
