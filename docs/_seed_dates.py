"""Seed docs/_dates.json from the git history, once.

For every page it walks the commits that touched the file, normalises each historical version the same way
_build_site.py does (nav, footer, contents strip, dateline and version stamps removed) and hashes it. The first
commit gives the day the finding landed; the last commit whose normalised body differs from its predecessor gives
the day the page last really changed, so the routine site rebuilds that restamp every file do not count. Entries
in "Recent findings" on index.html are dated the same way, by the commit that first introduced each one.

Run once:  python _seed_dates.py        After that _build_site.py keeps the file up to date on every build.
Re-running is safe: dates already in the file are kept, only missing ones are filled in.
"""
import subprocess, sys, pathlib, json, re

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import _build_site as B


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def history(relpath):
    """(sha, YYYY-MM-DD) for every commit that touched the file, oldest first."""
    out = git('log', '--reverse', '--format=%H %ad', '--date=short', '--', relpath)
    return [tuple(line.split(' ', 1)) for line in out.splitlines() if line.strip()]


def blobs(specs):
    """Read many `sha:path` blobs in one git call; missing ones come back as None."""
    proc = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT,
                          input=('\n'.join(specs) + '\n').encode('utf-8'), capture_output=True)
    out, pos, result = proc.stdout, 0, []
    for _ in specs:
        end = out.index(b'\n', pos)
        header = out[pos:end].decode('utf-8', 'replace').split()
        pos = end + 1
        if len(header) < 3:                      # "<spec> missing"
            result.append(None); continue
        size = int(header[2])
        result.append(out[pos:pos + size].decode('utf-8', 'replace'))
        pos += size + 1
    return result


def findings_keys(page):
    m = re.search(r'<h2 id="recent">.*?(?=\n<h2|\n<!-- |\Z)', page, re.S)
    if not m: return []
    return [B.finding_key(li) for li in re.findall(r'<li>.*?</li>', m.group(0), re.S)]


def main():
    dates = B.load_dates()
    pages, findings = dates.setdefault('pages', {}), dates.setdefault('findings', {})
    for path in sorted(HERE.glob('*.html')):
        rel = f'docs/{path.name}'
        hist = history(rel)
        if not hist:
            print(f'{path.stem:14} no history, dated today'); continue
        versions = blobs([f'{sha}:{rel}' for sha, _ in hist])
        first = updated = hist[0][1]
        prev = None
        for (sha, day), text in zip(hist, versions):
            if text is None: continue
            h = B.content_hash(text)
            if prev is not None and h != prev: updated = day
            prev = h
        rec = pages.setdefault(path.stem, {})
        rec.setdefault('first', first)
        rec.setdefault('updated', updated)
        rec['hash'] = B.content_hash(path.read_text(encoding='utf-8'))
        if path.stem in ('index', 'findings'):     # the list moved from index.html to findings.html on 5 Nov 2026
            for (sha, day), text in zip(hist, versions):
                if text is None: continue
                for key in findings_keys(text): findings.setdefault(key, day)
        print(f'{path.stem:14} first {rec["first"]}  updated {rec["updated"]}  ({len(hist)} commits)')
    B.save_dates(dates)
    print(f'\nwrote {B.DATES_PATH.name}: {len(pages)} pages, {len(findings)} findings')


if __name__ == '__main__':
    main()
