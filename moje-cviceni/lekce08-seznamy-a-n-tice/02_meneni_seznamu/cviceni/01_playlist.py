# Cvičení 1 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# Spravuješ playlist na večírek. Postupně:
#    - první skladbu přesuň na konec,
#    - na druhé místo vlož přání "Jožin z bažin",
#    - odeber skladbu "Holky z naší školky",
#    - vypiš playlist.
#
#    Vyjít má:  ['Severní vítr', 'Jožin z bažin', 'Trezor']

playlist = ["Trezor", "Severní vítr", "Holky z naší školky"]

playlist.append(playlist.pop(0))  # přesun první skladby na konec
playlist.insert(1, "Jožin z bažin")  # vložení přání na druhé místo
playlist.remove("Holky z naší školky")  # odebrání skladby

print(playlist)
