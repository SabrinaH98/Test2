TotaalAantalPunten = 7
puntenbehaald = [1, 2, 3, 90, 5, 6]

if len(puntenbehaald) < TotaalAantalPunten:
    print("Je bent er bijna!")

if len(puntenbehaald) >= TotaalAantalPunten:
    print("Je hebt gewonnen!!")

getal1 = int(input("noem hier getal 1 "))
getal2 = int(input("noem hier getal 2 "))

if getal1 > getal2:
    print("Je eerste getal is groter.")
if getal2 > getal1:
    print("Je tweede getal is groter.")
