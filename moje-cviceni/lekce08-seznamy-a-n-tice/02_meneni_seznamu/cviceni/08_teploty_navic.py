# Cvičení 8 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# V lekci 4 sis z naměřených teplot pamatovala jen nejvyšší. Teď si
#    ulož všechny. Ptej se "Teplota: ", dokud uživatel nenapíše "konec".
#    Pak vypiš nejvyšší teplotu, průměr a kolik teplot bylo nad průměrem.
#
#      Teplota: 10
#      Teplota: 20
#      Teplota: 30
#      Teplota: konec
#      Nejvyšší: 30
#      Průměr: 20.0
#      Nad průměrem: 1

teploty = []
while True:
    vstup = input("Teplota: ")
    if vstup == "konec":
        break
    teploty.append(int(vstup))

if teploty:
    print(f"Nejvyšší: {max(teploty)}")
    prumer = sum(teploty) / len(teploty)
    print(f"Průměr: {prumer}")
    nad_prumerem = len([t for t in teploty if t > prumer])
    print(f"Nad průměrem: {nad_prumerem}")
else:
    print("Nebyly zadány žádné teploty.")
