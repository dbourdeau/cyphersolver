"""Check the frozen files against their recorded sha256 and rerun both held-out tests.
Run from the target folder: python scripts/run_tests.py

Expected (recorded before this package was made):
  round 2, key v1 on Codex 534 f. 15r: 39 of 39 covered pairs; 200 shuffled keys at most 28.2%
  round 3, key v2 on Codex 534 f. 21r: 76 of 92 = 82.6%; 200 shuffled keys at most 35.9%, mean 23.9%
"""
import hashlib, subprocess, sys

FROZEN = {
    'key/key_v1.json': '8bedce853bb0d5d9d576117a6136c4024cb843e57302ef153ccff4c28686005f',
    'key/key_v2.json': '64783ab82d6e35fe68db16badd5a882ee80d66ab2686f3b1f1f4bd81375b8c20',
    'key/key_v3.json': 'bdc8b174fa08ca22176f4c73c540108718cf5a64f037e94be6afddbb3b87bc21',
    'key/key_v3_context.json': 'f5115d3872160fd5f714766a15a1c1538cc14cbe5a171c21ad742a17f33d8e72',
    'test/heldout_21r_cipher.tsv': '0727229d65547cd1910101579c30b2ddfc94fb0b4760ec7ee3fb3d52ce81b5a1',
    'transcriptions/reconciled_533.tsv': 'd1ec7443c95bfbacbcf8319c9fbf3ba247e51279c875b5ec3ebb7bed1c51b942',
    'transcriptions/reconciled_533_v2.tsv': 'd2866b78d2872b2711ad8751502f2b164515100949b98fb8b5241c23cac9e2c5',
    'readings/verify/montauti_1r1v_PART1_blind.md': '3e37c4f02a8d49c6d4b5edaf057018db23b3662b0e462ab1f0285db3308bafa8',
}
ok = True
for f, h in FROZEN.items():
    got = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    print(('ok  ' if got == h else 'FAIL'), f, got[:12])
    ok &= got == h

def run(args):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True).stdout.strip().splitlines()[-1]

r2 = run(['scripts/heldout_test.py', 'key/key_v1.json', 'test/heldout_534_f15r.tsv'])
r3 = run(['scripts/heldout_align.py', 'key/key_v2.json', 'test/heldout_21r_cipher.tsv', 'test/heldout_21r_interline.tsv'])
print('round 2:', r2)
print('round 3:', r3)
ok &= 'real key 100.0%' in r2 and 'shuffled max 28.2%' in r2
ok &= 'REAL 76/92 = 82.6%' in r3 and 'shuffled max 35.9%' in r3
print('result:', 'pass' if ok else 'FAIL')
sys.exit(0 if ok else 1)
