# Aplicaremos lo aprendido con diccionarios
# diccionario = {"Nombre": "Barbarita", "Teléfono": 56938489321}
# conjuntoOfertas = {"Barbarita" : 120, "Roberto" : 210}

from replit import clear
from day9_art import logo
print(logo)

conjuntoOfertas = {}
terminoSubasta = False

def encontrarMayorOferta(ofertantes):
  ofertaMayor = 0
  ganadorSubasta = ""
  
  for ofertante in ofertantes:
    cuantoOferta = ofertantes[ofertante]
    if cuantoOferta > ofertaMayor: 
      ofertaMayor = cuantoOferta
      ganadorSubasta = ofertante
  print(f"El ganador de la subasta es {ganadorSubasta} con una oferta de ${ofertaMayor}")

while not terminoSubasta:
  nombre = input("Cuál es tu nombre?: ")
  precio = int(input("Cual es tu oferta?: $"))
  conjuntoOfertas[nombre] = precio
  print(conjuntoOfertas) #debug
  debemosContinuar = input("Existen otros ofertantes? Tipee 'si' o 'no'.\n")
  if debemosContinuar == "no":
    terminoSubasta = True
    encontrarMayorOferta(conjuntoOfertas)
  elif debemosContinuar == "yes":
    clear()
