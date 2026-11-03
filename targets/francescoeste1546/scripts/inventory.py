"""Ask an AI language-model agent for a sign inventory (shape names only, no values) from a sample sheet of cipher bands."""
import sys, base64
import os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from agent import ask
P = """This sheet shows cipher lines from an Italian letter of 1546 written in a cipher of invented signs (many look like Latin or Greek letters, digits or geometric marks). Ignore any ordinary cursive Italian words (in the strips or cut off at the top edge).
Make a SIGN INVENTORY for transcription: list every distinct cipher sign you can see, give each a short unique ASCII name (1-2 characters, preferably a look-alike letter or digit, e.g. 3, q, x, m, w, t, L for an inverted T, etc.) and a one-line shape description that lets a copyist tell it from similar signs. Note which signs are easy to confuse. Also list any marks (superscript digits above signs, dots, bars). Do NOT give any letter values or meanings; shapes only.
Rules: name every visible component separately (never merge two components into one ligature name; e.g. a small raised o joined to a following sign is its own sign o). Names must be plain ASCII. Output ONLY a compact markdown table: name | description (max 20 words) | confusable with. No prose."""
b64 = base64.b64encode(open(sys.argv[1], 'rb').read()).decode()
t, u = ask(P, image_b64=b64, max_tokens=8000)
open(sys.argv[2], 'w', encoding='utf8').write(t); print(u)
