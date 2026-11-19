# Cvičení 2 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# Kamarádka ti poslala tajnou zprávu: skrývá se v prvních písmenech
#    slov. Postav seznam prvních písmen a pak je spoj do jednoho slova.
#
#    Vyjít má:  DORT

slova = ["Dům", "Okno", "Ryba", "Tužka"]

prvni_pismena = [slovo[0] for slovo in slova]
tajna_zprava = "".join(prvni_pismena)
print(tajna_zprava)
