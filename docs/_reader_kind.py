"""Who read a reading: a person, a model, or a person assisted by a model (16 Nov 2026).

Every `outcome.texts[].reading_review` names its reader in the free-text field `by`. Until now nothing said, in a
form a program can count, whether that reader was a person. This module classes the `by` string by rule and writes
two fields beside it:

  "reader_kind"   "model" | "person assisted by model" | "person"      (absent when the rule cannot tell)
  "independent"   false when the record itself says the reader was not independent of the work (same session, the
                  model that made the reading); true when the record itself says independent or blind; else absent

The rule reads only what the record says. It does not verify it. A value written here is "by rule, 16 Nov 2026" until
someone who knows the review corrects it by hand; a value already present is never overwritten.

  python docs/_reader_kind.py            counts by kind, and the strings the rule could not class
  python docs/_reader_kind.py --list     every reviewer string with its class
  python docs/_reader_kind.py --write    insert the fields into targets/*/profile.json (text insertion: the files keep
                                         their formatting)

counts() is what the site uses (the home-page tile and the method page).
"""
import json, re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
KINDS = ('model', 'person assisted by model', 'person')
MODEL = re.compile(r'claude|opus|sonnet|fable|haiku|codex|gpt|gemini|openai|anthropic|\bllm\b|\bai\b|\bmodel\b|agents?\b', re.I)
# a personal name at the start: "Brice Dudout", "B. Dudout", "Andrew Beling"
NAME = re.compile(r"^(?:[A-Z][a-zà-ÿ]+|[A-Z]\.)\s+(?:(?:de|van|von|da|di)\s+)?[A-Z][a-zà-ÿ]+(?![a-z])")
NOT_A_NAME = re.compile(r'^(Claude|Open\s?AI|AI|Author)\b', re.I)


def classify(by, note=''):
    """(reader_kind or None, independent or None) for a reading_review."""
    by = (by or '').strip()
    text = by + ' ' + (note or '')
    named = bool(NAME.match(by)) and not NOT_A_NAME.match(by)
    if named and re.match(r"^\S+(\s+\S+)?'s\s+(AI\s+)?agents?\b", by):
        named = False                             # "Brice Dudout's AI agents": the agents read, not the person
    has_model = bool(MODEL.search(by))
    if named and re.search(r'\(.*(edition|thesaurus|calendar)', by, re.I):
        kind = None                               # a printed edition, not a reviewer of this reading
    elif named and has_model:
        kind = 'person assisted by model'
    elif named:
        kind = 'person'
    elif has_model:
        kind = 'model'
    else:
        kind = None                               # "integration review (PR #418)", "project (...)": not stated
    low = text.lower()
    if re.search(r'not independent|same session|the model that made the reading|no second reader', low):
        indep = False
    elif re.search(r'\bindependent\b|\bblind\b', by.lower()) and not re.search(r'pending|not an? independent|no independent', by.lower()):
        indep = True
    else:
        indep = None
    return kind, indep


def reviews():
    """Yield (folder, text entry, reading_review) for every review in targets/*/profile.json."""
    for f in sorted((ROOT / 'targets').glob('*/profile.json')):
        try:
            p = json.loads(f.read_text(encoding='utf-8'))
        except ValueError:
            continue
        for t in (p.get('outcome') or {}).get('texts') or []:
            r = t.get('reading_review')
            if isinstance(r, dict):
                yield f.parent.name, t, r


def kind_of(r):
    return r.get('reader_kind') or classify(r.get('by'), r.get('note'))[0]


def counts():
    """{'reviews', 'model', 'person assisted by model', 'person', 'not stated', 'not independent', 'human_check'}"""
    c = collections.Counter()
    for _, _, r in reviews():
        c['reviews'] += 1
        c[kind_of(r) or 'not stated'] += 1
        ind = r['independent'] if 'independent' in r else classify(r.get('by'), r.get('note'))[1]
        if ind is False:
            c['not independent'] += 1
    for f in (ROOT / 'targets').glob('*/profile.json'):
        try:
            if (json.loads(f.read_text(encoding='utf-8')).get('outcome') or {}).get('human_check'):
                c['human_check'] += 1
        except ValueError:
            pass
    return dict(c)


def insert(text):
    """profile.json text with reader_kind / independent inserted after each reading_review's "by"; and how many."""
    dec, out, pos, n = json.JSONDecoder(), [], 0, 0
    for m in re.finditer(r'"reading_review"\s*:\s*(?=\{)', text):
        start = m.end()
        try:
            obj, end = dec.raw_decode(text, start)
        except ValueError:
            continue
        if not isinstance(obj, dict) or 'by' not in obj:
            continue
        kind, indep = classify(obj.get('by'), obj.get('note'))
        add = []
        if kind and 'reader_kind' not in obj:
            add.append(f'"reader_kind": {json.dumps(kind)}')
        if indep is not None and 'independent' not in obj:
            add.append(f'"independent": {json.dumps(indep)}')
        if not add:
            continue
        b = re.compile(r'"by"\s*:\s*').search(text, start, end)
        if not b:
            continue
        try:
            _, bend = dec.raw_decode(text, b.end())
        except ValueError:
            continue
        out.append(text[pos:bend]); out.append(', ' + ', '.join(add)); pos = bend; n += 1
    out.append(text[pos:])
    return ''.join(out), n


def main():
    if '--write' in sys.argv:
        files = changed = 0
        for f in sorted((ROOT / 'targets').glob('*/profile.json')):
            raw = f.read_bytes()
            text = raw.decode('utf-8')
            new, n = insert(text)
            if n:
                json.loads(new)                    # must still parse
                f.write_bytes(new.encode('utf-8')); files += 1; changed += n
        print(f'{changed} reviews in {files} profiles')
        return
    by = collections.Counter()
    for _, _, r in reviews():
        k, i = classify(r.get('by'), r.get('note'))
        by[(k or 'not stated', {True: 'independent', False: 'not independent', None: ''}[i], str(r.get('by')))] += 1
    if '--list' in sys.argv:
        for (k, i, s), n in sorted(by.items(), key=lambda x: (x[0][0], -x[1])):
            print(f'{n:5d}  {k:26s} {i:16s} {s[:120]}')
    c = counts()
    print(json.dumps(c, indent=1))
    print('not stated:')
    for (k, i, s), n in sorted(by.items(), key=lambda x: -x[1]):
        if k == 'not stated':
            print(f'{n:5d}  {s[:130]}')


if __name__ == '__main__':
    main()
