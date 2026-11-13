# Frozen copy of the Pentz 1636 tables exactly as defined in b106_dk_small/scripts/dec_pentz.py lines 4-6 (md5 of source 8a69d4a14dd795fb0576380a8cbf96d1). No change.
AL="abcdefghiklmnopqrstuwxyz"
T1={37-i:AL[i] for i in range(9)}; T1.update({14+i:AL[9+i] for i in range(15)})
T2={38+i:AL[i] for i in range(9)}; T2.update({61:'n',60:'o',57:'r',56:'s',54:'u'})
