# Declared before any transcription result (19 Nov 2026, ~11:15 AEST)
- Key: targets/milan1494/aaymeloglu/key.json on upstream main, sha256 abf087fb7f1176113e58cceea3c0731686b7cbcc5e6b81a17ffc4c16004cc89a, unchanged. The key is the Milan embassy sheet MAP LXXII 183 (1494); applying it to Niccolini 1492-93 tests whether the same key served.
- Images: ASF IIP server via Malcolm's Chrome (Italy VPN), region crops of A0000183 (doc 42), A0000209 (49), A0000357 (81), A0000403 (90), md5 in FETCH_MD5.txt.
- Blind sheet: neutral labels S01-S67 with shape descriptions only (SHEET.tsv sha256 54bcf329...); mapping kept outside the packet.
- Blind reader: Claude Fable sub-agent, packet /tmp/nicc_blind only.
- One decode (decode_once.py). Separate strict judge, word units S / E / N, per letter. Our line: 65% strict per letter.
- Shuffle control on every letter that passes: shuffle.py, 5,000 at seeds 20261112 and 7; pass needs < 5/5000 at both.
- Expectation stated now: d49, d81, d90 are one line each; the control is likely to fail on them as on the short Petkum passages.
- The main chat (not blind) captured and viewed the images and knows the key; it does not transcribe.
