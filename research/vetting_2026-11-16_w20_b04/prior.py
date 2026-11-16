"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 2113: ['GEN MSS MISC', 'Group 577', 'Beinecke', 'Bible'],
 2106: ['Streynsham', 'Osborn c491', 'Croston'],
 2515: ['Johann Moritz', 'Weiman', 'Nassau-Siegen', 'Rep. 11'],
 2514: ['Hoverbeck', 'Rep. 9'],
 2513: ['Brandt', 'Brandenburg', 'Frederick William', 'Friedrich Wilhelm'],
 2782: ['Rambaud', 'Ms. fr. 445', 'Genève', 'Geneve'],
 2781: ['Ivernois', 'Jacobi', 'Eynard', 'Kleiber', 'suppl. 976'],
 1239: ['Cascais', 'Pires de Castro', 'MSS. 14', 'Pereira de Castro', 'João IV', 'Joao IV'],
 1238: ['Correia de Abreu', 'Fonseca e', 'MSS. 41'],
 1242: ['Luís da Cunha', 'Luis da Cunha', 'Azevedo Coutinho', 'COD. 4417', 'Cunha'],
 1241: ['Esquilache', 'PBA. 636', 'Motim', 'Ayres de S'],
 2275: ['Pombal', 'AP/Mc'],
 1237: ['Ribeiro Saraiva', 'Saraiva', 'MSS. 99', 'Cadaval', 'Beira'],
 2270: ['Ribeiro Saraiva', 'MSS. 169'],
 2271: ['Fontes Pereira', 'FPM', 'Rebelo'],
 2274: ['Tavares de Andrade', 'Carlos de Andrade', 'EMUS13'],
 2780: ["Aubign", 'Tronchin'],
 1847: ['Noyers', 'Gonzague', 'Gonzaga', 'Chantilly', 'Ms 1888'],
}
ids = [int(a) for a in sys.argv[1:]] or list(TERMS)
for i in ids:
    print('=' * 20, i)
    for t in TERMS[i]:
        for name, src in (('TOMOKIYO', T), ('LASRY', G)):
            hits = [m.start() for m in re.finditer(re.escape(t), src, re.I)]
            if hits:
                print(f'  {name} {t!r}: {len(hits)} hit(s); first: ...{" ".join(src[max(0,hits[0]-120):hits[0]+160].split())}...')
            else:
                print(f'  {name} {t!r}: 0')
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py'] + TERMS[i], capture_output=True, text=True, encoding='utf8')
    print('  KNOWN.PY:'); print('   ' + '\n   '.join((r.stdout + r.stderr).strip().splitlines()[:40]))
