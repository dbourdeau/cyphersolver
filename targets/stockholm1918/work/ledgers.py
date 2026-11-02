"""Insert both targets into the manifest, README, front page and catalogue. Run from the repository root; safe to rerun."""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
P = {'stockholm1918': dict(label='German Foreign Office to Stockholm 1918', year='1918', y=1918.55, place='Berlin &rarr; Stockholm',
        title='The German Foreign Office to Stockholm, July 1918',
        blurb='Ten telegrams to the Stockholm legation, copied by American diplomats, in at least four numeric code systems. Every German code printed in Mendelsohn&rsquo;s 1937 study was ruled out, so the bodies stay unread. The heads were decoded: Nr. 923&ndash;925 and an unbroken Nr. 1010&ndash;1015, and one batch moves to about 2 July.',
        quote='&ldquo;017 556 405 4416&rdquo;: Nr. 1014, the body unread',
        lead='Nr. 1014, 26 July 1918: typed copy by the US Legation, Stockholm', credit='National Archives (US), RG 59, M367 roll 141 frame 1263, via the NARA catalogue'),
     'ludendorff1918': dict(label='Ludendorff to Stockholm 1918', year='1918', y=1918.56, place='Grosses Hauptquartier &rarr; Stockholm',
        title='Ludendorff to the attach&eacute; in Stockholm, July 1918',
        blurb='A very urgent five-part telegram signed Ludendorff, 26 July 1918, and five Berlin telegrams to the Stockholm legation and consulate-general, copied by American diplomats. The five-figure groups are flat in every column, with no depth, and no German code printed by Mendelsohn fits. Not solved.',
        quote='&ldquo;5 Teile 1 teil urachi 39 gruppe&rdquo;',
        lead='The Ludendorff telegram, 26 July 1918: typed copy by the US Legation, Stockholm', credit='National Archives (US), RG 59, M367 roll 141 frame 1264, via the NARA catalogue')}
b = open('docs/_build_site.py', encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in b else '\n'
for slug, d in P.items():
    if f"slug='{slug}'" in b: continue
    entry = (f"    dict(slug='{slug}', label='{d['label']}', year='{d['year']}', y={d['y']}, place='{d['place']}', st='stuck', stt='not solved',{nl}"
             f"         title='{d['title']}',{nl}         blurb='{d['blurb']}',{nl}         quote='{d['quote']}',{nl}"
             f"         rights='National Archives (US), via the NARA catalogue'),{nl}")
    k = b.index("    dict(slug='bernstorff1917'") if "slug='bernstorff1917'" in b else b.index("IMAGES = {")
    if "slug='bernstorff1917'" not in b:
        k = b.rindex("    dict(slug=", 0, k)
    b = b[:k] + entry + b[k:]
    img = f"IMAGES['{slug}'] = ('{slug}_lead.jpg', '{d['lead']}', '{d['credit']}'){nl}"
    k2 = b.index("IMAGES['camus1586'] = None")
    b = b[:k2] + img + b[k2:]
open('docs/_build_site.py', 'w', encoding='utf-8', newline='').write(b)

r = open('README.md', encoding='utf-8', newline='').read()
rows = {'stockholm1918': "| **German Foreign Office → Legation Stockholm**, ten telegrams signed Hintze, Bussche, Stumm, Auswaertig, copied by the US Legation, NARA RG 59 M367 rolls 141, 114, 122, 108 (catalogue 654, B) | 2 and 22–27 Jul 1918 | 2 Nov 2026 | &mdash; | **Not solved.** 938 groups transcribed and checked against cable copies, in four numeric systems (marks 1219, 44xx, two others). 13040, 5950, 26040, the 18470 family, slider no. 1 and Bernstorff's 1917 code, all from Mendelsohn 1937 or this repository, ruled out at chance. The heads were decoded with the Dreinummerheft rule: Nr. 923–925, unbroken Nr. 1010–1015 across three systems; despatch 1421 redated to about 2 July. Needs a code book or the Berlin drafts | [`targets/stockholm1918/`](targets/stockholm1918/) · [write-up](https://dbourdeau.github.io/cyphersolver/stockholm1918.html) |",
        'ludendorff1918': "| **Ludendorff → German military attaché Stockholm**, five-part \"Sehr dringend\" telegram, and five Berlin telegrams to Legation and Consulate-General, NARA RG 59 M367 rolls 141, 122, 108 (catalogue 656, C) | 22–26 Jul 1918 | 2 Nov 2026 | &mdash; | **Not solved.** 328 five-figure groups transcribed. Flat in every column (IC 0.97–1.06), two repeats, no additive reused across 1,575 offsets; system undetermined. All German codes printed in Mendelsohn 1937 ruled out. Needs the key or a clear copy | [`targets/ludendorff1918/`](targets/ludendorff1918/) · [write-up](https://dbourdeau.github.io/cyphersolver/ludendorff1918.html) |"}
for slug, row in rows.items():
    if f'targets/{slug}/' in r: continue
    i = r.index('### Not solved')
    j = r.index('|---', i)
    j = r.index('\n', j) + 1
    r = r[:j] + row + ('\r\n' if '\r\n' in r else '\n') + r[j:]
open('README.md', 'w', encoding='utf-8', newline='').write(r)

h = open('docs/index.html', encoding='utf-8', newline='').read()
for slug, li in {'ludendorff1918': '<li><b>Ludendorff to the attach&eacute; in Stockholm, July 1918</b> &mdash; <span class="fnd">not solved: a very urgent five-part telegram and five legation telegrams in flat five-figure groups, transcribed and tested</span> <a href="ludendorff1918.html">write-up</a></li>',
                 'stockholm1918': '<li><b>The German Foreign Office to Stockholm, July 1918</b> &mdash; <span class="fnd">not solved: four numeric codes ruled out against Mendelsohn&rsquo;s tables; the heads decoded, Nr. 1010&ndash;1015 in an unbroken run</span> <a href="stockholm1918.html">write-up</a></li>'}.items():
    if f'<a href="{slug}.html">write-up' in h: continue
    k = h.index('<ul class="findings">') + len('<ul class="findings">')
    k = h.index('\n', k) + 1
    h = h[:k] + li + '\n' + h[k:]
open('docs/index.html', 'w', encoding='utf-8', newline='').write(h)

c = json.load(open('catalogue.json', encoding='utf-8'))
for e in c['entries']:
    if e['id'] == 654:
        e['date'] = '2 and 22-27 Jul 1918 (copies sent 4 Oct, 8 Oct and 6 Nov 1918)'
        e['outcome'] = 'attempted, open'; e['as_of'] = '2026-11-02'
        e['status'] = ("2 Nov 2026 (targets/stockholm1918/): transcribed, 938 groups in four numeric systems, not deciphered. 13040, 5950, 26040, the 18470 family, slider no. 1 and Bernstorff's 1917 code ruled out. "
                       "Heads decoded with the Dreinummerheft (Mendelsohn 1937): Nr. 923-925 of about 2 July, Nr. 1010-1015 of 26-27 July. Needs a code book, an MI-8 or Room 40 decode, or the Berlin drafts by those numbers.")
        e['prior_art'] = 'open as far as checked (2 Nov 2026: Mendelsohn 1937 read for this traffic, not mentioned; Zeman 1958; web); FRUS 1918 not checked page by page; an MI-8 decode may exist in RG 165 or RG 457'
    if e['id'] == 656:
        e['outcome'] = 'attempted, open'; e['as_of'] = '2026-11-02'
        e['status'] = ("2 Nov 2026 (targets/ludendorff1918/): transcribed, 328 five-figure groups, not deciphered. Figures flat in every column, two repeats, no additive reused at any offset; every German code printed in Mendelsohn 1937 ruled out. "
                       "Stockholm 2952: 'number nine to German Military Attache ... signed Ludendorff'. Needs the key or a clear copy.")
        e['prior_art'] = 'open as far as checked (2 Nov 2026: Mendelsohn 1937, Zeman 1958, web); an MI-8 decode may exist in RG 165 or RG 457'
with open('catalogue.json', 'w', encoding='utf-8', newline='\n') as f:
    json.dump(c, f, ensure_ascii=False, indent=1); f.write('\n')
print('done')
