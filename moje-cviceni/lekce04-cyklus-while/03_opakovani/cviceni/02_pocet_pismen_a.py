# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.
slovo = input("Zadej slovo: ")
pocet_a = 0
for pismeno in slovo:
    if pismeno == "a":
        pocet_a += 1
print("Písmeno a se vyskytuje", pocet_a, "krát.")

