from replit import clear
from day10_art import logo

def sumar(n1, n2):
  return n1 + n2

def restar(n1, n2):
  return n1 - n2

def mutiplicar(n1, n2):
  return n1 * n2

def dividir(n1, n2):
  return n1 / n2

operaciones = {
  "+": sumar,
  "-": restar,
  "*": mutiplicar,
  "/": dividir
}

def calculadora():
  print(logo)

  numero1 = float(input("Cuál es el primer número?: "))
  for simbolo in operaciones:
    print(simbolo)
  continuar = True
 
  while continuar:
    operacion_simbolo = input("Elija un operador: ")
    numero2 = float(input("Cuál es el próximo número?: "))
    funcion_calculadora = operaciones[operacion_simbolo]
    respuesta = funcion_calculadora(numero1, numero2)
    print(f"{numero1} {operacion_simbolo} {numero2} = {respuesta}")

    if input(f"Tipee 'y' si quiere seguir operando con la {respuesta}, o tipee 'n' para empezar un nuevo cálculo: ") == 'y':
      numero1 = respuesta
    else:
      continuar = False
      clear()
      calculadora()

calculadora()
