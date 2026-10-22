# Řešení cvičení 6 – Vestavěné funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se uživatele na dvě čísla a vypiš to větší z nich.

prvni = int(input("Zadej první číslo: "))
druhe = int(input("Zadej druhé číslo: "))
print(max(prvni, druhe))


prvni = int(input("Zadej první číslo: "))
druhe = int(input("Zadej druhé číslo: "))
if prvni > druhe:
    print("Větší z nich je:", prvni)
else:
    print("Větší z nich je:", druhe)    
print("Větší z nich je:", max(prvni, druhe))