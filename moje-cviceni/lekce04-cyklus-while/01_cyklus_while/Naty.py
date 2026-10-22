from random import randrange

hod = randrange(1, 7)
while hod > 1 and hod < 6:
    if hod == 1:
        print("Kon4ime.")
        break
    print("Hodil jsi", hod, "– zkus to znovu.")
    hod = randrange(1, 7)
if hod == 1:
    print("Hodil jsi 1 – kon4ime.")
else:   
    print("Hodil jsi", hod, "– gratuluju!")



from random import randrange

hod = randrange(1, 7)
while hod > 1 and hod < 6:
    if hod == 1:
        print("Kon4ime.")
        break
    print("Hodil jsi", hod, "– zkus to znovu.")
    hod = randrange(1, 7)
if hod == 1:
    print("Hodil jsi 1 – kon4ime.")
else:   
    print("Hodil jsi", hod, "– gratuluju!")


    while True:
        odpoved=input("Zjak sxe mas: ")
        if odpoved == "spatne":
            print("tak to s tebou nebodu bavit!")
            break   
        print("ahoj.")
    print("Vítej!")



soucet = 0
while True:
    odpoved = input("Zadej číslo: ")
    if odpoved == "konec":
        break

    cislo = int(odpoved)
    if cislo < 0:
        print("Zadal jsi záporné číslo, zkus to znovu.")
        continue
    soucet = cislo + soucet
print("Součet je", soucet)  





soucet = 0
while True:
    odpoved = input("Zadej číslo: ")
    if odpoved == "konec":
        break
    
    cislo = float(odpoved)
    if cislo < 0:
        print("Zadal jsi záporné číslo, zkus to znovu.")
        continue
    soucet = cislo + soucet
print("Součet je", soucet)  



soucet = 0
for i in range(0,5):
    odpoved = input("Zadej číslo: ")
    if odpoved == "konec":
        break
    
    cislo = float(odpoved)
    if cislo < 0:
        print("Zadal jsi záporné číslo, zkus to znovu.")
        continue
    soucet = cislo + soucet
print("Součet je", soucet)  