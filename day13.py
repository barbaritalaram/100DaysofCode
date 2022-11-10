# hoy repasaremos como debuggear o depurar nuestro programa

# Queremos conseguir esto:
# Primero, si el número es divisible por 3, que imprima Fizz
# Segundo, si el número es divisible por 5, que imprima Buzz
# Tercero, si el número es divisible por 3 y 5, que imprima FizzBuzz 

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])





#original
#for number in range(1, 101):
#  if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#  if number % 3 == 0:
#    print("Fizz")
#  if number % 5 == 0:
#    print("Buzz")
#  else:
#    print([number])