# importar ibrerias
import sys

# Filtrar
def filtro_rev(umbral, condicion = 'mayor' ):
    if condicion == 'mayor' :
        filtro = ', '.join([k for k,v in precios.items() if v > umbral])
        return f'Los productos mayores al umbral son: {filtro}'
    if condicion == 'menor' :
        filtro = ', '.join([k for k,v in precios.items() if v < umbral])
        return f'Los productos menores al umbral son: {filtro}'
    else :
        print('Lo sentimos, no es una operación válida')
        exit(0)

# Diccionario

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Resultados
if len(argv[1]) <3 :
    print(filtro_rev(int(argv[1])))
else :
    print(filtro_rev(int(argv[1]), str(argv[2])))