heslo = input("Zadej své jméno: ")
while len(heslo) < 3:
    print("Jméno musí mít alespoň 3 znaky.")
    heslo = input("Zadej své jméno: ")
print(f"Dobrý den, {heslo}!")                          



heslo = input("Zadej heslo: ")
while len(heslo) != "pyladies":
    print("Špatné heslo, zkus to znovu.")
    heslo = input("Zadej heslo: ")
print(f"Dobrý den, {heslo}!")  



