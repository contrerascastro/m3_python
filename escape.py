#importar librerías
import math

#solicitar datos (strings)
radio_kilometros = input("Ingresa al radio del planeta en kilómetros")
radio_kilometros = float(radio_kilometros)
radio_metros = radio_kilometros * 1000

constante = input("Ingresa la constante gravitacional")
constante = float (constante)

#Cálculo de la velocidad ve= raíz cuadrada de 2*g*r
velocidad_escape = math.sqrt(2*radio_kilometros*constante)
velocidad_escape = float(velocidad_escape)

#Mostrar el resultado
print(f"La velocidad de escape es {round(velocidad_escape,2)} m/s")


