#Juego cachipún

import random

#Establecer variables tipo string
piedra = "piedra"
papel = "papel"
tijeras = "tijeras"

#Configurar opciones de la máquina
maquina = random.choice([piedra, papel, tijeras])


#Solicitar jugada
humano = input("Escribe piedra, papel o tijera para jugar \n")

#Validar entradas
if humano != "piedra" : print("ingresa datos válidos")
elif humano != "papel" : print("ingresa datos válidos")
elif humano != "tijeras" : print("ingresa datos válidos")


#judaga máquina
print(f"Mi jugada es: {maquina}")

#Resultado empates
if humano == "papel" and maquina == "papel" : print("Empatamos")
elif humano == "piedra" and maquina == "piedra" : print("Empatamos")
elif humano == "tijeras" and maquina == "tijeras" : print("Empatamos")

#Resultados ganadores
if humano == "piedra" and maquina == "tijeras" : print("Ganaste: Piedra gana")
elif humano == "tijeras" and maquina == "papel" : print("Ganaste: Tijeras ganan")
elif humano == "papel" and maquina == "piedra" : print("Ganaste: Papel gana")

#Resultados perdedores
if humano == "piedra" and maquina == "papel" : print("Gané: Papel gana")
elif humano == "tijeras" and maquina == "piedra" : print("Gané: Piedra gana")
elif humano == "papel" and maquina == "tijeras" : print("Gané: Tijeras ganan")




