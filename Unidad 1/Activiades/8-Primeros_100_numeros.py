contador = 0
for x in range(0, 200, 1):
    if x % 2 == 1:
        print(x)
        contador + 1
    if contador > 100:
        break
