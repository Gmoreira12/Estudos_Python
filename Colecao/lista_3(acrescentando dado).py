# Além de alterar elementos em listas, também é possível adicionar itens nelas,
#  pois já vêm com uma coleção de métodos predefinidos que podem ser usados para
#  manipular os objetos que ela contém.

livros = ['Milagre da manha', 'Superinteligencia','1984', 'Essencialismo']
print(livros)

#livros.append('Pequeno principe') # ".append" acrescenta mais um elemento na lista.
#print(livros)
livros.insert(1, 'Pai rico, pai pobre') # ".insert" acrescenta mais um elemento, porém você pode escolher onde ele ficará.
print(livros)
