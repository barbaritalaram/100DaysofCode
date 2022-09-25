print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a Treasure Island.")
print("Tu misión es encontrar el tesoro.")

opcion1 = input('Estás en una bifucarción y debes elegir el camino... Elige "izquierda" o "derecha" \n').lower()
if opcion1 == "izquierda":
  opcion2 = input('Llegaste a un lago y hay una isla en el medio. Elige "esperar" para esperar por un bote o "nadar" para cruzar el lago nadando. \n').lower()
  if opcion2 == "esperar":
    opcion3 = input("Llegaste a la isla desarmado. Hay una casa con 3 puertas. Una roja, otra amarilla y una azul. ¿Cuál eliges? \n").lower()
    if opcion3 == "roja":
      print("Entraste a una habitación llena de fuego. Game Over.")
    elif opcion3 == "amarilla":
      print("Encontraste el tesoro! GANASTE!")
    elif opcion3 == "azul":
      print("Entraste a una habitación llena de bestias. Game Over.")
    else:
      print("Entraste a una habitación que no te deja avanzar. Game Over.")
  else:
    print("Fuiste atacado por una trucha asesina!. Game Over.")
else:
  print("Te caíste a una trampa. Game Over.")