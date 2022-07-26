def dobra(lista):
    dobro = 0
    while dobro < len(lista):
        lista[dobro] *= 2
        dobro += 1


valores = [6, 3, 7, 8, 5, 9]
dobra(valores)
print(valores)
