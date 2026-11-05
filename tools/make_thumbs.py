"""Make the lighter copies of the site's images in docs/thumbs/: run before the build, on any machine with Pillow.

A copy is a WebP, 480 px wide for an image shown small (a card, a list row, a highlight) and 960 px wide for a large
one shown in a page. _images.py lists them in a srcset beside the original, which stays where it is for the deep-zoom
viewer. thumbs/index.json records each source's hash, so an unchanged image is not made again and a removed one loses
its copies. Without Pillow the script says so and exits cleanly: the site serves the originals until someone runs it.

    python tools/make_thumbs.py
"""
import hashlib, json, pathlib, re, sys

DOCS = pathlib.Path(__file__).resolve().parent.parent / 'docs'
THUMBS = DOCS / 'thumbs'
INDEX = THUMBS / 'index.json'
EXT = ('.jpg', '.jpeg', '.png')
SMALL_MIN = 40_000      # bytes: a smaller image is not worth a small copy
LARGE_MIN = 150_000     # bytes: likewise for the 960-px copy
QUALITY = 76

def used_images():
    """{image: shown small?} for every local image on the top-level pages."""
    out = {}
    for page in DOCS.glob('*.html'):
        s = page.read_text(encoding='utf-8', errors='replace')
        for m in re.finditer(r'(<figure class="hl-fig"[^>]*>\s*)?<img\b[^>]*>', s):
            src = re.search(r'\bsrc="([^"#?]+)"', m.group(0))
            if not src or re.match(r'(?:https?:|data:|//)', src.group(1)) or not src.group(1).lower().endswith(EXT): continue
            small = bool(m.group(1)) or 'class="thumb"' in m.group(0) or 'class="sc"' in m.group(0)
            out[src.group(1)] = out.get(src.group(1), False) or small
    return out

def main():
    try:
        from PIL import Image
    except ImportError:
        print('make_thumbs: Pillow is not installed; the site keeps serving the originals')
        return 0
    old = json.loads(INDEX.read_text(encoding='utf-8')) if INDEX.exists() else {}
    new, made = {}, 0
    for name, small in sorted(used_images().items()):
        src = DOCS / name
        if not src.is_file(): continue
        raw = src.read_bytes()
        digest = hashlib.sha1(raw).hexdigest()[:12]
        with Image.open(src) as im:
            width = im.width
            want = [w for w, ok in ((480, small and len(raw) > SMALL_MIN and width > 600), (960, len(raw) > LARGE_MIN and width > 1100)) if ok]
            if not want: continue
            new[name] = {'hash': digest, 'w': want}
            stem = pathlib.PurePosixPath(name).with_suffix('').as_posix()
            for w in want:
                out = THUMBS / f'{stem}-{w}.webp'
                if out.exists() and old.get(name, {}).get('hash') == digest: continue
                out.parent.mkdir(parents=True, exist_ok=True)
                copy = im.convert('RGB').resize((w, round(im.height * w / width)), Image.LANCZOS)
                copy.save(out, 'WEBP', quality=QUALITY, method=6)
                made += 1
    for name, rec in old.items():          # copies of removed or changed images
        stem = pathlib.PurePosixPath(name).with_suffix('').as_posix()
        for w in rec['w']:
            if w not in new.get(name, {}).get('w', []):
                (THUMBS / f'{stem}-{w}.webp').unlink(missing_ok=True)
    THUMBS.mkdir(exist_ok=True)
    INDEX.write_text(json.dumps(new, indent=0, sort_keys=True) + '\n', encoding='utf-8')
    total = sum(p.stat().st_size for p in THUMBS.rglob('*.webp'))
    print(f'make_thumbs: {made} new copies; {len(new)} images have copies, {total / 1048576:.1f} MB in all')
    return 0

if __name__ == '__main__':
    sys.exit(main())
