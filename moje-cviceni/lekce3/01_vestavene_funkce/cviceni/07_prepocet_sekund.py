# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.
pocet_sekund = int(input("Zadej počet sekund: "))
hodiny = pocet_sekund // 3600
zbytek_sekund = pocet_sekund % 3600
minuty = zbytek_sekund // 60
sekundy = zbytek_sekund % 60
print(f"{hodiny}:{minuty}:{sekundy}")   


