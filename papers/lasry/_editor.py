"""A local editor for the paper: edit its source in place, and highlight passages to leave instructions for an LLM.

  python papers/lasry/_editor.py                 serves http://127.0.0.1:48731 (open it in a browser)
  python papers/lasry/_editor.py --list          prints the open requests, for pasting to an LLM
  python papers/lasry/_editor.py --done 3 4      marks requests 3 and 4 done
  python papers/lasry/_editor.py --tex llm-ciphers.tex --port 48731 --tectonic path/to/tectonic

What it does
  Edit      the paper source (llm-ciphers.tex) as blocks; click a block, change it, Save. A backup of the whole file
            goes to _editor_backup/ before every save, and a save is refused if the block changed on disk meanwhile
            (so it is safe to leave open while an LLM edits the file).
  Highlight select text in a block: "Ask the LLM" stores your instruction with the quoted passage in
            editor_notes.json; "Just mark" stores a highlight with no instruction. Notes follow the quoted text
            when the paragraph moves. Tell the LLM: "do the open requests in papers/lasry/editor_notes.json"
            (or run --list). It marks each done with --done when finished; reload to see them.
  Preview   Build runs tectonic on the paper (submission or camera-ready) and shows the PDF beside the source.

Numbers: the \\N... macros come from generated/macros.tex (rerun _analysis.py to refresh); the editor never writes
anything under generated/. Only the one .tex file is editable. The server listens on 127.0.0.1 only.
"""
import argparse, hashlib, http.server, json, os, pathlib, re, shutil, subprocess, sys, threading, time, urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
NOTES = HERE / 'editor_notes.json'
BACKUPS = HERE / '_editor_backup'
LOCK = threading.Lock()
LOCAL = HERE / '.tools' / 'tectonic.exe'
CFG = {'tex': HERE / 'llm-ciphers.tex', 'tectonic': shutil.which('tectonic') or (str(LOCAL) if LOCAL.exists() else 'tectonic')}


def sha(s): return hashlib.sha1(s.encode('utf-8')).hexdigest()[:12]


def read_lines():
    return CFG['tex'].read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')


def blocks(lines):
    """Blocks of consecutive non-blank lines: [{start, end (exclusive), text, hash, kind}]."""
    out, i = [], 0
    while i < len(lines):
        if not lines[i].strip(): i += 1; continue
        j = i
        while j < len(lines) and lines[j].strip(): j += 1
        text = '\n'.join(lines[i:j])
        first = lines[i].lstrip()
        kind = ('section' if first.startswith((r'\section', r'\subsection')) else
                'comment' if all(l.lstrip().startswith('%') for l in lines[i:j]) else 'text')
        out.append({'start': i, 'end': j, 'text': text, 'hash': sha(text), 'kind': kind})
        i = j
    return out


def load_notes():
    try: return json.loads(NOTES.read_text(encoding='utf-8'))
    except Exception: return {'next': 1, 'notes': []}


def save_notes(d): NOTES.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')


def locate(note, text):
    """Index of the note's quote in the whole source, or -1 when the passage has changed."""
    return text.find(note['quote']) if note.get('quote') else -1


def api(method, path, body):
    q = urllib.parse.urlparse(path)
    p = q.path
    with LOCK:
        if p == '/api/doc':
            lines = read_lines()
            bl = blocks(lines)
            src = '\n'.join(lines)
            d = load_notes()
            for n in d['notes']:
                n['found'] = locate(n, src) >= 0
            return {'file': CFG['tex'].name, 'blocks': bl, 'notes': d['notes'], 'mtime': CFG['tex'].stat().st_mtime}
        if p == '/api/save' and method == 'POST':
            lines = read_lines()
            cur = '\n'.join(lines[body['start']:body['end']])
            if sha(cur) != body['hash']:
                return {'error': 'The block changed on disk since you opened it. Reload to see the new text.'}, 409
            BACKUPS.mkdir(exist_ok=True)
            shutil.copy2(CFG['tex'], BACKUPS / (time.strftime('%Y%m%d-%H%M%S-') + CFG['tex'].name))
            new = body['text'].replace('\r\n', '\n').split('\n')
            lines[body['start']:body['end']] = new
            tmp = CFG['tex'].with_suffix('.tex.tmp')
            tmp.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
            os.replace(tmp, CFG['tex'])
            return {'ok': True}
        if p == '/api/note' and method == 'POST':
            d = load_notes()
            n = {'id': d['next'], 'quote': body['quote'], 'instruction': body.get('instruction', '').strip(),
                 'status': 'open' if body.get('instruction', '').strip() else 'mark', 'section': body.get('section', ''),
                 'created': time.strftime('%Y-%m-%d %H:%M')}
            d['next'] += 1; d['notes'].append(n); save_notes(d)
            return n
        if p == '/api/note_update' and method == 'POST':
            d = load_notes()
            for n in d['notes']:
                if n['id'] == body['id']:
                    for k in ('instruction', 'status'):
                        if k in body: n[k] = body[k]
                    if 'instruction' in body and n['status'] == 'mark' and body['instruction'].strip(): n['status'] = 'open'
            if body.get('delete'): d['notes'] = [n for n in d['notes'] if n['id'] != body['id']]
            save_notes(d)
            return {'ok': True}
        if p == '/api/build' and method == 'POST':
            tex = 'llm-ciphers-camera.tex' if body.get('camera') else CFG['tex'].name
            t0 = time.time()
            try:
                r = subprocess.run([str(CFG['tectonic']), tex], cwd=HERE, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=240)
                log = (r.stdout + r.stderr)
                err = [l for l in log.split('\n') if (l.startswith('!') or 'error:' in l or 'undefined' in l.lower()) and 'Fontconfig' not in l]
                return {'ok': r.returncode == 0, 'seconds': round(time.time() - t0, 1), 'errors': err[:12], 'pdf': tex.replace('.tex', '.pdf'), 'log': log[-3000:]}
            except FileNotFoundError:
                return {'ok': False, 'errors': ['tectonic not found. Start the editor with --tectonic <path>, or put tectonic.exe on PATH or in papers/lasry/.tools/.'], 'log': ''}
            except subprocess.TimeoutExpired:
                return {'ok': False, 'errors': ['Build timed out after 240 s.'], 'log': ''}
    return {'error': 'not found'}, 404


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send(self, code, body, ctype='application/json'):
        b = body if isinstance(body, bytes) else (json.dumps(body, ensure_ascii=False).encode('utf-8') if ctype == 'application/json' else body.encode('utf-8'))
        self.send_response(code); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(b)))
        self.send_header('Cache-Control', 'no-store'); self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        p = urllib.parse.urlparse(self.path).path
        if p == '/': return self.send(200, (HERE / '_editor.html').read_bytes(), 'text/html; charset=utf-8')
        if p.startswith('/pdf/'):
            f = HERE / pathlib.PurePosixPath(urllib.parse.unquote(p[5:])).name
            if f.suffix == '.pdf' and f.exists(): return self.send(200, f.read_bytes(), 'application/pdf')
            return self.send(404, {'error': 'no pdf yet; press Build'})
        r = api('GET', self.path, None)
        self.send(*((r[1], r[0]) if isinstance(r, tuple) else (200, r)))

    def do_POST(self):
        n = int(self.headers.get('Content-Length') or 0)
        body = json.loads(self.rfile.read(n) or b'{}')
        r = api('POST', self.path, body)
        self.send(*((r[1], r[0]) if isinstance(r, tuple) else (200, r)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tex', default='llm-ciphers.tex'); ap.add_argument('--port', type=int, default=48731)
    ap.add_argument('--tectonic'); ap.add_argument('--list', action='store_true'); ap.add_argument('--done', nargs='*', type=int)
    a = ap.parse_args()
    CFG['tex'] = HERE / a.tex
    if a.tectonic: CFG['tectonic'] = a.tectonic
    if a.list:
        d = load_notes(); src = '\n'.join(read_lines()); opn = [n for n in d['notes'] if n['status'] == 'open']
        print(f'{len(opn)} open request(s) on {CFG["tex"].name}:\n')
        for n in opn:
            print(f'#{n["id"]} [{n.get("section") or "?"}] {"" if locate(n, src) >= 0 else "(passage changed since: search by meaning) "}')
            print(f'  passage: {n["quote"]!r}\n  instruction: {n["instruction"]}\n')
        return
    if a.done is not None:
        d = load_notes()
        for n in d['notes']:
            if n['id'] in a.done: n['status'] = 'done'
        save_notes(d); print('marked done:', a.done); return
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', a.port), H)
    print(f'Paper editor on http://127.0.0.1:{a.port}  (editing {CFG["tex"].name}; Ctrl+C to stop)')
    try: srv.serve_forever()
    except KeyboardInterrupt: pass


if __name__ == '__main__':
    main()
