#Nesse código temos duas listas com os nomes numeros e nomes.
#A primeira lista trabalha com números, então a função min()
#retorna o menor valor dela, enquanto que a função max() retorna o maior valor.
#Já a segunda lista contém strings, o que faz com que as funções trabalhem com comparações alfabéticas.

numeros = [1, 2, 7, 8, 3]
nomes = ['Lu', 'Julia','Anderson', 'Gabriel', 'Paulo']

print(min(numeros)) #1
print(max(numeros)) #8
print(min(nomes)) # Anderson
print(max(nomes)) # Paulo

# Na string a função faz a comparação de forma alfabética.
