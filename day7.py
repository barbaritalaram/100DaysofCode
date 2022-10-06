import random
from day7_art import etapas, logo
from day7_words import word_list
from replit import clear

print(logo)
termino_el_juego = False
vidas = len(etapas) - 1

palabra_elegida = random.choice(word_list)
largo_palabra = len(palabra_elegida)

display = []
for _ in range(largo_palabra):
    display += "_"

while not termino_el_juego:
    letra_elegida = input("Adivina la palabra. Dime una letra: ").lower()

# la función clear sirve limpiar la pantalla en cada jugada
    clear()

    if letra_elegida in display:
        print(f"Ya habías adivinado la letra {letra_elegida}")

    for posicion in range(largo_palabra):
        letter = palabra_elegida[posicion]
        if letter == letra_elegida:
            display[posicion] = letter
            print("Bien, le achuntaste!")
    print(f"{' '.join(display)}")

    if letra_elegida not in palabra_elegida:
        print(f"Elegiste {letra_elegida}, pero no está en la palabra. Perdiste una vida!")
        vidas -= 1
        if vidas == 0:
            termino_el_juego = True
            print(f"La palabra era {palabra_elegida}. Perdiste 😵 ")
    
    if not "_" in display:
        termino_el_juego = True
        print("Ganaste! 😜 ")

    print(etapas[vidas])