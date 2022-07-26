def resultado(lar, com):
    area = lar * com
    print(f'O seu terreno tem {lar} e {com}, portanto a área é de {area} metros quadrados')


print('Cálculo do terreno')
print('-' * 20)
largura = float(input('Digite em metros a largura: '))
comprimento = float(input('Digite em metros o comprimeto: '))
resultado(largura, comprimento)
