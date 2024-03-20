#importar librerías
import sys

#Capturar valor
umbral = int(sys.argv[1])

#Diccionario
ventas = {
    "Enero": 15000, 
    "Febrero": 22000, 
    "Marzo": 12000, 
    "Abril": 17000, 
    "Mayo": 81000, 
    "Junio": 13000, 
    "Julio": 21000,
    "Agosto": 41200, 
    "Septiembre": 25000, 
    "Octubre": 21500, 
    "Noviembre": 91000, 
    "Diciembre": 21000, 
    }
#ingresar valores al diccionario
mayor_umbral = {}

#recorrer diccionario
for clave, valor in ventas.items():
    if valor > umbral :
        mayor_umbral[clave] = valor 

print(f"Los meses que superan en umbral son: {mayor_umbral}")
