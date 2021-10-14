import os

test = os.path.join(os.path.dirname(__file__), "test.txt")

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

with open("test.txt", "r") as fichero:
    for linea in fichero:
        separado = linea.split(" ")
        if separado[1] == "+":
            resultado = suma(int(separado[0]), int(separado[2]))
            print(separado[0], " ", separado[1], " ", int(separado[2]), " = ", resultado)
        elif separado[1] == "-":
            resultado = resta(int(separado[0]), int(separado[2]))
            print(separado[0], " ", separado[1], " ", int(separado[2]), " = ", resultado)
        elif separado[1] == "*":
            resultado = multiplicacion(int(separado[0]), int(separado[2]))
            print(separado[0], " ", separado[1], " ", int(separado[2]), " = ", resultado)
        else:
            resultado = division(int(separado[0]), int(separado[2]))
            print(separado[0], " ", separado[1], " ", int(separado[2]), " = ", resultado)
