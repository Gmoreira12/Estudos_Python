from calculadora import Calculadora # importa a class Calculadora
from comodo import Comodo # importa a class Comodo

calc = Calculadora() # Objeto da class Calculadora
comodo = Comodo(
    input('Digite a largura do cômodo: '),
    input('Digite a profundidade do cômodo: ')
)
print(f'A área das paredes é: {calc.calcular_area_parede(comodo)}')
print(f'A área do teto é: {calc.calcular_area_teto(comodo)}')
print(f'Litragem de tinta necessária é: {calc.calcular_litragem_necessaria()} litros.')
5