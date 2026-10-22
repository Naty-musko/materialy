# ---------------------------------------------
#  Vnořené cykly (cyklus v cyklu)
# ---------------------------------------------
# Cyklus můžeme dát dovnitř jiného cyklu. Říká se tomu vnořený cyklus.
# Pravidlo: pro KAŽDÝ průchod vnějšího cyklu proběhne celý vnitřní cyklus.
# Spusť soubor a sleduj výsledky.


# Představ si hru o třech kolech a v každém kole dva pokusy.
# Vnějším cyklem jsou kola, vnitřním pokusy v rámci jednoho kola:
for kolo in range(1, 4):
    print("Kolo", kolo)
    for pokus in range(1, 3):
        print("  pokus", pokus)


for i in range(5):
    print("i:", i)
    for j in range(4):
        print(" kolo", i, ": pokus", j)
    print("Konec kola", i)  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
print("Konec cyklu")  # toto je už venku, takže se vypíše jen jednou na konci



for tyden in range(1, 4):
    print("Týden", tyden)
    for den in range(1, 8):
        print("  den", den)
    print("Konec týdne", tyden)  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
print("Konec cyklu")  # toto je už venku, takže se vypíše jen jednou na konci


for mesic in range(1, 4):
    print("Měsíc", mesic)
    for tyden in range(1, 5):
        print("  Týden", tyden)
        for den in range(1, 8):
            print("    den", den)
        print("  Konec týdne", tyden)  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
    print("Konec měsíce", mesic)  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
print("Konec cyklu")  # toto je už venku, takže se vypíše jen jednou na konci



for tyden in range(1, 4):
    print("Týden", tyden)
    for den in range(1, 8):
        print("  den", den)
    print("Konec týdne", tyden)  # toto už je uvnitř cyklu, takže se vypíše po každém čísle
print("Konec cyklu") 


# Odsazení určuje, co je uvnitř čeho: vnitřní cyklus je odsazený uvnitř
# vnějšího a řádek "Kolo" se provede jednou za kolo, "pokus" dvakrát.


# Vnořený cyklus se hodí, když chceme víc hodnot na JEDEN řádek a pak
# skočit na další. Vypíšeme třeba mini kalendář – tři týdny pod sebou,
# každý s čísly dnů 1 až 7. Vnitřní cyklus vypíše jeden řádek (týden),
# vnější ho zopakuje. Pomůže end (drží řádek) a prázdný print() (zalomí):
for tyden in range(1, 4):
    for den in range(1, 8):
        print(den, end=" ")       # dny 1 až 7 vedle sebe
    print()                       # po celém týdnu skoč na nový řádek
