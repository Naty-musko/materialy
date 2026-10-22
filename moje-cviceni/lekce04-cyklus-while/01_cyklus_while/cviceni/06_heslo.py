# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

pokusy = 0
while pokusy < 3:
    heslo = input("Zadej heslo: ")
    if heslo == "pyladies":
        print("Vítej!")
        break
    else:
        pokusy += 1
        print(f"Špatné heslo. Zbývá ti {3 - pokusy} pokusů.")
if pokusy == 3:     
    print("Zablokováno.")
    


