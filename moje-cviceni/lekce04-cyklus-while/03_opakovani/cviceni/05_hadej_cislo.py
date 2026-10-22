# Cvičení 5 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange
hadej = randrange(1, 21)
pokusy = 0
while pokusy < 5:
    tip = int(input("Hádej číslo od 1 do 20: "))
    pokusy += 1
    if tip < hadej:
        print("Moc malé.")
    elif tip > hadej:
        print("Moc velké.")
    else:
        print("Trefa!")
        break
if tip != hadej:
    print(f"Správné číslo bylo: {hadej}.")    
    
      


