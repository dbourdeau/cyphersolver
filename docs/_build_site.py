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
VERSION = '20260919a'
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
    r'<meta name="(?:date|last-modified)"[^>]*>', r'\?v=\d+[a-z]*',
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
    return li.replace('<li>', '<li>' + stamp, 1)

# slug, nav label, year label, sort year, place, status class, status text, title, blurb, quote, rights
PAGES = [
    dict(slug='throckmorton', label='Throckmorton', year='1560&ndash;63', y=1561.5, place='France', st='found', stt='key and printed text verified',
         title='Throckmorton &mdash; archived key and published plaintext',
         blurb='Twenty DECODE records in BL Add MS 4136 lead to Forbes and CSP. The archived third cipher reads two short samples, 42 tokens in all. A record-to-edition concordance separates the published counterparts from full token verification; composite material remains to be checked.',
         quote='&ldquo;all be it i be revoked or the warr breake&rdquo;',
         rights='British Library, Add MS 4136, via DECODE; photographs not republished'),
    dict(slug='beatrice1482', label='Beatrice d&rsquo;Aragona', year='1482&ndash;1505', y=1482, place='Pozsony / Buda / Naples &rarr; Ferrara', st='found', stt='earlier readings found',
         title='Beatrice d&rsquo;Aragona: four earlier readings and one plain letter',
         blurb='Four cipher letters have readings in editions of 1877&ndash;78; the May 1486 letter also has manuscript decipherment slips. The fifth record is plain Italian dated 1505, not 1504, and explicitly says the queen has no cipher. The March edition retains unexplained Virtus/Fortis/M. markers; no new key or exhaustive glyph validation is claimed.',
         quote='&ldquo;et per non havere cifra: non ce extendemo altramente per questa&rdquo;',
         rights='Printed edition: Nagy and Ny&aacute;ry, 1877, public domain. ASMo manuscript images not reproduced.'),

    dict(slug='sp106box10', label='SP 106/10 codebreaker', year='1623&ndash;24', y=1623.5, place='London', st='partial', stt='file explained, read in part',
         title='A codebreaker&rsquo;s file &mdash; the Italian intercepts of TNA SP 106/10',
         blurb='DECODE lists seven anonymous, undated, partly decrypted ciphertexts in State Papers 106 box 10. They are one case: the working file of a Jacobean codebreaker, with his solutions between the lines. The key he reconstructed is catalogued three records away as a key rather than a ciphertext, and so fell outside the target list; it sets out a two-figure cipher in which a bar or a tick over the group switches it from a letter to a word of one of two lists. Its vocabulary &mdash; Marques Inichiosa, Palatinato, C. Barberino, Il Principe &mdash; dates the file to 1623&ndash;24, against the catalogue&rsquo;s 1558/1625. The file holds three different ciphers, not one, and about forty-five values of the three-figure code were rebuilt from the codebreaker&rsquo;s own interlinear syllables.',
         quote='&ldquo;It seemes there are numbers of woordes expressed by this difference of &mdash; over the figures whereof in this Cifar.&rdquo;',
         rights='Manuscript rights: The National Archives, Kew, via DECODE'),
    dict(slug='richelieu', label='Richelieu', year='1629', y=1629, place='France', st='solved', stt='solved',
         title='Richelieu to M. de Ranc&eacute; &mdash; BnF Fran&ccedil;ais 3829',
         blurb='Ciphertext-only recovery of a homophonic alphabet with a doubling mark and nomenclature; then found to agree word for word with the decipherment Avenel printed in 1858, which the catalogues had missed.',
         quote='&ldquo;Castor voudroit bien que la [duchesse de Chevreuse] peust estre attrap&eacute;e pr&egrave;s de la fronti&egrave;re&hellip;&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='pallotto1629', label='Pallotto to Barberini 1629', year='1629', y=1629.6, place='Vienna &rarr; Rome', st='found', stt='already in print',
         title='Pallotto to Barberini &mdash; the ciphers of BAV Barb.lat. 6960, printed in 1897',
         blurb='Twenty-eight ciphered sheets in the register of the nuncio to the Emperor, catalogued as undeciphered with their contents unknown. Their contents have been published since 1897: Kiewning&rsquo;s volume of the Nuntiaturberichte prints these despatches from the Roman office&rsquo;s own decipherments, headed dechiffr. The identification is confirmed against the register&rsquo;s clear pages, which run straight through the cipher sheets and carry the edition&rsquo;s wording, and against the enclosure on p. 13. The cipher itself is not broken here, and no partial key is claimed: a held-out test shows the table an aligner learns predicts unseen text no better than the same table shuffled. The failure is measured instead. On synthetic ciphertext the identical pipeline recovers a random key in full from a clean transcription, 87 codes of 100 at a 0.5 per cent digit error rate and 7 of 100 at 1.7 per cent, and a run-length control then went further: the longest provably consistent alignment between cipher and plaintext is 39 letters against a chance baseline of 36 to 39, where the synthetic cipher at the same noise reaches 207. The sheet is not a two-digit encipherment of the text Kiewning prints, and the twenty-seven-letter opening match is below chance.',
         quote='&ldquo;&hellip;con che il demonio resteria ingannato e burlato.&rdquo;',
         rights='Manuscript rights: Biblioteca Apostolica Vaticana'),
    dict(slug='ceva1632', label='Barberini to Ceva 1632', year='1632', y=1632, place='Rome &rarr; Paris', st='partial', stt='read in part',
         title='Barberini to Nuncio Ceva &mdash; the two letters of ASV Francia 346 nobody had read',
         blurb='The catalogue listed five ciphertexts as a transcription job. George Lasry had in fact reconstructed the key of the dossier in 2020 and read four of its eleven letters, which covered three of the five; two were left unread. A beam search over the unseparated figures, under an Italian model built partly from the dossier&rsquo;s own clear passages, reads both, and agrees on 77.5% of letters with the decipherment written between the lines in 1632. Six of the ninety-five nomenclator elements Lasry left blank are given values, among them 830 = Francia; 117 stay unread.',
         quote='&ldquo;&hellip;conseguenze che tengano disunita per un lungo pezzo la Francia, e sotto giogo alle esterne violenze, o almeno impotente a soccorrer li suoi alleati.&rdquo;',
         rights='Manuscript rights: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='ormonde', label='Ormonde', year='1634&ndash;35', y=1634, place='Ireland / England', st='solved', stt='solved',
         title='Maltravers to Ormonde &mdash; a regular block cipher',
         blurb='Doubled letters written with consecutive figures betray a regular key (consonants three figures each from 7, vowels from 64, nulls 91&ndash;111). Every spelled word reads, and the nomenclator is then confirmed clause for clause against Wentworth&rsquo;s own dispatches in Knowler&rsquo;s <em>Strafforde&rsquo;s Letters</em> (1739): the King refusing Kildare, and Ormonde moved for the Council &ldquo;in exchange&rdquo; for Sir Piers Crosby.',
         quote='&ldquo;he was angry [with the Lord Deputy] &hellip; upon his motion [Ormonde] is to be a councellor&rdquo;'),
    dict(slug='vatican', label='Vatican', year='1542', y=1542, place='Rome &rarr; Spain', st='found', stt='solved by Simon Klee',
         title='The Farnese letter &mdash; Simon Klee&rsquo;s solution reviewed',
         blurb='Farnese to the nuncio Poggio, four folios of unseparated digits, set by George Lasry as Vatican Challenge Part 5 in 2019. Simon Klee recovered the mixed one-/two-digit key and a candidate plaintext in September 2026; MysteryTwister accepted the submission. Independent half-text recovery, controls, manuscript checks and historical corroboration support the key and the substance of the reading. The earlier Antonio Elio classification on this site is retracted.',
         quote='&ldquo;Dopo la partita del Montepulciano&hellip;&rdquo;'),
    dict(slug='warsaw', label='Warsaw', year='1627', y=1627, place='Warsaw', st='solved', stt='solved',
         title='From Warsaw, 24 December 1627 &mdash; an alphabet in plain order',
         blurb='DECODE R1408, one page of figures and stray letters with only a dateline in clear, listed as non-decrypted. The letters <em>a</em> and <em>m</em> are nulls, the letter pairs are alternates for consonants, the rare groups are syllables, and the alphabet, recovered blind by a 5-gram-plus-dictionary annealer against shuffled controls, turns out to run in order: odd figures <em>a</em> to <em>m</em>, even figures <em>n</em> to <em>z</em>. A reminder that a promised canonry of Olm&uuml;tz for one of the Queen of Poland&rsquo;s sons has not been conferred.',
         quote='&ldquo;un canonicato d&rsquo;Olmiz ad uno de li suoi figli &hellip; si degni darne subito a me benigna risposta&rdquo;'),
    dict(slug='segur', label='S&eacute;gur', year='1585&ndash;86', y=1585, place='B&eacute;arn &rarr; Germany', st='solved', stt='solved',
         title='Henry of Navarre to S&eacute;gur &mdash; an alphabetical syllabary cipher',
         blurb='Three letters in figures to the envoy raising a German army, BnF 500 de Colbert 401 ff. 233, 239 and 288v, catalogued as undeciphered letters of Henry III. The upper figures pile into one slot in five (mod 5), the signature of a syllable table in alphabetical order; an annealer built on that structure, with the letters&rsquo; own clear French as context, returns a key whose letter part is alphabetical by itself and reads a matched control at 97&nbsp;%. Conclude with Duke Casimir, raise the largest levy, march it at once; Clervant&rsquo;s two thousand reiters; the Vivarais or Dauphin&eacute; road.',
         quote='&ldquo;faictes s&rsquo;il vous est possible la plus grande lev&eacute;e qui ayt est&eacute; faite&rdquo;'),
    dict(slug='boswell', label='Boswell', year='1643', y=1643, place='Oxford &rarr; The Hague', st='solved', stt='read in substance',
         title='Charles I and Nicholas to Boswell &mdash; a regular key, four signs and the wrong addressee',
         blurb='Two ciphered letters of 2 November 1643 (TNA SP 84/157). The alphabet is Robert Pitt&rsquo;s: a 24-letter row four times over 20&ndash;115, verified here at z&nbsp;=&nbsp;9.6 against 20,000 permuted rows. Added here: the four graphic signs are word-signs introduced inside the spelled word (good, Cousin, Master, us), and the King&rsquo;s letter is his re-credentials to the Duke of Courland&rsquo;s envoy, sent through Boswell in Boswell&rsquo;s cipher. Both letters read in substance.',
         quote='&ldquo;back to our good Cousin your Master, to whom we herewith send your re-credentials&rdquo;'),
    dict(slug='kurtz1639', label='Kurz von Senftenau 1639', year='1639', y=1639.1, place='Hamburg &rarr; Vienna', st='partial', stt='key rebuilt, read in part',
         title='Kurz von Senftenau to Trauttmansdorff, Hamburg 1639 &mdash; the vice-chancellor&rsquo;s cipher rebuilt',
         blurb='Nine ciphered reports of the imperial vice-chancellor from Hamburg and Gl&uuml;ckstadt, January to April 1639, in the Trauttmansdorff archive at Kl&aacute;&scaron;ter (DECODE R3811&ndash;R4736). M&iacute;rka rebuilt the key in 2012 and read one letter but printed nothing. From the same interlinear glosses the key falls out as a regular table: 41&ndash;100 are consonant&ndash;vowel syllables, two consonants to each ten in reverse alphabetical order, and the low numbers are homophones. All nine letters decipher in a first pass: Ban&eacute;r in Lower Saxony, Arnim&rsquo;s bid for pardon, the Danish mediation and its collapse.',
         quote='&ldquo;besser ein ungeschlossener, durch den Feindt zertrennter Craistag als ein geschlossener mit einer expressen Neutralitet&rdquo;',
         rights='St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE R3811&ndash;R4736'),
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
         blurb='A letter of Florence&rsquo;s envoy to the Count of Urbino, listed on DECODE as non-decrypted. The abb&eacute; Gabbrielli glossed a few of its words in 1863 and built a key from them, which Meister printed in 1902; the letter was never printed. The three long runs he left unread are decoded sign by sign with his glosses as seeds, two of his nulls resolved and four new values confirmed on the siblings.',
         quote='&ldquo;perch&eacute; dice che Madonna &egrave; pure femina e sospetosa&rdquo;',
         rights='Manuscript images: Archivio di Stato di Firenze, via DECODE R3754'),
    dict(slug='maria1435', label='Mar&iacute;a 1435', year='1435', y=1435, place='Valencia &rarr; Gaeta', st='stuck', stt='not read, keys tested',
         title='Queen Mar&iacute;a to Alfonso V, Valencia 1435 &mdash; Attempted',
         blurb='The oldest unread ciphertext on DECODE with a public image: 42 signs inside a Catalan letter of Queen Mar&iacute;a to Alfonso V, written in Valencia on the day of Ponza, about something &ldquo;continued until All Saints&rdquo;, almost certainly the truce with Castile. Both printed Aragonese keys of the decade were tested: the 1437 alphabet is unrelated, and the 1429 nomenclator seems to match the word signs while its alphabet does not. Four neighbouring registers, 1,414 images, hold no cipher at all; the king&rsquo;s own register shows his letter to her of 27 July 1435 was sent <i>in ciffra</i>.',
         quote='he treballat que [&#541; a ff 8 9 d 3 8 v 8 6 8 2 &#8857;] es continuada daci a tots sants',
         rights='Images: Arxiu de la Corona d&rsquo;Arag&oacute;, via DECODE R10171 and PARES'),
    dict(slug='matthias1482', label='Matthias 1482', year='1482', y=1482, place='Pozsony &rarr; Ferrara', st='found', stt='read in 1877',
         title='Matthias Corvinus to Ercole I d&rsquo;Este, Pozsony 1 June 1482 &mdash; DECODE R1156',
         blurb='The King of Hungary answers Ferrara&rsquo;s call for help in the first weeks of the War of Ferrara, with troops, route, names and plan in a sign cipher. DECODE lists it as partly decrypted, but it was printed in 1877 and again by Fraknói in 1895. The runs are read here from the image and a working key rebuilt; four garbled places in the printed text are corrected, among them the closing sentence the edition prints as nonsense.',
         quote='&ldquo;Speramus cito nos res nostras ita disposituros, ut meliori postea modo vos iuvare possemus&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Modena (images not reproduced)'),
    dict(slug='sadoleto1482', label='Sadoleto 1482', year='1482', y=1482.5, place='Pozsony &rarr; Ferrara', st='partial', stt='read in part',
         title='Nicol&ograve; Sadoleto to Ercole I d&rsquo;Este, Pozsony 1482 &mdash; the Venetian counter-offer to Matthias Corvinus',
         blurb='Ferrara&rsquo;s envoy at the Hungarian court in the first summer of the War of Ferrara wrote parts of his despatches in a sign cipher; they were never printed, and DECODE lists four as partly decrypted. The alphabet is rebuilt from two sibling letters filed with their contemporary clear copies, which also shows that two of the four targets were read at the time. The seven cipher lines of 16 July 1482, which have no clear copy, are read in gist: the other side had offered Matthias Veglia, a fleet command for his natural son J&aacute;nos Corvin and a hundred thousand a year. A faded block of 17 August gives fragments only.',
         quote='&ldquo;et voleva dargli Vegla, et voleva lo figlio (e bastardo) per loco capitaneo &hellip; per mare, et gli voleva dare ogni anno cento milia&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Modena (images not reproduced)'),
    dict(slug='buda1489', label='Buda 1489', year='1489&ndash;90', y=1489, place='Buda &rarr; Milan', st='solved', stt='read',
         title='Maffeo da Treviglio to Ludovico Sforza, Buda 1489&ndash;1490 &mdash; the key reconstructed in 2016 had never been turned back into signs',
         blurb='Judit W. Somogyi reconstructed the cipher of Ludovico Sforza&rsquo;s ambassador at the court of Matthias Corvinus in 2016, but printed it only as a table of numbers, with no image of a single sign, so nothing could be read with it. Her numbering turns out to follow the order of first appearance in the letter of 2 April 1490, which survives with its contemporary clear copy: matching the two gives the shapes back, and about twenty further signs came out of the reading. The two despatches that have no decipherment are now read. The four pages of 22 November 1489, of which only the first two lines had ever been deciphered, cover the peace with Frederick III, the Diet, the marriage of John Corvinus against the rival Neapolitan match, the queen&rsquo;s &ldquo;insatiable wrath of Juno&rdquo;, and a warning that intercepted cipher letters had been read; the letter of 12 January 1490 reports the king riding to Vienna on the 8th and the ambassadors following on the 15th, which its own clear second page confirms word for word.',
         quote='&ldquo;Le littere in cifra che forono intercepte, le quale duplicate sono state scoperte ancora qua&rdquo;',
         rights='Manuscript rights: Archivio di Stato di Milano (images not reproduced)'),
    dict(slug='esp318', label='Espagnol 318', year='1497&ndash;1504', y=1497, place='Naples, Venice, Messina &rarr; Spain', st='partial', stt='keys found, part read',
         title='Espagnol 318 &mdash; five ciphered letters of the Catholic Monarchs, and which keys open them',
         blurb='The oldest item in the catalogue, and four different answers. No.&nbsp;5 was never open: Ivan Parisi printed the whole text in 2020, having found that the king of Naples had his secret letter enciphered in the Spanish ambassador&rsquo;s own cipher, by the ambassador&rsquo;s hand. No.&nbsp;92, the Great Captain to Lorenzo Su&aacute;rez of 17 August 1500, is written in the <em>Cifra general de los Reyes Cat&oacute;licos</em> that Galende D&iacute;az printed in 1994 &mdash; proposed by Tomokiyo from the look of the code groups, proved here against eight words a later hand wrote between the lines, with no misses; the key is transcribed, 683 groups, and the letter is readable. No.&nbsp;95 has George Lasry&rsquo;s alphabet and no published text: segmenting and clustering its 963 signs reads about two thirds, Spanish, about the French and about what a <em>Se&ntilde;or&iacute;a</em> can be brought to do. Nos.&nbsp;93 and 94 stay unread but are named: their code initials exclude both printed keys and point at the <em>Gran cifra</em> of 1501&ndash;04, whose only reconstruction sits in a Madrid manuscript that is not served online.',
         quote='&ldquo;y tiempo, por estar en tanto&rdquo; &middot; the glossator&rsquo;s own words, from the printed key',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='vasto1527', label='Del Vasto 1527', year='1527&ndash;28', y=1527.8, place='Rome and Madrid &rarr; Charles V', st='partial', stt='two of three read',
         title='Del Vasto to Charles V and a letter to &ldquo;Garbino&rdquo;, 1527&ndash;28 &mdash; one found solved, one read, one without its key',
         blurb='Three imperial ciphers in BnF fr. 3022, listed with no decipherment. Del Vasto&rsquo;s letter from Ischia of 27 September 1527 had been solved by George Lasry and Satoshi Tomokiyo. The anonymous &ldquo;report&rdquo; is del Vasto&rsquo;s own letter of December 1527: Lasry had its letters, and about forty of its code groups are identified here, which makes it readable as his plan to march on Siena, Perugia and Urbino. The Madrid letter to &ldquo;Garbino&rdquo; is in Hieronimo Ranzo&rsquo;s initial-letter code. Its numbering is not alphabetical, and without the table only its function words come out.',
         quote='&ldquo;el ex&eacute;rcito por lo de advenir no se puede sostener desta manera&rdquo; &middot; del Vasto, December 1527',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='raince', label='Raince', year='1526', y=1526, place='Rome &rarr; the Court', st='partial', stt='read in part',
         title='Raince to Montmorency, Rome, 1526 &mdash; the key was misread by one column',
         blurb='Eight ciphered despatches of the French embassy&rsquo;s secretary at Rome sit in BnF fr. 2984; about 106 lines of them, the 13 May and 20 November 1526 letters to Montmorency, exist in no edition. The obstacle was never cryptanalytic. Tomokiyo published the key in 2020, but reading which glyph sits under which letter in his table by eye slips a column: <em>l</em>, <em>m</em> and <em>n</em> were each a place wrong, and every reading built on it was corrupt. Measured off the image instead &mdash; every ink blob within 15&nbsp;px of a header column &mdash; the table resolves a control line glyph for glyph with nothing left over, and 86 of the 106 lines then read by hand from the microfilm. Nine days before the League of Cognac: the Castilians and the Bourguignons, <em>le chemin de Valence</em>, a capitulation for which <em>ilz seront cause de la destruction</em>, the plague in Rome, advices reaching the Imperials by their own people, and a man taken <em>un jour, en plaine place pres du palais</em>. Two months after the Colonna raid, a pontificate that <em>seroit la cause de la totale ruine de sa maison</em>. The clear close of 13 May, transcribed here, expects Andrea Doria at Civitavecchia within a day with six galleys.',
         quote='&ldquo;qui estoit en la court de Savoye est party pour venir icy&rdquo; &middot; &ldquo;[le] pontificat seroit la cause de la totale ruine de sa maison&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='sormano', label='Sormano 1529', year='1529', y=1529.2, place='Ferrara &rarr; the Court', st='solved', stt='read',
         title='Sormano and de Vaulx to Fran&ccedil;ois I, February 1529 &mdash; the duke of Ferrara declines the crown of Naples',
         blurb='Three ciphered despatches of the French agents at Ferrara, BnF fr. 3096 nos. 63, 65 and 66, listed unread beside two glossed siblings. Lasry&rsquo;s key holds; the leaves add a null, a nomenclator for the duke and four letter forms. Eighteen thousand signs segmented from the Gallica scans, clustered and classified, then every line read on review sheets; the duplicate pair, which enciphers different stretches, checks itself. Alfonso d&rsquo;Este will not take the kingdom or the captaincy of the French army, and the agents call his difficulties pretexts, eight months before Cambrai.',
         quote='&ldquo;risolutamente concluse per cosa dil mondo non voler per s&eacute; alcunamente accettare il regno et manco far l&rsquo;impresa a suo nome&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='gramont1529', label='Gramont 1529&ndash;37', year='1529&ndash;37', y=1529.8, place='Rome, Venice &rarr; the Court', st='solved', stt='read',
         title='Gramont, M&acirc;con and Langeac to Montmorency, 1529&ndash;1537 &mdash; four keys solved in 2023, four letters never read',
         blurb='Four ciphered letters to the grand ma&icirc;tre from the French ambassadors at Rome and Venice, catalogued with no decipherment. Each has its own key, and Lasry had reconstructed all four from siblings; nobody had applied them. Read: Saint-Pol and the Venetians in January 1529; Clement VII on the council, his dream and his feigned illness on the road to Bologna in October 1529; the princes&rsquo; return in 1530; Paul III and the Farnese marriage in 1537.',
         quote='&ldquo;le concile general, lequel il craignoit sur toutes les choses de ce monde&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='lopehurtado', label='Lope Hurtado 1522', year='1522', y=1522.8, place='Rome &rarr; Charles V', st='partial', stt='cipher broken, four letters read',
         title='Lope Hurtado de Mendoza at Rome, 1522 &mdash; an unpublished cipher broken, four letters read',
         blurb='Nine records in RAH Salazar 9/26, catalogued as part of Alonso S&aacute;nchez&rsquo;s Venice correspondence among which they are bound. They are in a different cipher, and nobody had published it: Tomokiyo&rsquo;s 2025 article covers S&aacute;nchez&rsquo;s and Juan Manuel&rsquo;s and not this. The crib was in the volume &mdash; R9644 and R9650 each carry the clerk&rsquo;s own full contemporary clear version beside the cipher, keyed by marginal letters. Fifty-seven values fixed against that plaintext; the key then reads two thirds of the tokens in records DECODE calls non-decrypted, and reads <i>el papa</i> unaided in a letter with no crib at all. Four of the nine are read complete as to content: Adrian VI temporising between Charles V and Francis I, the French coming into Italy with a great sum of money to Lyon, a Pope too parsimonious to pay his own household.',
         quote='&ldquo;tomalo tan tibiamente que no se espera de todo bien&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='sanchez1522', label='S&aacute;nchez 1522', year='1522', y=1522.5, place='Venice &rarr; Charles V', st='found', stt='already solved; entry corrected',
         title='Alonso S&aacute;nchez at Venice, 1522 &mdash; the cipher was already solved, and the catalogue entry was wrong',
         blurb='Twenty-nine DECODE records (RAH Salazar 9/23&ndash;9/26, R9593&ndash;R9657) held here as unread ciphertexts of the imperial ambassador at Venice. Satoshi Tomokiyo had reconstructed the cipher outright and published it in September 2025, a year before the entry was scored, so there is no break to be had. The entry is corrected instead: the run spans four volumes and not one, every record is dated 1522 so the treaty of July 1523 is not in it, nine of the letters are Lope Hurtado de Mendoza&rsquo;s, and almost all carry a contemporary decipherment. The nomenclator turns out to be alphabetically ordered, which fills in the numeral run; three values so predicted are then confirmed in two letters outside Tomokiyo&rsquo;s coverage, both read in part here: R9653 on the siege of Rhodes, and R9635, a whole page of cipher on the sums owed by the Signoria and the restitution of goods seized from imperial vassals. Lope Hurtado&rsquo;s code groups take finals S&aacute;nchez&rsquo;s key does not have &mdash; a third cipher, still unreconstructed.',
         quote='&ldquo;ducados allende de los otros xviii mil &hellip; mas de xv mil ducados&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='soria1523', label='Soria 1523', year='1523', y=1523.5, place='Genoa &rarr; Charles V', st='partial', stt='read in part',
         title='Lope de Soria to Charles V, Genoa, 1523 &mdash; two ciphers, one broken from a court decipherment and one with no key at all',
         blurb='Eleven DECODE records (RAH Salazar A-28, R9488&ndash;R9498), none deciphered before: five despatches of the imperial ambassador at Genoa, June to August 1523, with their duplicates. The later cipher was rebuilt from a Soria letter that carries the court&rsquo;s decipherment. The earlier one had no key or crib and fell to a substitution solver scored on Castilian of the 1520s. The letters read on the Venetian league, the French descent, a plan to seize Bergamo and Brescia, Siena, Beaurain&rsquo;s mission and Andrea Doria&rsquo;s first approach to the Emperor.',
         quote='&ldquo;los dichos [rip] usaran con [pur] los tratos que uso Otaviano Campofregoso quando se fizo la liga general&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
    dict(slug='sessa1524', label='Sessa 1524', year='1524', y=1524.3, place='Rome &rarr; Charles V', st='partial', stt='read in part',
         title='The Duke of Sessa to Charles V, Rome, 18 April 1524 &mdash; a &ldquo;1424&rdquo; cipher that is a century younger',
         blurb='DECODE catalogues RAH Salazar A-31 ff. 128&ndash;131 as a <em>Non-decrypted</em> letter of Luis Fern&aacute;ndez from Rome, April 1424, and it was taken up as the longest ciphertext before 1450. The date is a typo: the letter is the Duke of Sessa&rsquo;s despatch of 18 April 1524 and its duplicate, skipped by Bergenroth. Eight sibling letters in the same cipher carry the court&rsquo;s decipherment; about 110 code groups and the alphabet were rebuilt from them by token tiling and template matching. The cipher now reads at the word level: the Pope&rsquo;s secretary withholds the Bishop of Veroli&rsquo;s letters, and Sessa asks the Pope for money for the Swiss. Four groups are attested nowhere and stay open.',
         quote='&ldquo;habl&eacute; en la ora a Su Santidad a pedirle que haya provisi&oacute;n &hellip; pues tiene color para ello&rdquo;',
         rights='Manuscript: Real Academia de la Historia, via DECODE'),
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
    dict(slug='rennes1563', label='Rennes 1563', year='1563', y=1563, place='the camp before Le Havre &rarr; the imperial court', st='partial', stt='read in part',
         title='Catherine de M&eacute;dicis to the bishop of Rennes, 31 July 1563 &mdash; the passage La Ferri&egrave;re printed as an empty bracket',
         blurb='BnF fran&ccedil;ais 3181 f. 55: thirteen lines of cipher set between two passages of clear French. La Ferri&egrave;re printed the letter in 1885 and left the block blank with the footnote &laquo;&nbsp;Partie chiffr&eacute;e&nbsp;&raquo;; Tomokiyo, who reconstructed the Bishop of Rennes&rsquo; cipher, lists the folio as undeciphered. Tomokiyo&rsquo;s key was calibrated on this scribe&rsquo;s hand against the sibling letter f. 57, which carries a line-by-line decipherment in its margin and whose first ciphered line reads <em>que les princes</em>. About three fifths of the passage now reads. The enciphered subject is the Council of Trent and the Habsburg marriage &mdash; while the recovery of Le Havre, in the same letter, went in clear.',
         quote='&ldquo;sceu ce que vous avez descouvert&hellip; l&rsquo;avancement du concile&hellip; avoir l&rsquo;utilit&eacute; qui en sortira&rdquo;',
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
    dict(slug='yard1699', label='Yard 1699', year='1699', y=1699, place='Whitehall &rarr; Paris', st='solved', stt='read',
         title='Robert Yard to the Earl of Manchester &mdash; two &ldquo;undeciphered&rdquo; letters of October 1699, read with the key from the same papers',
         blurb='Two letters from the Secretary of State&rsquo;s office to the ambassador at Paris, 12 and 16 October 1699, catalogued at Yale as &ldquo;almost entirely in cipher, undeciphered&rdquo;; the Historical Manuscripts Commission said no key was known. The key was in the same Manchester papers: a printed code sheet with handwritten numbers, <em>the</em> = 454, as Tomokiyo had inferred. Checked on a sibling letter deciphered at the time, it reads both letters group for group, apart from five slips of Yard&rsquo;s pen. Messengers at Dover wait for Mills and Lord Drummond&rsquo;s priest, and Ireland and the north report a design <em>carryed on very privately at Saint Germains</em>.',
         quote='&ldquo;all is said to be carryed on very privately at Saint Germains&rdquo; &middot; Robert Yard, 12 October 1699',
         rights='Manuscript images: Beinecke Rare Book and Manuscript Library, Yale University'),
    dict(slug='nunzio1718', label='Nunziatura di Spagna 1718', year='1718&ndash;20', y=1718.1, place='Rome &rarr; Madrid', st='found', stt='already solved; key extended',
         title='The Secretariat of State to the Nuncio in Spain, 1718&ndash;1720 &mdash; already read by George Lasry, and 61 more nomenclator groups recovered',
         blurb='Twenty-four ciphered despatches of Clement XI&rsquo;s Secretariat to the nuncio at Madrid (ASV Segr. Stato Spagna 364D, DECODE R154&ndash;R177), catalogued here as an unread transcription job behind a login. They were neither. George Lasry reconstructed the key in October 2020 and filed his segmented decipherment of the whole Spagna 364 corpus on every one of the records; measured token by token it reads 97.6 per cent of the 34,243 cipher groups. The gap was the nomenclator, where 189 of the 399 four-digit groups in use carried no value. Because the key is alphabetical in runs, 61 of them are recovered from the brackets and the corpus contexts &mdash; promozione, aggiustamento, giurisdizione, tribunale, vascelli, Vicer&egrave;, corriere &mdash; and the calendar block resolves into two parallel Gennaio&ndash;Dicembre runs, with 4538 Luglio confirmed by the date of Alberoni&rsquo;s promotion.',
         quote='&ldquo;in data delli 12 Luglio passato, qual appunto fu il giorno della promozione del Sig. Card.&rdquo; &middot; group 4538 confirmed',
         rights='Manuscript images: Archivio Apostolico Vaticano, via DECODE'),
    dict(slug='windischgraetz1720', label='Windischgr&auml;tz 1720', year='1720&ndash;22', y=1720.5, place='Vienna &rarr; The Hague', st='solved', stt='read',
         title='Charles VI to Count Windischgr&auml;tz, 1720&ndash;1722 &mdash; the Emperor&rsquo;s secret letters read with the two keys from the same archive',
         blurb='Four autograph letters of Charles VI to his envoy at The Hague, catalogued on DECODE as non-decrypted, with both keys filed beside them: the Chancellery&rsquo;s 977-entry nomenclator and the Emperor&rsquo;s private key of numbers and signs. Transcribed and applied, they read every cipher passage. After Alberoni&rsquo;s fall the Emperor fears a French separate peace with Philip V through Morville, rejects Sardinia for Lorraine, claims the Montferrat equivalent and wants Portugal in the Alliance; in July 1720 Beretti Landi proposes a marriage between his children and Philip&rsquo;s sons.',
         quote='&ldquo;da nun der Alberoni aus Spannien abgeschafft&rdquo; &middot; Charles VI, 3 February 1720',
         rights='Manuscript images: St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE'),
    dict(slug='kauderbach1754', label='Kauderbach 1754', year='1754&ndash;56', y=1755.4, place='The Hague &rarr; Dresden', st='solved', stt='read',
         title='Kauderbach&rsquo;s intercepted despatches from The Hague, 1754&ndash;56 &mdash; an unseparated syllable cipher split and read',
         blurb='Ten Dutch copies of letters of the Saxon-Polish resident to Dresden, with passages in figures that DECODE says were never solved: the figures run on without separation. The digits 5 and 8 turned out to be nulls, the rest two-figure codes for letters and syllables; Kauderbach&rsquo;s 1761 key in Dresden supplied the vocabulary, a one-to-one annealing search the numbers. All ten read: the Dutch quarrel over the augmentation of 1755, Yorke and the Saxon subsidy treaty, and the news of the Treaty of Versailles.',
         quote='&ldquo;Cette nouvelle a caus&eacute; une consternation extraordinaire ici&rdquo; &middot; Kauderbach on the Treaty of Versailles, 25 May 1756',
         rights='Koninklijk Huisarchief, The Hague, and S&auml;chsisches Hauptstaatsarchiv Dresden, via DECODE'),
    dict(slug='affry1757', label='d&rsquo;Affry 1757', year='1757&ndash;58', y=1757.5, place='The Hague &rarr; Versailles', st='solved', stt='read',
         title='The comte d&rsquo;Affry&rsquo;s intercepted letters from The Hague, 1757&ndash;58 &mdash; the code rebuilt from Lyonet&rsquo;s decipherments',
         blurb='Eleven code letters of the French ambassador to Rouill&eacute; and Bernis in the Dutch royal archives, listed on DECODE as unsolved. The Dutch codebreaker Lyonet&rsquo;s decipherments of eight sibling letters were among the images, filed as clear pages; aligned group by group they rebuild the 1,200-group code, which reads nine of the undeciphered letters (the tenth transcribed from the scans). Convoys and herring, the Gouvernante&rsquo;s tears over her father, Ostend and Nieuport, spies for England and a French loan in London; Bussemaker&rsquo;s 1906 extracts recur word for word.',
         quote='&ldquo;faut-il que ce soit moi qui favorise les moyens de faire du mal &agrave; mon p&egrave;re?&rdquo; &middot; the Princess Governess to d&rsquo;Affry, April 1757',
         rights='Koninklijk Huisarchief, The Hague, via DECODE'),
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
    dict(slug='mondoucet', label='Mondoucet', year='1571&ndash;74', y=1572, place='Brussels &rarr; the Court', st='solved', stt='read',
         title='Mondoucet&rsquo;s despatch of 13 July 1572 &mdash; a segmenter, not the archive',
         blurb='A Gallica sweep for volumes outside the standard lists found BnF fr. 16127, the Court&rsquo;s file of Claude de Mondoucet&rsquo;s correspondence from the Low Countries, 1571&ndash;74: about twenty ciphered despatches in one system, most with the Court&rsquo;s decipherment, one long letter of 13 July 1572 without. Four aligners proved on controls had all sat at the shuffled baseline &mdash; not because of the archive but because an automatic glyph segmenter, the one stage never checked against a hand count, split looped d, crossbarred long-s and barred o/q into two components each and manufactured a 1.3&ndash;1.4 glyph-per-letter ratio. At glyph level it is an ordinary sixteenth-century homophonic substitution, one glyph per letter, four nulls. The key was built by hand from the 16 July crib in the same volume &mdash; the decipherer&rsquo;s interlinear glosses on f. 62r and the verbatim reading at f. 64 &mdash; and a French 5-gram beam decoder then read the despatch. The decisive control is internal: decoding the 16 July block reproduces the decipherer&rsquo;s own gloss verbatim. Partly enciphered, its clear bands give Spanish troop counts before Mons and German levies at Maastricht; the cipher carries Mondoucet&rsquo;s reading of the Protestant position four days before Genlis&rsquo;s column was destroyed at Saint-Ghislain and six weeks before St Bartholomew.',
         quote='&ldquo;leur delivrance des espagnols a ce moyen&rdquo; &middot; the recovered key reproduces the decipherer&rsquo;s own gloss',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='bethune', label='B&eacute;thune 1601', year='1601', y=1601, place='Paris &rarr; Rome', st='partial', stt='two of three read',
         title='Henri IV to B&eacute;thune, 9, 10 and 22 November 1601 &mdash; two letters read, and the ceiling on the third measured',
         blurb='Three ciphered letters of the King to his ambassador in Rome, BnF fr. 3484, catalogued &ldquo;avec chiffre&rdquo; with no decipherment. The notice&rsquo;s &ldquo;copie du n&deg; pr&eacute;c&eacute;dent&rdquo; turns out to be the minute of the 10 November letter in clear, and aligning it with the cipher recovers a Villeroy-office key of the design Bazeries printed for B&eacute;thune&rsquo;s brother in 1599: ten thousand &eacute;cus to Cardinal Aldobrandini for the Peace of Lyon. The 22 November letter is now read too &mdash; it interleaves clear French with its cipher, and carries the Camaiano pension, Barberini&rsquo;s coming and the dauphin&rsquo;s baptism. The 9 November letter, a solid page of cipher, stops at about six words in ten, and an oracle bound shows why: the decoder is already past the ceiling its transcription allows.',
         quote='&ldquo;car j&rsquo;affectionne led. Cardinal et desire m&rsquo;acquitter de lad. promesse que je luy ay faicte&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='norfolk1570', label='Mary to Norfolk', year='1570', y=1570.1, place='Tutbury &rarr; the Tower', st='solved', stt='read',
         title='Mary Queen of Scots to the Duke of Norfolk, &ldquo;the 20th&rdquo;, February or March 1570 &mdash; the one letter of the series never deciphered',
         blurb='BL Cotton MS Caligula C II f. 74r is the only letter of Mary&rsquo;s ciphered correspondence with Norfolk in the Tower with no contemporary decipherment, dated only &ldquo;the tventi of this instant&rdquo;. Tomokiyo rebuilt the key from the three deciphered siblings and overlaid a partial letter-by-letter decode. Here the key is checked on f. 66r, and the letter is read in 23 lines from the new British Library IIIF images, stitched from tiles. Written weeks after the Regent Moray&rsquo;s murder: Elizabeth blames Mary for the harquebus shot, Morton is rumoured on the move, and Norfolk is to write through the Bishop of Ross or Lady Scrope, never in his own hand.',
         quote='&ldquo;I am asured that sche &hellip; sueves me the veyt of Murray death; but God knoueth&rdquo;',
         rights='Manuscript images: British Library'),
    dict(slug='lanssac', label='Lanssac', year='1573', y=1573, place='Warsaw &rarr; Paris', st='solved', stt='read',
         title='Lanssac to Charles IX, Warsaw, 26 April 1573 &mdash; the Polish election embassy&rsquo;s cipher',
         blurb='BnF fr. 4735 f. 124, catalogued &ldquo;avec chiffre&rdquo; with no decipherment. The key is a homophonic letter cipher with word signs, recovered from a sibling letter whose Court decipherment survives as gutter-cut marginal notes (&ldquo;car je n&rsquo;ay pas cinquante escuz&rdquo;) and checked against the fragments on f. 124 itself. Both passages read, and the key then opens the three election letters whose only &ldquo;decipherment&rdquo; was that cut gloss: the Polish nation &ldquo;autant v&eacute;nale &hellip; comme sont les Allemans&rdquo;, the Emperor&rsquo;s three hundred thousand spent for nothing, and on 9 May the election carried against the Sultan, the Emperor, the princes of the Empire, Spain, Muscovy and Sweden, &ldquo;qui tous estoient bandez contre vostre Majest&eacute;&rdquo;. Tomokiyo&rsquo;s published table for the cipher is corrected.',
         quote='&ldquo;qui tous estoient bandez contre vostre Majest&eacute;&rdquo; &middot; P&#322;ock, 9 May 1573',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
    dict(slug='pelissier1592', label='Pelissier 1592', year='1592', y=1592.7, place='Burgos &rarr; France', st='solved', stt='read, gaps marked',
         title='Pelissier to Jeannin, Burgos, 13 September 1592 &mdash; the League&rsquo;s agent at Philip II&rsquo;s court',
         blurb='Nine pages, mostly in cipher, that Tomokiyo lists as only partially deciphered: the League&rsquo;s agent in Spain reporting to Mayenne&rsquo;s councillor four months before the Estates of 1593. Tomokiyo&rsquo;s key for Pelissier&rsquo;s later letters fits; calibrated on 1,764 signs of those letters aligned with their clear text, it reads 94&nbsp;% of the ciphered words, every gap marked. Philip grants 500 ducats, Pelissier argues against holding the Estates now and for two armies at 300,000 &eacute;cus a month, and reports the case being made in France for Navarre.',
         quote='&ldquo;la nomination d&rsquo;un roy legitime pour l&rsquo;opposer a l&rsquo;heretique et tyran&rdquo;',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
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
    dict(slug='orbais', label='Orbais 1589', year='1589', y=1589.65, place='Rome &rarr; Paris', st='partial', stt='read in part',
         title='A letter from Rome to the abb&eacute; d&rsquo;Orbais, 23 August 1589 &mdash; the three keys bound with it do not fit',
         blurb='BnF fr. 3413 no. 62 was catalogued with three cipher keys bound in the same volume that might read it. None does. The letter, from a secretary of Cardinal Pellev&eacute; in Rome to Jean de Piles of the League&rsquo;s council in Paris, is almost all in clear and carries the news of Henri&nbsp;III&rsquo;s murder as it reached Rome. Its ninety-odd signs of cipher are in the Nevers&ndash;Piles alphabet that Tomokiyo identified. His partial table was filled out from a deciphered letter of 1586 in fr. 4715 in the same cipher. Read: <em>Cassin</em>, <em>la protection</em>, <em>vostre regne</em>, <em>depeschera</em>, <em>mon maitre a est&eacute; retir&eacute;</em>, and the signature, probably <em>Baron</em>. About thirty signs, most of them code signs, remain open.',
         quote='&ldquo;le Roy a est&eacute; tu&eacute;, et c&rsquo;est le Roy de Navarre qui l&rsquo;a faict faire&rdquo;',
         rights='Manuscript images: Biblioth&egrave;que nationale de France'),
    dict(slug='lorraine1592', label='Lorraine 1592', year='1592', y=1592, place='Nancy &rarr; Vaud&eacute;mont', st='partial', stt='key recovered, read in part',
         author='Arya Sanketbhai Patel',
         title='Charles III of Lorraine to Vaud&eacute;mont, 18 June 1592 &mdash; a cipher catalogued as undecrypted, broken',
         blurb='BnF Fran&ccedil;ais 3621 no. 97, recorded in the DECODE database as <em>Non-decrypted</em>, with no key ever published and no crib in the volume: the January intercepts it was hoped to match exist only as a plaintext decipherment. An earlier attempt failed by treating it as a symbol cipher and clustering the glyphs by shape. They are <strong>ordinary cursive letterforms</strong> and can simply be read. The old solver was then shown, on controls with known keys, to be incapable of a cipher this size &mdash; 37&ndash;56% of letters at &minus;2.64 where the true key scored &minus;1.62 &mdash; and was replaced by a steepest-ascent search that recovers known keys at 98.7&ndash;99.6%. The key it found is verified against the manuscript, not the model: the group spelling <em>chasteau</em> occurs twice in the cipher, and Chasteauvillain stands in the clear on the same page. The Duke orders his son to conserve the plain and to bring the army back into the quarters of La Fauche.',
         quote='&ldquo;ramener mon arm&eacute;e &hellip; es quartiers de la Faulche&rdquo; &middot; DECODE 9449: Non-decrypted',
         rights='Manuscript rights: Biblioth&egrave;que nationale de France'),
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
IMAGES = {'throckmorton': None, 'hellen1752': None, 'beatrice1482': None, 'rennes1563': ('rennes1563_lead.jpg', 'BnF français 3181 f. 55: the clear address and first sentence, then the thirteen lines of cipher that La Ferrière printed as an empty bracket', 'Bibliothèque nationale de France'), 'sessa1593': ('sessa1593_lead.jpg', 'BnF Fran\u00e7ais 3995 f. 97: the Spanish office key, the letter alphabet across the top and the syllable table beneath, identical to Tomokiyo\u2019s reconstruction', 'Biblioth\u00e8que nationale de France'), 'maisse1592': ('maisse1592_lead.jpg', 'BnF Fran\u00e7ais 16093 f. 370, Henri IV to Maisse, 3 November 1592: six lines of clear French breaking off at ou la plus part des lettres se perdent, then some twenty-five lines of figures', 'Biblioth\u00e8que nationale de France'), 'sp106box10': ('sp106box10_lead.jpg', 'DECODE R725 p. 3 (SP 106/10 f. 205), the codebreaker&rsquo;s fair key: the letter alphabet, the letters that stand for whole words, and the two word-lists selected by a bar or a tick over the figure', 'The National Archives, Kew, via DECODE R725'), 'nunzio1718': None, 'ceva1632': None, 'pallotto1629': ('pallotto1629_lead.jpg', 'Barb.lat. 6960 p. 5: the clear heading Di Vienna 4 di Agosto, a struck-out opening line, then the unbroken figures of the despatch Kiewning printed as Nr. 153', 'Biblioteca Apostolica Vaticana'), 'kauderbach1754': ('kauderbach1754_lead.jpg', 'R2078, the copy of Kauderbach&rsquo;s letter of 23 December 1754: clear French, then the unseparated figures, 9332131922&hellip; = il n&rsquo;y a pas eu depuis longtems', 'Koninklijk Huisarchief, via DECODE'), 'affry1757': ('affry1757_lead.jpg', 'No. 171, 26 April 1757: the intercept in figures beside Lyonet&rsquo;s clear copy, J&rsquo;ai l&rsquo;honneur de vous addresser la copie d&rsquo;une lettre', 'Koninklijk Huisarchief, via DECODE'), 'acciaiuoli1757': ('acciaiuoli1757_lead.jpg', 'Portogallo 117/6 f. 106r, 24 October 1758: the decipherment made in Rome written above the figures, Benche si dica il R&egrave; assai meglio', 'Archivio Apostolico Vaticano, via DECODE R199'), 'kurtz1639': ('kurtz1639_lead.jpg', 'Kurz to Trauttmansdorff, Hamburg 17 January 1639 (R3811), first page: numbers with a contemporary decipherment written small above them', 'St&aacute;tn&iacute; oblastn&iacute; archiv v Plzni, via DECODE R3811'), 'lopehurtado': ('lopehurtado_lead.jpg', 'RAH Salazar 9/26 f. 237, Lope Hurtado&rsquo;s ciphered letter of 1 November 1522: clear Spanish and three-letter code groups alternating inside the sentence, with the section letter A in the margin keying it to the clerk&rsquo;s clear version on f. 241', 'Real Academia de la Historia, via DECODE R9644'), 'sanchez1522': ('sanchez1522_lead.jpg', 'RAH Salazar 9/26 f. 299r, S&aacute;nchez to Charles V, 20 November 1522: a ciphered paragraph at the head, the news of the siege of Rhodes in clear, and two ciphered lines above the signature', 'Real Academia de la Historia, via DECODE R9653'), 'soria1523': None, 'hm1645': None, 'balbases1677': ('balbases1677_lead.jpg', 'Balbases to Fuenmayor, 3 August 1677 (R985): the cipher block and its contemporary decipherment in the left margin', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, SEG 2559, via DECODE R985'), 'morosini1588': ('morosini1588_lead.jpg', 'Francia 22 f. 308r, the head of the despatch of 23 December 1588, docketed dup.to di 23 Decembre: the figures that report the murder of the Duke of Guise', 'Archivio Apostolico Vaticano, via DECODE R43'), 'sp106r927': ('sp106r927_lead.jpg', 'TNA SP 106/10 f. 243, the last lines turned to the writer&rsquo;s orientation: et vous supplie tres humblement, monsieur, me continuer l&rsquo;honneur de vostre bienveuillance', 'The National Archives, Kew, via DECODE R927'), 'michell1751': ('michell1751_lead.jpg', 'The Hague copy of Frederick II&rsquo;s letter to Michell, 28 December 1751: the clear opening, then the code from 1555 1550 (et suis)', 'Koninklijk Huisarchief, The Hague, via DECODE R1957'), 'carpio1677': ('carpio1677_lead.jpg', 'Carpio to Fuenmayor, 4 September 1677 (R1010): the cipher with its decipherment in the left margin, &ldquo;La Armada de Francia sali&oacute; de Mecina&hellip;&rdquo;', 'Archives g&eacute;n&eacute;rales du Royaume, Brussels, via DECODE R1010'), 'windischgraetz1720': ('windischgraetz1720_lead.jpg', 'Register copy of Charles VI’s letter of 3 February 1720, book 5 p. 402: clear German with runs of nomenclator numbers, den Pentenrider and Argwohn machen von Frankreich und dem Regenten', 'Státní oblastní archiv v Plzni, via DECODE R5020'), 'matthias1482': None, 'sadoleto1482': ('sadoleto1482_lead.jpg', 'ASMo Ambasciatori Ungheria b. 1/9 no. 8, Sadoleto to Ercole, Pozsony 16 July 1482: the seven cipher lines, from essendo in Buda to cento milia', 'Archivio di Stato di Modena, via DECODE R1102'), 'buda1489': ('buda1489_lead.jpg', 'ASMi Sforzesco 650, the letter of 22 November 1489: the clear address La Ex.tia vra and the first lines of cipher, intende ad quali termine la pratica de pace', 'Archivio di Stato di Milano, via Vestigia'), 'sessa1524': None, 'florence1429': ('florence1429_lead.jpg', 'ASF Dieci di Balìa, Responsive 2 no. 171: Galeotto da Ricasoli’s letter from Urbino, with Gabbrielli’s 1863 glosses between the lines', 'Archivio di Stato di Firenze, via DECODE R3754'), 'maria1435': ('maria1435_f59r_letter.jpg', 'ACA Cancillería reg. 3225 f. 59r, the queen’s letter to Alfonso V of 5 August 1435: three runs of signs in the first four lines of the clear Catalan', 'Arxiu de la Corona d’Aragó, via DECODE R10171'), 'heidelberg597': ('heidelberg597_lead.jpg', 'Cod. Pal. germ. 597 f. 1r: the compiler’s alphabet written as one unbroken run of signs and struck through, then vnd ich in clear and the signs for hab es', 'Universitätsbibliothek Heidelberg'), 'lorraine1592': ('lorraine1592_f109_cipher.jpg', 'BnF Fran\u00e7ais 3621 f. 109, a line of the cipher: ordinary cursive letterforms, opening with the group that spells chasteau', 'Biblioth\u00e8que nationale de France'), 'reserva12': ('reserva12_block1.jpg', 'ACA Reserva 12, the first lines of the strip: Senyor jous / pus compli / escriua ja, to be read down the columns of the block', 'Arxiu de la Corona d’Aragó, via DECODE R10170'), 'orbais': ('orbais_f126v_depeschera.jpg', 'BnF fr. 3413 f. 126v, to the abbé d’Orbais, 23 August 1589: Les jugemens de Dieu sont fort profons et inscrutables, then the cipher signs of depeschera, dedans deux jours', 'Bibliothèque nationale de France'), 'clair357': ('clair357_f167r_glosses.jpg', 'BnF Clairambault 357 f. 167r: two-digit figures with the 1586 decipherer’s words written between the lines, Fumé, visadmiral, du Roy de Navarre', 'Bibliothèque nationale de France'), 'breves1603': ('breves1603_key_leaf.jpg', 'BnF fr. 3462 f. 103, the key of Savary de Brèves for 1602–03: persons in the left column, the alphabet across the top, the nomenclator below, doubles and nulls at the foot on the right', 'Bibliothèque nationale de France'), 'pelissier1592': ('pelissier1592_f46r_head.jpg', 'BnF Français 3982 f. 46r, Pelissier to Jeannin, Burgos, 13 September 1592: the clear opening and the first rows of cipher, with the decipherer’s scattered glosses', 'Bibliothèque nationale de France'), 'soglia1848': ('soglia1848_block_head.jpg', "The Roman reprint of L'Italia del Popolo, 30 June 1848: the clear opening of Cardinal Soglia's dispatch and the first lines of digits, 5 the word break, 8XXX the code", 'Tony Gaffney, via Klaus Schmeh, Cipherbrain'), 'vich1511': ('vich1511_n46_cipher_decipher.jpg', "AHN Estado 8715 N.46, 5 July 1511: the opening lines of the cipher above the opening of the clerk's decipherment, Con beltran de cordona que partio de Sevilla a xvj de junio", 'Archivo Histórico Nacional (PARES)'), 'norfolk1570': ('norfolk1570_f74r_lines.jpg', 'BL Cotton MS Caligula C II f. 74r, the left half of the first five cipher lines of Mary to Norfolk, the 20th [1570]: I have, my oun good lord', 'British Library'), 'orpo1942': ('orpo1942_redform.jpg', 'W/T Red Form from intercept station 51 for the Mogilev message of 16 June 1942, with the discriminator ARTTN and the first cipher groups', 'NARA, RG 457, HCC, Box 202, via Weierud (CryptoCellar, 2020)'), 'legation': ('legation_no88.jpg', "NARA M35 reel 3 frame 0206, No. 88 of 25 June 1812: the clerk's pencil decode above the code groups stops where Ford's nine undecyphered lines begin", 'National Archives and Records Administration'), 'sunintercepts': ('sunintercepts_tenkiutai.jpg', 'Dai Jitao to Sun Yat-sen, 26 March 1917: condenser words on the received-message form, signed Tenkiutai; the last word ends in the rhyme code for the 26th', 'JACAR'), 'adrian1521': ('adrian1521_f1r_head.jpg', 'AGS Estado leg. 8 no. 150, f. 1r: the address, the clear opening and the first cipher lines, where Gredilla read the death of the King of England', 'Archivo General de Simancas, via PARES'), 'toledo1565': ('toledo1565_f1r_lead.jpg', "AGS Estado leg. 1394 no. 247 f. 1r, the first lines of García de Toledo's letter of 16 July 1565, figure runs inline in the clear Spanish, among them seiscientos soldados and en tiera", 'Archivo General de Simancas (PARES)'), 'yard1699': ('yard1699_oct12.jpg', 'Yard to Manchester, Whitehall, 12 October 1699, p. 1: runs of figure groups set inside the clear English', 'Beinecke Rare Book and Manuscript Library, Yale University'), 'sormano': ('sormano_f121r_head.jpg', 'BnF fr. 3096 f. 121r, the head of no. 66 with the docket duplicata, the clear opening and the first cipher runs', 'Bibliothèque nationale de France'), 'esp318': ('esp318_f116r_gloss.jpg', 'BnF Espagnol 318 f. 116r, two ciphered lines with a later hand carrying a partial decipherment written small between them', 'Bibliothèque nationale de France'), 'gramont1529': ('gramont1529_f45r_head.jpg', 'BnF fr. 3091 f. 45r, the clear opening of Gramont to Montmorency, 11 October 1529, and the first lines of the five pages of cipher', 'Bibliothèque nationale de France'), 'raince': ('raince_p30_lines.jpg', "BnF fr. 2984 p. 30, the first three lines of the second ciphered page of the letter of 13 May 1526", 'Bibliothèque nationale de France'), 'richelieu': None, 'bethune': ('bethune_f34.jpg', 'BnF fr. 3484 f. 34r, the first enciphered passage of Henri IV to Béthune, 10 November 1601', 'Bibliothèque nationale de France'), 'feuquieres': ('feuquieres_p283.jpg', 'Mémoires de Catinat 1819, vol. II p. 283, the ciphered despatch', 'Bayerische Staatsbibliothek'), 'urquhart': None, 'mondoucet': None, 'nevers1593': ('nevers1593_f209_lines.jpg', 'BnF Français 3985 f. 209, the copy of Nevers to Pisany of 8 September 1593, figures inside the clear text', 'Bibliothèque nationale de France'), 'mendoza1589': ('mendoza1589_f14.jpg', 'BnF Français 3641 f. 14, the copy made by the 1589 decipherer of letter A, with the unread code groups underlined and listed in the margin', 'Bibliothèque nationale de France'), 'herbault1626': ('herbault1626_f73r.jpg', 'BnF Français 3669 f. 73r, figure cipher with the 1626 decipherment written under each line', 'Bibliothèque nationale de France'), 'sormano1529': ('sormano1529_f124.jpg', 'BnF Français 3096 f. 124r, four lines of cipher with the contemporary decipherment down the margin', 'Bibliothèque nationale de France'), 'hesse1603': ('hesse1603_p310.jpg', 'Rommel 1840, p. 310, a page of the King\'s letter of 20 May 1606 in figures', 'Internet Archive'), 'catinat1691': ('catinat1691_p320.jpg', 'Mémoires de Catinat 1819, vol. II p. 320, the start of the King\'s letter of 14 September 1691 in figures', 'Bayerische Staatsbibliothek'), 'ormonde': ('ormonde_p28.jpg', 'Page of the Maltravers to Ormonde cipher letter, 1634', 'Ormonde manuscripts'), 'vatican': ('vatican_meister176.jpg', 'Meister 1906, page 176: the Farnese chancery keys of 1539 to 1542, including the last cipher with Poggio', 'Meister, Die Geheimschrift, 1906, via the Internet Archive'), 'lucca': None, 'boswell': None, 'forster': None, 'warsaw': None, 'hyde': ('hyde_p396.jpg', 'Page 396 of the Life of Barwick, 1724, with the ciphered superscription', 'Life of Barwick, 1724'), 'armstrong': ('armstrong_ps.jpg', 'The coded postscript of Armstrong to Madison, 30 August 1808', 'Founders Online'), 'debosnys': ('debosnys_verse.png', 'Debosnys cipher poem in his invented script, 1883', ''), 'sunyatsen': ('sunyatsen_telegram.png', 'The Swatow telegram to Sun Yat-sen, 3 April 1916', 'JACAR'), 'huangxing': ('huangxing_telegram.png', 'Telegram from Huang Xing, 25 May 1916', 'JACAR'), 'adfgvx': None, 'goldbar': ('goldbar_bar.jpg', 'One of the seven Chinese gold bars with its Latin-letter strings', 'IACR'), 'roosevelt': ('roosevelt_fig2.jpg', 'The Roosevelt letter of 1935: three lines of digits, the letter lines, a skull and crossbones and a dagger through a boot', 'The Friedman Legacy, NSA 1992, Internet Archive scan'), 'copenhagen': ('copenhagen_note.jpg', 'The Copenhagen cryptogram: three lines of digits, letters and strokes', 'Scan published by Klaus Schmeh, Cipherbrain, 2015'), 'scorpion': ('scorpion_s1.jpg', 'Scorpion cipher S1, 70 symbols in a 10 by 7 grid, 1991', 'FBI release via Oranchak and Schmeh'), 'voynich': ('voynich_f34r.jpg', 'Voynich manuscript, folio 34r: a herbal page with four paragraphs of Voynichese', 'Beinecke MS 408, public domain, via Wikimedia Commons'), 'famous': None, 'solved': None}

IMAGES['charlesixducroc'] = ('charlesixducroc_lead.jpg', 'Charles IX to Philibert du Croc: the main letter in graphic cipher, with the signature and postscript lower on the leaf', 'Archives d&eacute;partementales de la Ni&egrave;vre, reproduced by Destray (1924), via Gallica and DECODE R2789')

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
        f'    <a href="index.html#recent">Latest</a>\n'
        f'    <a href="catalogue.html"{" aria-current=\"page\"" if current == "catalogue" else ""}>Catalogue</a>\n'
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
                    f'<span class="t">{p["title"]}</span>{when_html(p, cls="dt")}<span class="yr">{p["year"]}</span>'
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

def card_html(p):
    im = IMAGES.get(p['slug'])
    thumb = f'    <img class="thumb" src="{im[0]}" alt="" loading="lazy">\n' if im else ''
    return (f'  <a class="card{" hasthumb" if im else ""}" href="{p["slug"]}.html">\n' + thumb +
            f'    <div class="eyebrow"><span>{p["place"]} &middot; {p["year"]}</span>{when_html(p)}<span class="st {p["st"]}">{p["stt"]}</span></div>\n'
            f'    <h3>{p["title"]}</h3>\n    <p>{p["blurb"]}</p>\n    <p class="quote">{p["quote"]}</p>\n    <span class="go">read &rarr;</span>\n  </a>\n')

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
    # versions, anchor for "Top", script
    s = re.sub(r'<link rel="stylesheet" href="style.css[^"]*">', f'<link rel="stylesheet" href="style.css?v={VERSION}">', s)
    if 'href="style.css' not in s: s = s.replace('</head>', f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>', 1)
    s = re.sub(r'<script src="site.js[^"]*"></script>\s*', '', s)
    s = s.replace('</body>', f'<script src="site.js?v={VERSION}"></script>\n</body>', 1)
    s = re.sub(r'<body(?![^>]*id=)', '<body id="top"', s, count=1)
    if slug == 'index':
        s = fold_findings(s)
        FEATURED =['raince', 'hesse1603', 'catinat1691', 'voynich', 'feuquieres', 'armstrong', 'lucca', 'warsaw', 'richelieu', 'sunyatsen']
        feat = [next(p for p in PAGES if p['slug'] == f) for f in FEATURED]
        rest = sorted([p for p in PAGES if p['slug'] not in FEATURED], key=lambda p: ({'solved': 0, 'found': 1, 'partial': 2, 'stuck': 3}[p['st']] if p['slug'] not in ('famous', 'solved') else 4, -p['y']))
        rows = ''.join(f'  <li><a href="{p["slug"]}.html"><span class="st {p["st"]}">{p["stt"]}</span><span class="t">{p["title"]}</span>'
                       f'{when_html(p, cls="dt")}<span class="yr">{p["year"]}</span></a></li>\n' for p in rest)
        cards = ('<!-- cards:start -->\n<div class="cards">\n' + ''.join(card_html(p) for p in feat) + '</div>\n'
                 '<h3 class="listhead">And the rest</h3>\n<ul class="list">\n' + rows + '</ul>\n'
                 f'<p class="allws"><a href="writeups.html">All {len(PAGES)} write-ups, filterable by outcome and period, '
                 f'with the results that are still only in the notes &rarr;</a></p>\n<!-- cards:end -->')
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

if __name__ == '__main__':
    for f in sorted(HERE.glob('*.html')):      # date every page before any menu is built: the menu lists the newest
        page_dates(f.stem, f.read_text(encoding='utf-8').lstrip('﻿'))
    (HERE / 'writeups.html').write_text(writeups_html(), encoding='utf-8')
    done = [process(p) for p in sorted(HERE.glob('*.html'))]
    save_dates(DATES)
    print('search index:', write_search_index(), 'entries')
    print('built', ', '.join(done))
