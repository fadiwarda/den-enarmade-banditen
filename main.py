import random
from gubb import gubben

orden = ["bil", "katt", "stockholm", "skola"]
random_ord = list(random.choice(orden).upper())
# underline_lista = []
#
# for char in random_ord:
#     underline_lista.append("_ ")

gissningar = []


def start():
    fel = 0
    while fel < 7:

        underline_lista = [ char if char in gissningar else "_ " for char in random_ord ]

        print(f"\nOrdet har valts: {' '.join(underline_lista)}")
        print(gubben[fel])
        print("\n")
        svar = input("Ange en bokstav: ").upper()


        print("\n\n\n")

        if svar in gissningar:
            print(f"Du har redan gissat på {svar}!")
            print("-----------------------------")


        elif svar in random_ord and svar not in gissningar:
            print(f"\nRätt, {svar} finns i ordet")
            print("-----------------------------")
            gissningar.append(svar)

            for x in range(len(random_ord)):
                char = random_ord[x]
                if char == svar:
                    underline_lista[x] = random_ord[x]
                    random_ord[x] = "_"


        else:
            print(f"Fel, {svar} finns inte i ordet")
            print("-----------------------------")
            fel += 1



        if all("_" == char for char in random_ord):
            print(f"Du vann med {fel} fel")
            print(f"Ordet var {random_ord}")
            break


        if fel == 7:
            print("\nDu förlorade! :(")

start()
