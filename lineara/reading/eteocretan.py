"""Linear A against Eteocretan, the non-Greek language of Praisos and Dreros written in Greek letters.

Eteocretan (7th-3rd c. BC) is often suggested as a late descendant of Minoan. Its sounds are known because it
is written alphabetically, but most of it is written without word division. So both sides are spelled the
Linear B way (lang_test.spell) and Linear A words are sought inside the Eteocretan syllable stream, one stream
per unbroken stretch of text (lacunae and word dividers break a stretch).

Texts: R. A. Brown's transcriptions of the five certain inscriptions (Dreros 1 and 2, Eteocretan parts only;
Praisos 1-3), as published on his Eteocretan pages (archived 2022-2025), which follow autopsy and agree with
Duhoux 1982 in readings. The disputed Psychro ("Epioi") stone is scored separately.

Nulls and controls:
  * Linear A sign values shuffled within frequency bins (as in soundvalues.py), 2,000 runs;
  * equal-size samples of word shapes from unrelated languages (Hawaiian, Maori, Yoruba), to show how often
    arbitrary real words turn up inside a stream this short;
  * positive control: Linear B words (a true relative of the Greek) sought in about 400 letters of Greek
    (Odyssey 19.172-177 and Strabo 10.475, which name Cretans; and, as a neutral text, Iliad 1.1-7 with
    Odyssey 1.1-4) under the same rules, with the same shuffle null applied to the
    Linear B values.
"""
from collections import Counter
import json
from pathlib import Path
import random
import re
import sys
import unicodedata as ud

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lang_test as L  # noqa: E402
import names_lb as N  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Brown's Roman transcriptions; '|' word divider, '--' lacuna, '.' illegible letter, 'vac' blank.
ETEOCRETAN = {
    'Dreros 1 (Eteocretan lines)': '--.rmaw|et|isalabre|komn --.d|men|inai|isaluria|lmo',
    'Dreros 2 (Eteocretan word)': '--s|tuprmēriēia',
    'Praisos 1': '--nkalmitke os barz̵e a-- o-- --ark.agset med. arkrkokles de.-- --asegdnanit',
    'Praisos 2': ('--onadesiemetepimitspʰa --do..iaralapʰraisoiinai --restnmtorsardopʰsano --satoisstepʰ.satiun '
                  '--animestepaluneutat --sanomoselospʰraisona --tsaadopʰtena-- --maprainaireri-- --ireirereie.-- '
                  '--nriranọ-- --askes-- --i.t--'),
    'Praisos 3': ('-x.nnumit --atarkomn --.ēdēsdea --sōpeirari --en tasetwseu --nnasiroukles --irermēiamarpʰ '
                  '--eirerpʰinsdan --mamdedikark --risrairaripʰ --.nneikarx --taridoēi --enba --dnas'),
}
PSYCHRO = {'Psychro "Epioi" (disputed)': 'epioi zētʰantʰē enetē par sipʰai'}
GREEK = ("Κρήτη τις γαῖ' ἔστι μέσῳ ἐνὶ οἴνοπι πόντῳ, καλὴ καὶ πίειρα, περίρρυτος· ἐν δ' ἄνθρωποι πολλοί, "
         "ἀπειρέσιοι, καὶ ἐννήκοντα πόληες. ἄλλη δ' ἄλλων γλῶσσα μεμιγμένη· ἐν μὲν Ἀχαιοί, ἐν δ' Ἐτεόκρητες "
         "μεγαλήτορες, ἐν δὲ Κύδωνες, Δωριέες τε τριχάϊκες δῖοί τε Πελασγοί. τούτων φησὶ Στάφυλος τὸ μὲν πρὸς "
         "ἔω Δοριεῖς κατέχειν, τὸ δὲ δυσμικόν Κύδωνας, τὸ δὲ νότιον Ἐτεόκρητας ὧν εἶναι πολίχνιον Πρᾶσον, ὅπου "
         "τὸ τοῦ Δικταίου Διὸς ἱερόν· τοὺς μὲν οὖν Ἐτεόκρητας καὶ Κύδωνας αὐτόχθονας ὑπάρξαι εἰκός, τοὺς δὲ "
         "λοιποὺς ἐπήλυδας")


HOMER = ("μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος οὐλομένην, ἣ μυρί' Ἀχαιοῖς ἄλγε' ἔθηκε, πολλὰς δ' ἰφθίμους ψυχὰς "
         "Ἄϊδι προΐαψεν ἡρώων, αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν οἰωνοῖσί τε πᾶσι, Διὸς δ' ἐτελείετο βουλή, ἐξ οὗ δὴ "
         "τὰ πρῶτα διαστήτην ἐρίσαντε Ἀτρεΐδης τε ἄναξ ἀνδρῶν καὶ δῖος Ἀχιλλεύς. ἄνδρα μοι ἔννεπε, μοῦσα, "
         "πολύτροπον, ὃς μάλα πολλὰ πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσε· πολλῶν δ' ἀνθρώπων ἴδεν ἄστεα "
         "καὶ νόον ἔγνω, πολλὰ δ' ὅ γ' ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν")  # Iliad 1.1-7, Odyssey 1.1-4: no Cretan names


def stretches(text):
    """Unbroken stretches of letters, normalised to plain Latin."""
    t = text.replace('pʰ', 'p').replace('tʰ', 't').replace('kʰ', 'k').replace('z̵', 'z').replace('x', 'ks')
    t = ud.normalize('NFD', t)
    t = ''.join(ch for ch in t if not ud.combining(ch))
    t = re.sub(r'vac', ' ', t)
    return [s for s in re.split(r'[^a-z]+', t) if s]


def greek_stretches(text):
    words = []
    for w in re.findall(r"[Ͱ-Ͽἀ-῿]+", text):
        g = ud.normalize('NFD', w.lower())
        g = ''.join(ch for ch in g if not ud.combining(ch))
        words.append(''.join(L.GREEK.get(ch, ch) for ch in g))
    return [''.join(words)]  # Greek scored as continuous text, like the undivided Eteocretan


def streams(stretch_list):
    out = []
    for s in stretch_list:
        sp = L.spell(s)
        if sp:
            out.append(sp)
    return out


def contains(streams_, word):
    n = len(word)
    return any(tuple(st[i:i + n]) == word for st in streams_ for i in range(len(st) - n + 1))


def hits(streams_, words):
    return sorted(w for w in words if contains(streams_, w))


def value_null(words, streams_, rng, reps):
    freq = Counter(s for w in words for s in w)
    signs = sorted(freq, key=lambda s: -freq[s])
    size = -(-len(signs) // 10)
    bins = [signs[i:i + size] for i in range(0, len(signs), size)]
    out = []
    for _ in range(reps):
        mp = {}
        for b in bins:
            v = b[:]
            rng.shuffle(v)
            mp.update(zip(b, v))
        out.append(len(hits(streams_, {tuple(mp[s] for s in w) for w in words})))
    return out


def lower(w):
    return tuple(x.lower() for x in w)


def main(reps=2000, seed=20260923):
    rng = random.Random(seed)
    la = {lower(w) for w in L.la_types()}
    et = streams([s for t in ETEOCRETAN.values() for s in stretches(t)])
    ps = streams([s for t in PSYCHRO.values() for s in stretches(t)])
    controls_text = {'Odyssey 19 + Strabo (names Cretans)': streams(greek_stretches(GREEK)),
                     'Iliad 1.1-7 + Odyssey 1.1-4 (neutral)': streams(greek_stretches(HOMER))}
    gr = controls_text['Odyssey 19 + Strabo (names Cretans)']
    sites, _ = N.lb_vocabulary()
    lb = {w for w in sites}
    res = {'method': __doc__.strip(), 'eteocretan_syllables': sum(map(len, et)), 'greek_control_syllables': sum(map(len, gr)),
           'eteocretan_streams': ['-'.join(s) for s in et], 'tests': {}}
    for minlen in (3, 2):
        la_m = {w for w in la if len(w) >= minlen}
        lb_m = sorted(w for w in lb if len(w) >= minlen)
        real = hits(et, la_m)
        null = value_null(la_m, et, rng, reps)
        # controls: word shapes of unrelated languages, samples as large as the Linear A list
        ctrl = {}
        for name in ('Hawaiian', 'Maori', 'Yoruba'):
            forms = sorted({L.spell(w) for w, _ in L.SOURCES[name][1]()} - {None})
            forms = [f for f in forms if len(f) >= minlen]
            k = min(len(forms), len(la_m))
            ctrl[name] = round(sum(len(hits(et, set(rng.sample(forms, k)))) for _ in range(200)) / 200, 2)
        # positive control: Linear B words in the Greek text, sample of the Linear A list's size
        lb_sample = set(rng.sample(lb_m, min(len(lb_m), len(la_m))))
        pcs = {}
        for cname, cstream in controls_text.items():
            g_real = hits(cstream, lb_sample)
            g_null = value_null(lb_sample, cstream, rng, 500)
            pcs[cname] = {'syllables': sum(map(len, cstream)), 'matches': ['-'.join(w) for w in g_real],
                          'null_mean': round(sum(g_null) / 500, 2),
                          'p_ge': round((sum(n >= len(g_real) for n in g_null) + 1) / 501, 4)}
        res['tests'][f'{minlen}+ signs'] = {
            'linear_a_types': len(la_m), 'matches_in_eteocretan': ['-'.join(w).upper() for w in real],
            'null_mean': round(sum(null) / reps, 2), 'p_ge': round((sum(n >= len(real) for n in null) + 1) / (reps + 1), 4),
            'control_language_samples_mean_hits': ctrl,
            'psychro_matches': ['-'.join(w).upper() for w in hits(ps, la_m)],
            'positive_control_linear_b_in_greek': pcs}
    (ROOT / 'reading/eteocretan_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('Eteocretan syllables', res['eteocretan_syllables'], '| Greek control syllables', res['greek_control_syllables'])
    print('streams:', res['eteocretan_streams'])
    for k, v in res['tests'].items():
        print(f"== {k}: {v['linear_a_types']} Linear A types")
        print(f"   in Eteocretan: {len(v['matches_in_eteocretan'])} {v['matches_in_eteocretan']}  null {v['null_mean']}  p {v['p_ge']}")
        print(f"   unrelated-language word samples of the same size: {v['control_language_samples_mean_hits']}")
        print(f"   Psychro: {v['psychro_matches']}")
        for cname, pc in v['positive_control_linear_b_in_greek'].items():
            print(f"   positive control, Linear B words in {cname} ({pc['syllables']} syl): {len(pc['matches'])} {pc['matches'][:10]}  null {pc['null_mean']}  p {pc['p_ge']}")


if __name__ == '__main__':
    main()
