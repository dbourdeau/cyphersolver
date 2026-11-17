"""Build key/code_B_table.tsv: every code B group with its value, where it is attested in Bougainville's two printed
cipher letters (Casgrain, Collection des manuscrits du marechal de Levis III, 1890, pp. 103-108 and 112-114), and
whether the value used for the 21 Nov 1758 letter is attested or inferred.

Inputs (all in this folder):
  key/code_B_solver_table.tsv   the solver's table of 11 Nov 2026 (group, value, count, conflicts, runs agreeing)
  letters/B1_aligned.tsv, letters/B2_aligned.tsv   one row per printed group with the clear text aligned to it
  transcriptions/figures_reconciled.txt   the figures of the 1758 letter (for the "used in 1758" count)

Standard library only.  python build_key_table.py   (run from this folder or anywhere; paths are relative to it)
"""
import csv, pathlib, re
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent

# Values used for the 1758 letter where the solver's string is a merge with a neighbour's letters (attested, trimmed).
TRIMMED = {
    '74': ('M. Bigot', "solver 'mbigotmpea' = M. Bigot + M. Pean, B1 p.104 'lettre forte a M. Bigot ; M. Pean'"),
    '97': ('la Louisiane', "solver 'lalouisiannea' takes the a of 'acceptee', B1 p.103"),
    '73': ('M. de Vaudreuil', ''),
    '110': ('Quebec', ''),
    '550': ('projet', "solver 'projetcontr' = projet + contre (302), B1 p.104 'Projet contre la Caroline'"),
    '427': ('je', "B1 p.108 aligned 'jefi' in 'je finis'; B1 p.104 aligned 'usie' inside 'jalousies' (a conflict); "
                  "'je' also fits the code's order (j block 426-432)"),
}
# Values not shown by the printed letters: taken from the code's number order and from sense. Inference, not tested.
INFERRED = {
    # group: (value, kind, basis)
    '674': ('janvier', 'not in the printed letters', "months at the end of the table: 675 fevrier (B2 p.112) and 681 aout (B2 p.114) attested"),
    '591': ('su', 'not in the printed letters', "S block sa 587, se 588, si 589, so 590; the letter uses 591 three times (su-r, su-re, su-r-pecte)"),
    '340': ('eau', 'not in the printed letters', "between donne 336 and ecri 342; gives la B-eau-bassin"),
    '286': ('cependant', 'not in the printed letters', "between celui 284 and cer 287"),
    '293': ('cher', 'not in the printed letters', "C block, before choi 295; gives je cher-c-he-ra-y"),
    '349': ('ence', 'not in the printed letters', "between en 348 and enfin 352; gives prefer-ence"),
    '461': ('moyens', 'not in the printed letters', "between monsieur 457 and munitions 465; other words fit the range"),
    '505': ('ordres', 'not in the printed letters', "between on 502 and ou 508; other words fit the range"),
    '535': ('possible', 'not in the printed letters', "between point 532 and pour 537; poste, port also fit"),
    '44': ('et', 'not in the printed letters', "end of the letter block (x 41, y 42, u 43, z 45); 'et' from sense only"),
    '101': ('la Caroline', 'not in the printed letters', "place-name block after 97 la Louisiane; weak: Bougainville spells 'la Caroline' "
                                                       "letter by letter in B1 p.104"),
    '4': ('b', 'printed, but not with this value', "printed twice in B2 p.112 as the numeral 4; b from the letter block "
                                                  "(a 1,3,5; c 6,8) and la B-eau-bassin"),
    '448': ('me', 'printed, but not with this value', "solver 'nne' (B1 p.108, in a name) and 'memanqu' ('me manque', B1 p.108); "
                                                     "me from ma 447, mi 449"),
    '524': ('peu', 'printed, but not with this value', "solver 'p' inside 'depense' (B1 p.104); peu from perdez 523 < x < place 526 "
                                                      "and 'a peu de frais'"),
}


def rows(path):
    with open(path, encoding='utf-8') as f:
        lines = [l for l in f if not l.startswith('#')]
    return list(csv.DictReader(lines, delimiter='\t'))


def main():
    solver = {r['group']: r for r in rows(HERE / 'key' / 'code_B_solver_table.tsv')}
    att = {}
    for name in ('B1', 'B2'):
        for r in rows(HERE / 'letters' / f'{name}_aligned.tsv'):
            if r['kind'] not in ('g', 'group'):
                continue
            clear = r['aligned_clear'] or '(null)'
            att.setdefault(r['group'], []).append(f"{r['letter']} p.{r['page']} para {r['unit']} group {r['seq']} '{clear}'")
    used = Counter()
    for line in open(HERE / 'transcriptions' / 'figures_reconciled.txt', encoding='utf-8'):
        if re.match(r'P\dL\d:', line):
            for g in line.split(':', 1)[1].split():
                used[g.split('|')[0].replace('+', '*')] += 1
    groups = set(solver) | set(INFERRED)
    key = lambda g: (int(re.match(r'\d+', g).group()), g)
    out = HERE / 'key' / 'code_B_table.tsv'
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        f.write('# Code B (Bougainville\'s code, Casgrain\'s "Pieces militaires No V"). One row per group. Built by build_key_table.py.\n')
        f.write('# status: attested = the value is aligned with Casgrain\'s printed clear text at the places listed;\n')
        f.write('#         inferred = the value is NOT shown by the printed letters; it comes from the code\'s number order and from sense.\n')
        f.write('# value: the value used to decode the 1758 letter (attested values trimmed where the solver merged a neighbour, see note).\n')
        f.write('# attestations: letter, page, paragraph and group number (letters/B1_aligned.tsv, B2_aligned.tsv) and the clear text aligned there.\n')
        f.write('# n_printed: how often the group is printed in B1 and B2; n_same_value: how many of those the solver aligned with its\n')
        f.write('#   value (solver_value). The difference is the conflicts (solver_other_values).\n')
        w.writerow(['group', 'value', 'status', 'inferred', 'n_printed', 'n_same_value', 'attestations', 'solver_value',
                    'solver_other_values', 'solver_runs_agreeing', 'used_in_1758_letter', 'note'])
        for g in sorted(groups, key=key):
            s = solver.get(g, {})
            a = att.get(g, [])
            same = sum(1 for x in a if x.endswith(f"'{s.get('value', '')}'")) if s.get('value') else 0
            if g in INFERRED:
                val, kind, basis = INFERRED[g]
                status, inferred, note = 'inferred', kind, basis
            elif g in TRIMMED:
                val, note = TRIMMED[g]
                status, inferred = 'attested', ''
            else:
                val, status, inferred, note = s.get('value', ''), 'attested', '', s.get('note', '')
            w.writerow([g, val, status, inferred, len(a), same, ' ; '.join(a), s.get('value', ''), s.get('other_values(count)', ''),
                        s.get('runs_agreeing', ''), used.get(g, 0), note])
    n = sum(1 for g in groups)
    print(f'{out.relative_to(HERE)}: {n} groups, {sum(1 for g in groups if g in INFERRED)} with inferred values '
          f'({sum(1 for g in INFERRED if INFERRED[g][1].startswith("not"))} not in the printed letters, '
          f'{sum(1 for g in INFERRED if INFERRED[g][1].startswith("printed"))} printed with another value)')


if __name__ == '__main__':
    main()
