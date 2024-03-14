#importar librerías
import math

#paso 1: captura de datos
precio_suscripcion = float(input("Ingrese el precio de suscripción\n"))
num_usuario_normal = int(input("Ingrese cantidad de usuarios normales\n"))
num_usuario_premiun = int(input("Ingrese cantidad de usuarios premiun\n"))
gastos_totales = float(input("Ingrese los gastos totales\n"))

#paso 2: calculo de utilidades
utilidad_usuarios_normales = precio_suscripcion * num_usuario_normal
utilidad_usuarios_premiun =   (1.5 * precio_suscripcion * num_usuario_premiun)

utilidades = (utilidad_usuarios_normales + utilidad_usuarios_premiun) - gastos_totales

#paso 3: entrega de resultado
print(f"Las utilidades del proyecto son: ${utilidades}.-")