import random
import time

# Introduktion:
# Du ska skapa ett litet program där man vinner om man får 3 likadan objekt.
#
# Förutsättningar:
# Lista med objekt
# Random modulen
# Skapa en funktion
# Print funktionen
#
# Innehåll:
# Äpple
# Banan
# Jordgubbe
# Kiwi
# Päron
#
# Utmaning:
# Du ska vidare utveckla på det du har gjort,
# med att det ska finnas poäng baserad på vilket 3 par man har fått.
# Exempelvis: 3 äpplen ger 5 poäng, 3 jordgubbar ger 3 poäng och etc ... Tips: dictionary


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
