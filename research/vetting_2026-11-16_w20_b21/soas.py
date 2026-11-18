"""SOAS archive catalogue (archives.soas.ac.uk/records/<ref with _ for spaces>) record text. Usage: soas.py REF ..."""
import re, sys, html, time, urllib.request
for ref in sys.argv[1:]:
    u = 'https://archives.soas.ac.uk/records/' + ref.replace(' ', '_')
    try:
        t = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}), timeout=40).read().decode('utf8', 'replace')
        t = re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', t)
        t = ' '.join(html.unescape(re.sub('<[^>]+>', ' ', t)).split())
        t = t.split(' Session inactive')[0]
    except Exception as e:
        t = 'ERR ' + str(e)
    print(ref, '|', t[:600], flush=True)
    time.sleep(1.1)
