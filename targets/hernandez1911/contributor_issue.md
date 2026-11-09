# The contributor's submission (issue #351, William Echols, 9 Nov 2026), as filed

Target: catalogue 1462. CEHM-Carso, Archivo Federico González Garza (Fondo CMXV), CMXV.15.1420.3-6: Federico González Garza sent the telegram from El Paso, Texas, to Braulio Hernández in Presidio, Texas, on 27 March 1911. Record: https://www.cehm.org.mx/Buscador/FichaBasica/12723?Tipo=A

Key: swap characters L<->A, N<->E, R<->I, S<->O and T<->U in place and in both directions; all other characters are unchanged. Key card: Hernández key card, CEHM CMXV.16.1557.1, scan 16.

All four coded words decode exactly (29 of 29 letters). Published before: none found. Tools: GPT-6.1 Sol worked independently in Codex. Credit: William Echols.

Condensed decoding:

    key = str.maketrans("LNRSTAEIOU", "AEIOULNRST")
    ciphertext = "VRAALIINLA OLADIL AANVLEDS CLESE"
    plaintext = ciphertext.translate(key)
