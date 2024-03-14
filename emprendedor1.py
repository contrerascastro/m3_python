"""_summary_ Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades del
proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
Para ello, se te pide desarrollar este cálculo en tres versiones
"""
#importar librerías
import math

precio_suscripcion = float(input ("Ingrese el precio de suscripción estándar en pesos chilenos"))
numero_usuarios_normal= float (input ("Ingrese el número de usuarios normales"))
numero_usuarios_premium= float (input ("Ingrese el número de usuarios premium"))
gasto_total = float (input("Ingrese el gasto total"))

#cálculo de utilidades
utilidades = (precio_suscripcion * numero_usuarios_normal + 1.5 * numero_usuarios_premium)

print(f"Las utilidades de este proyecto son: {utilidades}")