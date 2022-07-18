# Assim como podemos adicionar itens em nossa lista, também podemos retirá-los.
# E para isso temos dois métodos: remove() para a remoção pelo valor informado no parâmetro,
# e pop() para remoção pelo índice do elemento na lista.

paes = ['franceis', 'suico', 'bisnaga']
print(paes)

# paes.remove('bisnaga') # "remove" remove o elemento pelo valor.
# print(paes)

paes.pop(3)  # "pop" remove o elemento pelo índice.
print(paes)
