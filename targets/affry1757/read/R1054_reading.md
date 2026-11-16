# R1054 - d'Affry, The Hague, 19 July 1757 (to Bernis, "B."): reading

What this file is: the clerk's clear copy of the letter in the Fagel register, a decipherment of the time except at the places listed under "Figures over the register", where the figures are followed. It is not the
output of this folder's key; the keyed decode is `read/R1054.md`.

Rests on: the contemporary clear copy of this despatch in the Fagel register, Nationaal Archief 1.10.29 inv. 5186
scans 248R-249L (margin "Dat: 19. Juïllet 1757. A: à B:"), transcribed by WAINUT (21 Oct 2026,
`wainut/register_clear.txt`) and checked line by line against the NA IIIF scans 23 Oct 2026 (r2q). The register is the
deciphered text of the same letter: with this folder's key (`wainut/align_register.py`, `wainut/align/R1054.tsv`), 319
of the 364 keyed groups stand at the register's word (0.876; shuffled key values 0.144, max 0.206), from first group
to last. The DECODE record has one cipher page (image I5511, 372 groups); it ends inside the sentence on the gout
("... autant de monde que par le"), and the rest of the letter is not on the record. The reading covers that page; the
register's continuation is given below the reading. The reading follows the register in the clerk's spelling, except
where the figures give another word; those places are listed under "Figures over the register" and in
`R1054_reread_log.md`. Groups the register passes over without a word are listed in the log, not put into the reading.
The keyed decode this replaces is `R1054.md`.

## Reading

On ne dit point encore l'Objet du Voyage de Madame la Gouvernante: Les uns croyent, que c'est pour faire travailler à
une Augmentation dans les Troupes de Terre. Il est certain, que tous les Partisans murmurent sur l'état de foiblesse
dans lequel on laisse la Republique. Les Ministres commencent même à mettre en usage le danger de la Religion.
D'autres disent, que Son Altesse Royale, forcée par les plaintes reïtereés des Negociants veut proposer un Armement de
Mer. Il est à desirer que ce soit ce dernier objet qui l'amene ici. Si au contraire Elle travailloit à faire passer
une Augmentation dans les Troupes de Terre, il me paroit qu'il seroit essentiel aux Interets du Roy de m'envoyer ordre
de demander sur le Champ une confirmation de tout ce que les Etats Generaux ont promis à Sa Majesté, et en même tems
une Declaration de Leur part, qu'ils ne feront camper aucun Corps sur Leurs Frontieres. Je sens la dureté de cette
proposition, mais il me paroit qu'elle devient naturelle, en y ajoutant que Sa Majesté, par la juste confiance qu'Elle
avoit à la Parole de Leurs Hautes Puissances, n'a point ordonné à M. le Maréchal d'Estreés de prendre des precautions
pour la sureté de sa communication du Royaume, mais que des precautions deviendroient necessaires si malgré la Parole
donnée, le Gouvernement étoit entrainé par les Partisans de l'Angleterre, et forcé par l'insulte du Peuple à des
dispositions et à des demarches qui fissent craindre que Leurs Hautes Puissances ne s'écartassent malgré Elles de la
Sagesse de Leurs Regles. Une attaque de Goute m'empéche de voir autant de Monde que par le [...]

## Rest of the letter (register only, not on this record's image)

[...] que je le voudrois. J'espere malgé cela être au cour, et pouvoir vers la fin de la Semaine, ou aujourdhui en
huit vous en rendre compte. Je joins ici la Relation sur l'Objet de Delfzyl, elle m'a été remise hier fort tard. Vous
y verrez aussi les nouvelles d'Angleterre du 12. J'ai reçu aujourdhui une Lettre de Mr. de Moras du 11. qui me
confirme dans ce que j'ai eu l'honneur de vous marquer au Sujet de l'Oostfrise. Mr. le Cte. de Wassenaer, à qui j'en
ai parlé hier, pense comme moi. Il doit m'envoyer aujourdhui l'Abregé des Articles de la Convention du Roy
d'Angleterre, et de Mr. de Bentheim, pour la Comtesse de ce Nom. P. S. Le Comte de Wassenaer ne m'a point encore remis
l'Abregé dont j'ai eu l'honneur de vous parler. J'aurai celui de vous le faire tenir dès qu'il me sera parvenu.

## Figures over the register

- "n'a point ordonné à M. le Maréchal d'Estreés" for the register's "n'a point ordonné au Cte. d'Estreés": groups 402
  196 878 185 (à, m, le, maréchal; 185 = maréchal also in R1064 'M. le Marechal de Belle Isle'); DECODE transcribed
  '878^6', which the parse had split into 8 and 786; the register (and Bussemaker) have 'au Cte.' (d'Estrées was made
  maréchal de France in February 1757).
- "pour la sureté de sa communication du Royaume" for the register's "pour la sureté de la communication du Royaume":
  group 10 = sa (11 other occurrences at sa); 'du' has no group of its own and is the register's.
- "que par le [...]" for the register's "que je le voudrois.": the page ends with 197 306 628 (que, par, le); 306 =
  par at 34 other places; the register's 'que je le voudrois' has no group for 'je' or 'voudrois' here, and the letter
  goes on on a page that is not on the DECODE record.
