"""method.html and methode.html: how the project works and how its readings are reviewed (16 Nov 2026).

The page describes the process and its limits, for a researcher who will not read the repository. It follows the
outline in Brice Dudout's audit of 16 Nov 2026. It names no reviewer; a reviewer is named on a page only with that
person's agreement. Every figure is computed here from targets/*/profile.json at build time, so the page cannot
drift from the records. The rules themselves stay in README.md (Conventions), CONTRIBUTING.md and
profile.schema.json: this page points to them and does not restate them in full.

The French page is a translation of this page only. Reading pages are not translated.
"""
import json, pathlib, collections
import _reader_kind as RK

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
REPO = 'https://github.com/dbourdeau/cyphersolver'
VERIFY = REPO + '/issues/new?template=verification.yml'


def figures():
    f = dict(RK.counts())
    verdicts = collections.Counter(); crypt = crypt_val = 0
    for p in (ROOT / 'targets').glob('*/profile.json'):
        try:
            o = json.loads(p.read_text(encoding='utf-8')).get('outcome') or {}
        except ValueError:
            continue
        v = (o.get('validation') or {}).get('verdict')
        if v:
            verdicts[v] += 1
        if (o.get('method') or '').startswith('key recovered') and o.get('class') in ('read', 'read in part'):
            crypt += 1; crypt_val += bool(o.get('validation'))
    f.update(verdicts=dict(verdicts), crypt=crypt, crypt_val=crypt_val)
    try:
        log = json.loads((HERE / 'corrections.json').read_text(encoding='utf-8'))['corrections']
        f['corrections'] = len(log)
    except (OSError, ValueError, KeyError):
        f['corrections'] = 0
    return f


def n(x):
    return f'{x:,}'


EN = dict(
    lang='en', file='method.html', other=('fr', 'methode.html', 'Version fran&ccedil;aise'),
    title='Method and review &mdash; how readings are made, checked and corrected',
    desc='How Cyphersolver finds, transcribes, deciphers and reviews historical cipher texts, what its checks can and cannot show, who reviews a reading, and how to contest one.',
    kicker='Reference &middot; method &middot; review', h1='Method and review',
    sub='What this project does, how a reading is made and checked, who checks it, and what the checks cannot show. '
        'It is written for a cryptologist, a palaeographer or an archivist who wants to judge a result without reading the code.',
    sections=lambda f: [
        ('what', 'What this project is, and is not',
         '<p>An open ledger of historical cipher texts worked with AI language models, and an informal measure of what those models can do. '
         'It is not a critical edition, and its results are not peer-reviewed. A reading published here is a proposal with its evidence attached: '
         'the transcription, the key, the unedited output of the key and the reading are all in the repository for anyone to check.</p>'),
        ('sources', 'Where the texts come from',
         '<p>Each item is a document in an archive or library, cited with its holder, shelfmark and folio, and reached through public images '
         '(Gallica, the DECODE database, IIIF viewers and others). Before an item is treated as unread, earlier work is searched for and the result written down: '
         'the DECODE record, published lists of solved and unsolved ciphers, printed editions and calendars, and the literature. '
         f'The rule is the catalogue vetting bar in the <a href="{REPO}#conventions">README</a>. It has failed before: see the <a href="corrections.html">corrections</a>.</p>'),
        ('transcription', 'Transcription',
         '<p>Most transcriptions are made by a model from the images, by one reader. There is no systematic second, blind transcription and no published agreement rate. '
         'In some targets the transcription and the key were frozen and timestamped before the reading was scored. '
         'Where a transcription was revised after the solver had run, the target&rsquo;s notes should say so; not all do.</p>'
         '<p>This is the weakest step. In November 2026 a check of one ten-page text against its images found that the first transcription had written one code for signs the manuscript keeps apart; '
         '379 words of the transcription changed. In another target a file listed as a transcription had been generated from the reading.</p>'),
        ('key', 'How a key is obtained',
         '<p>Every page states one of the methods in the <a href="glossary.html#methods">glossary</a>. Three are cryptanalysis done here (from the ciphertext alone, '
         'from plaintext beside the cipher, from plaintext found elsewhere). Three apply a key or a decipherment that already existed. The home page counts the two families apart.</p>'),
        ('read', 'Decoded is not read',
         '<p>A document is in one of four states: read, read in part, decoded but not read, or not prose. It counts as <em>read</em> only when 95% of its words read as sense, measured on the reading file, '
         'and when it builds into sentences that a reader has read as sentences and that are translated into English. A word that is unread, guessed or supplied is a hole. Holes are counted by words.</p>'
         '<p><strong>The output of the key and the reading are two files.</strong> The decryption is the key applied to the transcription with nothing edited. '
         'The reading is that text made into sentences, and every letter or word in it that the key does not give must be marked. '
         'This rule was written down on 16 November 2026, after an audit found unmarked changes in 35 of 54 readings examined; they are now marked, and the audit is in '
         f'<a href="{REPO}/tree/main/research/decrypt_audit">research/decrypt_audit</a>. Readings not yet examined may still carry unmarked changes.</p>'),
        ('statistics', 'Statistical checks against false positives',
         '<p>For a key recovered by cryptanalysis, the reading is scored with a period language model and compared with two nulls: random keys of the same structure, '
         'and keys fitted to the same ciphertext shuffled (the overfitting test). A result passes when it is at least 5 standard deviations above the random keys, above every fitted key, '
         'and at least 3 standard deviations above their mean. The test also measures its own power and can answer &ldquo;too short&rdquo; or &ldquo;underdetermined&rdquo;.</p>'
         f'<p>Verdicts on record: {", ".join(f"{n(v)} {k}" for k, v in sorted(f["verdicts"].items(), key=lambda x: -x[1]))}. '
         f'Of {n(f["crypt"])} readings whose key was recovered by cryptanalysis, {n(f["crypt_val"])} carry this test; the others are mostly contributed results. '
         'What the test cannot show: it says the key yields language, not that each word is right. It does not cover code values filled in from context, '
         'it has no correction for many tests, and it has not been reviewed by a statistician outside the project.</p>'),
        ('review', 'Review',
         f'<p>Each reading is graded A or B by a reader. Of {n(f["reviews"])} reading reviews on record, <strong>{n(f.get("model", 0))} were made by a model</strong>, '
         f'{n(f.get("person assisted by model", 0))} by a person working with a model and {n(f.get("person", 0))} by a person alone; '
         f'{n(f.get("not stated", 0))} do not say. {n(f.get("not independent", 0))} say of themselves that the reader was not independent of the work. '
         f'A person has checked a passage against the image without any model in {n(f.get("human_check", 0))} targets.</p>'
         '<p>So the review of a reading is, in almost every case, a second model reading together with automated checks. It is not a human review, and it is not peer review. '
         'Changes from contributors arrive as pull requests that the maintainer approves; the maintainer and the site&rsquo;s rebuild job can also change the main branch directly, '
         'so this is not a two-person rule. Readings waiting for an independent check are listed on the <a href="contributors.html#verify">contributors page</a>.</p>'),
        ('ai', 'The role of AI',
         '<p>Each target&rsquo;s record names the models used and what the person did. Steps done by a model, such as transcribing from an image or proposing a code value from context, '
         'cannot be replayed exactly, and the models are commercial ones. The scripts, keys and transcriptions are versioned and can be rerun. '
         'Cost is not recorded: the project publishes no figure for tokens, money or hours.</p>'),
        ('credit', 'Credit and prior work',
         '<p>An earlier decipherment or key is credited by name on the page, also when it is found after the work was done; the result is then classed as read from an existing decipherment or with a known key. '
         'Contributors are credited for what they did. Text is released under CC BY 4.0; images stay under their holders&rsquo; terms and are credited one by one.</p>'),
        ('contest', 'Every reading stays open to correction',
         f'<p>To contest or check a reading, use the link at the foot of its page, the <a href="{VERIFY}" rel="noopener">verification form</a> (it needs a GitHub account), '
         'or <a href="contribute.html#email">email</a>. Say which passage and which images, and where your reading differs. No response time is promised. '
         f'A correction is made on the page with its date and entered in the <a href="corrections.html">corrections log</a> ({n(f["corrections"])} entries).</p>'),
        ('researchers', 'For researchers',
         '<p>Cryptologists, palaeographers, archivists and historians are invited to check a reading, to take on a series, or to co-sign a page. '
         'A checker is named on a page only with that person&rsquo;s written agreement, with what was checked and when. '
         'The project would rather be told that a reading is wrong than have it stand.</p>'),
        ('cite', 'How to cite',
         '<p>Every page has &ldquo;Cite this page&rdquo; with the date it was posted and last changed and the repository commit it was built from. '
         'Pages change; cite the commit. There is no DOI yet.</p>'),
    ],
    foot='The rules in full: <a href="{repo}#conventions">README, Conventions</a> &middot; <a href="{repo}/blob/main/CONTRIBUTING.md">CONTRIBUTING</a> &middot; '
         '<a href="{repo}/blob/main/profile.schema.json">the record schema</a> &middot; <a href="glossary.html">glossary</a>. Figures on this page are counted from the records each time the site is built.',
    meta='Daniel Bourdeau and contributors')

FR = dict(
    lang='fr', file='methode.html', other=('en', 'method.html', 'English version'),
    title='M&eacute;thode et relecture &mdash; comment les lectures sont faites, v&eacute;rifi&eacute;es et corrig&eacute;es',
    desc='Comment Cyphersolver rep&egrave;re, transcrit, d&eacute;chiffre et relit des textes chiffr&eacute;s anciens, ce que ses contr&ocirc;les montrent et ne montrent pas, qui relit une lecture et comment la contester.',
    kicker='R&eacute;f&eacute;rence &middot; m&eacute;thode &middot; relecture', h1='M&eacute;thode et relecture',
    sub='Ce que fait ce projet, comment une lecture est &eacute;tablie et contr&ocirc;l&eacute;e, par qui, et ce que les contr&ocirc;les ne montrent pas. '
        'Cette page s&rsquo;adresse au cryptologue, au pal&eacute;ographe ou &agrave; l&rsquo;archiviste qui veut juger un r&eacute;sultat sans lire le code. '
        'Seule cette page est traduite ; les pages de lecture restent en anglais.',
    sections=lambda f: [
        ('what', 'Ce que ce projet est, et n&rsquo;est pas',
         '<p>Un registre ouvert de textes chiffr&eacute;s anciens travaill&eacute;s avec des mod&egrave;les de langue, et une mesure informelle de ce que ces mod&egrave;les savent faire. '
         'Ce n&rsquo;est pas une &eacute;dition critique, et ses r&eacute;sultats ne sont pas &eacute;valu&eacute;s par les pairs. Une lecture publi&eacute;e ici est une proposition accompagn&eacute;e de ses pi&egrave;ces : '
         'la transcription, la cl&eacute;, la sortie brute de la cl&eacute; et la lecture sont dans le d&eacute;p&ocirc;t, o&ugrave; chacun peut les v&eacute;rifier.</p>'),
        ('sources', 'D&rsquo;o&ugrave; viennent les textes',
         '<p>Chaque pi&egrave;ce est un document d&rsquo;archives ou de biblioth&egrave;que, cit&eacute; avec son lieu de conservation, sa cote et son folio, et consult&eacute; sur des images publiques '
         '(Gallica, la base DECODE, des visionneuses IIIF, entre autres). Avant de tenir une pi&egrave;ce pour non lue, on cherche les travaux ant&eacute;rieurs et on note le r&eacute;sultat : '
         'la notice DECODE, les listes publi&eacute;es de chiffres r&eacute;solus ou non, les &eacute;ditions et inventaires imprim&eacute;s, la litt&eacute;rature. '
         f'La r&egrave;gle figure dans le <a href="{REPO}#conventions">README</a>. Elle a d&eacute;j&agrave; &eacute;t&eacute; prise en d&eacute;faut : voir les <a href="corrections.html">corrections</a>.</p>'),
        ('transcription', 'Transcription',
         '<p>La plupart des transcriptions sont faites par un mod&egrave;le &agrave; partir des images, par un seul lecteur. Il n&rsquo;y a pas de seconde transcription syst&eacute;matique &agrave; l&rsquo;aveugle, ni de taux d&rsquo;accord publi&eacute;. '
         'Pour certaines pi&egrave;ces, la transcription et la cl&eacute; ont &eacute;t&eacute; fig&eacute;es et horodat&eacute;es avant la mesure de la lecture. '
         'Quand une transcription a &eacute;t&eacute; reprise apr&egrave;s le passage du solveur, les notes de la pi&egrave;ce devraient le dire ; toutes ne le font pas.</p>'
         '<p>C&rsquo;est l&rsquo;&eacute;tape la plus fragile. En novembre 2026, le contr&ocirc;le sur images d&rsquo;un texte de dix pages a montr&eacute; que la premi&egrave;re transcription notait d&rsquo;un m&ecirc;me code des signes que le manuscrit distingue ; '
         '379 mots de la transcription ont chang&eacute;. Pour une autre pi&egrave;ce, un fichier class&eacute; comme transcription avait &eacute;t&eacute; produit &agrave; partir de la lecture.</p>'),
        ('key', 'Comment une cl&eacute; est obtenue',
         '<p>Chaque page indique l&rsquo;une des m&eacute;thodes du <a href="glossary.html#methods">glossaire</a>. Trois rel&egrave;vent de la cryptanalyse faite ici (&agrave; partir du seul texte chiffr&eacute;, '
         'd&rsquo;un clair voisin du chiffre, d&rsquo;un clair trouv&eacute; ailleurs). Trois appliquent une cl&eacute; ou un d&eacute;chiffrement qui existait d&eacute;j&agrave;. La page d&rsquo;accueil compte les deux familles &agrave; part.</p>'),
        ('read', 'D&eacute;cod&eacute; ne veut pas dire lu',
         '<p>Un document est dans l&rsquo;un de quatre &eacute;tats : lu, lu en partie, d&eacute;cod&eacute; mais non lu, ou sans prose. Il n&rsquo;est compt&eacute; comme <em>lu</em> que si 95 % de ses mots donnent un sens, mesur&eacute; sur le fichier de lecture, '
         'et s&rsquo;il forme des phrases qu&rsquo;un lecteur a lues comme des phrases et qui sont traduites en anglais. Un mot non lu, devin&eacute; ou suppl&eacute;&eacute; est une lacune. Les lacunes se comptent en mots.</p>'
         '<p><strong>La sortie de la cl&eacute; et la lecture sont deux fichiers distincts.</strong> Le d&eacute;chiffrement est la cl&eacute; appliqu&eacute;e &agrave; la transcription, sans aucune retouche. '
         'La lecture est ce texte mis en phrases, et toute lettre ou tout mot que la cl&eacute; ne donne pas doit y &ecirc;tre signal&eacute;. '
         'Cette r&egrave;gle a &eacute;t&eacute; &eacute;crite le 16 novembre 2026, apr&egrave;s un audit qui a trouv&eacute; des modifications non signal&eacute;es dans 35 des 54 lectures examin&eacute;es ; elles sont d&eacute;sormais signal&eacute;es, et l&rsquo;audit se trouve dans '
         f'<a href="{REPO}/tree/main/research/decrypt_audit">research/decrypt_audit</a>. Les lectures non encore examin&eacute;es peuvent en contenir.</p>'),
        ('statistics', 'Contr&ocirc;les statistiques contre les faux positifs',
         '<p>Pour une cl&eacute; retrouv&eacute;e par cryptanalyse, la lecture est not&eacute;e par un mod&egrave;le de langue d&rsquo;&eacute;poque et compar&eacute;e &agrave; deux hypoth&egrave;ses nulles : des cl&eacute;s al&eacute;atoires de m&ecirc;me structure, '
         'et des cl&eacute;s ajust&eacute;es sur le m&ecirc;me texte chiffr&eacute; m&eacute;lang&eacute; (test de surajustement). Un r&eacute;sultat est valid&eacute; s&rsquo;il d&eacute;passe d&rsquo;au moins 5 &eacute;carts types les cl&eacute;s al&eacute;atoires, d&eacute;passe chaque cl&eacute; ajust&eacute;e, '
         'et d&eacute;passe leur moyenne d&rsquo;au moins 3 &eacute;carts types. Le test mesure aussi sa propre puissance et peut r&eacute;pondre &laquo;&nbsp;trop court&nbsp;&raquo; ou &laquo;&nbsp;sous-d&eacute;termin&eacute;&nbsp;&raquo;.</p>'
         f'<p>Verdicts enregistr&eacute;s (libell&eacute;s du d&eacute;p&ocirc;t) : {", ".join(f"{n(v)} {k}" for k, v in sorted(f["verdicts"].items(), key=lambda x: -x[1]))}. '
         f'Sur {n(f["crypt"])} lectures dont la cl&eacute; a &eacute;t&eacute; retrouv&eacute;e par cryptanalyse, {n(f["crypt_val"])} portent ce test ; les autres sont pour la plupart des contributions ext&eacute;rieures. '
         'Ce que le test ne montre pas : il dit que la cl&eacute; produit de la langue, non que chaque mot est juste. Il ne couvre pas les valeurs de code propos&eacute;es d&rsquo;apr&egrave;s le contexte, '
         'ne corrige pas la multiplicit&eacute; des tests, et n&rsquo;a pas &eacute;t&eacute; relu par un statisticien ext&eacute;rieur au projet.</p>'),
        ('review', 'Relecture',
         f'<p>Chaque lecture re&ccedil;oit une note A ou B d&rsquo;un lecteur. Sur {n(f["reviews"])} relectures enregistr&eacute;es, <strong>{n(f.get("model", 0))} ont &eacute;t&eacute; faites par un mod&egrave;le</strong>, '
         f'{n(f.get("person assisted by model", 0))} par une personne aid&eacute;e d&rsquo;un mod&egrave;le et {n(f.get("person", 0))} par une personne seule ; '
         f'{n(f.get("not stated", 0))} ne le pr&eacute;cisent pas. {n(f.get("not independent", 0))} indiquent elles-m&ecirc;mes que le lecteur n&rsquo;&eacute;tait pas ind&eacute;pendant du travail. '
         f'Une personne a contr&ocirc;l&eacute; un passage sur l&rsquo;image, sans aucun mod&egrave;le, pour {n(f.get("human_check", 0))} pi&egrave;ces.</p>'
         '<p>La relecture d&rsquo;une lecture est donc, presque toujours, une seconde lecture par un mod&egrave;le, jointe &agrave; des contr&ocirc;les automatiques. Ce n&rsquo;est ni une relecture humaine ni une &eacute;valuation par les pairs. '
         'Les contributions arrivent sous forme de demandes de fusion que le mainteneur approuve ; le mainteneur et la reconstruction automatique du site peuvent aussi modifier directement la branche principale : '
         'il n&rsquo;y a donc pas de r&egrave;gle des deux personnes. Les lectures en attente d&rsquo;un contr&ocirc;le ind&eacute;pendant sont list&eacute;es sur la <a href="contributors.html#verify">page des contributeurs</a>.</p>'),
        ('ai', 'Le r&ocirc;le de l&rsquo;IA',
         '<p>La fiche de chaque pi&egrave;ce nomme les mod&egrave;les utilis&eacute;s et ce qu&rsquo;a fait la personne. Les &eacute;tapes confi&eacute;es &agrave; un mod&egrave;le, comme transcrire une image ou proposer une valeur de code d&rsquo;apr&egrave;s le contexte, '
         'ne peuvent pas &ecirc;tre rejou&eacute;es &agrave; l&rsquo;identique, et les mod&egrave;les sont commerciaux. Les scripts, les cl&eacute;s et les transcriptions sont versionn&eacute;s et peuvent &ecirc;tre relanc&eacute;s. '
         'Le co&ucirc;t n&rsquo;est pas enregistr&eacute; : le projet ne publie aucun chiffre en jetons, en argent ou en heures.</p>'),
        ('credit', 'Cr&eacute;dit et travaux ant&eacute;rieurs',
         '<p>Un d&eacute;chiffrement ou une cl&eacute; ant&eacute;rieurs sont cr&eacute;dit&eacute;s nomm&eacute;ment sur la page, y compris lorsqu&rsquo;ils sont d&eacute;couverts apr&egrave;s coup ; le r&eacute;sultat est alors class&eacute; comme lu d&rsquo;apr&egrave;s un d&eacute;chiffrement existant ou avec une cl&eacute; connue. '
         'Les contributeurs sont cr&eacute;dit&eacute;s pour ce qu&rsquo;ils ont fait. Le texte est diffus&eacute; sous licence CC BY 4.0 ; les images restent soumises aux conditions de leurs d&eacute;tenteurs et sont cr&eacute;dit&eacute;es une &agrave; une.</p>'),
        ('contest', 'Toute lecture reste ouverte &agrave; la correction',
         f'<p>Pour contester ou v&eacute;rifier une lecture, utilisez le lien au pied de sa page, le <a href="{VERIFY}" rel="noopener">formulaire de v&eacute;rification</a> (il demande un compte GitHub) '
         'ou le <a href="contribute.html#email">courriel</a>. Indiquez le passage, les images, et les endroits o&ugrave; votre lecture diff&egrave;re. Aucun d&eacute;lai de r&eacute;ponse n&rsquo;est promis. '
         f'Une correction est port&eacute;e sur la page avec sa date et inscrite au <a href="corrections.html">journal des corrections</a> ({n(f["corrections"])} entr&eacute;es, en anglais).</p>'),
        ('researchers', 'Pour les chercheurs',
         '<p>Cryptologues, pal&eacute;ographes, archivistes et historiens sont invit&eacute;s &agrave; v&eacute;rifier une lecture, &agrave; prendre en charge une s&eacute;rie ou &agrave; cosigner une page. '
         'Un v&eacute;rificateur n&rsquo;est nomm&eacute; sur une page qu&rsquo;avec son accord &eacute;crit, avec ce qui a &eacute;t&eacute; v&eacute;rifi&eacute; et la date. '
         'Le projet pr&eacute;f&egrave;re apprendre qu&rsquo;une lecture est fausse plut&ocirc;t que de la laisser en l&rsquo;&eacute;tat.</p>'),
        ('cite', 'Comment citer',
         '<p>Chaque page comporte &laquo;&nbsp;Cite this page&nbsp;&raquo;, avec la date de mise en ligne, celle de la derni&egrave;re modification et le commit du d&eacute;p&ocirc;t dont elle est issue. '
         'Les pages changent : citez le commit. Il n&rsquo;y a pas encore de DOI.</p>'),
    ],
    foot='Les r&egrave;gles compl&egrave;tes (en anglais) : <a href="{repo}#conventions">README, Conventions</a> &middot; <a href="{repo}/blob/main/CONTRIBUTING.md">CONTRIBUTING</a> &middot; '
         '<a href="{repo}/blob/main/profile.schema.json">le sch&eacute;ma des fiches</a> &middot; <a href="glossary.html">glossaire</a>. Les chiffres de cette page sont recompt&eacute;s sur les fiches &agrave; chaque construction du site.',
    meta='Daniel Bourdeau et les contributeurs')


def render(P, f, version=''):
    secs = P['sections'](f)
    body = ''.join(f'<h2 id="{a}"><span class="num">{i:02d}</span> {t}</h2>\n{b}\n\n' for i, (a, t, b) in enumerate(secs, 1))
    ol, ofile, olabel = P['other']
    return (
        f'<!DOCTYPE html>\n<html lang="{P["lang"]}">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{P["title"]}</title>\n<meta name="description" content="{P["desc"]}">\n'
        f'<link rel="alternate" hreflang="{P["lang"]}" href="{P["file"]}">\n<link rel="alternate" hreflang="{ol}" href="{ofile}">\n'
        f'<link rel="stylesheet" href="style.css?v={version}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        f'<section class="hero">\n  <p class="kicker">{P["kicker"]}</p>\n  <h1>{P["h1"]}</h1>\n'
        f'  <p class="sub">{P["sub"]}</p>\n'
        f'  <p class="meta">{P["meta"]} &middot; <a href="{ofile}" hreflang="{ol}" lang="{ol}">{olabel}</a></p>\n</section>\n\n<main>\n\n'
        f'{body}<p class="muted">{P["foot"].format(repo=REPO)}</p>\n\n</main>\n<!-- site:footer -->\n</body>\n</html>\n')


def build_html(version=''):
    f = figures()
    for P in (EN, FR):
        (HERE / P['file']).write_text(render(P, f, version), encoding='utf-8')
    return f


if __name__ == '__main__':
    print(build_html())
