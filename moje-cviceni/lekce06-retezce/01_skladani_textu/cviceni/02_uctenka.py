# Cvičení 2 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš účtenku tak, aby ceny byly pod sebou: název zarovnaný doleva
#    na dvanáct míst, cenu doprava na osm míst se dvěma desetinnými
#    místy. Na konec přidej řádek se součtem.
#
#    Když je součet vyšší než 150 Kč, přidej ještě řádek se slevou
#    deset procent a řádek s cenou po slevě.

polozka1 = "káva"
cena1 = 59
polozka2 = "dort"
cena2 = 84.5
polozka3 = "čaj"
cena3 = 45

print(f"{'Položka':<12}{'Cena':>8}")
print(f"{polozka1:<12}{cena1:>8.2f}")
print(f"{polozka2:<12}{cena2:>8.2f}")
print(f"{polozka3:<12}{cena3:>8.2f}")

soucet = cena1 + cena2 + cena3
print(f"{'Součet':<12}{soucet:>8.2f} Kč")

if soucet > 150:
    sleva = soucet * 0.10
    cena_po_sleve = soucet - sleva
    print(f"{'Sleva 10 %':<12}{sleva:>8.2f} Kč")
    print(f"{'Po slevě':<12}{cena_po_sleve:>8.2f} Kč")
