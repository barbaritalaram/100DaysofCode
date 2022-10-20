############### Blackjack #####################
## el deck es ilimitado
## no jugamos con jokers
## Recuerda que el AS vale 11
## J, Q, K valen 10
## se tiró y no se devuelve!
## al azar no más!

import random
from replit import clear
from day11_art import logo

def entregaCarta():
  """Función que devuelve una carta al azar"""
  cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  carta = random.choice(cartas)
  return carta

def calcularPuntuacion(cartas):
  """Toma una lista de cartas y devuelve la puntuación"""
  if sum(cartas) == 21 and len(cartas) == 2:
    return 0
  if 11 in cartas and sum(cartas) > 21:
    cartas.remove(11)
    cartas.append(1)
  return sum(cartas)

def compara(puntuacionJugador, puntuacionPC):
  if puntuacionJugador > 21 and puntuacionPC > 21:
    return "Te pasaste. Perdiste 😤\n"


  if puntuacionJugador == puntuacionPC:
    return "Empate 🙃\n"
  elif puntuacionPC == 0:
    return "Perdiste, el oponente tiene un Blackjack 😱\n"
  elif puntuacionJugador == 0:
    return "Ganaste con un Blackjack 😎\n"
  elif puntuacionJugador > 21:
    return "Te pasaste, Perdiste 😭\n"
  elif puntuacionPC > 21:
    return "Tu oponente se pasó, Ganaste 😁\n"
  elif puntuacionJugador > puntuacionPC:
    return "Ganaste 😃\n"
  else:
    return "Perdiste 😤\n"

def jugar():

  print(logo)

  cartasJugador = []
  cartasPC = []
  termino = False

  for _ in range(2):
    cartasJugador.append(entregaCarta())
    cartasPC.append(entregaCarta())

  while not termino:
    puntuacionJugador = calcularPuntuacion(cartasJugador)
    puntuacionPC = calcularPuntuacion(cartasPC)
    print(f"   Tus cartas son: {cartasJugador} y tu puntaje es: {puntuacionJugador}")
    print(f"   La primera carta del computador es: {cartasPC[0]}\n")

    if puntuacionJugador == 0 or puntuacionPC == 0 or puntuacionJugador > 21:
      termino = True
    else:
      sacarCartaUsuario = input("Tipea 'y' para obtener otra carta y 'n' para pasar: ")
      if sacarCartaUsuario == "y":
        cartasJugador.append(entregaCarta())
      else:
        termino = True

  while puntuacionPC != 0 and puntuacionPC < 17:
    cartasPC.append(entregaCarta())
    puntuacionPC = calcularPuntuacion(cartasPC)

  print(f"   Tu mano final es: {cartasJugador}, puntaje final: {puntuacionJugador}")
  print(f"   Mano final del computador: {cartasPC}, puntaje final: {puntuacionPC}")
  print(compara(puntuacionJugador, puntuacionPC))

while input("Quieres jugar Blackjack? Tipea 'y' o 'n': ") == "y":
  clear()
  jugar()
