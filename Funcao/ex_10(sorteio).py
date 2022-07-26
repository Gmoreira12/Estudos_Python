from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores de 1 a 100 e somando os números pares.')
    for contador in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(0.2)
    

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares, temos: {soma}')
    print('\n FEITO !!')



numeros = list()
sorteia(numeros)
somaPar(numeros)

