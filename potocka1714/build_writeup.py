"""Build the target page and its sign-level reveal from the saved research."""
from pathlib import Path
import json,csv,re,html
P=Path(__file__).parent;R=P.parent;D=R/'docs';E=html.escape
notes=(P/'NOTES.md').read_text(encoding='utf8');reading=(P/'reading.md').read_text(encoding='utf8')
profile=json.loads((P/'profile.json').read_text());key=json.loads((P/'key-potocka.json').read_text());cov=json.loads((P/'coverage.json').read_text())
rows=list(csv.DictReader((P/'potocka-segments.tsv').open(encoding='utf8'),delimiter='\t'))
glosses={m.group(1):m.group(2) for m in re.finditer(r'^- R(\d+): (.+)$',notes,re.M)}
page=['''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Potocka and Mniszech to Dunin — Read in part</title>
<meta name="description" content="A Polish postscript unlocks Barbara Potocka's French cipher passages: a recovered numerical alphabet, nine letters, and a separate unread Mniszech cipher.">
<link rel="stylesheet" href="style.css"></head><body>
<!-- site:nav -->
<section class="hero"><div class="cipherstrip">39 27 34 · 36 19 27 37 35 36 19 27<br>p a n · s t a r o s t a</div>
<p class="kicker">Archiwum Sanguszków · French and Polish · 1714–1716 and undated · read in part</p>
<h1>A Polish postscript unlocks Potocka’s French cipher</h1>
<p class="sub">Barbara Potocka and Józef Mniszech to Jakub Dunin, Crown regent. DECODE R7524–7530 and R7534–7536. Nine letters share a recoverable alphabet; the tenth uses another system.</p>
<p class="meta">Daniel Bourdeau</p></section><main>
<div class="callout"><strong>Summary.</strong> French-language searches did not read the postscript in R7526: it is Polish. A Polish substitution search recovered the alphabet, which then read short French passages in eight other Potocka letters. Doubled figures supply additional letter values. The reading concerns property, court influence, a political accusation, and the safety of correspondence. Of 887 Potocka cipher tokens, 863 have a letter value (97.3%); this is key coverage, not a claim of equally complete verified prose. Four person codes and one exceptional figure remain open, alongside uncertain spellings and names. Mniszech’s 232-token cipher is still unread, so the ten-letter group is <strong>read in part</strong>. There is no independent clear copy or original key to validate the editorial readings.</div>
<h2 id="documents"><span class="num">01</span>The documents and the evidence</h2>
<p>All 29 source images were inspected, including backs, addresses and spreads. These are chiefly clear letters with brief cipher inserts; the tables below transcribe those inserts and their immediate clear anchors, not all the unencrypted prose. Image numbers are DECODE image suffixes. Some letters have no year: placeholder catalogue dates have not been adopted as historical dates.</p>
<p>Potocka calls Dunin “mon fils,” but the university <a href="https://womenscourt.uken.krakow.pl/womencourt/potocka-barbara-z-duninow-zm-v-1719-r-1-v-uniechowska/">Women’s Court biography</a> identifies her as his aunt. That source was found after the key recovery and supplied no cipher values.</p>
<table><thead><tr><th>Record</th><th>Shelfmark</th><th>Tokens valued / transcribed</th></tr></thead><tbody>''']
for d in profile['documents']:
    c=cov['documents'][d['id'][1:]]
    page.append(f'<tr><td><a href="https://de-crypt.org/decrypt-web/RecordsView/{d["id"][1:]}">{d["id"]}</a></td><td>{E(d["shelfmark"])}</td><td>{c["valued"]} / {c["tokens"]}</td></tr>')
page+=['''</tbody></table><h2 id="key"><span class="num">02</span>The recovered alphabet</h2>
<p>The basic sequence runs backwards from 25=e through 14=x, and forwards from 26=a through 39=p, with a break before l. The Polish postscript uses 27 for a and distinguishes 31/32 in positions for l/ł; the exact diacritic rule remains uncertain. Attested higher homophones include 50=e, 52=a, 58=c, 68=n and 74=r. Doubling is a useful pattern, not permission to invent values: 14=x does not make 28=x, since 28=b.</p><table><thead><tr><th>Figure</th><th>Letter</th></tr></thead><tbody>''']
for k,v in sorted(key.items(),key=lambda x:int(x[0])):page.append(f'<tr><td>{k}</td><td>{v}</td></tr>')
page+=['</tbody></table><p>Every letter value is inferred here (grade I), with doubtful readings marked M. None has grade H (original key) or C (independent known plaintext). The standalone figures 87, 94, 100 and 270 are unvalued person codes. A possible identification of 100 as the king is contextual only.</p>']
num=3
for d in profile['documents']:
    rid=d['id'][1:];page.append(f'<h2 id="r{rid}"><span class="num">{num:02}</span>{d["id"]}</h2>');num+=1
    if rid=='7524':
        page.append('<p>Mniszech’s letter, 1714: all 232 numerical tokens remain unread. The clear Polish and Latin words do not constitute a decipherment. The tentative <em>hetmanow</em> crib and proposed nulls were unsuccessful hypotheses, not recovered values.</p>');continue
    page.append('<p>'+E(glosses[rid])+'</p>')
    if rid=='7526':
        raw=''.join(key.get(n,'?') for n in (P/'r7526-trial.txt').read_text().split())
        page.append('<p>A cautiously word-divided reading, retaining the source’s irregular forms:</p><blockquote>Pan starosta serecki? iest tu. Pytałam się ieżeli ma co postanowionego. Ni ma nic. Iedzie dzie? do Lublina. To tesz prawda że był u dominikanow wtenczas iak estancował z nią w polu. Powiedał mi p. Tabrowski?</blockquote><p>The starosta is present; she asked whether he had arranged anything, but he has nothing. The postscript mentions Lublin, the Dominicans and his staying with a woman. The two names are uncertain. The repeated <em>dzie</em> and other irregularities are not silently repaired.</p><details><summary>Literal unspaced output</summary><p>'+raw+'</p></details>')
    else:
        page.append('<table><thead><tr><th>Image / clear anchor</th><th>Literal cipher output</th><th>Editorial interpretation or uncertainty</th></tr></thead><tbody>')
        for r in sorted([x for x in rows if x['record']==rid],key=lambda x:x['page']):
            raw=''.join(key.get(n,'<'+n+'>') for n in r['cipher'].split())
            page.append(f'<tr><td>{E(r["page"])}: {E(r["context"])}</td><td>{E(raw)}</td><td>{E(r["reading_note"])}</td></tr>')
        page.append('</tbody></table>')
page+= [f'''<h2 id="method"><span class="num">{num:02}</span>Method and limits</h2>
<p>The initial French searches failed. Polish monoalphabetic annealing recovered the R7526 alphabet, and the key was tested on eight other letters before the remaining figures were assigned. Repeated words and names verified the higher homophones. Full-resolution crops and a final all-page audit corrected numerical readings, added the cipher on R7527’s reverse, and counted the standalone codes.</p>
<p>Mniszech’s different system was tried with Polish homophonic searches, a tentative crib, null and digraph hypotheses, and a frequency penalty. None produced coherent text. Crucially, a synthetic 232-token homophonic control recovered only 49 positions. The failed historical searches are therefore inconclusive: the current solver cannot establish impossibility. The letter is left open.</p>
<p>Three Sanguszko key records (R7515, R7460, R7461) were inspected and ruled out by their signs or numerical values. Searches for editions, these correspondents and the shelfmarks found contextual references but no matching key or plaintext. Further correspondence is catalogued without online images located here. No prior reading was found; its nonexistence is not asserted.</p>
<h2 id="gaps"><span class="num">{num+1:02}</span>What remains uncertain</h2><ul>''']
for gap in profile['outcome']['gaps']:page.append('<li>'+E(gap['item'])+'. '+E(gap['detail'])+'</li>')
page+= [f'''</ul><p>The full request has 863/1,119 valued tokens (77.1%). The conservative coherence count is 745/1,119 (66.6%): it excludes entire doubtful segments, so it is a lower bound, not an error-rate estimate. Raw output, editorial interpretation and confidence are kept distinct in the <a href="https://github.com/dbourdeau/cyphersolver/blob/main/potocka1714/reading.md">complete segment reading</a>.</p>
<h2 id="sources"><span class="num">{num+2:02}</span>Sources and reproducibility</h2>
<p>Archiwum Narodowe w Krakowie, Archiwum Sanguszków: the ten DECODE records linked in the document table. Related correspondence is catalogued as <a href="https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/41995540/obiekty/1601530">29/637/0/1.3/9477</a>, not established here as a duplicate of these letters. All ciphertext, the recovered key, the failed solver trials, the control and token-level measurements are in the repository. Run <code>prepare_reading.py</code> to reproduce the literal output and coverage.</p>
<p class="muted"><a href="https://github.com/dbourdeau/cyphersolver/tree/main/potocka1714">Research notes, transcription, key and scripts</a>. DECODE updates are queued, not submitted; the public reading files contain encrypted-passage extracts with gaps for omitted clear prose.</p></main>
<!-- site:footer -->
</body></html>''']
(D/'potocka1714.html').write_text('\n'.join(page),encoding='utf8')
nums=(P/'r7526-trial.txt').read_text().split()
reveal={'slug':'potocka1714','anchor':'r7526','title':'The Polish postscript','caption':'Literal values from the recovered alphabet; uncertain names are marked. Word division and diacritics are editorial.','unit':'number','key_note':'Recovered here by Polish annealing and transfer to eight other letters.','tokens':[dict(g=n,p=key.get(n,'?'),cls='unc' if 11<=i<18 or i>=len(nums)-9 else '') for i,n in enumerate(nums)]}
(D/'reveal'/'potocka1714.json').write_text(json.dumps(reveal,indent=1)+'\n')
