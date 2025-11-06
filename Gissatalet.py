namn = input("vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random
hemligt_tal = random.randint(1, 10)
gissning = int(input("Gissa ett tal mellan 1 och 10: "))
if gissning == hemligt_tal:
    print("Grattis! Du gissade rätt.")
else:
    print(f"Tyvärr, det rätta talet var {hemligt_tal}.")