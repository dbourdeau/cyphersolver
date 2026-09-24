"""Outcome method: the one vocabulary for how a target's text was obtained, shared by the site build, the checkers
and the classifier. The categories are George Lasry's (email 21 Sept 2026) plus "read from existing decipherment";
the full definitions live in profile.schema.json (outcome.method) and on docs/glossary.html.

Extent is kept apart from method: how much of the text was obtained (profile outcome.class), shown as complete or
partial. The words "solved" and "read" are no longer used as outcome labels, because they mixed the two.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

CT = 'key recovered from ciphertext-only'
EXT_PT = 'key recovered based on plaintext from external sources'
ADJ_PT = 'key recovered based on adjacent plaintext'
EXT_KEY = 'read after matching with key from external sources'
KNOWN = 'read with known key'
DECIPH = 'read from existing decipherment'
NOT = 'not solved'
NA = 'not applicable'
METHODS = [CT, EXT_PT, ADJ_PT, EXT_KEY, KNOWN, DECIPH, NOT, NA]
KEY_RECOVERED = {CT, EXT_PT, ADJ_PT}            # the key was rebuilt here (cryptanalysis); the rest applied one

# method -> (filter/anchor key, badge label, seal word, dateline verb)
INFO = {
    CT:      ('ct',      'ciphertext-only break',        'ciphertext-only', 'key recovered'),
    EXT_PT:  ('extpt',   'key from external plaintext',  'external text',   'key recovered'),
    ADJ_PT:  ('adjpt',   'key from adjacent plaintext',  'adjacent text',   'key recovered'),
    EXT_KEY: ('extkey',  'external key matched',         'key matched',     'deciphered'),
    KNOWN:   ('known',   'known key applied',            'known key',       'deciphered'),
    DECIPH:  ('deciph',  'existing decipherment',        'deciphered copy', 'transcribed'),
    NOT:     ('notsolved', 'not solved',                 'not solved',      'attempted'),
    NA:      ('na',      'not applicable',               'closed',          'resolved'),
}
KEY = {m: v[0] for m, v in INFO.items()}
LABEL = {m: v[1] for m, v in INFO.items()}

# the definitions shown on glossary.html and in README Conventions
DEFINE = {
    CT: 'The key was rebuilt from the ciphertext alone: frequencies, solvers, pattern words, the order of the key. '
        'No plaintext and no existing key was used. If someone had solved the same text earlier and it was found only '
        'afterwards, the write-up says so: an independent re-solution.',
    EXT_PT: 'The key was rebuilt by matching the ciphertext against a plaintext found elsewhere: a printed edition, a '
            'calendar of state papers, a copy of the same letter in another archive.',
    ADJ_PT: 'The key was rebuilt from plaintext next to the ciphertext: a partial decipherment written between the lines '
            'or in the margin, clear passages in the same letter, a deciphered copy in the same file.',
    EXT_KEY: 'An existing key that had not been connected with this document (a key for another correspondent or series, '
             'a key sheet filed elsewhere) was found to fit, and applied.',
    KNOWN: 'The key was already identified for this document or its correspondence (on its archive or DECODE record, '
           'published for it, filed with it) and was applied. The work is transcription and decipherment, which is '
           'not mechanical when the key is polyphonic or variable-length.',
    DECIPH: 'A complete decipherment already existed (between the lines, on a separate copy, or in print). The work was '
            'transcribing the cipher and checking the decipherment against it.',
    NOT: 'Attempted; the text was not obtained. What was learned is recorded.',
    NA: 'Not a cipher (clear text, shorthand, a key sheet, instructions), or the item could not be reached.',
}

def extent(prof):
    """'complete', 'partial', 'none' or 'n/a' from outcome.class."""
    cls = (prof.get('outcome') or {}).get('class')
    return {'read': 'complete', 'already solved': 'complete', 'read in part': 'partial',
            'not read': 'none'}.get(cls, 'n/a')

def status_class(method, ext):
    """The badge colour class the site already styles: solved (green), partial, stuck, found."""
    if method == NOT: return 'stuck'
    if method == NA: return 'found'
    return 'solved' if ext == 'complete' else 'partial'

def badge(method, ext, cls=None):
    if method == NA: return 'offline only' if cls == 'offline only' else 'not a cipher' if cls == 'not a cipher' else LABEL[NA]
    return LABEL[method] + (' &middot; partial' if ext == 'partial' else '')

def profile_paths():
    """{folder name (lower case): profile.json path}, nested sweep folders included."""
    out = {}
    for p in sorted(ROOT.glob('*/*/profile.json')) + sorted(ROOT.glob('*/profile.json')):
        out[p.parent.name.lower()] = p          # top-level folders win over nested ones of the same name
    return out

def load(path):
    try: return json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    except (OSError, ValueError): return None

# the cryptologic terms the write-ups use, in the sense they carry there (glossary.html)
TERMS = [
    ('cipher', 'Cipher and code', 'A cipher replaces letters or syllables with symbols. A code replaces whole words or names with '
     'groups taken from a list (a codebook). Most early-modern diplomatic keys mix the two.'),
    ('nomenclator', 'Nomenclator', 'The usual early-modern key: a cipher alphabet, often homophonic, plus a list of code groups for '
     'names, titles and common words, and sometimes nulls.'),
    ('substitution', 'Simple substitution', 'Each plaintext letter always becomes the same one symbol.'),
    ('homophonic', 'Homophonic', 'A plaintext letter can be written with any of several symbols (its homophones), to flatten the '
     'letter frequencies. Decryption is still unambiguous.'),
    ('polyphonic', 'Polyphonic', 'One symbol stands for more than one plaintext letter. Decryption is ambiguous: the reader chooses '
     'the value that makes sense, so applying even a known key takes judgement.'),
    ('variable-length', 'Variable-length', 'Cipher units of different lengths (for example one- and two-digit numbers) are written '
     'without separators, so the text has to be divided into units before it can be decrypted, and several divisions may be possible.'),
    ('null', 'Null', 'A symbol that means nothing, added to disturb frequency analysis.'),
    ('key', 'Key', 'The table that gives the plaintext value of every cipher symbol and code group.'),
    ('plaintext', 'Plaintext, ciphertext, cleartext', 'Plaintext is the message the cipher hides; ciphertext is the enciphered form. '
     'Cleartext is the part of a document that was written openly, not enciphered, often around the ciphered passages.'),
    ('decipherment', 'Decipherment', 'Plaintext obtained from ciphertext. A contemporary decipherment was made at the time, by the '
     'recipient\'s clerk, and is often written between the lines (interlinear) or on a separate sheet.'),
    ('cryptanalysis', 'Cryptanalysis (a break)', 'Recovering an unknown key from the material. The three routes used here are '
     'ciphertext-only, from adjacent plaintext and from external plaintext (see the methods above).'),
    ('crib', 'Crib', 'A guessed or known piece of plaintext placed against the ciphertext to recover part of the key.'),
    ('transcription', 'Transcription', 'Copying the cipher symbols from the image into text a program can read. Symbols that are not '
     'letters or digits have to be given labels first; misreadings here look like errors in the key.'),
    ('extent', 'Extent: complete or partial', 'Complete means at least 95% of the cipher symbols give sense, every document is '
     'covered, and what stays open is scattered code groups or pieces blocked from outside (illegible, too short). Anything less is partial.'),
    ('prior', 'Prior solution', 'Whether a decipherment or key existed anywhere before this project worked on the item, and when it '
     'was found. It is recorded for every target because a model may have seen it.'),
    ('decode', 'DECODE', 'The online database of historical cipher documents and keys (Megyesi et al.); record numbers are cited as R1234.'),
]

# README Results: one table per method, in this order (headings are matched by prefix)
SECTION = {
    CT: '### Key recovered from ciphertext-only',
    EXT_PT: '### Key recovered based on plaintext from external sources',
    ADJ_PT: '### Key recovered based on adjacent plaintext',
    EXT_KEY: '### Read after matching with key from external sources',
    KNOWN: '### Read with known key',
    DECIPH: '### Read from existing decipherment',
    NOT: '### Not solved',
    NA: '### Not applicable',
}
SECTION_NOTE = {
    CT: 'Key rebuilt here from the ciphertext alone. Independent re-solutions of items solved elsewhere are marked.',
    EXT_PT: 'Key rebuilt by matching the ciphertext against a plaintext found elsewhere (an edition, a calendar, a copy in another archive).',
    ADJ_PT: 'Key rebuilt from plaintext beside the ciphertext: a partial interlinear or marginal decipherment, clear passages, a deciphered copy in the same file.',
    EXT_KEY: 'An existing key not previously tied to the document was found to fit and applied.',
    KNOWN: 'The key was already identified for the document or its correspondence and was applied.',
    DECIPH: 'A complete decipherment already existed; the work was transcription and checking.',
    NOT: 'Attempted, text not obtained; the notes say why the work stops.',
    NA: 'Not a cipher, or the item could not be reached.',
}
def section_of(heading):
    """The method whose README section a '### ' heading opens, or None."""
    return next((m for m, h in SECTION.items() if heading.startswith(h)), None)
