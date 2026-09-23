"""Install this target's reviewed reading on the existing repository site."""
from pathlib import Path
from html import escape
import json,re
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
HERE=ROOT/'memoire1560'; DOCS=ROOT/'docs'; slug='memoire1560'
def read(p):return p.read_text(encoding='utf8')
def write(p,s):p.write_text(s,encoding='utf8')
def dump(p,obj):write(p,json.dumps(obj,ensure_ascii=False,indent=1)+'\n')
def add_after(s,marker,addition):
    assert marker in s,marker
    return s.replace(marker,marker+addition,1)
for name,src,box in [
 ('lead','pages/f152r.jpg',(540,130,3400,1200)),
 ('margin','pages/f153r.jpg',(0,2170,730,2660)),
 ('dorse','img/c159_dorse_r.jpg',None),
]:
    im=Image.open(HERE/src)
    if box:im=im.crop(box)
    im.thumbnail((1100,700))
    im.convert('RGB').save(DOCS/f'{slug}_{name}.jpg',quality=86,optimize=True)

rows=[l.split('\t',1) for l in read(HERE/'reading_working.tsv').splitlines() if l and not l.startswith('#')]
parts=[]
for fol in dict.fromkeys(l.split('.')[0] for l,t in rows):
    label='157v — presumed dorse' if fol=='157v' else fol
    body='\n'.join(f'<tr><td>{escape(l)}</td><td>{escape(t)}</td></tr>' for l,t in rows if l.startswith(fol+'.'))
    parts.append(f'<h3 id="f{fol}">{label}</h3><table class="reading"><thead><tr><th>Line</th><th>Editorial reading</th></tr></thead><tbody>{body}</tbody></table>')
page='''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mémoire en chiffre, 12 December 1560 — Read with uncertainties</title>
<meta name="description" content="A ten-page cipher report on unrest in the Agenais, BnF français 3157 no. 67. Full normalized editorial reading with seven small uncertainties; partial alphabet and no independent clear copy.">
<link rel="stylesheet" href="style.css">
<style>.reading td:first-child{width:6.5em;white-space:nowrap;color:var(--muted,#666);font-size:.85em}.reading td{vertical-align:top}.reading td:last-child{line-height:1.6}.reading{width:100%}</style>
</head><body>
<!-- site:nav -->
<section class="hero">
<p class="kicker">Agenais → Montmorency? · letter substitution and word signs · 12 December 1560 · editorial reading</p>
<h1>“Mémoire en chiffre du XIIe décembre 1560”</h1>
<p class="sub">BnF français 3157 no. 67, ff. 152r–156v. An unnamed writer reports preaching, armed gatherings, suspect officials and threats to his own life.</p>
<p class="sub">Ten pages, a marginal addition and a cipher endorsement read through a partial reconstructed key and image comparison. Seven small passages remain bracketed. The text is normalized; the alphabet is not completely recovered.</p>
<p class="meta">Daniel Bourdeau</p></section>
<main>
<div class="callout"><strong>Summary.</strong> This report is headed “Du XIIe decembre 1560”, a date confirmed on the image.
The writer addresses “vostre grandeur”; Montmorency is a likely recipient, not an explicit deciphered address.
The report describes Protestant preaching, an assembly of about two thousand men at Clairac, and allegations that nobles and officials conceal the situation from the king.
It criticizes Biron, describes threats by Lioux, and closes with a complaint against the writer’s neighbour, Fumel.
The present reading continues an earlier local project attempt, whose transcription, solver and partial key were already available.
Every body page was reviewed, the first five pages received a continuous reading, the final five were revised, and an omitted marginal addition was recovered.
<strong>Conservative editorial coverage is 8,071 of 8,262 transcribed sign units, or 97.688%:</strong> every sign on each of the seven doubtful lines is excluded, even where most of that line reads.
This is a measure of reconstructed textual coverage, <em>not independently established decryption accuracy</em>.
No contemporary decipherment, original codebook or other independent plaintext has been found.</div>

<h2 id="document"><span class="num">01</span> The manuscript</h2>
<p>The body occupies ten written sides, ff. 152r–156v. Gallica view 153 shows f. 152r on the right;
views 154–157 each show two cipher pages, and view 158 shows f. 156v on the left.
The collection’s item number 67 is not a folio number. A presumed dorse, f. 157v on view 159,
has the cipher word <em>Advertissemens</em> and a later clear annotation, <em>henry second</em>.
That later annotation conflicts with the dated heading and is not used to change the date.</p>
<p>The writer says that Fumel is “mon prochain voisin” and names “le sieur de Montluc” in the third person.
Neither detail securely identifies him. The “chief” and the expected “prince” remain unnamed in the reading;
identifying them with a particular historical figure would require additional evidence.</p>
<figure data-credit="Bibliothèque nationale de France, français 3157, f. 153r, Gallica btv1b90598645 view 154">
<img src="memoire1560_margin.jpg" alt="Three short cipher lines in the left margin of f. 153r" loading="lazy">
<figcaption>The marginal addition: <em>assemblez en la chambre du conseil</em>. This was missing from the inherited transcription.
</figcaption></figure>

<h2 id="content"><span class="num">02</span> What the writer reports</h2>
<p>The opening says that affairs have gone “de mal en pis”: preaching and assemblies continue, sometimes with two preachers where there had been one.
The writer names noblewomen attending the sermons, says that rebels hope to gain time and foreign support, and reports an armed gathering at Clairac.
He alleges that the Caulmont family shelters ministers and assemblies. Reclus and Boissonade, sent to court for the Agenais,
are said to be concealing the truth, with support from the local magistrates.</p>
<p>The central pages concern Biron’s raising and dismissing soldiers, rebel captains at Nérac, and the proposed examination of those captains.
Lioux, described as Montluc’s brother, is accused of threats. The writer says he dares leave his house only at night and considers withdrawing to court.
He forwards a religious composition called an edict made by God the Father, a letter from an Agen townsman, and a letter from the keeper of the seals at Cahors.
He also reports hopes of aid from an unnamed prince and foreigners near Geneva and the Swiss cantons.
These are the author’s reports and allegations; the cipher reading alone does not establish their truth.</p>

<h2 id="reading"><span class="num">03</span> Full normalized French reading</h2>
<p>Manuscript line numbers are retained. The line marked <strong>153r.14m</strong> is the marginal addition.
Spelling, punctuation, word boundaries and u/v–i/j are lightly normalized. This is an editorial reconstruction, not a diplomatic edition or the automatic output of a complete key.
Unbracketed text has grade <strong>I</strong> (inferred from the partial substitution, image and context);
bracketed passages have grade <strong>M</strong> (uncertain). <strong>[..]</strong> retains a mark whose function is unresolved.
There are no primary-key-confirmed H or independent-plaintext-confirmed C grades.</p>
<!-- FULL_READING -->

<h2 id="method"><span class="num">04</span> Method and the partial key</h2>
<p>The earlier project attempt transcribed the ten pages and used a French language model in an annealing solver.
Its notes record that a one-sign-per-letter treatment failed, then that repeated compound units and common words provided the first readable passages.
This continuation used that work explicitly. It did not independently rediscover the initial key.</p>
<p>Repeated groups support, for example, <code>T zo x</code> → <em>que</em>, <code>W x m</code> → <em>les</em>,
and <code>h x</code> → <em>de</em>. The inherited ASCII names stand for manuscript shapes, not literal Latin letters.
Short word signs include <em>roy</em> and <em>pour</em>. Several apparent homophones are still entangled with transcription inconsistencies:
the same ASCII label sometimes represents different looped shapes or crosses. Consequently the partial decoder still produces corrupt words
where the images and linguistic context permit an editorial reading. Its output is preserved, not silently replaced by the normalized prose.</p>
<p>Regional enlargements resolved the former blanks <em>Si ainsi estoit</em>, <em>qu’ils sement</em> and <em>pour oster le menu peuple</em>, among others.
A horizontal line filler on f. 155v had been mistaken for the word code <em>pour</em>.
The local copy of George Lasry’s Charles IX–du Croc table was inspected and did not match the target’s assignments.
The Henri II tables could not be retrieved: the source site returned HTTP 503. <strong>No successful Henri II table test is claimed.</strong></p>
<p>The coverage count uses the inherited transcription’s longest-first sign units, including compound ASCII labels as single units.
It includes the new margin and endorsement and excludes the misread filler. It is a reproducible editorial count, not a definitive census of every distinct graphic sign.
All 191 units on the seven bracketed lines are conservatively marked unresolved, giving 8,071/8,262.
The exact independently validated symbol-recovery rate is unknown.</p>

<h2 id="gaps"><span class="num">05</span> Seven small uncertainties</h2>
<ul>
<li><strong>152r.12:</strong> the name tentatively read <em>Montseuignac</em>. Enlarged signs support this reading, but its exact spelling and historical identification are unconfirmed.</li>
<li><strong>152r.15, 152v.21, 152v.26, 153r.10:</strong> short connected groups. The sentence meanings support plural-pronoun or relative expansions; exact <em>ils / qui / qu’ils</em> distinctions remain unconfirmed.</li>
<li><strong>153r.17:</strong> a possible negative in <em>pour n’irriter le roy</em>. The sense supports it; the exact initial sign remains doubtful.</li>
<li><strong>153v.08:</strong> a small mark beside a canceled group, possibly a further cancellation remnant. It has not been silently discarded.</li>
</ul>
<p>Every residual was retried against enlarged images and repeated forms. The reading offers the whole narrative;
it does not supply a completely recovered alphabet, an independently checked plaintext, or proof that no earlier reading exists anywhere.</p>
<figure data-credit="Bibliothèque nationale de France, français 3157, presumed f. 157v, Gallica btv1b90598645 view 159">
<img src="memoire1560_dorse.jpg" alt="Later clear endorsement henry second beside the cipher word Advertissemens" loading="lazy">
<figcaption>The presumed dorse: the cipher reads <em>Advertissemens</em>. The later clear note reads <em>henry second</em>.
</figcaption></figure>

<h2 id="sources"><span class="num">06</span> Sources and reproducible files</h2>
<ul>
<li>Bibliothèque nationale de France, français 3157 no. 67: <a href="https://gallica.bnf.fr/ark:/12148/btv1b90598645/f153.item">Gallica, opening at f. 152r</a>;
<a href="https://gallica.bnf.fr/ark:/12148/btv1b90598645/f159.item">presumed dorse, view 159</a>.</li>
<li><a href="https://portail.biblissima.fr/fr/ark%3A/43093/mdata92e9604a5a6f5abe2a59a35db669d7c3973cf899">Biblissima catalogue description of français 3157</a>, including item 67.</li>
<li>Satoshi Tomokiyo, <a href="https://cryptiana.web.fc2.com/code/GL.htm">George Lasry’s Solutions of Unsolved Ciphers</a>:
the local archived Charles IX table, dated 25 May 2022, was checked. Online Henri II material was inaccessible during this continuation.</li>
<li><a href="https://github.com/dbourdeau/cyphersolver/blob/main/memoire1560/READING.md">Full reading</a>,
<a href="https://github.com/dbourdeau/cyphersolver/blob/main/memoire1560/VERIFY.md">verification and uncertainty log</a>,
and <a href="https://github.com/dbourdeau/cyphersolver/blob/main/memoire1560/coverage.tsv">coverage audit</a>.</li>
</ul>
<p class="muted">The <a href="https://github.com/dbourdeau/cyphersolver/tree/main/memoire1560">repository folder</a>
preserves the inherited notes, transcription, partial key and mechanical output, together with the revised reading and scripts.
No DECODE record is known for this target; no external database edit was made.</p>
</main>
<!-- site:footer -->
</body></html>
'''
write(DOCS/f'{slug}.html',page.replace('<!-- FULL_READING -->','\n'.join(parts)))

manifest=read(DOCS/'_build_site.py')
entry="""    dict(slug='memoire1560', label='M&eacute;moire en chiffre 1560', year='1560', y=1560.95, place='Agenais &rarr; Montmorency?', st='solved', stt='editorial reading',
         title='M&eacute;moire en chiffre du XIIe d&eacute;cembre 1560',
         blurb='Ten-page report on unrest in the Agenais, BnF fr. 3157 no. 67. Full normalized reading with seven small uncertainties, continuing an inherited partial solution. Conservative editorial coverage 97.688%; the alphabet remains partial and no independent clear copy is known.',
         quote='Lesdicts rebelles m&rsquo;ont rendu en tel estat que je n&rsquo;ause sortir de ma maison si ce n&rsquo;est de nuict.',
         rights='Biblioth&egrave;que nationale de France, fran&ccedil;ais 3157, via Gallica'),
"""
if "slug='memoire1560'" not in manifest:
    marker="    dict(slug='throckmorton'"
    assert marker in manifest
    manifest=manifest.replace(marker,entry+marker,1)
if "'memoire1560':" not in manifest and "IMAGES['memoire1560']" not in manifest:
    manifest=manifest.replace('IMAGES = {','IMAGES = {\'memoire1560\': (\'memoire1560_lead.jpg\', \'The dated heading and opening cipher lines of the report, 12 December 1560\', \'Biblioth&egrave;que nationale de France, fran&ccedil;ais 3157 f. 152r, Gallica view 153\'),',1)
write(DOCS/'_build_site.py',manifest)

title='Mémoire en chiffre'
row='| **Mémoire en chiffre**, BnF fr. 3157 no. 67, ff. 152r–156v (catalogue 276, class C; unknown → Montmorency?) | 12 Dec 1560 | 23 Sept 2026 | **Read: editorial reconstruction.** Ten pages, margin and dorse; seven small uncertainties. Conservative coverage 8071/8262 sign units (97.688%), not independent accuracy. Continued prior local key/transcription; key partial, no clear-copy verification. | [`memoire1560/`](memoire1560/) · [write-up](https://dbourdeau.github.io/cyphersolver/memoire1560.html) |\n'
s=read(ROOT/'README.md')
if 'cyphersolver/memoire1560.html' not in s:
    start=s.index('### Solved: key broken here');at=s.index('|---|---|---|---|---|',start)+len('|---|---|---|---|---|')
    s=s[:at]+ '\n'+row+s[at:]
write(ROOT/'README.md',s)

s=read(ROOT/'SOLVED_CATALOGUE.md')
if 'memoire1560.html' not in s:
    nums=[int(x) for x in re.findall(r'^\| (\d+) \|',s,re.M)]; num=max(nums)+1
    row=f'| {num} | **Mémoire en chiffre**, BnF fr. 3157 no. 67, catalogue 276 | 12 Dec 1560 | 23 Sept 2026 | Inherited partial substitution followed by image-based editorial reconstruction; 8071/8262 conservative coverage | Full ten-page reading, omitted margin and dorse; seven doubts, key partial and no independent plaintext. Prior local attempt credited. [`memoire1560/`](memoire1560/) · [write-up](https://dbourdeau.github.io/cyphersolver/memoire1560.html)* |\n'
    s=add_after(s,'|---|---|---|---|---|---|\n',row)
write(ROOT/'SOLVED_CATALOGUE.md',s)
s=read(ROOT/'SOLVED_RANKING.md')
if 'memoire1560.html' not in s:
    n=max(int(x) for x in re.findall(r'\| p(\d+) \|',s))+1
    row=f'| p{n} | **Mémoire en chiffre**, BnF fr. 3157 no. 67 | 12 Dec 1560 | 3 | 4 | 3 | 3 | 1 | 2 | **2.95** | Extensive Agenais report; inherited local partial solution completed editorially, seven small uncertainties. Novelty unproven; no independent clear copy. [memoire1560](https://dbourdeau.github.io/cyphersolver/memoire1560.html) |\n'
    s=add_after(s,'|---|---|---|---|---|---|---|---|---|---|---|\n',row)
    s=s.replace('## Axes and weights',f'The **Mémoire en chiffre** is provisionally p{n} at **2.95**: substantial historical content, but an inherited partial key and an editorial reading without external plaintext verification. Novelty score is provisional.\n\n## Axes and weights',1)
    s+='\nMémoire en chiffre: 0.25×3 + 0.25×4 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×2 = **2.95** (provisional).\n'
write(ROOT/'SOLVED_RANKING.md',s)
s=read(ROOT/'TARGETS.md')
if 'memoire1560.html' not in s:
    s=add_after(s,'## Done elsewhere in this repo\n','\n- **Mémoire en chiffre**, 12 December 1560 (BnF fr. 3157 no. 67; catalogue 276): full editorial reading, 23 Sept 2026; 97.688% conservative coverage, seven small uncertainties, partial key. Prior local attempt used. [Write-up](https://dbourdeau.github.io/cyphersolver/memoire1560.html).\n')
write(ROOT/'TARGETS.md',s)
c=json.loads(read(ROOT/'catalogue.json'));entries=c if isinstance(c,list) else c['entries']
old=[e for e in entries if e.get('id')==276]
if old:
    dump(HERE/'catalogue_entry.json',old[0]);entries[:]=[e for e in entries if e.get('id')!=276];dump(ROOT/'catalogue.json',c)
s=read(ROOT/'CATALOGUE.md')
s='\n'.join(l for l in s.splitlines() if not(l.startswith('|') and re.search(r'\|\s*276\s*\|',l)))+'\n'
if '**276 —' not in s:
    marker='Read or resolved here, and removed\n'
    s=add_after(s,marker,'\n- **276 — Mémoire en chiffre**, BnF fr. 3157 no. 67, 12 December 1560: read editorially 23 Sept 2026; 97.688% conservative coverage, seven small uncertainties, partial key. The old no-prior-reading claim is retained as a catalogue assertion, not proven novelty. [Write-up](https://dbourdeau.github.io/cyphersolver/memoire1560.html).\n')
write(ROOT/'CATALOGUE.md',s)
s=read(DOCS/'index.html')
if 'href="memoire1560.html"' not in s:
    s=add_after(s,'<ul class="findings">','\n<li><b>Mémoire en chiffre, 12 December 1560</b> &mdash; <span class="fnd">Ten-page Agenais report read editorially</span>, with seven small uncertainties and a partial key. <a href="memoire1560.html">write-up</a></li>')
write(DOCS/'index.html',s)
kw=json.loads(read(DOCS/'keys.json'));kw.setdefault('unlinked',{})[slug]='Partial key reconstructed in earlier local project work and continued here from this text alone; no external named key. Editorial reading does not equal exact decoder output.';dump(DOCS/'keys.json',kw)
skip=json.loads(read(DOCS/'_explore_skip.json'))
skip.setdefault('portrait',{})[slug]='Writer unnamed; recipient Montmorency is conjectural, so no portrait is presented as a secure attribution.'
skip.setdefault('reveal',{})[slug]='Inherited ASCII transcription conflates graphic variants; the partial key does not generate the normalized editorial text. An exact reveal would misrepresent the evidence; raw decoder and output are preserved in the repository.'
dump(DOCS/'_explore_skip.json',skip)
print('Page, figures, manifest and ledgers installed.')
