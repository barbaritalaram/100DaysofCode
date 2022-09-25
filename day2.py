# Día 2
# Crearemos una calculadora de propina utilizando 
# diferentes tipos da datos y que entregue el resultado con dos decimales

print("--- Bienvenido a la calculadora de propina ---\n")
cuenta = float(input("¿Cuál es el total de la cuenta? $"))
propina = int(input("¿Cuánto porcentaje de propina desea dar?10, 12 o 15? "))
personas = int(input("Cuántas personas compartirán la cuenta? "))
propinaEnProcentaje = propina / 100
totalPropina = cuenta * propinaEnProcentaje
totalCuenta = cuenta + totalPropina
cuentaPorPersona = totalCuenta / personas
totalFinal = "{:.2f}".format(cuentaPorPersona)
print(f"Cada persona debe pagar: ${totalFinal}")
