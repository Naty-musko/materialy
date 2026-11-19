# Cvičení 3 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# U fotokoutku na večírku stojí fronta. Dokud v ní někdo je, vezmi
#    první na řadě a vypiš "Fotí se: ...". Na konci vypiš
#    "Fronta je prázdná.".

fronta = ["Anna", "Petra", "Jana"]  

while len(fronta) > 0:
    osoba = fronta.pop(0)
    print(f"Fotí se: {osoba}")

print("Fronta je prázdná.")
