"""Download the Internet Archive OCR of Kervyn de Lettenhove, Relations politiques IX (1886), to kervyn9_djvu.txt
and check its SHA-256 against the one frozen in verification/MANIFEST_v1.sha256."""
import hashlib, urllib.request
URL = 'https://archive.org/download/relationspolitiq09nethuoft/relationspolitiq09nethuoft_djvu.txt'
SHA = 'fc0a16f0fd7011eef8b45d777d8444a0956e795f132e8e0730960d38af7c74e3'
data = urllib.request.urlopen(URL).read()
assert hashlib.sha256(data).hexdigest() == SHA, 'not the frozen file'
open('kervyn9_djvu.txt', 'wb').write(data); print('ok', len(data))
