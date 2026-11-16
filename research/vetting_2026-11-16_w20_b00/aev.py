"""AEV (Archives de l'Etat du Valais) scopequery: SRU lookup by reference, then the detail page text."""
import sys, time, re, html, urllib.request, urllib.parse
UA = {'User-Agent': 'Mozilla/5.0'}
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40)
    return r.read().decode('utf-8', 'replace')
def sru(q, n=20):
    u = 'https://scopequery.vs.ch/SRU/?operation=searchRetrieve&version=1.2&maximumRecords=%d&query=%s' % (n, urllib.parse.quote(q))
    return get(u)
def text(h):
    h = re.sub(r'(?s)<script.*?</script>|<style.*?</style>', ' ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(h))
if __name__ == '__main__':
    for q in sys.argv[1:]:
        x = sru(q)
        refs = re.findall(r'<isad:reference>(.*?)</isad:reference>.*?<isad:title>(.*?)</isad:title>.*?<isad:date>(.*?)</isad:date>.*?<ap:link[^>]*>(.*?)</ap:link>', x, re.S)
        print('##', q, len(refs))
        for r in refs:
            print(' |'.join(html.unescape(s) for s in r))
        time.sleep(1)
