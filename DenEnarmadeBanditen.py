import random

Innehåll = {
    "Äpple":10,
    "Banan":20,
    "Jordgubbe":40,
    "Kiwi":80,
    "Päron":160

}




def main():
    lista = []

    for a in range(3):
        snurra = random.choice(list(Innehåll))
        print(snurra)
        lista.append(snurra)


    else:
        if lista.count(snurra) == 3:
            print("-----------")
            print("du vann")
            print(Innehåll.get(snurra))
        else:
            print("-----------")
            print("du förlora")


main()
