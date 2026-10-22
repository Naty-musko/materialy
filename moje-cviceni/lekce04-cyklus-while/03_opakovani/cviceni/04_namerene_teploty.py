# Cvičení 4 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.
teploty = []
while True:
    teplota = float(input("Zadej naměřenou teplotu: "))
    teploty.append(teplota)
    dalsi = input("Další? (ano/ne) ")
    if dalsi.lower() == "ne":
        break   

if teploty:
    nejvyssi_teplota = max(teploty)
    print("Nejvyšší teplota je:", nejvyssi_teplota)     