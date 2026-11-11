"""Which Unsolved Catalogue entries a target folder has taken up, read from the head of targets/<folder>/NOTES.md.

The catalogue's "attempted, open" tag is only set by the /writeup skill when a target closes, so an entry worked on
for days still showed as open (no. 450, duben1764, 27 Oct 2026). The catalogue build and the write-up audit read the
claims here instead.

A folder claims catalogue number N when the first twenty lines of its notes name it in the title line, or at the
start of a line or sentence: "Catalogue 450.", "Catalogue item 213 (class C)", "Unsolved Catalogue no. 450",
"Target: catalogue 217". A number named mid-sentence ("then test Fernando Teles de Faro (catalogue 385) as the
writer", "from `targets/kaa4591/` (catalogue 161)") points at someone else's entry and is not a claim.

The folder's state is its Status line in the first forty lines (CLAUDE.md): 'in progress', 'no write-up', or
'closed' for anything else, including no Status line (a finished target).
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
NUMS = r'(\d{1,4}(?:\s*(?:\+|,|and|&)\s*\d{1,4})*)\b'      # ids passed 999 in Oct 2026
IN_TITLE = re.compile(r'(?i)\b(?:catalogue(?: items?| nos?\.?)?|cat\.) ?' + NUMS)
AT_START = re.compile(r'(?:^[-*>\s]*|[.:;]\**\s+)(?:\**\s*)(?:Unsolved Catalogue|Catalogue|Target: catalogue)'
                      r'(?: items?| nos?\.?)? ?' + NUMS, re.M)
STATUS = re.compile(r'^\**Status(?::\**|\**:)\s*\**\s*(.*)$', re.I | re.M)


def state(head):
    m = STATUS.search(head)
    s = (m.group(1) if m else '').lower()
    return 'in progress' if s.startswith('in progress') else 'no write-up' if s.startswith('no write') else 'closed'


def claims():
    """{catalogue id: [(folder, state, status line)]}, folders in name order."""
    out = {}
    for notes in sorted((ROOT / 'targets').glob('*/NOTES.md')):
        try: lines = notes.read_text(encoding='utf-8').splitlines()
        except (OSError, UnicodeDecodeError): continue
        head = '\n'.join(lines[:40])
        m = STATUS.search(head)
        st, line = state(head), (m.group(1).strip() if m else '')
        found = [x for mm in IN_TITLE.finditer(lines[0] if lines else '') for x in re.findall(r'\d+', mm.group(1))]
        found += [x for mm in AT_START.finditer('\n'.join(lines[1:20])) for x in re.findall(r'\d+', mm.group(1))]
        for n in dict.fromkeys(int(x) for x in found):
            out.setdefault(n, []).append((notes.parent.name, st, line))
    return out


def in_progress(claimants):
    """The claimants still being worked: 'in progress' first, the rule the catalogue tag follows."""
    return [c for c in claimants if c[1] == 'in progress']
