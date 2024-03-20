import getpass
import string

alfabeto = string.ascii_lowercase
print(alfabeto)

clave = getpass.getpass("ingrese una contraseña de 4 letras en minúscula\n")
#clave = str(input("ingrese una clave de 4 letras en minúscula\n"))

for letra1 in alfabeto:
    for letra2 in alfabeto:
        for letra3 in alfabeto:
            for letra4 in alfabeto:
                intento = letra1 + letra2 +letra3 + letra4
                if intento == clave:
                    print("clave encontrada", intento)
                
                    veces = len(intento)
                    print(veces)