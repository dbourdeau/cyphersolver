"""Blind second sign pass for c. 13r: an AI language-model agent copies each cipher line by sign names from a legend of shapes.
It gets no values, no translation, no key. Output validation/pass2_raw.txt (+ full replies)."""
import sys, os, io, base64
# ask(prompt, image_b64=..., max_tokens=...) -> (reply_text, usage): a thin client for an AI language-model API
# that accepts an image. It is not part of this folder; supply your own.
def ask(prompt, image_b64, max_tokens):
    raise NotImplementedError('model client not included')

from PIL import Image, ImageOps

CENTRES = [190, 378, 552, 743, 939, 1121, 1309, 1489, 1698, 1907]
LEGEND = """Sign names to use (shapes only):
n u c a o g h k r v t L N : the letter shapes as they look ('L' = capital L with a loop; 'N' = capital N)
& : a looped sign like an ampersand or a Greek alpha
e : a Greek epsilon (reversed 3, open to the right)
q : a q-like sign whose stem ends in a loop or tail
9 : a 9-shape: a round head and a straight stem, no closed lower loop (g has a closed lower loop)
f : long s without a crossbar;  F : an f with a crossbar
1 : a plain vertical stroke
j : a d-like sign whose ascender curls back to the LEFT like a hook;  j' : the same with a dot above
d : an ordinary d with a looped ascender
D : a delta-like sign: round body, ascender curling to the RIGHT
# : two vertical strokes crossed by two short bars (like 4 and l crossed, or a double dagger)
T : a 3 with a cross or dagger standing above it;  + : a plain cross
X : an x-like sign with a dot above
Z : an x-like sign with a long horizontal tail to the right
8 : an x-like sign or lying 8 with a closed loop, no tail and no dot
w : an omega-like double loop
Dotted letters: n. (n with a dot below), a. (a with a dot below), o. (o with a dot below), o' (o with a dot above), u' (u with a dot or dots above)
Punctuation as on the line: ,  /  .  :
Words in ordinary Italian handwriting: copy them in square brackets, e.g. [Hora]."""
PROMPT = ("This image shows ONE line of a 16th-century cipher, cut in two halves stacked top to bottom (they overlap by a "
          "few signs: do not repeat them). Copy the signs left to right using only the names below, separated by single "
          "spaces. Write ? for a sign you cannot match. Ignore cut-off fragments of the lines above and below. This is a "
          "shape copy only: do not try to decipher.\n\n" + LEGEND + "\n\nGive the sign sequence on the LAST line of your reply, nothing after it.")


def band(im, c, hh=85):
    W = im.width
    parts = [im.crop((0, c - hh, W // 2 + 120, c + hh)), im.crop((W // 2 - 120, c - hh, W, c + hh))]
    out = Image.new('L', (parts[0].width, 2 * (2 * hh) + 10), 255)
    out.paste(parts[0], (0, 0)); out.paste(parts[1], (0, 2 * hh + 10))
    out = ImageOps.autocontrast(out, cutoff=1).resize((int(out.width * 0.62), int(out.height * 0.62)), Image.LANCZOS)
    b = io.BytesIO(); out.convert('RGB').save(b, 'JPEG', quality=92)
    return base64.b64encode(b.getvalue()).decode()


def main():
    im = Image.open('scans/c13r_cipher.jpg').convert('L'); res = []
    os.makedirs('validation', exist_ok=True)
    for i, c in enumerate(CENTRES):
        txt, u = ask(PROMPT, image_b64=band(im, c), max_tokens=3000)
        open(f'validation/pass2_full_M{i+1:02d}.txt', 'w', encoding='utf-8').write(txt)
        lines = [l for l in txt.strip().splitlines() if l.strip()]
        res.append(f'M{i+1:02d}\t' + (lines[-1].strip('` ') if lines else ''))
        print(res[-1].encode('ascii', 'replace').decode(), u, flush=True)
    open('validation/pass2_raw.txt', 'w', encoding='utf-8').write('\n'.join(res) + '\n')


main()
