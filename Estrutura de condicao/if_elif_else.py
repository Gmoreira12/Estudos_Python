# Em Python, assim como na maioria das linguagens de programação,
# o programa deve ser capaz de tomar decisões com base em valores
# e resultados gerados durante sua execução, ou seja, deve ser capaz
# de decidir se determinada instrução deve ou não ser executada de acordo com uma condição.

idade = int(input('Digite sua idade'))
if idade >= 10 and idade < 20:
    print('Você é adolescente')
elif idade >= 20 and idade < 30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Você é uma crinaça')