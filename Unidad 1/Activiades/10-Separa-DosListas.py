lista = [10, 2, 7, 4, 89, 40, 33, 45, 60, 43, 100, 22]
parells = list(filter(lambda x: x % 2 == 0, lista))
imparells = list(filter(lambda x: x % 2 == 1, lista))
print("Parells: {}".format(parells))
print("Parells: {}".format(imparells))
