# Cvičení 1 – Seznamy
# Doplň kód pod zadání a soubor spusť (Run).

# Vytvoř seznam pěti svých oblíbených filmů. Vypiš:
#    - první film,
#    - poslední film,
#    - první tři filmy jako výřez,
#    - všechny filmy, každý na vlastní řádek s pomlčkou na začátku,
#    - kolik filmů v seznamu je.
filmy = ["The Matrix", "Shrek", "Hledá se Nemo", "Harry Potter", "Pán prstenů"]   
print(filmy[0])  # první film
print(filmy[-1])  # poslední film
print(filmy[:3])  # první tři filmy jako výřez
for film in filmy:  # všechny filmy, každý na vlastní řádek s pomlčkou na začátku
    print(f"- {film}")
print(f"Počet filmů: {len(filmy)}")  # kolik filmů v seznamu je

