"""Run known.py per lead (filtered) and grep Tomokiyo unsolved.htm and Lasry GL.htm (fetched 15 Nov 2026)."""
import subprocess, re, html, sys, pathlib
SP = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad')
def txt(p):
    s = (SP / p).read_text(encoding='utf-8', errors='replace')
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)))
U, G = txt('unsolved.htm'), txt('GL.htm')
TERMS = {
 '2710': ['FRIAS,C.1815', 'Alonso de C', 'Frias'],
 '2709': ['FRIAS,C.635', 'FRIAS,C.1389', 'Conde de Haro', 'Haro'],
 '2708': ['FRIAS,C.1887', 'Ligni', 'Ligne', 'Oropesa'],
 '2711': ['MICHELENA,C.18', 'Sánchez Román', 'Sanchez Roman'],
 '2699': ['OSUNA,C.1634', 'Condestable', 'Velasco', 'Arcos'],
 '2700': ['OSUNA,C.1634,D.124', 'Treviño', 'Trevino', 'Bañuelos'],
 '2701': ['OSUNA,C.1635', 'Muñoz de C', 'Munoz de C', 'Pedro de Castilla'],
 '2702': ['OSUNA,CP.56', 'Téllez Girón', 'Tellez Giron', 'Osuna'],
 '2703': ['OSUNA,C.1977', 'Pastrana', 'Mondragón', 'Valdetoro'],
 '2704': ['OSUNA,CT.535', 'Caracena', 'Ronquillo'],
 '2707': ['OSUNA,CT.15', 'OSUNA,CT.18', 'Galarreta', 'Gradiñán', 'Antequera', 'Infantado'],
 '2706': ['OSUNA,CT.260', 'Navarrete', 'Tercia'],
 '2705': ['OSUNA,CT.80', 'Peña Zúñiga', 'Pena Zuniga'],
 '2930': ['OP16696', 'Lourenço Marques', 'Lourenco Marques', 'Delagoa', 'Berne'],
 '2931': ['OP16752', 'OP16773', 'OP16774', 'OP16775'],
 '2932': ['OP19560', 'Moçambique', 'Mozambique'],
 '2933': ['OP17197', 'caminhos-de-Ferro no Cabo'],
 '2935': ['MU-GM', 'Teleg0', 'Ministério do Ultramar', 'Angola'],
}
for lid in (sys.argv[1:] or TERMS):
    print('########', lid)
    for t in TERMS[lid]:
        r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py', t], capture_output=True, text=True, encoding='utf-8')
        lines = [l for l in r.stdout.splitlines() if l.startswith('  ') and 'leads.json' not in l and 'candidates.json' not in l]
        print(f'  known.py "{t}": {len(lines)} hits outside leads/candidates')
        for l in lines[:6]: print('     ', l.strip()[:260])
        for name, T in (('TOMOKIYO', U), ('LASRY', G)):
            for m in re.finditer(re.escape(t), T, re.I):
                print(f'     {name}: ...{T[max(0,m.start()-150):m.end()+150]}...')
