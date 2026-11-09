"""Rök (Ög 136): decode the three cipher layers from transcription.txt and check them against the stone's own cleartext.
Run: python targets/rok800/decode_layers.py   (writes layers_report.txt next to it)"""
import re, sys, difflib, pathlib
HERE = pathlib.Path(__file__).parent
uni = '\n'.join(l for l in (HERE/'transcription.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#'))
lat = '\n'.join(l for l in (HERE/'decryption.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#'))
YF = "fuþąrkhniastbmlʀ"                      # the 16-rune Younger Futhark row
G = {'ᚠ':'f','ᚢ':'u','ᚦ':'þ','ᚭ':'ą','ᚱ':'r','ᚴ':'k','ᚽ':'h','ᚼ':'h','ᚿ':'n','ᚾ':'n','ᛁ':'i','ᛆ':'a','ᛌ':'s','ᛋ':'s',
     'ᛐ':'t','ᛓ':'b','ᛙ':'m','ᛘ':'m','ᛚ':'l','ᛦ':'ʀ','ᛧ':'ʀ'}
TW = {3: "fuþąrk", 2: "hniast", 1: "tbmlʀ"}     # twig-rune rows; aett counted from the right
clean = lambda s: re.sub(r"[\s¶|᛭·×=\(\)\[\]\-\.]", '', s)
out = []; P = out.append

# 1. coordinate cipher [a:b]
pairs = set(re.findall(r"\[(\d):(\d) = (.)\]", uni)); bad = 0
for a, b, g in sorted(pairs):
    ok = TW[int(a)][int(b)-1] == G[g]; bad += not ok
P(f"1. coordinate cipher: {len(pairs)} distinct codes, {bad} disagree with the stone's own resolution")
tail = uni.split("᛭ ")[-1]
dec = lambda m: TW[int(m.group(1))][int(m.group(2))-1]
tail = re.sub(r"\(?\[(\d):(\d) = .\]\)?", dec, tail)
P("   coordinate-only lines: " + re.sub(r"\s+", " ", tail.replace('¶', '/')))

# 2. next-rune shift cipher: search all 16 shifts, score by 4-grams shared with the cleartext of the same stone
main = clean(uni.split("ᛋᛃᚷᚹ")[0]); mt = ''.join(G.get(c, '?') for c in main)
grams = lambda s, n=4: {s[i:i+n] for i in range(len(s)-n+1)}
base = grams(mt)
long_ = "airfbfrbnhnfinbantfąnhnu"
sc = sorted(((len(grams(''.join(YF[(YF.index(x)+k) % 16] for x in long_)) & base), k) for k in range(16)), reverse=True)
P(f"2. shift cipher, 24-rune string: best shift {sc[0][1]} (score {sc[0][0]}), runner-up {sc[1]}")
P("   " + ''.join(YF[(YF.index(x)+sc[0][1]) % 16] for x in long_))
P("   8-rune string with the same shift: " + ''.join(YF[(YF.index(x)+sc[0][1]) % 16] for x in "rhfþrhis"))

# 3. Elder Futhark layer: key from the crib 'sakum mukmini þat' (it stands in the main text), rest by unchanged runes
seg = "ᛋᛃᚷᚹᛗᛟᚷᛗᛖᚿᛇᚦᛃᛞᚺᛟᛃᛦᛇᚷᛟᛚᛞᚷᛃᛟᛃᛦᛇᚷᛟᛚᛞᛁᚿᛞᚷᛟᚭᚿᛃᛦᚺᛟᛋᛚᛇ"
crib = "sakumukmini" + "þat"
P(f"3. Elder layer: crib in main text: {'sakumukminiþat' in mt}")
key = {}
for r, p in zip(seg, crib): key.setdefault(r, set()).add(p)
P("   key from the crib: " + ' '.join(f"{r}={''.join(sorted(v))}" for r, v in key.items()))
ident = {'ᚺ':'h','ᛦ':'ʀ','ᛚ':'l','ᚭ':'ą','ᛋ':'s','ᛗ':'m','ᚿ':'n','ᚦ':'þ','ᛁ':'i'}
vow = {'ᛃ':'a','ᛟ':'u','ᚹ':'u','ᛖ':'i','ᛇ':'i','ᚷ':'k/g','ᛞ':'t/d'}
P("   remaining 33 runes: " + ''.join(ident.get(c) or vow[c] for c in seg[14:]))

# 4. main text against the published transliteration
L = clean(''.join(lat.split(chr(10)*2)[:3])); sm = difflib.SequenceMatcher(None, mt, L, autojunk=False)
P(f"4. main text, glyph values vs published transliteration: similarity {sm.ratio():.4f}")
(HERE/'layers_report.txt').write_text('\n'.join(out)+'\n', encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8'); print('\n'.join(out))
