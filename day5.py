1# Vamos a crear un generador de Passwords!
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido al generador de Passwords!")
numeroLetras = int(input("¿Cuántas letras le gustaría en su password?\n")) 
numeroSimbolos = int(input("¿Cuántos símbolos le gustaría?\n"))
numeroNumeros = int(input("¿Cuántos números le gustaría?\n"))

password_list = []

for char in range(1, numeroLetras + 1):
  password_list.append(random.choice(letras))

for char in range(1, numeroSimbolos + 1):
  password_list += random.choice(simbolos)

for char in range(1, numeroNumeros + 1):
  password_list += random.choice(numeros)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Tu password es: {password}")