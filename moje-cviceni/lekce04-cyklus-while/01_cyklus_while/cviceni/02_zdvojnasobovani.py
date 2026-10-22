# Cvičení 2 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Začni s číslem 1 a v cyklu ho pořád zdvojnásobuj. Zastav se,
#    jakmile přesáhne 1000, a vypiš, kolikrát jsi ho zdvojnásobila.

cislo = 1
pocet = 0                   

while cislo <= 1000:
    cislo *= 2
    pocet += 1

print(f"Číslo bylo zdvojnásobeno {pocet}krát.")     