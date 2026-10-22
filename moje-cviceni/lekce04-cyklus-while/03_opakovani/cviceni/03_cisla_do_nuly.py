# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))

while cislo != 0:
    cislo = int(input("Zadej číslo: "))
    soucet += cislo
    pocet += 1

if pocet > 0:
    prumer = soucet / pocet
    print("Součet je", soucet)
    print("Počet čísel je", pocet)
    print("Průměr je", round(prumer, 1))
else:
    print("Nebyla zadána žádná čísla.")