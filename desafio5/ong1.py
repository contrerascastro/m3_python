#Librerias
import math

#Funciones
def factorial(n) :
    fn = [i for i in range(1,n+1)]
    return prod(fn)

def productoria(lista) :
    return prod(lista)

def calcular(**parametros) :
    for k,v in parametros.items() :
        if "fact_" in k :
            print(f"El Factorial de {v} es {factorial(v)}")
        else :
            print(f"La productoria de {v} es {productoria(v)}")

#Resultado
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)