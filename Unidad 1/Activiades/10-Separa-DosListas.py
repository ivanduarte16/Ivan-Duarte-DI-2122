def EsPar(x):
    if x % 2 == 0:
        return True
    return False


def EsImpar(x):
    if x % 2 == 1:
        return True
    return False


lista = [10, 2, 7, 4, 89, 40, 33, 45, 60, 43, 100, 22]

impar = filter(EsImpar, lista)
par = filter(EsPar, lista)

par = list(par)
impar = list(impar)

print("Pares \n", par)
print("Impares \n", impar)
