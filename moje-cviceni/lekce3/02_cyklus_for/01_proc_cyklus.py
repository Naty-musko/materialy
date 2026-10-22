# ---------------------------------------------
#  Proč cyklus
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Často chceme něco zopakovat víckrát. Psát to pořád dokola je zdlouhavé –
# a co teprve stokrát! Od toho je cyklus: řekne Pythonu „udělej tohle N-krát".


# Takhle by to vypadalo bez cyklu – nudné a zbytečně dlouhé:
print("Ahoj")
print("Ahoj")
print("Ahoj")


# Cyklus for udělá totéž za nás. range(3) znamená tři opakování:
for cislo in range(3):
    print("Ahoj")

for cislo in range(3): 
    print("Ahoj", str(cislo))  # cislo je proměnná, do které cyklus postupně ukládá čísla z range


for i in range(3):
    if(i % 2 == 0):  # vypíše jen sudá čísla
        print("sude cislo:", i)
    else:
        print("liche cislo:", i)  
print("Konec cyklu")



for i in range(3, 9):  # range(3, 9) znamená čísla od 3 do 8 (9 už ne)
    if(i % 2 == 0):  # vypíše jen sudá čísla
        print("sude cislo:", i)
    else:
        print("liche cislo:", i)  
print("Konec cyklu")


for i in range(3, 9):  # range(3, 9) znamená čísla od 3 do 8 (9 už ne)
    print("cislo:", i)
    if(i % 2 == 0):  # vypíše jen sudá čísla
        print("sude cislo:", i)
    else:
        print("liche cislo:", i)  
print("Konec cyklu")


for i in range(3, 9):  # range(3, 9) znamená čísla od 3 do 8 (9 už ne)
    print("cislo:", i)
    if(i % 2 == 0):  # vypíše jen sudá čísla
        print("sude cislo:", i)
    else:
        print("liche cislo:", i)  
    print("Konec")  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
print("Konec cyklu")






# Jak takový cyklus přečíst:
#   for      = klíčové slovo (opakuj)
#   cislo    = proměnná, do které cyklus postupně ukládá čísla z range
#   range(3) = kolik čísel projdeme (a tím i kolikrát se cyklus zopakuje)
#   :        = dvojtečka na konci řádku (stejně jako u if z minulé lekce)
#   odsazení = řádky odsazené (Tab) patří dovnitř cyklu a opakují se


# Ta proměnná se opravdu postupně mění. range(5) dá čísla 0 až 4
# (pět čísel, poslední je o jedna míň – to už známe z minula):
for cislo in range(5):
    print(cislo)          # vypíše 0, 1, 2, 3, 4 – každé na svůj řádek
