"""Site builder: one manifest drives the navigation, footers, tables of contents and index cards of every page.

Run  python _build_site.py  from docs/ after editing any page. It is idempotent.

Per page it: replaces the first <nav class="nav">...</nav> (or the <!-- site:nav --> marker) with the generated
header; replaces the last <footer>...</footer> (or <!-- site:footer -->) with the generated footer, including
previous / next links in chronological order; inserts an "On this page" contents strip after <main> when the page
has three or more h2 sections with ids; stamps the stylesheet and script versions; and removes inline <style>
blocks whose rules now live in style.css. On index.html it also regenerates the write-up cards between
<!-- cards:start --> and <!-- cards:end -->, and refolds "Recent findings" so that only the newest RECENT_VISIBLE
entries show and the rest sit behind the "Show N earlier findings" button (add new entries at the top of the first
list and rebuild). The priority queue is still built by _build_queue.py.

It also stamps the dates: the hero dateline, the head meta tags, the index cards, the list rows and each line
of "Recent findings" all carry the day the finding landed, from _dates.json, which this script maintains.
"""
import re, pathlib, html, json, hashlib, datetime
HERE = pathlib.Path(__file__).parent
ICONS = ('<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n'
         '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n')
VERSION ='20260921e'
SITE = 'Unsolved Historical Ciphers'
REPO = 'https://github.com/dbourdeau/cyphersolver'

# ---------------------------------------------------------------------------
# Datestamps.  _dates.json records, per page, the day the finding first landed
# in the repository and the day its text last really changed.  "Really" means
# the page body: nav, footer, contents strip, lead figure, the dateline itself
# and the version stamps are all generated here, so normalise() removes them
# before hashing.  A rebuild that only reshuffles that furniture therefore does
# not move the date.  Findings on index.html are dated the same way, keyed by
# the bold lead-in of each entry, so a hand-added line dates itself on the next
# build.  Seed the file with _seed_dates.py; after that it maintains itself.
DATES_PATH = HERE / '_dates.json'
TODAY = datetime.date.today().isoformat()
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
SHORT = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
# what the first date means, by status class
VERB = {'solved': 'solved', 'found': 'resolved', 'partial': 'solved in part', 'stuck': 'attempted'}
VERB_SHORT = {'partial': 'part read'}      # the card and list stamps have less room

def fmt_date(iso, short=False):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} {(SHORT if short else MONTHS)[m-1]} {y}'

FINDINGS_REGION = re.compile(r'<h2 id="recent">.*?(?=\n<h2|\n<!-- |\Z)', re.S)
GENERATED = [
    r'<header class="nav">.*?</header>', r'<div class="search" id="search".*?</div>\n</div>', r'<nav class="nav">.*?</nav>', r'<footer.*?</footer>',
    r'<nav class="toc".*?</nav>', r'<figure class="lead">.*?</figure>',
    r'<!-- cards:start -->.*?<!-- cards:end -->', r'<!-- site:(?:nav|footer) -->',
    r'<script src="site\.js[^"]*"></script>',
    r'\n?<div class="seal [a-z]+" aria-hidden="true">.*?</div>',
    r'\n?<div class="parties">.*?</div><!-- /parties -->',
    r'<!-- replay:start -->.*?<!-- replay:end -->\n?', r'<script src="solve-replay\.js[^"]*" defer></script>\n?',
    r'<script src="zoom\.js[^"]*" defer></script>\n?',
    r'<!-- live:start -->.*?<!-- live:end -->\n?', r'<script src="home\.js[^"]*" defer></script>\n?',
    r'<meta name="(?:date|last-modified)"[^>]*>', r'<link rel="(?:icon|apple-touch-icon)"[^>]*>',
    r'\n?<!-- bnx -->.*?<!-- /bnx -->', r' data-bnx="1"', r'<span class="fth">.*?</span><!-- /fth -->',
    r'<!-- cattop:start -->.*?<!-- cattop:end -->\n?',
]

def normalise(s):
    """The page as content: everything this script generates removed, whitespace flattened."""
    def fold(m):        # the findings list is re-split on every build; compare the entries alone
        r = m.group(0)
        r = re.sub(r'</?ul class="findings">|</ul>|<div class="more" hidden>|</div>|'
                   r'<button class="showmore".*?</button>', ' ', r, flags=re.S)
        return r
    s = FINDINGS_REGION.sub(fold, s)
    s = re.sub(r'<time class="fdate"[^>]*>.*?</time>', '', s, flags=re.S)   # inserted flush, remove flush
    s = re.sub(r'<p class="meta">.*?</p>', ' ', s, count=1, flags=re.S)     # the hero dateline only: some pages
                                                                           # use .meta again in the body for notes
    s = re.sub(r'\?v=\w+', '', s)      # version stamps vanish without a trace, so a newly stamped src hashes as before
    for pat in GENERATED: s = re.sub(pat, ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', s).strip()

def content_hash(s):
    return hashlib.sha1(normalise(s).encode('utf-8')).hexdigest()[:12]

def load_dates():
    try: return json.loads(DATES_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError: return {'pages': {}, 'findings': {}}

def save_dates(d):
    DATES_PATH.write_text(json.dumps(d, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')

DATES = load_dates()

def page_dates(slug, s):
    """Record and return {'first', 'updated'} for a page, moving 'updated' when the body changed."""
    h = content_hash(s)
    rec = DATES['pages'].get(slug)
    if rec is None: rec = DATES['pages'][slug] = {'first': TODAY, 'updated': TODAY, 'hash': h}
    elif rec.get('hash') != h: rec['updated'], rec['hash'] = TODAY, h
    return rec

DATEISH = re.compile(r'^(?:solved(?: in part)?|resolved|attempted|posted|read|published|first published|updated)?'
                     r'\s*(?:\d{1,2}\s+)?(?:' + '|'.join(MONTHS) + r'|Sept?)?\s*\d{4}$', re.I)

def meta_html(p, rec, old):
    """Rebuild the hero dateline, keeping whatever else the page put on that line."""
    author = (p.get('author') if p else None) or 'Daniel Bourdeau'
    keep = []
    for part in re.split(r'\s*(?:&middot;|·)\s*', old or '')[1:]:
        flat = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', part))).strip()
        if flat and not DATEISH.match(flat): keep.append(part.strip())
    verb = VERB.get(p['st'], 'posted') if p else 'posted'
    if p and p['slug'] in ('famous', 'solved'): verb = 'posted'
    bits = [author, f'{verb} <time datetime="{rec["first"]}">{fmt_date(rec["first"])}</time>']
    if rec['updated'] != rec['first']:
        bits.append(f'updated <time datetime="{rec["updated"]}">{fmt_date(rec["updated"])}</time>')
    return '<p class="meta">' + ' &middot; '.join(bits + keep) + '</p>'

def finding_key(li):
    """A findings entry is identified by its bold lead-in, which does not change when the text is edited."""
    m = re.search(r'<b>(.*?)</b>', li, re.S)
    text = re.sub(r'<[^>]+>', '', m.group(1) if m else li[:160])
    return re.sub(r'\s+', ' ', html.unescape(text)).strip().lower()[:80]

def stamp_finding(li):
    li = re.sub(r'<time class="fdate"[^>]*>.*?</time>\s*', '', li, flags=re.S)
    key = finding_key(li)
    iso = DATES['findings'].setdefault(key, TODAY)
    stamp = f'<time class="fdate" datetime="{iso}">{fmt_date(iso, short=True)}</time>'
    li = re.sub(r'<span class="fth">.*?</span><!-- /fth -->', '', li, flags=re.S)
    slugs = [x for x in re.findall(r'href="([a-z0-9]+)\.html', li) if any(q['slug'] == x for q in PAGES)]
    th = mini_thumb(slugs[-1], 'fth') if slugs else ''
    if th: stamp = th + '<!-- /fth -->' + stamp
    return li.replace('<li>', '<li>' + stamp, 1)

# slug, nav label, year label, sort year, place, status class, status text, title, blurb, quote, rights
PAGES = [
    dict(slug='r8358', label='Burghley to Walsingham July 1572', year='1572', y=1572.51, place='Westminster &rarr; Paris', st='stuck', stt='key not found', title='Burghley to Walsingham, 5 July 1572 &mdash; name codes in a clear letter, one read', blurb='BL Harley MS 260 f. 262 (DECODE R8358), catalogued as Burghley to an unknown recipient, is a copy in Walsingham&rsquo;s Paris letter-book of Burghley&rsquo;s letter of 5 July 1572, printed in Digges 1655 with the cipher left as figures. Context and Walsingham&rsquo;s reply fix [3] as the French King; the other codes and a five-letter run need the lost key.', quote='Some that are come home bear us in hand that [3] reneweth the m o R. d A. [4] whereby the last matter is hindered', rights='British Library (images via DECODE, not reproduced)'),
    dict(slug='walsingham1572', label='Walsingham to Burghley 1573', year='1573', y=1573.05, place='Paris &rarr; London', st='stuck', stt='too short, no key', title='Walsingham to Burghley, 20 January 1572/3 &mdash; attempted, not read', blurb='A letter-book copy in Harley MS 260, printed by Digges in 1655. It is clear English apart from one six-sign port name in digits and signs, and a mark where the copyist left out another name. No key of 1572-73 survives, and the one other group in the same system, in Burghley&rsquo;s reply, is not enough to choose between Dieppe, Calais or Nantes.', quote='a Gentleman of [9] departed hence to 2 1 &#8984; &epsilon; 9 4 with intention to imbarke there', rights='British Library (images via DECODE, not reproduced)'),
    dict(slug='mercoeur1586', label='&ldquo;MR&rdquo; to Merc&oelig;ur 1586', year='[1586]', y=1586.48, place='? &rarr; Merc&oelig;ur, Brittany', st='stuck', stt='too short, no key',
         title='&ldquo;MR&rdquo; to the Duke of Merc&oelig;ur, 26 June [c. 1586] &mdash; attempted, not read',
         blurb='A slip in BnF fr. 15564 (f. 151) with six cipher runs inside clear French, 217 signs of 55 kinds. It is not in Lasry&rsquo;s 2022 key for the Guise letters in the volume, nor in the Mayenne&ndash;Forget or Clairambault 357 keys of 1586. A homophonic annealer scores it no better than shuffled text. The clear frame is transcribed.',
         quote='&ldquo;mais esperons beaucoup par sa valeur. Ce xxvj<sup>e</sup> juin&rdquo;',
         rights='Images: Biblioth&egrave;que nationale de France'),
    dict(slug='percy1559', label='Percy to Cecil 1559', year='1559', y=1559.55, place='Norham &rarr; Cecil', st='stuck', stt='too short, no key',
         title='Sir Henry Percy to Cecil, Norham, 23 July 1559 &mdash; attempted, not read',
         blurb='DECODE R9256 is a Forbes Papers tracing of the four cipher passages in Percy&rsquo;s letter of 23 July 1559: 63 signs in a box script with dot and underline marks. Cecil deciphered them at the time and the letter is calendared, but which words were in cipher is not printed. No single letter substitution fits the four passages, and the text is too short to break without the key.',
         quote='&ldquo;A few words in cipher, deciphered by Cecill&rdquo; (Bain, CSP Scotland I, no. 501)',
         rights='Images: British Library, via DECODE'),
    dict(slug='wod1568', label='Throckmorton leaves 1559', year='1559, 1568', y=1559.53, place='Paris &rarr; Elizabeth I', st='solved', stt='read',
         title='Throckmorton to Elizabeth, 10 July 1559, the margin cipher, and John Wood 1568 &mdash; read in part',
         blurb='Tomokiyo lists two unidentified ciphers on BL Add MS 4136 ff. 32&ndash;33. Throckmorton&rsquo;s own ciphered letter of 10 July 1559 on f. 32, never printed, is read at about 85&ndash;90% with his Cipher 1. The margin is a word-sign code (222 groups, half used once) that needs its key or the 8 July despatches; John Wood&rsquo;s 39-sign line of 1568 has no unique solution.',
         quote='&ldquo;I judge your Majesty will be desirous to be further enformed thereof&rdquo;',
         rights='British Library, Add MS 4136, via DECODE R2988, R2989'),
    dict(slug='throckmorton', label='Throckmorton', year='1560&ndash;63', y=1561.5, place='France', st='found', stt='key and printed text verified',
         title='Throckmorton &mdash; archived key and published plaintext',
         blurb='Twenty DECODE records in BL Add MS 4136 lead to Forbes and CSP. The archived third cipher reads two short samples, 42 tokens in all. A record-to-edition concordance separates the published counterparts from full token verification; composite material remains to be checked.',
         quote='&ldquo;all be it i be revoked or the warr breake&rdquo;',
         rights='British Library, Add MS 4136, via DECODE; photographs not republished'),
    dict(slug='smith1562', label='Smith 1563&ndash;66', year='1563&ndash;66', y=1564.5, place='France &rarr; Cecil', st='found', stt='read at the time; re-read',
         title='Sir Thomas Smith to Cecil and the Queen, 1563&ndash;1566 &mdash; DECODE R9248&ndash;R9254',
         blurb='Six DECODE records listed as not decrypted are Patrick Forbes&rsquo;s copies of the ciphered stretches of eighteen despatches of Elizabeth&rsquo;s ambassador in France. Smith&rsquo;s own key is in the same volume (f. 179, DECODE R9261). With it the 1563 passages agree word for word with Forbes&rsquo;s print of 1741, and the 1564&ndash;66 passages, which the Calendar of State Papers only summarises, are read in Smith&rsquo;s words: the Cardinal of Lorraine banqueting with Cond&eacute;, the Lennox marriage offer, a bearer &ldquo;double, or rather triple&rdquo;.',
         quote='&ldquo;this bearer Hume is altogether a Lidington, whom you shall find double, I am afraid, or rather triple&rdquo;',
         rights='British Library, Add MS 4136, via DECODE; photographs not republished beyond two details'),
    dict(slug='norreys1567', label='Norreys 1567&ndash;68', year='1567&ndash;68', y=1567.6, place='Paris &rarr; Cecil', st='solved', stt='read',
         title='Sir Henry Norreys to Cecil, 1567&ndash;68 &mdash; DECODE R9251',
         blurb='DECODE R9251 is Patrick Forbes&rsquo;s copy of only the ciphered words of seven letters of Elizabeth&rsquo;s ambassador in France. No key is on DECODE, but the Cecil&ndash;Norris cipher that Tomokiyo reconstructed from a decipherment printed by mistake in <em>Cabala</em> (1663) reads the siblings: demaund, reason, ruin, remain, Master Stewarde, as the Calendar of State Papers summarises them. A shuffle control (8 word hits against at most 3 in 1,000 shuffles) confirms the table is Norris&rsquo;s. The target letter of 9 March 1568 has three items: the French King&rsquo;s name sign, a name sign probably for the Queen of Scots, and a four-sign word not read.',
         quote='&ldquo;otherwise Norris much doubts the ruin of the Prince of Cond&eacute; and the Admiral&rdquo;',
         rights='British Library, Add MS 4136, via DECODE; one detail reproduced'),
    dict(slug='kaa4591b', label='&#321;aski, King John, Wardein 1531&ndash;37', year='1531&ndash;1537', y=1534, place='&#321;ask, Hungary, Wardein &rarr; Munich', st='partial', stt='read in part',
         title='&#321;aski, King John and a Bavarian at Wardein: three more ciphers in the Munich key volume',
         blurb='Three ciphertexts catalogued on DECODE as one &ldquo;unknown recipient&rdquo; entry are three letters to the Bavarian court from King John Z&aacute;polya&rsquo;s circle. &#321;aski&rsquo;s letter of September 1531 reads 99.5% in his own cipher with e and r swapped; a Latin letter of April 1533 on the diet of Pressburg and Ferdinand&rsquo;s secret peace suit reads 95.3%; a German report from Wardein of March 1537 on the Turkish arming reads 91.3%, with two homophonic keys rebuilt from their glosses.',
         quote='&ldquo;numquam pacem uel inducias consequuturum nisi cedat regno Hungarie&rdquo; (&#321;aski, 1531)',
         rights='Manuscript: Bayerisches Hauptstaatsarchiv, Munich, via DECODE'),
    dict(slug='kaa4591', label='Bavarian key volume 1529&ndash;83', year='1529&ndash;1583', y=1556, place='Buda, Krak&oacute;w, Pressburg &rarr; Munich', st='solved', stt='read',
         title='The Bavarian key volume: fourteen ciphertexts in Kurbayern &Auml;u&szlig;eres Archiv 4591',
         blurb='Fourteen ciphertexts bound in the Munich chancery&rsquo;s key volume, catalogued on DECODE as one &ldquo;unknown sender&rdquo; group, are letters in at least six systems. The Fulda protest of 1576 reads with the key five leaves earlier; &#321;aski&rsquo;s letters of 1529&ndash;30 read from a key rebuilt from their glosses; seven German reports of 1534&ndash;35 on Hungary, the Turks and France are broken and read in part, one from ciphertext alone with a new sixteenth-century German model.',
         quote='&ldquo;Rogatus Dux Bavariae auxilio sit&rdquo; (R9325, 1576)',
         rights='Manuscript: Bayerisches Hauptstaatsarchiv, Munich, via DECODE'),
    dict(slug='beatrice1482', label='Beatrice d&rsquo;Aragona', year='1482&ndash;1505', y=1482, place='Pozsony / Buda / Naples &rarr; Ferrara', st='found', stt='earlier readings found',
         title='Beatrice d&rsquo;Aragona: four earlier readings and one plain letter',
         blurb='Four cipher letters have readings in editions of 1877&ndash;78; the May 1486 letter also has manuscript decipherment slips. The fifth record is plain Italian dated 1505, not 1504, and explicitly says the queen has no cipher. The March edition retains unexplained Virtus/Fortis/M. markers; no new key or exhaustive glyph validation is claimed.',
         quote='&ldquo;et per non havere cifra: non ce extendemo altramente per questa&rdquo;',
         rights='Printed edition: Nagy and Ny&aacute;ry, 1877, public domain. ASMo manuscript images not reproduced.'),

    dict(slug='haga1620', label='Haga at the Porte', year='1620', y=1620.3, place='Constantinople &rarr; The Hague', st='solved', stt='read',
         title='Cornelis Haga to the States General, February&ndash;May 1620 &mdash; the Bohemian revolt seen from the Porte',
         blurb='DECODE lists two ciphered despatches of the first Dutch ambassador at Constantinople as non-decrypted, with a note that their signs are zodiacal and alchemistic. They are not: the cipher is a letter substitution whose signs are ordinary letter shapes, with a 116-entry numeric nomenclator, and its key sits in the same archival file as DECODE R2118. The two records hold four letters, not two, and their pages are bound out of order. The cipher carries Haga&rsquo;s advice on the Bohemian revolt &mdash; that the Hungarians should elect the King of Bohemia and proceed to the crowning of a new king &mdash; and the Porte&rsquo;s urgent questions about the truce with Spain. The key&rsquo;s cell for m falls outside the photograph and was recovered from the letters.',
         quote='&ldquo;dat de Ongaren regem Bohemiae mede erweelden&rdquo;',
         rights='Manuscript images: Nationaal Archief, The Hague, 1.01.02 inv. 6894, via DECODE'),

    dict(slug='sp106box10', label='SP 106/10 codebreaker', year='1623&ndash;24', y=1623.5, place='London', st='partial', stt='file explained, read in part',
         title='A codebreaker&rsquo;s file &mdash; the Italian intercepts of TNA SP 106/10',
         blurb='DECODE lists seven anonymous, undated, partly decrypted ciphertexts in State Papers 106 box 10. They are one case: the working file of a Jacobean codebreaker, with his solutions between the lines. The key he reconstructed is catalogued three records away as a key rather than a ciphertext, and so fell outside the target list; it sets out a two-figure cipher in which a bar or a tick over the group switches it from a letter to a word of one of two lists. Its vocabulary &mdash; Marques Inichiosa, Palatinato, C. Barberino, Il Principe &mdash; dates the file to 1623&ndash;24, against the catalogue&rsquo;s 1558/1625. The file holds three different ciphers, not one, and about forty-five values of the three-figure code were rebuilt from the codebreaker&rsquo;s own interlinear syllables.',
         quote='&ldquo;It seemes there are numbers of woordes expressed by this difference of &mdash; over the figures whereof in this Cifar.&rdquo;',
         rights='Manuscript rights: The National Archives, Kew, via DECODE'),
    dict(slug='boswell1628', label='Ralph Boswell 1627', year='1627&ndash;28', y=1627.95, place='England &rarr; William Boswell', st='found', stt='read by others',
         title='Sir Ralph Boswell to his cousin William Boswell, December 1627 &mdash; already read by Mark Woodard',
         blurb='Ten lines of invented signs in TNA SP 106/5, catalogued on DECODE as King Charles I to Boswell, 1628, and undeciphered. Mark Woodard read the monoalphabetic cipher on DECODE in 2021. Here: two of his three open signs read, the sender identified from the endorsement as Sir Ralph Boswell, and the letter dated to 15 December 1627.',
         quote='&ldquo;our greate Duke returned from Plimmouth to Whitehall, contrary to the opinion of very many&rdquo;',
         rights='The National Archives, Kew, via DECODE R413'),
    dict(slug='r1874', label='Mocenigo 1628', year='1628', y=1628.8, place='Madrid &rarr; Venice', st='found', stt='read at the time',
         title='Mocenigo to the Doge, Madrid 1628 &mdash; read at the time',
         blurb='DECODE R1874, catalogued as an undated letter of unknown sender and recipient (ASVe Busta 30 f. 174), is Alvise Mocenigo&rsquo;s despatch from Madrid to the Doge and Senate of 26 October 1628, <em>CSP Venice</em> 21 no. 515. The record holds the chancery&rsquo;s decipherment of the whole letter and a second, separately enciphered copy. Paragraph marks and the three &ldquo;conte di Olivares&rdquo; group runs tie the decipherment to the numerical syllabic cipher; the key was not rebuilt.',
         quote='&ldquo;Il Conte di Olivares ha desiderato con buone parole, et promesse condurlo &agrave; risolutione di ritornar in Fiandra&rdquo;',
         rights='Archivio di Stato di Venezia, via DECODE R1874 (images not reproduced)'),
    dict(slug='richelieu', label='Richelieu', year='1629', y=1629, place='France', st='solved', stt='solved',
         title='Richelieu to M. de Ranc&eacute; &mdash; BnF Fran&ccedil;ais 3829',
         blurb='Ciphertext-only recovery of a homophonic alphabet with a doubling mark and nomenclature; then found to agree word for word with the decipherment Avenel printed in 1858, which the catalogues had missed.',
         quote='&ldquo;Castor voudroit bien que la [duchesse de Chevreuse] peust estre attrap&eacute;e pr&egrave;s de la fronti&egrave;re&hellip;&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='pallotto1629', label='Pallotto to Barberini 1629', year='1629', y=1629.6, place='Vienna &rarr; Rome', st='found', stt='solved by others',
         title='Pallotto to Barberini &mdash; the ciphers of BAV Barb.lat. 6960, printed in 1897, key found in 2018',
         blurb='Twenty-eight ciphered sheets in the register of the nuncio to the Emperor, catalogued as undeciphered with their contents unknown. The contents have been in print since 1897: Kiewning&rsquo;s volume of the Nuntiaturberichte prints these despatches from the Roman office&rsquo;s own decipherments, and the register&rsquo;s clear pages confirm the identification. The key had also been found, though not by this project. George Lasry pointed out that 6960 uses the key Norbert Biermann and Thomas Bosbach recovered in 2018 for the sibling volume Barb.lat. 6956, which is filed on DECODE but was never linked to these records. Applied here, it reads all twenty-eight sheets, apart from about 1,750 name groups missing from the 1628 key. The system is two-digit homophones and syllable groups, three-digit nomenclator groups and one-digit nulls in a single digit stream. That mix of widths is why every fixed-width attack made here failed, though the controls had correctly shown that the cipher used fixed groups of varying length.',
         quote='&ldquo;&hellip;con che il demonio resteria ingannato e burlato.&rdquo;',
         rights='Manuscript rights: Biblioteca Apostolica Vaticana'),
    dict(slug='riksarkivet1628', label='Bremen to Salvius 1631', year='1628&ndash;33', y=1631.9, place='Bremen &rarr; Hamburg; Riksarkivet', st='partial', stt='Bremen letters read; 3 open',
         title='Riksarkivet ciphers 1628&ndash;1633 &mdash; the Bremen letters read, three ciphers open',
         blurb='Catalogue item 207 bundled fourteen DECODE records from the Riksarkivet as one Latin cipher of an unknown sender. They are four unrelated groups. The two letters of Johann Friedrich, archbishop of Bremen, to Johan Adler Salvius at Hamburg, November and December 1631, are <strong>read in full</strong>: the decipherer&rsquo;s interlinear glosses give four consecutive numbers per letter, and the bands follow the alphabet written in six columns and read downwards, which places the letters nobody glossed. The archbishop begs for Swedish succour against Gronsfeld&rsquo;s and B&ouml;nninghausen&rsquo;s troops. Three key-box ciphertexts &mdash; a Latin letter cipher, a Latin figure letter of 1628 and a figure letter to Amsterdam of 1632 &mdash; were attacked and stay open.',
         quote='&ldquo;und in die euserste gefahr kommen w&uuml;rden&rdquo; &middot; 73 38 97 75 83 98 20 74 = euserste',
         rights='Manuscript rights: Riksarkivet, Stockholm, via DECODE'),
    dict(slug='ceva1632', label='Barberini to Ceva 1632', year='1632', y=1632, place='Rome &rarr; Paris', st='solved', stt='read',
         title='Barberini to Nuncio Ceva &mdash; the two letters of ASV Francia 346 without a published reading',
         blurb='The catalogue listed five ciphertexts as a transcription job. George Lasry had in fact reconstructed the key of the dossier in 2020 and read four of its eleven letters, which covered three of the five; no reading of the other two was published. A beam search over the unseparated figures, under an Italian model built partly from the dossier&rsquo;s own clear passages, reads both, and agrees on 77.5% of letters with the decipherment written between the lines in 1632. Six of the ninety-five nomenclator elements Lasry left blank are given values, among them 830 = Francia; 117 stay unread.',
         quote='&ldquo;&hellip;conseguenze che tengano disunita per un lungo pezzo la Francia, e sotto giogo alle esterne violenze, o almeno impotente a soccorrer li suoi alleati.&rdquo;',
         rights='Manuscript rights: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='ormonde', label='Ormonde', year='1634&ndash;35', y=1634, place='Ireland / England', st='solved', stt='solved',
         title='Maltravers to Ormonde &mdash; a regular block cipher',
         blurb='Doubled letters written with consecutive figures betray a regular key (consonants three figures each from 7, vowels from 64, nulls 91&ndash;111). Every spelled word reads, and the nomenclator is then confirmed clause for clause against Wentworth&rsquo;s own dispatches in Knowler&rsquo;s <em>Strafforde&rsquo;s Letters</em> (1739): the King refusing Kildare, and Ormonde moved for the Council &ldquo;in exchange&rdquo; for Sir Piers Crosby.',
         quote='&ldquo;he was angry [with the Lord Deputy] &hellip; upon his motion [Ormonde] is to be a councellor&rdquo;'),
    dict(slug='harley286', label='D&rsquo;Ewes&rsquo;s cipher log 1635', year='1635&ndash;36', y=1635.3, place='Suffolk (private record)', st='solved', stt='read',
         title='Sir Simonds D&rsquo;Ewes&rsquo;s cipher log of his son&rsquo;s fits, 1635&ndash;36',
         blurb='BL Harley MS 286 f. 61, on DECODE as an undeciphered letter of 1635 from an unknown sender, is a private slip of the antiquary Sir Simonds D&rsquo;Ewes in the alphabet he invented at school. No key is printed; it was rebuilt by crib on <em>convulsio</em> and <em>plena luna</em>. The Latin log records, one line to a fit, the convulsions of his infant son Clopton from 3 April 1635, with weekdays and moon phases that check against the calendar; 96.5% of the words read.',
         quote='&ldquo;in quorum tertia os ipsius pene ad aurem dextram convulsum, quod ante numquam observavi&rdquo;',
         rights='Manuscript images: British Library, via DECODE R7759'),
    dict(slug='santacroce1552', label='Santa Croce 1553', year='1553', y=1553.5, place='France &rarr; Rome', st='found', stt='already in print',
         title='Prospero Santa Croce to Cardinal del Monte, 1553 &mdash; five ciphered despatches, read at the time and printed in 1972',
         blurb='DECODE R6&ndash;R10, catalogued as unread ciphers of the nuncio in France dated 1552, are passages of five letters of March&ndash;December 1553. All were deciphered on arrival and are printed deciphered in Lestocquoy&rsquo;s Acta Nuntiaturae Gallicae 9 (1972); Lasry&rsquo;s key has been on the records since 2020, and it reproduces the print. The one unprinted passage, three cancelled cipher lines of 14 December, is read here: the clear postscript about the fleet bound for Corsica, enciphered and struck out.',
         quote='&ldquo;l&rsquo;armata regia che part&igrave; per Corsica ha havuto fortuna et non si sa come n&eacute; dove sia&rdquo;',
         rights='Manuscript images: Archivio Apostolico Vaticano, via DECODE R6&ndash;R10'),
    dict(slug='malvezzi1548', label='Ferdinand I to Malvezzi 1548', year='1548', y=1548.06, place='Augsburg &rarr; Constantinople', st='solved', stt='read',
         title='Ferdinand I to Malvezzi, 23 January 1548 &mdash; the French at the Porte, and the envoy&rsquo;s money',
         blurb='DECODE R366, eight pages, carried as only partially decrypted: Ferdinand&rsquo;s letter to his resident at the Porte, mostly clear Latin with about three pages in graphic signs. The key was on DECODE itself, filed at the same shelfmark as a separate record (R367), and with it the ciphered passages read. They hold the politics: the French are working to wreck the Habsburg&ndash;Ottoman peace only because they dare not attack Charles V with their own forces and want it done at the Sultan&rsquo;s charges; R&uuml;stem Pasha is not to doubt Habsburg sincerity. The rest is Malvezzi&rsquo;s pay &mdash; 4,300 ducats by the hand of the secretary Justus de Argento, and a credit of 3,000 more repayable at Venice. The cipher&rsquo;s nulls are whole Latin words (<em>etiam</em>, <em>idcirco</em>, <em>Porro</em>) dropped among the signs. Short stretches on pages 1 and 7 stay unread.',
         quote='&ldquo;Galli tam multipliciter et dolose hanc pacem subuertere conantibus&hellip; imperatoris Turcorum sumptibus&rdquo;'),
    dict(slug='vatican', label='Vatican', year='1542', y=1542, place='Rome &rarr; Spain', st='stuck', stt='family identified',
         title='The Vatican cipher of April 1542 &mdash; an Antonio Elio cipher',
         blurb='Farnese to the nuncio Poggio, four folios, 6,549 digits, open since Lasry set it in 2019. Not read, but named: a polyphonic-syllabic cipher of the design Antonio Elio built for Paul III&rsquo;s chancery. Seven sessions, five model classes excluded against matched controls, the Meister keys excluded under any renumbering, and the 400&nbsp;dpi images read against the transcript: no separators, no decipherment, no key.',
         quote='27 and 80 end a third of the words &middot; 441 repeated 7-grams against 5 in a shuffle'),
    dict(slug='warsaw', label='Warsaw', year='1627', y=1627, place='Warsaw', st='solved', stt='solved',
         title='From Warsaw, 24 December 1627 &mdash; an alphabet in plain order',
         blurb='DECODE R1408, one page of figures and stray letters with only a dateline in clear, listed as non-decrypted. The letters <em>a</em> and <em>m</em> are nulls, the letter pairs are alternates for consonants, the rare groups are syllables, and the alphabet, recovered blind by a 5-gram-plus-dictionary annealer against shuffled controls, turns out to run in order: odd figures <em>a</em> to <em>m</em>, even figures <em>n</em> to <em>z</em>. A reminder that a promised canonry of Olm&uuml;tz for one of the Queen of Poland&rsquo;s sons has not been conferred.',
         quote='&ldquo;un canonicato d&rsquo;Olmiz ad uno de li suoi figli &hellip; si degni darne subito a me benigna risposta&rdquo;'),
    dict(slug='segur', label='S&eacute;gur', year='1585&ndash;86', y=1585, place='B&eacute;arn &rarr; Germany', st='solved', stt='solved',
         title='Henry of Navarre to S&eacute;gur &mdash; an alphabetical syllabary cipher',
         blurb='Three letters in figures to the envoy raising a German army, BnF 500 de Colbert 401 ff. 233, 239 and 288v, catalogued as undeciphered letters of Henry III. The upper figures pile into one slot in five (mod 5), the signature of a syllable table in alphabetical order; an annealer built on that structure, with the letters&rsquo; own clear French as context, returns a key whose letter part is alphabetical by itself and reads a matched control at 97&nbsp;%. Conclude with Duke Casimir, raise the largest levy, march it at once; Clervant&rsquo;s two thousand reiters; the Vivarais or Dauphin&eacute; road.',
         quote='&ldquo;faictes s&rsquo;il vous est possible la plus grande lev&eacute;e qui ayt est&eacute; faite&rdquo;'),
    dict(slug='harley7001', label='Reade 1641', year='1641', y=1641.3, place='Paris &rarr; his cousin in England', st='partial', stt='read in part',
         title='Robert Reade to his cousin, Paris, 19 April 1641 &mdash; Windebank&rsquo;s return, in the Windebank cipher',
         blurb='DECODE R7766, a letter from Paris with writer and recipient unknown, is signed R. Reade: Secretary Windebank&rsquo;s nephew and secretary, writing from the exiled household. Its two cipher passages read with the Deciphering Branch&rsquo;s reconstruction of the Windebank cipher in Add MS 32256 (DECODE R9115): whether Windebank can return under a summons without losing his person or his fortune, and a warning about Sir William St Ravy. 89% read from the key, 5% from rebuilt values, 6% conjectured.',
         quote='&ldquo;they have not enough against him to confiscate his fortune, and they would be willing to take the advantage of his refusall to return&rdquo;',
         rights='British Library, via DECODE'),
    dict(slug='boswell', label='Boswell', year='1643', y=1643, place='Oxford &rarr; The Hague', st='solved', stt='read in substance',
         title='Charles I and Nicholas to Boswell &mdash; a regular key, four signs and the wrong addressee',
         blurb='Two ciphered letters of 2 November 1643 (TNA SP 84/157). The alphabet is Robert Pitt&rsquo;s: a 24-letter row four times over 20&ndash;115, verified here at z&nbsp;=&nbsp;9.6 against 20,000 permuted rows. Added here: the four graphic signs are word-signs introduced inside the spelled word (good, Cousin, Master, us), and the King&rsquo;s letter is his re-credentials to the Duke of Courland&rsquo;s envoy, sent through Boswell in Boswell&rsquo;s cipher. Both letters read in substance.',
         quote='&ldquo;back to our good Cousin your Master, to whom we herewith send your re-credentials&rdquo;'),
    dict(slug='kurtz1639', label='Kurz von Senftenau 1639', year='1639', y=1639.1, place='Hamburg &rarr; Vienna', st='partial', stt='key rebuilt, read in part',
         title='Kurz von Senftenau to Trauttmansdorff, Hamburg 1639 &mdash; the vice-chancellor&rsquo;s cipher rebuilt',
         blurb='Nine ciphered reports of the imperial vice-chancellor from Hamburg and Gl&uuml;ckstadt, January to April 1639, in the Trauttmansdorff archive at Kl&aacute;&scaron;ter (DECODE R3811&ndash;R4736). M&iacute;rka rebuilt the key in 2012 and read one letter but printed nothing. From the same interlinear glosses the key falls out as a regular table: 41&ndash;100 are consonant&ndash;vowel syllables, two consonants to each ten in reverse alphabetical order, and the low numbers are homophones. All nine letters decipher in a first pass: Ban&eacute;r in Lower Saxony, Arnim&rsquo;s bid for pardon, the Danish mediation and its collapse.',
         quote='&ldquo;besser ein ungeschlossener, durch den Feindt zertrennter Craistag als ein geschlossener mit einer expressen Neutralitet&rdquo;',
         rights='St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE R3811&ndash;R4736'),
    dict(slug='marburg1635', label='Marburg cipher report', year='1635&ndash;52', y=1635.5, place='Unknown &rarr; Hesse-Kassel', st='solved', stt='read',
         title='The Marburg cipher report &mdash; a Hesse-Kassel letter&rsquo;s digit cipher rebuilt and read',
         blurb='DECODE R4500, a German report in Hesse-Kassel&rsquo;s cipher files at Marburg, ends in fourteen lines of digits and signs, with a contemporary gloss over the first four. No key sheet in the volume fits; the key was rebuilt by annealing against a sixteenth-century German model and checked against the gloss. The passage reads: the writer has reported to the Emperor and the Elector of Bavaria and asks to be held excused. Nine signs stay open.',
         quote='&ldquo;damit ich aus allen fall entschuldigt sein&rdquo;',
         rights='Hessisches Staatsarchiv Marburg, HStAM 4 d Nr. 1218, via DECODE'),
    dict(slug='heusner1637', label='Heusner 1637', year='1637', y=1637.4, place='Kassel &rarr; Oxenstierna', st='found', stt='read by others',
         title='Heusner von Wandersleben to Oxenstierna, 1637 &mdash; already read by Waldisp&uuml;hl and Kopal',
         blurb='A German numerical homophonic letter from Kassel, catalogued twice (DECODE R4332 &ldquo;partly solved&rdquo;, R3816 &ldquo;not solved&rdquo;). The two records carry the same three scans, and the letter was deciphered by Michelle Waldisp&uuml;hl and Nils Kopal (HistoCrypt 2024). Their key, applied here to a fresh transcription of one page, reproduces their reading. The letter is dated 15 May 1637, not March; the code numbers stay open.',
         quote='&ldquo;am ganzen Hofe ausser der 503 nicht einer mehr uffrecht schwedisch&rdquo;',
         rights='Riksarkivet, Stockholm, via DECODE R4332'),
    dict(slug='rupert1645', label='Charles I to Rupert 1645', year='1645', y=1645.33, place='Oxford &rarr; Prince Rupert', st='solved', stt='read',
         title='Charles I to Prince Rupert, 29 April 1645', blurb='A holograph cipher letter of the King to his nephew, catalogued as undeciphered (BL Add MS 18983 f. 14, DECODE R4921). Read with George Lasry&rsquo;s reconstruction of the King&rsquo;s cipher with the Queen, applied unchanged: the King cannot convoy his artillery train and asks Rupert to march and fetch it. About twenty code groups stay open.', quote='that in case I can not bring my train of artillery to you, you may come and fetch it', rights='British Library, via DECODE'),
    dict(slug='hm1645', label='Henrietta Maria 1645', year='1645&ndash;46', y=1645.7, place='St Germain &rarr; Charles I', st='found', stt='read by others',
         title='Henrietta Maria&rsquo;s household to Charles I, 1645&ndash;46 &mdash; already read by George Lasry',
         blurb='Six numerical homophonic letters in TNA SP 106/10, catalogued as undeciphered and still on Tomokiyo&rsquo;s unsolved list. The DECODE records carry George Lasry&rsquo;s reconstructed keys and plaintexts for the whole run, ff. 207&ndash;247 (October 2020). Only the nomenclator numbers are left open. His key, applied here to the raw transcription of f.&nbsp;247, reads it at once.',
         quote='&ldquo;no hope of money from thence but upon new termes &hellip; a total takeing away of al the penall lawes against papists&rdquo;',
         rights='The National Archives, Kew, via DECODE R785&ndash;R929'),
    dict(slug='forster', label='Forster', year='1644', y=1644.2, place='France', st='found', stt='read by others, verified',
         title='Sir Richard Forster, 13 May 1644 &mdash; verified blind, and why the first attack fails',
         blurb='Already read by Lasry, Biermann and Pitt; Tomokiyo&rsquo;s page still says unsolved. Not a regular Stuart key but a mixed homophonic alphabet of 34 symbols over 207 tokens. Pitt&rsquo;s key stands at z&nbsp;=&nbsp;8.8 against 20,000 permutations, and an annealer recovers 31 of 34 symbols blind &mdash; but only after the French model writes <em>u</em> for <em>v</em> and <em>i</em> for <em>j</em>; before that it reads five of six matched controls and still fails the target.',
         quote='&ldquo;prenez seulement les uoyes de prudence pour conseruer uotre uie&rdquo; &middot; 202 of 207 tokens blind'),
    dict(slug='lucca', label='Lucca', year='1644', y=1644, place='Vienna', st='solved', stt='solved',
         title='Fra Giovanni di Lucca to the Emperor &mdash; a polyphonic figure cipher',
         blurb='DECODE R2159, 231 dot-delimited figures of Italian, listed as non-decrypted and left half-read on Tomokiyo&rsquo;s page because its crib is self-contradictory under any substitution. It is a 24-figure alphabet in which 17 stands for both <em>i</em> and <em>n</em> and 19 for both <em>t</em> and <em>s</em>. Eight crib letters fixed, the rest annealed, every seed agrees, shuffled controls do not; a Viterbi pass over the two alternatives reads it end to end: an offer to keep the Turk off R&aacute;k&oacute;czi, raise Moldavia against him and give two thousand Cossacks.',
         quote='&ldquo;il principe di Bogdania, et li dar&ograve; dumilia Cosachi &hellip; che non faccia pace fin che l&rsquo;habbi humiliato o vinto&rdquo;'),
    dict(slug='hernannunez1674', label='Hern&aacute;n N&uacute;&ntilde;ez 1674', year='1674', y=1674.9, place='Stockholm &rarr; Copenhagen', st='solved', stt='read',
         title='The Conde de Hern&aacute;n N&uacute;&ntilde;ez to Fuenmayor, 1674 &mdash; four Stockholm despatches read with the Balbases key',
         blurb='Four December 1674 despatches from Spain&rsquo;s envoy in Sweden to its envoy in Denmark, clear Spanish with cipher passages deciphered in the margin at the time. Aligning the margins showed the cipher to be the one rebuilt here for Balbases 1677; that key reads all four unchanged, verifying the margins and recovering what DECODE could not read. Sweden on the eve of the Scanian War: the senate about to decide on arming for France.',
         quote='se tomar&aacute; resoluci&oacute;n en &eacute;l sobre el asistir o no a la Francia a mano armada',
         rights='Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R1012&ndash;R1015'),
    dict(slug='ronquillo1676', label='Salinas &amp; Ronquillo 1676', year='1676&ndash;78', y=1677.1, place='London, Nijmegen &rarr; Copenhagen', st='partial', stt='read in part &mdash; 88% of groups',
         title='Salinas and Ronquillo to Fuenmayor, 1676&ndash;78 &mdash; twenty letters in one shared cipher, four read for the first time',
         blurb='The rest of Fuenmayor&rsquo;s ciphered correspondence in Brussels: eight letters from Spain&rsquo;s envoy in London and twelve from its plenipotentiary at Nijmegen. The key rebuilt here for Balbases reads all twenty unchanged, 88% of 23,463 groups, once six boundary-less DECODE transcriptions are re-segmented. Sixteen margins are confirmed; four letters without one, two catalogued as non-decrypted, are read only in gist, so the set stays read in part.',
         quote='ni de la paz ni de la guerra mientras no tuviremos apariencias m&aacute;s ciertas',
         rights='Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R966&ndash;R984, R1001'),
    dict(slug='balbases1677', label='Balbases 1677', year='1677&ndash;78', y=1677.6, place='Nijmegen &rarr; Copenhagen', st='solved', stt='read',
         title='The marqu&eacute;s de los Balbases to Fuenmayor, 1677&ndash;78 &mdash; a Nijmegen plenipotentiary&rsquo;s cipher rebuilt and four undeciphered letters read',
         blurb='Fourteen ciphered letters from Spain&rsquo;s plenipotentiary at the Nijmegen congress to its envoy in Denmark. Ten carry a contemporary decipherment in the margin; four, of September 1677 and March 1678, carry none, and no key survives. The key was rebuilt from the ten margins by anchoring repeated words and aligning: letters and syllables in numbers, disguised letter-pair syllables, reversed vowel-first pairs and some twenty word codes. It reads all fourteen, down to the fear after the fall of Ghent.',
         quote='con la p&eacute;rdida de Gante estamos temiendo la de otras importantes plazas',
         rights='Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R985&ndash;R998'),
    dict(slug='carpio1677', label='Carpio 1677', year='1677', y=1677.8, place='Rome &rarr; Copenhagen', st='solved', stt='read',
         title='The Marqu&eacute;s del Carpio to Fuenmayor, 1677 &mdash; a Spanish ambassador&rsquo;s syllabic cipher rebuilt and all ten letters read',
         blurb='Ten ciphered letters from Spain&rsquo;s ambassador in Rome to its envoy in Denmark, eight deciphered in the margin without the key and two catalogued as non-decrypted. The key was rebuilt from the letters: numbers for letters and for syllables in rows of five, struck numbers for a second syllable table, and letter pairs that are syllables with a disguised consonant. It reads all ten: the French fleet at Messina and Catania, Orange raising the siege of Charleroi, Innocent XI refusing Carpio an audience, and Cardinal d&rsquo;Estr&eacute;es at Turin.',
         quote='la pr&oacute;xima campa&ntilde;a habr&aacute; guerra en Mil&aacute;n, pues el Cardenal de Estr&eacute;es, que est&aacute; en Tur&iacute;n, no se descuida',
         rights='Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R1002&ndash;R1011'),
    dict(slug='feuquieres', label='Feuqui&egrave;res', year='1691', y=1691, place='Pignerol &rarr; Suze', st='solved', stt='read',
         title='Feuqui&egrave;res to Catinat &mdash; the petit chiffre of the Pignerol governors',
         blurb='The 418-group despatch of 25 January 1691 that the 1819 editor of Catinat&rsquo;s papers could not read and Bazeries read but never printed. The same edition prints a second letter in the same 367-group code, Louvois to d&rsquo;Herleville of 6 September 1690, with its contemporary translation; the two letters share 72 groups, and hand alignment carried between them reads 586 of their 601 tokens. Feuqui&egrave;res&rsquo; plan for the surprise of Veillane: two roads into the town, eighty horse to Saint-Ambroise, an attack at two points, and the dragoons not to be let escape into the castle.',
         quote='&ldquo;j&rsquo;attaqueray [par] deux endrois, et surtout &hellip; prendray garde que les dragons ne puissent m&rsquo;eschaper&rdquo;',
         rights='Page images: Bayerische Staatsbibliothek, CC BY-NC-SA'),
    dict(slug='catinat1691', label='Catinat 1691', year='1691', y=1691.5, place='Versailles &rarr; Piedmont', st='solved', stt='read',
         title='Louis XIV and Louvois to Catinat &mdash; seven Grand Chiffre despatches, and the decision to abandon Piedmont',
         blurb='The 1819 editor of Catinat&rsquo;s papers printed seven court despatches of July&ndash;September 1691 in figures and could not read them; Bazeries rebuilt the code from them in 1893, printed two in clear for the Man in the Iron Mask, and stopped. His table reads all seven from the library&rsquo;s OCR of the volume, 12,362 groups, checked against the page images; the two he printed agree at 98 and 99 %. The other five are read here for the first time, among them the King&rsquo;s twenty-page letter of 14 September: bring the army back over the Alps, hold the passes, keep Carmagnole to cover the negotiation with the Pope, then burn it, and take Coni in the winter.',
         quote='&ldquo;je me suis d&eacute;termin&eacute; &agrave; pr&eacute;f&eacute;rer le parti solide &agrave; l&rsquo;honorable&rdquo; &middot; Louis XIV, 14 September 1691',
         rights='Page images: Bayerische Staatsbibliothek, CC BY-NC-SA'),
    dict(slug='herbault1626', label='Herbault', year='1626', y=1626, place='Paris &rarr; Rome', st='solved', stt='resolved',
         author='Arya Sanketbhai Patel',
         title='Herbault to B&eacute;thune, 13 February 1626 &mdash; the decipherment three folios away',
         blurb='The one letter marked &ldquo;avec chiffre&rdquo; and not &ldquo;avec chiffre et d&eacute;chiffrement&rdquo; among some thirty of 1625&ndash;26 to the ambassador in Rome. It is not an undeciphered text: no. 26 is not a second letter but the same despatch, carrying the same cipher with the plaintext written between the lines in 1626. Identity fixed on the word-for-word clear text, the cipher runs falling at the same points and matching groups. The ciphered passages are the papal Legate and &ldquo;le Pape pour l&rsquo;acheminement de ces troupes in la Valteline&rdquo;, the admission that France made peace with the Huguenots because &ldquo;le faix d&rsquo;une double guerre ne se pouvoit plus supporter&rdquo;, the Dutch squadron sailing home with the Huguenot admiral, and Savoy&rsquo;s attempt to engage France against Spain six weeks before Monz&oacute;n. Contributed by Arya Sanketbhai Patel.',
         quote='&ldquo;principallement sy le Pape entroit dans la partialit&eacute;&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='sormano1529', label='Sormano', year='1529', y=1529, place='Ferrara &rarr; France', st='partial', stt='key supplied, substance read',
         author='Arya Sanketbhai Patel',
         title='Sormano and Passano from Ferrara &mdash; eight failures, a published key, and two corrections',
         blurb='Three ciphered letters of Fran&ccedil;ois I&rsquo;s agents at Ferrara, February 1529. Eight independent methods failed on a 1960s microfilm that will not separate thirty-six symbol forms &mdash; and then George Lasry&rsquo;s 2023 key, published all along on a page I had not searched, read them. It also graded the attempt: 20 of the 22 values derived here were right, and the two wrong ones were exactly what had blocked it. The Duke&rsquo;s answer comes out as <em>&ldquo;risolutamente concluse per cosa dil mondo non voler &hellip; se alcunamente accetare il regno&rdquo;</em> &mdash; Alfonso d&rsquo;Este refusing the kingdom for nothing in the world. With the documentary findings from the failure: no. 63&rsquo;s lost third sheet, the duplicate that cribs its twin, and Passano identified. The page also records two things this write-up previously got wrong. Contributed by Arya Sanketbhai Patel.',
         quote='&ldquo;per cosa dil mondo non voler &hellip; accetare il regno&rdquo; &middot; 20 of 22 values right',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='hesse1603', label='Hesse', year='1602&ndash;09', y=1605, place='Paris &rarr; Kassel', st='solved', stt='read',
         author='Arya Sanketbhai Patel',
         title='Henri IV to Landgrave Maurice &mdash; the figures Rommel printed in 1840 and the key he printed in 1846',
         blurb='Rommel set the King&rsquo;s ciphered passages to the Landgrave of Hesse-Kassel as rows of figures he could not read, then printed the key six years later with one sample and stopped. Put together, they read all seven passages, about 4,100 groups: Bouillon and the German princes, the Gunpowder Plot and M&eacute;rargues &ldquo;forg&eacute;s sur mesme enclume&rdquo;, two million livres for the Dutch, and on 20 May 1606 the call to the princes to take counsel together against a Spanish King of the Romans, &ldquo;pour la conservation de la libert&eacute; germanique&rdquo;. Contributed by Arya Sanketbhai Patel.',
         quote='&ldquo;tous les roys et princes qui doivent avoir jalousie de l&rsquo;agrandissement &hellip; de la puissance espagnole doibvent d&rsquo;heure aviser et prendre conseil ensemble&rdquo;',
         rights='Page images: Internet Archive'),
    dict(slug='urquhart', label='Urquhart', year='1652', y=1652, place='London', st='solved', stt='octastich read',
         title='Urquhart&rsquo;s Cyphral Octastich &mdash; a book cipher on his own Jewel, read without the plaintext',
         blurb='Eight lines and a &ldquo;Decagram&rdquo; of numbers on the last leaf of The Jewel (1652), Schmeh&rsquo;s Top 50 no. 28. Number k indexes a word on physical page k of the book, and Urquhart took the first word of the initial he needed: a habit checkable without any plaintext. The public transcription was thirteen numbers short; the 1983 edition&rsquo;s photographs on the HCPortal give 285, which decode straight with 238 of 284 first-occurrence hits against 0.43 for shuffled and random-page controls, into a royalist prayer for Charles II. Vals AI published the rule in August 2026 as a Claude Fable 5.1 result; the companion distich claim does not reproduce.',
         quote='&ldquo;Great Lord, mantaine that regal familie &hellip; Our Emperour, King, Monarch and Protector&rdquo;'),
    dict(slug='reserva12', label='Reserva 12', year='1413&ndash;16', y=1414, place='Barcelona &rarr; the King of Aragon', st='found', stt='read in 1931',
         title='A Catalan letter in transposition, Barcelona 2 May [1413&ndash;16] &mdash; ACA Reserva 12',
         blurb='The oldest item on DECODE with a public image, listed as an undeciphered cipher of unknown type. It is a Catalan letter to the King written down the columns of each block, the word chunks cut by slashes, and Xavier de Salas explained the rule and printed the whole text in 1931, in the article the record itself cites. The rule is checked here on the image: the first block reads <em>Senyor, jo us auie quezacom escrit&hellip;</em> A royal financial officer in Barcelona, with Roger de Pallars, urges Ferdinand I to leave Val&egrave;ncia and hold the corts, and defends his own accounts.',
         quote='&ldquo;No us anugets de legir, car con lest ho ajats prazer n&rsquo;aurets e no playarets l&rsquo;afany&rdquo;',
         rights='Manuscript rights: Arxiu de la Corona d&rsquo;Arag&oacute;'),
    dict(slug='heidelberg597', label='Alchymey teuczsch', year='1426', y=1426, place='East Bavaria, near Passau', st='found', stt='read in 1869',
         title='Alchymey teuczsch, 1426 &mdash; the sign alphabets of an alchemists&rsquo; notebook (Cod. Pal. germ. 597)',
         blurb='A German recipe book of a circle of gold-makers near Passau, dated 1426 and listed on DECODE as non-decrypted, with substance names hidden in three home-made sign alphabets. The compiler wrote the key on the first leaf as one unbroken run of signs &ldquo;so that no one should understand that it is an alphabet&rdquo;, then struck it through. Wilhelm Wattenbach read it in 1869 and printed three facsimiles with their plaintexts. Here the struck alphabet of f.&nbsp;1r and the invocation alphabet of f.&nbsp;6v are recovered from the images and checked against his readings, a third set is partly fixed from the Heidelberg catalogue&rsquo;s reading of f.&nbsp;93r, and the book is ruled out as a record candidate.',
         quote='&ldquo;Das ist ein abc vnd das haben wir selbs neus gemacht&rdquo;',
         rights='Manuscript images: Universit&auml;tsbibliothek Heidelberg, Public Domain Mark'),
    dict(slug='florence1429', label='Ricasoli 1425', year='1425', y=1425, place='Urbino &rarr; Florence', st='solved', stt='read',
         title='Galeotto da Ricasoli to the Dieci di Bal&iacute;a, Urbino 1425 &mdash; Read',
         blurb='A letter of Florence&rsquo;s envoy to the Count of Urbino, listed on DECODE as non-decrypted, though its interlinear decipherment makes it decrypted; what the record lacks is the key or a reference to it. The abb&eacute; Gabbrielli glossed a few of its words in 1863 and built a key from them, which Meister printed in 1902; the letter was never printed. The three long runs he left unread are decoded sign by sign with his glosses as seeds, two of his nulls resolved and four new values confirmed on the siblings.',
         quote='&ldquo;perch&eacute; dice che Madonna &egrave; pure femina e sospetosa&rdquo;',
         rights='Manuscript images: Archivio di Stato di Firenze, via DECODE R3754'),
    dict(slug='maria1435', label='Mar&iacute;a 1435', year='1435', y=1435, place='Valencia &rarr; Gaeta', st='stuck', stt='not read, keys tested',
         title='Queen Mar&iacute;a to Alfonso V, Valencia 1435 &mdash; Attempted',
         blurb='The oldest unread ciphertext on DECODE with a public image: 42 signs inside a Catalan letter of Queen Mar&iacute;a to Alfonso V, written in Valencia on the day of Ponza, about something &ldquo;continued until All Saints&rdquo;, almost certainly the truce with Castile. Both printed Aragonese keys of the decade were tested: the 1437 alphabet is unrelated, and the 1429 nomenclator seems to match the word signs while its alphabet does not. Four neighbouring registers, 1,414 images, hold no cipher at all; the king&rsquo;s own register shows his letter to her of 27 July 1435 was sent <i>in ciffra</i>.',
         quote='he treballat que [&#541; a ff 8 9 d 3 8 v 8 6 8 2 &#8857;] es continuada daci a tots sants',
         rights='Images: Arxiu de la Corona d&rsquo;Arag&oacute;, via DECODE R10171 and PARES'),
    dict(slug='it1583', label='Zorzo Maino 1446', year='1446', y=1446, place='Sforza chancery &rarr; Giorgio del Maino', st='stuck', stt='not read, keys scanned',
         title='A reply to Zorzo Maino, 4 May 1446 &mdash; Attempted',
         blurb='An undescribed DECODE slip (R7898) turns out to be, by Mazzatinti&rsquo;s 1883 inventory, the Sforza side&rsquo;s reply to its agent Giorgio del Maino: clear Lombard Italian with runs of invented signs. A second cipher of the same day, Vincenzo Amidani&rsquo;s from Milan, was found photographed on R7899. Both were transcribed and annealed without result. Among the 208 Sforza keys on DECODE, Simonetta&rsquo;s cipher with Vincentius shows the family uses syllable and word signs, but no key matches.',
         quote='ne cerchamo ne domandamo [cipher] tocha ad nuy cerchare questo',
         rights='Biblioth&egrave;que nationale de France, via DECODE R7898 (no image reproduced)'),
    dict(slug='matthias1482', label='Matthias 1482', year='1482', y=1482, place='Pozsony &rarr; Ferrara', st='found', stt='read in 1877',
         title='Matthias Corvinus to Ercole I d&rsquo;Este, Pozsony 1 June 1482 &mdash; DECODE R1156',
         blurb='The King of Hungary answers Ferrara&rsquo;s call for help in the first weeks of the War of Ferrara, with troops, route, names and plan in a sign cipher. DECODE lists it as partly decrypted, but it was printed in 1877 and again by Fraknói in 1895. The runs are read here from the image and a working key rebuilt; four garbled places in the printed text are corrected, among them the closing sentence the edition prints as nonsense.',
         quote='&ldquo;Speramus cito nos res nostras ita disposituros, ut meliori postea modo vos iuvare possemus&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Modena (images not reproduced)'),
    dict(slug='sadoleto1482', label='Sadoleto 1482', year='1482', y=1482.5, place='Pozsony &rarr; Ferrara', st='solved', stt='read',
         title='Nicol&ograve; Sadoleto to Ercole I d&rsquo;Este, Pozsony 1482 &mdash; the Venetian counter-offer to Matthias Corvinus',
         blurb='Ferrara&rsquo;s envoy at the Hungarian court in the first summer of the War of Ferrara wrote parts of his despatches in a sign cipher; they were never printed, and DECODE lists four as partly decrypted. The alphabet is rebuilt from two sibling letters filed with their contemporary clear copies, which also shows that two of the four targets were read at the time. The cipher of 16 July 1482, which has no clear copy, is read but for a few words under stains and the fold: Venice had offered Matthias Veglia, a fleet command for his natural son J&aacute;nos Corvin and a hundred thousand ducats a year, and Sadoleto urged that the League match it. A faded block of 17 August gives fragments only.',
         quote='&ldquo;et voleva dargli Vegla, et voleva lo figlio (e bastardo) per loco capitaneo &hellip; per mare, et gli voleva dare ogni anno cento milia&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Modena (images not reproduced)'),
    dict(slug='buda1489', label='Buda 1489', year='1489&ndash;90', y=1489, place='Buda &rarr; Milan', st='solved', stt='read',
         title='Maffeo da Treviglio to Ludovico Sforza, Buda 1489&ndash;1490 &mdash; the key reconstructed in 2016 had never been turned back into signs',
         blurb='Judit W. Somogyi reconstructed the cipher of Ludovico Sforza&rsquo;s ambassador at the court of Matthias Corvinus in 2016, but printed it only as a table of numbers, with no image of a single sign, so nothing could be read with it. Her numbering turns out to follow the order of first appearance in the letter of 2 April 1490, which survives with its contemporary clear copy: matching the two gives the shapes back, and about twenty further signs came out of the reading. The two despatches that have no decipherment are now read. The four pages of 22 November 1489, of which only the first two lines had been published deciphered, cover the peace with Frederick III, the Diet, the marriage of John Corvinus against the rival Neapolitan match, the queen&rsquo;s &ldquo;insatiable wrath of Juno&rdquo;, and a warning that intercepted cipher letters had been read; the letter of 12 January 1490 reports the king riding to Vienna on the 8th and the ambassadors following on the 15th, which its own clear second page confirms word for word.',
         quote='&ldquo;Le littere in cifra che forono intercepte, le quale duplicate sono state scoperte ancora qua&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Milano (images not reproduced)'),
    dict(slug='esp318', label='Espagnol 318', year='1497&ndash;1504', y=1497, place='Naples, Venice, Messina &rarr; Spain', st='partial', stt='keys found, two part read',
         title='Espagnol 318 &mdash; five ciphered letters of the Catholic Monarchs, and which keys open them',
         blurb='The oldest item in the catalogue, and four different answers. No.&nbsp;5 was never open: Ivan Parisi printed the whole text in 2020, having found that the king of Naples had his secret letter enciphered in the Spanish ambassador&rsquo;s own cipher, by the ambassador&rsquo;s hand. No.&nbsp;92, the Great Captain to Lorenzo Su&aacute;rez of 17 August 1500, is written in the <em>Cifra general de los Reyes Cat&oacute;licos</em> that Galende D&iacute;az printed in 1994 &mdash; proposed by Tomokiyo from the look of the code groups, proved here against eight words a later hand wrote between the lines, with no misses; both pages are now transcribed and about three quarters read: the Great Captain&rsquo;s price for joining Venice against the Turk in 1500, harbours in Italy for his sick, wounded and stores. No.&nbsp;95 has George Lasry&rsquo;s alphabet and no published text: segmenting and clustering its 963 signs reads about two thirds, Spanish, about the French and about what a <em>Se&ntilde;or&iacute;a</em> can be brought to do. Nos.&nbsp;93 and 94 stay unread but are named: their code initials exclude both printed keys and point at the <em>Gran cifra</em> of 1501&ndash;04, whose only reconstruction sits in a Madrid manuscript that is not served online.',
         quote='&ldquo;y tiempo, por estar en tanto&rdquo; &middot; the glossator&rsquo;s own words, from the printed key',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='poyntz1527', label='Poyntz 1527', year='1527', y=1527.54, place='Valladolid &rarr; Wolsey', st='found', stt='read at the time',
         author='Arya Sanketbhai Patel',
         title='Ghinucci, Lee and Poyntz to Wolsey, Valladolid 1527 &mdash; read at the time',
         blurb='DECODE R8565, catalogued as a ciphered letter of Francis Poyntz to an unknown recipient, is the separated second part of the joint despatch of Ghinucci, Lee and Poyntz to Cardinal Wolsey, Valladolid 17 July 1527 (<em>Letters and Papers</em> IV no. 3271). The folio offset from its neighbour R8566 places it, and the public thumbnails fit. Its short passages in the Lee&ndash;Worcester sign cipher are deciphered between the lines, and Tuke&rsquo;s decipherment is in print: Milan and the daughter of Portugal for the duke of Richmond, and the French envoy&rsquo;s secret fourth instruction.',
         quote='&ldquo;the Emperor might give it along with the daughter of Portugal to the duke of Richmond&rdquo;',
         rights='Manuscript: British Library, Cotton MS Vespasian C IV (images on DECODE, not reproduced)'),
    dict(slug='vasto1527', label='Del Vasto 1527', year='1527&ndash;28', y=1527.8, place='Rome and Madrid &rarr; Charles V', st='partial', stt='two of three read',
         title='Del Vasto to Charles V and a letter to &ldquo;Garbino&rdquo;, 1527&ndash;28 &mdash; one found solved, one read, one without its key',
         blurb='Three imperial ciphers in BnF fr. 3022, listed with no decipherment. Del Vasto&rsquo;s letter from Ischia of 27 September 1527 had been solved by George Lasry and Satoshi Tomokiyo. The anonymous &ldquo;report&rdquo; is del Vasto&rsquo;s own letter of December 1527: Lasry had its letters, and about forty of its code groups are identified here, which makes it readable as his plan to march on Siena, Perugia and Urbino. The Madrid letter to &ldquo;Garbino&rdquo; is in Hieronimo Ranzo&rsquo;s initial-letter code. Its numbering is not alphabetical, and without the table only its function words come out.',
         quote='&ldquo;el ex&eacute;rcito por lo de advenir no se puede sostener desta manera&rdquo; &middot; del Vasto, December 1527',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='raince', label='Raince', year='1526', y=1526, place='Rome &rarr; the Court', st='solved', stt='read',
         title='Raince to Montmorency, Rome, 1526 &mdash; the key was misread by one column',
         blurb='Eight ciphered despatches of the French embassy&rsquo;s secretary at Rome sit in BnF fr. 2984; about 106 lines of them, the 13 May and 20 November 1526 letters to Montmorency, exist in no edition. The obstacle was never cryptanalytic. Tomokiyo published the key in 2020, but reading which glyph sits under which letter in his table by eye slips a column: <em>l</em>, <em>m</em> and <em>n</em> were each a place wrong, and every reading built on it was corrupt. Measured off the image instead &mdash; every ink blob within 15&nbsp;px of a header column &mdash; the table resolves a control line glyph for glyph with nothing left over, and 86 of the 106 lines then read by hand from the microfilm. Nine days before the League of Cognac: the Castilians and the Bourguignons, <em>le chemin de Valence</em>, a capitulation for which <em>ilz seront cause de la destruction</em>, the plague in Rome, advices reaching the Imperials by their own people, and a man taken <em>un jour, en plaine place pres du palais</em>. Two months after the Colonna raid, a pontificate that <em>seroit la cause de la totale ruine de sa maison</em>. The clear close of 13 May, transcribed here, expects Andrea Doria at Civitavecchia within a day with six galleys.',
         quote='&ldquo;qui estoit en la court de Savoye est party pour venir icy&rdquo; &middot; &ldquo;[le] pontificat seroit la cause de la totale ruine de sa maison&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='sormano', label='Sormano 1529', year='1529', y=1529.2, place='Ferrara &rarr; the Court', st='solved', stt='read',
         title='Sormano and de Vaulx to Fran&ccedil;ois I, February 1529 &mdash; the duke of Ferrara declines the crown of Naples',
         blurb='Three ciphered despatches of the French agents at Ferrara, BnF fr. 3096 nos. 63, 65 and 66, listed unread beside two glossed siblings. Lasry&rsquo;s key holds; the leaves add a null, a nomenclator for the duke and four letter forms. Eighteen thousand signs segmented from the Gallica scans, clustered and classified, then every line read on review sheets; the duplicate pair, which enciphers different stretches, checks itself. Alfonso d&rsquo;Este will not take the kingdom or the captaincy of the French army, and the agents call his difficulties pretexts, eight months before Cambrai.',
         quote='&ldquo;risolutamente concluse per cosa dil mondo non voler per s&eacute; alcunamente accettare il regno et manco far l&rsquo;impresa a suo nome&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='egmond', label='Charles of Egmond', year='18 July (?) · year unknown', y=1525, place='Arnhem &rarr; grand master of France', st='solved', stt='read; minor uncertainties',
         title='Charles of Egmond &mdash; a ciphered request for support in war',
         blurb='A cipher George Lasry had already solved in 2023 (key on cryptiana), solved again here independently: the French body and ciphered address read with an inferred graphic substitution key and nulls. Charles asks the grand master to support his affairs and assist the commander of Saint John. Arnhem, apparently 18 July; year unknown. Minor glyph uncertainties and literal anomalies remain explicit.',
         quote='lequel est cause que suis entre en ceste guerre', rights='Biblioth&egrave;que nationale de France / Gallica'),
    dict(slug='gramont1529', label='Gramont 1529&ndash;37', year='1529&ndash;37', y=1529.8, place='Rome, Venice &rarr; the Court', st='solved', stt='read',
         title='Gramont, M&acirc;con and Langeac to Montmorency, 1529&ndash;1537 &mdash; four keys and texts Lasry solved in 2023, read again in public',
         blurb='Four ciphered letters to the grand ma&icirc;tre from the French ambassadors at Rome and Venice, catalogued with no decipherment. Each has its own key. Lasry reconstructed all four from siblings in 2023 and decoded the texts then, but his decipherments were never posted. Read again here from the scans with his tables: Saint-Pol and the Venetians in January 1529; Clement VII on the council, his dream and his feigned illness on the road to Bologna in October 1529; the princes&rsquo; return in 1530; Paul III and the Farnese marriage in 1537.',
         quote='&ldquo;le concile general, lequel il craignoit sur toutes les choses de ce monde&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='caracciolo1537', label='Caracciolo 1537', year='1537', y=1537.87, place='Milan &rarr; Charles V', st='solved', stt='read',
         title='Cardinal Caracciolo to Charles V, 14 November 1537 &mdash; a published key, read through, past the first four lines',
         blurb='A letter from Milan catalogued on DECODE as Non-decrypted. Its eleven cipher lines are in the cipher Charles V used with Caracciolo from 1530 to 1538, reconstructed by Wanruo Luo in 2021 as Cifrario 38: a sign alphabet with homophones and a syllabary of consonant signs with superscript vowel digits. Tomokiyo had named the key and read four lines. The key reads the whole passage unchanged; about ten signs stay doubtful.',
         quote='&ldquo;se accorge hora de la malignita et perfidia de Suiza[..]&rdquo;',
         rights='Espa&ntilde;a, Ministerio de Cultura, Archivo General de Simancas, via DECODE'),
    dict(slug='marechaux1520', label='Campeggio&rsquo;s articles 1534', year='c. 1534', y=1534.8, place='Rome &rarr; Francis I', st='solved', stt='read',
         title='Cardinal Campeggio&rsquo;s conclave articles for Francis I, c. 1534',
         blurb='Catalogued as a letter of the French marshals to the King dated 1520 (BnF fr. 3081 f. 41, DECODE R2322), the two cipher pages are a copy of the articles Cardinal Campeggio swore to the cardinals Bourbon, Lorraine and Tournon: if elected pope, he would work for the return of Milan, Asti and Genoa to Francis I. George Lasry read the first page in 2022; the second, unpublished, is read here with his key and a few sign corrections.',
         quote='&ldquo;s&rsquo;il plaist a Dieu me donner grace d&rsquo;estre pape&rdquo;',
         rights='Biblioth&egrave;que nationale de France, via DECODE R2322'),
    dict(slug='rome1536', label='M&acirc;con 1536&ndash;37', year='1536&ndash;37', y=1536.5, place='Rome, Orvieto &rarr; the grand ma&icirc;tre', st='solved', stt='read',
         title='The cardinal de M&acirc;con in Rome to Montmorency, 1536&ndash;1537 &mdash; eight letters from an &ldquo;unknown sender&rdquo;',
         blurb='Eight ciphered records of BnF fr. 3053, catalogued as an unknown correspondent writing to Anne de Montmorency from Rome. The sender signs three of them in clear: Charles H&eacute;mard de Denonville, bishop and then cardinal of M&acirc;con, ambassador to Paul III. Tomokiyo reconstructed the cipher from this very volume and Lasry re-tabulated it in 2023, but nobody published a word of the text. Seven records are now read in part and the eighth resolved &mdash; its cipher is a second fr. 3053 key whose contemporary decipherment stands on the next leaf. The Pope manoeuvring over the general council and the Germans, Andrea Doria&rsquo;s galleys and a suspected secret treaty, Milan refused to the Farnese, the Sienese exiles, a conclave weighed while Paul III fails, and an estate in France offered to the Pope&rsquo;s son.',
         quote='&ldquo;le dict pape vouloit entretenir le roy de mariage &hellip; pour ce s&rsquo;en prevaloir vers le dict Empereur&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France; images via DECODE'),
    dict(slug='lopehurtado', label='Lope Hurtado 1522', year='1522', y=1522.8, place='Rome &rarr; Charles V', st='partial', stt='cipher broken, four letters read',
         title='Lope Hurtado de Mendoza at Rome, 1522 &mdash; an unpublished cipher broken, four letters read',
         blurb='Nine records in RAH Salazar 9/26, catalogued as part of Alonso S&aacute;nchez&rsquo;s Venice correspondence among which they are bound. They are in a different cipher, and nobody had published it: Tomokiyo&rsquo;s 2025 article covers S&aacute;nchez&rsquo;s and Juan Manuel&rsquo;s and not this. The crib was in the volume &mdash; R9644 and R9650 each carry the clerk&rsquo;s own full contemporary clear version beside the cipher, keyed by marginal letters. Fifty-seven values fixed against that plaintext; the key then reads two thirds of the tokens in records DECODE calls non-decrypted, and reads <i>el papa</i> unaided in a letter with no crib at all. Four of the nine are read complete as to content: Adrian VI temporising between Charles V and Francis I, the French coming into Italy with a great sum of money to Lyon, a Pope too parsimonious to pay his own household.',
         quote='&ldquo;tomalo tan tibiamente que no se espera de todo bien&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='poupet1522', label='La Chaulx 1522', year='1522', y=1522.4, place='Vitoria &rarr; Charles V', st='found', stt='read at the time',
         title='La Chaulx to Charles V, Vitoria 1522 &mdash; read at the time',
         blurb='DECODE R1187, catalogued as an unread Spanish cipher letter of 1 January 1522, is a French despatch of Charles de Poupet, sieur de La Chaulx, envoy to Adrian VI, dated Vitoria 28 May 1522. Its five homophonic cipher passages, marked A to E, are read in the contemporary decipherment bound in as MSS/20212/39/2; the first line was checked against it. The cipher covers the Pope&rsquo;s sailing: plague at Barcelona, the galleys of Naples, 4,000 men rumoured as 20,000.',
         quote='&ldquo;il fait courre le bruit quil emmenera vingt mille&rdquo;',
         rights='Manuscript images: Biblioteca Nacional de Espa&ntilde;a, via DECODE R1187'),
    dict(slug='sanchez1522', label='S&aacute;nchez 1522', year='1522', y=1522.5, place='Venice &rarr; Charles V', st='found', stt='already solved; entry corrected',
         title='Alonso S&aacute;nchez at Venice, 1522 &mdash; the cipher was already solved, and the catalogue entry was wrong',
         blurb='Twenty-nine DECODE records (RAH Salazar 9/23&ndash;9/26, R9593&ndash;R9657) held here as unread ciphertexts of the imperial ambassador at Venice. Satoshi Tomokiyo had reconstructed the cipher outright and published it in September 2025, a year before the entry was scored, so there is no break to be had. The entry is corrected instead: the run spans four volumes and not one, every record is dated 1522 so the treaty of July 1523 is not in it, nine of the letters are Lope Hurtado de Mendoza&rsquo;s, and almost all carry a contemporary decipherment. The nomenclator turns out to be alphabetically ordered, which fills in the numeral run; three values so predicted are then confirmed in two letters outside Tomokiyo&rsquo;s coverage, both read in part here: R9653 on the siege of Rhodes, and R9635, a whole page of cipher on the sums owed by the Signoria and the restitution of goods seized from imperial vassals. Lope Hurtado&rsquo;s code groups take finals S&aacute;nchez&rsquo;s key does not have &mdash; a third cipher, still unreconstructed.',
         quote='&ldquo;ducados allende de los otros xviii mil &hellip; mas de xv mil ducados&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='lopehurtado1523', label='Lope Hurtado 1523&ndash;24', year='1523&ndash;24', y=1523.6, place='Rome &rarr; Charles V and Gattinara', st='solved', stt='read',
         title='Lope Hurtado de Mendoza at Rome, 1523&ndash;24 &mdash; the key rebuilt, six letters read in part',
         blurb='Eight DECODE records (RAH Salazar 9/28 and 9/30, R9667&ndash;R9869) catalogued as unread June 1523 ciphertexts to an unknown recipient are letters of May 1523 to March 1524 to Charles V and the Grand Chancellor Gattinara. Two were calendared by Bergenroth from contemporary decipherings (CSP Spain 2, nos. 548 and 617); the &ldquo;Claro&rdquo; leaf bound with R9667 is the Abbot of N&aacute;jera&rsquo;s, not Hurtado&rsquo;s. The key, changed since 1522, is rebuilt from the clerk&rsquo;s clear bound with the letter of 5 February 1524, and the six uncalendared letters are read in part: Beaurain&rsquo;s mission, a Pope who wants France ruined or a truce, the Datary Giberti, an agent unpaid.',
         quote='&ldquo;lo que mas dessea es que el Rey de Francia se destruya&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='sanchez1523', label='S&aacute;nchez 1523', year='1523', y=1523.5, place='Venice &rarr; Charles V', st='found', stt='already calendared; read in part',
         title='Alonso S&aacute;nchez at Venice, 1523 &mdash; already calendared, key unchanged',
         blurb='Ten DECODE records (RAH Salazar 9/28, R9670&ndash;R9770) were catalogued as unread 1523 ciphertexts to an unknown recipient. They are the ambassador&rsquo;s despatches to Charles V, in the cipher he used in 1522. Bergenroth calendared the May and June letters in 1866 from the contemporary decipherings (CSP Spain 2, nos. 549, 552, 554, 558), and seven of the records are those letters or their duplicates. The three letters of 16 August 1523 are not in the Calendar and are mostly in the clear. S&aacute;nchez&rsquo;s own letter of that day is read in part here with the unchanged 1522 key.',
         quote='&ldquo;vuestra magestad vera por la capitulacion que no se ha expressado&hellip;&rdquo;',
         rights='Real Academia de la Historia, via DECODE'),
    dict(slug='sessa1523', label='Sessa 1523', year='1523', y=1523.2, place='Sessa, Rome &rarr; Charles V', st='found', stt='mostly in print',
         title='The Duke of Sessa to Charles V, February&ndash;April 1523 &mdash; seven &ldquo;unknown&rdquo; letters, four already calendared',
         blurb='DECODE R9660&ndash;R9666 were catalogued as seven Non-decrypted letters of &ldquo;Luis Fern&aacute;ndez?&rdquo; from Sesa to an unknown recipient. They are the Duke of Sessa&rsquo;s despatches to Charles V, 20 February to 27 April 1523, in RAH Salazar A-27. Bergenroth calendared four of them in 1866 from the court&rsquo;s decipherments on other leaves of the volume. The cipher is the 1524 Sessa nomenclator, and a paragraph of the uncalendared February letter was read with that key as a check.',
         quote='&ldquo;&hellip; a ver a Su Santidad, mas con color de &hellip;&rdquo;',
         rights='Real Academia de la Historia, via DECODE'),
    dict(slug='soria1523', label='Soria 1523', year='1523', y=1523.5, place='Genoa &rarr; Charles V', st='solved', stt='read',
         title='Lope de Soria to Charles V, Genoa, 1523 &mdash; two ciphers, one broken from a court decipherment and one with no key at all',
         blurb='Eleven DECODE records (RAH Salazar A-28, R9488&ndash;R9498), none deciphered before: five despatches of the imperial ambassador at Genoa, June to August 1523, with their duplicates. The later cipher was rebuilt from a Soria letter that carries the court&rsquo;s decipherment. The earlier one had no key or crib and fell to a substitution solver scored on Castilian of the 1520s. The letters read on the Venetian league, the French descent, a plan to seize Bergamo and Brescia, Siena, Beaurain&rsquo;s mission and Andrea Doria&rsquo;s first approach to the Emperor.',
         quote='&ldquo;los dichos [rip] usaran con [pur] los tratos que uso Otaviano Campofregoso quando se fizo la liga general&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='sessa1524', label='Sessa 1524', year='1524', y=1524.3, place='Rome &rarr; Charles V', st='solved', stt='read',
         title='The Duke of Sessa to Charles V, Rome, 18 April 1524 &mdash; a &ldquo;1424&rdquo; cipher that is a century younger',
         blurb='DECODE catalogues RAH Salazar A-31 ff. 128&ndash;131 as a <em>Non-decrypted</em> letter of Luis Fern&aacute;ndez from Rome, April 1424, and it was taken up as the longest ciphertext before 1450. The date is a typo: the letter is the Duke of Sessa&rsquo;s despatch of 18 April 1524 and its duplicate, skipped by Bergenroth. Eight sibling letters in the same cipher carry the court&rsquo;s decipherment; about 110 code groups and the alphabet were rebuilt from them by token tiling and template matching. The cipher now reads at the word level: the Pope&rsquo;s secretary withholds the Bishop of Veroli&rsquo;s letters, and Sessa asks the Pope for money for the Swiss. Four groups are attested nowhere and stay open.',
         quote='&ldquo;habl&eacute; en la ora a Su Santidad a pedirle que haya provisi&oacute;n &hellip; pues tiene color para ello&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='bizozola1520', label='Bizozola 1529', year='1529', y=1529.85, place='Bologna &rarr; Maximilian Sforza in France', st='solved', stt='read',
         title='Ambrogio Bizozola to Maximilian Sforza, Bologna, 4 November 1529 &mdash; read with Lasry&rsquo;s key',
         blurb='Catalogue item 176, BnF fr. 3034 ff. 156&ndash;157 (DECODE R4224): four pages of invented signs to the exiled Duke of Milan. George Lasry rebuilt the key in 2023 but no text was published. Read here from the Gallica scans, all four pages: written at Bologna on the eve of Charles V&rsquo;s entry (5 November 1529), it reports that the Emperor&rsquo;s council was discussing a partition of the Milanese state among Savoy, Monferrato, Mantua and Ferrara. The Archbishop of Bari is reported to say that Milan should rather go to Maximilian himself. 97% of the signs read; the date numerals stay open.',
         quote='&ldquo;al marchese di Monferrato, al marchese di Mantua, al duca di Ferrara, et Milano al duca&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France / Gallica'),
    dict(slug='jantini1517', label='Fantini 1517&ndash;18', year='1517&ndash;1518', y=1517.5, place='Buda, Eger &rarr; Ferrara', st='stuck', stt='key not found',
         title='Benedetto Fantini, Buda and Eger, 1517&ndash;1518 &mdash; a two-tier syllabic cipher, not read',
         blurb='Two letters of a Ferrarese in Ippolito d&rsquo;Este&rsquo;s household in Hungary (ASMo Ungheria b. 4, Fantini nos. 5&ndash;6; DECODE R1126&ndash;R1127, filed as &ldquo;Jantini&rdquo;). The cipher is of the family of Caprile&rsquo;s 1519 letters, shown here to be syllabic from a pairing with their 1882 decipherment. The 1,370 columns were transcribed; a syllabary annealer that recovers a control of the same size produces no Italian, and Caprile&rsquo;s values do not fit.',
         quote='&ldquo;&hellip; per la mandata dil duca Lorezo in Franza&rdquo;, then two pages of signs',
         rights='Archivio di Stato di Modena, via DECODE R1126'),
    dict(slug='caprile1519', label='Caprile 1519&ndash;21', year='1519&ndash;21', y=1520.3, place='Eger, Buda &rarr; Ferrara', st='solved', stt='read',
         title='Giuliano Caprile and Alfonso Cistarelli to Ferrara, 1519&ndash;1521 &mdash; most read at the time or since, two more read in part',
         blurb='Catalogue items 157 and 158: eight DECODE records of two agents of Cardinal Ippolito d&rsquo;Este at Eger (ASMo Ambasciatori Ungheria b. 4). The 1519 letters were deciphered in 1882 and the postscript of 16 February 1521 by Judit W. Somogyi in 2025. Her texts were used as a crib to rebuild the homophonic sign cipher of 1520&ndash;21, which reads two letters with no decipherment anywhere, R1136 and R1139, in part. R1128 (a different 1519 cipher) and Cistarelli&rsquo;s figure cipher R1137 stay open.',
         quote='&ldquo;lui m&rsquo;ha resposto dice de voler andar in Italia&rdquo;',
         rights='Manuscript images: Archivio di Stato di Modena, via DECODE and Vestigia'),
    dict(slug='adrian1521', label='Adrian 1521', year='1521', y=1521, place='Vitoria &rarr; Charles V', st='found', stt='printed reading corrected',
         title='Adrian of Utrecht, the Admiral and the Constable to Charles V, 30 December 1521 &mdash; a printed decipherment checked and corrected',
         blurb='AGS Estado leg. 8 no. 150, catalogued as &ldquo;cifrada pr&aacute;cticamente en su totalidad&rdquo;, was deciphered by Claudio P&eacute;rez Gredilla and printed by Danvila in 1899. The ciphertext was transcribed from PARES and aligned with his text on the group <em>xif</em> = V. M. That rebuilds a nomenclator of three-letter code groups and homophonic signs, shows that the dead king he called &ldquo;de Inglaterra&rdquo; is Manuel I of Portugal, and reads or corrects about seventeen of the groups he left unread. About ten are still open.',
         quote='&ldquo;los Reyes de Portugal tienen [alianza] antigua con los de Francia, y creemos que los franceses no estar&aacute;n perezosos&rdquo;',
         rights='Manuscript images: Archivo General de Simancas (PARES)'),
    dict(slug='breves1603', label='Br&egrave;ves 1603', year='1603', y=1603.1, place='the Court &rarr; Constantinople', st='found', stt='key and text found',
         title='Henri IV to Savary de Br&egrave;ves, 1603 &mdash; the key in fr. 3462 and the letters in print since 1853',
         blurb='Twelve royal letters of 1603 to the ambassador at the Porte, BnF fr. 3541, &ldquo;avec chiffre&rdquo; and listed as undeciphered, with a partial reading by Tomokiyo from a rebuilt key. The office&rsquo;s own table survives as fr. 3462 f. 103, and Berger de Xivrey printed the letters in 1853 from a contemporary copy in clear: three in full, nine as summaries. Tomokiyo&rsquo;s overlay of f. 60 is checked against the print (<em>revolteur d&rsquo;Asie</em>, <em>protestans</em>). The cipher leaves are not digitised, so the letters have not been read against the key.',
         quote='&ldquo;mais ils doivent plustost craindre les armes du revolteur d&rsquo;Asie que celles des autres&rdquo; &middot; 18 February 1603',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='conti1649', label='Conti 1649', year='1649', y=1649, place='Paris &rarr; the Archduke', st='solved', stt='read',
         title='The prince de Conti&rsquo;s ciphered m&eacute;moires, March 1649 &mdash; the Fronde&rsquo;s instructions to its envoys with the Archduke',
         blurb='BnF fr. 3854 nos. 41&ndash;43. The two &ldquo;undeciphered&rdquo; m&eacute;moires of 26&ndash;27 March were read by Lasry in 2023; they are read again here from the leaves, with three small corrections. The third, whose decipherment was meant to be the crib, is a different number code, and its clerk never glossed the first twelve lines. A key rebuilt from about 3,300 glossed groups reads them: Conti to Laigue, 5 March 1649, explaining the Rueil conference away to Archduke Leopold Wilhelm.',
         quote='&ldquo;d&egrave;s le moment qu&rsquo;il entrera en France, cette conf&eacute;rence se rompra&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='vich1511', label='Vich 1511&ndash;12', year='1511&ndash;12', y=1511.5, place='Spain &rarr; Rome', st='solved', stt='3 of 4 read',
         title='Ferdinand the Catholic to Jer&oacute;nimo de Vich, 1511&ndash;12 &mdash; Ravenna, Milan and a spiritual war on Louis XII',
         blurb='Three letters of Ferdinand the Catholic to his ambassador at Rome, AHN Estado 8715 N.45, N.57 and N.60 (April 1511 to September 1512), written wholly in cipher and filed without the decipherment their siblings carry. The nomenclator, a homophonic alphabet with 153 code groups for words and syllables, was rebuilt by lining two deciphered siblings up with the clerk&rsquo;s text, and then read the three letters it was not built from. Julius II&rsquo;s cardinals and Venice, Ferdinand&rsquo;s account of how his army was pushed into Ravenna, the Sforza restoration in Milan. The 1515 letter is another system. Terrateig&rsquo;s 1963 edition, not seen, may already print them.',
         quote='&ldquo;las cosas de guerra es muy peligroso [&hellip;] los que estan absentes della; que siempre se ha de remitir a los que las tienen presentes&rdquo;',
         rights='Manuscript images: Archivo Hist&oacute;rico Nacional (PARES)'),
    dict(slug='ayala1516', label='Ayala 1516', year='1516', y=1516.66, place='Brussels &rarr; Cardinal Cisneros', st='found', stt='printed 1875; re-read',
         title='Diego L&oacute;pez de Ayala to Cardinal Cisneros, 30 August 1516 &mdash; a &ldquo;Non-decrypted&rdquo; letter read with a sibling key',
         blurb='DECODE R9954 is five pages of invented signs from Cisneros&rsquo;s agent at the court of King Charles, catalogued as Non-decrypted. Tomokiyo&rsquo;s key for Ayala&rsquo;s letter of 12 July (R10024) reads it unchanged. Read here before the 1875 edition was found, and checked against it: the sale of vacant Castilian offices around Chi&egrave;vres, Queen Germaine&rsquo;s dealings with France, the peace of Noyon to be proclaimed, and the King&rsquo;s departure for Spain fixed on 30 August.',
         quote='&ldquo;cerca de los oficios que estan vacos en estos reynos&rdquo;',
         rights='Archivo General de Simancas, via DECODE R9954'),
    dict(slug='spinelly1516', label='Spinelly 1517', year='1517', y=1517.1, place='Brussels &rarr; Henry VIII', st='solved', stt='read',
         title='Thomas Spinelly to Henry VIII, Brussels, 1 February 1517',
         blurb='BL Cotton MS Galba B V ff. 40&ndash;41 (DECODE R8416), catalogued as a letter of Spinelly to an unknown recipient, London 1516, not decrypted. It is Spinelly&rsquo;s clear despatch to the King from the court of Charles at Brussels, with five lines in a substitution of invented signs and no decipherment. A crib from the clear text (&ldquo;audensier&rdquo;) gives the alphabet: the Audiencier and Luigi Marliano expect the King&rsquo;s entry into Brussels, and the Emperor at Cambrai about the 15th. <i>Letters and Papers</i> had only summarised the Cambrai clause.',
         quote='&ldquo;and [the Emperor] about the xv day of the present monethe so to Cambray&rdquo;',
         rights='Manuscript images: British Library (via DECODE)'),
    dict(slug='guiche1551', label='La Guiche 1551', year='1551', y=1551, place='Rome &rarr; the French court', st='solved', stt='read',
         title='La Guiche from Rome, 1551, with Noailles and Seure, 1558 &mdash; a symbol cipher nobody deciphered',
         blurb='BnF fran&ccedil;ais 3138 no. 22: Claude de La Guiche&rsquo;s letter to Montmorency of 22 November 1551 carries 406 signs of cipher with no decipherment anywhere. The 22 invented signs are a simple substitution, broken here by permutation annealing with a French despatch model. Dom Diego and the Sienese envoy, and the Count of Santa Fiora ready to come over to the king. Noailles&rsquo;s Venice letter of 1558 was deciphered in the margin at the time; Seure&rsquo;s Lisbon letters are left open.',
         quote='&ldquo;le conte Sainte Fiore est mal satisfaict&hellip; et que facilement se reduiroit au service du roy&rdquo;',
         rights='Biblioth&egrave;que nationale de France / Gallica'),
    dict(slug='rennes1563', label='Rennes 1562&ndash;64', year='1562&ndash;64', y=1563, place='the French court &rarr; the imperial court', st='solved', stt='read',
         title='Catherine de M&eacute;dicis and the bishop of Rennes: four unread cipher letters, 1562&ndash;64',
         blurb='Four letters to the French ambassador at the imperial court in the Bishop of Rennes&rsquo; cipher, none deciphered before: Catherine&rsquo;s of 31 July 1563 (BnF fr. 3181 f. 55), whose cipher La Ferri&egrave;re printed as an empty bracket; a 1564 order to leave the precedence quarrel; Bourdin&rsquo;s of December 1562 on the leaked marriage overture; and a note to be deciphered by Rennes himself and burned. Each secretary&rsquo;s hand was calibrated on glossed letters in the same hand and every line decoded by a language-model lattice: from 65% to 99% of each letter read.',
         quote='&ldquo;pour le bien de la Chrestient&eacute; et avancer le concile&hellip; laisser l&agrave; quelque secretaire&hellip; soubz couleur d&rsquo;aucuns voz affaires particuliers&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='charlesixducroc', label='Charles IX to du Croc', year='1565&ndash;67 or 1572', y=1567.5, place='the French court &rarr; Scotland', st='found', stt='already solved',
         title='Charles IX to Philibert du Croc &mdash; an undated Scottish cipher already read by George Lasry',
         blurb='A two-page letter wholly in graphic cipher, addressed to Charles IX&rsquo;s ambassador in Scotland and catalogued by DECODE as non-decrypted. George Lasry had already solved it and Satoshi Tomokiyo published his full-page plaintext overlays in 2022. Charles directs du Croc to shape the peace, government and council around the young James VI, prevent a marriage before France is consulted, preserve Scottish attachment to France, and stop English encroachment. The catalogue&rsquo;s &ldquo;1 Jan 1550&rdquo; is a metadata error: Destray labels the original without place or date; it belongs to 1565&ndash;67 or 1572.',
         quote='&ldquo;donner ordre que les Anglois n&rsquo;empi&egrave;tent aucune chose en Escosse&rdquo; &middot; Charles IX to du Croc',
         rights='Archives d&eacute;partementales de la Ni&egrave;vre, reproduced by Destray (1924), via Gallica and DECODE R2789'),
    dict(slug='toledo1565', label='Toledo 1565', year='1565', y=1565, place='Messina &rarr; Philip II', st='solved', stt='solved',
         title='Garc&iacute;a de Toledo to Philip II, 16 July 1565 &mdash; a relief of Malta waved off by the Grand Master&rsquo;s fires',
         blurb='The duplicate of the viceroy of Sicily&rsquo;s ciphered despatch from Messina, two months into the Great Siege, AGS Estado leg. 1394 no. 247: clear Spanish with every sensitive word in two-digit figures, and no decipherment on the leaf or in PARES. Two runs beside clear words, <em>seiscientos soldados</em> and <em>en tiera</em>, gave eleven letters; the figures 12&ndash;43 run through the alphabet in order, so the rest was predicted and confirmed, and all 1,930 groups read. The Piccolo Soccorso got into the Borgo; a second run of galleys turned back four miles out on La Valette&rsquo;s signals, as <em>Mosiur de Lenni</em> reported; and Sicily cannot pay for the war.',
         quote='&ldquo;el maestre les hizo las sennales del fuego clarissimas para que no entrassen&rdquo;',
         rights='Manuscript images: Archivo General de Simancas (PARES)'),
    dict(slug='nuncio1566', label='Alessandrino 1567', year='1567', y=1567.5, place='Rome &rarr; Madrid', st='solved', stt='read',
         title='Cardinal Alessandrino to the nuncio in Spain, 1567 &mdash; six &ldquo;unknown sender&rdquo; ciphers read with Lasry&rsquo;s key',
         blurb='Six DECODE records catalogued with no sender, no recipient and the date 1566. The archive&rsquo;s description of the volume puts them among Cardinal Alessandrino&rsquo;s letters to the nuncio of 1567, and the key George Lasry reconstructed for the 1568 letters reads all six unchanged. Philip II&rsquo;s journey to Flanders, Borromeo against the Milan senate, the unconfirmed archbishop of Cologne, and advice to imprison the Constable Montmorency during the second French civil war.',
         quote='&ldquo;facesse mettere in una prigione sicura il conestabile Memoransi e suo figliolo&rdquo;',
         rights='Archivio Apostolico Vaticano, via DECODE R85&ndash;R90'),
    dict(slug='alessandrino1568', label='Alessandrino 1568', year='1568&ndash;69', y=1568.5, place='Rome &rarr; Madrid', st='solved', stt='read',
         title='Cardinal Alessandrino to the nuncio in Spain, 1568&ndash;69 &mdash; eleven papal ciphers read with Lasry&rsquo;s polyphonic key',
         blurb='Eleven ciphers from Pius V&rsquo;s nephew and secretary to the nuncio at Madrid, catalogued on DECODE as partially decrypted, with George Lasry&rsquo;s reconstructed key attached but no plaintext. Every digit stands for two letters and zero is a null, so a beam search chose each letter under an Italian model. All eleven read end to end: a French bride for Philip II, the King&rsquo;s ministers and Church jurisdiction, Bolognese exiles, and the Turk courted by the German Protestants.',
         quote='&ldquo;&egrave; ricercato qui da alcuni amorevoli della corona di Francia&rdquo;',
         rights='Archivio Apostolico Vaticano, via DECODE R93&ndash;R102, R115'),
    dict(slug='dandini1580', label='Como to Dandini 1580', year='1580', y=1580.4, place='Rome &rarr; Paris', st='solved', stt='read',
         title='The Cardinal of Como to the nuncio Dandini, 1580 &mdash; Henri III and the nun',
         blurb='Two cipher enclosures from the papal Secretariat to the nuncio in France, catalogued on DECODE as partially decrypted. George Lasry had decrypted the longer one (R73) in 2020. The other (R72) keeps his frame and nomenclator but reassigns the letter codes; the letters were rebuilt here by annealing, and the text matches the clerk&rsquo;s decipherment written below the figures. Both letters tell the nuncio to stop Henri III visiting a nun, discreetly.',
         quote='&ldquo;La voce et l&rsquo;opinione della pratica del Re Chr.mo con la monaca&rdquo;',
         rights='Archivio Apostolico Vaticano, via DECODE R72&ndash;R73'),
    dict(slug='sauli1579', label='Sauli and Riario 1579', year='1579&ndash;81', y=1580, place='Portugal &rarr; Rome', st='solved', stt='read',
         title='Sauli and Riario, from Portugal to the Secretariat, 1579&ndash;81 &mdash; contemporary decipherments checked with Lasry&rsquo;s key',
         blurb='Five ciphertexts from the papal nunciature and Cardinal Riario&rsquo;s legation to Philip II, catalogued on DECODE as partially decrypted, with George Lasry&rsquo;s key and a decryption of the first two. Nearly every passage carries the secretariat&rsquo;s decipherment above it. The other three were transcribed digit by digit and decrypted with the key, and they agree with the glosses. The comparison adds 16 Inghilterra, 30 S.S.t&agrave;, 36 Francia and 40 cattolici to the key. The ciphers cover the Piedmont plot, the papal Italian troops for Ireland, and the English enterprise put off until Flanders is subdued.',
         quote='&ldquo;sopra il negotio di Piamonte&rdquo;',
         rights='Archivio Apostolico Vaticano, via DECODE R190&ndash;R194'),
    dict(slug='yard1699', label='Yard 1699', year='1699', y=1699, place='Whitehall &rarr; Paris', st='solved', stt='read',
         title='Robert Yard to the Earl of Manchester &mdash; two &ldquo;undeciphered&rdquo; letters of October 1699, read with the key from the same papers',
         blurb='Two letters from the Secretary of State&rsquo;s office to the ambassador at Paris, 12 and 16 October 1699, catalogued at Yale as &ldquo;almost entirely in cipher, undeciphered&rdquo;; the Historical Manuscripts Commission said no key was known. The key was in the same Manchester papers: a printed code sheet with handwritten numbers, <em>the</em> = 454, as Tomokiyo had inferred. Checked on a sibling letter deciphered at the time, it reads both letters group for group, apart from five slips of Yard&rsquo;s pen. Messengers at Dover wait for Mills and Lord Drummond&rsquo;s priest, and Ireland and the north report a design <em>carryed on very privately at Saint Germains</em>.',
         quote='&ldquo;all is said to be carryed on very privately at Saint Germains&rdquo; &middot; Robert Yard, 12 October 1699',
         rights='Manuscript images: Beinecke Rare Book and Manuscript Library, Yale University'),
    dict(slug='r8356', label='Walsingham letter-book 1571', year='1571', y=1571.48, place='Paris &rarr; London', st='stuck', stt='key not found',
         title='Walsingham&rsquo;s letter-book, June 1571 &mdash; a cipher run and two codes in a clear letter, not read',
         blurb='BL Harley MS 260 ff. 112v&ndash;113r (DECODE R8356), catalogued as a ciphered letter of Elizabeth R., is Walsingham&rsquo;s Paris letter-book: Walsingham to Burghley, 25 June 1571, and the Queen&rsquo;s letter to Walsingham in clear. Digges printed the letter in 1655 with the cipher as figures. A nine-sign run and two boxed codes name an informant on a plot to carry off the Queen of Scots; no key survives.',
         quote='The [12] 6174aH6HH shewed me his Masters letters',
         rights='British Library, via DECODE R8356'),
    dict(slug='r8361', label='Walsingham letter-book 1572', year='1572', y=1572.85, place='London &harr; Paris', st='stuck', stt='key not found',
         title='Walsingham&rsquo;s letter-book, November 1572 &mdash; name codes in clear letters, one read',
         blurb='BL Harley MS 260 ff. 367&ndash;369 (DECODE R8361), catalogued as unknown sender to unknown recipient, is Walsingham&rsquo;s Paris letter-book: Leicester and Burghley to Walsingham, and Walsingham to Smith and Burghley, November 1572. The letters are clear and printed in Digges 1655, with the cipher left as figures. Context fixes [3] as the Queen; [7], [9], H and a nine-sign letter run need the lost key.',
         quote='He wisheth [3] to look well to Scotland',
         rights='British Library, via DECODE R8361'),
    dict(slug='palm1727', label='Palm 1727', year='1727', y=1727.2, place='London &rarr; Starhemberg', st='stuck', stt='key not found',
         title='Palm to Starhemberg and Visconti, 1727 &mdash; German letter with ciphered passages, not read',
         blurb='DECODE R7927 is a German letter of the Emperor&rsquo;s London resident, mostly clear, with fourteen passages in a homophonic cipher with a small nomenclator; the Deciphering Branch glossed only a handful of groups. R7930 holds only a cover and a worksheet for a different code. The adjacent Windischgr&auml;tz key does not fit, and 162 letter tokens are too few to break the cipher without Palm&rsquo;s key.',
         quote='&hellip; dass im Fall es zu einer Ruptur kommen solte, man 9. 24. 77. 59. 423 &hellip;',
         rights='British Library, via DECODE'),
    dict(slug='jones1753', label='Schaeblin to Mr Jones 1753', year='1753', y=1753.05, place='The Hague', st='found', stt='not a cipher',
         title='Schaeblin to Mr Jones, The Hague, 1753 &mdash; a letter about a cipher, not in one',
         blurb='BL Add MS 32256 f. 235 (DECODE R9218), catalogued as a ciphered numerical nomenclator letter of Mr Jones to Ben. Schaeblin. It is a clear English letter the other way round: Schaeblin, at The Hague on 16 January 1753, proposes a new French cipher of 3000 numbers on the model of the English one, and ways to disguise it by reversing or rotating the figures of each group or adding a dummy figure.',
         quote='&ldquo;by taking ye Figures of every Cypher backwards, E.G. 1753. write 3571&rdquo;',
         rights='British Library, via DECODE R9218'),
    dict(slug='visconti1727', label='Visconti Italian cipher', year='1727', y=1727, place='Add MS 32270', st='found', stt='a key, not a letter',
         title='The Visconti Italian cipher, 1727 &mdash; catalogued as a letter, it is the key',
         blurb='BL Add MS 32270 f. 42 (DECODE R7931), catalogued as a partly decrypted ciphered letter of Count Visconti. It is the Deciphering Branch&rsquo;s fair copy of the key it rebuilt for Count Visconti at Brussels and the Marquis Visconti in London: 300 places, 193 filled, letters with homophones, syllables and names from Walpole and Townshend to Ostenda and Congresso. The next leaf is the working draft; nothing on f. 42 is enciphered.',
         quote='&ldquo;Count Visconti at Bruxelles with Marq.s Visconti here, 1727, Italian Cypher&rdquo; &middot; the endorsement',
         rights='Manuscript images: British Library, via DECODE'),
    dict(slug='sp106r597', label='Stosch&ndash;Walton cipher instructions', year='c. 1731', y=1731, place='SP 106/7', st='found', stt='instructions, read',
         title='The Stosch&ndash;Walton cipher instructions &mdash; not a letter but how to use the code',
         blurb='TNA SP 106/7 f. 33 (DECODE R597), catalogued as a partly decrypted French nomenclator letter with lines unsolved. It is an English instruction sheet for the cipher used with Baron Stosch, the British spy on the Stuart court who wrote as John Walton: three-digit syllable groups in two keys, 371 to change key, no separators, nulls 110, 220 and all above 900. The worked example carries its syllables and reads in full; the &ldquo;unsolved&rdquo; lines are the same example run together.',
         quote='&ldquo;Les Adherens du Pretendant se donnent beaucoup de mouvement &agrave; Rome&rdquo;',
         rights='The National Archives, Kew, via DECODE R597'),
    dict(slug='loeschnen1816', label='Loeschner&rsquo;s cipher memorandum', year='1816', y=1816.5, place='Vienna', st='found', stt='not a cipher',
         title='Loeschner, Vienna 1816 &mdash; a memorandum on the Staatskanzlei cipher instruction, not a cipher',
         blurb='DECODE R2227 was catalogued as a ciphered letter of &ldquo;W. Loeschnen?&rdquo; of 1 July 1816. It is W. Loeschner&rsquo;s clear German memorandum proposing additions and changes to the instruction for using the Staatskanzlei&rsquo;s cipher keys. Its only figures are worked examples with the plaintext written above them. Nothing is hidden.',
         quote='le Roi d&rsquo;Espagne vient de nommer (Parenthesis) M. le Duc de San Carlos (Claudatur)',
         rights='&Ouml;sterreichisches Staatsarchiv, HHStA, via DECODE R2227'),
    dict(slug='sloane3188', label='Shippen&rsquo;s notes on Dee', year='17th c.', y=1595, place='Sloane MS 3188', st='found', stt='not a cipher',
         title='Sloane MS 3188 ff. 109&ndash;169 &mdash; shorthand notes on John Dee&rsquo;s spirit actions, not a cipher',
         blurb='DECODE lists 25 leaves of Sloane MS 3188 (R8506&ndash;R8530) as non-decrypted ciphertexts of unknown sender and recipient. They are the notes that follow Dee&rsquo;s own spirit diaries in the volume, attributed to William Shippen: an index of the Actions, a list of Dee&rsquo;s writings, a note on Kelley and Prague dated 1595. The script is 17th-century English stroke shorthand with names and titles in longhand. No cipher and no despatches.',
         quote='&ldquo;Actio 4 &hellip; Uriel als Nariel&rdquo;',
         rights='British Library, via DECODE R8506'),
    dict(slug='prussia1702', label='A lesson in cipher (Blenheim)', year='1702&ndash;23', y=1702, place='Add MS 61575', st='found', stt='not a cipher',
         title='&ldquo;Frederic, Re di Prussia&rdquo; to an unknown recipient &mdash; a thank-you for lessons in cipher, not a cipher',
         blurb='Blenheim Papers Add MS 61575 f. 95 is catalogued on DECODE (R8774) as a non-decrypted numerical cipher. The page has no numbers: it is seven lines of plain French, spelled by ear and split into syllables, thanking someone for teaching the writer to write in cipher and wishing them a good journey. Writer and recipient are unidentified.',
         quote='&ldquo;en me mon trant d&rsquo;es cria re en sif fer&rdquo;',
         rights='British Library, via DECODE; image not reproduced'),
    dict(slug='bay1706', label='Bay to R&aacute;k&oacute;czi 1706', year='1706', y=1706.2, place='J&aacute;szv&aacute;s&aacute;r &rarr; R&aacute;k&oacute;czi', st='solved', stt='read',
         title='Andr&aacute;s Bay to Ferenc R&aacute;k&oacute;czi II, J&aacute;szv&aacute;s&aacute;r, 8 March 1706',
         blurb='A ciphered despatch from R&aacute;k&oacute;czi&rsquo;s man at the Moldavian court (DECODE R478) was catalogued as undeciphered, with no key. Scoring all 94 R&aacute;k&oacute;czi chancery keys on DECODE against it picked out R609, a Hungarian syllabic nomenclator, which reads it unchanged. The Tsar suing Charles XII for peace, the Muscovite and Polish envoys at Ia&#351;i, a message from Pekri to the voivode, and the Swede at Vilna.',
         quote='&ldquo;tudv&aacute;n az bar&aacute;t az Port&aacute;nak szem&eacute;nek &eacute;s f&uuml;l&eacute;nek lenni&rdquo;',
         rights='MNL OL, via DECODE; lead crop only'),
    dict(slug='papai1706', label='P&aacute;pai to R&aacute;k&oacute;czi 1706&ndash;10', year='1706&ndash;10', y=1706.5, place='Constantinople &rarr; R&aacute;k&oacute;czi', st='solved', stt='read',
         title='J&aacute;nos P&aacute;pai to Ferenc R&aacute;k&oacute;czi II, 1706&ndash;1710 &mdash; the envoy&rsquo;s own key',
         blurb='Twelve ciphered despatches of R&aacute;k&oacute;czi&rsquo;s envoy at the Porte (DECODE R731&ndash;R823, filed under three catalogue entries, one as from an &lsquo;unknown sender&rsquo;) were catalogued as undeciphered. The key issued to P&aacute;pai survives as DECODE R580, a Hungarian syllabic nomenclator, and nothing linked the two. Applied unchanged, it gives values for 16,346 of 16,861 groups in eleven letters, the rest mostly nulls: Imperial troops crossing Ottoman ground, audiences before the internuncio, the French ambassador failing to bring the Porte to war, the French and Muscovite ambassadors, money. The twelfth letter (Belgrade, 1710) uses a graphic-sign alphabet and stays unread.',
         quote='&ldquo;legyen patientia &hellip; ne kellyen illy haszontalan k&ouml;lteni&rdquo; &middot; the Kiaya&rsquo;s answer, 2 January 1710',
         rights='Manuscript: Magyar Nemzeti Lev&eacute;lt&aacute;r; images not reproduced'),
    dict(slug='rakoczi1707', label='Groffey to R&aacute;k&oacute;czi 1707', year='1707', y=1707, place='Polish&ndash;Swedish theatre &rarr; R&aacute;k&oacute;czi', st='partial', stt='cipher identified; read in substance',
         title='Philippe Groffey (?) to Ferenc R&aacute;k&oacute;czi II, 15 October 1707 &mdash; the catalogue had the direction backwards',
         blurb='DECODE R902 was catalogued as a non-decrypted letter from R&aacute;k&oacute;czi under his alias Pompeio Cesoni. The clear address says the opposite: it is addressed <em>&agrave; Monsieur Pompeio Cesoni</em>. A matching preserved key, DECODE R639, identifies 1,020 of 1,108 transcribed groups and exposes a French intelligence and lobbying report from the Polish&ndash;Swedish theatre: R&aacute;day&rsquo;s letters to Rehnski&ouml;ld, work at the Swedish and Polish courts, and Polish liberty oppressed in favour of King Stanis&#322;aw. The key heading and diplomatic context make Philippe Groffey the probable unsigned writer. A fresh manuscript transcription is still needed for an exact continuous edition.',
         quote='&ldquo;les lettres de Monsieur R&aacute;day au g&eacute;n&eacute;ral Rehnski&ouml;ld&rdquo;',
         rights='Manuscript: Magyar Nemzeti Lev&eacute;lt&aacute;r; images not reproduced because archive permission is required'),
    dict(slug='rakoczi1704', label='Letters to R&aacute;k&oacute;czi 1706&ndash;11', year='1706&ndash;11', y=1707.2, place='Danzig, Poland &rarr; R&aacute;k&oacute;czi; Lw&oacute;w', st='solved', stt='read',
         title='Four letters &ldquo;of Ferenc R&aacute;k&oacute;czi II&rdquo;: three were written to him',
         blurb='Catalogue item 44 grouped four DECODE records as ciphered despatches of R&aacute;k&oacute;czi. Three are French reports sent to him from Danzig and the Polish court. Re-transcribed from the images, and with the key sheet DECODE R639 itself corrected, two read at 97% of groups; the third carries its own clear copy. The fourth is R&aacute;k&oacute;czi&rsquo;s signed Latin letter from Lw&oacute;w, 27 June 1711, rejecting the Peace of Szatmár; its syllabic key is rebuilt from the clerk&rsquo;s interlinear decipherment.',
         quote='&ldquo;nos Regem extra dietam promulgatum &hellip; agnoscere non posse&rdquo;',
         rights='Manuscript: Magyar Nemzeti Lev&eacute;lt&aacute;r; images not reproduced because archive permission is required'),
    dict(slug='henter1707', label='Hent&eacute;r to R&aacute;k&oacute;czi 1707', year='1707', y=1707.5, place='Constantinople &rarr; R&aacute;k&oacute;czi', st='found', stt='decipherment found',
         title='Mih&aacute;ly Hent&eacute;r to Ferenc R&aacute;k&oacute;czi II, Constantinople, 8 July 1707 &mdash; the &ldquo;non-decrypted&rdquo; letter carries its decipherment between the lines',
         blurb='DECODE R496 lists a one-page cipher letter of &ldquo;1 January 1707&rdquo; as non-decrypted with no inline plaintext. The folio carries a contemporary Hungarian decipherment written between the cipher lines, and it is dated Constantinople, 8 July 1707. Two sibling Hent&eacute;r letters (R533, R534) confirm the monoalphabetic key (<em>wi6xi2i4</em> = <em>Fels&eacute;ged</em>). The pasha of Belgrade offers troops, powder and grain if R&aacute;k&oacute;czi sends six or seven thousand men against the Serbs, while Hent&eacute;r chases an audience with the grand vizier.',
         quote='&ldquo;ha Fels&eacute;ged hat vagy h&eacute;t ezer hadat a r&aacute;cok ellen k&uuml;ldene&rdquo;',
         rights='Manuscript: Magyar Nemzeti Lev&eacute;lt&aacute;r; images not reproduced because archive permission is required'),
    dict(slug='nunzio1718', label='Nunziatura di Spagna 1718', year='1718&ndash;20', y=1718.1, place='Rome &rarr; Madrid', st='found', stt='already solved; key extended',
         title='The Secretariat of State to the Nuncio in Spain, 1718&ndash;1720 &mdash; already read by George Lasry, and 61 more nomenclator groups recovered',
         blurb='Twenty-four ciphered despatches of Clement XI&rsquo;s Secretariat to the nuncio at Madrid (ASV Segr. Stato Spagna 364D, DECODE R154&ndash;R177), catalogued here as an unread transcription job behind a login. They were neither. George Lasry reconstructed the key in October 2020 and filed his segmented decipherment of the whole Spagna 364 corpus on every one of the records; measured token by token it reads 97.6 per cent of the 34,243 cipher groups. The gap was the nomenclator, where 189 of the 399 four-digit groups in use carried no value. Because the key is alphabetical in runs, 61 of them are recovered from the brackets and the corpus contexts &mdash; promozione, aggiustamento, giurisdizione, tribunale, vascelli, Vicer&egrave;, corriere &mdash; and the calendar block resolves into two parallel Gennaio&ndash;Dicembre runs, with 4538 Luglio confirmed by the date of Alberoni&rsquo;s promotion.',
         quote='&ldquo;in data delli 12 Luglio passato, qual appunto fu il giorno della promozione del Sig. Card.&rdquo; &middot; group 4538 confirmed',
         rights='Manuscript images: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='nunzio1736', label='Nunziatura di Spagna 1736', year='1736', y=1736.5, place='Rome &rarr; Madrid', st='found', stt='already solved; nomenclator recovered',
         title='The Secretariat of State to the Nunciature in Spain, 1736 &mdash; already read by George Lasry, and 46 of its code words recovered',
         blurb='Eleven ciphered despatches of Clement XII&rsquo;s Secretariat to Abate Guiccioli at Madrid, July to December 1736, during the rupture over Spanish recruiting in Rome (ASV Segr. Stato Spagna 423, DECODE R179&ndash;R188), catalogued as unread. George Lasry reconstructed the key in 2020 and filed his decipherment on every record, but his key gives no value to any of the 166 four-digit nomenclator groups. The nomenclator is not alphabetical, so 46 groups were recovered from context alone, among them N.S., V.S., S. Sede, Corte, Spagna, Napoli, Brevi, -mente and -zione, taking the text from 90.6 to 95.3 per cent read.',
         quote='&ldquo;N.S. &egrave; rimasto sommamente amareggiato nell&rsquo;udire che codesto [&hellip;] Molina, scordatosi degli obblighi di Vescovo&hellip;&rdquo;',
         rights='Manuscript: Archivio Apostolico Vaticano; images not reproduced'),
    dict(slug='windischgraetz1720', label='Windischgr&auml;tz 1720', year='1720&ndash;22', y=1720.5, place='Vienna &rarr; The Hague', st='solved', stt='read',
         title='Charles VI to Count Windischgr&auml;tz, 1720&ndash;1722 &mdash; the Emperor&rsquo;s secret letters read with the two keys from the same archive',
         blurb='Four autograph letters of Charles VI to his envoy at The Hague, catalogued on DECODE as non-decrypted, with both keys filed beside them: the Chancellery&rsquo;s 977-entry nomenclator and the Emperor&rsquo;s private key of numbers and signs. Transcribed and applied, they read every cipher passage. After Alberoni&rsquo;s fall the Emperor fears a French separate peace with Philip V through Morville, rejects Sardinia for Lorraine, claims the Montferrat equivalent and wants Portugal in the Alliance; in July 1720 Beretti Landi proposes a marriage between his children and Philip&rsquo;s sons.',
         quote='&ldquo;da nun der Alberoni aus Spannien abgeschafft&rdquo; &middot; Charles VI, 3 February 1720',
         rights='Manuscript images: St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE'),
    dict(slug='colonia1721', label='Brussels 1721', year='1721', y=1721.8, place='Brussels &rarr; Cologne', st='found', stt='already read; three values added',
         title='A cipher slip from Brussels to the Cologne nunciature, 9 October 1721 &mdash; already read by Lasry and Bonavoglia',
         blurb='A single leaf of comma-separated figures in the archive of the Cologne nunciature (DECODE R24), catalogued as an unread 1721 letter of unknown sender. The record already carries George Lasry&rsquo;s 2020 key and Paolo Bonavoglia&rsquo;s reading: a curate suspended <i>a divinis</i>, news wanted from Tournai, &ldquo;the Cologne affair&rdquo;, an offer to write to a correspondent. Checked against the image; three values added from context (qu, gli, g), date and place fixed from the heading; seven tokens stay open.',
         quote='sopra l&rsquo;affare di Colonia, ma egli, a quel che vedo, ne &egrave; informato',
         rights='Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='windischgraetz1721', label='Windischgr&auml;tz 1721', year='1721', y=1721.9, place='Brussels &rarr; Windischgr&auml;tz', st='solved', stt='read',
         title='The Windischgr&auml;tz brothers&rsquo; key letter, 18 November 1721 &mdash; read with Jakub M&iacute;rka&rsquo;s reconstructed key',
         blurb='A family letter of the Counts Windischgr&auml;tz catalogued on DECODE as non-decrypted: German in clear with thirteen passages in dotted numbers. The key Jakub M&iacute;rka reconstructed in 2023 from the brothers&rsquo; other letters, attached to the record, with no reading of the letter published, reads every letter-spelled passage at once. The writer, waiting for the Congress of Cambrai, complains of the Emperor, the Prince&rsquo;s plan and the succession; 23 nomenclator codes stay open.',
         quote='&ldquo;eine Excusation zu machen&rdquo; &middot; 22.38.23.3.40.36.27.20.6.30',
         rights='Manuscript images: St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE'),
    dict(slug='swieten1757', label='Van Swieten 1757', year='1757&ndash;59', y=1758.5, place='Bonn &rarr; Brussels', st='solved', stt='read',
         title='Van Swieten to Cobenzl from Bonn, 1757&ndash;59 &mdash; an alphabetical syllabary rebuilt from the ciphertext',
         blurb='Three despatches of the young Gottfried van Swieten to Count Cobenzl, catalogued on DECODE as non-decrypted. The 1757 passage carries its own decipherment and shows the system: an alphabetical list of letters and syllables. No key survives for the 1759 table, so it was rebuilt from 553 groups by annealing a code map held in alphabetical order against a French language model, then corrected from the clear text round each run. Read at 96%: the Gueldre convention, Moers, and a frank verdict on Soubise&rsquo;s army and its generals.',
         quote='&ldquo;le grand principe para&icirc;t &ecirc;tre de faire subsister l&rsquo;arm&eacute;e du roi sans qu&rsquo;il en co&ucirc;te un sou&rdquo; &middot; Bonn, 4 February 1759',
         rights='Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE'),
    dict(slug='kauderbach1754', label='Kauderbach 1754', year='1754&ndash;56', y=1755.4, place='The Hague &rarr; Dresden', st='solved', stt='read',
         title='Kauderbach&rsquo;s intercepted despatches from The Hague, 1754&ndash;56 &mdash; an unseparated syllable cipher split and read',
         blurb='Ten Dutch copies of letters of the Saxon-Polish resident to Dresden, with passages in figures that DECODE says were never solved: the figures run on without separation. The digits 5 and 8 turned out to be nulls, the rest two-figure codes for letters and syllables; Kauderbach&rsquo;s 1761 key in Dresden supplied the vocabulary, a one-to-one annealing search the numbers. All ten read: the Dutch quarrel over the augmentation of 1755, Yorke and the Saxon subsidy treaty, and the news of the Treaty of Versailles.',
         quote='&ldquo;Cette nouvelle a caus&eacute; une consternation extraordinaire ici&rdquo; &middot; Kauderbach on the Treaty of Versailles, 25 May 1756',
         rights='Koninklijk Huisarchief, The Hague, and S&auml;chsisches Hauptstaatsarchiv Dresden, via DECODE'),
    dict(slug='affry1757', label='d&rsquo;Affry 1757', year='1757&ndash;58', y=1757.5, place='The Hague &rarr; Versailles', st='partial', stt='read in part &mdash; 86% of groups; R1071 open',
         title='The comte d&rsquo;Affry&rsquo;s intercepted letters from The Hague, 1757&ndash;58 &mdash; the code rebuilt from Lyonet&rsquo;s decipherments',
         blurb='Eleven code letters of the French ambassador to Rouill&eacute; and Bernis in the Dutch royal archives, listed on DECODE as unsolved. The Dutch codebreaker Lyonet&rsquo;s decipherments of eight sibling letters were among the images, filed as clear pages; aligned group by group they rebuild the 1,200-group code, which reads nine of the undeciphered letters in part (86% of groups overall; R1071, in another code, stays unread). Convoys and herring, the Gouvernante&rsquo;s tears over her father, Ostend and Nieuport, spies for England and a French loan in London; Bussemaker&rsquo;s 1906 extracts recur word for word.',
         quote='&ldquo;faut-il que ce soit moi qui favorise les moyens de faire du mal &agrave; mon p&egrave;re?&rdquo; &middot; the Princess Governess to d&rsquo;Affry, April 1757',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='r1875', label='Foscarini 1761', year='1761', y=1761.8, place='Escorial &rarr; Venice', st='found', stt='read at the time',
         title='Foscarini to the Doge, Escorial 1761 &mdash; read at the time',
         blurb='DECODE R1875, catalogued as a ciphered letter from an unnamed sender in Spain to an unknown recipient, is despatch no. 178 of Sebastiano Foscarini, Venetian ambassador at the court of Charles III, written at the Escorial on 13 October 1761. The chancery deciphered it on the despatch itself, between the lines and on the facing pages, and barred out every cipher line. The letter reads in full: Madrid&rsquo;s view of the broken-off Anglo-French peace talks, and a union with &ldquo;another court&rdquo; &mdash; the secret Family Compact.',
         quote='&ldquo;&hellip;credono agevole il caso di una congiunzione atta a sostenere li vicendevoli interessi.&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Venezia, via DECODE (images not reproduced)'),
    dict(slug='lucini1767', label='Lucini 1767', year='1767', y=1767.8, place='Madrid &rarr; Rome', st='solved', stt='read',
         title='Nuncio Lucini from Madrid to the Secretariat of State, 13 October 1767',
         blurb='A clear letter from the Madrid nunciature whose last sentence goes into figures. Lasry&rsquo;s 2020 key for the series was on the DECODE record, but nobody had deciphered this passage. Read here after one transcription slip and one wrong key value were corrected: the nuncio thinks Charles III wants a permanent licence to try clergy before lay judges in order to put down unrest.',
         quote='i tumulti interni della monarchia, i quali di quando in quando si fanno sentire',
         rights='Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='eichel1758', label='Eichel 1758', year='1758', y=1758.0, place='Prussia', st='found', stt='nulls only, no message',
         title='Mr Eichel&rsquo;s cipher sheet of 1758 &mdash; a page made only of nulls and blank key cells',
         blurb='TNA SP 106/7 (DECODE R595), 139 number groups docketed &ldquo;Cypher from Mr Eichel 1758 / Prussia&rdquo; and listed as an unsolved letter whose key was thought to be R594. R594 does not fit. The key in the same volume, R596, declares every number containing a 7 and four ranges to be nulls: that makes 117 of the 139 groups nulls, and 21 of the other 22 fall on cells the key leaves blank. The sheet hides no message.',
         quote='&ldquo;Tous les nro o&ugrave; je trouve un ou plusieurs 7 sont les nonvaleurs&rdquo; &middot; heading of key R596',
         rights='The National Archives, Kew, via DECODE R595'),
    dict(slug='acciaiuoli1757', label='Acciaiuoli 1758', year='1758&ndash;60', y=1758.7, place='Lisbon &rarr; Rome', st='solved', stt='read',
         title='Nuncio Acciaiuoli from Lisbon to the Secretariat of State, 1758&ndash;60',
         blurb='Eight nunciature ciphers from Portogallo 117 that DECODE lists as partially decrypted. Lasry&rsquo;s 2020 key had turned them into letters with the code words open; three leaves deciphered at the time fix 25 codes, and the rest read as Italian. The first is the nuncio&rsquo;s secret account of the attempt on Jos&eacute; I of 3 September 1758.',
         quote='il Teixeira ferito a morte &hellip; il Re molto ferito del braccio destro',
         rights='Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='michell1751', label='Michell 1751', year='1751', y=1751.99, place='Berlin &rarr; London', st='found', stt='already in print',
         title='Frederick the Great to Louis Michell, 28 December 1751 &mdash; an intercepted Prussian cipher matched to the King&rsquo;s printed minute',
         blurb='A numerical nomenclator letter of Frederick II to his London resident, copied by the Dutch in The Hague and catalogued on DECODE as non-decrypted (R1957). Its clear opening, its length and the order of its repeated groups (1064 Vienne four times, 4310 Sardaigne three times, 3042 dessein) identify it as no. 5263 of the Politische Correspondenz, printed in 1882 from the minute: the King&rsquo;s secret order to learn whether London knew of an Austro-Russian plan to crown Charles of Lorraine in Poland.',
         quote='&ldquo;il faut que vous ne le fassiez sur tout ce que dessus qu&rsquo;&agrave; moi seul imm&eacute;diatement&rdquo; &middot; Frederick II, 28 December 1751',
         rights='Manuscript images: Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='anne1711', label='Queen Anne to Peterborough 1712', year='1712', y=1712.15, place='London &rarr; Turin', st='found', stt='already in print',
         title='Queen Anne to the Earl of Peterborough, 22 February 1712 &mdash; ciphered instructions matched to the text printed in 1798',
         blurb='Signed instructions, clear English with 61 runs of a numerical code (414 groups), catalogued on DECODE as non-decrypted and described as for Peterborough&rsquo;s embassy to Turin (R4878). The whole text is printed in Parke&rsquo;s edition of Bolingbroke&rsquo;s correspondence (1798), and every code run falls into place: 534 is <em>to</em> at all eight places, 894 <em>him</em>, 609 <em>his</em>, 1373 <em>religion</em>. What the cipher hides is a secret mission to stop the Electoral Prince of Saxony from turning Catholic in Rome, and if need be to spirit him away to a Protestant country.',
         quote='&ldquo;the proper measures for rescuing him out of the hands he is in, and bringing him safe to our dominions&rdquo; &middot; Queen Anne, 22 February 1711/12',
         rights='Text: Parke 1798. Manuscript: British Library Add MS 4107 (images not reproduced)'),
    dict(slug='mondoucet', label='Mondoucet', year='1571&ndash;74', y=1572, place='Brussels &rarr; the Court', st='partial', stt='read in part',
         title='Mondoucet&rsquo;s despatch of 13 July 1572 &mdash; a segmenter, not the archive',
         blurb='A Gallica sweep for volumes outside the standard lists found BnF fr. 16127, the Court&rsquo;s file of Claude de Mondoucet&rsquo;s correspondence from the Low Countries, 1571&ndash;74: about twenty ciphered despatches in one system, most with the Court&rsquo;s decipherment, one long letter of 13 July 1572 without. Four aligners proved on controls had all sat at the shuffled baseline &mdash; not because of the archive but because an automatic glyph segmenter, the one stage never checked against a hand count, split looped d, crossbarred long-s and barred o/q into two components each and manufactured a 1.3&ndash;1.4 glyph-per-letter ratio. At glyph level it is an ordinary sixteenth-century homophonic substitution, one glyph per letter, four nulls. The key was built by hand from the 16 July crib in the same volume &mdash; the decipherer&rsquo;s interlinear glosses on f. 62r and the verbatim reading at f. 64 &mdash; and a French 5-gram beam decoder then decoded the despatch; a re-check on 21 Sept 2026 found that decode over-read: only scattered words (1&ndash;8&nbsp;%) are sense, so the despatch stays unread. The decisive control is internal: decoding the 16 July block reproduces the decipherer&rsquo;s own gloss verbatim. Partly enciphered, its clear bands give Spanish troop counts before Mons and German levies at Maastricht; the cipher carries Mondoucet&rsquo;s reading of the Protestant position four days before Genlis&rsquo;s column was destroyed at Saint-Ghislain and six weeks before St Bartholomew. The 1573 letters are settled too: 9 September has a verbatim Court decipherment, and the 4 January passage, which has none, was decoded ciphertext-only to about 60&nbsp;% with a key rebuilt from it, then found printed in clear in Didier&rsquo;s 1891 edition of Mondoucet&rsquo;s register.',
         quote='&ldquo;leur delivrance des espagnols a ce moyen&rdquo; &middot; the recovered key reproduces the decipherer&rsquo;s own gloss',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='bethune', label='B&eacute;thune 1601', year='1601', y=1601, place='Paris &rarr; Rome', st='partial', stt='two of three read',
         title='Henri IV to B&eacute;thune, 9, 10 and 22 November 1601 &mdash; two letters read, and the ceiling on the third measured',
         blurb='Three ciphered letters of the King to his ambassador in Rome, BnF fr. 3484, catalogued &ldquo;avec chiffre&rdquo; with no decipherment. The notice&rsquo;s &ldquo;copie du n&deg; pr&eacute;c&eacute;dent&rdquo; turns out to be the minute of the 10 November letter in clear, and aligning it with the cipher recovers a Villeroy-office key of the design Bazeries printed for B&eacute;thune&rsquo;s brother in 1599: ten thousand &eacute;cus to Cardinal Aldobrandini for the Peace of Lyon. The 22 November letter is now read too &mdash; it interleaves clear French with its cipher, and carries the Camaiano pension, Barberini&rsquo;s coming and the dauphin&rsquo;s baptism. The 9 November letter, a solid page of cipher, stops at about six words in ten, and an oracle bound shows why: the decoder is already past the ceiling its transcription allows.',
         quote='&ldquo;car j&rsquo;affectionne led. Cardinal et desire m&rsquo;acquitter de lad. promesse que je luy ay faicte&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='randolph1570', label='Randolph to Sussex 1570', year='1570', y=1570.51, place='Edinburgh &rarr; the Earl of Sussex', st='found', stt='read at the time',
         title='Randolph to Sussex, 5 July 1570 &mdash; the cipher and its decipherment on the next leaf',
         blurb='DECODE R4931 (Cotton Caligula C II f. 277), catalogued as an unread Randolph letter of 1569, is Randolph&rsquo;s despatch from Edinburgh of 5 July 1570. A crib attack from Boyd&rsquo;s abstract read about 70% of the cipher before the next leaf, f. 278 (DECODE R4932), turned out to be its contemporary decipherment. Every cipher run is read: the Scottish Queen&rsquo;s party&rsquo;s distrust of Elizabeth, the stayed regency, Morton, the money, the soldiers&rsquo; pay, Grange.',
         quote='have litle confidens [in] the Q. of England, that so ofte changeth her course',
         rights='British Library, via DECODE R4931/R4932'),
    dict(slug='hamilton1569', label='Mary to Archbishop Hamilton 1569', year='1569', y=1569.05, place='Bolton &rarr; the Archbishop of St Andrews', st='found', stt='read at the time',
         title='Mary Queen of Scots to Archbishop Hamilton, 18 January 1569 &mdash; the decipherment transcribed',
         blurb='DECODE R8347 (BL Add MS 33531 ff. 73&ndash;74), catalogued with no names and dated January 1568, is Mary Queen of Scots writing from Bolton to John Hamilton, Archbishop of St Andrews, on 18 January 1569. The contemporary decipherment is bound in as f. 74, Bain calendared it and Tomokiyo published the key. The decipherment is transcribed in full: Mary refuses to hand over her son, counts on ten thousand men from France and Spain, and orders the rebels&rsquo; houses taken before an amnesty.',
         quote='&ldquo;I wil not leif thame that hes not left me&rdquo;',
         rights='Manuscript images: British Library, via DECODE R8347'),
    dict(slug='throck1569', label='Throckmorton to Moray 1569', year='1569', y=1569.55, place='Greenwich &rarr; the Regent of Scotland', st='found', stt='read at the time; text recovered',
         title='Throckmorton to the Regent Moray, 20 July 1569 &mdash; the Norfolk marriage letter, read',
         blurb='DECODE R8348 (BL Add MS 33531 ff. 79&ndash;80), catalogued with no sender and dated 26 July, is Sir Nicholas Throckmorton&rsquo;s letter to Moray from Greenwich, 20 July 1569. It was deciphered between the lines at the time and summarised by Bain, but a water stain has faded half of the old decipherment. Every cipher passage is read again from the cipher with Tomokiyo&rsquo;s key: the council&rsquo;s plan for the Queen of Scots&rsquo; restoration and marriage, and a plea to send Lethington.',
         quote='&ldquo;I can assure your lordship there is not one, no, not one&rdquo;',
         rights='Manuscript images: British Library, via DECODE R8348'),
    dict(slug='norfolk1570', label='Mary to Norfolk', year='1570', y=1570.1, place='Tutbury &rarr; the Tower', st='solved', stt='read',
         title='Mary Queen of Scots to the Duke of Norfolk, &ldquo;the 20th&rdquo;, February or March 1570 &mdash; the one letter of the series with no contemporary decipherment',
         blurb='BL Cotton MS Caligula C II f. 74r is the only letter of Mary&rsquo;s ciphered correspondence with Norfolk in the Tower with no contemporary decipherment, dated only &ldquo;the tventi of this instant&rdquo;. Tomokiyo rebuilt the key from the three deciphered siblings and overlaid a partial letter-by-letter decode. Undeciphered did not mean unsolved: the key was available, and the contribution here is the transcription and the reading. The key is checked on f. 66r, and the letter is read in 23 lines from the new British Library IIIF images, stitched from tiles. Written weeks after the Regent Moray&rsquo;s murder: Elizabeth blames Mary for the harquebus shot, Morton is rumoured on the move, and Norfolk is to write through the Bishop of Ross or Lady Scrope, never in his own hand.',
         quote='&ldquo;I am asured that sche &hellip; sueves me the veyt of Murray death; but God knoueth&rdquo;',
         rights='Manuscript images: British Library'),
    dict(slug='lanssac', label='Lanssac', year='1573', y=1573, place='Warsaw &rarr; Paris', st='solved', stt='read',
         title='Lanssac to Charles IX, Warsaw, 26 April 1573 &mdash; the Polish election embassy&rsquo;s cipher',
         blurb='BnF fr. 4735 f. 124, catalogued &ldquo;avec chiffre&rdquo; with no decipherment. The key is a homophonic letter cipher with word signs, recovered from a sibling letter whose Court decipherment survives as gutter-cut marginal notes (&ldquo;car je n&rsquo;ay pas cinquante escuz&rdquo;) and checked against the fragments on f. 124 itself. Both passages read, and the key then opens the three election letters whose only &ldquo;decipherment&rdquo; was that cut gloss: the Polish nation &ldquo;autant v&eacute;nale &hellip; comme sont les Allemans&rdquo;, the Emperor&rsquo;s three hundred thousand spent for nothing, and on 9 May the election carried against the Sultan, the Emperor, the princes of the Empire, Spain, Muscovy and Sweden, &ldquo;qui tous estoient bandez contre vostre Majest&eacute;&rdquo;. Tomokiyo&rsquo;s published table for the cipher is corrected.',
         quote='&ldquo;qui tous estoient bandez contre vostre Majest&eacute;&rdquo; &middot; P&#322;ock, 9 May 1573',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='pelissier1592', label='Pelissier 1592', year='1592', y=1592.7, place='Burgos &rarr; France', st='partial', stt='read in part &mdash; 93% of words',
         title='Pelissier to Jeannin, Burgos, 13 September 1592 &mdash; the League&rsquo;s agent at Philip II&rsquo;s court',
         blurb='Nine pages, mostly in cipher, that Tomokiyo lists as only partially deciphered: the League&rsquo;s agent in Spain reporting to Mayenne&rsquo;s councillor four months before the Estates of 1593. Tomokiyo&rsquo;s key for Pelissier&rsquo;s later letters fits; calibrated on 1,764 signs of those letters aligned with their clear text, it reads 93&nbsp;% of the plaintext words, about 250 gaps marked. Philip grants 500 ducats, Pelissier argues against holding the Estates now and for two armies at 300,000 &eacute;cus a month, and reports the case being made in France for Navarre.',
         quote='&ldquo;la nomination d&rsquo;un roy legitime pour l&rsquo;opposer a l&rsquo;heretique et tyran&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='needham1587', label='Needham before Sluys 1587', year='1587', y=1587.57, place='Sluys &rarr; Walsingham', st='solved', stt='read',
         title='Francis Needham before Sluys, 28 July 1587 &mdash; the pigpen letter, read',
         blurb='BL Harley MS 287 ff. 39&ndash;40, catalogued on DECODE as a partially decrypted letter of &ldquo;Needham&rdquo; to an unknown recipient, is Francis Needham&rsquo;s letter to Walsingham from Leicester&rsquo;s fleet before Sluys. A contemporary hand glossed a few cipher words; the long runs of f. 39v were bare. The key, a three-grid pigpen with the alphabet in order, was rebuilt from the glosses and every run was read: Parma had closed the channel with hoys and flyboats chained together.',
         quote='&ldquo;the chanel was b[&hellip;]ed with hoyes and flyboates fastened wyth chaynes, strengthned behind wyth flatt bootes&rdquo;',
         rights='Manuscript images: British Library, via DECODE'),
    dict(slug='harley287', label='Cobham at Ostend 1588', year='1588', y=1588.2, place='Ostend &rarr; Walsingham', st='solved', stt='read',
         title='Lord Cobham at Ostend, 20&ndash;22 March 1588 &mdash; the peace commissioner&rsquo;s cipher, read',
         blurb='BL Harley MS 287 ff. 70&ndash;72, catalogued on DECODE as seven ciphertexts of an unknown sender to an unknown recipient, are two letters of Lord Cobham, Elizabeth&rsquo;s peace commissioner at Ostend, of 20 and 22 March 1587/8, with a report from Middelburg. No decipherment existed. Broken from the clear words around the runs: a graphic-sign substitution with a small nomenclator (15 = Parma, &#9633; = the States). Every run reads, among them Parma&rsquo;s new canal from Ghent to Sluys and the prisoners Pigot and Barney.',
         quote='&ldquo;I would think myself most unhappy to be a means to conclude an irreligious peace&rdquo;',
         rights='Manuscript images: British Library, via DECODE'),
    dict(slug='morosini1588', label='Morosini 1588', year='1588&ndash;89', y=1588.8, place='Blois &rarr; Rome', st='solved', stt='read',
         title='Cardinal Morosini, legate in France, to Montalto, 1588&ndash;89 &mdash; thirty-six nunciature ciphers read with the 1587 key',
         blurb='Thirty-six cipher enclosures from the papal legate in France to the Cardinal Nephew, catalogued on DECODE as partially decrypted, with the key Meister printed in 1906 attached but no plaintext. The figures run on without separators and each letter has one-, two- and three-digit homophones, so every page was cut up by a beam search scored with an Italian model. Thirty-four read end to end and two in a second key in part: the Council of Trent, the Estates of Blois, Saluzzo, the murder of the Guises, and Henri III&rsquo;s march on Paris.',
         quote='&ldquo;il Duca di Guisa nela camera di S. M.t&agrave; &egrave; stato per ordine di S. M.t&agrave; amazato a colpi di pugnale&rdquo;',
         rights='Archivio Apostolico Vaticano, via DECODE R18&ndash;R58'),
    dict(slug='maisse1592', label='Maisse 1592&ndash;93', year='1592&ndash;93', y=1592.85, place='the Court &rarr; Venice', st='solved', stt='key verified, read',
         author='Arya Sanketbhai Patel',
         title='Henri&nbsp;IV to Maisse at Venice, 1592&ndash;93 &mdash; four &ldquo;undeciphered&rdquo; leaves, two ciphers, and a clear copy of every one',
         blurb='Four royal despatches to the ambassador at Venice, BnF fr. 16093 ff. 370, 373, 406 and 410, listed as undeciphered. They are two ciphers, not one, and Tomokiyo had already reconstructed a key for each from the sibling letters &mdash; published <em>as images</em>, which is why a text dump of his page shows no table and the keys look missing. Applying the 1592 key to f. 370 decodes its opening letter-for-letter: 81 of 81 characters against a contemporary clear copy found independently, through the old Harlay pi&egrave;ce numbers, in Brienne 13 = BnF NAF 6984. The leaf also carries an omega-shaped sign for <em>d</em> that is not in the published table. f. 406 turns out to be the duplicate of f. 404, so the four leaves are three despatches.',
         quote='&ldquo;le cardinal de Gondy aura pass&eacute; pr&eacute;s de vous&rdquo; &middot; f. 370 decoded, 3 November 1592',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='orbais', label='Orbais 1589', year='1589', y=1589.65, place='Rome &rarr; Paris', st='solved', stt='read',
         title='A letter from Rome to the abb&eacute; d&rsquo;Orbais, 23 August 1589 &mdash; the three keys bound with it do not fit',
         blurb='BnF fr. 3413 no. 62 was catalogued with three cipher keys bound in the same volume that might read it. None does. The letter, from a secretary of Cardinal Pellev&eacute; in Rome to Jean de Piles of the League&rsquo;s council in Paris, is almost all in clear and carries the news of Henri&nbsp;III&rsquo;s murder as it reached Rome. Its ninety-odd signs of cipher are in the Nevers&ndash;Piles alphabet that Tomokiyo identified. His partial table was filled out from a deciphered letter of 1586 in fr. 4715 in the same cipher. Read: <em>Cassin</em>, <em>la protection</em>, <em>vostre regne</em>, <em>depeschera</em>, <em>mon maitre a est&eacute; retir&eacute;</em>, and the signature, probably <em>Baron</em>. About thirty signs, most of them code signs, remain open.',
         quote='&ldquo;le Roy a est&eacute; tu&eacute;, et c&rsquo;est le Roy de Navarre qui l&rsquo;a faict faire&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='cobham1588', label='Cobham 1588', year='1588', y=1588.4, place='Ostend &rarr; Walsingham', st='solved', stt='read',
         title='Lord Cobham to Walsingham, May&ndash;June 1588',
         blurb='Four letters of the English peace commissioner in the Low Countries, clear English with cipher passages in Greek-like signs (BL Harley 287, DECODE R8490&ndash;R8496). The key record the catalogue pointed to is Bodley&rsquo;s 1590 cipher. The right alphabet comes from Cobham&rsquo;s April letters in the same volume, deciphered between the lines at the time. A sign inventory from the glosses and a word solver read about a third of the cipher words: armadas, the haven, Italians arriving, within France.',
         quote='&Lambda;&#1016;7&perp;V = their (f. 75, interlinear)',
         rights='British Library, via DECODE'),
    dict(slug='dinteville1592', label='Dinteville 1592', year='1592', y=1592.5, place='Langres &rarr; Nevers', st='stuck', stt='not read',
         title='Dinteville to the Duke of Nevers, 3 July 1592',
         blurb='DECODE lists BnF fr. 3621 f. 130 as a letter with its decipherment, but the leaf has none: two cipher passages in a clear letter, and a clear postscript. A sibling Dinteville letter on f. 128, in the same signs, carries an interlinear decipherment of about 150 signs. It does not fit a one-sign-one-letter key, and the letter stays unread.',
         quote='avoir veu d&rsquo;ascendre a Geneve deux millions d&rsquo;or d&rsquo;Espaigne (f. 128)',
         rights='Biblioth&egrave;que nationale de France'),
    dict(slug='gonzaga1590', label='Mantua to Nevers 1590', year='1590', y=1590.71, place='Mantua &rarr; Nevers', st='solved', stt='read',
         title='Vincenzo Gonzaga, Duke of Mantua, to the duc de Nevers (1590)',
         blurb='A letter of 17 September 1590 from the Duke of Mantua to his uncle Nevers, with long passages in unbroken two-digit figures, catalogued as not deciphered and credited to &ldquo;the duke of Nevers&rdquo;. The key filed in Nevers&rsquo;s papers, BnF fr. 3995 f. 64 (Tomokiyo no. 35), reads it unchanged: 95% of the cipher. Mantua passes on the rumour that Sixtus V was poisoned by the Spaniards and assures Henri IV of his devotion against the common enemy.',
         quote='che la morte del Papa sia stata procurata con veleno da Spagnoli',
         rights='Biblioth&egrave;que nationale de France'),
    dict(slug='champagne1590', label='Champagne 1590', year='1590&ndash;91', y=1590.5, place='Paris, Champagne &rarr; Nevers', st='solved', stt='read',
         title='Champagne news-letters to Nevers (1590&ndash;91)',
         blurb='Six letters to the duc de Nevers catalogued as one ciphered correspondence. No. 23 is a clear copy with a nine-entry name code whose key is bound on the next leaf, and reads in full. Nos. 24, 25 and 60 share a two-digit alphabet laid out in alphabetical order, rebuilt from a few letters glossed between the lines: ten of twelve runs read. No. 78 and Lauri&egrave;re&rsquo;s 1593 letter stay open.',
         quote='la rupture de l&rsquo;edict [de] l&rsquo;union &middot; contre la ligue',
         rights='Biblioth&egrave;que nationale de France'),
    dict(slug='stowe166', label='Edmondes to Burghley 1592&ndash;94', year='1592&ndash;94', y=1592.2, place='Henri IV&rsquo;s court &rarr; Burghley', st='solved', stt='read',
         title='Edmondes to Burghley, 1592&ndash;1594 &mdash; &ldquo;Lord Threr?&rdquo; and the King&rsquo;s secrets',
         blurb='BL Stowe MS 166, catalogued on DECODE as six ciphertexts of &ldquo;Lord Threr?&rdquo; to an unknown recipient, are despatches to the Lord Treasurer, Burghley, in Thomas Edmondes&rsquo;s papers, written from Henri IV&rsquo;s camp in 1592 and 1594. The graphic-sign cipher is a simple substitution of English with a few homophones and person signs, broken from the clear text around it. Every passage reads except four lines on f. 59: the King breaking off his sister&rsquo;s marriage, Montmorency&rsquo;s demand for the young Cond&eacute;, and designs on Reims in 1594.',
         quote='&ldquo;the K. thereuppon saide vnto me that his faith is not vendible&rdquo;',
         rights='Manuscript images: British Library, via DECODE'),
    dict(slug='lorraine1592', label='Lorraine 1592', year='1592', y=1592, place='Nancy &rarr; Vaud&eacute;mont', st='partial', stt='key recovered, read in part',
         author='Arya Sanketbhai Patel',
         title='Charles III of Lorraine to Vaud&eacute;mont, 18 June 1592 &mdash; a cipher catalogued as undecrypted, broken',
         blurb='BnF Fran&ccedil;ais 3621 no. 97, recorded in the DECODE database as <em>Non-decrypted</em>, with no key ever published and no crib in the volume: the January intercepts it was hoped to match exist only as a plaintext decipherment. An earlier attempt failed by treating it as a symbol cipher and clustering the glyphs by shape. They are <strong>ordinary cursive letterforms</strong> and can simply be read. The old solver was then shown, on controls with known keys, to be incapable of a cipher this size &mdash; 37&ndash;56% of letters at &minus;2.64 where the true key scored &minus;1.62 &mdash; and was replaced by a steepest-ascent search that recovers known keys at 98.7&ndash;99.6%. The key it found is verified against the manuscript, not the model: the group spelling <em>chasteau</em> occurs twice in the cipher, and Chasteauvillain stands in the clear on the same page. The Duke orders his son to conserve the plain and to bring the army back into the quarters of La Fauche.',
         quote='&ldquo;ramener mon arm&eacute;e &hellip; es quartiers de la Faulche&rdquo; &middot; DECODE 9449: Non-decrypted',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='nevers1589', label='Nevers intercepts 1589', year='1589', y=1589.8, place='intercepted traffic &rarr; Nevers', st='found', stt='nothing to read; eleven found',
         author='Arya Sanketbhai Patel',
         title='The intercepts summarised for Nevers, 1589 &mdash; the ciphertext is not there, and eleven deciphered ones are',
         blurb='BnF fr. 3977 no. 96 digests several letters written in cipher by the King&rsquo;s enemies in September and October 1589 and sent to the duc de Nevers to be interpreted. The catalogue could not say whether the ciphered originals survive beside it. They do not: every September&ndash;October piece in the volume is in clear, and the digest itself is clear French &mdash; Merc&oelig;ur asking Spain for help, powder carried to Nantes &ldquo;avec le chiffre g&eacute;n&eacute;ral d&rsquo;Espagne&rdquo;, Mendoza at Bayonne on Arques and Dieppe, Spain pressing the Pope to renew the excommunication. The sweep turned up something better: eleven <em>other</em> intercepted ciphered letters in the same volume, February to August 1589, each carrying its contemporary decipherment written word by word above the cipher &mdash; three of them from Mendoza to the duke of Parma, hidden in a multi-folio catalogue entry.',
         quote='&ldquo;plusieurs lettres escriptes en chiffre par les ennemis du Roy &hellip; envoy&eacute;es pour estre interpret&eacute;es&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='lebel1593', label='Lebel to Savoy 1593', year='1593', y=1593.15, place='Paris &rarr; Turin', st='solved', stt='read',
         title='Lebel to Charles Emmanuel I of Savoy, 1593 &mdash; three unread letters from the Estates of the League',
         blurb='BnF fr. 3983 nos. 11, 62 and 100, January&ndash;March 1593: Tomokiyo rebuilt the key in 2017 and published these letters as images with many code groups undeciphered, but no reading. They are read here with his key, a dozen corrections to its letter signs and code values harvested from the letters deciphered at the time and from context in BnF esp. 336: about 98% of the enciphered tokens valued, all of no. 100 and 98% of no. 62&rsquo;s recto. Mayenne wants the crown or the regency, Spain buys him off with 40,000 &eacute;cus and offers four millions, the Cardinal de Bourbon offers a marriage, Feria&rsquo;s jurist is laughed at, and Mayenne&rsquo;s council prepares a truce. Open: the bled-through verso of no. 62 and a set of single-context code values.',
         quote='&ldquo;qui sont le de Lyon, Villeroy, et le troisiesme qu&rsquo;est le pr&eacute;sident Jannin&rdquo;',
         rights='Biblioth&egrave;que nationale de France, Gallica'),
    dict(slug='nevers1593', label='Nevers 1593', year='1593', y=1593.5, place='Nevers &rarr; Rome', st='partial', stt='2 of 7 read',
         title='Nevers to Pisany, 1593 &mdash; the numerical key reads two letters, and the other five were never in it',
         blurb='Seven ciphered copies of the duc de Nevers&rsquo; letters from the road to Rome, catalogued as one office&rsquo;s key. They are two. Tomokiyo&rsquo;s Nevers cipher no. 46, read from the full-resolution table in fr. 3995 and checked against the office&rsquo;s own decipherment of a Gondi letter, resolves every figure of the two letters to Pisany: the 8 September letter whole, the 14 October one in long stretches. The five letters to Revol are in the Court&rsquo;s symbol cipher no. 60; one copy is in clear, one carries ninety symbols, three were not reached.',
         quote='&ldquo;l&rsquo;on n&rsquo;a volont&eacute; de contanter le Pape, que l&rsquo;on n&rsquo;y aille poynt&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='sp106r927', label='SP 106/10 pigpen letter', year='17th c.', y=1650, place='? &rarr; &ldquo;Monsieur&rdquo;', st='partial', stt='broken, read in part',
         title='The SP 106/10 pigpen letter &mdash; a French letter in a homophonic &ldquo;masonic&rdquo; cipher',
         blurb='TNA SP 106/10 ff. 241&ndash;243, catalogued in DECODE as an undeciphered letter in the masonic alphabet. The textbook dotted-pigpen key pencilled on its flap reads nothing. The cipher is homophonic: cell shape plus dot count, several signs for common letters. A hand transcription of the last page let a quadgram solver find French, and the last page now reads almost in full: a client condoling to a patron over a gentleman&rsquo;s marriage and begging the continuance of his goodwill. The first page is read in fragments; writer and recipient are unnamed.',
         quote='&ldquo;et vous supplie tres humblement, monsieur, me continuer l&rsquo;honneur de vostre bienveuillance&rdquo;',
         rights='Manuscript rights: The National Archives, Kew'),
    dict(slug='walsingham1585', label='Walsingham 1585', year='1585', y=1585.65, place='London &rarr; Scotland', st='partial', stt='read in part &mdash; 14 sign words open',
         title='Walsingham to Edward Wotton in Scotland, July&ndash;September 1585',
         blurb='Four letters of the Secretary to his ambassador during the Arran crisis, listed on DECODE as non-decrypted ciphers with graphic signs. They are signed letters in clear English with a two-digit name code; two are already calendared in CSP Scotland vol. 8, whose glosses fix 19 Arran, 39 the Master of Gray, 40 the Justice Clerk, 24 Farnihurst and 20 Morton. The other two are transcribed here. About fourteen words in a sign alphabet on 10 September stay unread: the decipherment written above them was blotted out.',
         quote='&ldquo;The best is to deal warily with them all&rdquo;',
         rights='Manuscript rights: British Library, Add MS 32657 (images via DECODE)'),
    dict(slug='wotton1585', label='Wotton 1585', year='1585', y=1585.7, place='Scotland &rarr; London', st='solved', stt='read &mdash; clear drafts, code names identified',
         title='Edward Wotton from Scotland to Walsingham, August&ndash;September 1585',
         blurb='Three despatches of the English ambassador in Scotland, listed on DECODE as non-decrypted numerical ciphers. The pages are Wotton&rsquo;s own drafts in clear English, with one- and two-digit code numbers for persons and places. Read in full, and the numbers identified from context: 19 Arran, 39 the Master of Gray, 10 King James certain, four more probable, four open. They carry the plot that toppled Arran in November 1585.',
         quote='&ldquo;Sir, 39. came to me yesterday&rdquo; &middot; &ldquo;to disgrace 19 with 10&rdquo;',
         rights='British Library, via DECODE'),
    dict(slug='bergamo1585', label='Paris nunciature, Francia 18', year='1585&ndash;87', y=1586.2, place='Paris &rarr; Rome', st='solved', stt='read &mdash; R16 and R17 read here',
         title='The Paris nunciature to the Secretariat, Francia 18, 1585&ndash;87', blurb='Three ciphered despatches catalogued as partly decrypted (AAV Segr. Stato Francia 18, DECODE R15&ndash;R17). R15 had been read by George Lasry; R16&rsquo;s decryption on DECODE is a copy of R15&rsquo;s, so R16 was unread. Read here with Lasry&rsquo;s key and the nomenclator Meister printed in 1906: Guise refuses the King&rsquo;s sale of church property unless given Metz and money. R17 reads with Meister&rsquo;s key no. 40 of 1587: Lorraine, the Guises and the reiters.', quote='il Duca di Guisa mi ha mandato a dire', rights='Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='harley1582r8500', label='Stafford August 1586', year='1586', y=1586.63, place='Paris &rarr; Walsingham', st='solved', stt='read',
         title='Stafford to Walsingham, Paris, 20 August 1586 &mdash; Read',
         blurb='DECODE R8500, catalogued as a non-decrypted letter of an unknown sender, London, is Sir Edward Stafford&rsquo;s holograph despatch from Paris of 20 August 1586 (BL Harley MS 1582 ff. 65&ndash;66). Its five cipher runs in the postscript were never deciphered on the page. Read here with Stafford&rsquo;s letter key, rebuilt from a contemporary decipherment (f. 72r) and glosses (f. 73r) on sibling letters: <code>6</code> is <i>e</i>, not a null. Junius&rsquo; son came from Cambrai with papers of his credit with Balagny.',
         quote='&ldquo;came hither Junius sonne from Cambraye&rdquo;',
         rights='Manuscript: British Library, Harley MS 1582 (images on DECODE, not reproduced)'),
    dict(slug='stafford1586', label='Stafford 1586', year='1586', y=1586.72, place='Paris &rarr; Walsingham', st='found', stt='read at the time',
         title='Stafford to Walsingham, Paris 1586 &mdash; Read',
         blurb='DECODE R8503, catalogued as a cipher letter of Sir Edward Stafford to an unknown recipient, is his holograph despatch from Paris to Sir Francis Walsingham of 19 September 1586 (BL Harley MS 1582 ff. 74&ndash;75). Its four short cipher runs were deciphered between the lines at the time. Re-read sign by sign here, they check exactly: a null <code>6</code>, homophones for <i>i</i>, <i>l</i> and <i>e</i>, and codes 47, 59 and 74 for Navarre, Cond&eacute; and Guise.',
         quote='&ldquo;three &hellip; sworn and dispatched to kill him and the Prince of Cond&eacute;&rdquo;',
         rights='Manuscript: British Library, Harley MS 1582 (images on DECODE, not reproduced)'),
    dict(slug='harley1582r8504', label='Stafford November 1586', year='1586', y=1586.86, place='Paris &rarr; Walsingham', st='solved', stt='read',
         title='Stafford to Walsingham, 9 November 1586 &mdash; Read',
         blurb='DECODE R8504, catalogued as a non-decrypted cipher letter of Sir Edward Stafford to an unknown recipient (BL Harley MS 1582 ff. 76&ndash;77), is a short holograph in clear English. Its one cipher word, seven signs on line 2, reads <i>princes</i> with Stafford&rsquo;s letter key rebuilt from sibling letters in the same volume. Not calendared in CSP Foreign.',
         quote='&ldquo;a paquet wth princes from your honor&rdquo;',
         rights='Manuscript: British Library, Harley MS 1582 (images on DECODE, not reproduced)'),
    dict(slug='clair357', label='Clairambault 357, 1586', year='1586', y=1586.8, place='Angoumois &rarr; a League leader', st='found', stt='decipherment found',
         title='An anonymous figure cipher of October 1586 &mdash; the &ldquo;unread&rdquo; two thirds were deciphered in 1586, on the next leaf and between the lines',
         blurb='A League-period letter in two-digit figures, listed with a partial key and two thirds of its first page unread. The volume holds its own decipherment: folio 168 is a clear text of the cipher down to a cross mark, and from that cross to the end the decipherer wrote the plaintext between the lines. Tomokiyo&rsquo;s key agrees with the glosses (<em>Guienne</em>, <em>tres confident</em>, <em>Fum&eacute;</em>), which also give 87&nbsp;=&nbsp;e and the King of Navarre&rsquo;s sign. The letter: Fum&eacute;, vice-admiral of Guyenne and Navarre&rsquo;s Catholic confidant, keeps proposing a reconciliation between Navarre and the addressee, probably Guise, while Catherine de M&eacute;dicis negotiates.',
         quote='&ldquo;Fum&eacute;, visadmiral de Guienne, tres confident du Roy de Navarre, bien qu&rsquo;il soit catholique&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='mendoza1589', label='Mendoza 1589', year='1589', y=1589, place='San Lorenzo &rarr; Paris', st='found', stt='resolved',
         title='Philip II to Mendoza, 7 September 1589 &mdash; the &ldquo;second undeciphered letter&rdquo; is the decipherer&rsquo;s copy',
         blurb='BnF fr. 3641 holds both of Philip II&rsquo;s letters of that day twice: the originals in the general cipher Cg.13 and the 1589 decipherer&rsquo;s fair copies, laid out like the originals with the unread code words in the margin, one of them miscatalogued as a second cipher letter. Aligning the pairs rebuilds some seventy syllables and fifty code groups of Cg.13, reads groups the decipherers left blank (respeto, vuestro, negocio) and corrects their &ldquo;Francia&rdquo; to England. Fourteen groups open.',
         quote='&ldquo;dos papeles que se han escapado de [Inglaterra] refieren que salieron de alli en compa&ntilde;ia de Manuel de Andrada, [portugu&eacute;s]&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='conley1652', label='Cowley&rsquo;s hand 1652&ndash;53', year='1652&ndash;53', y=1652.99, place='Paris &rarr; Holland', st='stuck', stt='too short, no key',
         title='&ldquo;Mr. Conleys Hand&rdquo;: two royalist letters in Abraham Cowley&rsquo;s hand, Paris 1652&ndash;53 &mdash; clear text read, code groups open',
         blurb='DECODE R7768&ndash;R7769, catalogued under an author &ldquo;Mr. Conleys Hand&rdquo;, are a fair copy of two letters from the Queen&rsquo;s court at Paris to a royalist in Holland; the docket reads &ldquo;mr Cowleys Hand&rdquo;, the poet who ciphered for Jermyn and Henrietta Maria. The letters are clear English; the cipher is 23 numbers in five runs hiding a few names and a place. Too few to break without a key; the Hyde&ndash;Barwick key does not fit, and the letters are not in Cowley&rsquo;s printed correspondence.',
         quote='&ldquo;the person that came lately from 248:88:46:47:96:52:7:57&rdquo; &mdash; perhaps Scotland',
         rights='British Library, via DECODE'),
    dict(slug='bordeaux1653', label='Bordeaux 1653', year='1653', y=1653, place='London &rarr; Paris', st='solved', stt='read',
         title='Bordeaux to Brienne, London, 30 May 1653 &mdash; read with the English key sheet, once the transcription was right',
         blurb='Thurloe&rsquo;s intercept of the French envoy&rsquo;s despatch, BL Add MS 4200 f. 88: 810 tokens of a Brienne-office cipher whose syllables run alphabetically through three marked series. A solver built on that design read its controls but not the letter. The Deciphering Branch&rsquo;s own sheet for &ldquo;Mr. Bordeaux&rdquo;, Add MS 32263 f. 1 (DECODE R7537), is the key; checked against the page images, the transcription had merged two signs (ꝺ = u, ∂ = n), dropped tokens and lost marks. The Council heard the deputies of rebel Bordeaux before Cromwell gave the King&rsquo;s envoy his audience, and Brienne is told to hold back French mediation.',
         quote='&ldquo;l&rsquo;audiance que j&rsquo;avois demand&eacute;e au General ne me fut donn&eacute;e qu&rsquo;apr&egrave;s la leur&rdquo;',
         rights='Manuscripts: British Library (not reproduced)'),
    dict(slug='hyde', label='Hyde', year='1659&ndash;60', y=1659, place='Brussels', st='found', stt='explained',
         title='Hyde&rsquo;s ciphered superscriptions &mdash; not a cipher at all',
         blurb='The four &ldquo;undeciphered addresses&rdquo; on Hyde&rsquo;s letters to Barwick decode to nothing under the full Hyde&ndash;Barwick key printed in 1721, because, as the 1724 editor states, they were numbers &ldquo;signifying nothing &hellip; only to puzzle the Enemy&rdquo;.',
         quote='&ldquo;some Persons &hellip; have wondered what was the meaning of them&rdquo; &mdash; Life of Barwick, 1724'),
    dict(slug='sessa1593', label='Miranda, Sessa, Ibarra 1593', year='1593', y=1593.2, place='Naples, Rome, Paris', st='partial', stt='key found, all four read in part',
         author='Arya Sanketbhai Patel',
         title='Spanish despatches of 1593 &mdash; the office&rsquo;s own key, with the nomenclature, found in another volume',
         blurb='Four Spanish despatches catalogued as undeciphered and cited only by piece number: Miranda to Feria, Sessa to Ibarra, Sessa to Philip&nbsp;II, and Ibarra from Paris. The BnF d&eacute;pouillement gives their folios and the leaves were found on the images (ff. 98, 162, 108, 145). They are in two ciphers, and Tomokiyo had reconstructed a key for each &mdash; published, like the Maisse keys, as images a text dump drops. But his table has only the syllables. The catalogue said to verify with DECODE, and DECODE&rsquo;s only two hits for these correspondents are not letters but <em>keys</em>, both pointing into the Nevers cipher book fr. 3995. Folio 97 there is the Spanish office&rsquo;s own key, complete with the nomenclature, and it confirms Tomokiyo&rsquo;s syllable table against the original. All four leaves now decode: Miranda to Feria under cover of an errand and at the expense of the purse; Sessa to Ibarra on the testimonies raised against everyone and on those who live in Rome; Sessa to Philip&nbsp;II, where the decode agrees with the 1593 decipherer&rsquo;s own interlinear gloss; and Ibarra from Paris in a second cipher, the Feria&ndash;Mansfeld key.',
         quote='&ldquo;con este achaque, que siendo confidente &hellip; a costa de la bolsa&rdquo; &middot; Miranda to Feria, Naples, 25 February 1593',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='zeschau1841', label='Zeschau 1841&ndash;43', year='1841&ndash;1843', y=1841.5, place='Dresden &rarr; St Petersburg', st='stuck', stt='key not found',
         title='Zeschau to Seebach, 1841&ndash;1843 &mdash; a two-digit syllabary, not read',
         blurb='Four despatches of the Saxon foreign minister to his minister resident in St Petersburg (HStAD 10731 Nr. 12, DECODE R5005&ndash;R5008). The 1841 despatch was transcribed in full, 3,969 unseparated digits. The rubbed-out pencil decipherment still shows <em>la pre m i er e</em> over 11 70 82 34 29 40, so the table is letters and syllables in pairs. No key survives on DECODE, and homophonic and syllabic solvers checked on a control produce no French.',
         quote='&ldquo;la pre m i er e&rdquo; over 11 70 82 34 29 40',
         rights='Hauptstaatsarchiv Dresden, via DECODE'),
    dict(slug='soglia1848', label='Soglia 1848', year='1848', y=1848, place='Rome &rarr; Innsbruck', st='solved', stt='read',
         title='Cardinal Soglia to the nuncio Viale Prel&agrave; &mdash; a nomenclator with an alphabetical code',
         blurb='Rome, 15 June 1848: a ciphered dispatch to the nuncio at Innsbruck, intercepted at Turin and printed by Mazzini&rsquo;s <em>L&rsquo;Italia del Popolo</em> with a prize for its reader, posted on Cipherbrain in 2014 as unsolved. 5 is the word break, pairs of the other eight digits are letters and syllables, 8XXX is a one-part code in alphabetical order; a nomenclator annealer, checked first on a synthetic control, gave the first words. A counter-order: stay with the Emperor, do not ask for your passports. The nuncio had left Innsbruck the day before. Eleven code groups stay open.',
         quote='&ldquo;per nuove sopraggiunte circostanze Le partecipo [&hellip;] del (Padre) che Ella rimanga in Inspruck presso l&rsquo;(Imperatore)&rdquo;',
         rights='Broadsheet scan: Tony Gaffney, via Klaus Schmeh, Cipherbrain'),
    dict(slug='hellen1752', label='Hellen 1752–1763', year='1752&ndash;63', y=1752, place='The Hague &rarr; Prussia', st='stuck', stt='unsolved; investigation open',
         title='Hellen to Frederick II &mdash; transcription audited, decipherment sought',
         blurb='Seven intercepted letters and one supporting letter remain unread. The parser now preserves uncertain figures and marks; a repeated passage was confirmed on the manuscript. Fagel inventory 5206 lists digitized decipherments from 1752–1753, but no matching text has yet been retrieved.',
         quote='No verified plaintext; a concrete archival lead for 1752.',
         rights='Source manuscripts: KHA, Prins Willem V, inventory 196; no manuscript images reproduced'),
    dict(slug='deswart1782', label='De Swart 1782', year='1782', y=1782.2, place='St Petersburg &rarr; The Hague', st='solved', stt='read',
         title='De Swart to Van Bleiswijk, 8 March 1782 &mdash; the unidentified codebook was the Croiset key of 1765',
         blurb='DECODE lists two ciphered letters of the Dutch resident at St Petersburg as non-decrypted, with a codebook that &ldquo;could not be identified&rdquo;. The despatch of 1782 is in the Croiset codebook of 1765 for the Russia legation, whose key survives as DECODE R1038. Parsed with the digit marks that make separate groups, the key and 34 values recovered from context read 93.8% of its 1,719 groups. It reports the French and Spanish answers to the Austro-Russian mediation, Catherine II&rsquo;s Greek project for Grand Duke Constantine, and Prussia&rsquo;s accession to the Armed Neutrality. The second part of the 1787 letter reads with the same key; its first 1,928 groups are in another codebook that is missing.',
         quote='&ldquo;of nu den Keizer in dezen met haar oprecht handelt&rdquo;',
         rights='Manuscript image: Nationaal Archief, The Hague, via DECODE R1036'),
    dict(slug='rechteren1785', label='Rechteren 1785', year='1785', y=1785.75, place='St Petersburg &rarr; The Hague', st='found', stt='read at the time',
         title='Rechteren to the Griffier, St Petersburg 1785 &mdash; read at the time',
         blurb='DECODE R1039, catalogued as an undeciphered letter of the new Dutch envoy to Catherine II, dated 4 October 1785. Its first two images are the Griffie&rsquo;s decipherment, headed &ldquo;Ont cyfferde Missive&rdquo; and keyed to the 424 cipher groups by margin numbers. Rechteren withheld his letter to Grand Duke Paul on De Swart&rsquo;s advice and, sure that all his post was opened, asked for couriers and replies in cipher. The pair is the best known-plaintext sample of the code still missing for De Swart&rsquo;s 1787 letter.',
         quote='&ldquo;De zekere overtuiging, waarin ik ben, dat alle mijne Brieven geopend worden&rdquo;',
         rights='Manuscript: Nationaal Archief, The Hague, via DECODE'),
    dict(slug='vanreede1787', label='Van Reede 1787', year='1787&ndash;93', y=1787.9, place='Berlin &rarr; The Hague', st='solved', stt='read',
         title='Van Reede from Berlin, 1787&ndash;1793 &mdash; the Grand Chiffre despatches read, the 1793 code open',
         blurb='DECODE lists three ciphered letters of the Dutch envoy at Berlin as non-decrypted. The French despatches of December 1787 and March 1788 are in William V&rsquo;s Grand Chiffre of 1782 (DECODE R1024), confirmed on a control letter with known plaintext; the digits the DECODE transcription left under one catch-all sign were resolved with a French language model. They report the King of Prussia&rsquo;s refusal to guarantee the Dutch possessions overseas in the 1788 alliance, and Russian and Austrian moves in the Turkish war. The 1793 letter to the Secret Committee is in another, marked three-digit code and stays unread.',
         quote='&ldquo;le Roi a dit qu&rsquo;il ne pouvoit pas garantir nos possessions d&rsquo;outre-mer&rdquo;',
         rights='Manuscript image: Nationaal Archief, The Hague, via DECODE R1026'),
    dict(slug='vanreede1792', label='Van Reede 1792', year='1792', y=1792.1, place='Berlin &rarr; The Hague', st='solved', stt='read',
         title='Van Reede to William V, 1792 &mdash; the lemon-juice letter',
         blurb='A one-page letter in William V&rsquo;s Grand Chiffre, catalogued on DECODE as partially decrypted with its contents unknown. Read in full with the 1782 key R1024. It is a cover note: the Prince&rsquo;s secretary Larrey is told that the enclosure&rsquo;s four blank half-pages carry writing in lemon juice, and that the figures after the message are nulls.',
         quote='&ldquo;il y a du citron sur les quatre demi-pages blanches de l&rsquo;incluse&rdquo;',
         rights='Manuscript image: Koninklijk Huisarchief, The Hague, via DECODE R1057'),
    dict(slug='r1944', label='Bourdeaux 1801', year='1801', y=1801.1, place='Berlin &rarr; The Hague', st='found', stt='clear copy found',
         title='Bourdeaux to Van der Goes, 31 January 1801 &mdash; the clear copy, misfiled under another record',
         blurb='DECODE lists R1944, the Batavian charg&eacute; Bourdeaux&rsquo;s ciphered dispatch no. 16 from Berlin, as non-decrypted. Its clear copy is the third image of the next record, R1946, on the following folio (294, 295). It reports that the Danish diplomat Rosenkrantz, sent away from Petersburg, blamed a servant who copied his cipher, while the Prussian envoy Lusi said the desk holding it had been forced. The code groups are not yet aligned to the text.',
         quote='&ldquo;dat het bureau, waar in zyn Cyffer was, is geforceerd geworden&rdquo;',
         rights='Manuscript images: Nationaal Archief, The Hague, via DECODE R1944 and R1946'),
    dict(slug='r1942', label='Hogendorp 1803', year='1803', y=1803, place='St Petersburg &rarr; The Hague', st='found', stt='subject identified',
         title='Hogendorp to Van der Goes, 5 July 1803 &mdash; the Van Suchtelen channel identified from print',
         blurb='DECODE R1942 is Hogendorp&rsquo;s ciphered dispatch no. 12, listed as non-decrypted with its subject unknown. Sillem&rsquo;s 1890 biography says that, after Vorontsov rebuffed him, Hogendorp sought to reach Alexander I through the Dutch-born Russian general Van Suchtelen; its footnote names the source as the ciphered dispatch of the same day, no. 12. The matching 1803 codebook is DECODE R1035. The subject is secure, but the 286 groups have not yet been aligned to an exact plaintext.',
         quote='&ldquo;Hogendorp vond zijne houding althans zo wonderlijk dat hij naar andere kanalen zocht&rdquo;',
         rights='Manuscript image: Nationaal Archief, The Hague, via DECODE R1942'),
    dict(slug='r1892', label='Orange prince 1795', year='c. 1795', y=1795.5, place='Germany &rarr; the Orange troops', st='solved', stt='read',
         title='A son of William V on the &eacute;migr&eacute; rassemblement, c. 1795 &mdash; the &ldquo;non-decrypted&rdquo; R1892 is a 6&times;6 digit square',
         blurb='DECODE R1892, two pages in the papers of Prince William V catalogued as an unsolved letter from an unknown writer. Every letter is a pair of digits 1&ndash;6 written one above the other; the square was recovered ciphertext-only from the Dutch postscript and read the French page unchanged. A son of the Stadholder tells the officer of the Dutch troops in Germany to accept it if General Dundas stops their pay or orders them to embark, and to explain their footing in British service. About thirty graphic word signs remain unread.',
         quote='&ldquo;il faudroit y souscrire et vous borner uniquement &agrave; t&acirc;cher d&rsquo;obtenir &hellip; une gratification&rdquo;',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='r2242', label='Prince Frederick 1795', year='1795', y=1795.35, place='London &rarr; the Hereditary Prince', st='solved', stt='read',
         title='Prince Frederick of Orange to his brother, 7 May 1795 &mdash; the &ldquo;non-decrypted&rdquo; R2242 reads with the R1892 key',
         blurb='DECODE R2242, four pages in the papers of King William I catalogued as an unread numerical substitution. The digit pairs are the square recovered for R1892, and it reads them unchanged; page 1 carries its own clear Dutch under the cipher, which confirms the key and a dozen word signs. The cipher pages report the scattered &eacute;migr&eacute; troops, the Basel ratification and envoys sent to Paris. About twenty word signs remain unread.',
         quote='&ldquo;dan zoo zij geen Robespierismus durven te introduceeren&rdquo;',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='hereditary1796', label='Hereditary Prince 1796', year='1796', y=1796.2, place='Berlin &rarr; Prince Frederik', st='solved', stt='read',
         title='The Hereditary Prince from Berlin, 12 March 1796 &mdash; the &ldquo;non-decrypted&rdquo; R2239 reads with a word list rebuilt from its sibling',
         blurb='DECODE R2239, three pages of numbers in the papers of William V, catalogued as an unsolved book cipher. Each group takes a whole entry of a numbered word list, chosen letters of it, or the entry cut at the front or back; the sibling R2237 carries its own contemporary decipherment, and aligning the two rebuilt the list. It read 70% of the letter; the body then proved to be printed by Colenbrander in 1906, and with that crib the unprinted opening was read: the conference between Haugwitz and Lord Elgin on a Prussian d&eacute;marche in Paris for the Orange restoration.',
         quote='&ldquo;le comte Haugwitz me dit avant-hier au bal du Roi qu&rsquo;il viendroit un de ces jours chez moi pour me parler sur cet objet&rdquo;',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='r2234', label='Basle to William V 1796', year='1796', y=1796.6, place='Basle &rarr; William V', st='solved', stt='read',
         title='An Orangist at Basle to William V, 17 August 1796 &mdash; the &ldquo;non-decrypted&rdquo; R2234 reads with its own key sheet',
         blurb='DECODE R2234, one page in the papers of Prince William V catalogued as an unread homophonic letter. The key sheet R2235 in the same file gives five alphabets, D, G, L, N and R; the letter changes alphabet on every line, starting from the capital that opens each section. Read that way, a correspondent at Basle asks for money and a decision on his lodging and reports on Salm&rsquo;s hussars, Barth&eacute;lemy, Degelmann and the French armies of Italy and the Rhine.',
         quote='&ldquo;la jonction de l&rsquo;arm&eacute;e d&rsquo;Italie &agrave; celle du Rhin par le Tyrol; cela ne ressemble pas &agrave; la paix&rdquo;',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='r2232', label='Wolff to Wilhelmina 1801', year='1801', y=1801.6, place='The Hague &rarr; the Princess of Orange', st='solved', stt='read',
         title='Wolff to Princess Wilhelmina, 25 July 1801 &mdash; the &ldquo;non-decrypted&rdquo; R2232 reads with the key he sent after it',
         blurb='DECODE R2232, three pages from an unidentified Wolff at The Hague to the exiled Princess of Orange, listed as unread. The next record, R2233, is his covering letter of 8 September 1801 with the key: 45 rows of four consecutive values, a number with a superscript picking one. Applied unchanged it reads the whole letter: a 1798 plan for a landing at Le Havre and in Holland, an arrest on 14 September 1795 and 39 months in prison, and a plea for British half-pay.',
         quote='&ldquo;je n&rsquo;aurais point soupir&eacute; 39 mois et 5 jours dans la prison&rdquo;',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
    dict(slug='dedem1788', label='Van Dedem 1788&ndash;99', year='1788&ndash;1799', y=1788.9, place='Constantinople &rarr; The Hague', st='stuck', stt='key not found',
         title='Van Dedem at Constantinople, 1788&ndash;1799',
         blurb='Four ciphered despatches of the Dutch ambassador to the Porte. The 1788 letter was read at the time: its decipherment is filed as DECODE R2121. The 1789 and 1793 letters use the same heavily homophonic word code, which three deciphered siblings are not enough to rebuild, and the 1799 despatch uses a different marked system.',
         quote='al de inkomsten van de Provincie Morea, Negropont, Salonique &hellip;', rights='Nationaal Archief, via DECODE'),
    dict(slug='desmarets1710', label='Desmarets 1710', year='1710', y=1710.0, place='Marly', st='stuck', stt='key not found',
         title='Desmarets to an unnamed correspondent, 4 June 1710 &mdash; clear prose between the lines, the code unread',
         blurb='DECODE R10198: a letter of the Controller General of Finances on the Geertruidenberg talks, with French prose alternating with lines of a numerical code and 22 lines of code alone. Four alignment models show the French is not the decipherment of the figures. The 471-group code has no key on DECODE or in print.',
         quote='on veut la paix, ou la veut seure, mais on veut encore menager l&rsquo;honneur de son gouvernement',
         rights='Via DECODE R10198; not in the public domain'),
    dict(slug='spaen1808', label='Van Spaen 1808', year='1808', y=1808.0, place='D&uuml;sseldorf &rarr; The Hague', st='stuck', stt='key not found',
         title='Van Spaen to Van der Goes, 14&ndash;15 January 1808 &mdash; transcribed, no key survives online',
         blurb='DECODE R1941 holds a letter and its annex in a plain numerical code reaching at least 1339: 303 groups, 222 distinct. The archive inventory places it with the commissioners for the districts ceded around Zevenaar, writing from D&uuml;sseldorf in the Grand Duchy of Berg. No key is on DECODE, Croiset&rsquo;s 1803 book does not fit, and Colenbrander does not print it.',
         quote='&ldquo;602 441 373&rdquo;, three times: probably a name or title',
         rights='Nationaal Archief, via DECODE'),
    dict(slug='castelcicala1816', label='Castelcicala 1816&ndash;23', year='1816&ndash;1823', y=1819.5, place='London, Paris &rarr; Naples', st='solved', stt='read',
         title='Castelcicala to the Marchese di Circello and to Medici, 1816&ndash;1823 &mdash; the code rebuilt from four glossed letters',
         blurb='Twenty-four ciphered despatches of the Neapolitan ambassador Fabrizio Ruffo, principe di Castelcicala, in the Naples archive (DECODE R9553&ndash;R9589), all in one syllabic, homophonic code of about 2,450 groups. &ldquo;Marchese di Ciscello&rdquo; is the recipient, Circello, misread. Contemporary decipherments on four letters of 1816 and 1823 gave 162 values and 45% of the groups; no letter reads through yet.',
         quote='&ldquo;La Francia desidera il Cardinale Castiglione per Papa&rdquo; (R9571, 8 September 1823)',
         rights='Manuscript: Archivio di Stato di Napoli, via DECODE'),
    dict(slug='roell1809', label='Roell to Van Dedem 1809', year='1809', y=1809.1, place='Amsterdam &rarr; Constantinople', st='stuck', stt='key not found',
         title='Roell to Van Dedem, 9 February 1809 &mdash; transcribed, no key survives online',
         blurb='Two unsigned code letters in the papers of the Dutch legation at Constantinople, DECODE R1469 and R1470, attributed to the foreign minister W. F. R&ouml;ell. The 13 pages hold 2,585 groups of a heavily homophonic code reaching about 3,300, with no decipherment. The code is not the 1788&ndash;93 Dedem code, nor the Spaen 1808 or Fagel 1804 codes, and no key is on DECODE or in R&ouml;ell&rsquo;s papers.',
         quote='&ldquo;1390 &middot; 460 &middot; 1576 &middot; 804&rdquo;: the commonest groups, none above one per cent',
         rights='Manuscript: Nationaal Archief, The Hague, via DECODE'),
    dict(slug='fagel1804', label='Fagel 1804', year='1804', y=1804.5, place='The Hague &rarr; William V in exile', st='stuck', stt='key not found',
         title='Robert Fagel to William V, 18 June 1804 &mdash; transcribed, every online key ruled out',
         blurb='DECODE R2238 carries 128 groups of a French syllabic nomenclator reaching at least 2510, in a letter on the 1804 settlement of the House of Orange&rsquo;s claims. Euler&rsquo;s Grand Chiffre (direct, with its additive table and under 5,000 renumberings), all KHA and Fagel family keys in DECODE, and the British Library and Uppsala French codes were tested and ruled out. The key is most likely in the undigitised KHA packet A31-902.',
         quote='&ldquo;j&rsquo;attends la r&eacute;ponse pour partir&rdquo;',
         rights='Manuscript image: Koninklijk Huisarchief, The Hague, via DECODE R2238'),
    dict(slug='armstrong', label='Armstrong', year='1808', y=1808, place='United States', st='solved', stt='solved',
         title='Armstrong to Madison &mdash; the coded postscript',
         blurb='Forty-nine groups of the 1,600-element &ldquo;THE = 972&rdquo; diplomatic code, read in full after reconstructing 580 groups from the State Department&rsquo;s own pencil decodes on NARA microfilm M34 roll 13.',
         quote='&ldquo;Russel ought to be the consul: he is an American by birth &hellip; Next to him in fitness is O&rsquo;Mealy, but he is, like Warden, an Irishman.&rdquo;'),
    dict(slug='legation', label='Erving &amp; Adams', year='1807&ndash;12', y=1810, place='Madrid, St Petersburg &rarr; Washington', st='partial', stt='gaps read',
         title='Erving at Madrid (1807) and Adams at St Petersburg (1812) &mdash; two legation codes',
         blurb='Two American diplomatic-code results from the State Department&rsquo;s microfilmed despatch books. Erving&rsquo;s private letter of 24 March 1807, printed from Madison&rsquo;s own decode with the key &ldquo;not found&rdquo;: every hole closes from both received copies and Pinckney&rsquo;s decoded despatches, and the holes turn out to be Madison&rsquo;s slips. John Quincy Adams&rsquo;s despatches are not in Armstrong&rsquo;s code; his own (the = 1385) is rebuilt from the clerk&rsquo;s decodes on NARA M35 reel 3, and the nine lines of No. 88 that Ford printed as not decyphered read, 124 of 134 groups: Count Rumyantsev&rsquo;s strokes at Wilna.',
         quote='&ldquo;which was undoubtedly an apo[plec]tic &hellip; s-tr-[oke]. Since then he has had a [second] and a more [seve]re one.&rdquo;',
         rights='Microfilm images: National Archives and Records Administration'),
    dict(slug='debosnys', label='Debosnys', year='1883', y=1883, place='Elizabethtown, NY', st='stuck', stt='too short to break',
         title='The Debosnys cryptograms &mdash; a French syllabary, and why it stops there',
         blurb='A convicted wife-killer&rsquo;s invented script, about 1,200 glyphs, unread since he was hanged. Three passages transcribed. The cipher poem is twenty lines of rhyming couplets, and line length and rhyme both make it a syllabary too short for any crib-free attack.',
         quote='final glyph matches in 9 of 10 couplets &middot; 0 of 9 across &middot; planted 1,000-glyph syllabary: 0% recovered'),
    dict(slug='sunyatsen', label='Sun Yat-sen', year='1916', y=1916, place='Swatow &rarr; Tokyo', st='solved', stt='solved',
         title='The Swatow telegram to Sun Yat-sen &mdash; a systematic code condenser',
         blurb='Twenty consonants, five vowels, ten-letter words: a code condenser over the standard Chinese telegraph code. The family of systematic tables is small enough to brute-force, and one key reads 41 characters: Mo Qingyu&rsquo;s independence at Chaozhou and Sun&rsquo;s men ordered out of the Swatow garrison headquarters, 3 April 1916.',
         quote='潮城由莫擎宇獨立。我軍亦光復汕頭。後莫率大隊來，令我退出鎮守府&hellip;'),
    dict(slug='sunintercepts', label='Sun Yat-sen wires', year='1916&ndash;17', y=1916.3, place='Shanghai &harr; Tokyo', st='solved', stt='read',
         title='Sun Yat-sen&rsquo;s circle on the wire, 1916&ndash;17 &mdash; the intercepts the Foreign Ministry could not read',
         blurb='The Ministry of Communications copied every telegram to or from Sun Yat-sen&rsquo;s people for the Japanese Foreign Ministry, which filed them unread. Fifty-six condenser telegrams of March&ndash;May 1916 read under five more keys of the Swatow telegram&rsquo;s family, each accepted only when it read telegrams it was not fitted to, with rhyme-day dates as an independent check. They cover the monarchy cancelled, money wired via Taiwan, the price of a Wuhan rising, Chen Qimei&rsquo;s murder, and the Foreign Ministry&rsquo;s own advice relayed back to Sun. Also a Hankow +111 telegram and Sun &harr; Dai Jitao, March 1917.',
         quote='克強言外務省意先生宜緩赴青島。 &middot; Tokyo to Shanghai, 26 May 1916',
         rights='Telegram images: JACAR'),
    dict(slug='huangxing', label='Huang Xing', year='1916', y=1916.5, place='China / Japan', st='solved', stt='scheme found',
         title='Huang Xing to Lin Hu and Li Genyuan &mdash; a kana condenser',
         blurb='Listed as &ldquo;solved but specific scheme unknown&rdquo;: the Japanese Foreign Ministry filed a decode nobody could read, and an encipherment nobody could name. Both recovered, and then corrected from the frames: three kana carry one character deterministically from a private code, a superfluous kana had hidden the repeats, and the vowel is not free.',
         quote='護國軍能速入湘贛甚好。章行嚴何日東渡？速令出發，並望預電。興　徑'),
    dict(slug='adfgvx', label='ADFGVX', year='1918', y=1918, place='Eastern Front', st='partial', stt='9 of 22 read',
         title='The ADFGVX residue of 1918 &mdash; twenty-two mutilated messages against known keys',
         blurb='Schmeh&rsquo;s Top 50 lists twenty-two German radio messages of November 1918 as unsolved, but the keys were published in 2017 and the messages are garbled in transmission. The comment thread that read nine of them is tabulated for the first time, Lasry&rsquo;s unpublished CHI key is rebuilt, his readers&rsquo; method re-derives the solved pages blind, and the ten never read resist every key and a key-free attack that fails its own control.',
         quote='9 solved &middot; 3 partial &middot; 10 open &middot; best open score &minus;6.9 against &minus;4.4 to &minus;6.0 solved'),
    dict(slug='goldbar', label='Gold bars', year='1933', y=1933, place='Shanghai', st='found', stt='no message',
         title='The Chinese gold bar cryptograms &mdash; ten of everything',
         blurb='Sixteen strings on seven bars said to certify $300,000,000, unread for ninety years. They contain almost exactly ten of every letter of the alphabet: chi-squared 1.25 against uniform where chance predicts 25. No cipher can flatten a distribution past what randomness allows, so there is nothing to read.',
         quote='MQOLCSJTLGAJOKBSSBOMUPCE &middot; ZUQUPNZN &middot; FEWGDRHDDEEUMFFTEEMJXZR',
         rights='Bar photographs from the IACR'),
    dict(slug='roosevelt', label='Roosevelt', year='1935', y=1935, place='Washington', st='found', stt='no message',
         title='The Roosevelt cryptogram &mdash; the numbers 1 to 52, written once each',
         blurb='Three lines of digits above a threat to the President, reproduced by Friedman and unread since 1935. Read at glyph level they are a permutation of 1 to 52 with zero padding; the permutation drifts upward, runs 39 40 41 42 and falls into sixteen rising chains where a shuffle gives 26, the marks of a hand-written list. The ordered-key cipher readings that can be tested fail while matched controls are recovered.',
         quote='16 rising chains against 26 &middot; rank correlation +0.39 &middot; every value once',
         rights='Figure from The Friedman Legacy, NSA 1992, via the Internet Archive'),
    dict(slug='ormanetto1573', label='Ormanetto 1573', year='1573', y=1573.4, place='Madrid &rarr; Rome', st='stuck', stt='key not found',
         title='Philip II&rsquo;s letter to the nuncio Ormanetto, 1573 &mdash; two cipher passages not read',
         blurb='Catalogued as Ormanetto to the Secretariat, 7 January 1573, DECODE R116 is the nuncio&rsquo;s copy for the Cardinal of Como of a letter from Philip II: the King&rsquo;s recovery, jurisdiction, the Turkish slaves, the bishop of Li&egrave;ge in clear, and two passages in dotted and marked figures. Lasry&rsquo;s 1568 Spain key and four keys printed by Meister do not read them, and annealers that read matched controls find nothing.',
         quote='quedo bueno y levantado &middot; 1,098 digits &middot; 5 keys ruled out',
         rights='Images: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='ormanetto1576', label='Ormanetto 1576', year='1576&ndash;77', y=1576.7, place='Madrid &rarr; Rome', st='stuck', stt='no key, not a crib',
         title='Ormanetto and Clementino, Spain nunciature, 1576&ndash;77 &mdash; one record not a cipher, the other not read',
         blurb='Two DECODE records from ASV Segr. Stato Spagna 10, catalogued as nunciature ciphers with a decipherment on the leaf. R117 is a clear Spanish memorial on the Pamplona vacancy whose only figures are Roman-numeral ducat sums. R118 is six lines of figures, 389 digits. The Italian note beneath them, on the nuncio&rsquo;s talk with Antonio P&eacute;rez, was tested as their plaintext and fits no better than shuffled controls. No key for the nunciature is known.',
         quote='crib 43 tokens for 60 letters &middot; shuffled 47&ndash;51 &middot; no fit',
         rights='Images: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='bl32305', label='Paris 1719 / Carr&eacute;', year='1719&ndash;45', y=1719, place='Paris, London', st='stuck', stt='two-part codes, too short',
         title='Paris 1719 and Carr&eacute; 1742&ndash;45 code letters &mdash; two-part codes, not read',
         blurb='Six DECODE records from BL Add MS 32305, catalogued as one Paris correspondence, are a codebreaker&rsquo;s working file. Two were deciphered at the time. The Paris letters of February 1719 carry about a dozen contemporary glosses; they are not alphabetical, so the code is two-part, and 354 groups with 191 distinct values cannot be broken from the ciphertext. The letters to Mr Carr&eacute; in Pall Mall, 1742&ndash;45, have no gloss at all; all three were transcribed (1,323 groups, 381 distinct) and tested: not a letter cipher, not a one-part code, so a two-part code of about 800 entries.',
         quote='36 re &middot; 95 le &middot; 184 que &middot; 243 vous &middot; 347 a: not in alphabetical order',
         rights='Images: British Library, via DECODE'),
    dict(slug='orpo1942', label='Police radiograms', year='1942', y=1942, place='Eastern Front', st='stuck', stt='double pass not broken',
         title='German police double-box radiograms, 1942 &mdash; one key, not broken',
         blurb='Six Ordnungspolizei radio messages from the Eastern Front in the Army&rsquo;s double-box cipher, published by Frode Weierud and posted by Klaus Schmeh in 2020 as unsolved. One has a Bletchley decrypt: sixteen police killed on the Bobruisk&ndash;Mogilev road and the village of Borki razed. The five of 27 February 1942 turn out to share one key, 970 letters. Every ciphertext-only attack fails, on the real text and on a synthetic control of the same size, because the second pass through the same boxes leaves no gradient. A known-plaintext solver needs about 80 pairs, and the Borki decrypt does not align with its ciphertext.',
         quote='seven parts, four discriminators, one key &middot; synthetic 970-letter controls unbroken too &middot; known plaintext solves from ~80 pairs',
         rights='Images: NARA, RG 457 (HCC), via Weierud 2020 and Hanyok 2005'),
    dict(slug='copenhagen', label='Copenhagen', year='c.1950s', y=1955, place='Copenhagen', st='stuck', stt='not a simple substitution',
         title='The Copenhagen cryptogram &mdash; not a simple substitution of any language tested',
         blurb='Three lines found behind an 1835 portrait of a Danish general, 107 characters, unsolved at the American Cryptogram Association since the 1950s. Transcribed twice, attacked in ten languages under six reading conventions; the same solver recovers matched controls at 96 to 100 percent and the note never comes close.',
         quote='best &minus;2.7 nats per letter in any language &middot; controls solve at &minus;1.4 to &minus;2.1'),
    dict(slug='scorpion', label='Scorpion', year='1991', y=1991, place='United States', st='stuck', stt='below unicity distance',
         title='The Scorpion letters &mdash; two ciphers below the unicity distance',
         blurb='Two Zodiac-style cryptograms sent to John Walsh in 1991, 70 and 180 symbols with 53 and 145 distinct. Both carry more key than the English text has redundancy, so fluent false solutions are guaranteed; matched controls produce them at 3 to 13 percent accuracy, and a claimed 2018 solution is tested against the same rule.',
         quote='S5: every repeat at a multiple of 16 &middot; key 682 bits against 576 of redundancy'),
    dict(slug='voynich', label='Voynich', year='c.1420', y=1420, place='Beinecke MS 408', st='stuck', stt='adjudicated, not read',
         title='The Voynich manuscript &mdash; hoax, cipher or language, adjudicated',
         blurb='Six computational tests on the transliteration against eleven languages and implemented hoax generators, each re-run adversarially, and five literature sweeps. A plain or simply enciphered European language is excluded on transliteration-robust entropy; a verbose encoding and a structured meaningless text are left roughly even, with the tests that would separate them.',
         quote='h2 2.2&ndash;2.9 bits against a 3.3 floor &middot; slot grammar 1.7&ndash;2.3&times; more rigid than any language'),
    dict(slug='famous', label='The famous ones', year='survey', y=9999, place='Survey', st='partial', stt='the famous ones',
         title='Why the famous ciphers resist',
         blurb='Kryptos, Voynich, Dorabella, Beale, Linear A, Phaistos, the pigeon message. Sorted by the actual reason each has held out: undeciphered writing systems, one that is information-theoretically secure, several too short for any answer to be provable, and at least two that were probably never enciphered.',
         quote='Fame is a poor guide to tractability.'),
    # Unpublished 18 Sept 2026; the page is kept in unpublished/solved.html. To republish, move it back to
    # docs/ and uncomment this entry.
    # dict(slug='solved', label='What has been read', year='catalogue', y=9998, place='Catalogue', st='partial', stt='solved catalogue',
    #      title='What has been read, and how',
    #      blurb='Thirty-four ciphers solved, read or partly read, from an unaddressed Spanish cipher of January 1497 to Sun Yat-sen&rsquo;s telegrams of 1917, each with the thing that actually broke it, and an account of what a frontier AI did well on the way and where it stopped.',
    #      quote='Eight to a solver, seventeen to a printed or archived sibling, five to looking at the leaf, two verifications.'),
]
IMAGES = {'harley7001': ('harley7001_lead.jpg', 'Harley MS 7001 f. 149r: the cipher continued from f. 148v, the one side, I am of opinion they have not enough against him to confiscate his fortune', 'British Library, via DECODE R7766'), 'r8356': ('r8356_lead.jpg', 'BL Harley MS 260 f. 112v: Walsingham to Burghley, June 1571, cipher run in line 1', 'British Library, via DECODE R8356'), 'swieten1757': ('swieten1757_lead.jpg', 'ARA Brussels, SEG 1236 f. 141: the ciphered sentence on Hanau and, below it, the same sentence in clear', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R955'), 'r8358': None, 'walsingham1572': None, 'r8361': ('r8361_lead.jpg', 'Harley MS 260 f. 367r: written to Rome [9], then The partie 776 + w5 &Dagger; 6 3 &cap; 6 remaineth here in London', 'British Library, via DECODE R8361'), 'harley286': ('harley286_lead.jpg', 'BL Harley MS 286 f. 61: D&rsquo;Ewes&rsquo;s cipher slip, 1635&ndash;36, one line to each of his son&rsquo;s convulsion fits', 'British Library, via DECODE R7759'), 'jantini1517': ('jantini1517_lead.jpg', 'ASMo Ungheria b. 4, Fantini no. 5 (R1126) p. 1: the clear opening, per la mandata dil duca Lorezo in Franza, and the first lines of the two-tier signs', 'Archivio di Stato di Modena, via DECODE R1126'), 'gonzaga1590': ('gonzaga1590_lead.jpg', 'BnF fr. 3979 f. 92r: che la morte del Papa, then the figures for sia stata procurata con veleno da Spagnoli', 'Biblioth&egrave;que nationale de France'), 'bizozola1520': ('bizozola1520_lead.jpg', 'BnF fr. 3034 f. 156r: the clear salutation and the first cipher lines, per le mie ultime di Cremona', 'Biblioth&egrave;que nationale de France'), 'marechaux1520': ('marechaux1520_lead.jpg', 'BnF fr. 3081 f. 41v, the head of the second cipher page: &hellip;stien et serenissime seigneur Francois roy de France', 'Biblioth&egrave;que nationale de France, via DECODE R2322'), 'caracciolo1537': ('caracciolo1537_lead.jpg', 'AGS Estado leg. 1184 f. 110v (scan 0409): the clear text ends at the struck words, then the cipher of Cifrario 38 with its superscript vowel digits', 'Archivo General de Simancas, via DECODE R9966'), 'zeschau1841': ('zeschau1841_lead.jpg', 'R5005 image P5: 0064029740671170823429402062&hellip; with the rubbed pencil la pre m i er e above 11 70 82 34 29 40', 'Hauptstaatsarchiv Dresden, via DECODE R5005'), 'desmarets1710': ('desmarets1710_lead.jpg', 'R10198 p. 1, the head: a Marly ce 4 juin 1710, then French prose over dotted figures', 'Via DECODE R10198'), 'ormanetto1573': ('ormanetto1573_lead.jpg', 'R116, f. 303r: the end of the clear copy of Philip II&rsquo;s letter and the first lines of cipher passage A', 'Archivio Apostolico Vaticano, via DECODE R116'), 'colonia1721': ('colonia1721_lead.jpg', 'Arch. Nunz. Colonia 5 f. 26r: headed Brusselles 9 ott.re 1721, nine lines of comma-separated figures', 'Archivio Apostolico Vaticano, via DECODE R24'), 'needham1587': ('needham1587_lead.jpg', 'Harley MS 287 f. 39v: campe nor the towne glossed above its signs, and beneath the bare line whether there was any bridge or not', 'British Library, via DECODE R8479'), 'loeschnen1816': ('loeschnen1816_lead.jpg', 'R2227 opening 9: a worked example, le Roi d&rsquo;Espagne vient de nommer &hellip; M. le Duc de San Carlos written above its code groups', '&Ouml;sterreichisches Staatsarchiv, HHStA, via DECODE R2227'), 'ayala1516': ('ayala1516_lead.jpg', 'AGS Estado leg. 496 fol. 22, image 0002: the first cipher lines, cerca delos oficios que estan vacos en estos reynos', 'Archivo General de Simancas, via DECODE R9954'), 'palm1727': ('palm1727_lead.jpg', 'Add MS 32270 f. 16v: clear German text and a ciphered passage with interlinear glosses', 'British Library, via DECODE R7927'), 'it1583': None, 'eichel1758': ('eichel1758_lead.jpg', 'SP 106/7 image 0020, the Eichel sheet: groups ending in 7 and runs through the 1900s and 2600s&ndash;2800s, the key&rsquo;s null ranges', 'The National Archives, Kew, via DECODE R595'), 'visconti1727': ('visconti1727_lead.jpg', 'Add MS 32270 f. 42, the head of the key table: 1 Walpole, 3 Maest&agrave;, 21 Vienna, 22 Sinzendorff, the syllables from 101, 201 Parlamento', 'British Library, via DECODE R7931'), 'jones1753': ('jones1753_lead.jpg', 'Add MS 32256 f. 235r, foot: the methods of disguise worked on the number 1753', 'British Library, via DECODE R9218'), 'nuncio1566': None, 'sloane3188': ('sloane3188_lead.jpg', 'Sloane MS 3188 f. 109r, the chronology column: longhand years and E.T., Uriel, Reuchlin among shorthand strokes', 'British Library, via DECODE R8506'), 'lopehurtado1523': ('lopehurtado1523_lead.jpg', 'RAH Salazar A-30 f. 130r (R9846), Lope Hurtado to Charles V, 5 February 1524: the clear opening on Beaurain&rsquo;s coming, then the cipher from para lo de con[tribucion]', 'Real Academia de la Historia, via DECODE R9846'), 'sp106r597': ('sp106r597_lead.jpg', 'SP 106/7 f. 33: the worked example in key A, syllables over the groups, Les Adherens du Pretendant se donnent beaucoup de mouvement &agrave; Rome', 'The National Archives, Kew, via DECODE R597'), 'castelcicala1816': ('castelcicala1816_lead.jpg', 'R9566 p. 3, despatch 3874 (Paris, 1 December 1816), with its contemporary interlinear decipherment', 'Archivio di Stato di Napoli, Esteri 2337, via DECODE'), 'stowe166': ('stowe166_lead.jpg', 'Stowe MS 166 f. 50 (R7770): clear English, then six lines of invented signs, to breake of the marriage betwene her and [9]', 'British Library, via DECODE R7770'), 'anne1711': None, 'prussia1702': None, 'champagne1590': ('champagne1590_lead.jpg', 'BnF fr. 3623 f. 36r, the name key bound after Bienvenut&rsquo;s letter of 28 February 1590: 1 Le Roy d&rsquo;Espaigne, 10 Le Pape, 36 Madame de Nemours', 'Biblioth&egrave;que nationale de France'), 'bergamo1585': ('bergamo1585_lead.jpg', 'Francia 18 f. 206r (DECODE R16): the heading 3. di Marzo 1586 and the first lines of figures, hoggi il Duca di Guisa mi ha mandato a dire', 'Archivio Apostolico Vaticano, via DECODE R16'), 'mercoeur1586': ('mercoeur1586_lead.jpg', 'BnF fr. 15564 f. 151, the head of the slip: Tout a est&eacute; [cipher] que je vous ay adverty, then the second cipher run', 'Biblioth&egrave;que nationale de France'), 'dedem1788': ('dedem1788_lead.jpg', 'R2122, 15 January 1789: the opening groups 2504 2604 2704 recur in the other letters', 'Nationaal Archief, via DECODE'), 'conley1652': ('conley1652_lead.jpg', 'Harley MS 7003 f. 314r: the code runs 102:43:97:133:52:180 and 57:102:58:20:30 inside the clear letter of 28 December 1652', 'British Library, via DECODE'), 'rupert1645': ('rupert1645_lead.jpg', 'BL Add MS 18983 f. 14: the King&rsquo;s clear opening, I very much like your opinion, and the first cipher lines', 'British Library, via DECODE R4921'), 'spaen1808': ('spaen1808_lead.jpg', 'R1941, the letter of 14 January 1808: docket, clear salutation and the first rows of figures', 'Nationaal Archief, via DECODE'), 'lucini1767': ('lucini1767_lead.jpg', 'Spagna 304 f. 280: the foot of the letter of 13 October 1767, where the clear text breaks into figures after &ldquo;tenda ad estinguere i&rdquo;', 'Archivio Apostolico Vaticano, via DECODE R120'), 'smith1562': ('smith1562_lead.jpg', 'Add MS 4136 f. 166: Forbes&rsquo;s copy of Smith&rsquo;s letter from Arles, 24 November 1564, the Cardinal of Lorraine and Cond&eacute; conferring at Soissons', 'British Library, Add MS 4136, via DECODE R9253'), 'malvezzi1548': None, 'percy1559': ('percy1559_lead.jpg', 'BL Add MS 4136 f. 172: the Forbes tracing of the four cipher passages of Percy&rsquo;s letter, Norham, 23 July 1559', 'British Library, Add MS 4136, via DECODE R9256'), 'caprile1519': ('caprile1519_lead.jpg', 'ASMo Ambasciatori Ungheria b. 4, Caprile to Duke Alfonso, 6 April 1521: the ciphered slip, read in part here with the key rebuilt from Somogyi&rsquo;s 2025 decipherment', 'Archivio di Stato di Modena, via DECODE R1139'), 'sanchez1523': ('sanchez1523_lead.jpg', 'RAH Salazar 9/28 f. 563r, S&aacute;nchez to Charles V, 16 August 1523: <em>vuestra magestad vera por la capitulacion</em> between code groups', 'Real Academia de la Historia, via DECODE R9767'), 'harley287': ('harley287_lead.jpg', 'Harley MS 287 f. 70v, Cobham at Ostend, 22 March 1587/8: This <em>preparation, together with the reinforcing of his garrisons</em> hereabout', 'British Library, via DECODE R8483'), 'cobham1588': None, 'ormanetto1576': ('ormanetto1576_lead.jpg', 'R118, f. 365: six lines of figures and, beneath, the nuncio&rsquo;s clear note Il Nuntio ha trattato col Sig.r Perez', 'Archivio Apostolico Vaticano, via DECODE R118'), 'heusner1637': ('heusner1637_lead.jpg', 'R4332, letter page 2: dem 503 and the figures of zuwieder gewesen', 'Riksarkivet, Stockholm, via DECODE R4332'), 'bl32305': ('bl32305_lead.jpg', 'R2964, f. 6r, Paris 7 February 1719: the code with the decipherer&rsquo;s que, qu&rsquo;il and vous above it', 'British Library, Add MS 32305, via DECODE R2964'), 'sessa1523': ('sessa1523_lead.jpg', 'RAH Salazar A-27 f. 141r, Sessa to Charles V, 20 February 1523: code groups with clear words left inside the cipher, estonces dava, mas con color', 'Real Academia de la Historia, via DECODE R9660'), 'windischgraetz1721': ('windischgraetz1721_lead.jpg', 'R5029, first page: clear German with the dotted numbers that spell eine Excusation zu machen', 'St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE R5029'), 'dandini1580': ('dandini1580_lead.jpg', 'R72, f. 52: the figures and, below, the secretariat&rsquo;s decipherment in clear', 'Archivio Apostolico Vaticano, via DECODE R72'), 'dinteville1592': ('dinteville1592_lead.jpg', 'BnF Fran&ccedil;ais 3621 f. 130r, Dinteville to Nevers, Langres, 3 July 1592: clear French with the first cipher passage inline', 'Biblioth&egrave;que nationale de France'), 'henter1707': None, 'rome1536': None, 'riksarkivet1628': ('riksarkivet1628_lead.jpg', 'R4330, the archbishop of Bremen to Salvius, 27 November 1631: figure runs inside the clear German with the decipherer&rsquo;s words above them', 'Riksarkivet, Stockholm, via DECODE'), 'sauli1579': ('sauli1579_lead.jpg', 'R192, fol. 195r: the decipherment written over the figures, &ldquo;sopra il neg.o di Piamonte&rdquo;', 'Archivio Apostolico Vaticano, via DECODE R192'), 'ronquillo1676': ('ronquillo1676_lead.jpg', 'Ronquillo to Fuenmayor, Nijmegen, 26 February 1678 (R984), the first cipher block, with no decipherment in the margin: he visto con atenci&oacute;n', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, SEG 2559, via DECODE R984'), 'boswell1628': ('boswell1628_lead.jpg', 'TNA SP 106/5 f. 20, the first three cipher lines turned to the writer&rsquo;s orientation: Upon Saterday being our fifteenth of the presente', 'The National Archives, Kew, via DECODE R413'), 'hernannunez1674': ('hernannunez1674_lead.jpg', 'Hern&aacute;n N&uacute;&ntilde;ez to Fuenmayor, 5 December 1674 (R1012 p. 2): cipher lines with their decipherment in the left margin, ya tengo assegurado a VS que he representado', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, SEG 2559, via DECODE R1012'), 'alessandrino1568': None, 'fagel1804': ('fagel1804_lead.jpg', 'R2238, the cipher page: the clear sentence ending parfaitement d&rsquo;accord, then the figure groups', 'Koninklijk Huisarchief, via DECODE'), 'egmond': ('egmond_lead.jpg', 'The ciphered address: A mon bon cousin / Monsieur le grant maistre / de France', 'Biblioth&egrave;que nationale de France / Gallica'), 'throckmorton': None, 'hellen1752': None, 'beatrice1482': None, 'rennes1563': ('rennes1563_lead.jpg', 'BnF français 3181 f. 55: the clear address and first sentence, then the thirteen lines of cipher that La Ferrière printed as an empty bracket', 'Bibliothèque nationale de France'), 'sessa1593': ('sessa1593_lead.jpg', 'BnF Fran\u00e7ais 3995 f. 97: the Spanish office key, the letter alphabet across the top and the syllable table beneath, identical to Tomokiyo\u2019s reconstruction', 'Biblioth\u00e8que nationale de France'), 'maisse1592': ('maisse1592_lead.jpg', 'BnF Fran\u00e7ais 16093 f. 370, Henri IV to Maisse, 3 November 1592: six lines of clear French breaking off at ou la plus part des lettres se perdent, then some twenty-five lines of figures', 'Biblioth\u00e8que nationale de France'), 'sp106box10': ('sp106box10_lead.jpg', 'DECODE R725 p. 3 (SP 106/10 f. 205), the codebreaker&rsquo;s fair key: the letter alphabet, the letters that stand for whole words, and the two word-lists selected by a bar or a tick over the figure', 'The National Archives, Kew, via DECODE R725'), 'nunzio1718': None, 'nunzio1736': None, 'ceva1632': None, 'pallotto1629': ('pallotto1629_lead.jpg', 'Barb.lat. 6960 p. 5: the clear heading Di Vienna 4 di Agosto, a struck-out opening line, then the unbroken figures of the despatch Kiewning printed as Nr. 153', 'Biblioteca Apostolica Vaticana'), 'kauderbach1754': ('kauderbach1754_lead.jpg', 'R2078, the copy of Kauderbach&rsquo;s letter of 23 December 1754: clear French, then the unseparated figures, 9332131922&hellip; = il n&rsquo;y a pas eu depuis longtems', 'Koninklijk Huisarchief, via DECODE'), 'affry1757': ('affry1757_lead.jpg', 'No. 171, 26 April 1757: the intercept in figures beside Lyonet&rsquo;s clear copy, J&rsquo;ai l&rsquo;honneur de vous addresser la copie d&rsquo;une lettre', 'Koninklijk Huisarchief, via DECODE'), 'acciaiuoli1757': ('acciaiuoli1757_lead.jpg', 'Portogallo 117/6 f. 106r, 24 October 1758: the decipherment made in Rome written above the figures, Benche si dica il R&egrave; assai meglio', 'Archivio Apostolico Vaticano, via DECODE R199'), 'kurtz1639': ('kurtz1639_lead.jpg', 'Kurz to Trauttmansdorff, Hamburg 17 January 1639 (R3811), first page: numbers with a contemporary decipherment written small above them', 'St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE R3811'), 'lopehurtado': ('lopehurtado_lead.jpg', 'RAH Salazar 9/26 f. 237, Lope Hurtado&rsquo;s ciphered letter of 1 November 1522: clear Spanish and three-letter code groups alternating inside the sentence, with the section letter A in the margin keying it to the clerk&rsquo;s clear version on f. 241', 'Real Academia de la Historia, via DECODE R9644'), 'sanchez1522': ('sanchez1522_lead.jpg', 'RAH Salazar 9/26 f. 299r, S&aacute;nchez to Charles V, 20 November 1522: a ciphered paragraph at the head, the news of the siege of Rhodes in clear, and two ciphered lines above the signature', 'Real Academia de la Historia, via DECODE R9653'), 'soria1523': None, 'hm1645': None, 'balbases1677': ('balbases1677_lead.jpg', 'Balbases to Fuenmayor, 3 August 1677 (R985): the cipher block and its contemporary decipherment in the left margin', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, SEG 2559, via DECODE R985'), 'morosini1588': ('morosini1588_lead.jpg', 'Francia 22 f. 308r, the head of the despatch of 23 December 1588, docketed dup.to di 23 Decembre: the figures that report the murder of the Duke of Guise', 'Archivio Apostolico Vaticano, via DECODE R43'), 'sp106r927': ('sp106r927_lead.jpg', 'TNA SP 106/10 f. 243, the last lines turned to the writer&rsquo;s orientation: et vous supplie tres humblement, monsieur, me continuer l&rsquo;honneur de vostre bienveuillance', 'The National Archives, Kew, via DECODE R927'), 'michell1751': ('michell1751_lead.jpg', 'The Hague copy of Frederick II&rsquo;s letter to Michell, 28 December 1751: the clear opening, then the code from 1555 1550 (et suis)', 'Koninklijk Huisarchief, The Hague, via DECODE R1957'), 'carpio1677': ('carpio1677_lead.jpg', 'Carpio to Fuenmayor, 4 September 1677 (R1010): the cipher with its decipherment in the left margin, &ldquo;La Armada de Francia sali&oacute; de Mecina&hellip;&rdquo;', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R1010'), 'windischgraetz1720': ('windischgraetz1720_lead.jpg', 'Register copy of Charles VI’s letter of 3 February 1720, book 5 p. 402: clear German with runs of nomenclator numbers, den Pentenrider and Argwohn machen von Frankreich und dem Regenten', 'Státní oblastní archiv v Plzni, via DECODE R5020'), 'matthias1482': None, 'sadoleto1482': ('sadoleto1482_lead.jpg', 'ASMo Ambasciatori Ungheria b. 1/9 no. 8, Sadoleto to Ercole, Pozsony 16 July 1482: the seven cipher lines, from essendo in Buda to cento milia', 'Archivio di Stato di Modena, via DECODE R1102'), 'buda1489': ('buda1489_lead.jpg', 'ASMi Sforzesco 650, the letter of 22 November 1489: the clear address La Ex.tia vra and the first lines of cipher, intende ad quali termine la pratica de pace', 'Archivio di Stato di Milano, via Vestigia'), 'sessa1524': None, 'florence1429': ('florence1429_lead.jpg', 'ASF Dieci di Balìa, Responsive 2 no. 171: Galeotto da Ricasoli’s letter from Urbino, with Gabbrielli’s 1863 glosses between the lines', 'Archivio di Stato di Firenze, via DECODE R3754'), 'maria1435': ('maria1435_f59r_letter.jpg', 'ACA Cancillería reg. 3225 f. 59r, the queen’s letter to Alfonso V of 5 August 1435: three runs of signs in the first four lines of the clear Catalan', 'Arxiu de la Corona d’Aragó, via DECODE R10171'), 'heidelberg597': ('heidelberg597_lead.jpg', 'Cod. Pal. germ. 597 f. 1r: the compiler’s alphabet written as one unbroken run of signs and struck through, then vnd ich in clear and the signs for hab es', 'Universitätsbibliothek Heidelberg'), 'lorraine1592': ('lorraine1592_f109_cipher.jpg', 'BnF Fran\u00e7ais 3621 f. 109, a line of the cipher: ordinary cursive letterforms, opening with the group that spells chasteau', 'Biblioth\u00e8que nationale de France'), 'reserva12': ('reserva12_block1.jpg', 'ACA Reserva 12, the first lines of the strip: Senyor jous / pus compli / escriua ja, to be read down the columns of the block', 'Arxiu de la Corona d’Aragó, via DECODE R10170'), 'orbais': ('orbais_f126v_depeschera.jpg', 'BnF fr. 3413 f. 126v, to the abbé d’Orbais, 23 August 1589: Les jugemens de Dieu sont fort profons et inscrutables, then the cipher signs of depeschera, dedans deux jours', 'Bibliothèque nationale de France'), 'clair357': ('clair357_f167r_glosses.jpg', 'BnF Clairambault 357 f. 167r: two-digit figures with the 1586 decipherer’s words written between the lines, Fumé, visadmiral, du Roy de Navarre', 'Bibliothèque nationale de France'), 'breves1603': ('breves1603_key_leaf.jpg', 'BnF fr. 3462 f. 103, the key of Savary de Brèves for 1602–03: persons in the left column, the alphabet across the top, the nomenclator below, doubles and nulls at the foot on the right', 'Bibliothèque nationale de France'), 'pelissier1592': ('pelissier1592_f46r_head.jpg', 'BnF Français 3982 f. 46r, Pelissier to Jeannin, Burgos, 13 September 1592: the clear opening and the first rows of cipher, with the decipherer’s scattered glosses', 'Bibliothèque nationale de France'), 'soglia1848': ('soglia1848_block_head.jpg', "The Roman reprint of L'Italia del Popolo, 30 June 1848: the clear opening of Cardinal Soglia's dispatch and the first lines of digits, 5 the word break, 8XXX the code", 'Tony Gaffney, via Klaus Schmeh, Cipherbrain'), 'vich1511': ('vich1511_n46_cipher_decipher.jpg', "AHN Estado 8715 N.46, 5 July 1511: the opening lines of the cipher above the opening of the clerk's decipherment, Con beltran de cordona que partio de Sevilla a xvj de junio", 'Archivo Histórico Nacional (PARES)'), 'norfolk1570': ('norfolk1570_f74r_lines.jpg', 'BL Cotton MS Caligula C II f. 74r, the left half of the first five cipher lines of Mary to Norfolk, the 20th [1570]: I have, my oun good lord', 'British Library'), 'orpo1942': ('orpo1942_redform.jpg', 'W/T Red Form from intercept station 51 for the Mogilev message of 16 June 1942, with the discriminator ARTTN and the first cipher groups', 'NARA, RG 457, HCC, Box 202, via Weierud (CryptoCellar, 2020)'), 'legation': ('legation_no88.jpg', "NARA M35 reel 3 frame 0206, No. 88 of 25 June 1812: the clerk's pencil decode above the code groups stops where Ford's nine undecyphered lines begin", 'National Archives and Records Administration'), 'sunintercepts': ('sunintercepts_tenkiutai.jpg', 'Dai Jitao to Sun Yat-sen, 26 March 1917: condenser words on the received-message form, signed Tenkiutai; the last word ends in the rhyme code for the 26th', 'JACAR'), 'adrian1521': ('adrian1521_f1r_head.jpg', 'AGS Estado leg. 8 no. 150, f. 1r: the address, the clear opening and the first cipher lines, where Gredilla read the death of the King of England', 'Archivo General de Simancas, via PARES'), 'toledo1565': ('toledo1565_f1r_lead.jpg', "AGS Estado leg. 1394 no. 247 f. 1r, the first lines of García de Toledo's letter of 16 July 1565, figure runs inline in the clear Spanish, among them seiscientos soldados and en tiera", 'Archivo General de Simancas (PARES)'), 'yard1699': ('yard1699_oct12.jpg', 'Yard to Manchester, Whitehall, 12 October 1699, p. 1: runs of figure groups set inside the clear English', 'Beinecke Rare Book and Manuscript Library, Yale University'), 'sormano': ('sormano_f121r_head.jpg', 'BnF fr. 3096 f. 121r, the head of no. 66 with the docket duplicata, the clear opening and the first cipher runs', 'Bibliothèque nationale de France'), 'esp318': ('esp318_f116r_gloss.jpg', 'BnF Espagnol 318 f. 116r, two ciphered lines with a later hand carrying a partial decipherment written small between them', 'Bibliothèque nationale de France'), 'gramont1529': ('gramont1529_f45r_head.jpg', 'BnF fr. 3091 f. 45r, the clear opening of Gramont to Montmorency, 11 October 1529, and the first lines of the five pages of cipher', 'Bibliothèque nationale de France'), 'raince': ('raince_p30_lines.jpg', "BnF fr. 2984 p. 30, the first three lines of the second ciphered page of the letter of 13 May 1526", 'Bibliothèque nationale de France'), 'richelieu': None, 'bethune': ('bethune_f34.jpg', 'BnF fr. 3484 f. 34r, the first enciphered passage of Henri IV to Béthune, 10 November 1601', 'Bibliothèque nationale de France'), 'feuquieres': ('feuquieres_p283.jpg', 'Mémoires de Catinat 1819, vol. II p. 283, the ciphered despatch', 'Bayerische Staatsbibliothek'), 'urquhart': None, 'mondoucet': None, 'nevers1593': ('nevers1593_f209_lines.jpg', 'BnF Français 3985 f. 209, the copy of Nevers to Pisany of 8 September 1593, figures inside the clear text', 'Bibliothèque nationale de France'), 'mendoza1589': ('mendoza1589_f14.jpg', 'BnF Français 3641 f. 14, the copy made by the 1589 decipherer of letter A, with the unread code groups underlined and listed in the margin', 'Bibliothèque nationale de France'), 'herbault1626': ('herbault1626_f73r.jpg', 'BnF Français 3669 f. 73r, figure cipher with the 1626 decipherment written under each line', 'Bibliothèque nationale de France'), 'sormano1529': ('sormano1529_f124.jpg', 'BnF Français 3096 f. 124r, four lines of cipher with the contemporary decipherment down the margin', 'Bibliothèque nationale de France'), 'hesse1603': ('hesse1603_p310.jpg', 'Rommel 1840, p. 310, a page of the King\'s letter of 20 May 1606 in figures', 'Internet Archive'), 'catinat1691': ('catinat1691_p320.jpg', 'Mémoires de Catinat 1819, vol. II p. 320, the start of the King\'s letter of 14 September 1691 in figures', 'Bayerische Staatsbibliothek'), 'ormonde': ('ormonde_p28.jpg', 'Page of the Maltravers to Ormonde cipher letter, 1634', 'Ormonde manuscripts'), 'vatican': ('vatican_meister176.jpg', 'Meister 1906, page 176: the Farnese chancery keys of 1539 to 1542, including the last cipher with Poggio', 'Meister, Die Geheimschrift, 1906, via the Internet Archive'), 'lucca': None, 'boswell': None, 'forster': None, 'warsaw': None, 'hyde': ('hyde_p396.jpg', 'Page 396 of the Life of Barwick, 1724, with the ciphered superscription', 'Life of Barwick, 1724'), 'armstrong': ('armstrong_ps.jpg', 'The coded postscript of Armstrong to Madison, 30 August 1808', 'Founders Online'), 'debosnys': ('debosnys_verse.png', 'Debosnys cipher poem in his invented script, 1883', ''), 'sunyatsen': ('sunyatsen_telegram.png', 'The Swatow telegram to Sun Yat-sen, 3 April 1916', 'JACAR'), 'huangxing': ('huangxing_telegram.png', 'Telegram from Huang Xing, 25 May 1916', 'JACAR'), 'adfgvx': None, 'goldbar': ('goldbar_bar.jpg', 'One of the seven Chinese gold bars with its Latin-letter strings', 'IACR'), 'roosevelt': ('roosevelt_fig2.jpg', 'The Roosevelt letter of 1935: three lines of digits, the letter lines, a skull and crossbones and a dagger through a boot', 'The Friedman Legacy, NSA 1992, Internet Archive scan'), 'copenhagen': ('copenhagen_note.jpg', 'The Copenhagen cryptogram: three lines of digits, letters and strokes', 'Scan published by Klaus Schmeh, Cipherbrain, 2015'), 'scorpion': ('scorpion_s1.jpg', 'Scorpion cipher S1, 70 symbols in a 10 by 7 grid, 1991', 'FBI release via Oranchak and Schmeh'), 'voynich': ('voynich_f34r.jpg', 'Voynich manuscript, folio 34r: a herbal page with four paragraphs of Voynichese', 'Beinecke MS 408, public domain, via Wikimedia Commons'), 'famous': None, 'solved': None}
IMAGES['lebel1593'] = ('lebel1593_lead.jpg', 'Fr. 3983 no. 62, f. 130r (10 March 1593): the clear opening, then the cipher, letter signs run together and code numbers set off by dots', 'Biblioth&egrave;que nationale de France, Gallica')
IMAGES['wod1568'] = ('wod1568_lead.jpg', 'Add MS 4136 f. 32: the first four lines of Throckmorton&rsquo;s letter of 10 July 1559 in his Cipher 1', 'British Library, Add MS 4136, via DECODE R2988')
IMAGES['norreys1567'] = ('norreys1567_lead.jpg', 'Add MS 4136 f. 161: Forbes&rsquo;s numbered copy of Norreys&rsquo;s ciphered words, 6 February to 9 March 1567/8', 'British Library, Add MS 4136, via DECODE R9251')
IMAGES['guiche1551'] = ('guiche1551_lead.jpg', 'BnF fr. 3138 f. 60v, La Guiche to Montmorency, 22 November 1551: invented signs between lines of clear French, the first two cipher lines struck through', 'Biblioth&egrave;que nationale de France')

IMAGES['rakoczi1707'] = None
IMAGES['rakoczi1704'] = None
IMAGES['papai1706'] = None
IMAGES['bay1706'] = ('bay1706_lead.jpg', 'The opening of the letter, clear salutation then cipher', 'MNL OL G15 D 81/5, via DECODE R478')
IMAGES['charlesixducroc'] = ('charlesixducroc_lead.jpg', 'Charles IX to Philibert du Croc: the main letter in graphic cipher, with the signature and postscript lower on the leaf', 'Archives d&eacute;partementales de la Ni&egrave;vre, reproduced by Destray (1924), via Gallica and DECODE R2789')
IMAGES['vanreede1792'] = ('vanreede1792_lead.jpg', 'Van Reede to William V, 4 February 1792: the figures with the contemporary pencil gloss &mdash; ci tro n sur le(s) &hellip; demi', 'Koninklijk Huisarchief, The Hague, via DECODE R1057')
IMAGES['vanreede1787'] = ('vanreede1787_lead.jpg', 'Van Reede&rsquo;s despatch of 29 December 1787, first page: the gloss dites &hellip; avant hier over the first groups, 2750 &hellip; 2578 3350', 'Nationaal Archief, The Hague, via DECODE R1026')
IMAGES['kaa4591'] = None
IMAGES['kaa4591b'] = None
IMAGES['r1874'] = None
IMAGES['r1875'] = None
IMAGES['haga1620'] = ('haga1620_lead.jpg', 'R2113 p.2, Constantinople 31 March 1620: clear Dutch with the cipher spans inline, (44) ende (45) arbeiden bij (4) om tyt te winnen', 'Nationaal Archief, The Hague, via DECODE R2113')
IMAGES['deswart1782'] = ('deswart1782_lead.jpg', 'De Swart&rsquo;s despatch of 8 March 1782, first page: the clear salutation, then the marked groups 15, 452, 730, 833 = waar bij ingesloten', 'Nationaal Archief, The Hague, via DECODE R1036')
IMAGES['nevers1589'] = ('nevers1589_lead.jpg', 'BnF Fran\u00e7ais 3977 f. 318: the Recueil sommaire of letters written in cipher by the King\u2019s enemies, September and October 1589 \u2014 a digest in clear French, the cipher itself elsewhere', 'Biblioth\u00e8que nationale de France')
IMAGES['roell1809'] = ('roell1809_lead.jpg', 'R1469, first page: &ldquo;Monsieur&rdquo; and the opening rows of code, with line numbers in the margin', 'Nationaal Archief, The Hague, via DECODE R1469')
IMAGES['rechteren1785'] = ('rechteren1785_lead.jpg', 'Head of the deciphered letter, &ldquo;Ont cyfferde Missive&rdquo;, 23 Sept/4 Oct 1785, with the cipher groups down the margin', 'Nationaal Archief, The Hague, via DECODE R1039')
IMAGES['r1944'] = ('r1944_lead.jpg', 'The clear copy of Bourdeaux&rsquo;s dispatch no. 16, Berlin, 31 January 1801, fol. 295', 'Nationaal Archief, The Hague, via DECODE R1946')
IMAGES['hereditary1796'] = ('hereditary1796_lead.jpg', 'R2239, head of the letter: Berlin 12. Mars 1796, then number groups with superscript marks and clear words', 'Koninklijk Huisarchief, The Hague, via DECODE R2239')
IMAGES['r1892'] = ('r1892_lead.jpg', 'Page 2, the head of the Dutch postscript: in het hollandsch met cijffer, then digit pairs written top over bottom', 'Koninklijk Huisarchief, The Hague, via DECODE R1892')
IMAGES['r2242'] = ('r2242_lead.jpg', 'Page 1: four cipher lines, the clear Dutch written beneath', 'Koninklijk Huisarchief, The Hague, via DECODE R2242')
IMAGES['r2234'] = ('r2234_lead.jpg', 'The head of the letter: section capital D, the date in clear, then one line per alphabet', 'Koninklijk Huisarchief, The Hague, via DECODE R2234')
IMAGES['marburg1635'] = ('marburg1635_lead.jpg', 'The cipher lines with the contemporary gloss over the first four', 'Hessisches Staatsarchiv Marburg, via DECODE R4500')
IMAGES['r2232'] = ('r2232_lead.jpg', 'The opening of the letter: clear text, then the numbers with superscript indices', 'Koninklijk Huisarchief, The Hague, via DECODE R2232')
IMAGES['r1942'] = ('r1942_lead.jpg', 'Hogendorp&rsquo;s ciphered dispatch no. 12 of 5 July 1803: the clear address to Maarten van der Goes followed by the marked numerical groups', 'Nationaal Archief, The Hague, via DECODE R1942')

SURVEYS = ('famous', 'solved')
# chip value on writeups.html, menu label, badge class, predicate
GROUPS = [('solved', 'Solved', 'solved', lambda p: p['st'] == 'solved'),
          ('found', 'Explained', 'found', lambda p: p['st'] == 'found'),
          ('partial', 'Partly read', 'partial', lambda p: p['st'] == 'partial' and p['slug'] not in SURVEYS),
          ('stuck', 'Attempted, not solved', 'stuck', lambda p: p['st'] == 'stuck'),
          ('survey', 'Surveys', 'todo', lambda p: p['slug'] in SURVEYS)]
NAV_LATEST = 6          # write-ups shown in the menu; the rest are one click away on writeups.html

def kind_of(p): return 'survey' if p['slug'] in SURVEYS else p['st']

def nav_html(current):
    """The Write-ups menu. It stopped listing every page when the count passed forty: it now shows the newest few,
    the counts by outcome (each a link into the filtered index) and the way to the full list on writeups.html."""
    cur = lambda slug: ' aria-current="page"' if slug == current else ''
    latest = sorted([p for p in PAGES if p['slug'] not in SURVEYS],
                    key=lambda p: (DATES['pages'].get(p['slug'], {}).get('first', TODAY), p['y']), reverse=True)[:NAV_LATEST]
    lis = ''.join(f'<li><a href="{p["slug"]}.html"{cur(p["slug"])}><span class="st {p["st"]}">{p["stt"]}</span>'
                  f'<b>{p["label"]}</b><span class="yr">{p["year"]}</span></a></li>' for p in latest)
    groups = ''.join(f'<li><a href="writeups.html#kind={key}"><span class="st {cls}">{sum(1 for p in PAGES if pred(p))}</span>'
                     f'<b>{name}</b></a></li>' for key, name, cls, pred in GROUPS)
    on = ' class="active"' if current == 'writeups' or any(p['slug'] == current for p in PAGES) else ''
    panel = (f'<div class="grp"><h4>Latest</h4><ul>{lis}</ul></div>'
             f'<div class="grp"><h4>By outcome</h4><ul>{groups}</ul></div>'
             f'<div class="foot"><a href="writeups.html"{cur("writeups")}>All {len(PAGES)} write-ups, with filters &rarr;</a>'
             f'<a href="writeups.html#src=notes">Results only in the notes</a></div>')
    return (
        f'<header class="nav"><div class="in">\n'
        f'  <a class="brand" href="index.html"><span class="glyph">972</span><span>{SITE}</span></a>\n'
        f'  <button class="navtoggle" type="button" aria-expanded="false" aria-controls="sitemenu"><span></span><span></span><span></span><i>Menu</i></button>\n'
        f'  <nav id="sitemenu" class="links" aria-label="Site">\n'
        f'    <details class="menu"><summary{on}>Write-ups <svg width="10" height="7" viewBox="0 0 10 7" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></summary>\n'
        f'      <div class="panel wp">{panel}</div></details>\n'
        f'    <a href="catalogue.html"{" aria-current=\"page\"" if current == "catalogue" else ""}>The Unsolved Catalogue</a>\n'
        f'    <a href="atlas.html"{cur("atlas")}>Atlas</a>\n'
        f'    <a href="keys.html"{cur("keys")}>Key web</a>\n'
        f'    <a href="secret.html"{cur("secret")}>Secret letter</a>\n'
        f'    <button class="searchbtn" type="button" aria-label="Search the site" aria-keyshortcuts="/ Control+K"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.8" cy="6.8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10.5 10.5L15 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Search</span><kbd>/</kbd></button>\n'
        f'    <a class="ext" href="{REPO}" rel="noopener">Code &#8599;</a>\n'
        f'    <button class="theme" type="button" aria-label="Switch between dark and light" title="Dark / light"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.8a6.2 6.2 0 0 1 0 12.4z" fill="currentColor"/></svg></button>\n'
        f'  </nav>\n</div></header>\n' + SEARCH_HTML)

SEARCH_HTML = (
    '<div class="search" id="search" hidden>\n'
    '  <div class="sbox" role="dialog" aria-modal="true" aria-label="Search the site">\n'
    '    <form class="sform" role="search" onsubmit="return false">\n'
    '      <svg width="18" height="18" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.8" cy="6.8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10.5 10.5L15 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>\n'
    '      <input type="search" id="sq" placeholder="Search names, places, shelfmarks, words of the cipher&hellip;" autocomplete="off" spellcheck="false" aria-label="Search" aria-controls="sres">\n'
    '      <button type="button" class="sclose" aria-label="Close search">Esc</button>\n'
    '    </form>\n'
    '    <div class="sres" id="sres" role="listbox" aria-label="Results"></div>\n'
    '    <div class="shint"><span><kbd>&uarr;</kbd><kbd>&darr;</kbd> move</span><span><kbd>&crarr;</kbd> open</span><span><kbd>Esc</kbd> close</span><span class="sn" id="sn"></span></div>\n'
    '  </div>\n</div>')

# ---------------------------------------------------------------------------
# writeups.html: every write-up, filterable, followed by the results that exist only as notes in the repository.
# The second list is read from ../README.md, whose Results tables are the ledger every session keeps: a row whose
# "Where" column links to a site page is a write-up (checked against PAGES), any other row is notes only.
PERIODS = [('1500s', 'to 1599', lambda y: y < 1600), ('1600s', '1600s', lambda y: 1600 <= y < 1700),
           ('1800s', '1700s and 1800s', lambda y: 1700 <= y < 1900), ('1900s', '1900s', lambda y: 1900 <= y < 9000)]
KINDS = [('solved', 'solved'), ('found', 'explained or found solved'), ('partial', 'partly read'),
         ('stuck', 'attempted, not solved'), ('offline', 'waiting on an archive'), ('survey', 'survey')]
# README section heading, status class, badge text
README_SECTIONS = [('### Solved', 'solved', 'solved'), ('### Explained', 'found', 'explained'),
                   ('### Partly read', 'partial', 'partly read'), ('### Found already solved', 'found', 'found solved'),
                   ('### Attempted and closed', 'stuck', 'attempted'), ('### Offline only', 'offline', 'offline only'),
                   ('### In progress', 'partial', 'in progress')]

def period_of(y):
    return next((k for k, _, f in PERIODS if f(y)), 'survey')

def repo_url(link):
    if link.startswith('http'): return link
    link = link.lstrip('./')
    return f'{REPO}/{"tree" if link.endswith("/") else "blob"}/main/{link}'

def md_inline(s):
    """The little Markdown the README cells use: links, bold, italic, code."""
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{repo_url(m.group(2))}" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

def year_of(date):
    m = re.search(r'(\d{4})', date)
    if m: return int(m.group(1))
    m = re.search(r'(\d{2})th c', date)
    return int(m.group(1)) * 100 - 50 if m else 0

def readme_notes():
    """Rows of the README results tables that have no site page: target, date, result, link, status."""
    try: text = (HERE.parent / 'README.md').read_text(encoding='utf-8')
    except FileNotFoundError: return []
    slugs = {p['slug'] for p in PAGES}
    notes, seen_pages, st = [], set(), None
    for line in text.splitlines():
        if line.startswith('## '): st = None
        if line.startswith('### '):
            st = next(((k, t) for h, k, t in README_SECTIONS if line.startswith(h)), None); continue
        if not st or not line.startswith('| ') or line.startswith('| Target') or line.startswith('|---'): continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 4: continue
        target, date, result, where = cells[0], cells[1], cells[-2], cells[-1]
        pages = re.findall(r'cyphersolver/([a-z0-9]+)\.html', where)
        if pages:
            for slug in pages:
                if slug in slugs: seen_pages.add(slug)
                else: print(f'  note: README links {slug}.html, which is not in the manifest')
            continue
        links = re.findall(r'\]\(([^)\s]+)\)', where)
        if not links: continue
        notes.append(dict(target=md_inline(target), date=html.escape(date, quote=False), y=year_of(date),
                          result=md_inline(result), url=repo_url(links[0]), st=st[0], stt=st[1]))
    for slug in sorted(slugs - seen_pages - set(SURVEYS)):
        print(f'  note: {slug}.html has no README row')
    return notes

def writeups_html():
    def q(*parts): return html.escape(plain(' '.join(parts)).lower(), quote=True)
    rows = []
    for p in sorted(PAGES, key=lambda p: p['y']):
        rows.append(f'<li data-kind="{kind_of(p)}" data-period="{period_of(p["y"])}" data-src="page" '
                    f'data-q="{q(p["label"], p["title"], p["place"], p["year"], p["blurb"], p["stt"])}">'
                    f'<a href="{p["slug"]}.html"><span class="st {p["st"]}">{p["stt"]}</span>'
                    f'<span class="t">{avatars_html(p["slug"])}{p["title"]}</span>{when_html(p, cls="dt")}<span class="yr">{p["year"]}</span>'
                    f'<span class="b">{p["blurb"]}</span></a></li>')
    notes = readme_notes()
    nrows = []
    for n in sorted(notes, key=lambda n: n['y']):
        nrows.append(f'<li data-kind="{n["st"]}" data-period="{period_of(n["y"])}" data-src="notes" '
                     f'data-q="{q(n["target"], n["result"], n["date"], n["stt"])}">'
                     f'<a href="{n["url"]}" rel="noopener"><span class="st {n["st"]}">{n["stt"]}</span>'
                     f'<span class="t">{n["target"]}</span><span class="dt">notes &#8599;</span><span class="yr">{n["date"]}</span>'
                     f'<span class="b">{n["result"]}</span></a></li>')
    chips = lambda facet, vals: ''.join(f'<button type="button" class="chip" data-facet="{facet}" data-val="{k}" aria-pressed="false">{label}</button>' for k, label in vals)
    total = len(rows) + len(nrows)
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>All write-ups &mdash; {len(rows)} ciphers by outcome and date, and {len(nrows)} results still in the notes</title>\n'
        f'<meta name="description" content="Every write-up on the site, filterable by outcome, period and text, followed by the '
        f'results that exist only as notes in the repository: read, explained, attempted or waiting on an archive.">\n'
        f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        '<section class="hero">\n'
        f'  <p class="kicker">Index &middot; {len(rows)} write-ups &middot; {len(nrows)} results only in the notes</p>\n'
        '  <h1>Every write-up</h1>\n'
        '  <p class="sub">Each cipher this site has worked on, in date order, with its outcome. Filter by outcome or period, or search '
        'the titles and summaries. The second list is work that exists only as notes in the repository: results not yet written up, '
        'attempts closed from the evidence, and items waiting on an archive.</p>\n'
        '  <div class="jump"><a href="#pages">Write-ups</a><a href="#notes">Only in the notes</a><a href="catalogue.html">Catalogue</a></div>\n'
        '  <p class="meta">Daniel Bourdeau</p>\n</section>\n\n<main>\n\n'
        '<div class="wfilters" role="search">\n'
        f'  <div class="facet"><span class="flabel">Outcome</span>{chips("kind", KINDS)}</div>\n'
        f'  <div class="facet"><span class="flabel">Period</span>{chips("period", [(k, l) for k, l, _ in PERIODS])}</div>\n'
        f'  <div class="facet"><span class="flabel">Where</span>{chips("src", [("page", "site page"), ("notes", "notes only")])}</div>\n'
        '  <div class="facet"><span class="flabel">Search</span><input id="wq" type="search" placeholder="titles, places, summaries" aria-label="Search the write-ups">'
        '<button type="button" class="chip" id="wreset">reset</button></div>\n'
        f'  <p class="wcount" id="wcount" aria-live="polite">All {total} entries</p>\n</div>\n\n'
        '<section class="wsec" id="pages">\n<h2 id="write-ups"><span class="num">01</span> Write-ups</h2>\n'
        '<ul class="list wl">\n' + '\n'.join(rows) + '\n</ul>\n</section>\n\n'
        '<section class="wsec" id="notes">\n<h2 id="only-in-the-notes"><span class="num">02</span> Only in the notes</h2>\n'
        f'<p>Results recorded in the repository <a href="{REPO}#results" rel="noopener">README</a> that have no page here yet. '
        'Each row links to the folder with the notes, transcriptions and code. The rows are read from the README at build time, '
        'so a result lands here as soon as it is logged there.</p>\n'
        '<ul class="list wl">\n' + '\n'.join(nrows) + '\n</ul>\n</section>\n\n</main>\n<!-- site:footer -->\n</body>\n</html>\n')

def footer_html(current):
    order = sorted([p for p in PAGES if p['slug'] not in ('famous', 'solved')], key=lambda p: p['y'])
    prev = nxt = None
    for i, p in enumerate(order):
        if p['slug'] == current:
            prev = order[i-1] if i > 0 else None; nxt = order[i+1] if i+1 < len(order) else None
    cur = next((p for p in PAGES if p['slug'] == current), None)
    rights = f' &middot; {cur["rights"]}' if cur and cur.get('rights') else ''
    links = ['<a href="index.html">Overview</a>']
    if prev: links.append(f'<a href="{prev["slug"]}.html" rel="prev">&larr; {prev["label"]} {prev["year"]}</a>')
    if nxt: links.append(f'<a href="{nxt["slug"]}.html" rel="next">{nxt["label"]} {nxt["year"]} &rarr;</a>')
    links.append(f'<a href="{REPO}" rel="noopener">Code &#8599;</a>')
    links.append('<a href="mailto:dnbourdeau@gmail.com" title="dnbourdeau@gmail.com">Contact &#9993;</a>')
    links.append('<a href="#top">Top &uarr;</a>')
    author = cur.get('author', 'Daniel Bourdeau') if cur else 'Daniel Bourdeau'
    return (f'<footer><div class="in">\n  <span>{author}, September 2026 &middot; Text released under CC BY 4.0{rights}</span>\n'
            f'  <nav aria-label="Footer">{"".join(links)}</nav>\n</div></footer>')

def toc_html(s):
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', s, re.S)
    if len(heads) < 3: return ''
    links = []
    for hid, inner in heads:
        text = re.sub(r'<span class="num">.*?</span>', '', inner); text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'\s+', ' ', html.unescape(text)).strip()
        text = text.split(' &mdash; ')[0]
        links.append(f'<a href="#{hid}">{html.escape(text[:48])}</a>')
    return '<nav class="toc" aria-label="On this page"><span>On this page</span>' + ''.join(links) + '</nav>\n'

def when_html(p, cls='when'):
    """The short datestamp shown on the index cards and list rows."""
    rec = DATES['pages'].get(p['slug'])
    if not rec: return ''
    verb = 'posted' if p['slug'] in ('famous', 'solved') else VERB.get(p['st'], 'posted')
    return (f'<time class="{cls}" datetime="{rec["first"]}" '
            f'title="{verb} {fmt_date(rec["first"])}, updated {fmt_date(rec["updated"])}">'
            f'{VERB_SHORT.get(p["st"], verb)} {fmt_date(rec["first"], short=True)}</time>')

def avatars_html(slug):
    """The correspondents' portraits as a small overlapping pair, for cards and list rows."""
    people = sorted(PICTURED.get(slug, []), key=lambda p: p['role'] != 'sender')
    if not people: return ''
    tip = html.escape(' → '.join(p['name'] for p in people), quote=True)
    return (f'<span class="avs" title="{tip}">' +
            ''.join(f'<img src="{p["img"]}" alt="" loading="lazy">' for p in people) + '</span>')

def mini_thumb(slug, cls):
    """A small square for list rows and findings: a crop of the script when there is one, the correspondent's
    portrait tucked into its corner; the portrait alone when there is no script image; '' when there is neither."""
    im = IMAGES.get(slug)
    people = sorted(PICTURED.get(slug, []), key=lambda p: p['role'] != 'sender')
    if not im and not people: return ''
    inner = f'<img class="sc" src="{im[0]}" alt="" loading="lazy">' if im else f'<img class="pt" src="{people[0]["img"]}" alt="" loading="lazy">'
    if im and people: inner += f'<img class="pc" src="{people[0]["img"]}" alt="" loading="lazy">'
    return f'<span class="{cls}">{inner}</span>'

def reveal_run(slug, n=9):
    """The opening run of a reveal passage, for the slides on the index: n cipher tokens with their readings."""
    f = HERE / 'reveal' / f'{slug}.json'
    if not f.exists(): return None
    d = json.loads(f.read_text(encoding='utf-8'))
    toks = [t for t in d.get('tokens', []) if t.get('g') and t.get('p') and t.get('cls') not in ('plain', 'null', 'unk') and t['p'] != '?']
    if len(toks) < 4: return None
    return d, toks[:n]

def slide_extras(slug):
    """Portraits of the correspondents and a strip of the cipher deciphering itself, for a slide on the index."""
    people = sorted(PICTURED.get(slug, []), key=lambda p: p['role'] != 'sender')
    who = ''
    if people:
        one = lambda p: (f'<span class="bw"><img src="{p["img"]}" alt="" loading="lazy"><span><i>{"from" if p["role"] == "sender" else "to"}</i>'
                         f'{html.escape(p["name"])}</span></span>')
        who = '<div class="bn-who">' + '<b aria-hidden="true">&rarr;</b>'.join(one(p) for p in people) + '</div>'
    run = reveal_run(slug)
    strip = ''
    if run:
        d, toks = run
        tiles = ''.join(f'<span class="bt"><span class="g">{html.escape(t["g"])}</span><span class="p">{html.escape(t["p"])}</span></span>' for t in toks)
        strip = (f'<div class="bn-solve"><span class="bk">See it solved</span><div class="bts">{tiles}<span class="bt more">&hellip;</span></div>'
                 f'<a href="{slug}.html#{html.escape(d.get("anchor") or "", quote=True)}" class="bl">{html.escape(d.get("unit") or "")}</a></div>')
    return who, strip

def bnx_panels(s):
    """Dress every slide of the index carousel: its correspondents over the picture and the opening of its
    cipher deciphering underneath. A slide without a picture gets a panel made of the two. Idempotent."""
    s = re.sub(r'\n?<!-- bnx -->.*?<!-- /bnx -->', '', s, flags=re.S)
    s = s.replace('class="bn-panel hasart" data-bnx="1"', 'class="bn-panel noart"').replace('class="bn-panel hasart on" data-bnx="1"', 'class="bn-panel noart on"')
    def dress(panel):
        cta = re.search(r'class="cta" href="([a-z0-9]+)\.html"', panel)
        if not cta: return panel
        who, strip = slide_extras(cta.group(1))
        if not (who or strip): return panel
        if '<figure class="art">' in panel:
            panel = panel.replace('<figure class="art">', '<figure class="art">' + (f'<!-- bnx -->{who}<!-- /bnx -->' if who else ''), 1)
            if strip: panel = panel.replace('</figure>', f'<!-- bnx -->{strip}<!-- /bnx --></figure>', 1)
        else:       # after the text column, which closes on the first </div> after the call to action
            j = panel.index('</div>', panel.index('</a>', cta.end())) + len('</div>')
            panel = panel[:j] + f'\n<!-- bnx --><figure class="art solveart">{who}{strip}</figure><!-- /bnx -->' + panel[j:]
            panel = re.sub(r'class="bn-panel noart( on)?"', lambda k: f'class="bn-panel hasart{k.group(1) or ""}" data-bnx="1"', panel, count=1)
        return panel
    # each slide runs from its opening tag to the next slide's, the last one to the end of the carousel
    starts = [m.start() for m in re.finditer(r'<div class="bn-panel', s)]
    if not starts: return s
    end = s.index('<h2 id="recent">', starts[-1]) if '<h2 id="recent">' in s[starts[-1]:] else len(s)
    bounds = starts + [end]
    return s[:starts[0]] + ''.join(dress(s[bounds[i]:bounds[i + 1]]) for i in range(len(starts))) + s[end:]

def cattop_html(n=6):
    """The highest-priority open entries of the Unsolved Catalogue, for the index."""
    import _catalogue_page as C
    top = sorted([e for e in C.DATA['entries'] if e['counted'] and C.is_open(e)], key=lambda e: (-C.priority(e), e['id']))[:n]
    li = ''.join(f'  <li><a href="catalogue.html#e{e["id"]}">{C.people_html(e) or C.blank_html(e)}<span class="t">{C.esc(e["title"])}</span>'
                 f'<span class="pr" title="priority">{C.priority(e):.1f}</span><span class="yr">{C.esc(e["date"])}</span></a></li>\n' for e in top)
    return f'<!-- cattop:start -->\n<h3 class="listhead">Top of the queue</h3>\n<ul class="list cattop">\n{li}</ul>\n<!-- cattop:end -->\n'

def card_html(p):
    im = IMAGES.get(p['slug'])
    thumb = f'    <img class="thumb" src="{im[0]}" alt="" loading="lazy">\n' if im else ''
    return (f'  <a class="card{" hasthumb" if im else ""}" href="{p["slug"]}.html">\n' + thumb +
            f'    <div class="eyebrow"><span>{p["place"]} &middot; {p["year"]}</span>{when_html(p)}<span class="st {p["st"]}">{p["stt"]}</span></div>\n'
            f'    <h3>{p["title"]}</h3>\n    <p>{p["blurb"]}</p>\n    <p class="quote">{p["quote"]}</p>\n    {avatars_html(p["slug"])}<span class="go">read &rarr;</span>\n  </a>\n')

PORTRAITS = json.loads((HERE / '_portraits.json').read_text(encoding='utf-8')) if (HERE / '_portraits.json').exists() else {}
# entries with no image are names only: the atlas shows them as a lettered circle, the pages and cards leave them out
PICTURED = {k: [p for p in v if p.get('img')] for k, v in PORTRAITS.items() if any(p.get('img') for p in v)}

def parties_html(people):
    """Sender and recipient portraits, sender first, an arrow between them when both are known."""
    order = sorted(people, key=lambda p: p['role'] != 'sender')
    def one(p):
        tip = html.escape(f"{p['name']}: {p['what']}. {p['credit']}.", quote=True)
        return (f'<figure class="party {p["role"]}"><img src="{p["img"]}" alt="{html.escape(p["name"], quote=True)}" title="{tip}" loading="lazy">'
                f'<figcaption><span class="role">{"from" if p["role"] == "sender" else "to"}</span>{p["name"]}</figcaption></figure>')
    sep = '<span class="arrow" aria-hidden="true">&rarr;</span>'
    return '\n<div class="parties">' + sep.join(one(p) for p in order) + '</div><!-- /parties -->'

RECENT_VISIBLE = 5      # "Recent findings" on index.html shows this many entries; the rest fold behind the button

def fold_findings(s, n=RECENT_VISIBLE):
    """Rebuild the Recent findings section so the first n <li> are visible and the rest sit in the hidden
    .more block. Entries may be added to either list by hand; this gathers them all in order and re-splits."""
    m = re.search(r'(<h2 id="recent">.*?</h2>\n(?:<p>.*?</p>\n)?)(<ul class="findings">.*?)(?=\n<h2|\n<!-- |\Z)', s, re.S)
    if not m: return s
    items = [stamp_finding(li) for li in re.findall(r'<li>.*?</li>', m.group(2), re.S)]
    if not items: return s
    head = '<ul class="findings">\n' + '\n'.join(items[:n]) + '\n</ul>'
    rest = items[n:]
    if rest:
        head += ('\n<div class="more" hidden><ul class="findings">\n' + '\n'.join(rest) + '\n</ul></div>\n'
                 f'<button class="showmore" type="button" data-target="findings">Show {len(rest)} earlier finding{"s" if len(rest) != 1 else ""}</button>')
    return s[:m.start(2)] + head + s[m.end(2):]

SHARED_INLINE = ('.why', '.w-yes', '.w-no', '.w-lang', '.w-otp', '.w-short', '.w-fake', '.w-open', '.item', '.item h3', '.item .meta2', '.ct', '.callout', '.callout h3', '.tw')

def process(path):
    slug = path.stem
    s = path.read_text(encoding='utf-8')
    if s.startswith('﻿'): s = s[1:]
    rec = page_dates(slug, s)
    page = next((p for p in PAGES if p['slug'] == slug), None)
    if page and '<section class="hero">' not in s:
        print(f'  note: {slug}.html has no hero section (kicker, title, byline); every write-up has one')
    nav = nav_html(slug)
    s = re.sub(r'\n?<div class="search" id="search".*?</div>\n</div>', '', s, count=1, flags=re.S)
    if '<!-- site:nav -->' in s: s = s.replace('<!-- site:nav -->', nav, 1)
    else: s = re.sub(r'<header class="nav">.*?</header>|<nav class="nav">.*?</nav>', lambda m: nav, s, count=1, flags=re.S)
    s = re.sub(r'(</div></header>)(\s*</div></header>)+', r'\1', s)      # stray closers left by an earlier build
    foot = footer_html(slug)
    if '<!-- site:footer -->' in s: s = s.replace('<!-- site:footer -->', foot, 1)
    else:
        ms = list(re.finditer(r'<footer.*?</footer>', s, re.S))
        if ms: m = ms[-1]; s = s[:m.start()] + foot + s[m.end():]
        else: s = s.replace('</main>', '</main>\n' + foot, 1)
    # give every h2 an id so the contents strip and deep links work
    used = set(re.findall(r'<h2 id="([^"]+)"', s))
    def add_id(m):
        text = re.sub(r'<span class="num">.*?</span>', '', m.group(2)); text = html.unescape(re.sub(r'<[^>]+>', '', text))
        base = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40] or 'section'
        hid = base; k = 2
        while hid in used: hid = f'{base}-{k}'; k += 1
        used.add(hid); return f'<h2 id="{hid}"{m.group(1)}>{m.group(2)}</h2>'
    s = re.sub(r'<h2((?![^>]*\bid=)[^>]*)>(.*?)</h2>', add_id, s, flags=re.S)
    # contents strip
    s = re.sub(r'<nav class="toc".*?</nav>\n*', '', s, flags=re.S)      # also eat blank lines an earlier build left
    if slug != 'index':
        toc = toc_html(s)
        if toc: s = re.sub(r'<main>\n*', lambda m: '<main>\n' + toc, s, count=1)
    # lead figure: pages that have an image in the manifest but no figure of their own get one after the contents strip
    im = IMAGES.get(slug)
    s = re.sub(r'<figure class="lead">.*?</figure>\n?', '', s, flags=re.S)
    if im and '<figure' not in s:
        cap = im[1] + (f'. {im[2]}.' if im[2] else '.')
        fig = f'<figure class="lead"><img src="{im[0]}" alt="{im[1]}"><figcaption>{cap}</figcaption></figure>\n'
        if '<nav class="toc"' in s:
            s = re.sub(r'(<nav class="toc".*?</nav>\n)', lambda m: m.group(1) + fig, s, count=1, flags=re.S)
        else:
            s = s.replace('<main>', '<main>\n' + fig, 1)
    # the correspondents: sender and recipient portraits from _portraits.json, under the hero title
    s = re.sub(r'\n?<div class="parties">.*?</div><!-- /parties -->', '', s, flags=re.S)
    if PICTURED.get(slug) and '<section class="hero">' in s:
        s = re.sub(r'(<section class="hero">.*?</h1>)', lambda m: m.group(1) + parties_html(PICTURED[slug]), s, count=1, flags=re.S)
    # drop inline style blocks made of shared rules only
    def strip_style(m):
        rules = re.findall(r'([^{}]+)\{', m.group(1))
        if rules and all(r.strip() in SHARED_INLINE for r in rules): return ''
        return m.group(0)
    s = re.sub(r'<style>(.*?)</style>\s*', strip_style, s, flags=re.S)
    # dateline: when the finding landed, and when the page last really changed
    mm = re.search(r'<p class="meta">(.*?)</p>', s, re.S)
    if mm: s = s[:mm.start()] + meta_html(page, rec, mm.group(1)) + s[mm.end():]
    s = re.sub(r'<meta name="(?:date|last-modified)"[^>]*>\n?', '', s)
    s = s.replace('</head>', f'<meta name="date" content="{rec["first"]}">\n'
                             f'<meta name="last-modified" content="{rec["updated"]}">\n</head>', 1)
    # the wax seal pressed into a write-up's hero: its outcome, in the colour of its badge
    s = re.sub(r'\n?<div class="seal [a-z]+" aria-hidden="true">.*?</div>', '', s)
    if page and page['slug'] not in SURVEYS and '<section class="hero">' in s:
        word = plain(page['stt']) if len(plain(page['stt'])) <= 14 else VERB[page['st']]
        seal = f'\n<div class="seal {page["st"]}" aria-hidden="true"><span>{html.escape(word)}</span></div>'
        s = re.sub(r'(<section class="hero">.*?)(\n</section>)', lambda m: m.group(1) + seal + m.group(2), s, count=1, flags=re.S)
    # "Watch it decipher": a page with docs/reveal/<slug>.json and no reveal of its own gets one, once, right after the h2
    # the data names as its "anchor" (else before the sources); from then on it is ordinary page content
    rv = HERE / 'reveal' / f'{slug}.json'
    if slug != 'index' and rv.exists() and 'class="creveal"' not in s and '<main>' in s:
        anchor = json.loads(rv.read_text(encoding='utf-8')).get('anchor', '')
        fig = f'<figure class="creveal" data-src="reveal/{slug}.json"></figure>\n'
        m = anchor and re.search(r'<h2 id="%s"[^>]*>.*?</h2>\n?' % re.escape(anchor), s, re.S)
        m2 = re.search(r'<!-- replay:start -->|<h2 id="sources"', s)
        if m: s = s[:m.end()] + fig + s[m.end():]
        elif m2: s = s[:m2.start()] + fig + s[m2.start():]
        else: s = s.replace('</main>', fig + '</main>', 1)
    if 'class="creveal"' in s and 'cipher-reveal.js' not in s:
        s = s.replace('</body>', '<script src="cipher-reveal.js" defer></script>\n</body>', 1)
    # "How it was solved": the replay of the profile's solution steps, before the sources
    s = re.sub(r'<!-- replay:start -->.*?<!-- replay:end -->\n?', '', s, flags=re.S)
    s = re.sub(r'<script src="solve-replay\.js[^"]*" defer></script>\n?', '', s)
    if slug in STEPS:
        block = f'<!-- replay:start -->\n<figure class="sreplay" data-src="steps/{slug}.json"></figure>\n<!-- replay:end -->\n'
        m = re.search(r'<h2 id="sources"', s)
        s = s[:m.start()] + block + s[m.start():] if m else s.replace('</main>', block + '</main>', 1)
        s = s.replace('</body>', f'<script src="solve-replay.js?v={VERSION}" defer></script>\n</body>', 1)
    # the deep-zoom viewer on every page with a figure image (zoom.js; overlays from docs/zoom/<image>.json)
    s = re.sub(r'<script src="zoom\.js[^"]*" defer></script>\n?', '', s)
    if re.search(r'<figure[^>]*>\s*<img', s):
        s = s.replace('</body>', f'<script src="zoom.js?v={VERSION}" defer></script>\n</body>', 1)
    # versions, anchor for "Top", script
    s = re.sub(r'<link rel="stylesheet" href="style.css[^"]*">', f'<link rel="stylesheet" href="style.css?v={VERSION}">', s)
    if 'href="style.css' not in s: s = s.replace('</head>', f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>', 1)
    # the tab icon: a wax seal with a key (favicon.svg, PNG fallbacks rendered from it)
    s = re.sub(r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n?', '', s)
    s = s.replace('</head>', ICONS + '</head>', 1)
    # page scripts carry a hash of their own content, so an edit reaches browsers without a VERSION bump
    s = re.sub(r'<script src="(secret|cipher-reveal|atlas)\.js(?:\?[^"]*)?"',
               lambda m: f'<script src="{m.group(1)}.js?v={hashlib.sha1((HERE / (m.group(1) + ".js")).read_bytes()).hexdigest()[:8]}"', s)
    s = re.sub(r'<script src="site.js[^"]*"></script>\s*', '', s)
    s = s.replace('</body>', f'<script src="site.js?v={VERSION}"></script>\n</body>', 1)
    s = re.sub(r'<body(?![^>]*id=)', '<body id="top"', s, count=1)
    if slug == 'index':
        s = fold_findings(s)
        s = re.sub(r'<!-- live:start -->.*?<!-- live:end -->\n?', '', s, flags=re.S)
        s = re.sub(r'<script src="home\.js[^"]*" defer></script>\n?', '', s)
        s = re.sub(r'(<section class="hero">.*?)(\s*<div class="jump">)', lambda m: m.group(1) + '\n' + live_html() + m.group(2), s, count=1, flags=re.S)
        s = s.replace('</body>', f'<script src="home.js?v={VERSION}" defer></script>\n</body>', 1)
        FEATURED = ['raince', 'hesse1603', 'catinat1691', 'voynich', 'feuquieres', 'armstrong']
        feat = [next(p for p in PAGES if p['slug'] == f) for f in FEATURED]
        rest = sorted([p for p in PAGES if p['slug'] not in FEATURED], key=lambda p: ({'solved': 0, 'found': 1, 'partial': 2, 'stuck': 3}[p['st']] if p['slug'] not in ('famous', 'solved') else 4, -p['y']))
        row = lambda p: (f'  <li><a href="{p["slug"]}.html">{mini_thumb(p["slug"], "rth") or "<span class=rth></span>"}<span class="st {p["st"]}">{p["stt"]}</span><span class="t">{p["title"]}</span>'
                         f'{when_html(p, cls="dt")}<span class="yr">{p["year"]}</span></a></li>\n')
        REST_VISIBLE = 10       # "And the rest" shows this many rows; the others fold behind the button
        shown, folded = rest[:REST_VISIBLE], rest[REST_VISIBLE:]
        more = (f'<div class="more" hidden><ul class="list">\n' + ''.join(row(p) for p in folded) + '</ul></div>\n'
                f'<button class="showmore" type="button">Show {len(folded)} more write-ups</button>\n') if folded else ''
        cards = ('<!-- cards:start -->\n<div class="cards">\n' + ''.join(card_html(p) for p in feat) + '</div>\n'
                 '<h3 class="listhead">And the rest</h3>\n<ul class="list">\n' + ''.join(row(p) for p in shown) + '</ul>\n' + more +
                 f'<p class="allws"><a href="writeups.html">All {len(PAGES)} write-ups, filterable by outcome and period, '
                 f'with the results that are still only in the notes &rarr;</a></p>\n<!-- cards:end -->')
        s = bnx_panels(s)
        s = re.sub(r'<!-- cattop:start -->.*?<!-- cattop:end -->\n?', '', s, flags=re.S)
        s = re.sub(r'(<h2 id="catalogue">.*?)(\n<p><a class="more" href="catalogue\.html")', lambda m: m.group(1) + '\n' + cattop_html().rstrip('\n') + m.group(2), s, count=1, flags=re.S)
        if '<!-- cards:start -->' in s:
            s = re.sub(r'<!-- cards:start -->.*?<!-- cards:end -->', lambda m: cards, s, flags=re.S)
        else:
            s = re.sub(r'(<h2(?: id="writeups")?><span class="num">01</span> Write-ups</h2>\s*)<div class="cards">.*?</div>\n(?=\n<h2)', lambda m: m.group(1) + cards + '\n', s, count=1, flags=re.S)
    after = content_hash(s)
    if after != rec['hash']:     # a generated element normalise() does not know about
        print(f'  note: {slug} rehashed after build; check normalise()')
        rec['hash'] = after
    path.write_text(s, encoding='utf-8')
    return slug

# ---------------------------------------------------------------------------
# Search.  search.json is a flat list of entries that the overlay in site.js
# loads the first time the box is opened: one entry per page (title, blurb and
# opening text) and one per h2 section (heading and the section's text), each
# with the URL that lands on it, plus one per entry of ../catalogue.json.  The
# text is the page as a reader sees it, tags removed, so a word from a quoted
# cipher line or a footnote is found as readily as a title.  Keys: u url,
# t title, h section heading, p page label, y year, st status class,
# stt status text, b body text.
def visible_text(frag):
    frag = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', frag, flags=re.S)
    frag = re.sub(r'<[^>]+>', ' ', frag)
    frag = html.unescape(frag).replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', frag).strip()

def search_entries():
    out = []
    for path in sorted(HERE.glob('*.html')):
        slug = path.stem
        if slug in ('catalogue', 'writeups'): continue   # catalogue from catalogue.json below; writeups is a list of the pages
        s = path.read_text(encoding='utf-8')
        s = re.sub(r'<header class="nav">.*?</header>|<div class="search" id="search".*?</div>\n</div>|<footer.*?</footer>|'
                   r'<nav class="toc".*?</nav>', ' ', s, flags=re.S)
        p = next((q for q in PAGES if q['slug'] == slug), None)
        tm = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S) or re.search(r'<title>(.*?)</title>', s, re.S)
        title = visible_text(p['title'] if p else (tm.group(1) if tm else slug))
        m = re.search(r'<main>(.*?)</main>', s, re.S)
        body = m.group(1) if m else s
        hero = re.search(r'<(header|section|div) class="hero.*?</\1>', s, re.S)
        hero = re.sub(r'<div class="cipherstrip">.*?</div>', ' ', hero.group(0), flags=re.S) if hero else ''   # decorative digits
        base = dict(p=visible_text(p['label']) if p else {'index': 'Overview'}.get(slug, title), y=visible_text(p['year']) if p else '',
                    st=p['st'] if p else '', stt=p['stt'] if p else '')
        parts = re.split(r'(?=<h2 id="[^"]+")', body)
        intro = visible_text((p['blurb'] if p else '') + ' ' + hero + ' ' + parts[0])
        out.append(dict(base, u=f'{slug}.html', t=title, h='', b=intro))
        for part in parts[1:]:
            hm = re.match(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', part, re.S)
            if not hm: continue
            head = visible_text(re.sub(r'<span class="num">.*?</span>', '', hm.group(2)))
            text = visible_text(part[hm.end():])
            if not text and not head: continue
            out.append(dict(base, u=f'{slug}.html#{hm.group(1)}', t=title, h=head, b=text))
    try:
        cat = json.loads((HERE.parent / 'catalogue.json').read_text(encoding='utf-8'))
        for e in cat['entries']:
            b = ' · '.join(str(e.get(k) or '') for k in ('correspondents', 'place', 'shelfmark', 'status', 'why', 'verify', 'outcome'))
            out.append(dict(u=f'catalogue.html#e{e["id"]}', t=e['title'], h='', p='Catalogue',
                            y=str(e.get('date') or e.get('year') or ''), st='', stt=f'no. {e["id"]}', b=visible_text(b)))
    except FileNotFoundError:
        pass
    return out

def write_search_index():
    entries = search_entries()
    (HERE / 'search.json').write_text(json.dumps(entries, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    return len(entries)

# The home page's live header (home.js): a random-cipher button, and the list of
# reveal passages the header deciphers in turn (reveal/index.json).
def live_html():
    rv = sorted(p.stem for p in (HERE / 'reveal').glob('*.json') if p.stem != 'index')
    titles = {p['slug']: plain(p['label']) for p in PAGES}
    (HERE / 'reveal' / 'index.json').write_text(json.dumps([dict(slug=r, label=titles.get(r, r)) for r in rv if r in titles],
                                                           ensure_ascii=False), encoding='utf-8')
    return ('<!-- live:start -->\n<div class="livecount">'
            + '<button type="button" class="randbtn" aria-label="Open a random write-up">Random cipher &rarr;</button></div>\n<!-- live:end -->')

# steps/<slug>.json: the solution steps of each target's profile.json, with its conditions and outcome, for the
# "How it was solved" replay (solve-replay.js).  A profile folder is its page's slug, give or take case.
PROFILE_SLUG = {'bordeaux': 'bordeaux1653'}
STEPS = set()
def write_steps():
    slugs = {p['slug'] for p in PAGES}
    out = HERE / 'steps'; out.mkdir(exist_ok=True)
    for f in sorted(HERE.parent.glob('*/profile.json')):
        slug = PROFILE_SLUG.get(f.parent.name, f.parent.name.lower())
        if slug not in slugs: continue
        pr = json.loads(f.read_text(encoding='utf-8'))
        steps = pr.get('solution') or []
        if len(steps) < 3: continue
        c = pr.get('conditions', {})
        d = dict(slug=slug, title=pr.get('title', ''), steps=steps, outcome=pr.get('outcome', {}),
                 attack=c.get('attack'), inputs=c.get('inputs', []), prior=c.get('prior_solution', {}),
                 human=c.get('human_role'), first=c.get('first_date'), last=c.get('last_date'))
        (out / f'{slug}.json').write_text(json.dumps(d, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        STEPS.add(slug)
    return len(STEPS)

if __name__ == '__main__':
    print('solution replays:', write_steps())
    for f in sorted(HERE.glob('*.html')):      # date every page before any menu is built: the menu lists the newest
        page_dates(f.stem, f.read_text(encoding='utf-8').lstrip('﻿'))
    (HERE / 'writeups.html').write_text(writeups_html(), encoding='utf-8')
    done = [process(p) for p in sorted(HERE.glob('*.html'))]
    save_dates(DATES)
    print('search index:', write_search_index(), 'entries')
    # pages.json: label, year and outcome of every write-up, for the atlas and the key web
    meta = [dict(slug=p['slug'], label=plain(p['label']), title=plain(p['title']), y=p['y'], st=p['st'], stt=plain(p['stt']),
                 **({'people': [{k: q[k] for k in ('role', 'name', 'img')} for q in PORTRAITS[p['slug']]]} if PORTRAITS.get(p['slug']) else {}))
            for p in PAGES if p['slug'] not in SURVEYS]
    (HERE / 'pages.json').write_text(json.dumps(meta, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print('built', ', '.join(done))
IMAGES['poyntz1527'] = None
IMAGES['stafford1586'] = None
IMAGES['harley1582r8500'] = None
IMAGES['harley1582r8504'] = None
IMAGES['poupet1522'] = ('poupet1522_lead.jpg', 'Passage A in cipher and in the 1522 decipherment: <em>Combien que je vouldroie mectre mon ame en gaige</em>', 'Biblioteca Nacional de Espa&ntilde;a, via DECODE R1187')
IMAGES['santacroce1552'] = ('santacroce1552_lead.jpg', 'ASV Francia 3 f. 248r (DECODE R9), Paris, 14 December 1553: three cipher lines struck through, the same postscript written in clear beneath', 'Archivio Apostolico Vaticano, via DECODE R9')
IMAGES['walsingham1585'] = ('walsingham1585_lead.jpg', 'Add MS 32657 f. 194, 10 September 1585: &ldquo;The 13 will in no sort neither be [signs] nor otherwise make [signs] a party&rdquo;, the decipherment above blotted out', 'British Library, Add MS 32657 f. 194 (via DECODE R4844)')
IMAGES['spinelly1516'] = ('spinelly1516_lead.jpg', 'Cotton MS Galba B V f. 40v: the five cipher lines of 1 February 1517, after &ldquo;and of this opinion is the&rdquo;', 'British Library, Cotton MS Galba B V f. 40v (via DECODE R8416)')
IMAGES['wotton1585'] = ('wotton1585_lead.jpg', 'Add MS 32657 f. 167: the draft of 25 August 1585, &ldquo;Sir, 39. came to me yesterday&rdquo;', 'British Library, Add MS 32657 f. 167 (via DECODE R4841)')
IMAGES['randolph1570'] = ('randolph1570_lead.jpg', 'BL Cotton MS Caligula C II f. 278, the contemporary decipherment of Randolph to Sussex, 5 July 1570: cipher words with the English written above', 'British Library, via DECODE R4932')
IMAGES['hamilton1569'] = ('hamilton1569_lead.jpg', 'BL Add MS 33531 f. 73r, Mary Queen of Scots to Archbishop Hamilton, 18 January 1569: the clear salutation and the first lines of cipher', 'British Library, via DECODE R8347')
IMAGES['throck1569'] = ('throck1569_lead.jpg', 'BL Add MS 33531 f. 79r, Throckmorton to Moray, 20 July 1569: cipher words among the clear text, the interlinear decipherment faded under a water stain', 'British Library, via DECODE R8348')
