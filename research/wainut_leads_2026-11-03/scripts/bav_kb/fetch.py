import sys, time, urllib.request, urllib.parse
UA = "WAINUT-research"
def get(url, accept=None):
    time.sleep(1.1)
    h = {"User-Agent": UA}
    if accept: h["Accept"] = accept
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:500]
    except Exception as e:
        return 0, str(e)
if __name__ == "__main__":
    s, b = get(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print("STATUS", s, len(b)); print(b[:int(sys.argv[3]) if len(sys.argv) > 3 else 3000])
