"""Build docs/method.html and docs/method-fr.html: how a reading is made, checked and graded, and by whom.

Every figure on the two pages is counted here from the records when the site is built (review_counts below), never
written by hand. Only the fixed rules are written in the text (the 95% bar, the 5 and 3 standard deviations, 40
symbols, 6 shuffles, the 28 October 2026 vetting date).

The reviewer classes follow the rule of the maintainers' count_reviews.py: one graded entry per outcome.texts[] item
of targets/<folder>/profile.json that carries a reading_review, its `by` string classed by kind_of(). Only
targets/<folder>/profile.json is read, one level below targets/. The "not independent" and "an agent working for the
author" counts are word searches in `by` and `note`, so they are lower bounds.

Called from _build_site.py: build_html(PAGES, PROFILES) before the pages are processed, so both pages get the nav,
footer, contents strip and dateline like any other page. The French page is a translation of this page only.

  python docs/_method_page.py [reviews.json]   print the figures as the build computes them (read-only); the optional
                                               path stands in for research/reading_audit/reviews.json
"""
import collections, html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = 'https://github.com/dbourdeau/cyphersolver'

# --- who signed a reading_review (same rule as count_reviews.py) ------------------------------------------------
MODEL = re.compile(r'claude|anthropic|opus|sonnet|fable|haiku|\bgpt|chatgpt|codex|openai|gemini|'
                   r'\bmodel\b|\bAI\b|agent|session|reading audit|integration (pass|review)', re.I)
# names neither a model nor a person: a pass by the project as a whole ("project (the project's verification pass)")
UNCLEAR = re.compile(r'^\s*(project|integration|the project)\b', re.I)
# a person named first, who says a model assisted: "Brice Dudout (with Claude)", "Andrew Beling, with two ... (Claude)"
PERSON_ASSISTED = re.compile(r"^\s*[A-Z][\w.]*\.?\s+[A-Z][\w-]+(\s*\((with|review assisted|claude|grade confirmed)|,\s*with)",
                             re.I)
# a "person" string that names a published edition or an institution rather than a reviewer
EDITION = re.compile(r'\((?:[^)]*\b(?:university|universit\w*|thesaurus|edition|edited)\b)[^)]*\)', re.I)
# a review whose own record says the reader was not independent of the work
NOT_INDEPENDENT = re.compile(r'not independent|same session', re.I)
# a review signed by an agent working for the author of the reading ("Author's agents (...)", "Claude (for <author>)")
AUTHORS_AGENT = re.compile(r"\bauthor'?s\b", re.I)


def kind_of(by):
    """model | person+model | person | unclear, by count_reviews.py's rule."""
    by = by or ''
    if not MODEL.search(by):
        return 'unclear' if UNCLEAR.search(by) else 'person'
    if PERSON_ASSISTED.search(by):
        return 'person+model'
    return 'model'


def authors_agent(by, authors):
    """True when `by` says the grade came from an agent working for an author of the reading (a lower bound)."""
    by = by or ''
    if AUTHORS_AGENT.search(by):
        return True
    return any(a and re.search(r'\bfor\s+' + re.escape(a.split()[0]) + r'\b', by) for a in authors)


def as_list(x):
    if not x:
        return []
    return x if isinstance(x, list) else [x]


CRYPT = ('key recovered from ciphertext-only', 'key recovered based on plaintext from external sources',
         'key recovered based on adjacent plaintext')
APPLIED = ('read after matching with key from external sources', 'read with known key', 'read from existing decipherment')
EARLIER = ('in archive', 'in print', 'online', 'partial', 'unpublished')
TO_CREDIT = ('in print', 'online', 'partial', 'unpublished')          # the write-up checker asks for a credit on these
SOLVER_ROLES = ('solution', 'new cipher with solution')
GRADED_STATES = ('read', 'read in part')                              # the states the Reading check asks a grade for


def load_audit(path=None):
    """The 22 Oct 2026 reading audit's grades (research/reading_audit/reviews.json), {} when absent."""
    p = pathlib.Path(path) if path else ROOT / 'research' / 'reading_audit' / 'reviews.json'
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def audit_grade(audit, folder, entry):
    """The audit grade that stands in for an entry with no reading_review: the document's own, else the target's
    (the rule of docs/_texts.py audit_review)."""
    rec = audit.get(folder) or {}
    doc = (rec.get('docs') or {}).get('/'.join(map(str, as_list(entry.get('doc')))))
    return (doc or rec).get('grade')


def reading_check_failures(files, audit):
    """(failing, total): reading targets that would fail the Reading check (docs/_texts.py reading_problems, without
    the sentence score) if a pull request touched them. (None, None) when _texts cannot be imported."""
    try:
        if str(HERE) not in sys.path:
            sys.path.insert(0, str(HERE))
        import _texts
    except Exception:
        return None, None
    saved = _texts._AUDIT
    _texts._AUDIT = audit
    total = bad = 0
    try:
        for path in files:
            try:
                prof = json.loads(path.read_text(encoding='utf-8'))
            except (OSError, ValueError):
                continue
            if not _texts.needs_texts(prof):
                continue
            total += 1
            hard, _ = _texts.reading_problems(path.parent, prof, score=False)
            bad += bool(hard)
    finally:
        _texts._AUDIT = saved
    return bad, total


SIGN_MIN_SIGNS, SIGN_MIN_CONTROLS = 8, 2      # the sign-check level's floor (method page, 18 Nov 2026)


def sign_level(s):
    """True when one outcome.sign_check sheet meets the level's floor: at least SIGN_MIN_CONTROLS controls, all
    passed, and at least SIGN_MIN_SIGNS target signs counted. Anything not a number ("unknown") does not meet it, nor
    does a sheet whose record says why it is below the level (below_level: e.g. a rule written after the answers)."""
    num_ = lambda k: s.get(k) if isinstance(s.get(k), int) and not isinstance(s.get(k), bool) else None
    signs, ctl, ok = num_('signs_checked'), num_('controls'), num_('controls_passed')
    return (None not in (signs, ctl, ok) and ctl >= SIGN_MIN_CONTROLS and ok == ctl and signs >= SIGN_MIN_SIGNS
            and isinstance(s.get('checker'), str) and bool(s['checker'].strip())
            and isinstance(s.get('rule'), str) and bool(s['rule'].strip())
            and isinstance(s.get('rule_hash'), str)
            and re.fullmatch(r'[0-9a-fA-F]{64}', s['rule_hash']) is not None
            and not s.get('below_level'))


def review_counts(root=ROOT, audit=None, names=None):
    """All the figures of the page, from root/targets/*/profile.json. Pure: reads files, writes nothing.
    audit: the reading audit's grades (default: root's reviews.json); names: contributor id -> name."""
    root = pathlib.Path(root)
    audit = load_audit(root / 'research' / 'reading_audit' / 'reviews.json') if audit is None else audit
    names = contributor_names(root) if names is None else names
    c = collections.defaultdict(int)
    for k in ('sc_profiles', 'sc', 'sc_level', 'sc_signs', 'sc_external', 'sc_model'):
        c[k] = 0
    kinds, states, verdicts, transcr, prov = (collections.Counter() for _ in range(5))
    exists, found, hc_result, unval_prov, unval_who = (collections.Counter() for _ in range(5))
    ts_prov = collections.Counter()
    files = sorted(root.glob('targets/*/profile.json'))
    for path in files:
        try:
            prof = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            c['unreadable'] += 1
            continue
        c['profiles'] += 1
        o = prof.get('outcome') or {}
        cond = prof.get('conditions') or {}
        provenance = o.get('provenance', 'project')
        prov[provenance] += 1
        method = o.get('method') or ''
        c['m_crypt'] += method in CRYPT
        c['m_applied'] += method in APPLIED
        c['m_notsolved'] += method == 'not solved'
        c['m_na'] += method == 'not applicable'
        verification = as_list(o.get('verification'))
        c['notsolved_control'] += method == 'not solved' and 'matched control' in verification
        c['indep_verif'] += 'independent verification' in verification
        authors = [names.get(x.get('who'), x.get('who')) for x in as_list(o.get('credits'))
                   if isinstance(x, dict) and x.get('role') in SOLVER_ROLES and x.get('who')]
        # documents: who transcribed
        for d in as_list(prof.get('documents')):
            if isinstance(d, dict):
                t = d.get('transcription')
                transcr[(t.get('by') if isinstance(t, dict) else None) or 'not stated'] += 1
        # text entries: state, read_share, reading_review
        graded_here = False
        for t in as_list(o.get('texts')):
            if not isinstance(t, dict):
                continue
            c['texts'] += 1
            state = t.get('state', 'read')
            states[state] += 1
            if state == 'read' and not isinstance(t.get('read_share'), (int, float)):
                c['read_no_share'] += 1
            r = t.get('reading_review')
            if not r:
                c['read_no_rr'] += state == 'read'
                if state in GRADED_STATES:
                    c['graded_no_rr'] += 1
                    g = audit_grade(audit, path.parent.name, t)
                    c['no_rr_audit_ab' if g in ('A', 'B') else 'no_rr_audit_other' if g else 'no_rr_none'] += 1
                continue
            graded_here = True
            c['rr'] += 1
            k = kind_of(r.get('by'))
            kinds[k] += 1
            if k == 'person' and EDITION.search(r.get('by') or ''):
                c['rr_edition'] += 1
            if NOT_INDEPENDENT.search(f"{r.get('by') or ''} {r.get('note') or ''}"):
                c['rr_not_independent'] += 1
            elif authors_agent(r.get('by'), authors):
                c['rr_authors_agent'] += 1
            c['rr_A'] += r.get('grade') == 'A'
            c['rr_B'] += r.get('grade') == 'B'
        c['rr_profiles'] += graded_here
        # human_check
        hcs = [h for h in as_list(o.get('human_check')) if isinstance(h, dict)]
        if hcs:
            c['hc_profiles'] += 1
            c['hc'] += len(hcs)
            hc_result.update(h.get('result') for h in hcs)
        # sign checks (the level "AI decipherment, human-checked on a sample of signs")
        scs = [x for x in as_list(o.get('sign_check')) if isinstance(x, dict)]
        if scs:
            c['sc_profiles'] += 1
            c['sc'] += len(scs)
            c['sc_level'] += sum(bool(sign_level(x)) for x in scs)
            c['sc_signs'] += sum(x['signs_checked'] for x in scs if isinstance(x.get('signs_checked'), int))
            c['sc_external'] += sum(x.get('checker_kind') == 'external' for x in scs)
            c['sc_model'] += sum(bool(as_list(x.get('model_roles'))) for x in scs)
        # statistical validation
        v = o.get('validation')
        if isinstance(v, dict):
            verdicts[v.get('verdict')] += 1
        if method.startswith('key recovered') and o.get('class') in ('read', 'read in part'):
            c['crypt_read'] += 1
            if 'validation' in o:
                c['crypt_val'] += 1
            else:
                c['crypt_unval'] += 1
                unval_prov[provenance] += 1
                if provenance == 'contributed':
                    for w in sorted({x.get('who') for x in as_list(o.get('credits')) if isinstance(x, dict)
                                     and x.get('role') in SOLVER_ROLES and x.get('who')}):
                        unval_who[w] += 1
        # earlier readings
        ps = cond.get('prior_solution')
        if isinstance(ps, dict):
            exists[ps.get('exists')] += 1
            if ps.get('exists') in EARLIER:
                found[ps.get('found')] += 1
            if ps.get('exists') in TO_CREDIT:
                c['to_credit'] += 1
                roles = {x.get('role') for x in as_list(o.get('credits')) if isinstance(x, dict)}
                c['credited'] += bool(roles & {'prior solution', 'key or decipherment used'})
        if (root / 'targets' / path.parent.name / 'timestamps').is_dir():
            c['timestamped'] += 1
            ts_prov[provenance] += 1
    c.update(dict(kinds=kinds, states=states, verdicts=verdicts, transcr=transcr, prov=prov, exists=exists, found=found,
                  hc_result=hc_result, unval_prov=unval_prov, unval_who=unval_who, ts_prov=ts_prov))
    c['verdicts_total'] = sum(verdicts.values())
    c['exists_answered'] = sum(n for k, n in exists.items() if k not in (None, 'unknown'))
    c['exists_earlier'] = sum(exists[k] for k in EARLIER)
    c['rc_fail'], c['rc_total'] = reading_check_failures(files, audit)
    # a count no target reached (a reduced tree: no timestamps/, no human_check ...) reads as 0, not a KeyError
    return collections.defaultdict(int, c)


def contributor_names(root=ROOT):
    try:
        reg = json.loads((pathlib.Path(root) / 'contributors.json').read_text(encoding='utf-8'))['contributors']
    except (OSError, ValueError, KeyError):
        return {}
    return {x['id']: x.get('name', x['id']) for x in reg if isinstance(x, dict) and x.get('id')}


# --- formatting -----------------------------------------------------------------------------------------------
def num(n, lang):
    s = f'{int(n or 0):,}'
    return s.replace(',', '&#8239;') if lang == 'fr' else s


def pct(a, b, lang):
    if not b:
        return '0'
    p = round(100 * a / b)
    return f'{p}&nbsp;%' if lang == 'fr' else f'{p}%'


def esc(s):
    return html.escape(str(s), quote=False)


def gh(path, label=None):
    """A link to a file of the repository."""
    return f'<a href="{REPO}/blob/main/{path}" rel="noopener"><code>{esc(label or path)}</code></a>'


def join(items, lang):
    items = [i for i in items if i]
    if len(items) < 2:
        return ''.join(items)
    last = ' et ' if lang == 'fr' else ' and '
    return ', '.join(items[:-1]) + last + items[-1]


def table(head, rows, total=None):
    """A plain table: head and rows are lists of cells (HTML), total an optional last row in bold."""
    out = ['<table>', '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead>', '<tbody>']
    out += ['<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows]
    if total:
        out.append('<tr>' + ''.join(f'<td><b>{x}</b></td>' if x else '<td></td>' for x in total) + '</tr>')
    return '\n'.join(out + ['</tbody>', '</table>'])


def fr_typo(s):
    """French spacing: a no-break space before ; : ? ! and inside « »."""
    s = re.sub(r' ([;:?!])', r'&nbsp;\1', s)
    return s.replace('« ', '«&nbsp;').replace(' »', '&nbsp;»')


def solver_list(c, lang, names):
    who = c['unval_who'].most_common()
    return join([f'{num(n, lang)} {esc(names.get(w, w))}' for w, n in who], lang)


def unval_text(c, lang, names):
    """Who produced the cryptanalytic results that carry no statistical verdict, zero parts left out."""
    up = c['unval_prov']
    one = lambda x: x in ('0', '1')
    if lang == 'fr':
        parts = [(up.get('contributed', 0), lambda x: f"{x} {'est un résultat' if one(x) else 'sont des résultats'} de contributeurs extérieurs ({solver_list(c, lang, names)})"),
                 (up.get('mixed', 0), lambda x: f"{x} {'est mixte' if one(x) else 'sont mixtes'}"),
                 (up.get('project', 0), lambda x: f"{x} {'relève' if one(x) else 'relèvent'} du projet")]
    else:
        parts = [(up.get('contributed', 0), lambda x: f"{x} {'is a result' if one(x) else 'are results'} contributed from outside ({solver_list(c, lang, names)})"),
                 (up.get('mixed', 0), lambda x: f"{x} {'is' if one(x) else 'are'} mixed"),
                 (up.get('project', 0), lambda x: f"{x} {'is' if one(x) else 'are'} the project&rsquo;s own")]
    return join([f(num(v, lang)) for v, f in parts if v], lang)


def head(lang, title, desc):
    return ('<!DOCTYPE html>\n'
            f'<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n<meta name="description" content="{desc}">\n'
            '<link rel="alternate" hreflang="en" href="https://cyphersolver.com/method.html">\n'
            '<link rel="alternate" hreflang="fr" href="https://cyphersolver.com/method-fr.html">\n'
            '<link rel="stylesheet" href="style.css">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n')


TAIL = '\n</main>\n<!-- site:footer -->\n</body>\n</html>\n'
VERDICTS = ('pass', 'weak', 'underdetermined', 'too short', 'fail', 'not applicable')
TR_KEYS = ('llm from images', 'mixed', 'DECODE', 'published', 'human (project)')


def c_sum(counter, exclude):
    return sum(v for k, v in counter.items() if k not in exclude)


def figures(c, lang):
    """The values both pages share, formatted for lang."""
    n = lambda x: num(x, lang)
    k = c['kinds']
    return dict(n=n, k=k, st=c['states'], v=c['verdicts'], tr=c['transcr'], pv=c['prov'], hr=c['hc_result'],
                model_pct=pct(k['model'], c['rr'], lang),
                tr_other=c_sum(c['transcr'], TR_KEYS), tr_total=sum(c['transcr'].values()),
                ts_all_contrib=bool(c.get('timestamped', 0)) and c['ts_prov'].get('contributed', 0) == c.get('timestamped', 0))


# --- English ---------------------------------------------------------------------------------------------------
def page_en(c, queue, names):
    L = 'en'
    F = figures(c, L)
    n, k, st, v, tr, pv, hr = (F[x] for x in ('n', 'k', 'st', 'v', 'tr', 'pv', 'hr'))
    hc_txt = join([f'{n(hr[x])} {x}' for x in ('confirmed', 'corrected', 'disagreed') if hr.get(x)], L)
    ts_txt = (f"<p>In {n(c.get('timestamped', 0))} targets{', all contributed from outside,' if F['ts_all_contrib'] else ''} the "
              'work files were time-stamped: an RFC 3161 token and an OpenTimestamps proof over the SHA-256 of a list of files. '
              'This can prove that the listed files existed at that date.</p>') if c.get('timestamped', 0) else ''
    rc = ('' if c.get('rc_fail') is None else
          f"<p>Today {n(c['rc_fail'])} of the {n(c['rc_total'])} targets that present a reading would not pass the "
          'Reading check if a pull request changed them.</p>\n')
    steps = table(['Step', 'Usually done by', 'What is checked'], [
        ['1. Find the document and any earlier reading', 'an AI agent, run by a person', 'since 28 October 2026, a vetting list for the catalogue (&sect;&nbsp;03)'],
        ['2. Transcribe the cipher', 'an AI model, from the images', 'no systematic double transcription (&sect;&nbsp;04)'],
        ['3. Obtain the key', 'an AI model, or a key that already existed', 'the statistical test, where it applies (&sect;&nbsp;07)'],
        ['4. Build the text and translate it', 'an AI model (the method is in CONTRIBUTING)', 'the share of words read, <code>read_share</code> (&sect;&nbsp;06)'],
        ['5. Grade the reading A or B', f"an AI model, in {F['model_pct']} of entries", 'that a grade is there (&sect;&nbsp;08)'],
        ['6. Check a passage on the image without AI', f"a person, in {n(c['hc_profiles'])} records", 'nothing automatic (&sect;&nbsp;08)'],
        ['7. Merge into the repository', 'a maintainer; for a pull request, one who is not its author', 'the approval, for pull requests (&sect;&nbsp;09)']])
    methods = table(['How the key was obtained', 'Records'], [
        ['key recovered here by cryptanalysis: from the ciphertext alone, from a plaintext found elsewhere, or from a plaintext next to the cipher', n(c['m_crypt'])],
        ['a key or decipherment that already existed, applied here', n(c['m_applied'])],
        ['neither key nor text obtained (<code>not solved</code>)', n(c['m_notsolved'])],
        ['not a cipher, or the document could not be reached', n(c['m_na'])]], total=['All records', n(c['profiles'])])
    trans = table(['Transcribed by', 'Documents'], [
        ['an AI model, from the images', n(tr['llm from images'])], ['several sources combined', n(tr['mixed'])],
        ['DECODE', n(tr['DECODE'])], ['a printed edition', n(tr['published'])],
        ['a person working for the project', n(tr['human (project)'])], ['other, or not stated', n(F['tr_other'])]],
        total=['All documents', n(F['tr_total'])])
    state_t = table(['State', 'What it means', 'Documents'], [
        ['<code>read</code>', 'coherent sentences, an English translation, and at least 95% of words read', n(st['read'])],
        ['<code>read in part</code>', 'coherent sentences and a translation, but under 95% of words read', n(st['read in part'])],
        ['<code>decoded, not read</code>', 'a decode that does not build sentences: shown, but not counted as a reading', n(st['decoded, not read'])],
        ['<code>not prose</code>', 'a key sheet, a code list, figures or names', n(st['not prose'])]],
        total=['All entries', '', n(c['texts'])])
    vmean = {'pass': 'the three conditions above', 'weak': 'at least 1 standard deviation above the shuffled fits, short of a pass',
             'underdetermined': 'the search does better than the reading on the real ciphertext: the test cannot decide',
             'too short': 'under 40 symbols read, or under 80 letters', 'fail': 'a key fitted to the shuffled text does as well',
             'not applicable': 'a transposition, a non-alphabetic plaintext, or symbols with several values (over 10%)'}
    verd = table(['Verdict', 'Meaning', 'Records'], [[f'<code>{x}</code>', vmean[x], n(v.get(x, 0))] for x in VERDICTS],
                 total=['All verdicts', '', n(c['verdicts_total'])])
    signers = table(['Who signed the grade', 'Entries'], [
        ['an AI model', f"{n(k['model'])} ({F['model_pct']})"], ['a person assisted by an AI model', n(k['person+model'])],
        ['a person, no AI model named', f"{n(k['person'])} ({n(c.get('rr_edition', 0))} of them name a published edition, not a reviewer)"],
        ['cannot tell', n(k['unclear'])]], total=['All graded entries', f"{n(c['rr'])}, in {n(c['rr_profiles'])} records"])
    checks = table(['Check', 'When it runs', 'What it checks', 'What it does not check'], [
        ['Check write-ups', 'every push to <code>main</code> and every pull request',
         'page heads, dead links and HTML markup; the unit tests of the scripts', 'nothing about the readings themselves'],
        ['Reading check', 'every pull request, on the targets it changes only',
         'for each <code>read</code> or <code>read in part</code> document: a grade A or B (its own, or the audit&rsquo;s) and an English translation; <code>read_share</code> at 0.95 or more for a <code>read</code> document, when it is recorded; that the target&rsquo;s class matches its documents',
         'who gave the grade; the statistical test; the matched control; any comparison with the images; the targets the pull request does not touch']])
    return head(L, 'Method and review &mdash; how a reading is made, checked and graded',
                'How each reading on Cyphersolver is transcribed, deciphered, tested and graded, who does each step, '
                'and what the checks do not cover. The figures are counted from the records at each build.') + f'''<section class="hero">
  <p class="kicker">Reference &middot; method &middot; review</p>
  <h1>Method and review</h1>
  <p class="sub">How a reading on this site is made, checked and graded. Who does each step. What the checks do not cover. Every count on this page is made again from the repository each time the site is built.</p>
  <p class="meta">Daniel Bourdeau</p>
  <p class="langswitch"><a href="method-fr.html" hreflang="fr" lang="fr">Version fran&ccedil;aise</a></p>
</section>

<main>

<div class="callout glance"><p><b>At a glance</b></p>
<ul>
<li>The work is done mostly by AI models, run by people.</li>
<li>The reading grade (A or B) is given by an AI model in {F['model_pct']} of entries. It is not a human review.</li>
<li>A check of a passage against the image by a person, without AI, is declared in {n(c['hc_profiles'])} records.</li>
<li>The automated checks test the form of a reading. They do not test that it is right.</li>
<li>Any reading can be challenged. Corrections stay in the repository&rsquo;s history.</li>
</ul></div>

<h2 id="what-it-is"><span class="num">01</span> What this project is</h2>
<p>Cyphersolver is an open ledger of historical ciphers. The ciphers are worked on with AI models. The ledger is also an informal benchmark of what those models can do with them.</p>
<p>People run the AI models: the project&rsquo;s maintainers and outside contributors.</p>
<p>The ledger holds {n(c['profiles'])} target records. {n(pv['project'])} are the project&rsquo;s own work, {n(pv['contributed'])} were contributed from outside, and {n(pv['mixed'])} are mixed.</p>
<p>The ledger is not a critical edition. Its results have not been peer-reviewed in the academic sense.</p>
<p>Words used on this page:</p>
<ul>
<li>A <b>target</b> is a folder of the repository: one cipher document or a group of them.</li>
<li>Its <b>record</b> is the file <code>profile.json</code>, with fixed fields. The working notes are in <code>NOTES.md</code>.</li>
<li>A <b>write-up</b> is the site&rsquo;s page on the target.</li>
</ul>
<p>The full rules are in the {gh('README.md', 'README')} (Conventions), {gh('CONTRIBUTING.md')} and {gh('profile.schema.json')}.</p>

<h2 id="steps"><span class="num">02</span> The steps of a reading</h2>
{steps}

<h2 id="sources"><span class="num">03</span> Sources and earlier work</h2>
<p>Every image on the site is to be credited to its source: holder, shelfmark, folio, and the route to it (Gallica, DECODE, an archive&rsquo;s viewer, IIIF, an edition). That is the README&rsquo;s rule. It is not checked page by page.</p>
<p>Images remain under their holders&rsquo; terms. Text is under CC BY 4.0, code under MIT.</p>
<p>Since 28 October 2026, a document enters the <a href="catalogue.html">catalogue</a> only when its record shows two things. The ciphertext was seen on an image. The usual places for an earlier decipherment were searched: DECODE, Satoshi Tomokiyo&rsquo;s lists, the printed calendar or edition, and the literature. Older entries did not go through this list.</p>
<p>A record can say whether a reading existed before the project&rsquo;s. {n(c['exists_answered'])} of {n(c['profiles'])} records answer. {n(c['exists_earlier'])} record an earlier reading, complete or partial. In {n(c['found'].get('after reading', 0))} of these it came to light only after the project&rsquo;s reading.</p>
<p>The write-up checker asks that an earlier reading in print, online, unpublished or partial be credited in the record. {n(c.get('credited', 0))} of the {n(c.get('to_credit', 0))} records concerned do so. An earlier solution that was never published is shown in full only with its author&rsquo;s agreement.</p>

<h2 id="transcription"><span class="num">04</span> Transcription</h2>
<p>Copying the cipher from the manuscript is a source of error in itself. The records say who transcribed each document.</p>
{trans}
<p>There is no systematic double blind transcription. The notes of some targets compare two transcriptions; the project publishes no overall rate of agreement.</p>
<p>A transcription is sometimes corrected after the key is found. The reading can then depend on the key it is meant to test. The write-ups do not flag this in a uniform way.</p>
{ts_txt}

<h2 id="key"><span class="num">05</span> How the key is obtained</h2>
<p>Each record puts its method in one of the categories of the <a href="glossary.html">glossary</a>.</p>
{methods}
<p>A negative result is to come with a <b>matched control</b>: a synthetic text of the same length, alphabet and cipher design that the same solver does recover. That is the README&rsquo;s rule. It is not checked: {n(c.get('notsolved_control', 0))} of the {n(c['m_notsolved'])} <code>not solved</code> records list a matched control.</p>
<p>A <b>held-out test</b> means finding the key without looking at part of the text, then trying the key on that part. No rule of the project requires it. Some contributors do it and describe it in the target&rsquo;s notes.</p>
<p>In the protocol some contributors follow, a key found by cryptanalysis is found <b>on part of the text only</b>. The rest is not analysed and serves as validation. The steps are: choose the held-out portion before any work on it; freeze the key with a SHA-256 hash; then decrypt the held-out portion once, with no change to the key. The test passes when the share of letters that make sense reaches 0.85 and beats the best of 200 shuffled keys by at least 0.30. The notes of these targets give the hash, the portion and the score, including when the test fails.</p>

<h2 id="decoded-is-not-read"><span class="num">06</span> A decryption is not yet a reading</h2>
<p>A key that turns the cipher into words does not yet give a text. Each document in a record carries one of four states.</p>
{state_t}
<p><b>The share of words read</b> (<code>read_share</code>) counts cipher words only. In a letter that mixes clear text and cipher, it is measured over the words written in cipher; the clear words around them are neither read nor unread and stay out of both numerator and denominator.</p>
<p>Only sure words count as read: a word counts as read when the key gives it, or the plain text beside it does, with nothing supplied. A probable word (<code>&#123;x&#125;</code>), an inferred or supplied word, a grade-M word and an unvalued code are holes, and so is a letter supplied inside a word. <code>read_share</code> is 1 minus the share of holes among the cipher words. It is counted by a script where the reading declares its markup.</p>
<p>The 95% bar applies to the cipher words of each document. <b>Floor for short texts:</b> a document of fewer than 40 cipher words is <code>read</code> when its holes are at most 5% of its cipher words or at most 2 words, whichever allows more. The floor never applies to a text of 40 words or more, and the page and the record state the number of holes and that the floor was used.</p>
<p>This number counts the holes the reader marked. It does not say whether the words read are right.</p>
<p><b>The decryption and the reading are two files.</b> The decryption is the key applied to the transcription, sign by sign, with nothing edited: a word the key gets wrong stays wrong in it. The reading is that text made into sentences, and every letter or word in it that the key does not give for the signs as transcribed is marked; marked letters are holes. A text that is a decipherment of the time, a clear copy or an edition is labelled as such. This rule dates from 16 November 2026 (README, Conventions). An audit of the 54 targets its script flagged found words departing from the key, without a mark, in 35 of them; marks were added in 31 targets (858 places). The script could not compare 757 of 938 texts with their keys, so readings made before that date may still carry unmarked changes. The audit is in <a href="{REPO}/tree/main/research/decrypt_audit" rel="noopener"><code>research/decrypt_audit</code></a>.</p>
<p>{n(c.get('read_no_share', 0))} documents in state <code>read</code> have no <code>read_share</code> recorded. For them, the 95% is not measured document by document.</p>
<p>The 95% bar is the project&rsquo;s own. No standard of the field sets one.</p>
<p>One special case. In a code read with its surviving period key, a group one digit away from the value the sense needs counts as read, on three conditions. The slip can be seen on the image. The other groups of the word come from the key. The corrected groups spell the whole word. The group is marked <code>{{+...}}</code> in the text.</p>

<h2 id="statistical-checks"><span class="num">07</span> The statistical test against false positives</h2>
<p>The risk: a key with enough free values can produce words even when it is wrong.</p>
<p>The test is {gh('docs/_validate.py')}. It scores the reading with a letter model of the period (sequences of 4 letters). It then compares that score with two baselines:</p>
<ul>
<li>random keys of the same structure;</li>
<li>keys fitted by the same search to the ciphertext once shuffled (6 shuffles).</li>
</ul>
<p>A reading <b>passes</b> when its score is at least 5 standard deviations above the random keys, above every key fitted to shuffled text, and at least 3 standard deviations above their mean.</p>
{verd}
<p>The automated checks do not require the test. Of the {n(c['crypt_read'])} records whose key was recovered here and whose text was obtained in full or in part, {n(c['crypt_unval'])} carry no verdict: {unval_text(c, L, names)}.</p>
<p>What the test does not show:</p>
<ul>
<li>it scores letters, so it checks neither the sense nor a code value proposed from context;</li>
<li>it makes no correction for the number of readings tested;</li>
<li>on short texts and homophonic ciphers it often cannot decide;</li>
<li>as far as we know, no outside statistician has reviewed it.</li>
</ul>

<h2 id="review"><span class="num">08</span> The reading grade and the human check</h2>
<p>A <b>reading grade</b> (<code>reading_review</code>) is recorded in the record, document by document. A reader has read the decryption as sentences and gives it A or B:</p>
<ul>
<li>A: coherent sentences, with scattered holes;</li>
<li>B: coherent but raw (unspaced, in capitals, in decoder lines), and put into normal form in the reading or the translation.</li>
</ul>
<p>A and B are not grades of accuracy. They say the text builds sentences. They do not say it was compared with the images.</p>
<p>A grade is needed for <code>read</code> and <code>read in part</code> documents. The schema allows a person or an AI model named as such. CONTRIBUTING wants the grade recorded by the reviewer, not by the author. No automated check looks at who gave it.</p>
<p><b>Most A and B grades are given by an AI model.</b></p>
{signers}
<p>In at least {n(c.get('rr_not_independent', 0))} entries the record itself says the reader was not independent of the work (for example, the same session). At least {n(c.get('rr_authors_agent', 0))} more are signed by an agent working for the author of the reading. These entries do not meet, or do not clearly meet, the rule of CONTRIBUTING.</p>
<p>{n(c.get('graded_no_rr', 0))} <code>read</code> or <code>read in part</code> documents have no grade of their own. For {n(c.get('no_rr_audit_ab', 0))} of them, the check uses the grade of the reading audit of 22 October 2026, which an AI model gave. {n(c.get('no_rr_audit_other', 0))} have an audit grade that is neither A nor B, and {n(c.get('no_rr_none', 0))} have no grade at all. They are not counted in the table.</p>
<p><b>The second review of a reading is therefore an AI model reader together with the automated checks. It is not a human review.</b></p>
<p>The <b>human check</b> (<code>human_check</code>) is something else. A person compares a passage with the image, without AI help, and records the result: confirmed, corrected or disagreed. It is declared in the record. It covers {n(c['hc_profiles'])} records ({hc_txt}).</p>
<p>When a character or an alphabet is doubtful, a contributor can make <b>targeted blind re-readings</b>. A person sees only the doubtful sign, cut out of the image, next to two or three candidate shapes. They do not see the expected reading, the gloss or the context. They choose the shape they see. This confirms or refutes one value, one reading or a whole alphabet without the bias of knowing the answer. It is a check of sign shapes, not a re-reading of the text, and it is recorded as such.</p>
<p>{n(c.get('indep_verif', 0))} records also declare an &ldquo;independent verification&rdquo;: someone outside the project checked the reading against the images or with their own key. The field does not say whether that person used an AI model.</p>
<p>{n(queue)} readings whose key was recovered or matched here are <a href="contributors.html#verify">waiting for an independent check</a>.</p>
<p class="cmuted"><b>How these figures are counted.</b> One graded entry is one item of <code>outcome.texts</code> in a target&rsquo;s <code>profile.json</code> that carries a <code>reading_review</code>, whatever its state. Only the <code>targets/&lt;folder&gt;/profile.json</code> files are counted. The signer is classed from the <code>by</code> field: <i>model</i> when it names an AI model, an agent or an AI session and no person comes first; <i>person assisted by an AI model</i> when a person comes first and says an AI model assisted; <i>person</i> when no model is named; <i>cannot tell</i> when it names neither (&ldquo;project verification pass&rdquo;). &ldquo;Not independent&rdquo; and &ldquo;an agent working for the author&rdquo; are found by a word search in <code>by</code> and <code>note</code>, so they are lower bounds. Counting per document or per target gives other totals. The rule is in {gh('docs/_method_page.py')}.</p>

<h3 id="sign-check">A verification level: AI decipherment, human-checked on a sample of signs</h3>
<p>Between no check and a full proofreading against the images, a reading can carry the level <b>AI decipherment, human-checked on a sample of signs</b>. An AI model transcribed and deciphered the text. A person then picked, blind, the shape they see for a set of signs on a review sheet:</p>
<ul>
<li>a rule written before the sheet is built, and dated before any answer, picks the signs: doubtful shapes, signs that several words depend on, code groups;</li>
<li>each question boxes one sign on its line. The options are shapes cut from the same document, plus &ldquo;none / other shape&rdquo;, &ldquo;illegible&rdquo; and &ldquo;not a sign&rdquo;, which leave the word marked. No gloss, reading, value or place is shown;</li>
<li>at least two controls with a known answer are mixed in, taken from places as hard as the targets. The answer key stays private until the answers are exported.</li>
</ul>
<p>The record (<code>sign_check</code> in <code>profile.json</code>) gives the date; who answered, and whether that person is inside or outside the project; what an AI model did (wrote the rule, cut the thumbnails, built the sheet, scored the answers, interpreted free-text remarks); how many signs were checked and how they were chosen (a section of the target&rsquo;s NOTES); how many controls passed; and the results: as transcribed, corrected, unresolved, not counted. A write-up shows it as one sentence, for example: &ldquo;9 doubtful signs checked blind by a project member, on a sheet an AI model built and scored; rule in NOTES; controls 2 of 2; 2 as transcribed, 7 corrected, 1 not counted (faulty thumbnail)&rdquo;.</p>
<p>A sheet meets the level only with at least {SIGN_MIN_CONTROLS} controls, all passed, and at least {SIGN_MIN_SIGNS} target signs once the answers touched by a faulty thumbnail are removed. An answer &ldquo;none / other&rdquo; on a control counts as a failure. Whatever an answer contradicts is recoded or marked in the reading first. These are the project&rsquo;s rules (README, Conventions; the owner&rsquo;s decision of 19 November 2026): the checker is named, and the label says nothing about the key. The dated rule and its SHA-256 identify the criteria recorded before the answers. On shared sheets, count the signs for each target separately.</p>
<p><b>The level says how a reading was checked, not how much of the text counts as read.</b> It never changes the class, the state or the read share: a reading can carry it and keep the state <code>read in part</code>. It checks the shapes of signs, not the key, the value of a code or the reading as a whole. The signs are chosen because they are doubtful, so the check is a diagnostic, not a random sample, and it says nothing about the signs that were not shown. Two passed controls show little on their own: a checker who is right one time in two passes both one time in four. It is not a <code>human_check</code>, which the schema defines as a check without AI help.</p>
<p>The first readings to carry it are those whose key was built on part of the material (the document or sister letters in the same cipher) and passed a test on a passage not used to build it, against a threshold written first; the write-up gives the history of attempts. On these first readings <b>the checker is the contributor</b> of the reading, a project member who answered the sheets of his own readings: the check is not independent, and the record and the write-up say so. {n(c['sc_profiles'])} records carry a <code>sign_check</code> ({n(c['sc'])} sheets, {n(c['sc_level'])} meeting the level, {n(c['sc_external'])} answered by someone outside the project).</p>

<h2 id="checks"><span class="num">09</span> What the automated checks require</h2>
<p>Two checks run on GitHub by themselves (continuous integration, CI).</p>
{checks}
<p>The other rules (the statistical test, the credit for earlier readings, the human check, the catalogue vetting list) are checked by scripts run by hand. They do not block a merge.</p>
{rc}<p><b>Merging.</b> A change to a result enters the repository through a pull request approved by a maintainer who is not its author (CONTRIBUTING, &ldquo;Review and merging&rdquo;). A ruleset on <code>main</code> enforces part of this: it requires a pull request and a code owner&rsquo;s review ({gh('.github/CODEOWNERS', 'CODEOWNERS')}), but not that the two checks pass, which CONTRIBUTING also asks. The repository&rsquo;s administrator and the site&rsquo;s rebuild job (through a deploy key) can push to <code>main</code> without a pull request, and the owner has pushed directly, so the rule does not bind every change.</p>

<h2 id="ai"><span class="num">10</span> The part played by AI</h2>
<p>The records name the AI models that did the work (<code>conditions.models</code>). They say what the person did (<code>conditions.human_role</code>): supply images or logins, point to a source, correct a reading.</p>
<p>Scripts, keys and transcriptions are kept under version control. The README gives the commands that reproduce two results.</p>
<p>A step done by an AI model cannot be replayed exactly: transcribing an image, proposing a code value from context. The models are proprietary.</p>
<p>The cost of each result (model use, money, human time) is not published.</p>

<h2 id="corrections"><span class="num">11</span> Corrections and challenges</h2>
<p>Any reading can be challenged or checked.</p>
<p>On GitHub, the <a href="{REPO}/issues/new?template=verification.yml" rel="noopener">Verification form</a> asks for the passage and the images used, every place where your reading agrees with the page or differs from it, and the key values you would change.</p>
<p>Without a GitHub account, write by <a href="contribute.html#email">email</a>.</p>
<p>Every write-up has a &ldquo;Contest or verify this reading&rdquo; link at its foot. Say which passage and which images, and where your reading differs. No response time is promised.</p>
<p>A correction is made on the page with its date, stays in the repository&rsquo;s history, and is entered in the <a href="corrections.html">corrections log</a>: the date, the pages, what changed, who reported it and why it was wrong. The log starts on 16 November 2026.</p>

<h2 id="researchers"><span class="num">12</span> For researchers, and how to cite</h2>
<p>Cryptologists, palaeographers, archivists and historians can:</p>
<ul>
<li>check a reading from the images (<a href="contributors.html#verify">the list waiting for a check</a>);</li>
<li>take a partial reading further (<a href="further.html">Read further</a>);</li>
<li>look at a document in its archive (<a href="archives.html">To the archive</a>).</li>
</ul>
<p>Contributions are credited in the record (<code>outcome.credits</code>) and on <a href="contributors.html">Contributors</a>.</p>
<p>Each write-up has a &ldquo;Cite this page&rdquo; block with a BibTeX entry: the date the page was posted and last changed, and the repository commit the site was built from. A page can change at the same address, so cite the commit and the date you consulted it. There is no DOI.</p>
''' + TAIL


# --- French ----------------------------------------------------------------------------------------------------
FR_HC = {'confirmed': 'confirmés', 'corrected': 'corrigés', 'disagreed': 'en désaccord'}
FR_VERDICT = {'pass': 'réussi', 'weak': 'faible', 'underdetermined': 'indécidable', 'too short': 'trop court',
              'fail': 'échec', 'not applicable': 'non applicable'}


def page_fr(c, queue, names):
    L = 'fr'
    F = figures(c, L)
    n, k, st, v, tr, pv, hr = (F[x] for x in ('n', 'k', 'st', 'v', 'tr', 'pv', 'hr'))
    hc_txt = join([f'{n(hr[x])} {FR_HC[x]}' for x in ('confirmed', 'corrected', 'disagreed') if hr.get(x)], L)
    ts_txt = (f"<p>Pour {n(c.get('timestamped', 0))} cibles{', toutes des contributions extérieures,' if F['ts_all_contrib'] else ''} les "
              'fichiers de travail ont été horodatés : un jeton RFC 3161 et une preuve OpenTimestamps sur l’empreinte '
              'SHA-256 d’une liste de fichiers. Cela permet de prouver que les fichiers listés existaient à cette date.</p>') if c.get('timestamped', 0) else ''
    rc = ('' if c.get('rc_fail') is None else
          f"<p>Aujourd’hui, {n(c['rc_fail'])} des {n(c['rc_total'])} cibles qui présentent une lecture ne passeraient pas le "
          'Reading check si une demande de fusion les modifiait.</p>\n')
    steps = table(['Étape', 'Faite le plus souvent par', 'Ce qui est contrôlé'], [
        ['1. Trouver le document et ses lectures antérieures', 'un agent d’IA, piloté par une personne', 'depuis le 28 octobre 2026, une grille pour le catalogue (§&nbsp;03)'],
        ['2. Transcrire le chiffré', 'un modèle d’IA, à partir des images', 'pas de double transcription systématique (§&nbsp;04)'],
        ['3. Obtenir la clé', 'un modèle d’IA, ou une clé qui existait déjà', 'le test statistique, quand il s’applique (§&nbsp;07)'],
        ['4. Établir le texte et le traduire', 'un modèle d’IA (la méthode est dans CONTRIBUTING)', 'la part de mots lus, <code>read_share</code> (§&nbsp;06)'],
        ['5. Noter la lecture A ou B', f"un modèle d’IA, pour {F['model_pct']} des entrées", 'la présence de la note (§&nbsp;08)'],
        ['6. Vérifier un passage sur l’image, sans IA', f"une personne, dans {n(c['hc_profiles'])} fiches", 'rien d’automatique (§&nbsp;08)'],
        ['7. Intégrer au dépôt', 'un mainteneur ; pour une demande de fusion, celui qui n’en est pas l’auteur', 'l’approbation, pour les demandes de fusion (§&nbsp;09)']])
    methods = table(['Comment la clé a été obtenue', 'Fiches'], [
        ['clé reconstituée ici par cryptanalyse : à partir du seul chiffré, d’un texte clair trouvé ailleurs, ou d’un texte clair voisin du chiffré', n(c['m_crypt'])],
        ['clé ou déchiffrement qui existait déjà, appliqué ici', n(c['m_applied'])],
        ['ni clé ni texte obtenus (<code>not solved</code>)', n(c['m_notsolved'])],
        ['pas un chiffre, ou document inaccessible', n(c['m_na'])]], total=['Toutes les fiches', n(c['profiles'])])
    trans = table(['Transcrit par', 'Documents'], [
        ['un modèle d’IA, à partir des images', n(tr['llm from images'])], ['plusieurs sources combinées', n(tr['mixed'])],
        ['DECODE', n(tr['DECODE'])], ['une édition imprimée', n(tr['published'])],
        ['une personne travaillant pour le projet', n(tr['human (project)'])], ['autre, ou non indiqué', n(F['tr_other'])]],
        total=['Tous les documents', n(F['tr_total'])])
    state_t = table(['État', 'Ce que cela veut dire', 'Documents'], [
        ['<code>read</code> (lu)', 'des phrases cohérentes, une traduction anglaise, et au moins 95&nbsp;% de mots lus', n(st['read'])],
        ['<code>read in part</code> (lu en partie)', 'des phrases cohérentes et une traduction, mais moins de 95&nbsp;% de mots lus', n(st['read in part'])],
        ['<code>decoded, not read</code> (décodé, non lu)', 'un décodage qui ne forme pas de phrases : montré, mais pas compté comme lecture', n(st['decoded, not read'])],
        ['<code>not prose</code> (pas de la prose)', 'une table de chiffre, une liste de codes, des nombres ou des noms', n(st['not prose'])]],
        total=['Toutes les entrées', '', n(c['texts'])])
    vmean = {'pass': 'les trois conditions ci-dessus', 'weak': 'au moins 1 écart-type au-dessus des clés ajustées sur le mélange, sans réussir',
             'underdetermined': 'la recherche fait mieux que la lecture sur le vrai chiffré : le test ne tranche pas',
             'too short': 'moins de 40 symboles lus, ou moins de 80 lettres', 'fail': 'une clé ajustée sur le texte mélangé fait aussi bien',
             'not applicable': 'transposition, texte clair non alphabétique, ou symboles à plusieurs valeurs (plus de 10&nbsp;%)'}
    verd = table(['Verdict', 'Sens', 'Fiches'], [[f'<code>{x}</code> ({FR_VERDICT[x]})', vmean[x], n(v.get(x, 0))] for x in VERDICTS],
                 total=['Tous les verdicts', '', n(c['verdicts_total'])])
    signers = table(['Qui a signé la note', 'Entrées'], [
        ['un modèle d’IA', f"{n(k['model'])} ({F['model_pct']})"], ['une personne assistée d’un modèle d’IA', n(k['person+model'])],
        ['une personne, sans modèle nommé', f"{n(k['person'])} (dont {n(c.get('rr_edition', 0))} désignent une édition publiée, pas un relecteur)"],
        ['on ne sait pas', n(k['unclear'])]], total=['Toutes les entrées notées', f"{n(c['rr'])}, dans {n(c['rr_profiles'])} fiches"])
    checks = table(['Contrôle', 'Quand il tourne', 'Ce qu’il vérifie', 'Ce qu’il ne vérifie pas'], [
        ['Check write-ups', 'à chaque envoi sur <code>main</code> et à chaque demande de fusion',
         'les en-têtes des pages, les liens morts et le balisage HTML ; les tests unitaires des scripts', 'rien sur les lectures elles-mêmes'],
        ['Reading check', 'à chaque demande de fusion, sur les seules cibles qu’elle modifie',
         'pour chaque document <code>read</code> ou <code>read in part</code> : une note A ou B (la sienne, ou celle de l’audit) et une traduction anglaise ; un <code>read_share</code> d’au moins 0,95 pour un document <code>read</code>, s’il est enregistré ; l’accord entre la classe de la cible et l’état de ses documents',
         'qui a donné la note ; le test statistique ; le témoin ; toute comparaison avec les images ; les cibles que la demande ne touche pas']])
    body = f'''<main>

<div class="callout glance"><p><b>En bref</b></p>
<ul>
<li>Le travail est fait surtout par des modèles d’IA, pilotés par des personnes.</li>
<li>La note de lecture (A ou B) est donnée par un modèle d’IA pour {F['model_pct']} des entrées. Ce n’est pas une relecture humaine.</li>
<li>Une vérification d’un passage sur l’image par une personne, sans IA, est déclarée dans {n(c['hc_profiles'])} fiches.</li>
<li>Les contrôles automatiques vérifient la forme d’une lecture. Ils ne vérifient pas qu’elle est juste.</li>
<li>Toute lecture peut être contestée. Les corrections restent dans l’historique du dépôt.</li>
</ul></div>

<h2 id="ce-qu-est-le-projet"><span class="num">01</span> Ce qu’est ce projet</h2>
<p>Cyphersolver est un registre ouvert de chiffres historiques. Les chiffres y sont travaillés avec des modèles d’IA. Le registre sert aussi de banc d’essai informel de ce que ces modèles savent en faire.</p>
<p>Des personnes pilotent les modèles d’IA : les mainteneurs du projet et des contributeurs extérieurs.</p>
<p>Le registre compte {n(c['profiles'])} fiches de cibles. {n(pv['project'])} relèvent du travail du projet, {n(pv['contributed'])} sont des contributions extérieures et {n(pv['mixed'])} sont mixtes.</p>
<p>Ce registre n’est pas une édition critique. Ses résultats n’ont pas été évalués par des pairs au sens académique.</p>
<p>Mots employés sur cette page :</p>
<ul>
<li>Une <b>cible</b> est un dossier du dépôt : un document chiffré ou un groupe de documents.</li>
<li>Sa <b>fiche</b> est le fichier <code>profile.json</code>, à champs fixes. Les notes de travail sont dans <code>NOTES.md</code>.</li>
<li>Un <b>article</b> est la page du site consacrée à la cible.</li>
</ul>
<p>Les règles complètes sont dans le {gh('README.md', 'README')} (section Conventions), {gh('CONTRIBUTING.md')} et {gh('profile.schema.json')}, en anglais.</p>

<h2 id="etapes"><span class="num">02</span> Les étapes d’une lecture</h2>
{steps}

<h2 id="sources"><span class="num">03</span> Sources et travaux antérieurs</h2>
<p>Chaque image du site doit être créditée à sa source : détenteur, cote, folio, et voie d’accès (Gallica, DECODE, visionneuse d’un service d’archives, IIIF, édition). C’est la règle du README. Elle n’est pas vérifiée page par page.</p>
<p>Les images restent soumises aux conditions de leurs détenteurs. Les textes sont sous licence CC BY 4.0, le code sous licence MIT.</p>
<p>Depuis le 28 octobre 2026, un document n’entre au <a href="catalogue.html">catalogue</a> que si sa fiche montre deux choses. Le chiffré a été vu sur une image. Les lieux habituels d’un déchiffrement antérieur ont été consultés : DECODE, les listes de Satoshi Tomokiyo, l’inventaire ou l’édition imprimée, et la littérature. Les entrées plus anciennes ne sont pas passées par cette grille.</p>
<p>Une fiche peut dire si une lecture existait avant celle du projet. {n(c['exists_answered'])} fiches sur {n(c['profiles'])} répondent. {n(c['exists_earlier'])} signalent une lecture antérieure, complète ou partielle. Pour {n(c['found'].get('after reading', 0))} d’entre elles, elle n’a été trouvée qu’après la lecture du projet.</p>
<p>Le contrôleur des articles demande de créditer dans la fiche une lecture antérieure imprimée, en ligne, inédite ou partielle. {n(c.get('credited', 0))} des {n(c.get('to_credit', 0))} fiches concernées le font. Une solution antérieure jamais publiée n’est montrée en entier qu’avec l’accord de son auteur.</p>

<h2 id="transcription"><span class="num">04</span> Transcription</h2>
<p>Recopier le chiffré depuis le manuscrit est déjà une source d’erreur. Les fiches disent qui a transcrit chaque document.</p>
{trans}
<p>Il n’y a pas de double transcription à l’aveugle systématique. Les notes de certaines cibles comparent deux transcriptions ; le projet ne publie pas de taux d’accord d’ensemble.</p>
<p>Une transcription est parfois corrigée après que la clé a été trouvée. La lecture peut alors dépendre de la clé qu’elle doit mettre à l’épreuve. Les articles ne le signalent pas de façon uniforme.</p>
{ts_txt}

<h2 id="cle"><span class="num">05</span> Comment la clé est obtenue</h2>
<p>Chaque fiche range sa méthode dans l’une des catégories du <a href="glossary.html">glossaire</a> (en anglais).</p>
{methods}
<p>Un résultat négatif doit venir avec un <b>témoin</b> : un texte synthétique de même longueur, de même alphabet et de même système, que le même solveur parvient à casser. C’est la règle du README. Elle n’est pas contrôlée : {n(c.get('notsolved_control', 0))} des {n(c['m_notsolved'])} fiches <code>not solved</code> déclarent un témoin.</p>
<p>Un <b>test sur une portion tenue à l’écart</b> consiste à trouver la clé sans regarder une partie du texte, puis à essayer la clé sur cette partie. Aucune règle du projet ne l’exige. Certains contributeurs le font et le décrivent dans les notes de la cible.</p>
<p>Dans le protocole que suivent certains contributeurs, une clé trouvée par cryptanalyse l’est <b>sur une partie du texte seulement</b>. Le reste n’est pas analysé et sert de validation. Les étapes sont les suivantes : choisir la portion tenue à l’écart avant tout travail dessus ; geler la clé par une empreinte SHA-256 ; puis déchiffrer une seule fois la portion tenue à l’écart, sans retoucher la clé. Le test est réussi quand la part des lettres qui font sens atteint 0,85 et dépasse d’au moins 0,30 la meilleure de 200 clés mélangées. Les notes de ces cibles donnent l’empreinte, la portion et le score, y compris quand le test échoue.</p>

<h2 id="dechiffre-n-est-pas-lu"><span class="num">06</span> Un déchiffrement n’est pas encore une lecture</h2>
<p>Une clé qui change le chiffré en mots ne donne pas encore un texte. Chaque document d’une fiche porte l’un de quatre états. Les noms sont ceux des fiches, en anglais.</p>
{state_t}
<p><b>La part de mots lus</b> (<code>read_share</code>) ne compte que les mots chiffrés. Dans une lettre qui mêle texte clair et chiffre, elle se mesure sur les mots écrits en chiffre ; les mots en clair qui les entourent ne sont ni lus ni non lus et restent hors du numérateur comme du dénominateur.</p>
<p>Seuls les mots sûrs comptent comme lus. Un mot est lu quand la clé le donne, ou le texte clair voisin, sans rien restituer. Un mot probable (<code>&#123;x&#125;</code>), un mot inféré ou restitué, un mot de note M et un code non valué sont des trous, de même qu’une lettre restituée à l’intérieur d’un mot. <code>read_share</code> vaut 1 moins la part des trous parmi les mots chiffrés. Elle est comptée par un script quand la lecture déclare son balisage.</p>
<p>Le seuil de 95&nbsp;% s’applique aux mots chiffrés de chaque document. <b>Plancher des textes courts :</b> un document de moins de 40 mots chiffrés est <code>read</code> quand ses trous font au plus 5&nbsp;% de ses mots chiffrés ou au plus 2 mots, selon ce qui en permet le plus. Le plancher ne s’applique jamais à un texte de 40 mots ou plus, et la page et la fiche indiquent le nombre de trous et que le plancher a servi.</p>
<p>Ce nombre compte les trous que le lecteur a marqués. Il ne dit pas si les mots lus sont justes.</p>
<p><b>Le déchiffrement et la lecture sont deux fichiers.</b> Le déchiffrement est la clé appliquée à la transcription, signe par signe, sans aucune retouche : un mot que la clé donne faux y reste faux. La lecture est ce texte mis en phrases, et toute lettre ou tout mot que la clé ne donne pas pour les signes tels que transcrits y est marqué ; les lettres marquées sont des trous. Un texte qui est un déchiffrement d’époque, une copie au net ou une édition est signalé comme tel. Cette règle date du 16 novembre 2026 (README, Conventions). Un audit des 54 cibles signalées par son script a trouvé des mots qui s’écartent de la clé, sans marque, dans 35 d’entre elles ; des marques ont été ajoutées dans 31 cibles (858 endroits). Le script n’a pas pu comparer 757 textes sur 938 à leur clé : des lectures faites avant cette date peuvent donc encore contenir des modifications non marquées. L’audit est dans <a href="{REPO}/tree/main/research/decrypt_audit" rel="noopener"><code>research/decrypt_audit</code></a>.</p>
<p>{n(c.get('read_no_share', 0))} documents à l’état <code>read</code> n’ont pas de <code>read_share</code> enregistré. Pour eux, les 95&nbsp;% ne sont pas mesurés document par document.</p>
<p>Le seuil de 95&nbsp;% est propre au projet. Aucune norme du domaine n’en fixe un.</p>
<p>Un cas particulier. Dans un code lu avec la clé d’époque conservée, un groupe qui s’écarte d’un seul chiffre de la valeur qu’exige le sens compte comme lu, à trois conditions. L’erreur se voit sur l’image. Les autres groupes du mot viennent de la clé. Les groupes corrigés forment le mot entier. Le groupe est marqué <code>{{+...}}</code> dans le texte.</p>

<h2 id="controles-statistiques"><span class="num">07</span> Le test statistique contre les faux positifs</h2>
<p>Le risque : une clé qui a assez de valeurs libres peut produire des mots, même quand elle est fausse.</p>
<p>Le test est {gh('docs/_validate.py')}. Il donne un score à la lecture avec un modèle de lettres de l’époque (suites de 4 lettres). Puis il compare ce score à deux références :</p>
<ul>
<li>des clés tirées au hasard, de même structure ;</li>
<li>des clés ajustées par la même recherche sur le chiffré mélangé (6 mélanges).</li>
</ul>
<p>Une lecture <b>réussit</b> quand son score dépasse d’au moins 5 écarts-types celui des clés au hasard, dépasse toutes les clés ajustées sur le texte mélangé, et dépasse leur moyenne d’au moins 3 écarts-types.</p>
{verd}
<p>Les contrôles automatiques n’exigent pas ce test. Sur les {n(c['crypt_read'])} fiches dont la clé a été reconstituée ici et dont le texte a été obtenu en tout ou en partie, {n(c['crypt_unval'])} n’ont pas de verdict : {unval_text(c, L, names)}.</p>
<p>Ce que le test ne montre pas :</p>
<ul>
<li>il note des lettres : il ne vérifie ni le sens, ni une valeur de code proposée d’après le contexte ;</li>
<li>il ne tient pas compte du nombre de lectures testées ;</li>
<li>sur les textes courts et les chiffres homophoniques, il ne tranche souvent pas ;</li>
<li>à notre connaissance, aucun statisticien extérieur ne l’a examiné.</li>
</ul>

<h2 id="relecture"><span class="num">08</span> La note de lecture et la vérification humaine</h2>
<p>Une <b>note de lecture</b> (<code>reading_review</code>) est enregistrée dans la fiche, document par document. Un lecteur a lu le déchiffrement comme des phrases. Il lui donne A ou B :</p>
<ul>
<li>A : des phrases cohérentes, avec des trous épars ;</li>
<li>B : cohérent mais brut (sans espaces, en capitales, en lignes de décodeur), et remis en forme dans la lecture ou la traduction.</li>
</ul>
<p>A et B ne sont pas des notes d’exactitude. Elles disent que le texte forme des phrases. Elles ne disent pas qu’il a été comparé aux images.</p>
<p>La note est exigée pour les documents <code>read</code> et <code>read in part</code>. Le schéma admet une personne ou un modèle d’IA désigné comme tel. CONTRIBUTING veut que la note soit enregistrée par le relecteur, pas par l’auteur. Aucun contrôle automatique ne regarde qui l’a donnée.</p>
<p><b>La plupart des notes A et B sont attribuées par un modèle d’IA.</b></p>
{signers}
<p>Pour au moins {n(c.get('rr_not_independent', 0))} entrées, la fiche dit elle-même que le lecteur n’était pas indépendant du travail (par exemple, la même session). Au moins {n(c.get('rr_authors_agent', 0))} autres sont signées par un agent qui travaille pour l’auteur de la lecture. Ces entrées ne remplissent pas, ou pas clairement, la règle de CONTRIBUTING.</p>
<p>{n(c.get('graded_no_rr', 0))} documents <code>read</code> ou <code>read in part</code> n’ont pas de note propre. Pour {n(c.get('no_rr_audit_ab', 0))} d’entre eux, le contrôle reprend la note de l’audit des lectures du 22 octobre 2026, donnée par un modèle d’IA. {n(c.get('no_rr_audit_other', 0))} ont une note d’audit qui n’est ni A ni B, et {n(c.get('no_rr_none', 0))} n’ont aucune note. Ils ne sont pas comptés dans le tableau.</p>
<p><b>La seconde relecture d’une lecture est donc un lecteur-modèle, associé aux contrôles automatiques. Ce n’est pas une relecture humaine.</b></p>
<p>La <b>vérification humaine</b> (<code>human_check</code>) est autre chose. Une personne compare un passage à l’image, sans aide de l’IA, et note le résultat : confirmé, corrigé ou en désaccord. C’est déclaré dans la fiche. Cela concerne {n(c['hc_profiles'])} fiches ({hc_txt}).</p>
<p>Quand un caractère ou un alphabet est douteux, un contributeur peut faire des <b>relectures ciblées à l’aveugle</b>. Une personne voit seulement le signe douteux, découpé dans l’image, à côté de deux ou trois formes candidates. Elle ne voit ni la lecture attendue, ni la glose, ni le contexte. Elle choisit la forme qu’elle voit. Cela confirme ou infirme une valeur, une lecture ou un alphabet entier, sans le biais de connaître la réponse. C’est une vérification de la forme des signes, pas une relecture du texte, et elle est notée comme telle.</p>
<p>{n(c.get('indep_verif', 0))} fiches déclarent aussi une « independent verification » : quelqu’un d’extérieur au projet a vérifié la lecture sur les images ou avec sa propre clé. Ce champ ne dit pas si cette personne a utilisé un modèle d’IA.</p>
<p>{n(queue)} lectures dont la clé a été reconstituée ou rapprochée ici <a href="contributors.html#verify">attendent une vérification indépendante</a>.</p>
<p class="cmuted"><b>Comment ces chiffres sont comptés.</b> Une entrée notée est un élément de <code>outcome.texts</code> dans la fiche <code>profile.json</code> d’une cible qui porte un <code>reading_review</code>, quel que soit son état. Seuls les fichiers <code>targets/&lt;dossier&gt;/profile.json</code> sont comptés. Le signataire est classé d’après le champ <code>by</code> : <i>modèle</i> s’il nomme un modèle d’IA, un agent ou une session d’IA et qu’aucune personne n’est nommée d’abord ; <i>personne assistée d’un modèle d’IA</i> si une personne est nommée d’abord et dit qu’un modèle d’IA l’a assistée ; <i>personne</i> si aucun modèle n’est nommé ; <i>on ne sait pas</i> s’il ne nomme ni l’un ni l’autre (« project verification pass »). « Non indépendant » et « agent qui travaille pour l’auteur » sont repérés par une recherche de mots dans <code>by</code> et <code>note</code> : ce sont des bornes basses. Compter par document ou par cible donne d’autres totaux. La règle est dans {gh('docs/_method_page.py')}.</p>

<h3 id="signes">Un niveau de vérification : déchiffrement par IA, vérifié par une personne sur un échantillon de signes</h3>
<p>Entre aucune vérification et une relecture complète sur les images, une lecture peut porter le niveau <b>Déchiffrement par IA, vérifié par une personne sur un échantillon de signes</b>. Un modèle d’IA a transcrit et déchiffré le texte. Une personne a ensuite choisi, à l’aveugle, la forme qu’elle voit pour un ensemble de signes, sur une planche de relecture :</p>
<ul>
<li>une règle écrite avant la construction de la planche, et datée avant toute réponse, choisit les signes : formes douteuses, signes dont dépendent plusieurs mots, groupes de code ;</li>
<li>chaque question encadre un seul signe sur sa ligne. Les options sont des formes découpées dans le même document, plus « aucune / autre forme », « illisible » et « pas un signe », qui laissent le mot marqué. Aucune glose, lecture, valeur ni aucun lieu n’est montré ;</li>
<li>au moins deux contrôles à réponse connue sont mêlés aux questions, pris à des endroits aussi difficiles que les cibles. La correspondance reste privée jusqu’à l’export des réponses.</li>
</ul>
<p>La fiche (<code>sign_check</code> dans <code>profile.json</code>) donne la date ; qui a répondu, et si cette personne est du projet ou extérieure ; ce qu’un modèle d’IA a fait (écrit la règle, découpé les vignettes, construit la planche, dépouillé les réponses, interprété les remarques libres) ; combien de signes ont été vérifiés et comment ils ont été choisis (une section des NOTES de la cible) ; combien de contrôles ont réussi ; et les résultats : tels que transcrits, corrigés, non résolus, non comptés. La page d’une lecture le dit en une phrase, par exemple : « 9 signes douteux vérifiés à l’aveugle par un membre du projet, sur une planche construite et dépouillée par un modèle d’IA ; règle dans les NOTES ; contrôles 2 sur 2 ; 2 tels que transcrits, 7 corrigés, 1 non compté (vignette fautive) ».</p>
<p>Une planche n’atteint le niveau qu’avec au moins {SIGN_MIN_CONTROLS} contrôles, tous réussis, et au moins {SIGN_MIN_SIGNS} signes cibles une fois retirées les réponses touchées par une vignette fautive. Une réponse « aucune / autre » à un contrôle compte comme un échec. Ce qu’une réponse contredit est d’abord recodé ou marqué dans la lecture. Ce sont les règles du projet (README, Conventions ; décision du propriétaire du 19 novembre 2026) : le vérificateur est nommé, et le libellé ne dit rien de la clé. La date de la règle et son empreinte SHA-256 identifient les critères enregistrés avant les réponses. Pour une planche commune, compter les signes de chaque cible séparément.</p>
<p><b>Le niveau dit comment une lecture a été vérifiée, pas quelle part en est lue.</b> Il ne change jamais la classe, l’état ni la part lue : une lecture peut le porter et garder l’état <code>read in part</code>. Il vérifie la forme des signes, pas la clé, la valeur d’un code ni la lecture dans son ensemble. Les signes sont choisis parce qu’ils sont douteux : c’est un diagnostic, pas un échantillon tiré au hasard, et il ne dit rien des signes qui n’ont pas été montrés. Deux contrôles réussis disent peu de chose à eux seuls : un vérificateur qui a raison une fois sur deux les réussit tous les deux une fois sur quatre. Ce n’est pas une <code>human_check</code>, que le schéma définit comme une vérification sans aide de l’IA.</p>
<p>Les premières lectures à le porter sont celles dont la clé a été construite sur une partie du matériau (le document ou des lettres sœurs du même chiffre) et a réussi un test sur un passage qui n’a pas servi à la construire, contre un seuil écrit d’abord ; la page de la lecture donne l’historique des essais. Sur ces premières lectures, <b>le vérificateur est le contributeur</b> de la lecture, membre du projet, qui a répondu aux planches de ses propres lectures : la vérification n’est pas indépendante, et la fiche comme la page de la lecture le disent. {n(c['sc_profiles'])} fiches portent une <code>sign_check</code> ({n(c['sc'])} planches, dont {n(c['sc_level'])} au niveau et {n(c['sc_external'])} remplies par une personne extérieure au projet).</p>

<h2 id="controles"><span class="num">09</span> Ce que les contrôles automatiques imposent</h2>
<p>Deux contrôles tournent seuls sur GitHub (intégration continue, ou CI).</p>
{checks}
<p>Les autres règles (le test statistique, le crédit des lectures antérieures, la vérification humaine, la grille du catalogue) sont vérifiées par des scripts lancés à la main. Elles ne bloquent pas une fusion.</p>
{rc}<p><b>L’intégration.</b> Une modification d’un résultat entre dans le dépôt par une demande de fusion approuvée par un mainteneur qui n’en est pas l’auteur (CONTRIBUTING, « Review and merging »). Un jeu de règles sur la branche <code>main</code> en applique une partie : il exige une demande de fusion et la relecture d’un responsable du code ({gh('.github/CODEOWNERS', 'CODEOWNERS')}), mais pas que les deux contrôles passent, ce que CONTRIBUTING demande aussi. L’administrateur du dépôt et la reconstruction automatique du site (par une clé de déploiement) peuvent envoyer sur <code>main</code> sans demande de fusion, et le propriétaire l’a fait directement : la règle ne s’applique donc pas à toute modification.</p>

<h2 id="ia"><span class="num">10</span> La part de l’IA</h2>
<p>Les fiches nomment les modèles d’IA qui ont fait le travail (<code>conditions.models</code>). Elles disent ce qu’a fait la personne (<code>conditions.human_role</code>) : fournir des images ou des accès, indiquer une source, corriger une lecture.</p>
<p>Les scripts, les clés et les transcriptions sont versionnés. Le README donne les commandes qui reproduisent deux résultats.</p>
<p>Une étape faite par un modèle d’IA ne peut pas être rejouée à l’identique : transcrire une image, proposer une valeur de code d’après le contexte. Les modèles sont propriétaires.</p>
<p>Le coût de chaque résultat (usage des modèles, argent, temps humain) n’est pas publié.</p>

<h2 id="corrections"><span class="num">11</span> Corrections et contestations</h2>
<p>Toute lecture peut être contestée ou vérifiée.</p>
<p>Sur GitHub, le <a href="{REPO}/issues/new?template=verification.yml" rel="noopener">formulaire Verification</a> demande le passage et les images utilisées, chaque point où votre lecture s’accorde avec la page ou s’en écarte, et les valeurs de clé que vous changeriez.</p>
<p>Sans compte GitHub, écrivez par <a href="contribute.html#email">courriel</a>.</p>
<p>Chaque article porte à son pied un lien « Contest or verify this reading ». Indiquez le passage, les images, et les endroits où votre lecture diffère. Aucun délai de réponse n’est promis.</p>
<p>Une correction est portée sur la page avec sa date, reste dans l’historique du dépôt et est inscrite au <a href="corrections.html">journal des corrections</a> (en anglais) : la date, les pages, ce qui a changé, qui l’a signalé et pourquoi c’était faux. Le journal commence le 16 novembre 2026.</p>

<h2 id="chercheurs"><span class="num">12</span> Pour les chercheurs, et comment citer</h2>
<p>Cryptologues, paléographes, archivistes et historiens peuvent :</p>
<ul>
<li>vérifier une lecture sur les images (<a href="contributors.html#verify">la liste en attente de vérification</a>) ;</li>
<li>prolonger une lecture partielle (<a href="further.html">Read further</a>) ;</li>
<li>consulter un document dans son service d’archives (<a href="archives.html">To the archive</a>).</li>
</ul>
<p>Les contributions sont créditées dans la fiche (<code>outcome.credits</code>) et sur la page <a href="contributors.html">Contributors</a>.</p>
<p>Chaque article a un bloc « Cite this page » avec une notice BibTeX : la date de mise en ligne, celle de la dernière modification et le commit du dépôt dont le site est issu. Une page peut changer à la même adresse : citez le commit et la date de consultation. Il n’y a pas de DOI.</p>
'''
    return head(L, 'Méthode et relecture &mdash; comment une lecture est établie, contrôlée et notée',
                'Comment chaque lecture de Cyphersolver est transcrite, déchiffrée, testée et notée, qui fait chaque étape, '
                'et ce que les contrôles ne couvrent pas. Les chiffres sont comptés dans les fiches à chaque construction du site.') + f'''<section class="hero">
  <p class="kicker">Référence &middot; méthode &middot; relecture</p>
  <h1>Méthode et relecture</h1>
  <p class="sub">Comment une lecture de ce site est établie, contrôlée et notée. Qui fait chaque étape. Ce que les contrôles ne couvrent pas. Chaque décompte de cette page est refait dans le dépôt à chaque construction du site.</p>
  <p class="meta">Daniel Bourdeau</p>
  <p class="langswitch"><a href="method.html" hreflang="en" lang="en">English version</a></p>
</section>

''' + fr_typo(body) + TAIL


def build_html(pages, profiles):
    """Write method.html and method-fr.html; returns the counts."""
    import _contributors_page as CP
    names = contributor_names()
    c = review_counts(names=names)
    q = len(CP.queue(pages, profiles))
    (HERE / 'method.html').write_text(page_en(c, q, names), encoding='utf-8')
    (HERE / 'method-fr.html').write_text(page_fr(c, q, names), encoding='utf-8')
    return c


if __name__ == '__main__':
    audit = load_audit(sys.argv[1]) if len(sys.argv) > 1 else None      # optional: a reviews.json outside the checkout
    c = review_counts(audit=audit)
    for key in sorted(c):
        print(f'{key}: {c[key]}')
