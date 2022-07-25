# O comando while faz com que um conjunto de instruções seja executado
#  enquanto uma condição é atendida. Quando o resultado dessa condição
#  passa a ser falso, a execução do loop é interrompida
contador = 0
multiplicador = int(input("Digite o multiplicador: "))

while(contador <= 10):
    print(contador, ' x', multiplicador, ' = ', (contador * multiplicador))
    contador = contador + 1
else:
    print('\n')
    print('Tabuada de', multiplicador,'calculada com sucesso.')