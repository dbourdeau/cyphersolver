"""Image furniture for the site build: width and height on every <img> (so a page does not jump as its images load, and
an anchor lands where it should) and a srcset of the lighter copies in docs/thumbs/ where they exist.

The build is stdlib-only, so sizes are read from the file headers here. The copies are made by tools/make_thumbs.py,
which needs Pillow; a page simply serves the original until its copy exists. Originals stay where they are: the
deep-zoom viewer (zoom.js) opens them, not the copies.
"""
import json, pathlib, re, struct

HERE = pathlib.Path(__file__).parent
THUMBS = HERE / 'thumbs'
# what annotate() adds, removed flush by normalise() in _build_site.py so that adding it is not an edit of the page
ADDED = re.compile(r' width="\d+" height="\d+" decoding="async"| srcset="[^"]*" sizes="[^"]*"')
IMG = re.compile(r'(<figure class="hl-fig"[^>]*>\s*)?<img\b[^>]*>')

_sizes = {}

def size(path):
    """(width, height) of a PNG, JPEG, GIF or WebP from its header, or None."""
    path = pathlib.Path(path)
    if path in _sizes: return _sizes[path]
    out = None
    try:
        with path.open('rb') as f:
            head = f.read(32)
            if head[:8] == b'\x89PNG\r\n\x1a\n': out = struct.unpack('>II', head[16:24])
            elif head[:6] in (b'GIF87a', b'GIF89a'): out = struct.unpack('<HH', head[6:10])
            elif head[:4] == b'RIFF' and head[8:12] == b'WEBP':
                if head[12:16] == b'VP8 ': out = tuple(v & 0x3fff for v in struct.unpack('<HH', head[26:30]))
                elif head[12:16] == b'VP8L':
                    b = struct.unpack('<I', head[21:25])[0]; out = ((b & 0x3fff) + 1, ((b >> 14) & 0x3fff) + 1)
                elif head[12:16] == b'VP8X': out = (int.from_bytes(head[24:27], 'little') + 1, int.from_bytes(head[27:30], 'little') + 1)
            elif head[:2] == b'\xff\xd8':
                f.seek(2)
                while True:
                    b = f.read(1)
                    while b and b != b'\xff': b = f.read(1)
                    while b == b'\xff': b = f.read(1)
                    if not b: break
                    if b[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                        h, w = struct.unpack('>xHH', f.read(5)); out = (w, h); break
                    if b[0] in (0xD8, 0xD9, 0x01) or 0xD0 <= b[0] <= 0xD7: continue
                    f.seek(struct.unpack('>H', f.read(2))[0] - 2, 1)
    except (OSError, struct.error):
        out = None
    _sizes[path] = out
    return out

def _copies():
    """The copies made so far: {'name.jpg': {480: 'thumbs/name-480.webp', 960: ...}}, from thumbs/index.json."""
    try: idx = json.loads((THUMBS / 'index.json').read_text(encoding='utf-8'))
    except FileNotFoundError: return {}
    return {src: {int(w): f'thumbs/{pathlib.PurePosixPath(src).with_suffix("").as_posix()}-{w}.webp' for w in rec['w']}
            for src, rec in idx.items()}

COPIES = _copies()

def annotate(s, base=HERE):
    """Add width, height and srcset to the local images of a page. Idempotent; a hand-set width is left alone."""
    s = ADDED.sub('', s)
    def one(m):
        tag = m.group(0)
        src = re.search(r'\bsrc="([^"#?]+)"', tag)
        if not src or re.match(r'(?:https?:|data:|//)', src.group(1)): return tag
        name = src.group(1)
        wh = size(base / name)
        if not wh: return tag
        add = ''
        if not re.search(r'<img\b[^>]*\bwidth=', tag): add += f' width="{wh[0]}" height="{wh[1]}" decoding="async"'
        cp = COPIES.get(name)
        if cp:
            small = 'class="thumb"' in tag or 'class="sc"' in tag or 'hl-fig' in tag
            sizes = '96px' if 'class="sc"' in tag else '(max-width: 760px) 100vw, 420px' if small else '(max-width: 1000px) 100vw, 940px'
            add += ' srcset="' + ', '.join(f'{cp[w]} {w}w' for w in sorted(cp)) + f', {name} {wh[0]}w" sizes="{sizes}"'
        return tag.replace(f'src="{name}"', f'src="{name}"{add}', 1)
    return IMG.sub(one, s)
