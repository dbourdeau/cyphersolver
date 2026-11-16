"""Build docs/method.html and docs/method-fr.html: how a reading is made, checked and graded, and by whom.

Every figure on the two pages is counted here from the records when the site is built (review_counts below), never
written by hand. The reviewer classes follow the rule of the maintainers' script count_reviews.py: one entry per
outcome.texts[] item of targets/<folder>/profile.json that carries a reading_review, its `by` string classed by
kind_of(). Only targets/<folder>/profile.json is read, one level below targets/.

Called from _build_site.py: build_html(PAGES, PROFILES) before the pages are processed, so both pages get the nav,
footer, contents strip and dateline like any other page. The French page is a translation of this page only.

  python docs/_method_page.py          print the figures as the build computes them (read-only)
"""
import collections, html, json, pathlib, re

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
# model families for conditions.models (the ids are free text and not normalised)
CLAUDE = re.compile(r'claude|anthropic|opus|sonnet|fable|haiku', re.I)
OPENAI = re.compile(r'\bgpt|chatgpt|codex|openai', re.I)


def kind_of(by):
    """model | person+model | person | unclear, by count_reviews.py's rule."""
    by = by or ''
    if not MODEL.search(by):
        return 'unclear' if UNCLEAR.search(by) else 'person'
    if PERSON_ASSISTED.search(by):
        return 'person+model'
    return 'model'


def as_list(x):
    if not x:
        return []
    return x if isinstance(x, list) else [x]


CRYPT = ('key recovered from ciphertext-only', 'key recovered based on plaintext from external sources',
         'key recovered based on adjacent plaintext')
APPLIED = ('read after matching with key from external sources', 'read with known key', 'read from existing decipherment')
EARLIER = ('in archive', 'in print', 'online', 'partial', 'unpublished')


def review_counts(root=ROOT):
    """All the figures of the page, from root/targets/*/profile.json. Pure: reads files, writes nothing."""
    root = pathlib.Path(root)
    c = collections.defaultdict(int)
    kinds, states, verdicts, transcr, prov = (collections.Counter() for _ in range(5))
    exists, found, hc_result, unval_prov, unval_who = (collections.Counter() for _ in range(5))
    families = collections.Counter()
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
        prov[o.get('provenance', 'project')] += 1
        method = o.get('method') or ''
        c['m_crypt'] += method in CRYPT
        c['m_applied'] += method in APPLIED
        c['m_notsolved'] += method == 'not solved'
        c['m_na'] += method == 'not applicable'
        # documents: who transcribed
        for d in as_list(prof.get('documents')):
            if isinstance(d, dict):
                t = d.get('transcription')
                transcr[(t.get('by') if isinstance(t, dict) else None) or 'not stated'] += 1
        # text entries: state, reading_review
        for t in as_list(o.get('texts')):
            if not isinstance(t, dict):
                continue
            c['texts'] += 1
            states[t.get('state', 'read')] += 1
            r = t.get('reading_review')
            if not r:
                c['read_no_rr'] += t.get('state', 'read') == 'read'
                continue
            c['rr'] += 1
            k = kind_of(r.get('by'))
            kinds[k] += 1
            if k == 'person' and EDITION.search(r.get('by') or ''):
                c['rr_edition'] += 1
            if NOT_INDEPENDENT.search(f"{r.get('by') or ''} {r.get('note') or ''}"):
                c['rr_not_independent'] += 1
            c['rr_A'] += r.get('grade') == 'A'
            c['rr_B'] += r.get('grade') == 'B'
        # human_check
        hcs = [h for h in as_list(o.get('human_check')) if isinstance(h, dict)]
        if hcs:
            c['hc_profiles'] += 1
            c['hc'] += len(hcs)
            hc_result.update(h.get('result') for h in hcs)
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
                unval_prov[o.get('provenance', 'project')] += 1
                if o.get('provenance', 'project') == 'contributed':
                    for w in sorted({x.get('who') for x in as_list(o.get('credits')) if isinstance(x, dict)
                                     and x.get('role') in ('solution', 'new cipher with solution') and x.get('who')}):
                        unval_who[w] += 1
        # earlier readings
        ps = cond.get('prior_solution')
        if isinstance(ps, dict):
            exists[ps.get('exists')] += 1
            if ps.get('exists') in EARLIER:
                found[ps.get('found')] += 1
        # models
        ms = [str(m) for m in as_list(cond.get('models'))]
        if not ms or any(m.strip().lower() == 'unknown' for m in ms):
            families['unknown'] += 1
        else:
            if any(CLAUDE.search(m) for m in ms): families['claude'] += 1
            if any(OPENAI.search(m) for m in ms): families['openai'] += 1
            if any(not CLAUDE.search(m) and not OPENAI.search(m) for m in ms): families['other'] += 1
        if (root / 'targets' / path.parent.name / 'timestamps').is_dir():
            c['timestamped'] += 1
    c.update(dict(kinds=kinds, states=states, verdicts=verdicts, transcr=transcr, prov=prov, exists=exists, found=found,
                  hc_result=hc_result, unval_prov=unval_prov, unval_who=unval_who, families=families))
    c['verdicts_total'] = sum(verdicts.values())
    c['exists_answered'] = sum(n for k, n in exists.items() if k not in (None, 'unknown'))
    c['exists_earlier'] = sum(exists[k] for k in EARLIER)
    return dict(c)


def contributor_names():
    try:
        reg = json.loads((ROOT / 'contributors.json').read_text(encoding='utf-8'))['contributors']
    except (OSError, ValueError, KeyError):
        return {}
    return {x['id']: x.get('name', x['id']) for x in reg if isinstance(x, dict) and x.get('id')}


# --- formatting -----------------------------------------------------------------------------------------------
def num(n, lang):
    s = f'{int(n):,}'
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


def solver_list(c, lang, names):
    who = c['unval_who'].most_common()
    return join([f'{num(n, lang)} {esc(names.get(w, w))}' for w, n in who], lang)


def unval_text(c, lang, names):
    """Who produced the cryptanalytic results that carry no statistical verdict, zero parts left out."""
    up = c['unval_prov']
    if lang == 'fr':
        parts = [(up.get('contributed', 0), lambda x: f"{x} {'sont des r&eacute;sultats' if int(x.replace('&#8239;', '')) > 1 else 'est un r&eacute;sultat'} de contributeurs ext&eacute;rieurs ({solver_list(c, lang, names)})"),
                 (up.get('mixed', 0), lambda x: f"{x} {'sont mixtes' if int(x.replace('&#8239;', '')) > 1 else 'est mixte'}"),
                 (up.get('project', 0), lambda x: f"{x} {'rel&egrave;vent' if int(x.replace('&#8239;', '')) > 1 else 'rel&egrave;ve'} du projet")]
    else:
        parts = [(up.get('contributed', 0), lambda x: f"{x} {'are results' if x != '1' else 'is a result'} contributed from outside ({solver_list(c, lang, names)})"),
                 (up.get('mixed', 0), lambda x: f"{x} {'are' if x != '1' else 'is'} mixed"),
                 (up.get('project', 0), lambda x: f"{x} {'are' if x != '1' else 'is'} the project&rsquo;s own")]
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


# --- English ---------------------------------------------------------------------------------------------------
def page_en(c, queue, names):
    L = 'en'
    n = lambda x: num(x, L)
    k, st, v, tr, pv, hr = c['kinds'], c['states'], c['verdicts'], c['transcr'], c['prov'], c['hc_result']
    fam = c['families']
    verdict_txt = join([f'{n(v[x])} {x}' for x in ('pass', 'weak', 'underdetermined', 'too short', 'fail', 'not applicable') if v.get(x)], L)
    hc_txt = join([f'{n(hr[x])} {x}' for x in ('confirmed', 'corrected', 'disagreed') if hr.get(x)], L)
    tr_other = c_sum(tr, exclude=('llm from images', 'mixed', 'DECODE', 'published', 'human (project)'))
    up = c['unval_prov']
    unval_txt = unval_text(c, L, names)
    return head(L, 'Method and review &mdash; how a reading is made, checked and graded',
                'How each reading on Cyphersolver is transcribed, deciphered, tested and graded, who does each step, '
                'and what the checks do not cover. The figures are counted from the records at each build.') + f'''<section class="hero">
  <p class="kicker">Reference &middot; method &middot; review</p>
  <h1>Method and review</h1>
  <p class="sub">How a reading on this site is made, checked and graded, who does each step, and what the checks do not cover. Every count on this page is computed from the repository&rsquo;s records each time the site is built.</p>
  <p class="meta">Daniel Bourdeau</p>
  <p class="langswitch"><a href="method-fr.html" hreflang="fr" lang="fr">Version fran&ccedil;aise</a></p>
</section>

<main>

<h2 id="what-it-is"><span class="num">01</span> What this project is</h2>
<p>Cyphersolver is an open ledger of historical ciphers worked on with AI models, and an informal benchmark of what those models can do with them. Most of the work is done with Anthropic&rsquo;s Claude models, run by the project&rsquo;s maintainers; outside contributors send results too, some made with other models. Of the {n(c['profiles'])} target records, {n(pv['project'])} are the project&rsquo;s own work, {n(pv['contributed'])} were contributed from outside and {n(pv['mixed'])} are mixed.</p>
<p>The ledger is not a critical edition, and its results have not been peer-reviewed in the academic sense. This page summarises the rules; the full text is in the repository: the Conventions in the {gh('README.md', 'README')}, {gh('CONTRIBUTING.md')} and {gh('profile.schema.json')}. Each target has a folder with its working notes (<code>NOTES.md</code>) and a fixed-field record (<code>profile.json</code>).</p>

<h2 id="sources"><span class="num">02</span> Sources and earlier work</h2>
<p>The project&rsquo;s rule is that every image on the site is credited to its source: holder, shelfmark and folio, and the route to it (Gallica, a DECODE record, an archive&rsquo;s viewer, IIIF or a printed edition). Images remain under their holders&rsquo; terms; text is released under CC BY 4.0 and code under MIT.</p>
<p>Since 28 October 2026, a document enters the <a href="catalogue.html">catalogue</a> of open items only when its record shows that the ciphertext was seen and that the usual places for an earlier decipherment were searched: the DECODE record, Satoshi Tomokiyo&rsquo;s lists, the printed calendar or edition, and the literature.</p>
<p>The records say whether a reading existed before the project&rsquo;s, and when it was found. {n(c['exists_answered'])} of {n(c['profiles'])} records answer the question: {n(c['exists_earlier'])} record an earlier reading, complete or partial, in an archive, in print, online or unpublished; in {n(c['found'].get('after reading', 0))} of these it came to light only after the project&rsquo;s own reading. By the project&rsquo;s rule, an earlier decipherment is credited by name on the write-up and on <a href="contributors.html">Contributors</a>, including when it is found afterwards. An earlier solution that was never published is credited only with its author&rsquo;s agreement.</p>

<h2 id="transcription"><span class="num">03</span> Transcription</h2>
<p>Copying the cipher from the manuscript into a text file is a source of error in its own right. The records say who transcribed each document. Of {n(sum(tr.values()))} documents, {n(tr['llm from images'])} were transcribed by a model from the images, {n(tr['mixed'])} combine several sources, {n(tr['DECODE'])} were taken from DECODE, {n(tr['published'])} from a printed edition, and {n(tr['human (project)'])} by a person working for the project; {n(tr_other)} have another source or none stated.</p>
<p>There is no systematic double blind transcription and no published rate of agreement between two transcribers. A transcription is sometimes corrected after the key is found; the reading can then depend on the key it is meant to test. The write-ups do not yet flag this in a uniform way. In {n(c['timestamped'])} targets the key and the transcriptions were frozen and time-stamped (an RFC 3161 token and an OpenTimestamps proof) before scoring, so that a later test on a held-out part can be dated against them.</p>

<h2 id="key"><span class="num">04</span> How the key is obtained</h2>
<p>Every write-up states its method in one of the categories of the <a href="glossary.html">glossary</a>. Three are cryptanalysis done here: the key was recovered from the ciphertext alone, from a plaintext found elsewhere, or from a plaintext next to the cipher (a decipherment written between the lines, a passage in clear). The others apply a key or a decipherment that already existed; there the work is transcription and decipherment. Of the {n(c['profiles'])} records, {n(c['m_crypt'])} recovered a key by cryptanalysis, {n(c['m_applied'])} applied an existing key or decipherment, {n(c['m_notsolved'])} obtained neither key nor text, and {n(c['m_na'])} are not ciphers or could not be reached.</p>
<p>By the project&rsquo;s rule, a negative result is reported only with a matched control: a synthetic text of the same length, alphabet and cipher design that the same solver does recover.</p>

<h2 id="decoded-is-not-read"><span class="num">05</span> A decryption is not yet a reading</h2>
<p>A key that turns the cipher into words does not by itself give a text. Each document in a record carries one of four states:</p>
<ul>
<li><code>read</code>: the decryption builds coherent sentences in its language, has an English translation, and at least 95% of its words give sense. The share is measured from the reading file (<code>read_share</code>), not estimated.</li>
<li><code>read in part</code>: coherent sentences, but fewer than 95% of the words give sense.</li>
<li><code>decoded, not read</code>: the decode does not build sentences. It is shown as such and is not counted as a reading.</li>
<li><code>not prose</code>: a key sheet, a list of codes, figures or names, where sentences are not expected.</li>
</ul>
<p>Gaps are counted in words. A guessed word <code>[?word]</code>, a supplied word <code>[word]</code> and each unread word count against the 95%. In a code deciphered with its surviving period key, a group one digit away from the value the sense needs counts as deciphered only if the slip can be seen on the image and the other groups of the word come from the key; it is marked <code>{{+...}}</code> in the text and listed on the page. Of the {n(c['texts'])} document entries in the records, {n(st['read'])} are in state <code>read</code>, {n(st['read in part'])} <code>read in part</code>, {n(st['decoded, not read'])} <code>decoded, not read</code> and {n(st['not prose'])} <code>not prose</code>.</p>

<h2 id="statistical-checks"><span class="num">06</span> Statistical checks against false positives</h2>
<p>A key with enough free values can be fitted to a ciphertext and produce words even when it is wrong. {gh('docs/_validate.py')} scores a reading with a letter n-gram model of the period and compares it with two baselines: random keys of the same structure, and keys fitted by the same search to the ciphertext once shuffled. It also measures whether the search is strong enough for its failure on shuffled text to mean something. A reading passes when it scores at least 5 standard deviations above the random keys, above every key fitted to shuffled text, and at least 3 standard deviations above their mean. Below 40 deciphered symbols (or 80 letters) the verdict is <code>too short</code>. When the search on the real ciphertext scores higher than the reading, the test cannot decide (<code>underdetermined</code>). It does not apply to transpositions, to non-alphabetic plaintexts or to readings where one symbol takes several values.</p>
<p>Verdicts recorded, on {n(c['verdicts_total'])} records: {verdict_txt}.</p>
<p>Of the {n(c['crypt_read'])} records whose key was recovered here by cryptanalysis and whose text was obtained in full or in part, {n(c['crypt_val'])} carry a verdict and {n(c['crypt_unval'])} do not. The test has not been run on these {n(c['crypt_unval'])}: {unval_txt}.</p>
<p>What the test does not show: it has not been reviewed by an outside statistician; there is no correction for the number of readings tested; it scores letters, so it does not check code values that a model proposed from context; and on short texts and homophonic ciphers it often cannot decide.</p>

<h2 id="review"><span class="num">07</span> Review</h2>
<p>Two different steps are called review here.</p>
<p><b>Merging.</b> A change to a result (a reading, a key, a transcription, a credit, a write-up) enters the repository only with the approval of a maintainer who is not its author, and only when the two required checks pass (&ldquo;Check write-ups&rdquo; and &ldquo;Reading check&rdquo;). The repository enforces this for pull requests ({gh('.github/CODEOWNERS', 'CODEOWNERS')} and the ruleset on <code>main</code>); the owner&rsquo;s direct changes follow it as a convention.</p>
<p><b>Grading the reading.</b> A document in state <code>read</code> needs a grade in a <code>reading_review</code>: a reader has read the decryption as sentences and graded it A (coherent sentences with scattered gaps) or B (coherent but raw, put into normal form in the reading or the translation). The schema allows that reader to be a person or a model named as such. The rule is that the grade is recorded by the reviewer, not by the author of the reading.</p>
<p><b>Most A and B grades are given by a model.</b> Of {n(c['rr'])} graded entries, {n(k['model'])} ({pct(k['model'], c['rr'], L)}) are signed by a model; {n(k['person+model'])} by a person assisted by a model; {n(k['person'])} name a person and no model, {n(c.get('rr_edition', 0))} of them a published edition rather than a reviewer; {n(k['unclear'])} do not say whether a person or a model graded. In {n(c.get('rr_not_independent', 0))} entries the record itself says that the reader was not independent of the work (for example, the same session), so the rule above was not met there. A further {n(c.get('read_no_rr', 0))} entries in state <code>read</code> have no <code>reading_review</code> of their own; where the check applies, it uses the grade of the reading audit of 22 October 2026 (<a href="{REPO}/tree/main/research/reading_audit" rel="noopener"><code>research/reading_audit/</code></a>), which a model reader gave. They are not counted in these figures.</p>
<p><b>The second review of a reading is therefore a model reader together with the automated checks. It is not a human review.</b></p>
<p>Apart from these grades, a person checked a passage against the image without AI help in {n(c['hc'])} records ({hc_txt}). {n(queue)} readings whose key was recovered or matched here are <a href="contributors.html#verify">waiting for an independent check</a>.</p>
<p class="cmuted"><b>How these figures are counted.</b> One graded entry is one item of <code>outcome.texts</code> in a target&rsquo;s <code>profile.json</code> (a document, or a group of documents as the record lists them) that carries a <code>reading_review</code>, whatever its state. Only the <code>targets/&lt;folder&gt;/profile.json</code> files are counted. The signer is classed from the <code>by</code> field: <i>model</i> when it names a model, an agent or an AI session and no person comes first as the reader; <i>person assisted by a model</i> when a person is named first and says a model assisted; <i>person</i> when no model is named; <i>unclear</i> when it names neither (&ldquo;project verification pass&rdquo;). Counting per document, per target or for state <code>read</code> only gives other totals. The rule is in {gh('docs/_method_page.py')}.</p>

<h2 id="ai"><span class="num">08</span> The part played by AI</h2>
<p>The records name the models that did the work (<code>conditions.models</code>) and say what the person did (<code>conditions.human_role</code>): supply images or logins, point to a source, correct a reading. {n(fam['claude'])} records name a Claude model, {n(fam['openai'])} an OpenAI model and {n(fam['other'])} another model or agent (a record can name several); {n(fam['unknown'])} do not name the model.</p>
<p>Scripts, keys and transcriptions are kept under version control, and the README gives the commands that reproduce two results. Steps done by a model, such as transcribing from images or proposing a code value from context, cannot be replayed exactly, and the models are proprietary. The cost of each result (model use, money, human time) is not published.</p>

<h2 id="corrections"><span class="num">09</span> Corrections and challenges</h2>
<p>Any reading can be challenged or checked. On GitHub, the <a href="{REPO}/issues/new?template=verification.yml" rel="noopener">Verification form</a> asks for the passage, the images used, and every place where your reading agrees with the page or differs from it. Without a GitHub account, write by <a href="contribute.html#email">email</a>. Corrections are made on the page and kept in the repository&rsquo;s history; each page gives the date its text last changed. There is not yet a single public list of corrections.</p>

<h2 id="researchers"><span class="num">10</span> For researchers</h2>
<p>Cryptologists, palaeographers, archivists and historians can check a reading from the images (<a href="contributors.html#verify">the list waiting for a check</a>), take a partial reading further (<a href="further.html">Read further</a>) or look at a document in its archive (<a href="archives.html">To the archive</a>). Every contribution is credited. A reviewer is named on the site only with their agreement.</p>

<h2 id="cite"><span class="num">11</span> How to cite</h2>
<p>Each write-up has a &ldquo;Cite this page&rdquo; block with a BibTeX entry. A page can change at the same address, so give the date you consulted it. The site has no DOI or version number yet.</p>
''' + TAIL


def c_sum(counter, exclude):
    return sum(v for k, v in counter.items() if k not in exclude)


# --- French ----------------------------------------------------------------------------------------------------
FR_VERDICT = {'pass': 'réussis', 'weak': 'faibles', 'underdetermined': 'indécidables', 'too short': 'trop courts',
              'fail': 'échecs', 'not applicable': 'non applicables'}
FR_HC = {'confirmed': 'confirmés', 'corrected': 'corrigés', 'disagreed': 'en désaccord'}


def page_fr(c, queue, names):
    L = 'fr'
    n = lambda x: num(x, L)
    k, st, v, tr, pv, hr = c['kinds'], c['states'], c['verdicts'], c['transcr'], c['prov'], c['hc_result']
    fam = c['families']
    verdict_txt = join([f'{n(v[x])} {FR_VERDICT[x]}' for x in ('pass', 'weak', 'underdetermined', 'too short', 'fail', 'not applicable') if v.get(x)], L)
    hc_txt = join([f'{n(hr[x])} {FR_HC[x]}' for x in ('confirmed', 'corrected', 'disagreed') if hr.get(x)], L)
    tr_other = c_sum(tr, exclude=('llm from images', 'mixed', 'DECODE', 'published', 'human (project)'))
    up = c['unval_prov']
    unval_txt = unval_text(c, L, names)
    return head(L, 'Méthode et relecture &mdash; comment une lecture est établie, contrôlée et notée',
                'Comment chaque lecture de Cyphersolver est transcrite, déchiffrée, testée et notée, qui fait chaque étape, '
                'et ce que les contrôles ne couvrent pas. Les chiffres sont comptés dans les fiches à chaque construction du site.') + f'''<section class="hero">
  <p class="kicker">R&eacute;f&eacute;rence &middot; m&eacute;thode &middot; relecture</p>
  <h1>M&eacute;thode et relecture</h1>
  <p class="sub">Comment une lecture de ce site est &eacute;tablie, contr&ocirc;l&eacute;e et not&eacute;e, qui fait chaque &eacute;tape, et ce que les contr&ocirc;les ne couvrent pas. Chaque d&eacute;compte de cette page est calcul&eacute; &agrave; partir des fiches du d&eacute;p&ocirc;t &agrave; chaque construction du site.</p>
  <p class="meta">Daniel Bourdeau</p>
  <p class="langswitch"><a href="method.html" hreflang="en" lang="en">English version</a></p>
</section>

<main>

<h2 id="ce-qu-est-le-projet"><span class="num">01</span> Ce qu&rsquo;est ce projet</h2>
<p>Cyphersolver est un registre ouvert de chiffres historiques travaill&eacute;s avec des mod&egrave;les d&rsquo;IA, et un banc d&rsquo;essai informel de ce que ces mod&egrave;les en font. L&rsquo;essentiel du travail est fait avec les mod&egrave;les Claude d&rsquo;Anthropic, pilot&eacute;s par les mainteneurs du projet ; des contributeurs ext&eacute;rieurs envoient aussi des r&eacute;sultats, parfois obtenus avec d&rsquo;autres mod&egrave;les. Sur {n(c['profiles'])} fiches de cibles, {n(pv['project'])} rel&egrave;vent du travail du projet, {n(pv['contributed'])} sont des contributions ext&eacute;rieures et {n(pv['mixed'])} sont mixtes.</p>
<p>Le registre n&rsquo;est pas une &eacute;dition critique, et ses r&eacute;sultats n&rsquo;ont pas &eacute;t&eacute; &eacute;valu&eacute;s par les pairs au sens acad&eacute;mique. Cette page r&eacute;sume les r&egrave;gles ; le texte complet est dans le d&eacute;p&ocirc;t : les Conventions du {gh('README.md', 'README')}, {gh('CONTRIBUTING.md')} et {gh('profile.schema.json')} (en anglais). Chaque cible a un dossier avec ses notes de travail (<code>NOTES.md</code>) et une fiche &agrave; champs fixes (<code>profile.json</code>).</p>

<h2 id="sources"><span class="num">02</span> Sources et travaux ant&eacute;rieurs</h2>
<p>La r&egrave;gle du projet est que chaque image du site soit cr&eacute;dit&eacute;e &agrave; sa source : d&eacute;tenteur, cote et folio, et chemin d&rsquo;acc&egrave;s (Gallica, une fiche DECODE, la visionneuse d&rsquo;un service d&rsquo;archives, IIIF ou une &eacute;dition imprim&eacute;e). Les images restent soumises aux conditions de leurs d&eacute;tenteurs ; les textes sont publi&eacute;s sous licence CC BY 4.0 et le code sous licence MIT.</p>
<p>Depuis le 28 octobre 2026, un document n&rsquo;entre au <a href="catalogue.html">catalogue</a> des pi&egrave;ces ouvertes que si sa fiche montre que le chiffr&eacute; a &eacute;t&eacute; vu et que les lieux habituels d&rsquo;un d&eacute;chiffrement ant&eacute;rieur ont &eacute;t&eacute; consult&eacute;s : la fiche DECODE, les listes de Satoshi Tomokiyo, l&rsquo;inventaire analytique ou l&rsquo;&eacute;dition imprim&eacute;e, et la litt&eacute;rature.</p>
<p>Les fiches indiquent si une lecture existait avant celle du projet, et quand elle a &eacute;t&eacute; trouv&eacute;e. {n(c['exists_answered'])} fiches sur {n(c['profiles'])} r&eacute;pondent : {n(c['exists_earlier'])} signalent une lecture ant&eacute;rieure, compl&egrave;te ou partielle, dans un fonds d&rsquo;archives, imprim&eacute;e, en ligne ou in&eacute;dite ; pour {n(c['found'].get('after reading', 0))} d&rsquo;entre elles, elle n&rsquo;a &eacute;t&eacute; trouv&eacute;e qu&rsquo;apr&egrave;s la lecture du projet. Selon la r&egrave;gle du projet, un d&eacute;chiffrement ant&eacute;rieur est cr&eacute;dit&eacute; nomm&eacute;ment sur l&rsquo;article et sur la page <a href="contributors.html">Contributors</a>, y compris quand il est trouv&eacute; apr&egrave;s coup. Une solution ant&eacute;rieure jamais publi&eacute;e n&rsquo;est cr&eacute;dit&eacute;e qu&rsquo;avec l&rsquo;accord de son auteur.</p>

<h2 id="transcription"><span class="num">03</span> Transcription</h2>
<p>Recopier le chiffr&eacute; du manuscrit dans un fichier texte est en soi une source d&rsquo;erreur. Les fiches indiquent qui a transcrit chaque document. Sur {n(sum(tr.values()))} documents, {n(tr['llm from images'])} ont &eacute;t&eacute; transcrits par un mod&egrave;le &agrave; partir des images, {n(tr['mixed'])} combinent plusieurs sources, {n(tr['DECODE'])} viennent de DECODE, {n(tr['published'])} d&rsquo;une &eacute;dition imprim&eacute;e, et {n(tr['human (project)'])} ont &eacute;t&eacute; transcrits par une personne travaillant pour le projet ; {n(tr_other)} ont une autre source ou aucune n&rsquo;est indiqu&eacute;e.</p>
<p>Il n&rsquo;y a pas de double transcription &agrave; l&rsquo;aveugle syst&eacute;matique, ni de taux d&rsquo;accord publi&eacute; entre deux transcripteurs. Une transcription est parfois corrig&eacute;e apr&egrave;s que la cl&eacute; a &eacute;t&eacute; trouv&eacute;e ; la lecture peut alors d&eacute;pendre de la cl&eacute; qu&rsquo;elle est cens&eacute;e mettre &agrave; l&rsquo;&eacute;preuve. Les articles ne le signalent pas encore de fa&ccedil;on uniforme. Pour {n(c['timestamped'])} cibles, la cl&eacute; et les transcriptions ont &eacute;t&eacute; fig&eacute;es et horodat&eacute;es (jeton RFC 3161 et preuve OpenTimestamps) avant le calcul des scores, de sorte qu&rsquo;un test ult&eacute;rieur sur une partie r&eacute;serv&eacute;e puisse &ecirc;tre dat&eacute; par rapport &agrave; elles.</p>

<h2 id="cle"><span class="num">04</span> Comment la cl&eacute; est obtenue</h2>
<p>Chaque article indique sa m&eacute;thode dans l&rsquo;une des cat&eacute;gories du <a href="glossary.html">glossaire</a> (en anglais). Trois rel&egrave;vent de la cryptanalyse faite ici : la cl&eacute; a &eacute;t&eacute; reconstitu&eacute;e &agrave; partir du seul chiffr&eacute;, d&rsquo;un texte clair trouv&eacute; ailleurs, ou d&rsquo;un texte clair voisin du chiffr&eacute; (un d&eacute;chiffrement interlin&eacute;aire, un passage en clair). Les autres appliquent une cl&eacute; ou un d&eacute;chiffrement qui existait d&eacute;j&agrave; ; le travail est alors la transcription et le d&eacute;chiffrement. Sur {n(c['profiles'])} fiches, {n(c['m_crypt'])} ont reconstitu&eacute; une cl&eacute; par cryptanalyse, {n(c['m_applied'])} ont appliqu&eacute; une cl&eacute; ou un d&eacute;chiffrement existant, {n(c['m_notsolved'])} n&rsquo;ont obtenu ni cl&eacute; ni texte, et {n(c['m_na'])} ne sont pas des chiffres ou n&rsquo;ont pas pu &ecirc;tre atteintes.</p>
<p>Selon la r&egrave;gle du projet, un r&eacute;sultat n&eacute;gatif n&rsquo;est publi&eacute; qu&rsquo;avec un t&eacute;moin : un texte synth&eacute;tique de m&ecirc;me longueur, de m&ecirc;me alphabet et de m&ecirc;me syst&egrave;me de chiffrement, que le m&ecirc;me solveur parvient &agrave; casser.</p>

<h2 id="dechiffre-n-est-pas-lu"><span class="num">05</span> Un d&eacute;chiffrement n&rsquo;est pas encore une lecture</h2>
<p>Une cl&eacute; qui change le chiffr&eacute; en mots ne donne pas &agrave; elle seule un texte. Chaque document d&rsquo;une fiche porte l&rsquo;un de quatre &eacute;tats (les noms sont ceux des fiches, en anglais) :</p>
<ul>
<li><code>read</code> (lu) : le d&eacute;chiffrement forme des phrases coh&eacute;rentes dans sa langue, a une traduction anglaise, et au moins 95&nbsp;% de ses mots ont un sens. La part est mesur&eacute;e sur le fichier de lecture (<code>read_share</code>), non estim&eacute;e.</li>
<li><code>read in part</code> (lu en partie) : des phrases coh&eacute;rentes, mais moins de 95&nbsp;% des mots ont un sens.</li>
<li><code>decoded, not read</code> (d&eacute;cod&eacute;, non lu) : le d&eacute;codage ne forme pas de phrases. Il est montr&eacute; comme tel et n&rsquo;est pas compt&eacute; comme une lecture.</li>
<li><code>not prose</code> (pas de la prose) : une table de chiffre, une liste de codes, des nombres ou des noms, o&ugrave; l&rsquo;on n&rsquo;attend pas de phrases.</li>
</ul>
<p>Les lacunes se comptent en mots. Un mot conjectur&eacute; <code>[?mot]</code>, un mot restitu&eacute; <code>[mot]</code> et chaque mot non lu comptent contre les 95&nbsp;%. Dans un code d&eacute;chiffr&eacute; avec la cl&eacute; d&rsquo;&eacute;poque conserv&eacute;e, un groupe qui s&rsquo;&eacute;carte d&rsquo;un seul chiffre de la valeur qu&rsquo;exige le sens ne compte comme d&eacute;chiffr&eacute; que si l&rsquo;erreur se voit sur l&rsquo;image et que les autres groupes du mot viennent de la cl&eacute; ; il est marqu&eacute; <code>{{+...}}</code> dans le texte et relev&eacute; sur la page. Sur les {n(c['texts'])} entr&eacute;es de documents des fiches, {n(st['read'])} sont &agrave; l&rsquo;&eacute;tat <code>read</code>, {n(st['read in part'])} <code>read in part</code>, {n(st['decoded, not read'])} <code>decoded, not read</code> et {n(st['not prose'])} <code>not prose</code>.</p>

<h2 id="controles-statistiques"><span class="num">06</span> Contr&ocirc;les statistiques contre les faux positifs</h2>
<p>Une cl&eacute; qui a assez de valeurs libres peut &ecirc;tre ajust&eacute;e &agrave; un chiffr&eacute; et produire des mots m&ecirc;me quand elle est fausse. {gh('docs/_validate.py')} note une lecture avec un mod&egrave;le de n-grammes de lettres de l&rsquo;&eacute;poque et la compare &agrave; deux r&eacute;f&eacute;rences : des cl&eacute;s al&eacute;atoires de m&ecirc;me structure, et des cl&eacute;s ajust&eacute;es par la m&ecirc;me recherche sur le chiffr&eacute; m&eacute;lang&eacute;. Il mesure aussi si la recherche est assez puissante pour que son &eacute;chec sur le texte m&eacute;lang&eacute; ait un sens. Une lecture r&eacute;ussit le test quand son score d&eacute;passe d&rsquo;au moins 5 &eacute;carts-types celui des cl&eacute;s al&eacute;atoires, d&eacute;passe celui de toutes les cl&eacute;s ajust&eacute;es sur le texte m&eacute;lang&eacute;, et d&eacute;passe leur moyenne d&rsquo;au moins 3 &eacute;carts-types. En dessous de 40 symboles d&eacute;chiffr&eacute;s (ou de 80 lettres), le verdict est <code>too short</code> (trop court). Quand la recherche sur le vrai chiffr&eacute; obtient un meilleur score que la lecture, le test ne peut pas trancher (<code>underdetermined</code>, ind&eacute;cidable). Il ne s&rsquo;applique pas aux transpositions, aux textes clairs non alphab&eacute;tiques, ni aux lectures o&ugrave; un m&ecirc;me symbole prend plusieurs valeurs.</p>
<p>Verdicts enregistr&eacute;s, sur {n(c['verdicts_total'])} fiches : {verdict_txt}.</p>
<p>Sur les {n(c['crypt_read'])} fiches dont la cl&eacute; a &eacute;t&eacute; reconstitu&eacute;e ici par cryptanalyse et dont le texte a &eacute;t&eacute; obtenu en entier ou en partie, {n(c['crypt_val'])} portent un verdict et {n(c['crypt_unval'])} n&rsquo;en portent pas. Le test n&rsquo;a pas &eacute;t&eacute; lanc&eacute; sur ces {n(c['crypt_unval'])} fiches : {unval_txt}.</p>
<p>Ce que le test ne montre pas : il n&rsquo;a pas &eacute;t&eacute; examin&eacute; par un statisticien ext&eacute;rieur ; aucune correction ne tient compte du nombre de lectures test&eacute;es ; il note des lettres, et ne v&eacute;rifie donc pas les valeurs de code qu&rsquo;un mod&egrave;le a propos&eacute;es d&rsquo;apr&egrave;s le contexte ; sur les textes courts et les chiffres homophoniques, il ne peut souvent pas trancher.</p>

<h2 id="relecture"><span class="num">07</span> Relecture</h2>
<p>Deux &eacute;tapes diff&eacute;rentes portent ici le nom de relecture.</p>
<p><b>L&rsquo;int&eacute;gration.</b> Une modification d&rsquo;un r&eacute;sultat (une lecture, une cl&eacute;, une transcription, un cr&eacute;dit, un article) n&rsquo;entre dans le d&eacute;p&ocirc;t qu&rsquo;avec l&rsquo;approbation d&rsquo;un mainteneur qui n&rsquo;en est pas l&rsquo;auteur, et seulement si les deux contr&ocirc;les obligatoires passent (&laquo;&nbsp;Check write-ups&nbsp;&raquo; et &laquo;&nbsp;Reading check&nbsp;&raquo;). Le d&eacute;p&ocirc;t l&rsquo;impose pour les demandes de fusion ({gh('.github/CODEOWNERS', 'CODEOWNERS')} et les r&egrave;gles de la branche <code>main</code>) ; les modifications directes du propri&eacute;taire du d&eacute;p&ocirc;t le suivent par convention.</p>
<p><b>La notation de la lecture.</b> Un document &agrave; l&rsquo;&eacute;tat <code>read</code> doit recevoir une note dans un <code>reading_review</code> : un lecteur a lu le d&eacute;chiffrement comme des phrases et lui a donn&eacute; la note A (phrases coh&eacute;rentes, lacunes &eacute;parses) ou B (coh&eacute;rent mais brut, mis en forme dans la lecture ou la traduction). Le sch&eacute;ma admet que ce lecteur soit une personne ou un mod&egrave;le d&eacute;sign&eacute; comme tel. La r&egrave;gle veut que la note soit enregistr&eacute;e par le relecteur, et non par l&rsquo;auteur de la lecture.</p>
<p><b>La plupart des notes A et B sont attribu&eacute;es par un mod&egrave;le.</b> Sur {n(c['rr'])} entr&eacute;es not&eacute;es, {n(k['model'])} ({pct(k['model'], c['rr'], L)}) sont sign&eacute;es par un mod&egrave;le ; {n(k['person+model'])} par une personne assist&eacute;e d&rsquo;un mod&egrave;le ; {n(k['person'])} nomment une personne et aucun mod&egrave;le, dont {n(c.get('rr_edition', 0))} une &eacute;dition publi&eacute;e plut&ocirc;t qu&rsquo;un relecteur ; {n(k['unclear'])} ne disent pas si une personne ou un mod&egrave;le a not&eacute;. Pour {n(c.get('rr_not_independent', 0))} entr&eacute;es, la fiche elle-m&ecirc;me indique que le lecteur n&rsquo;&eacute;tait pas ind&eacute;pendant du travail (par exemple, la m&ecirc;me session) : la r&egrave;gle n&rsquo;y a donc pas &eacute;t&eacute; respect&eacute;e. Par ailleurs, {n(c.get('read_no_rr', 0))} entr&eacute;es &agrave; l&rsquo;&eacute;tat <code>read</code> n&rsquo;ont pas de <code>reading_review</code> propre ; quand le contr&ocirc;le s&rsquo;applique, il reprend la note de l&rsquo;audit des lectures du 22 octobre 2026 (<a href="{REPO}/tree/main/research/reading_audit" rel="noopener"><code>research/reading_audit/</code></a>), attribu&eacute;e par un lecteur-mod&egrave;le. Elles ne sont pas compt&eacute;es dans ces chiffres.</p>
<p><b>La seconde relecture d&rsquo;une lecture est donc un lecteur-mod&egrave;le, associ&eacute; aux contr&ocirc;les automatiques. Ce n&rsquo;est pas une relecture humaine.</b></p>
<p>En dehors de ces notes, une personne a v&eacute;rifi&eacute; un passage sur l&rsquo;image sans aide de l&rsquo;IA pour {n(c['hc'])} fiches ({hc_txt}). {n(queue)} lectures dont la cl&eacute; a &eacute;t&eacute; reconstitu&eacute;e ou rapproch&eacute;e ici <a href="contributors.html#verify">attendent une v&eacute;rification ind&eacute;pendante</a>.</p>
<p class="cmuted"><b>Comment ces chiffres sont compt&eacute;s.</b> Une entr&eacute;e not&eacute;e est un &eacute;l&eacute;ment de <code>outcome.texts</code> dans la fiche <code>profile.json</code> d&rsquo;une cible (un document, ou un groupe de documents tel que la fiche les liste) qui porte un <code>reading_review</code>, quel que soit son &eacute;tat. Seuls les fichiers <code>targets/&lt;dossier&gt;/profile.json</code> sont compt&eacute;s. Le signataire est class&eacute; d&rsquo;apr&egrave;s le champ <code>by</code> : <i>mod&egrave;le</i> s&rsquo;il nomme un mod&egrave;le, un agent ou une session d&rsquo;IA et qu&rsquo;aucune personne n&rsquo;est nomm&eacute;e d&rsquo;abord comme lecteur ; <i>personne assist&eacute;e d&rsquo;un mod&egrave;le</i> si une personne est nomm&eacute;e d&rsquo;abord et indique qu&rsquo;un mod&egrave;le l&rsquo;a assist&eacute;e ; <i>personne</i> si aucun mod&egrave;le n&rsquo;est nomm&eacute; ; <i>ind&eacute;termin&eacute;</i> s&rsquo;il ne nomme ni l&rsquo;un ni l&rsquo;autre (&laquo;&nbsp;project verification pass&nbsp;&raquo;). Compter par document, par cible ou pour le seul &eacute;tat <code>read</code> donne d&rsquo;autres totaux. La r&egrave;gle est dans {gh('docs/_method_page.py')}.</p>

<h2 id="ia"><span class="num">08</span> La part de l&rsquo;IA</h2>
<p>Les fiches nomment les mod&egrave;les qui ont fait le travail (<code>conditions.models</code>) et disent ce qu&rsquo;a fait la personne (<code>conditions.human_role</code>) : fournir des images ou des acc&egrave;s, indiquer une source, corriger une lecture. {n(fam['claude'])} fiches nomment un mod&egrave;le Claude, {n(fam['openai'])} un mod&egrave;le d&rsquo;OpenAI et {n(fam['other'])} un autre mod&egrave;le ou agent (une fiche peut en nommer plusieurs) ; {n(fam['unknown'])} ne nomment pas le mod&egrave;le.</p>
<p>Les scripts, les cl&eacute;s et les transcriptions sont versionn&eacute;s, et le README donne les commandes qui reproduisent deux r&eacute;sultats. Les &eacute;tapes faites par un mod&egrave;le, comme la transcription &agrave; partir des images ou une valeur de code propos&eacute;e d&rsquo;apr&egrave;s le contexte, ne peuvent pas &ecirc;tre rejou&eacute;es &agrave; l&rsquo;identique, et les mod&egrave;les sont propri&eacute;taires. Le co&ucirc;t de chaque r&eacute;sultat (usage des mod&egrave;les, argent, temps humain) n&rsquo;est pas publi&eacute;.</p>

<h2 id="corrections"><span class="num">09</span> Corrections et contestations</h2>
<p>Toute lecture peut &ecirc;tre contest&eacute;e ou v&eacute;rifi&eacute;e. Sur GitHub, le <a href="{REPO}/issues/new?template=verification.yml" rel="noopener">formulaire Verification</a> demande le passage, les images utilis&eacute;es, et chaque point o&ugrave; votre lecture s&rsquo;accorde avec la page ou s&rsquo;en &eacute;carte. Sans compte GitHub, &eacute;crivez par <a href="contribute.html#email">courriel</a>. Les corrections sont faites sur la page et conserv&eacute;es dans l&rsquo;historique du d&eacute;p&ocirc;t ; chaque page donne la date de la derni&egrave;re modification de son texte. Il n&rsquo;existe pas encore de liste publique unique des corrections.</p>

<h2 id="chercheurs"><span class="num">10</span> Pour les chercheurs</h2>
<p>Cryptologues, pal&eacute;ographes, archivistes et historiens peuvent v&eacute;rifier une lecture sur les images (<a href="contributors.html#verify">la liste en attente de v&eacute;rification</a>), prolonger une lecture partielle (<a href="further.html">Read further</a>) ou consulter un document dans son service d&rsquo;archives (<a href="archives.html">To the archive</a>). Toute contribution est cr&eacute;dit&eacute;e. Un relecteur n&rsquo;est nomm&eacute; sur le site qu&rsquo;avec son accord.</p>

<h2 id="citer"><span class="num">11</span> Comment citer</h2>
<p>Chaque article comporte un bloc &laquo;&nbsp;Cite this page&nbsp;&raquo; avec une notice BibTeX. Une page peut changer &agrave; la m&ecirc;me adresse : indiquez la date de consultation. Le site n&rsquo;a pas encore de DOI ni de num&eacute;ro de version.</p>
''' + TAIL


def build_html(pages, profiles):
    """Write method.html and method-fr.html; returns the counts."""
    import _contributors_page as CP
    c = review_counts()
    q = len(CP.queue(pages, profiles))
    names = contributor_names()
    (HERE / 'method.html').write_text(page_en(c, q, names), encoding='utf-8')
    (HERE / 'method-fr.html').write_text(page_fr(c, q, names), encoding='utf-8')
    return c


if __name__ == '__main__':
    c = review_counts()
    for key in sorted(c):
        print(f'{key}: {c[key]}')
