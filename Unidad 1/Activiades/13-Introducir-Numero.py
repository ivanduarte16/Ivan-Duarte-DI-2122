import random


class MasPequenyo(Exception):
    pass


class MasGrannde(Exception):
    pass


aleatorio = random.randint(0, 100)
numero = -8
while numero != aleatorio:
    try:
        numero = int(input("Introduzca un numero entre 0 y 100: "))
        if numero < aleatorio:
            raise MasPequenyo()
        elif numero > aleatorio:
            raise MasGrannde()
        else:
            print("Has acertado el numero ")
            break
    except MasPequenyo:
        print(str(numero) + " mas pequeño")
    except MasGrannde:
        print(str(numero) + " mas grande")
