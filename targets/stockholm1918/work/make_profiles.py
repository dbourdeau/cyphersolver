"""Write both profile.json files. Run from the repository root."""
import json, subprocess, sys, re
sys.stdout.reconfigure(encoding='utf-8')
MODEL = 'claude-opus-5-5'; DAY = '2026-11-02'
PLAIN_S = {'location': ['none'], 'source': 'No decipherment filed in M367 rolls 108, 114, 122, 141; the cables were routed To MID. An MI-8 or Room 40 decode may exist, not located.'}
def measure(folder, t):
    p = f'targets/{folder}/groups/{t}.txt'
    g = open(p, encoding='utf-8').read().split()
    r = subprocess.run([sys.executable, '-X', 'utf8', 'docs/_check_profile.py', '--measure', p], capture_output=True, text=True)
    d = json.loads(r.stdout)
    return {'tokens': d['tokens'], 'distinct': d['distinct'], 'unit': 'code groups', 'measured': True, 'file': f'groups/{t}.txt'}
def doc(folder, t, shelf, date, pages, route, note, places=None, year=1918):
    d = {'id': t, 'shelfmark': shelf, 'date': date, 'year': year, 'country': 'Germany', 'route': route, 'language': 'unknown',
         'pages': pages, 'cleartext_in_document': 'none', 'plaintext': PLAIN_S, 'length': measure(folder, t),
         'transcription': {'by': 'llm from images', 'source': 'NARA catalogue scans, M367, checked against NARA OCR of the frame and of the cable copy',
                           'image_quality': 'fair', 'notes': note}}
    if places: d['places'] = places
    return d
BS = {'from': 'Berlin', 'to': 'Stockholm'}
R = 'Berlin -> Stockholm'
S = 'NARA RG 59 M367 '
A = [doc('stockholm1918', 'w765', S + 'roll 141 ff. 1265-66; roll 108 ff. 0747-53', '27 Jul 1918', 2, R, 'Header 284 groups, matched. Nr. 1010, signed Hintze. System A.', BS),
     doc('stockholm1918', 'w752', S + 'roll 141 f. 1259; roll 108 ff. 0700-01', '26 Jul 1918', 1, R, 'Header 120 groups, 73 in both copies. Nr. 1011. System C.', BS),
     doc('stockholm1918', 'w763', S + 'roll 141 f. 1256; roll 108 ff. 0691-95', '27 Jul 1918', 1, R, 'Header 190 groups, matched. Nr. 1012, signed Hintze. System A.', BS),
     doc('stockholm1918', 'w749', S + 'roll 141 f. 1261; roll 108 ff. 0723-24', '26 Jul 1918', 1, R, 'Header 41 groups, matched. Nr. 1013. System B.', BS),
     doc('stockholm1918', 'w746', S + 'roll 141 f. 1263; roll 108 ff. 0726-27', '26 Jul 1918', 1, R, 'Header 70 groups, matched once two typed lines repeated by the copyist are dropped. Nr. 1014. System B.', BS),
     doc('stockholm1918', 'w735', S + 'roll 141 f. 1262; roll 108 f. 0725', '26 Jul 1918', 1, R, 'Header 24 groups, matched. Nr. 1015, signed Bussche. System A.', BS),
     doc('stockholm1918', 'w643', S + 'roll 122 f. 0155', '22 Jul 1918', 1, R, 'Header 149 groups, 142 legible, 4 struck; no cable copy. System D.', BS),
     doc('stockholm1918', 'w2635', S + 'roll 114 f. 0416; roll 108 ff. 0512-13', '2 Jul 1918', 1, R, 'Header 46 groups, matched. Nr. 925, signed Stumm. System A. Date from 961 = vom 2 Juli.', BS),
     doc('stockholm1918', 'w512', S + 'roll 114 f. 0417; roll 108 ff. 0513-14', '2 Jul 1918', 1, R, 'Header 28 groups, matched. Nr. 923. System B.', BS),
     doc('stockholm1918', 'w513', S + 'roll 114 f. 0418; roll 108 ff. 0514-15', '2 Jul 1918', 1, R, 'Header 40 groups, matched. Nr. 924. System B.', BS)]
L = [doc('ludendorff1918', 'w791', S + 'roll 141 f. 1264; roll 108 ff. 0705-09', '26 Jul 1918', 1, 'Grosses Hauptquartier -> Stockholm', 'Five parts, declared 39, 30, 38, 31, 33; 170 groups legible. Signed Ludendorff.', {'from': 'Spa', 'to': 'Stockholm'}),
     doc('ludendorff1918', 'w769', S + 'roll 141 f. 1257; roll 108 ff. 0698-99', '26 Jul 1918', 1, R, 'Opens funfacht vanadopote.', BS),
     doc('ludendorff1918', 'w716', S + 'roll 141 f. 1258; roll 108 ff. 0699-0700', '26 Jul 1918', 1, R, 'Opens funfneun cavesaltri.', BS),
     doc('ludendorff1918', 'w592', S + 'roll 141 f. 1260; roll 108 ff. 0722-23', '26 Jul 1918', 1, R, 'To the Consulate-General. Opens 2507 18; one garbled group left out; ends bidenus 177/2.', BS),
     doc('ludendorff1918', 'w628', S + 'roll 122 f. 0156', '22 Jul 1918', 1, R, 'Opens Fuefsecho Ifesuijuni; no cable copy.', BS),
     doc('ludendorff1918', 'w611', S + 'roll 122 f. 0157', '22 Jul 1918', 1, R, 'Opens hansa 22 juli; clear words between the groups; no cable copy.', BS)]
sysbase = {'symbol_kind': 'digits', 'distinct_symbols': 'unknown', 'diacritics': {'used': False}, 'homophones': {'used': 'unknown'},
           'nomenclator': {'present': 'unknown'}, 'nulls': {'present': 'unknown'}, 'key_order': 'unknown', 'word_division': 'unknown',
           'doubled_letters': 'unknown', 'sibling_key': 'unknown'}
cond = lambda: {'prior_solution': {'exists': 'unknown', 'where': 'An MI-8 or Room 40 decode may exist (the cables were routed To MID); none located. Mendelsohn 1937 does not mention this traffic.', 'found': 'not found', 'used': False},
    'inputs': ['images'], 'attack': 'none', 'human_role': 'Selected the two catalogue entries and set the goal.',
    'tools': ['NARA catalogue scans and OCR', 'Internet Archive', 'python statistics and additive, slider and page-table tests'],
    'models': [MODEL], 'sessions': 1, 'first_date': DAY, 'last_date': DAY}
step = lambda kind, what, result, tech=None: dict(date=DAY, kind=kind, **({'technique': tech} if tech else {}), what=what, result=result)
shared = [
 step('access', 'Downloaded the telegram frames of M367 rolls 141, 114, 122 and the Christiania cable copies on roll 108; fetched NARA OCR of all four rolls.', 'worked'),
 step('literature search', 'Found Mendelsohn, Studies in German Diplomatic Codes (1937) on the Internet Archive after nsa.gov returned 403: 13040, 5950, 26040, the 18470 family, the Dreinummerheft, sliders.', 'worked'),
 step('literature search', 'Searched Zeman, Germany and the Revolution in Russia (1958), and the web for these telegrams or a decode: nothing for these days. FRUS not checked page by page.', 'failed')]
tests = [
 step('sibling key', 'Plain 13040, 18470-family and Bernstorff 1917 groups against every telegram: exact hits at chance. System D looked close (13049, 13047, 18147 = entziffern) but 3 of 142 hits is chance.', 'ruled out'),
 step('statistics', 'Constant additive -999 to +999 against those sets, the 26040 scheme. Best outliers come from repeated groups and give nonsense.', 'ruled out'),
 step('sibling key', 'Slider no. 1 rebuilt from Mendelsohn p. 98, worked example reproduced, all 1000 settings both ways against 13040 and Verkehrsbuch groups. Top settings give nonsense.', 'ruled out'),
 step('sibling key', '18470 groups converted to 12444, 1777, 2310 through the page tables and block shift, with a shuffled-table control: chance. About 125 of 300 pages survive the OCR, so this pass is partial.', 'ruled out')]
stock = {'schema_version': 1, 'target': 'stockholm1918',
 'title': 'German Foreign Office to Legation Stockholm, numeric-code telegrams, 2 and 22-27 July 1918 (NARA M367; catalogue 654)',
 'documents': A,
 'system': dict(types=['code'], summary='At least four separate numeric code systems in one numbered series, none identified: four figures with prefix (mark 1219); to about 24000 (marks 44xx); to about 48000; to about 18200.', **sysbase),
 'conditions': cond(),
 'solution': shared + [
  step('transcription', 'Transcribed ten telegrams, 938 groups; header counts match on eight and flag truncation on w752 and a shortfall on w643; checked against OCR of frame and cable.', 'worked'),
  step('statistics', 'Split into four systems by group range, first-figure index of coincidence and repeats. Found the shared openings 9405 2837 and 23456 21890 in system B.', 'worked')] + tests + [
  step('reading', 'Decoded the heads with the Dreinummerheft rule rebuilt from Mendelsohn pp. 5, 21, 29: Nr. 923-925 and Nr. 1010-1015, a consecutive run across three systems; 961 = vom 2 Juli redates despatch 1421 from 22-27 July to about 1-2 July.', 'worked')],
 'outcome': {'method': 'not solved', 'method_basis': 'No key or skeleton for any of the four systems could be reached, all known German codes printed by Mendelsohn were ruled out, and 938 groups are too few for a ciphertext-only attack.',
  'contribution': ['transcription', 'sender or date identified', 'catalogue correction'], 'class': 'not read', 'key': 'none', 'fraction_read': 0, 'verification': [],
  'notes': 'Blocked on the code books or the clear drafts. The heads now give the numbers to ask for in the Politisches Archiv.',
  'gaps': [{'item': 'All four systems, 938 groups', 'blocker': 'no-key-material'}, {'item': 'w752, last 47 of 120 groups', 'blocker': 'no-key-material'}, {'item': 'Any MI-8 or Room 40 decode', 'blocker': 'needs-physical-access'}]}}
lud = {'schema_version': 1, 'target': 'ludendorff1918',
 'title': 'Ludendorff to the military attache Stockholm, and Berlin to Legation and Consulate-General Stockholm, July 1918 (NARA M367; catalogue 656)',
 'documents': L,
 'system': dict(types=['undetermined'], summary='Five-figure groups flat in every column, with almost no repeats and no reused additive; system undetermined.', **sysbase),
 'conditions': cond(),
 'solution': shared + [
  step('transcription', 'Transcribed six telegrams, 328 groups; w791 part counts 39, 30, 37, 31, 33 against 39, 30, 38, 31, 33 declared, a struck group in part 3.', 'worked'),
  step('statistics', 'Index of coincidence per column 1.01-1.06 and 0.97-1.04, flat; two repeats (71903, 03515) against 0.5 expected.', 'worked'),
  step('statistics', 'Digit kappa at every offset within and across the six telegrams: 1,575 tests, one at |z| >= 3.5 against 0.7 expected. No depth.', 'failed')] + tests,
 'outcome': {'method': 'not solved', 'method_basis': 'Figures flat, no depth, no key reachable, and all known German codes printed by Mendelsohn ruled out.',
  'contribution': ['transcription', 'catalogue correction'], 'class': 'not read', 'key': 'none', 'fraction_read': 0, 'verification': [],
  'notes': 'Blocked on the key or a clear copy.',
  'gaps': [{'item': 'All six telegrams, 328 groups', 'blocker': 'no-key-material'}, {'item': 'Any MI-8 or Room 40 decode', 'blocker': 'needs-physical-access'}]}}
for name, p in (('stockholm1918', stock), ('ludendorff1918', lud)):
    with open(f'targets/{name}/profile.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(p, f, ensure_ascii=False, indent=1); f.write('\n')
