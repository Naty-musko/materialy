# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".
if True:
    tah_hrac1 = input("Tah hráče 1: ")
    tah_hrac2 = input("Tah hráče 2: ")
    if tah_hrac1 == tah_hrac2:
        print("Remíza.")
    elif (tah_hrac1 == "kamen" and tah_hrac2 == "nuzky") or (tah_hrac1 == "nuzky" and tah_hrac2 == "papir") or (tah_hrac1 == "papir" and tah_hrac2 == "kamen"):
        print("Vyhrál hráč 1.")
    else:
        print("Vyhrál hráč 2.") 

