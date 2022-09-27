import random # función que nos permite elegir algo al azar

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
manos = [piedra, papel, tijeras]

opcionUsuario = int(input("Cachipún! Tipea 0 para Piedra, 1 para Papel o 2 para Tijeras.\n"))
if opcionUsuario >= 3 or opcionUsuario < 0: 
    print("Elegiste una opción no válida, perdiste!") 
    # si eliges fuera del rango permitido pierdes!
else:
    print(manos[opcionUsuario]) 
    # a imprimir tu mano elegida

    opcionComputador = random.randint(0, 2)
    # que el computador saque al azar una opción
    # entre el 0 y el 2
    print("Computador elige:")
    print(manos[opcionComputador])
    # se imprime la mano elegida

    if opcionUsuario == 0 and opcionComputador == 2:
        print("Ganaste!")
    elif opcionComputador == 0 and opcionUsuario == 2:
        print("Perdiste :( ")
    elif opcionComputador > opcionUsuario:
        print("Perdiste :( ")
    elif opcionUsuario > opcionComputador:
        print("Ganaste!")
    elif opcionComputador == opcionUsuario:
        print("Empate!")

''' 
Recuerda que estos Ejemplos y el contenido necesario para entender
la materia relacionada lo puedes encontrar en el curso de Udemy de 
la Dra. Angela Yu
'''