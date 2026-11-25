"""Shared parsing for the Casgrain vol. III cipher transcriptions (*.tr).

Transcription format (one file per letter, checked against page images):
  #letter ...        header
  #page N            printed page number of following lines
  #para              start of a paragraph (figure stream and clear stream both restart)
  F tok tok ...      printed figure line; {words} = words printed in clear inside the figures;
                     [ ] marks groups substituted by the editor (B1 p.108)
  C text             printed clear-text line (Casgrain's decipherment)
"""
import re, unicodedata

def norm(s):
    s = s.replace('(sic)', '').replace('œ', 'oe').replace('Œ', 'oe')
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]', '', s)

def parse(path):
    """Return dict(header, units=[{groups:[(kind,tok,page,line)], text:str, textpage:[page per char], clear_lines:[(page,str)]}])."""
    header = ''
    units = []
    cur = None
    page = None
    def new():
        u = {'groups': [], 'text': '', 'textpage': [], 'clear_lines': []}
        units.append(u)
        return u
    for ln_no, ln in enumerate(open(path, encoding='utf-8'), 1):
        ln = ln.rstrip('\n')
        if ln.startswith('#letter'):
            header = ln[len('#letter'):].strip(); continue
        if ln.startswith('#page'):
            page = ln.split()[1]; continue
        if ln.startswith('#para'):
            cur = new(); continue
        if ln.startswith('#'):
            continue
        if cur is None:
            cur = new()
        if ln.startswith('F '):
            body = ln[2:]
            for m in re.finditer(r'\{([^}]*)\}|(\d+\*?)', body.replace('[', ' ').replace(']', ' ')):
                if m.group(1) is not None:
                    w = norm(m.group(1))
                    if w:
                        cur['groups'].append(('w', w, page, ln_no))
                else:
                    cur['groups'].append(('g', m.group(2), page, ln_no))
        elif ln.startswith('C '):
            t = norm(ln[2:])
            cur['text'] += t
            cur['textpage'] += [page] * len(t)
            cur['clear_lines'].append((page, ln[2:]))
    return {'header': header, 'units': [u for u in units if u['groups'] or u['text']]}

def editor_substituted(path):
    """Line numbers + positions of groups inside [ ] (editor's substitution)."""
    out = []
    inside = False
    for ln_no, ln in enumerate(open(path, encoding='utf-8'), 1):
        if not ln.startswith('F '):
            continue
        for m in re.finditer(r'\[|\]|\d+\*?|\{[^}]*\}', ln[2:]):
            t = m.group(0)
            if t == '[': inside = True
            elif t == ']': inside = False
            elif inside and not t.startswith('{'): out.append((ln_no, t))
    return out
