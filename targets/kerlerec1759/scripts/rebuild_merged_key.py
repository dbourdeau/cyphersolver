"""Rebuild the frozen merged key of the first held-out test (13 Nov 2026) and re-score it, for anyone with Pusch 2008.

Usage (from the repository root or anywhere):
  python3 -I targets/kerlerec1759/scripts/rebuild_merged_key.py <pusch_table.tsv> [n_shuffles=200]

<pusch_table.tsv> is Table 2 of Donald E. Pusch, "Kerlérec's Cipher: The Code Book of Louisiana's Last French
Governor", Louisiana History 49:4 (Fall 2008), pp. 463-480 (Table 2 on pp. 477-480; https://www.jstor.org/stable/25478601),
typed by the user, one row per code: code<TAB>value (several values separated by commas; an accented letter that an OCR printed
as '?' is accepted). It is not in this folder because it would reproduce his published table.

The merged key is the first round's clerks' pairs (key/pairs_build.tsv, nos. 194 and 228) with Pusch's value for every
code that has no clerk's pair (scripts/build_key.py, unchanged since the first test). The script builds it in a
temporary folder, compares its sha256 with the value frozen in test/TEST_PLAN.md
(b54686fb...cba89), and runs the held-out test of test/TEST_PLAN.md on no. 228 ff. 48v-49r. With our local
extraction of the table (accents printed as '?') the hash matches and the score is 243 of 253 (96.0%). A table typed
afresh from the book will usually differ in spelling or accents, so the hash may differ and the score move slightly.
"""
import hashlib, os, subprocess, sys, tempfile

FROZEN = 'b54686fb9b253cd0f1d089539fe0e4ace3ea4f0f0f949e6550ecc2c4b85cba89'
here = os.path.dirname(os.path.abspath(__file__))
td = os.path.dirname(here)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    table = os.path.abspath(argv[0])
    n = argv[1] if len(argv) > 1 else '200'
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, '-I', os.path.join(here, 'build_key.py'),
                        os.path.join(td, 'key/pairs_build.tsv'), table, tmp], check=True, capture_output=True)
        merged = os.path.join(tmp, 'key_merged.tsv')
        h = hashlib.sha256(open(merged, 'rb').read()).hexdigest()
        print('merged key sha256', h, '(frozen value: %s)' % ('same' if h == FROZEN else 'DIFFERENT, ' + FROZEN))
        out = subprocess.run([sys.executable, '-I', os.path.join(here, 'heldout_test.py'), merged,
                              os.path.join(td, 'transcriptions/heldout_no228_1760-06-12.txt'), n],
                             check=True, capture_output=True, text=True).stdout
        print(out.rstrip())


if __name__ == '__main__':
    main(sys.argv[1:])
