alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(texto, desplazamiento, tipoCifrado):
  texto_procesado = ""
  if tipoCifrado == "decode":
    desplazamiento *= -1
  for caracter in texto:
    if caracter in alfabeto:
      posicion = alfabeto.index(caracter)
      nuevaPosicion = posicion + desplazamiento
      texto_procesado += alfabeto[nuevaPosicion]
    else:
      texto_procesado += caracter
  print(f"Aqui el resultado de {tipoCifrado}: {texto_procesado}")

from day8_art import logo
print(logo)

haTerminado = False
while not haTerminado:

  direction = input("Escriba 'encode' para encriptar o 'decode' para desencriptar:\n")
  msg = input("Escriba su mensaje:\n").lower()
  shift = int(input("Indique el número de desplazamiento:\n"))
  shift = shift % 26

  cesar(texto=msg, desplazamiento=shift, tipoCifrado=direction)

  reiniciar = input("Escriba 'si' si desea volver a empezar. Sino, escriba 'no'.\n")
  if reiniciar == "no":
    haTerminado = True
    print("Chao!")