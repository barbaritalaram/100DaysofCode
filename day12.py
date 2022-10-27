from random import randint
from day12_art import logo

TURNOS_NIVEL_DIFICIL = 5
TURNOS_NIVEL_FACIL = 10

def chequear_respuesta(adivina, respuesta, turnos):
  if adivina > respuesta:
    print("Muy alto👇 .")
    return turnos - 1
  elif adivina < respuesta:
    print("Muy bajo👆.")
    return turnos - 1
  else:
    print(f"Wena! Le achuntaste! {respuesta} era el número.")

def seleccionDificultad():
  nivel = input("Selecciona una dificultad. Tipea 'facil' o 'dificil': ")
  if nivel == "facil":
    return TURNOS_NIVEL_FACIL
  else:
    return TURNOS_NIVEL_DIFICIL

def game():
  print(logo)
  print("Bienvenido a Adivina el número!!")
  print("Estoy pensando en un número entre el 1 y el 100.")
  respuesta = randint(1, 100)
  print(f"La respuesta es {respuesta}")

  turnos = seleccionDificultad()
  adivina = 0
  while adivina != respuesta:
    print(f"Te quedan {turnos} para adivinar el número.")

    adivina = int(input("Adivina: "))

    turnos = chequear_respuesta(adivina, respuesta, turnos)
    if turnos == 0:
      print("No te quedan más oportunidades para adivinar. Perdiste.")
      return
    elif adivina != respuesta:
      print("Adivina de nuevo.")

game()