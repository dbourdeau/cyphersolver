"""Credits: who contributed what to each target, read from targets/<folder>/profile.json outcome.credits and the
registry ../contributors.json.  One module for the site build (credit lines, contributors.html, the landing-page
strip), the scoreboard, the profile checker and the paper export.

A credit is {who, role, note?, date?, source?, published?}; 'who' is a contributors.json id.  The project's own work
is not stored as credits: it is outcome.method and outcome.contribution.  outcome.provenance says whose result it
is (project, contributed, mixed; omitted = project).
"""
import json, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
REGISTRY = ROOT / 'contributors.json'
import _methods as M

ROLES = ['solution', 'new cipher', 'new cipher with solution', 'verification', 'key or decipherment used',
         'prior solution', 'key corrected', 'transcription', 'identification', 'pointer']
# Direct contributions to the ledger (George Lasry's four kinds, plus the smaller ones) and the scholarship it builds on.
DIRECT = ['solution', 'new cipher with solution', 'new cipher', 'verification', 'key corrected', 'transcription',
          'identification', 'pointer']
BUILDS_ON = ['key or decipherment used', 'prior solution']
ROLE_LABEL = {
    'solution': 'solution', 'new cipher': 'new cipher', 'new cipher with solution': 'new cipher with solution',
    'verification': 'verification', 'key or decipherment used': 'key or decipherment used',
    'prior solution': 'earlier solution', 'key corrected': 'key corrected', 'transcription': 'transcription',
    'identification': 'identification', 'pointer': 'pointer to a source'}
ROLE_SHORT = {
    'solution': 'solutions', 'new cipher': 'new ciphers', 'new cipher with solution': 'new ciphers solved',
    'verification': 'verifications', 'key or decipherment used': 'keys used', 'prior solution': 'earlier solutions',
    'key corrected': 'key corrections', 'transcription': 'transcriptions', 'identification': 'identifications',
    'pointer': 'pointers'}
PROVENANCE = ('project', 'contributed', 'mixed')
RANKED_KINDS = ('person',)            # who appears in "top contributors"; historical, archive, database are listed apart


def registry():
    d = json.loads(REGISTRY.read_text(encoding='utf-8'))
    return {c['id']: c for c in d['contributors']}


def credits_of(prof):
    out = (prof or {}).get('outcome') or {}
    return [c for c in out.get('credits') or [] if isinstance(c, dict)]


def provenance_of(prof):
    return ((prof or {}).get('outcome') or {}).get('provenance') or 'project'


def check(prof, reg=None):
    """Errors in a profile's credits: unknown ids, roles, provenance without a matching credit."""
    reg = reg or registry()
    errs = []
    out = (prof or {}).get('outcome') or {}
    for i, c in enumerate(credits_of(prof)):
        if c.get('who') not in reg:
            errs.append(f'outcome.credits[{i}].who: {c.get("who")!r} is not in contributors.json (add them there first)')
        if c.get('who') == 'project':
            errs.append(f'outcome.credits[{i}].who: the project is not credited here (outcome.contribution says what it added)')
    prov = out.get('provenance')
    if prov == 'contributed' and not any(c.get('role') in ('solution', 'new cipher', 'new cipher with solution') for c in credits_of(prof)):
        errs.append('outcome.provenance: "contributed" needs a credit with role "solution", "new cipher" or "new cipher with solution" naming the contributor')
    if prov == 'mixed' and not any(reg.get(c.get('who'), {}).get('kind') == 'person' and c.get('role') not in ('pointer', 'prior solution')
                                   for c in credits_of(prof)):
        errs.append('outcome.provenance: "mixed" needs a credit naming the outside contributor whose work the result contains')
    return errs


def load_all():
    """{folder: profile} for every profile outside the famous set."""
    out = {}
    for folder, path in M.profile_paths().items():
        p = M.load(path)
        if p: out[folder] = p
    return out


def tally(profiles, reg=None):
    """{who: {'targets': set(folders), 'roles': Counter(role), 'items': [(folder, credit)]}}"""
    reg = reg or registry()
    t = collections.defaultdict(lambda: {'targets': set(), 'roles': collections.Counter(), 'items': []})
    for folder, prof in profiles.items():
        seen = set()
        for c in credits_of(prof):
            w = c.get('who')
            if w not in reg: continue
            t[w]['targets'].add(folder)
            if (w, c['role']) not in seen: t[w]['roles'][c['role']] += 1
            seen.add((w, c['role']))
            t[w]['items'].append((folder, c))
    return t


def direct_score(entry):
    return sum(n for r, n in entry['roles'].items() if r in DIRECT)


def ranked(t, reg=None, direct_only=False):
    """Contributors of a ranked kind, most targets first (direct contributions break ties)."""
    reg = reg or registry()
    rows = [(w, e) for w, e in t.items() if reg[w]['kind'] in RANKED_KINDS and (direct_score(e) if direct_only else len(e['targets']))]
    return sorted(rows, key=lambda we: (-len(we[1]['targets']), -direct_score(we[1]), reg[we[0]]['name']))
