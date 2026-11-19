# Cvičení 4 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na větu. Vypiš, kolik má slov. Pak ji vypiš se slovy
#    v opačném pořadí.
#
#      Věta: Python je fajn
#      Slov: 3
#      fajn je Python

veta = input("Zadej větu: ")   # načti větu
slova = veta.split()          # rozděl na slova
print(f"Slov: {len(slova)}")  # vypiš počet slov
print(" ".join(slova[::-1]))  # vypiš slova obráceně