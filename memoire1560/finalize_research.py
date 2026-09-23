from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
cov=json.loads((ROOT/'coverage.json').read_text(encoding='utf8'))
p=json.loads((ROOT/'profile.json').read_text(encoding='utf8'))
d=p['documents'][0]
d.update(read='read',date='12 December 1560',pages=11)
d['length']={'tokens':8262,'distinct':55,'unit':'symbols','measured':True,'file':'cipher_tokens.txt'}
d['transcription']['notes']='Editorial sign units measured by docs/_check_profile.py --measure cipher_tokens.txt --drop-first. The inherited ASCII convention conflates some graphic variants; 55 is not a definitive inventory of distinct cipher signs. Ten body pages, marginal addition and one-word dorse included.'
p['system']['summary']='Cursive letter substitution with whole-word signs, provisionally homophonic; some apparent variants are transcription inconsistencies.'
p['system']['word_division']='separator symbol'
p['system']['notes']='The alphabet is only partially reconstructed. Do not use the inherited decoder as if it produced the normalized editorial reading.'
p['conditions'].update(last_date='2026-09-23',tools=['inherited solve.py and partial key','image comparisons and enlarged crops','audit_alignment.py (alignment aid, not evidence)','measure_reading.py'])
p['conditions']['prior_solution'].update(exists='unknown',where='Previous local project attempt was used. No external decipherment located; absence of all published prior art is not proven.',used=True)
p['solution'] += [
 {'date':'2026-09-23','kind':'reading','what':'Inspected all ten page images and inherited sign transcription; reconstructed the first five pages and revised the final five. Normalization uses language context as well as partial substitution.','result':'worked'},
 {'date':'2026-09-23','kind':'sibling key','what':'Inspected Lasry Charles IX–du Croc table preserved in ducroc/GL_CharlesIX.png; incompatible letter and code values. Henri II table retrieval failed with HTTP 503, so no Henri II test is claimed.','result':'ruled out'},
 {'date':'2026-09-23','kind':'transcription','what':'Read omitted marginal addition at 153r.14 and the cipher endorsement Advertissemens on presumed dorse 157v.','result':'worked'},
 {'date':'2026-09-23','kind':'verification','what':'Regional enlargements resolved most inherited blanks, including pour les faire respondre par leur bouche, Si ainsi estoit, sement, oster; recognized a horizontal filler falsely transcribed as POUR.','result':'worked'},
 {'date':'2026-09-23','kind':'literature search','what':'Exact title, shelfmark and name searches found catalogue descriptions and general context but no matching reading or secure identification of Montseuignac. This is a limited negative search, not proof of novelty.','result':'partial'},
 {'date':'2026-09-23','kind':'verification','what':'Retried seven residual passages against enlarged scans and repeated forms. Preserved doubts rather than choosing exact name or pronoun expansions. No independent clear copy or primary codebook found.','result':'partial'},
 {'date':'2026-09-23','kind':'statistics','what':'Counted 8262 transcribed sign units; excluded all 191 units on seven doubtful lines, yielding 8071/8262 = 97.688% conservative editorial coverage. Not independently measured decipherment accuracy.','result':'worked'}
]
p['outcome']={
 'class':'read','key':'partial','fraction_read':'unknown','fraction_coherent':cov['fraction_coherent'],
 'fraction_read_method':'measured','fraction_read_source':'coverage.tsv and cipher_tokens.txt: 8262 editorial sign units, 191 units on all seven bracketed lines conservatively excluded. Measures coverage of reconstructed coherent prose, not independent symbol accuracy.',
 'grades':{'H':0,'C':0,'M':191,'I':8071},
 'codes_open':{'open':'unknown','total':'unknown','tokens_open':5},
 'verification':['none'],
 'gaps':[
  {'item':'152r.12, name Montseuignac','blocker':'no-key-material','detail':'Plausible literal spelling, no external confirmation or exact graphic key; enlarged and searched.'},
  {'item':'152r.15, 152v.21, 152v.26, 153r.10: four short groups','blocker':'open-codes','detail':'Pronoun/relative meanings inferred, exact expansions and graphic distinctions remain uncertain after repeated-form comparison.'},
  {'item':'153r.17 negative before irriter','blocker':'no-key-material','detail':'Sense suggests negative; exact initial glyph value not established at this occurrence.'},
  {'item':'153v.08 mark beside cancellation','blocker':'open-codes','detail':'Could be part of canceled group or an additional sign; retained unread.'}
 ],
 'notes':'Read as a normalized editorial reconstruction with limited bracketed uncertainties. Partial inherited alphabet, no independent decipherment or held-out control. Continuing prior local work, not a fresh blind solve; first-publication priority not established.'
}
(ROOT/'profile.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
old=(ROOT/'NOTES.md').read_text(encoding='utf8')
if not (ROOT/'NOTES_inherited.md').exists():(ROOT/'NOTES_inherited.md').write_text(old,encoding='utf8')
notes='''# Mémoire en chiffre du XIIe décembre 1560

Status: read — normalized editorial reconstruction; key partial.

BnF français 3157 no. 67, ff. 152r–156v; presumed dorse 157v. Catalogue 276, class C.
Gallica btv1b90598645. Unknown writer in the Agenais → Montmorency? Date: 12 December 1560.
Completed editorial pass: 23 September 2026, continuing the local attempt of 22 September.

The full ten-page report, one marginal addition and the one-word cipher endorsement have a reading.
Seven short passages retain brackets. A conservative count treats all signs on those seven lines as
unread: **8071/8262 = 97.688% editorial coverage**. The count is reproducible in coverage.tsv and
measure_reading.py. It is not independent token-accuracy validation. Key state: **partial**.

## Reading and evidence

READING.md presents the full normalized French with manuscript line numbers. VERIFY.md records
the image checks, corrections, source limitations and every remaining doubt. reading_working.tsv
is the machine-readable editorial text. The raw inherited key.txt, decrypt.py, decrypt_lines.txt
and transcription/ are deliberately retained to expose the remaining gap between mechanical
decoding and editorial reconstruction. These files must not be advertised as a complete exact decoder.

The report complains of Protestant preaching and assemblies, says about two thousand rebels met
at Clairac, names the Caulmont family, Reclus and Boissonade, accuses the Agen magistrates of concealing
the truth, criticizes Biron's handling of armed men, and describes threats from Lioux and Fumel.
The writer calls Fumel his near neighbour and asks permission, in effect, to retire to court for safety.
An expected unnamed prince and foreign help from the direction of Geneva and the Swiss cantons appear
in the final portion. These are the writer's allegations, not independently established events.
Neither the writer nor the unnamed chief or prince has been securely identified.

## Source and prior work

The inherited project folder was found in .claude/worktrees/memoire-chiffre-1560-76e15d/memoire1560
and copied before continuation. NOTES_inherited.md preserves its account of transcription and the
initial annealing/key work. That prior partial solution was used; this was not a blind solve.
The catalogue's assertion of no previous reading, no Tomokiyo/Lasry listing and no DECODE record
was the starting information, not a proven conclusion of this session. Limited fresh searches
found no matching publication. No DECODE record was accessed or edited.

The ten pages correspond to Gallica views 153–158, two pages per opening; f.152r is the right
side of view 153. The catalogue item number 67 must not be confused with a folio number.
The later dorse annotation henry second is inconsistent with the dated heading and is not used
to redetermine the year. Source: https://gallica.bnf.fr/ark:/12148/btv1b90598645/f153.item

## Remaining gaps

- 152r.12 Montseuignac — blocker: no-key-material; enlarged literal reading, exact spelling and historical identity unconfirmed.
- 152r.15, 152v.21, 152v.26, 153r.10 — blocker: open-codes; small connected groups, exact ils/qui/qu'ils expansion unconfirmed.
- 153r.17 — blocker: no-key-material; bracketed negative before irriter, not a diplomatic certainty.
- 153v.08 — blocker: open-codes; small mark alongside a canceled group, possible cancellation remnant.

## Escalation

- [x] siblings: inherited adjacent leaves and catalogue notice reviewed as available; no matching clear copy identified.
- [x] clear-pages: no decipherment among the supplied cipher pages; margin and dorse read anew.
- [x] known-keys: local Lasry Charles IX–du Croc table excluded; Henri II retrieval blocked by HTTP 503, not tested and explicitly outstanding.
- [x] print: exact-title, shelfmark, and contextual name searches; no matching reading found, limited search only.
- [x] key-rebuild: inherited partial substitution extended at the reading level through repeated signs, words, syntax and image corrections; exact key remains partial.
- [x] retry: all seven residual passages inspected again at larger scale; no further secure exact readings justified.

## Publication features

No atlas route or portrait: sender and destination town unknown, recipient uncertain.
No animated exact decoder: the inherited glyph transcription conflates signs and does not mechanically
generate the editorial reading. The partial key and uncorrected output remain available for review.
No external named key read this item. DECODE queue is not applicable: no record number is known.
'''
(ROOT/'NOTES.md').write_text(notes,encoding='utf8')
head='''# Mémoire en chiffre, 12 December 1560 — full editorial reading

BnF français 3157 no. 67, ff. 152r–156v, with marginal addition and presumed dorse f.157v.
Unknown writer, probably to Montmorency. Normalized French, reconstructed from cipher images and
the inherited partial key; **not a diplomatic transcription or the output of a complete decoder**.
u/v, i/j, word boundaries, punctuation and some spelling have been regularized. Brackets mark
uncertainty; `[..]` marks an unread sign or cancellation remnant. Unbracketed readings are
inferred (I), not primary-key or independent-clear-copy confirmations. See VERIFY.md.

Conservative editorial coverage: 8071/8262 transcribed sign units (97.688%); all signs on every
bracketed line are excluded. This measures coverage, not independently established accuracy.

'''
fol=None;out=[head]
for line in (ROOT/'reading_working.tsv').read_text(encoding='utf8').splitlines():
    if not line or line.startswith('#'):continue
    lab,t=line.split('\t',1); f=lab.split('.')[0]
    if fol!=f:out.append('\n## '+f+'\n');fol=f
    out.append(lab+' — '+t+'  \n')
(ROOT/'READING.md').write_text(''.join(out),encoding='utf8')
print('Research profile, notes and reading finalized.')
