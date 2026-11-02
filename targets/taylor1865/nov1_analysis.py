"""Local 1 November research: raw candidates stay distinct from reconstructions.
Run with Python 3; no dependencies or network. Offsets count ciphertext only.
This is a known-key alignment aid, not a ciphertext-only solver.
"""
import csv
import json
from pathlib import Path
from continue_analysis import vig
ROOT=Path(__file__).resolve().parent

def main():
    docs=json.loads((ROOT/'nov1_alignment.json').read_text())
    rows=[]; report=[]
    for d in docs:
        offset=0; exact=total=0
        for n,g in enumerate(d['groups'],1):
            raw=g['raw']; p=g['proposed_plaintext']
            expected=vig(p,d['key'],enc=True,offset=offset)
            # Counts deliberately exclude unequal-length groups: no implicit insertion.
            same=sum(a==b for a,b in zip(raw,expected)) if len(raw)==len(expected) else None
            if same is not None: exact+=same;total+=len(raw)
            rows.append([d['id'],n,offset,raw,vig(raw,d['key'],offset=offset),p,expected,
                         same if same is not None else 'length differs',g.get('note') or 'No additional note.'])
            offset+=len(p) # Reconstructed stream; explicit if raw has an omission.
        report.append(f"{d['id']}: {exact}/{total} position matches in equal-length groups; reconstructed length {offset}. Unequal-length groups excluded. This is not a raw decipherment accuracy score.")
        (ROOT/(d['id']+'_cipher.txt')).write_text(' '.join(g['raw'] for g in d['groups'])+'\n')
        (ROOT/(d['id']+'_decryption.txt')).write_text('Candidate alignment, not a clean reading. See '+d['id']+'_reading.md\n'+
            '\n'.join(f'{r[1]:02d} offset {r[2]}: {r[3]} -> {r[4]} | proposed {r[5]} | reconstructed {r[6]} | {r[8]}' for r in rows if r[0]==d['id'])+'\n')
        raw=''.join(g['raw'] for g in d['groups'])
        plain=''.join(g['proposed_plaintext'] for g in d['groups'])
        report.append('Uncorrected, uninterrupted raw decryption: '+vig(raw,d['key']))
        if len(raw)==len(plain):
            for key in ['COMERETRIBUTION','COMPLETEVICTORY','MANCHESTERBLUFF','THENAVYOURPRIDE']:
                score=[sum(a==b for a,b in zip(vig(raw,key,offset=i),plain)) for i in range(len(key))]
                report.append(f'  {key}: offset0 {score[0]}/{len(raw)}, best {max(score)}/{len(raw)} at offset {score.index(max(score))}')
        reconstructed=vig(plain,d['key'],enc=True)
        assert vig(reconstructed,d['key'])==plain
    with (ROOT/'nov1_alignment.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n')
        w.writerow(['document','group','reconstructed_offset','raw_candidate','raw_at_reconstructed_offset','proposed_plaintext','reconstructed_cipher','position_matches','note']);w.writerows(rows)
    (ROOT/'nov1_controls.txt').write_text('\n'.join(report)+'\n')
    print('\n'.join(report))
if __name__=='__main__': main()
