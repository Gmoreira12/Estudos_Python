# Uma observação a ser feita no uso de uma tupla é que se ela tiver um único item,
# é necessário colocar uma vírgula depois dele, pois caso contrário,
# o objeto que vamos obter é uma string, porque o valor do item é do tipo string.

objeto_string = ('computador')
objeto_tupla = ('computador',)

print(type(objeto_string))
print(type(objeto_tupla))

#As tuplas devem ser usadas em situações em que não haverá necessidade de adicionar,
#remover ou alterar elementos de um grupo de itens. Exemplos bons seriam os meses do ano,
#os dias da semana, as estações do ano etc. 
