namn = input("vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random
hemligt_tal = random.randint(1, 10)
gissning = int(input("Gissa ett tal mellan 1 och 10: "))
antal_gissningar = 1

while gissning < 4:
    if gissning != hemligt_tal:
        print("Fel gissning, försök igen.")
        gissning = int(input("Gissa ett tal mellan 1 och 10: "))
        antal_gissningar += 1
    elif gissning == hemligt_tal:
        print("Rätt gissat!")
        break