"""Numbers, tables and the data release for the HistoCrypt draft llm-ciphers.tex, computed from every profile.json.

  PYTHONUTF8=1 python papers/lasry/_analysis.py

Writes papers/lasry/generated/{macros,tables,appendix}.tex, so that no figure in the paper is typed by hand, and the
data release papers/lasry/targets.csv + codebook.md (via docs/_export_profiles.py), filtered to the same corpus.

Corpus: the paper covers historical (classical) ciphers of any region dated 1350 to 1950. The famous targets (docs/_check_writeup.py FAMOUS) keep no profile. OUT_OF_SCOPE lists the profiled targets
that fall outside that range; they are left out of every number, table and the data release.

Outcome: outcome.method (George Lasry's categories, docs/_methods.py) says how the text was obtained, and extent
(complete / partial, docs/_methods.extent) says how much of it. The unit of analysis is the target (one profile);
per-document fields are aggregated (lengths summed, earliest year).
"""
import json, pathlib, collections, csv, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'docs'))
import _methods as MT
import _check_profile as cp
import _check_writeup as cw
import _export_profiles as ex

OUT = HERE / 'generated'
OUT.mkdir(exist_ok=True)
U = 'unknown'

# profiled targets outside the paper's corpus (historical ciphers, 1350-1950, any region since 28 Oct 2026)
OUT_OF_SCOPE = {
    'feynman': 'United States, 1953', 'scorpion': 'United States, 1991',
    'kaliningrad': 'modern find, undated', 'copenhagen': 'undated slip, no archival context',
}
YEAR_MIN, YEAR_MAX = 1350, 1950
# targets where the human's role went beyond the project level (conditions.human_role): a source supplied or a route suggested
HUMAN_INPUT = {'bagno1652', 'chaulnes', 'feuquieres', 'rohan1636', 'segura1596'}

CT, EXT_PT, ADJ_PT, EXT_KEY, KNOWN, DECIPH, NOT, NA = MT.METHODS
SHORT = {CT: 'key from ciphertext only', EXT_PT: 'key from external plaintext', ADJ_PT: 'key from adjacent plaintext',
         EXT_KEY: 'external key matched', KNOWN: 'known key applied', DECIPH: 'existing decipherment',
         NOT: 'not solved', NA: 'not applicable'}
ABBR = {CT: 'CT', EXT_PT: 'EPT', ADJ_PT: 'APT', EXT_KEY: 'EK', KNOWN: 'KK', DECIPH: 'DEC', NOT: 'NS', NA: 'NA'}
GROUP = {CT: 'key recovered', EXT_PT: 'key recovered', ADJ_PT: 'key recovered', EXT_KEY: 'key applied',
         KNOWN: 'key applied', DECIPH: 'decipherment existed', NOT: 'not solved', NA: 'not applicable'}
GROUPS = ['key recovered', 'key applied', 'decipherment existed', 'not solved']
WORKED = [CT, EXT_PT, ADJ_PT, EXT_KEY, KNOWN, DECIPH, NOT]          # every method but not applicable


LANGS = ['French', 'English', 'Italian', 'Spanish', 'German', 'Latin', 'Dutch', 'Hungarian', 'Polish', 'Portuguese',
         'Swedish', 'Danish', 'Catalan', 'Castilian', 'Czech', 'Russian', 'Japanese', 'Chinese', 'Arabic', 'Persian', 'Hebrew', 'Korean', 'Greek', 'Occitan', 'Scots', 'Norwegian', 'Turkish']


def norm_langs(raw):
    """Canonical language names found in a free-text language field ('French (with Polish names)' -> {'French', 'Polish'})."""
    out = set()
    for r in raw:
        hits = {l for l in LANGS if l.lower() in str(r).lower()}
        if 'Castilian' in hits: hits = (hits - {'Castilian'}) | ({'Spanish'} if 'Catalan' not in hits or 'Latin' not in hits else set())
        out |= hits or {str(r).split()[0].strip(',;()').capitalize()}
    return out - {'None', 'Unknown', 'Undetermined', 'N/a'}


REGIONS = [('North America', ('United States', 'Confederate', 'Canada')),
           ('Latin America', ('Mexico', 'Argentina', 'Peru', 'Colombia', 'Martinique', 'Brazil', 'Cuba', 'Chile')),
           ('East Asia', ('Japan', 'China', 'Korea')),
           ('Middle East and South Asia', ('Turkey', 'Ottoman', 'Persia', 'Egypt', 'India', 'Baghdad')),
           ('Oceania', ('New Zealand', 'Australia'))]
EUROPE = 'Europe'


def regions_of(country):
    """Regions named in a free-text country field ('United States (cipher); Japan (copies)' -> two); Europe by default."""
    hit = [r for r, keys in REGIONS if any(k in str(country) for k in keys)]
    return hit or [EUROPE]


def as_list(v): return v if isinstance(v, list) else []
def as_dict(v): return v if isinstance(v, dict) else {}


def load():
    ps, skipped = [], []
    for folder, p in sorted(MT.profile_paths().items()):
        if folder in cw.FAMOUS or folder in OUT_OF_SCOPE: continue
        d = MT.load(p)
        if d is None: skipped.append(folder); continue
        docs = [x for x in d['documents'] if isinstance(x, dict)]
        years = [x.get('year') for x in docs if isinstance(x.get('year'), int)]
        if years and not (YEAR_MIN <= min(years) <= YEAR_MAX): skipped.append(folder); continue
        if cp.check(p.parent.relative_to(ROOT / 'targets').as_posix() if (ROOT / 'targets') in p.parents else p.parent.relative_to(ROOT).as_posix(), quiet=True)[0] != 'valid': skipped.append(folder); continue
        toks = [as_dict(x.get('length')).get('tokens') for x in docs]
        known = [t for t in toks if isinstance(t, int)]
        s, c, o = d['system'], d['conditions'], d['outcome']
        ps.append(dict(
            target=folder, title=d.get('title', ''), prof=d, method=o.get('method'), cls=o.get('class'),
            ext=MT.extent(d), year=min(years) if years else None,
            tokens=sum(known) if known else None, tokens_complete=bool(known) and len(known) == len(toks),
            measured=all(as_dict(x.get('length')).get('measured') is True for x in docs) and bool(known),
            types=set(as_list(s.get('types'))), key_order=s.get('key_order', U), kind=s.get('symbol_kind', U),
            nomen=as_dict(s.get('nomenclator')).get('present'),
            attack=c.get('attack', U), inputs=set(as_list(c.get('inputs'))),
            prior=as_dict(c.get('prior_solution')).get('exists', U), found=as_dict(c.get('prior_solution')).get('found', U),
            prior_used=as_dict(c.get('prior_solution')).get('used'),
            langs=norm_langs(x.get('language') for x in docs if x.get('language') not in (None, U)),
            ctry={x.get('country') for x in docs if x.get('country') not in (None, U)},
            trby=[as_dict(x.get('transcription')).get('by', U) for x in docs],
            models=[str(x) for x in as_list(c.get('models'))],
            first=str(c.get('first_date') or ''), last=str(c.get('last_date') or ''),
            steps=[x for x in as_list(d['solution']) if isinstance(x, dict)],
            frac=o.get('fraction_read') if isinstance(o.get('fraction_read'), (int, float)) and not isinstance(o.get('fraction_read'), bool) else None,
            frac_method=o.get('fraction_read_method'),
            verification=set(as_list(o.get('verification'))), contribution=set(as_list(o.get('contribution'))),
            region=collections.Counter(r for x in docs if x.get('country') not in (None, U) for r in regions_of(x['country'])).most_common(1)[0][0]
                   if any(x.get('country') not in (None, U) for x in docs) else U,
            ndocs=len(docs), prov=o.get('provenance') or 'project',
            credits=[x for x in as_list(o.get('credits')) if isinstance(x, dict)]))
    return ps, skipped


def family(t):
    ty = t['types']
    if 'not a cipher' in ty: return 'not a cipher'
    if ty & {'polygraphic', 'transposition', 'polyalphabetic', 'superencipherment'}: return 'transposition, polygraphic, polyalphabetic'
    if 'code' in ty: return 'code or codebook'
    if 'syllabic' in ty: return 'syllabic nomenclator'
    if 'nomenclator' in ty: return 'homophonic or simple + nomenclator'
    if ty & {'homophonic', 'polyphonic', 'monoalphabetic'}: return 'substitution, no nomenclator'
    return 'undetermined'


def century(y):
    if y is None: return 'undated'
    return f'{(y // 100) + 1}th'


def lenband(n):
    if n is None: return 'unknown'
    return '$<$ 250' if n < 250 else '250--999' if n < 1000 else '1,000--4,999' if n < 5000 else '$\\geq$ 5,000'


def attack_group(t):
    a = t['attack']
    if a == 'ciphertext-only': return 'ciphertext only'
    if a == 'crib': return 'crib from clear text'
    if a in ('known plaintext', 'archive decipherment'): return 'decipherment or known plaintext'
    if a in ('published key', 'key from archive', 'sibling key'): return 'a key (archive, print, sibling)'
    return 'none recorded'


def prior_group(t):
    p, f = t['prior'], t['found']
    if p == 'no': return 'none known'
    if p == U: return 'unknown'
    if f == 'before attempt': return 'existed, known before the attempt'
    if f in ('during attempt',): return 'existed, found during the attempt'
    if f in ('after reading', 'not found'): return 'existed, found after or not at all'
    return 'existed, when found unknown'


def model_family(t):
    ms = ' '.join(t['models']).lower()
    fam = []
    if 'claude' in ms: fam.append('Claude')
    if 'gpt' in ms: fam.append('GPT')
    return ' + '.join(fam) if fam else 'not recorded'


def tex(s): return str(s).replace('\\', '/').replace('&', '\\&').replace('%', '\\%').replace('_', '\\_').replace('#', '\\#').replace('$', '\\$')


def mark(t): return tex(t['target']) + ('$^\\dagger$' if t.get('external') else '')


def pct(a, b): return f'{100 * a / b:.0f}' if b else '0'


# The paper reports the project's own work. Set True to add the contributed targets (provenance 'contributed') as a
# lower block in each group table, a section, a table and an appendix list; the paper's text would need them back too.
INCLUDE_CONTRIBUTED = False
CONTRIBUTED = []          # set in main(): the contributed targets, shown under the project targets in each group table


def group_table(ps, keyf, label, caption, tag, order=None):
    """Rows = keyf values; columns = the four method groups (not applicable left out). Upper block: the project's
    targets; lower block: the contributed targets (same rows, same columns)."""
    def tally(ts):
        rows = collections.OrderedDict()
        for t in ts:
            if t['method'] == NA: continue
            rows.setdefault(keyf(t), collections.Counter())[GROUP[t['method']]] += 1
        return rows
    rp, rc = tally(ps), tally(CONTRIBUTED)
    seen = list(dict.fromkeys(list(rp) + list(rc)))
    keys = [k for k in (order or sorted(seen, key=lambda k: -(sum(rp.get(k, {}).values()) + sum(rc.get(k, {}).values())))) if k in seen]
    out = [r'\begin{table}[t]', r'\centering\small', r'\resizebox{\columnwidth}{!}{%', r'\begin{tabular}{@{}lrrrrr@{}}', r'\toprule',
           label + r' & $n$ & recovered & applied & existed & not solved \\']
    two = bool(CONTRIBUTED)
    for title, rows in ((('project targets', rp), ('contributed targets', rc)) if two else (('', rp),)):
        out.append(r'\midrule')
        if two: out.append(r'\multicolumn{6}{@{}l}{\emph{' + title + r'}} \\')
        tot = collections.Counter()
        for k in keys:
            r = rows.get(k, collections.Counter()); tot.update(r)
            if not sum(r.values()): continue
            out.append((r'\quad ' if two else '') + (tex(k) if '$' not in str(k) else k) + f' & {sum(r.values())} & ' + ' & '.join(str(r[g]) for g in GROUPS) + r' \\')
        out.append(r'\midrule' if not two else '')
        out.append((r'\quad\emph{all} & ' if two else r'all & ') + str(sum(tot.values())) + ' & ' + ' & '.join(str(tot[g]) for g in GROUPS) + r' \\')
    cols = ('Columns: key recovered (from ciphertext only, adjacent or external plaintext); key applied (a known '
            'key, or an external key matched to the document); a decipherment already existed; not solved. Targets '
            'classed not applicable are left out.}') if tag == 'attack' else 'Columns as in Table~\\ref{tab:attack}.}'
    out += [r'\bottomrule', r'\end{tabular}}',
            r'\caption{\label{tab:' + tag + '} ' + caption + (r" Upper block: the project's targets; lower block: the contributed targets of Section~\ref{sec:contrib}. " if two else ' ') + cols,
            r'\end{table}', '']
    return '\n'.join(out)


SOLVER_ROLES = ('solution', 'new cipher with solution')


def solvers(t):
    """Contributor ids credited with the solution of a target."""
    return [c['who'] for c in t['credits'] if c.get('role') in SOLVER_ROLES]


def main():
    everyone, skipped = load()
    # contributed results are the contributors' own (contribute.html: "kept out of the model's figures"); they are
    # reported in their own section, table and appendix. Mixed targets (the model and an outside solver) stay in the
    # model figures and carry a dagger.
    cs = [t for t in everyone if t['prov'] == 'contributed']
    if INCLUDE_CONTRIBUTED: CONTRIBUTED.extend(cs)
    ps = [t for t in everyone if t['prov'] != 'contributed']
    M = {}
    def m(name, v): M[name] = v
    by = collections.Counter(t['method'] for t in ps)
    worked = [t for t in ps if t['method'] != NA]
    rec = [t for t in ps if t['method'] in MT.KEY_RECOVERED]
    app = [t for t in ps if t['method'] in (EXT_KEY, KNOWN)]
    dec = [t for t in ps if t['method'] == DECIPH]
    obtained = [t for t in worked if t['method'] != NOT]
    m('Ntargets', len(ps)); m('Ndocs', sum(t['ndocs'] for t in ps)); m('Nworked', len(worked))
    m('Nobtained', len(obtained)); m('PctObtained', pct(len(obtained), len(worked)))
    m('Ncomplete', sum(1 for t in obtained if t['ext'] == 'complete')); m('Npartial', sum(1 for t in obtained if t['ext'] == 'partial'))
    for meth in MT.METHODS:
        k = ABBR[meth]
        m('N' + k, by[meth])
        m('N' + k + 'complete', sum(1 for t in ps if t['method'] == meth and t['ext'] == 'complete'))
        m('N' + k + 'partial', sum(1 for t in ps if t['method'] == meth and t['ext'] == 'partial'))
    m('Nrecovered', len(rec)); m('Napplied', len(app)); m('Ndeciph', len(dec))
    m('Nrecoveredcomplete', sum(1 for t in rec if t['ext'] == 'complete'))
    m('NnotCipher', sum(1 for t in ps if t['method'] == NA and t['cls'] == 'not a cipher'))
    m('NoffLine', sum(1 for t in ps if t['method'] == NA and t['cls'] == 'offline only'))
    m('NnaOther', by[NA] - M['NnotCipher'] - M['NoffLine'])
    m('NnotSolvedByOthers', sum(1 for t in ps if t['method'] == NOT and t['cls'] == 'already solved'))
    yrs = [t['year'] for t in ps if t['year']]
    m('YearMin', min(yrs)); m('YearMax', max(yrs)); m('Nundated', sum(1 for t in ps if not t['year']))
    toks = [t['tokens'] for t in ps if t['tokens']]
    m('TokensTotal', f'{sum(toks):,}'); m('Nlengthknown', len(toks)); m('Nmeasured', sum(1 for t in ps if t['measured']))
    langs = collections.Counter(l for t in ps for l in t['langs'])
    m('Nlanguages', len(langs))
    cen = collections.Counter(century(t['year']) for t in ps)
    m('NsixteenthC', cen['16th']); m('NseventeenthC', cen['17th']); m('NfifteenthC', cen['15th'])
    m('NfourteenthC', cen['14th']); m('NeighteenthC', cen['18th']); m('NnineteenthC', cen['19th']); m('NtwentiethC', cen['20th'])
    m('NmodernC', cen['19th'] + cen['20th'])

    # regions (the first country field of each document; Europe unless a non-European country is named)
    rg = collections.Counter(t['region'] for t in ps)
    m('Nregions', len([r for r in rg if r not in (EUROPE, U)]) + 1)
    m('NEurope', rg[EUROPE]); m('NnonEurope', len(ps) - rg[EUROPE] - rg[U]); m('NregionUnknown', rg[U])
    m('NnonEuropeObtained', sum(1 for t in obtained if t['region'] not in (EUROPE, U)))
    m('NnonEuropeCT', sum(1 for t in ps if t['region'] not in (EUROPE, U) and t['method'] == CT))
    for key, r in (('NA', 'North America'), ('LA', 'Latin America'), ('EA', 'East Asia'), ('ME', 'Middle East and South Asia'), ('OC', 'Oceania')):
        m('NR' + key, rg[r])
    crg = collections.Counter(t['region'] for t in cs)
    m('NcontribnonEurope', len(cs) - crg[EUROPE] - crg[U]); m('NcontribEurope', crg[EUROPE])
    m('NcontribnonEuropeObtained', sum(1 for t in cs if t['region'] not in (EUROPE, U) and t['method'] not in (NA, NOT)))

    # starting point
    cto = [t for t in worked if t['attack'] == 'ciphertext-only']
    m('Ncto', len(cto)); m('NctoCT', sum(1 for t in cto if t['method'] == CT))
    m('NctoOther', sum(1 for t in cto if t['method'] not in (CT, NOT))); m('NctoDEC', sum(1 for t in cto if t['method'] == DECIPH))
    m('NCTnotcto', sum(1 for t in ps if t['method'] == CT and t['attack'] != 'ciphertext-only')); m('NctoNot', sum(1 for t in cto if t['method'] == NOT))
    m('NctoPct', pct(M['NctoCT'], len(cto)))
    crib = [t for t in worked if t['attack'] == 'crib']
    m('Ncrib', len(crib)); m('Ncribobtained', sum(1 for t in crib if t['method'] != NOT))
    keyed = [t for t in worked if attack_group(t) == 'a key (archive, print, sibling)']
    m('Nkeyed', len(keyed)); m('Nkeyedobtained', sum(1 for t in keyed if t['method'] != NOT)); m('Nkeyedpct', pct(M['Nkeyedobtained'], len(keyed)))
    decs = [t for t in worked if attack_group(t) == 'decipherment or known plaintext']
    m('Ndecstart', len(decs)); m('Ndecstartobtained', sum(1 for t in decs if t['method'] != NOT))

    # contamination
    clean = [t for t in worked if t['prior'] == 'no']
    m('Nclean', len(clean)); m('Ncleanobtained', sum(1 for t in clean if t['method'] != NOT))
    m('Ncleanrecovered', sum(1 for t in clean if t['method'] in MT.KEY_RECOVERED))
    m('NcleanCT', sum(1 for t in clean if t['method'] == CT))
    m('NcleanApplied', sum(1 for t in clean if t['method'] in (EXT_KEY, KNOWN)))
    m('Ncleancomplete', sum(1 for t in clean if t['method'] != NOT and t['ext'] == 'complete'))
    ctprior = [t for t in ps if t['method'] == CT and t['prior'] != 'no']
    m('NCTprior', len(ctprior)); m('NCTclean', by[CT] - len(ctprior))
    m('NCTpriorbefore', sum(1 for t in ctprior if t['found'] == 'before attempt'))
    m('NpriorFoundDuring', sum(1 for t in worked if t['prior'] not in ('no', U) and t['found'] == 'during attempt'))
    m('NpriorFoundBefore', sum(1 for t in worked if t['prior'] not in ('no', U) and t['found'] == 'before attempt'))
    m('Nprintprior', sum(1 for t in ps if t['prior'] == 'in print'))

    # key order within key recoveries
    ko = collections.Counter(t['key_order'] for t in rec)
    m('Nrecalpha', ko['alphabetical'] + ko['partly alphabetical']); m('Nrecrandom', ko['random'] + ko['keyword-derived'])
    ko_ct = collections.Counter(t['key_order'] for t in ps if t['method'] == CT)
    m('NCTalpha', ko_ct['alphabetical'] + ko_ct['partly alphabetical']); m('NCTrandom', ko_ct['random'] + ko_ct['keyword-derived'])
    m('Nkeyorderunknown', sum(1 for t in ps if t['key_order'] == U))

    # steps, controls, verification
    steps = [s for t in ps for s in t['steps']]
    nfail = sum(1 for s in steps if s.get('result') in ('failed', 'ruled out'))
    m('Nsteps', f'{len(steps):,}'); m('Nfailedsteps', nfail)
    m('PctFailedSteps', pct(nfail, len(steps)))
    kinds = collections.Counter(s.get('kind') for s in steps)
    m('Nsolversteps', kinds['solver']); m('Nlitsteps', kinds['literature search']); m('Ntranssteps', kinds['transcription'])
    m('Nsolverfailed', sum(1 for s in steps if s.get('kind') == 'solver' and s.get('result') in ('failed', 'ruled out')))
    m('Ncontrol', sum(1 for t in ps if any(s.get('kind') == 'control' for s in t['steps'])))
    m('NnotControl', sum(1 for t in ps if t['method'] == NOT and 'matched control' in t['verification']))
    m('NCTcontrol', sum(1 for t in ps if t['method'] == CT and 'matched control' in t['verification']))
    m('NCTverified', sum(1 for t in ps if t['method'] == CT and t['verification'] - {'none', U}))
    m('NCTsolverstep', sum(1 for t in ps if t['method'] == CT and any(s.get('kind') == 'solver' and s.get('result') in ('worked', 'partial') for s in t['steps'])))

    # transcription
    alldocs = [b for t in ps for b in t['trby']]
    m('Ndocsllm', sum(1 for b in alldocs if b == 'llm from images')); m('Ndocsdecode', sum(1 for b in alldocs if b == 'DECODE'))
    m('Ndocspublished', sum(1 for b in alldocs if b == 'published'))
    m('PctDocsllm', pct(M['Ndocsllm'], len(alldocs)))
    img = [t for t in worked if t['trby'] and all(b == 'llm from images' for b in t['trby'])]
    m('Nimg', len(img)); m('Nimgobtained', sum(1 for t in img if t['method'] != NOT))

    # contributions of the targets whose text already existed
    m('Ndeciphtranscribed', sum(1 for t in dec if 'transcription' in t['contribution']))
    m('Ncatcorr', sum(1 for t in ps if 'catalogue correction' in t['contribution']))
    m('Nsenderid', sum(1 for t in ps if 'sender or date identified' in t['contribution']))
    m('Nkeyextended', sum(1 for t in ps if 'key extended or corrected' in t['contribution']))
    m('Nambiguous', sum(1 for t in ps if 'decipherment with ambiguous key' in t['contribution']))

    # read bar sensitivity: targets with a numeric share of tokens read
    fr = [t for t in obtained if t['frac'] is not None]
    def f01(t): return t['frac'] / 100 if t['frac'] > 1 else t['frac']
    m('Nfrac', len(fr)); m('Nfracmeasured', sum(1 for t in fr if t['frac_method'] == 'measured'))
    m('Nbarup', sum(1 for t in fr if t['ext'] == 'complete' and f01(t) < 0.98))
    m('Nbardown', sum(1 for t in fr if t['ext'] == 'partial' and 0.90 <= f01(t) < 0.95))
    m('Npartialhigh', sum(1 for t in fr if t['ext'] == 'partial' and f01(t) >= 0.95))

    # models and dates
    mf = collections.Counter(model_family(t) for t in ps)
    m('Nclaude', mf['Claude'] + mf['Claude + GPT']); m('Ngpt', mf['GPT'] + mf['Claude + GPT']); m('Nboth', mf['Claude + GPT'])
    m('Nmodelunknown', mf['not recorded'])
    firsts = sorted(t['first'][:10] for t in ps if t['first'][:4] == '2026')
    lasts = sorted(t['last'][:10] for t in ps if t['last'][:4] == '2026')
    import datetime
    def dstr(s): d = datetime.date.fromisoformat(s); return f'{d.day} {d.strftime("%B")} {d.year}'
    m('DateFirst', dstr(firsts[0])); m('DateLast', dstr(max(lasts + firsts)))
    m('Nhumaninput', sum(1 for t in ps if t['target'] in HUMAN_INPUT))

    # the method review (classification_review.csv: rule-based proposal from the older fields, final method by review agents)
    rev = HERE / 'classification_review.csv'
    agree = tot = flagged = flagged_agree = 0
    if rev.exists():
        final = {t['target']: t['method'] for t in ps}
        for r in csv.DictReader(rev.open(encoding='utf-8')):
            f = r['folder'].lower()
            if f not in final: continue
            tot += 1; a = r['proposed'] == final[f]; agree += a
            if r['flags']: flagged += 1; flagged_agree += a
    m('Nreview', tot); m('Nreviewagree', agree); m('PctReviewagree', pct(agree, tot)); m('Nreviewflagged', flagged)
    m('Nreviewchanged', tot - agree); m('Nflaggedchanged', flagged - flagged_agree)

    # the working record: the repository's commit history and the target folders
    import subprocess
    def git(*a): return subprocess.run(['git', '-C', str(ROOT), *a], capture_output=True, text=True, encoding='utf-8').stdout
    span = ('--since=2026-09-14', '--until=' + (datetime.date.fromisoformat(max(lasts + firsts)) + datetime.timedelta(days=1)).isoformat())
    m('Ndays', (datetime.date.fromisoformat(max(lasts + firsts)) - datetime.date.fromisoformat(firsts[0])).days + 1)
    m('Ncommits', f'{len(git("log", *span, "--format=%H", "HEAD").split()):,}')
    m('Ncommitsmodel', f'{len(git("log", *span, "-i", "--grep=Co-Authored-By: Claude", "--format=%H", "HEAD").split()):,}')
    other = [t for t in ps if t['prov'] == 'mixed']
    m('Nexternal', len(other)); m('Nexternalworked', sum(1 for t in other if t['method'] != NA))
    m('Nexternalobtained', sum(1 for t in other if t['method'] not in (NA, NOT)))
    for t in ps: t['external'] = t['prov'] == 'mixed'
    folders = [MT.profile_paths()[t['target']].parent for t in ps]
    m('Nnotes', sum(1 for f in folders if (f / 'NOTES.md').exists()))
    m('Ncode', sum(1 for f in folders if any(f.rglob('*.py')) or any(f.rglob('*.cs'))))


    # ---- contributed solutions: the contributors' own results, reported apart from the model figures
    import re
    reg = json.loads((ROOT / 'contributors.json').read_text(encoding='utf-8'))['contributors']
    name = {c['id']: c['name'] for c in reg}
    cworked = [t for t in cs if t['method'] != NA]
    cobt = [t for t in cworked if t['method'] != NOT]
    m('Ncontrib', len(cs)); m('Ncontribworked', len(cworked)); m('Ncontribobtained', len(cobt))
    m('Ncontribcomplete', sum(1 for t in cobt if t['ext'] == 'complete')); m('Ncontribpartial', sum(1 for t in cobt if t['ext'] == 'partial'))
    cby = collections.Counter(t['method'] for t in cs)
    for meth in MT.METHODS:
        k = ABBR[meth]
        m('Nc' + k, cby[meth])
        m('Nc' + k + 'complete', sum(1 for t in cs if t['method'] == meth and t['ext'] == 'complete'))
        m('Nc' + k + 'partial', sum(1 for t in cs if t['method'] == meth and t['ext'] == 'partial'))
    m('Ncontribrecovered', sum(1 for t in cs if t['method'] in MT.KEY_RECOVERED))
    who = collections.defaultdict(list)
    for t in cs + [t for t in ps if t['prov'] == 'mixed']:
        for w in dict.fromkeys(solvers(t)): who[w].append(t)
    people = sorted(who, key=lambda w: -len(who[w]))
    m('NcontribTop', len(who[people[0]])); m('Ncontributors', len(people)); m('Nmixed', sum(1 for t in ps if t['prov'] == 'mixed'))
    m('Nallworked', len([t for t in everyone if t['method'] != NA]))
    m('Nalltargets', len(everyone))
    cyears = [t['year'] for t in cs if t['year']]
    ccto = [t for t in cworked if t['attack'] == 'ciphertext-only']
    m('Nccto', len(ccto)); m('NcctoCT', sum(1 for t in ccto if t['method'] == CT))
    cclean = [t for t in cworked if t['prior'] == 'no']
    m('Ncclean', len(cclean)); m('Nccleanobtained', sum(1 for t in cclean if t['method'] != NOT))
    m('NccleanCT', sum(1 for t in cclean if t['method'] == CT))
    cko = collections.Counter(t['key_order'] for t in cs if t['method'] == CT)
    m('NcCTalpha', cko['alphabetical'] + cko['partly alphabetical']); m('NcCTrandom', cko['random'] + cko['keyword-derived'])
    m('NcCTunknownorder', sum(1 for t in cs if t['method'] == CT) - M['NcCTalpha'] - M['NcCTrandom'])
    m('NcCTprior', sum(1 for t in cs if t['method'] == CT and t['prior'] != 'no'))
    m('Ncsteps', sum(len(t['steps']) for t in cs)); m('Ncdocs', sum(t['ndocs'] for t in cs))
    m('NcontribYearMin', min(cyears)); m('NcontribYearMax', max(cyears))
    cl = collections.Counter(l for t in cs for l in t['langs'])
    m('NcontribLanguages', len(cl))
    m('NcontribCountries', len({c for t in cs for c in t['ctry']}))
    cfirst = sorted(t['first'][:10] for t in cs if t['first'][:4] == '2026')
    m('ContribDateFirst', dstr(cfirst[0]) if cfirst else '?')

    # per-contributor table (names in the camera-ready version only; the submission shows C1, C2 ...)
    EOL = ' \\\\'
    cr = [r'\begin{table}[t]', r'\centering\small', r'\resizebox{\columnwidth}{!}{%', r'\begin{tabular}{@{}lrrrrrrrr@{}}', r'\toprule',
          r'contributor & $n$ & CT & APT & EPT & EK & KK & DEC & NS' + EOL, r'\midrule']
    for i, w in enumerate(people, 1):
        ts = who[w]; c = collections.Counter(t['method'] for t in ts)
        cr.append('\\Who{C%d}{%s} & %d & ' % (i, tex(name.get(w, w)), len(ts)) + ' & '.join(str(c[x]) for x in (CT, ADJ_PT, EXT_PT, EXT_KEY, KNOWN, DECIPH, NOT)) + EOL)
    cr += [r'\bottomrule', r'\end{tabular}}',
           r'\caption{\label{tab:contributors} Targets by the contributor credited with the solution, for the contributed targets and the mixed ones of Table~\ref{tab:methods}. A target with two solvers counts under each. Method abbreviations as in Table~\ref{tab:all}.}',
           r'\end{table}', '']
    (OUT / 'contributors_table.tex').write_text('\n'.join(cr), encoding='utf-8')
    cred = ', '.join('%s (%d)' % (tex(name.get(w, w)), len(who[w])) for w in people)
    (OUT / 'contributors.tex').write_text('\\newcommand{\\ContribCredits}{' + cred + '}\n', encoding='utf-8')

    # contributed table, to be appended to the tables below
    crow = [r'\begin{table}[t]', r'\centering\small', r'\begin{tabular}{@{}lrrr@{}}', r'\toprule',
            r'outcome method & $n$ & complete & partial' + EOL, r'\midrule']
    for meth in MT.METHODS:
        if meth in (NA, NOT): crow.append(r'\midrule')
        if meth in (NA, NOT):
            crow.append('%s & %d & -- & --' % (SHORT[meth], cby[meth]) + EOL)
        else:
            crow.append('%s & %d & %d & %d' % (SHORT[meth], cby[meth], M['Nc' + ABBR[meth] + 'complete'], M['Nc' + ABBR[meth] + 'partial']) + EOL)
    crow += [r'\midrule', 'all contributed targets & %d & %d & %d' % (len(cs), M['Ncontribcomplete'], M['Ncontribpartial']) + EOL, r'\bottomrule', r'\end{tabular}',
             r'\caption{\label{tab:contrib} Outcome method and extent for the %d contributed targets: those whose solution is credited to someone outside the project. The model figures of Table~\ref{tab:methods} leave them out.}' % len(cs),
             r'\end{table}', '']
    CONTRIB_TABLE = '\n'.join(crow)

    # appendix rows for the contributed targets
    ident = {w: 'C%d' % i for i, w in enumerate(people, 1)}
    cA = [r'{\scriptsize', r'\begin{longtable}{@{}llrlllr@{}}',
          r'\caption{\label{tab:allcontrib} The contributed targets, by date of the earliest document, with the credited solver (Table~\ref{tab:contributors}). Methods as in Table~\ref{tab:all}.}\\',
          r'\toprule', r'target & solver & year & language & method & extent & tokens' + EOL, r'\midrule', r'\endfirsthead',
          r'\toprule', r'target & solver & year & language & method & extent & tokens' + EOL, r'\midrule', r'\endhead', r'\bottomrule', r'\endlastfoot']
    for t in sorted(cs, key=lambda t: (t['year'] or 9999, t['target'])):
        sv = ', '.join('\\Who{%s}{%s}' % (ident.get(w, 'C?'), tex(name.get(w, w))) for w in dict.fromkeys(solvers(t))) or '--'
        cA.append('%s & %s & %s & %s & %s & %s & %s' % (tex(t['target']), sv, t['year'] or '--', tex(', '.join(sorted(t['langs'])) or '--'),
                                                     ABBR[t['method']], t['ext'], t['tokens'] if t['tokens'] else '--') + EOL)
    cA += [r'\end{longtable}}', '']
    CONTRIB_APPENDIX = '\n'.join(cA)

    # ---- macros
    names = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    lines = ['% generated by papers/lasry/_analysis.py; do not edit']
    for k, v in M.items():
        safe = ''.join(names.get(ch, ch) for ch in k)
        lines.append(f'\\newcommand{{\\{safe}}}{{{str(v).replace(",", "{,}")}}}')
    lines.append('\\newcommand{\\ContribTargets}{' + '; '.join(
        f'{tex(t["target"])} ({SHORT[t["method"]]}' + (f', {t["ext"]})' if t['ext'] in ('complete', 'partial') else ')')
        for t in sorted(other, key=lambda t: t['target'])) + '}')
    lines.append('\\newcommand{\\TopLanguages}{' + ', '.join(f'{tex(k)} {v}' for k, v in langs.most_common(6)) + '}')
    (OUT / 'macros.tex').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    # ---- tables
    T = []
    # Table 1: method x extent
    rows = ['\\begin{table}[t]', '\\centering\\small', '\\begin{tabular}{@{}lrrr@{}}', '\\toprule',
            'outcome method & $n$ & complete & partial \\\\', '\\midrule']
    for meth in MT.METHODS:
        if meth == NA:
            rows.append('\\midrule')
            rows.append(f'{SHORT[meth]} & {by[meth]} & -- & -- \\\\')
        elif meth == NOT:
            rows.append('\\midrule')
            rows.append(f'{SHORT[meth]} & {by[meth]} & -- & -- \\\\')
        else:
            rows.append(f'{SHORT[meth]} & {by[meth]} & {M["N" + ABBR[meth] + "complete"]} & {M["N" + ABBR[meth] + "partial"]} \\\\')
        if meth == ADJ_PT:
            rows.append(f'\\quad\\emph{{key recovered, all routes}} & \\emph{{{len(rec)}}} & \\emph{{{M["Nrecoveredcomplete"]}}} & \\emph{{{len(rec) - M["Nrecoveredcomplete"]}}} \\\\')
    rows += ['\\midrule', f'all targets & {len(ps)} & {M["Ncomplete"]} & {M["Npartial"]} \\\\', '\\bottomrule', '\\end{tabular}',
             f'\\caption{{\\label{{tab:methods}} Outcome method and extent for the {len(ps)} targets. The first three methods '
             'recover the key here; the next two apply a key that already existed; the sixth transcribes and checks a '
             'decipherment that already existed. Complete means the read bar of Section~\\ref{sec:schema} is met.}', '\\end{table}', '']
    T.append('\n'.join(rows))
    # Table 2: corpus by century and language
    cen_order = ['14th', '15th', '16th', '17th', '18th', '19th', '20th', 'undated']
    lang_rows = langs.most_common(8)
    cen_rows = [(c + (' c.' if c != 'undated' else ''), cen[c]) for c in cen_order if cen[c]]
    n = max(len(lang_rows), len(cen_rows))
    lang_rows += [('', '')] * (n - len(lang_rows)); cen_rows += [('', '')] * (n - len(cen_rows))
    T.append('\n'.join(['\\begin{table}[t]', '\\centering\\small', '\\begin{tabular}{@{}lr@{\\qquad}lr@{}}', '\\toprule',
                        'century & $n$ & plaintext language & $n$ \\\\', '\\midrule'] +
                       [f'{a} & {b} & {tex(c)} & {d} \\\\' for (a, b), (c, d) in zip(cen_rows, lang_rows)] +
                       ['\\bottomrule', '\\end{tabular}',
                        f'\\caption{{\\label{{tab:corpus}} The corpus by century of the earliest document and by plaintext language '
                        f'(a target with letters in two languages counts under both; {len(langs)} languages in all).}}', '\\end{table}', '']))
    T.append(group_table(ps, lambda t: t['region'] if t['region'] != U else 'not recorded', 'region (most documents)',
                         'Outcome by region of the correspondence: the region named by most documents of the target (Europe where no other is named).', 'region',
                         order=[EUROPE, 'North America', 'Latin America', 'East Asia', 'Middle East and South Asia', 'Oceania', 'not recorded']))
    T.append(group_table(ps, attack_group, 'starting point', 'Outcome by what the attack started from (profile field conditions.attack).', 'attack',
                         order=['ciphertext only', 'crib from clear text', 'decipherment or known plaintext', 'a key (archive, print, sibling)', 'none recorded']))
    T.append(group_table(ps, family, 'cipher family', 'Outcome by cipher family, from the system types in the profile.', 'family'))
    T.append(group_table(ps, prior_group, 'prior reading', 'Outcome by whether a reading of the text existed anywhere before this project, and when it was found (the contamination question).', 'prior',
                         order=['none known', 'existed, known before the attempt', 'existed, found during the attempt', 'existed, found after or not at all', 'existed, when found unknown', 'unknown']))
    T.append(group_table(ps, lambda t: lenband(t['tokens']), 'ciphertext tokens', 'Outcome by ciphertext length (enciphered tokens summed over the documents of a target).', 'length',
                         order=['$<$ 250', '250--999', '1,000--4,999', '$\\geq$ 5,000', 'unknown']))
    # Table: the ciphertext-only key recoveries
    ct = sorted([t for t in ps if t['method'] == CT], key=lambda t: (t['year'] or 9999))
    rows = ['\\begin{table*}[t]', '\\centering\\small', '\\resizebox{\\textwidth}{!}{%', '\\begin{tabular}{@{}lrllrll@{}}', '\\toprule',
            'target & year & language & system & tokens & key order & extent \\\\', '\\midrule']
    for t in ct:
        rows.append(f'{mark(t)} & {t["year"] or "--"} & {tex(", ".join(sorted(t["langs"])) or "--")} & {tex(family(t))} & '
                    f'{t["tokens"] if t["tokens"] else "--"} & {tex(t["key_order"])} & {t["ext"]} \\\\')
    rows += ['\\bottomrule', '\\end{tabular}}',
             f'\\caption{{\\label{{tab:ct}} The {len(ct)} targets whose key was recovered from the ciphertext alone. $^\\dagger$~solved in part by an outside contributor.}}', '\\end{table*}', '']
    T.append('\n'.join(rows))
    if INCLUDE_CONTRIBUTED: T.append(CONTRIB_TABLE)
    (OUT / 'tables.tex').write_text('\n'.join(T), encoding='utf-8')

    # ---- appendix
    head = 'target & year & language & system & method & extent & tokens \\\\'
    A = ['\\onecolumn', '{\\scriptsize', '\\begin{longtable}{@{}llrlllr@{}}',
         '\\caption{\\label{tab:all} Every target in the corpus, by date of the earliest document. Methods: '
         + '; '.join(f'{ABBR[x]} {SHORT[x]}' for x in MT.METHODS) + '. $^\\dagger$~solved in part by an outside contributor. Full profiles are in the data release.}\\\\',
         '\\toprule', head.replace('target & year', 'target & year'), '\\midrule', '\\endfirsthead',
         '\\toprule', head, '\\midrule', '\\endhead', '\\bottomrule', '\\endlastfoot']
    for t in sorted(ps, key=lambda t: (t['year'] or 9999, t['target'])):
        A.append(f'{mark(t)} & {t["year"] or "--"} & {tex(", ".join(sorted(t["langs"])) or "--")} & {tex(family(t))} & '
                 f'{ABBR[t["method"]]} & {t["ext"]} & {t["tokens"] if t["tokens"] else "--"} \\\\')
    A += ['\\end{longtable}}', '']
    if INCLUDE_CONTRIBUTED: A.append(CONTRIB_APPENDIX)
    (OUT / 'appendix.tex').write_text('\n'.join(A), encoding='utf-8')

    # ---- data release, same corpus
    rows_ = []
    for t in (everyone if INCLUDE_CONTRIBUTED else ps):
        prof = t['prof']
        base = {'target': t['target'], 'title': prof['title']}
        for sect in ('system', 'conditions', 'outcome'): ex.flat(prof[sect], sect, base)
        base['solution.steps'] = len(t['steps'])
        base['solution.kinds'] = '; '.join(x.get('kind', '') for x in t['steps'])
        base['solution.failed_steps'] = sum(1 for x in t['steps'] if x.get('result') in ('failed', 'ruled out'))
        base['documents.count'] = t['ndocs']
        base['provenance'] = t['prov']
        base['solved_by'] = '; '.join(name.get(w, w) for w in dict.fromkeys(solvers(t))) if t['prov'] != 'project' else 'project'
        for d in prof['documents']: rows_.append({**base, **ex.flat(d, 'doc', {})})
    cols = []
    for r in rows_:
        for k in r:
            if k not in cols: cols.append(k)
    with (HERE / 'targets.csv').open('w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows_)
    (HERE / 'codebook.md').write_text(ex.codebook(cols), encoding='utf-8')

    for k, v in M.items(): print(f'{k:22} {v}')
    print('skipped (invalid or outside the date range):', ', '.join(skipped) or 'none')
    print('methods:', dict(by))


if __name__ == '__main__':
    main()
