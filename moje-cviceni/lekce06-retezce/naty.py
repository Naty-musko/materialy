def odpocet(od):
    for i in range(od, 0, -1):
        print(i)
    print("Teď!")
odpocet(3)
odpocet(5)



def je_heslo_silne(heslo):
    #return len(heslo) >= 8
    if len(heslo) < 3:
        return false
    elif len(heslo) < 15:
        return false
    else:
        return true


def prihlaseni():
    heslo = input("Zadej heslo: ")
    if je_heslo_silne(heslo):
        print("Heslo je silné.")
    else:
        print("Heslo je slabé.")

def zeptej_se_na_jmeno():
    jmeno = input("Zadej jméno: ")
    print(f"Ahoj, {jmeno}!")


def zeptej_se_na_jmenp ():
    return input("Zadej jméno: ")


def zeptej_se_na_email():
    return input("Zadej email: ")



def prihla3eni_emailem():
    jmeno=zeptej_se_na_jmeno()
    heslo=zeptej_se_na_heslo
    if je_heslo_dlouhe(heslo)
        print("Vitej", jmeno):

    else:
    print("Heslo ma spatnou delku")
prihla3eni_emailem

