"""NOTE (11 Nov 2026): profile.json has been edited by hand since this script last ran (Carmichael summary, the six Code
No. 16 letters of PR #399, credits, gaps, texts). Do not re-run it without carrying those edits over.

Write ct/<letter>.txt, texts/<letter>_decryption.txt and profile.json for legation1788.

Lengths are measured with docs/_check_profile.py's measure(); counts come from reading.tsv (make_reading.py).
Solution steps are kept here in order, failures included. Run after make_reading.py.
"""
import csv, json, os, sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'docs'))
from _check_profile import measure  # noqa: E402

DOCS = OrderedDict([
    ('short_17920726', dict(
        label='William Short to Jefferson, The Hague, 26 Jul 1792 (Code No. 10)', date='26 Jul 1792', year=1792,
        shelf='Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 016_0998-1009 (RC, TJ interlinear decoding); '
              'extract re-enciphered in Short to TJ 27 Jul 1792, 016_1010-1012',
        route='The Hague -> Philadelphia', loc=['interlinear'], src="TJ's interlinear decoding (incomplete) and the PTJ editors' reading",
        partial=True, quality='fair', clear='mostly clear',
        review=('A', "The coded paragraphs read through as Short's sentences (Jefferson's interlinear on 511 groups, the editors' reading on the rest); two short holes: 401/1083/401 and 359 199 34 724."),
        summary="Short's private complaint at being passed over for Paris in favour of Gouverneur Morris: Lafayette's mortification, "
                "the French diplomatic committee's wish to refuse Morris, and Short's preferences for a post (the Hague as resident, "
                "Spain as plenipotentiary) and for the grades of the American diplomatic establishment.")),
    ('carmichael_17880414', dict(
        label='William Carmichael to Jefferson, Madrid, 14 Apr 1788 (Code No. 13)', date='14 Apr 1788', year=1788,
        shelf='Library of Congress, Thomas Jefferson Papers ser. 1, mtj1 009_0223-0230 (RC)',
        route='Madrid -> Paris', loc=['none'], src='No decoding; five code items read by context (PTJ editors, conjecture)',
        partial=True, quality='fair', clear='mostly clear',
        review=('B', 'Two sentences of clear text with four code names read by context (Maryland, Massachusetts, majority) and one open item (597).'),
        summary='A clear letter with five code numbers used as a test of his cypher: Maryland (twice), Massachusetts and '
                'the majority on the ratification of the Constitution; the last item (597) stays open.')),
    ('pinckney_17930828', dict(
        label='Thomas Pinckney to Jefferson, London, 28 Aug 1793 (Code No. 16)', date='28 Aug 1793', year=1793,
        shelf='NARA RG 59, Despatches from U.S. Ministers to Great Britain, M30 roll 2 frame 0140 (RC)',
        route='London -> Philadelphia', loc=['none'], src="PTJ editors' partial decipherment; values checked against George Taylor's decodings of Pinckney's other letters",
        partial=True, quality='fair', clear='mostly clear',
        review=('A', 'Three coherent sentences; the number of regiments (447) open and two words ([time], [secret]) conjectural.'),
        summary='Three coded sentences: regiments are to embark shortly on a secret expedition under Sir Charles Grey with '
                'Generals Stuart and Dundas, generally thought to be for the West Indies; the number of regiments (447) stays open.')),
])

STEPS = [
    ('2026-10-26', 'literature search', 'Catalogue 484 brief (Founders Online sweep): Short 26 Jul 1792 Code No. 10 (401, 1083, 401; 359, 199, 34, 724 undeciphered), Carmichael 14 Apr 1788 Code No. 13 (conjectural), T. Pinckney 28 Aug 1793 Code No. 16 (deciphered in part, 497 undeciphered).', 'worked', None),
    ('2026-10-27', 'access', 'Founders texts through the built-in browser (plain HTTP blocked); LoC item JSON gave mtj1 016_0998-1009 (Short) and 009_0223-0230 (Carmichael); master JPEGs from tile.loc.gov.', 'worked', None),
    ('2026-10-27', 'access', "Short's private letter of 27 Jul 1792 (016_1010-1012) re-enciphers the paragraph with the same groups and no decoding: digits confirmed, no plaintext.", 'partial', None),
    ('2026-10-27', 'hypothesis', 'Code No. 10 values on 016_1007-1008 sorted by number to test alphabetical bracketing: no ordered run (two-part code); bracketing ruled out.', 'failed', ['key-structure hypothesis']),
    ('2026-10-27', 'sibling key', "Carmichael's groups looked up in the Code No. 11 table rebuilt in jefferson1787: 597 = freedom, 223 = trouble there; Code No. 13 is a different code. Founders 'Code No. 13' = this letter only.", 'failed', ['key matching']),
    ('2026-10-27', 'access', 'Pinckney despatches found on NARA M30 roll 2 (catalog media server): 28 Aug 1793 = frame 0140; frames 0101-0330 downloaded (dl_m30.py).', 'worked', None),
    ('2026-10-27', 'transcription', 'Subagent transcribed all code on 15 coded Pinckney frames (~2,660 rows) with George Taylor\'s interlinear decodings (20 Jun, 25 Sep, 27 Nov, 17 Dec 1793, 28 Jan, Feb 1794) and the 25 Nov 1793 Explication aligned by hand.', 'worked', None),
    ('2026-10-27', 'reading', '28 Aug 1793 groups checked against the attested Code No. 16 values: 30 of 58 confirmed (to be, with, general-s, and, under him, des-tina-tion, general-ly thought, for); 447, 234, 501 occur nowhere else.', 'worked', ['key matching']),
    ('2026-10-27', 'verification', "First group re-read at 2x: two matching open 4s, 447 (the editors printed 497).", 'worked', None),
    ('2026-10-27', 'sibling key', "Search of the 39 Code No. 10 documents (Founders notes, six letters on the images, ~1,100 groups of 31 May 1793): 401, 1083, 359, 199, 34, 724 occur only in the 26 Jul 1792 passage; 'been' = 1700, not 401.", 'failed', ['key matching']),
    ('2026-10-27', 'transcription', "Subagent transcribed all 674 code groups of Short's 26 Jul 1792 letter with TJ's interlinear (511 groups under a TJ word).", 'worked', None),
    ('2026-10-27', 'literature search', "Web search for the number of regiments in Grey's force (Aug 1793) as a crib for 447: nothing specific.", 'failed', ['crib testing']),
    ('2026-10-27', 'reading', 'reading.tsv measured: 737 groups, 728 with a reading (720 without conjectures), 9 open single-occurrence groups.', 'worked', ['contextual inference']),
]


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8'), delimiter='\t'))
    by = OrderedDict((k, [r for r in rows if r['letter'] == k]) for k in DOCS)
    os.makedirs(os.path.join(HERE, 'ct'), exist_ok=True)
    os.makedirs(os.path.join(HERE, 'texts'), exist_ok=True)
    docs, texts, grades, groups = [], [], Counter(), Counter()
    N = R = RC = 0
    for name, d in DOCS.items():
        rs = by[name]
        lines, cur, key = [], [], None
        for r in rs:
            k = (r['frame'], r['line'])
            if k != key and cur:
                lines.append(cur); cur = []
            key = k
            cur.append(r)
        if cur:
            lines.append(cur)
        ct = os.path.join(HERE, 'ct', name + '.txt')
        with open(ct, 'w', encoding='utf-8') as f:
            f.write(f'# {d["label"]}: code groups as transcribed, one line per manuscript line\n')
            for l in lines:
                f.write('.'.join(r['group'] for r in l) + '.\n')
        with open(os.path.join(HERE, 'texts', name + '_decryption.txt'), 'w', encoding='utf-8') as f:
            f.write(f'# {d["label"]}: group = reading [grade]; T TJ interlinear, H attested elsewhere, E editors, C conjecture, O open\n')
            for l in lines:
                f.write(' '.join(f"{r['group']}={r['reading'] or '-'}[{r['grade']}]" for r in l) + '\n')
        m = measure(ct)
        n = len(rs); o = sum(r['grade'] == 'O' for r in rs); c = sum(r['grade'] == 'C' for r in rs)
        N += n; R += n - o - c; RC += n - o
        for r in rs:
            grades[r['grade']] += 1; groups[r['group']] += 1
        state = 'read' if n and (n - o - c) / n >= 0.95 else 'read in part'
        docs.append({
            'id': name, 'read': state, 'shelfmark': d['shelf'], 'date': d['date'], 'year': d['year'],
            'country': 'United States', 'route': d['route'], 'language': 'English',
            'cleartext_in_document': d['clear'],
            'plaintext': {'location': d['loc'], 'source': d['src'], 'partial': d['partial']},
            'length': {'tokens': m['tokens'], 'distinct': m['distinct'], 'unit': 'code groups', 'measured': True,
                       'file': 'ct/' + name + '.txt'},
            'transcription': {'by': 'llm from images', 'source': d['shelf'], 'image_quality': d['quality'],
                              'notes': f'{n} groups in reading.tsv: {o} open, {c} conjectural.'}})
        texts.append({'doc': name, 'label': d['label'], 'transcription': 'ct/' + name + '.txt',
                      'decryption': 'texts/' + name + '_decryption.txt', 'reading': 'texts/' + name + '_reading.txt',
                      'summary': d['summary'], 'language': 'en',
                      'read_share': round((n - o - c) / n, 3), 'state': state,
                      'reading_review': {'grade': d['review'][0], 'by': 'Claude Opus 5.5', 'date': '2026-10-27', 'note': d['review'][1]}})
    p = os.path.join(HERE, 'profile.json')
    prof = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    prof.update({'schema_version': 1, 'target': 'legation1788',
                 'title': "Jefferson-era legation codes Nos. 10, 13 and 16: residual groups in Short 1792, Carmichael 1788 and Thomas Pinckney 1793 (catalogue 484)"})
    prof['documents'] = docs
    prof['system'] = {
        'types': ['code', 'syllabic'],
        'summary': 'Three two-part numerical codes of about 1,700-1,850 groups (words, syllables, letters), groups separated by dots.',
        'symbol_kind': 'digits', 'digit_groups': {'width': '1-4', 'separation': 'dots'},
        'distinct_symbols': len(groups), 'diacritics': {'used': False},
        'homophones': {'used': 'unknown'},
        'nomenclator': {'present': True, 'entries': 'unknown', 'kinds': ['syllables', 'word parts', 'common words', 'names'],
                        'unread_groups': len({r['group'] for r in rows if r['grade'] == 'O'})},
        'nulls': {'present': 'unknown'}, 'key_order': 'random', 'word_division': 'none', 'doubled_letters': 'unknown',
        'sibling_key': "No key sheet survives for Codes 10, 13 or 16. Code No. 16 values collected from George Taylor's interlinear decodings of Pinckney's other letters on M30 roll 2; Code No. 11 (jefferson1787) does not fit Code No. 13.",
        'notes': 'Three different codes in one record; distinct_symbols counts distinct groups across the three counted passages. '
                 "Code No. 10 checked for alphabetical order: none. '+' after a Code No. 16 group marks a plural."}
    prof['conditions'] = {
        'prior_solution': {'exists': 'in print',
                           'where': 'The Papers of Thomas Jefferson vols. 13 (1956), 24 (1990) and 26 (1995), via Founders Online: the three letters printed decoded from partial reconstructions of Codes 10, 13 and 16, conjectures in brackets, named groups undeciphered.',
                           'found': 'before attempt', 'used': True},
        'inputs': ['images', 'published reading', 'cleartext context', 'sibling key'],
        'attack': 'archive decipherment',
        'human_role': "Pasted the catalogue no. 484 task brief (from the project's solve page) into the session; no target-specific intervention.",
        'tools': ['built-in browser (Founders Online, LoC item JSON)', 'curl (tile.loc.gov, NARA catalog media)', 'PIL crops',
                  'subagents for transcription and sibling search', 'make_reading.py, make_profile.py'],
        'models': ['claude-opus-5-5'], 'sessions': 1, 'first_date': '2026-10-26', 'last_date': '2026-10-27'}
    prof['solution'] = [dict(date=a, kind=b, what=c, result=e, **({'technique': t} if t else {})) for a, b, c, e, t in STEPS]
    o = prof.setdefault('outcome', {})
    o.update({
        'method': 'read from existing decipherment',
        'method_basis': "The readings are Jefferson's interlinear decoding of Short's letter and the Jefferson Papers editors' printed decodings of all three; the work transcribed every group, checked them against values attested in sibling letters of the same code, and searched the siblings for the open groups.",
        'contribution': ['transcription', 'key extended or corrected', 'catalogue correction'],
        'class': 'already solved', 'key': 'partial',
        'fraction_read_method': 'measured',
        'fraction_read_source': f'reading.tsv: {N} counted code groups (one struck group excluded), {R} with a reading, {RC - R} more by conjecture only (counted unread), {N - RC} open',
        'fraction_read': round(R / N, 3),
        'codes_open': {'open': len({r['group'] for r in rows if r['grade'] == 'O'}), 'total': 'unknown', 'tokens_open': N - RC},
        'grades': {'H': grades['T'] + grades['H'], 'M': grades['E'], 'I': grades['C']},  # T/H attested, E editors only, C context
        'verification': ['contemporary decipherment', 'key confirms', 'historical consistency'],
        'credits': [
            {'who': 'contemporary', 'role': 'key or decipherment used',
             'note': "Jefferson's interlinear decoding of Short's letter; George Taylor Jr.'s State Department decodings of Pinckney's letters in Code No. 16"},
            {'who': 'ptj-editors', 'role': 'prior solution',
             'note': 'the three letters printed decoded from partial reconstructions of Codes 10, 13 and 16, with the open groups named; used here as the reading',
             'date': '1956-1995', 'source': 'The Papers of Thomas Jefferson vols. 13, 24, 26, via Founders Online', 'published': True},
            {'who': 'ajbeling', 'role': 'identification',
             'note': "Code No. 16 (Weber's '663' code, 1979 p. 155) found in T. Pinckney's 1795 Madrid and Paris letters, W. Eaton's Tunis letters of 1801-02 and T. Lear's of 1813; Weber had tied Pinckney's code to King and Livingston, and the Madison editors read Eaton and Lear with one key (beling/)",
             'date': '2026-11'},
            {'who': 'ajbeling', 'role': 'key corrected',
             'note': 'Code No. 16 key of 537 groups from those letters, with held-out tests; 234 = time, 501 = secret, 1328 1374 = Sir, 668 = at, 675 = ly, 1010 = tin in the 28 Aug 1793 passage (beling/)',
             'date': '2026-11'}],
        'gaps': [
            {'item': 'Pinckney 28 Aug 1793, group 447 (before "regiments")', 'blocker': 'too-short',
             'detail': 'single occurrence in all 15 coded Pinckney frames on M30 roll 2; no decoding; the editors printed it as 497'},
            {'item': 'Pinckney 28 Aug 1793, 234 [time?], 501 [secret?], ?55 668 [Dunda-]', 'blocker': 'too-short',
             'detail': "single occurrences kept as the editors' conjectures; first digits of ?55 in the gutter"},
            {'item': 'Short 26 Jul 1792, 401 (x2), 1083, 359, 199, 34, 724', 'blocker': 'too-short',
             'detail': 'only in this passage and its 27 Jul re-encipherment; no decoding in any Code No. 10 letter checked; been = 1700'},
            {'item': 'Carmichael 14 Apr 1788, 597 and the context-only values of 108, 223, 273', 'blocker': 'no-key-material',
             'detail': 'Code No. 13 survives in this letter only; no key'}],
        'notes': "Everything readable was read before (TJ's interlinear; PTJ editors). Added: 447 for the printed 497; 30 of the 58 Pinckney groups confirmed from Taylor's decodings; Code No. 13 shown not to be Code No. 11; 'been' = 1700 in Code No. 10, so the editors could not have meant 401 = been without a homophone; full transcriptions of Short's 674 groups and of Pinckney's 15 coded frames.",
        'texts': texts, 'key_file': 'key.tsv'})
    json.dump(prof, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    open(p, 'a', encoding='utf-8').write('\n')
    print(f'{len(docs)} documents; {R}/{N} read ({R/N:.3f}), {RC}/{N} incl. conjecture; grades {dict(grades)}')


if __name__ == '__main__':
    main()
