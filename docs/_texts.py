"""Full texts on every reading (George Lasry, 22 Oct 2026).

A reading (classed "read" or "read in part", or "already solved" with a reading method) lists, in profile.json outcome.texts, the transcription and the decryption of
every document it reports on, and in outcome.key_file the key it used when the project recovered, extended or
corrected it. Paths are relative to the target folder (or http(s) URLs, discouraged: a copy in the folder survives).

  "texts": [{"doc": "<documents[].id>", "label": "R1072, 6 Jan 1757 (optional)",
             "transcription": "transcr/R1072.txt", "decryption": "read/R1072.md",
             "reading": "read/R1072_reading.md (optional: the decryption as sentences)",
             "translation": "read/R1072_en.md", "language": "fr",
             "contemporary": "transcr/R1072_decifrado.txt (optional: the decipherment of the time, transcribed)",
             "transcription_missing": "reason (only when the cipher itself was never transcribed: never put the
                                      clear copy or the decipherment of the time under transcription)",
             "state": "read | read in part | decoded, not read | not prose",
             "summary": "One or two sentences on what the document says."}],
  "key_file": "key_X.tsv"          (or a list)
  "texts_withheld": "reason"         when the texts must not be republished (the owner asked); exempts the target

One entry may cover several documents ("doc": ["a", "b"]) when one file holds them all. The site builder renders a
"Full texts" section from it (short files inline, long ones linked); docs/_check_writeup.py refuses a reading
without it. texts_problems() is the shared check.

A reading must read (George Lasry, 22 Oct 2026, on matignon1586): "the LLM can build coherent sentences - that can
later be translated to English ... It is OK to have a few holes, but not holes in almost every sentence."
reading_problems() is that check, per entry:

  state "read" (default)    a reader has read the decryption as sentences and recorded reading_review {grade A|B,
                            by, date, note} (A coherent with scattered holes; B coherent but raw, normalised in the
                            reading or translation); and it carries an English translation unless language is "en".
                            docs/_check_reading.py's sentence score is printed as a pointer for the reader;
                            and it meets the README read bar: 95% of its words read as sense (read_share), or,
                            for a text of fewer than 40 cipher words, the floor: at most 5% or 2 holes, recorded
                            as floor_used, cipher_words and holes (19 Nov 2026)
  state "read in part"      (24 Oct 2026) builds coherent sentences, reviewed and translated as above, but under
                            95% of its words read as sense; read_share records the measure
  state "decoded, not read" a mechanical decode shown for checking, not counted as a reading; no translation needed
  state "not prose"         a key sheet, code list, worksheet, numbers or names; say what in note
A target classed "read" may hold only "read" (and "not prose") entries.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
READING = ('read', 'read in part')
NOT_READINGS = ('not solved', 'not applicable')   # methods that mean no reading exists
KEY_WORK = ('key recovered', 'key extended or corrected')


def listify(v):
    return [] if v in (None, '') else v if isinstance(v, list) else [v]


def needs_texts(profile):
    """A reading: classed read / read in part, or already solved elsewhere with a reading method (from an existing
    decipherment, a known or external key, plaintext ...): the text was deciphered, so it is shown (22 Oct 2026)."""
    o = (profile or {}).get('outcome') or {}
    if o.get('class') in READING: return True
    return o.get('class') == 'already solved' and o.get('method') not in NOT_READINGS and bool(o.get('method'))


def texts_problems(folder_path, profile):
    """Problems with outcome.texts / key_file for a reading; [] when fine or when the target is not a reading."""
    if not needs_texts(profile): return []
    o = profile.get('outcome') or {}
    if o.get('texts_withheld'): return []          # e.g. fr3029/fr3092: Lasry asked (22 Sept 2026) not to republish
    probs = []
    texts = o.get('texts') or []
    if not texts:
        return ['no outcome.texts: list the transcription and decryption of every document (George Lasry, 22 Oct 2026)']
    docs = [d.get('id') for d in profile.get('documents') or [] if d.get('id')]
    covered = {x for t in texts for x in listify(t.get('doc'))}
    if 'all' not in covered:
        missing = [d for d in docs if d not in covered]
        if missing: probs.append('documents without texts: ' + ', '.join(missing[:8]) + (' ...' if len(missing) > 8 else ''))
    for t in texts:
        label = '/'.join(listify(t.get('doc'))) or '?'
        for kind in ('transcription', 'decryption'):
            files = listify(t.get(kind))
            if not files and not (kind == 'transcription' and t.get('transcription_missing')):
                probs.append(f'{label}: no {kind} file')
        # the transcription is the cipher as written, not a plaintext (philip1574, 24 Oct 2026)
        plain = {str(f) for k in ('decryption', 'reading', 'translation', 'contemporary') for f in listify(t.get(k))}
        for f in listify(t.get('transcription')):
            if str(f) in plain and str(f) in {str(x) for x in listify(t.get('reading')) + listify(t.get('translation')) + listify(t.get('contemporary'))}:
                probs.append(f'{label}: transcription file {f} is also the reading/translation/contemporary decipherment')
        for kind in ('transcription', 'contemporary', 'decryption', 'reading', 'translation'):
            for f in listify(t.get(kind)):
                if not str(f).startswith('http') and not (folder_path / f).exists():
                    probs.append(f'{label}: {kind} file {f} does not exist')
    contrib = o.get('contribution') or []
    if any(c in KEY_WORK for c in contrib):
        keys = listify(o.get('key_file'))
        if not keys: probs.append('no outcome.key_file although the key was recovered, extended or corrected')
        for f in keys:
            if not str(f).startswith('http') and not (folder_path / f).exists():
                probs.append(f'key file {f} does not exist')
    return probs


def entry_state(t):
    return t.get('state') or 'read'


_AUDIT = None


def audit_review(folder_path, entry=None):
    """The 22 Oct 2026 reading audit's grade (research/reading_audit/reviews.json), standing in for the reading_review
    of entries that have none of their own: the document's own grade when the per-document pass reached it, else the
    target's. A or B passes; C, D and N do not."""
    global _AUDIT
    if _AUDIT is None:
        p = ROOT / 'research' / 'reading_audit' / 'reviews.json'
        _AUDIT = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
    rec = _AUDIT.get(pathlib.Path(folder_path).name) or {}
    if entry is not None:
        key = '/'.join(map(str, listify(entry.get('doc'))))
        doc = (rec.get('docs') or {}).get(key)
        if doc: return doc
    return rec


FLOOR_WORDS, FLOOR_HOLES = 40, 2   # README Conventions, 19 Nov 2026: a text of fewer than 40 cipher words is "read" with at most 5% or 2 holes


def floor_problem(t):
    """None when the entry may be "read" under the short-text floor (it declares floor_used, cipher_words and holes, the
    text has fewer than 40 cipher words, holes are at most 5% of them or at most 2, and read_share agrees with the
    counts); else a string saying why not."""
    if not t.get('floor_used'):
        return 'not declared (floor_used, cipher_words, holes)'
    cw, holes, rs = t.get('cipher_words'), t.get('holes'), t.get('read_share')
    if not isinstance(cw, int) or not isinstance(holes, int) or cw <= 0 or holes < 0:
        return 'cipher_words and holes must be whole numbers'
    if cw >= FLOOR_WORDS:
        return f'the floor does not apply to a text of {FLOOR_WORDS} or more cipher words ({cw})'
    if holes > max(FLOOR_HOLES, 0.05 * cw):
        return f'{holes} holes in {cw} cipher words is over the floor (at most {FLOOR_HOLES} or 5%)'
    if isinstance(rs, (int, float)) and abs(rs - (cw - holes) / cw) > 0.01:
        return f'read_share {rs:.3f} does not match {cw - holes} of {cw} cipher words'
    return None


def reading_problems(folder_path, profile, score=True):
    """Problems with the readability of a reading's texts (George Lasry, 22 Oct 2026): [] when fine.
    Returns (hard, soft): hard refuses the write-up, soft is a warning."""
    if not needs_texts(profile): return [], []
    o = profile.get('outcome') or {}
    if o.get('texts_withheld'): return [], []
    hard, soft = [], []
    states = [entry_state(t) for t in o.get('texts') or []]
    if o.get('class') == 'read' and 'decoded, not read' in states:
        hard.append('classed "read" but an entry is "decoded, not read": a reading must read throughout')
    if o.get('class') == 'read' and 'read in part' in states:
        hard.append('classed "read" but an entry is "read in part" (under 95% of its words read as sense)')
    if states and all(s == 'decoded, not read' for s in states):
        hard.append('every entry is "decoded, not read": this is not a reading (class it "not read"; the method stays the one that obtained the key, or "not solved" when no key was obtained)')
    cr = None
    for t in o.get('texts') or []:
        label = t.get('label') or '/'.join(map(str, listify(t.get('doc')))) or '?'
        st = entry_state(t)
        if st == 'not prose':
            if not t.get('note'): soft.append(f'{label}: "not prose" without a note saying what it is')
            continue
        if st == 'decoded, not read': continue
        rs = t.get('read_share')
        if st == 'read' and isinstance(rs, (int, float)) and rs < 0.95:
            fl = floor_problem(t)
            if fl is None:
                pass                                     # a very short text read under the floor (19 Nov 2026)
            elif t.get('floor_used'):
                hard.append(f'{label}: floor_used but {fl}')
            else:
                hard.append(f'{label}: state "read" but read_share {rs:.3f} < 0.95 (mark it "read in part", or, for a text of fewer than {FLOOR_WORDS} cipher words with at most {FLOOR_HOLES} holes or 5%, record floor_used, cipher_words and holes)')
        if not listify(t.get('translation')) and (t.get('language') or '').lower() != 'en':
            hard.append(f'{label}: no English translation (outcome.texts[].translation; or language "en")')
        # the test is a reader's: someone read the decryption as sentences and recorded it (Lasry: "the acceptance
        # process should validate that the submission includes ... readable coherent text + translations"). The
        # sentence score is a pointer for that reader, not the verdict: on the 327 readings of the 22 Oct 2026 audit
        # it did not separate the readers' D grades from their A grades (research/reading_audit/README.md).
        rv = t.get('reading_review') or audit_review(folder_path, t)
        if rv.get('grade') not in ('A', 'B'):
            hard.append(f'{label}: no reading_review: a reader must read the decryption as sentences and record '
                        f'{{"grade": "A|B", "by": ..., "date": ..., "note": ...}} (or mark it "decoded, not read")')
        if not score: continue
        if cr is None:
            import _check_reading as cr
        best = None
        for f in listify(t.get('decryption')) + listify(t.get('reading')):
            fp = folder_path / f
            if str(f).startswith('http') or not fp.is_file() or fp.suffix.lower() in ('.pdf', '.json'): continue
            r = cr.score_text(fp.read_text(encoding='utf-8', errors='ignore'), lang=(t.get('language') or None))
            if r['shape'] == 'other script': best = ('n/a', r); break
            if best is None or (r['clean_share'] or 0) > (best[1]['clean_share'] or 0): best = (f, r)
        if best is None or best[0] == 'n/a': continue
        share = best[1]['clean_share'] or 0
        if share < cr.READABLE or best[1]['shape'] != 'reading':
            soft.append(f'{label}: {share:.0%} of sentences clean in {best[0]} (shape {best[1]["shape"]}): '
                        f'look at the weak sentences before recording the review')
    return hard, soft


def summary_missing(profile):
    """True when no document entry carries a summary of its contents (a nudge, not a refusal)."""
    if ((profile or {}).get('outcome') or {}).get('texts_withheld'): return False
    return needs_texts(profile) and not any(t.get('summary') for t in ((profile.get('outcome') or {}).get('texts') or []))
