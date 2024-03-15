#Desafío IMC

import math

#Solicitar datos
peso = input("Ingrese su peso en kilogramos\n")
peso = float(peso)

#Solicitar talla
talla = input("Ingrese su altura en centímetros. Por ejemplo, si mide un metro y setenta y cino centímetos (1,75), ingrese el número 175\n")
talla = float(talla)

#Transforamción de talla
talla = float(talla/100)

#calculo
imc= round(peso/(talla**2),2)

print(f"tu índice de masa corporal es {imc}")

if imc <= 18.5 : print("Según tu IMC, tu clasificación es Bajo peso ")
elif imc > 18.5 and imc <= 25 : print("Según tu IMC, tu clasificación es Adecuado ")
elif imc > 25 and imc <= 30 : print("Según tu IMC, tu clasificación es Sobrepeso ")
elif imc > 30 and imc <= 35 : print("Según tu IMC, tu clasificación es Obesidad grado 1 ")
elif imc > 35 and imc <= 40 : print("Según tu IMC, tu clasificación es Obesidad grado 2 ")
elif imc > 40 : print("Según tu IMC, tu clasificación es Obesidad grado 3 ")
