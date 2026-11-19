# Cvičení 1 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci nadpis(text), která vypíše text a pod něj čáru
#    z pomlček dlouhou přesně jako ten text.
#    Vyzkoušej ji na dvou různě dlouhých nadpisech.

def nadpis(text):
    print(text)
    print("-" * len(text))

nadpis("Lekce 5")
nadpis("Vlastní funkce a návratové hodnoty")
