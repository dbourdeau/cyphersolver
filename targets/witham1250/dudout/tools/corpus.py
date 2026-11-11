# -*- coding: utf-8 -*-
"""Corpus for the Alphen / Witham sword-inscription study (11 Nov 2026).

SIBLINGS: inscriptions of the same family as published (source given). Readings are
the published authors' letter transcriptions, NOT expansions.
SOLVED: inscriptions / amulet formulas whose expansion is secured by full words or by a
contemporary key (used for letter->word statistics).
FORMULAS: Latin liturgical / biblical texts (Vulgate, Roman rite, Romano-Germanic
Pontifical) a 12th-13th c. invocation could abbreviate. Public-domain texts typed from
the standard Latin; checked words only, no translation.
"""

TARGETS = {
    # van Hasselt, Madoc 28/2 (2014) afb. 1 (= Daniel inscription.txt); Z for printed "7"
    "alphen_A": "BENEDOXOFTISSCSDRRISCDICECMTINIUSCSDNI",
    "alphen_B": "DIOXMTINIUSESDIOMTINIUSCSDICCCMTDICIIZISI",
    # Witham, as BL 2015 / Daniel inscription.txt
    "witham_BL": "NDXOXCHWDRGHDXORVI",
    # Witham, as read here from the BM photograph (BL blog 2015 image) -- see TRANSCRIPTION.md
    "witham_new": "NDXOXCHWDNCHDXORVI",
}

SIBLINGS = {
    # Wagner, Worley, Holst Blennow, Beckholmen, WKK 51 (2009)
    "karlstad": ("ERTISSDXCNERTISSDX", "Wagner et al. 2009 p.24 (both faces identical)"),
    "fyris74": ("SCSDXCEROXMATRCIIISSCSDXCERNISSCSDXMTOERISC", "Wagner et al. 2009 p.30"),
    "w897_a": ("NREHRISSDXCIC", "Wagner et al. 2009 p.33 (W 897, DHM Berlin)"),
    "w897_b": ("NEHRISSDXCNERISS", "Wagner et al. 2009 p.33"),
    "w879_a": ("NEHDXOEHRNISSDX", "Wagner et al. 2009 p.33 (W 879 obverse, written twice)"),
    "w879_b": ("NRISSDVIX", "Wagner et al. 2009 p.33 (W 879 reverse)"),
    "w879_c": ("SBENIS", "Wagner et al. 2009 p.33"),
    "marburg": ("NEHDXOEHRNISSDXOEHRNISS", "Wagner et al. 2009 p.33"),
    "w1830_a": ("SCSMAOAUTERRINIUS", "Wagner et al. 2009 p.30"),
    "w1830_b": ("CEIINISROXMTINIUSRN", "Wagner et al. 2009 p.30"),
    "stomer_a": ("NEDRINFISSDRNFISCCDXMAISSDRIFISSDRIN", "Wagner et al. 2009 fn 80 (their reading of Wegeli fig. 32)"),
    "stomer_b": ("NEDRIATNGDRINFISRCCDRINCDRINFISSDRINEN", "Wagner et al. 2009 fn 80"),
    "finland_a": ("BENEDICATNTVSDOCATRAOAO", "Wagner et al. 2009 p.35 (Lappaaho 1964 tab. 28), lacunae dropped"),
    "finland_b": ("ETIVSMIETDICITMAVRICIVSBEN", "Wagner et al. 2009 p.35, lacunae dropped"),
    "oldenburg": ("NEDRCNEDRUSDRCNEDRUI", "Post 1926-28 via Wagner et al. 2009 fn 58/82"),
    "danish_a": ("SCSPETRNNS", "Wagner et al. 2009 fn 20 (NM D8801)"),
    "danish_b": ("BENEDICATNTIUSETMAT", "Wagner et al. 2009 fn 20"),
    "fyris78": ("NIA", "Wagner et al. 2009 p.21"),
    # secondary (BL blog commenters, 2015) -- flagged, not used for conclusions
    "stevensweert*": ("NEXORENEXORENEXORENEXORENS", "BL blog comment p.3 (2015), unverified"),
    "berg*": ("RGDIEUNSDXGDIEUNSDIEUN", "BL blog comment p.3 (2015), unverified"),
}

# Controls: inscriptions of other, unrelated types (maker's names, spelled formulas)
CONTROLS = {
    "ulfberht": "VLFBERHT",
    "innomine": "INNOMINEDOMINI",
    "gicelin": "GICELINMEFECIT",
    "homodei": "HOMODEI",
    "ingelrii": "INGELRIIMEFECIT",
}

# Solved acronym / abbreviation formulas with secure expansions (amulet, medal, coin, liturgy)
SOLVED = [
    ("CSPB", "Crux Sancti Patris Benedicti", "St Benedict medal (legend attested 1647)"),
    ("CSSML NDSMD", "Crux sancta sit mihi lux non draco sit mihi dux", "St Benedict medal"),
    ("VRSNSMV SMQLIVB", "Vade retro Satana numquam suade mihi vana sunt mala quae libas ipse venena bibas", "St Benedict medal"),
    ("INRI", "Iesus Nazarenus rex Iudaeorum", "John 19:19, crucifixes"),
    ("AGLA", "Atta gibor leolam Adonai", "Hebrew amulet acronym on medieval rings/brooches"),
    ("IHS", "Iesus", "nomen sacrum"),
    ("XPS", "Christus", "nomen sacrum"),
    ("DNS", "Dominus", "standard contraction"),
    ("DNI", "Domini", "standard contraction"),
    ("DS", "Deus", "standard contraction"),
    ("DI", "Dei", "standard contraction"),
    ("SCS", "Sanctus", "standard contraction; marked on Fyris 74 (Wagner 2009)"),
    ("XC", "Christus", "Greek-letter nomen sacrum"),
    ("IN NOMINE DO", "In nomine Domini", "Radhus sword SHM 34525 (Wagner 2009)"),
    ("BENEDICAT", "benedicat", "Danish NM D8801, Finland (Wagner 2009)"),
    ("XVXRXI", "Christus vincit Christus regnat Christus imperat", "laudes; spelled on the Vienna Mauritius sword crossguard (Madoc 2014 n.11)"),
    ("IAPMII", "Iesus autem transiens per medium illorum ibat", "Luke 4:30; English nobles 1344+ (spelled)"),
]

FORMULAS = {
    "in_nomine_domini": "in nomine domini amen",
    "in_nomine_patris": "in nomine patris et filii et spiritus sancti amen",
    "adiutorium": "adiutorium nostrum in nomine domini qui fecit caelum et terram",
    "sit_nomen": "sit nomen domini benedictum ex hoc nunc et usque in saeculum",
    "benedictus_qui_venit": "benedictus qui venit in nomine domini osanna in excelsis",
    "ps143_benedictus": "benedictus dominus deus meus qui docet manus meas ad proelium et digitos meos ad bellum",
    "laudes": "christus vincit christus regnat christus imperat christus ab omni malo nos defendat",
    "ave_maria": "ave maria gratia plena dominus tecum benedicta tu in mulieribus et benedictus fructus ventris tui",
    "pater_noster": "pater noster qui es in caelis sanctificetur nomen tuum adveniat regnum tuum fiat voluntas tua sicut in caelo et in terra",
    "agnus_dei": "agnus dei qui tollis peccata mundi miserere nobis agnus dei qui tollis peccata mundi dona nobis pacem",
    "sanctus": "sanctus sanctus sanctus dominus deus sabaoth pleni sunt caeli et terra gloria tua osanna in excelsis",
    "gloria_patri": "gloria patri et filio et spiritui sancto sicut erat in principio et nunc et semper",
    "iesus_autem": "iesus autem transiens per medium illorum ibat",
    "inri": "iesus nazarenus rex iudaeorum",
    "verbum_caro": "verbum caro factum est et habitavit in nobis",
    "o_rex_gloriae": "o rex gloriae christe veni cum pace",
    "deus_in_adiutorium": "deus in adiutorium meum intende domine ad adiuvandum me festina",
    "kyrie": "kyrie eleison christe eleison kyrie eleison",
    "christe_audi": "christe audi nos christe exaudi nos",
    "sancta_maria": "sancta maria ora pro nobis sancta dei genitrix ora pro nobis",
    "sancte_michael": "sancte michael archangele defende nos in proelio",
    "sancte_martine": "sancte martine ora pro nobis",
    "sancte_mauriti": "sancte mauriti ora pro nobis",
    "trisagion": "sanctus deus sanctus fortis sanctus immortalis miserere nobis",
    "domine_iesu": "domine iesu christe fili dei vivi miserere nobis",
    "ps34_iudica": "iudica domine nocentes me expugna impugnantes me apprehende arma et scutum et exsurge in adiutorium mihi",
    "ps44_accingere": "accingere gladio tuo super femur tuum potentissime",
    "ps67_exsurgat": "exsurgat deus et dissipentur inimici eius et fugiant qui oderunt eum a facie eius",
    "ps26_dominus_illuminatio": "dominus illuminatio mea et salus mea quem timebo",
    "ps66_benedicat": "benedicat nos deus deus noster benedicat nos deus et metuant eum omnes fines terrae",
    "ps113_non_nobis": "non nobis domine non nobis sed nomini tuo da gloriam",
    "ecce_crucem": "ecce crucem domini fugite partes adversae vicit leo de tribu iuda radix david",
    "ichthys": "iesus christus dei filius salvator",
    "te_deum": "te deum laudamus te dominum confitemur",
    "magnificat": "magnificat anima mea dominum et exsultavit spiritus meus in deo salutari meo",
    "credo": "credo in unum deum patrem omnipotentem factorem caeli et terrae",
    "o_crux": "o crux ave spes unica",
    "dominus_vobiscum": "dominus vobiscum et cum spiritu tuo",
    "dominus_iesus_christus": "dominus iesus christus",
    "benedictio_ensis": ("exaudi quaesumus domine preces nostras et hunc ensem quo hic famulus tuus se "
                         "circumcingi desiderat maiestatis tuae dextera benedicere dignare quatenus defensio "
                         "atque protectio possit esse ecclesiarum viduarum orphanorum omniumque deo servientium "
                         "contra saevitiam paganorum"),
    "benedicite": "benedicite omnia opera domini domino laudate et superexaltate eum in saecula",
    "in_manus_tuas": "in manus tuas domine commendo spiritum meum",
    "salve_regina": "salve regina mater misericordiae vita dulcedo et spes nostra salve",
    "regina_caeli": "regina caeli laetare alleluia quia quem meruisti portare alleluia",
}

# Contractions allowed as single units (letters -> one word), standard medieval nomina sacra
UNITS = {
    "xps": {"christus", "christe", "christi", "christo"},
    "xpc": {"christus"}, "xc": {"christus", "christe"}, "x": {"christus", "christe", "christi", "christo"},
    "ihs": {"iesus"}, "is": {"iesus"}, "ihc": {"iesus"},
    "dns": {"dominus"}, "dni": {"domini"}, "dne": {"domine"}, "dno": {"domino"}, "dnm": {"dominum"},
    "ds": {"deus"}, "di": {"dei"}, "do": {"deo", "domino"},
    "scs": {"sanctus"}, "sca": {"sancta"}, "sce": {"sancte"}, "sci": {"sancti"},
    "ch": {"christus", "christe", "christi", "christo"},  # vernacular-style, allowed but flagged
}
