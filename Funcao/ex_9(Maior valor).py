from time import sleep


def maior(*num):
    contador = maior = 0
    print(f'\n Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado  foi {maior}.')


maior(10, 1, 2 , 6, 15)
maior(2, 9, 4)
maior(5, 3, 8, 2)
