# Build reading_<doc>.md from work/marked/<doc>.txt: a sentence text (marks resolved to the reading side) and the
# marked block that scripts/reading.py checks.  python scripts/make_reading.py <folder> <doc> "<title>" "<note>"
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
R = pathlib.Path(__file__).resolve().parent.parent
fold, doc, title, note = sys.argv[1:5]
BREAK = set(sys.argv[5].split(',')) if len(sys.argv) > 5 else set()  # labels after which clear text was left out
lines = [l for l in (R / 'work' / 'marked' / f'{doc}.txt').read_text(encoding='utf-8').splitlines() if l.strip()]
def side(t):
    t = re.sub(r'\{([^{}/]*)/([^{}]*)\}', lambda m: m.group(2), t)
    t = re.sub(r'\{\+([^{}]*)\}', lambda m: m.group(1), t)
    return re.sub(r'\[\?([^\]\d.][^\]]*)\]', lambda m: m.group(1), t)
text = ''
for l in lines:
    lab = l.split('|', 1)[0].strip(); t = side(l.split('|', 1)[1].strip())
    if lab in BREAK: text = (text + ' [... clear text not edited ...]\n\n') if text else text
    if text.endswith('-'): text = text[:-1] + t
    else: text += ('' if (not text or text.endswith('\n')) else ' ') + t
md = (f'# {title}\n\n{note}\n\nMarks in the block below: `{{x/y}}` mechanical x read as y; `{{+a}}` added letter; `[?word]` guess; '
      '`{[...]/abc}` letters lost in the binding, filled from context (counted as a guess); `{[...]/}` a line end in the binding '
      'where nothing is lost (the word runs on to the next line; counted as a repair); `[...]` hole; `[51]` number not '
      'in the key (a code word). Everything else is the mechanical decryption of `transcription_' + doc + '.txt` with `key.tsv`, '
      're-spaced; clear words are copied. `uu` (3.3) is written w.\n\n## Text (original spelling, re-spaced and punctuated)\n\n'
      + text + '\n\n## Marked reading (line by line)\n\n```marked\n' + '\n'.join(lines) + '\n```\n')
(R / fold / f'reading_{doc}.md').write_text(md, encoding='utf-8')
(R / 'work' / f'text_{doc}.txt').write_text(text + '\n', encoding='utf-8')
