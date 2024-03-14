#Importar librerías
import math

#Solicitud de datos
precio_suscripcion = float(input("Ingrese precio de suscripcion en clp: \n"))
usuarios = int(input("Ingrese numero de usuarios: \n"))
gastos_totales = float(input("Ingrese gastos totales en clp: \n"))
utilidades_año_anterior= float(input("Ingrese las utilidades del año anterior mayor a cero, en clp: \n"))

#utilidades = p * u - gt
utilidades_actuales = precio_suscripcion * usuarios - gastos_totales

#validacion de variables (condicional)
if utilidades_año_anterior > 0 :
    #realizar lo que este tabulado
    
    #se divide la utilidad actual por la ultilidad del año anterior para obtener la razon
    razon_utilidad_actual_y_anterior = utilidades_actuales / utilidades_año_anterior

    #el resultado de la division se puede mulpiplicar por 100 para pasarlo a % 
    #razon_utilidad_actual_y_anterior = razon_utilidad_actual_y_anterior * 100

    print(f"La razón entre la utilidad actual y del año anterior es: {round(razon_utilidad_actual_y_anterior,2)} de crecimiento")

