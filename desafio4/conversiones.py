import sys

monto_peso_chileno = sys.argv[1]
#monto_peso_chileno = float(monto_peso_chileno)

#monto_peso_chileno = float(input("Ingrese la cantidad de pesos chilenos que quiere cambiar"))

#Valores de prueba tasas_conversion
tasa_conversion_soles = 0.0046
tasa_conversion_peso_argentino = 0.093
tasa_conversion_dolar_americano = 0.0013 #en los valores entregados hay un error en esta tasa. sobre 1 0


# monto_peso_chileno = sys.argv[4]
print(f"Los {monto_peso_chileno} pesos chilenos equivalen a:")

soles = monto_peso_chileno * tasa_conversion_soles
arg = monto_peso_chileno * tasa_conversion_peso_argentino
dolar = monto_peso_chileno * tasa_conversion_dolar_americano

print(f"{soles} Soles")
print(f"{arg} Pesos Argentinos")
print(f"{dolar} Dólares")

