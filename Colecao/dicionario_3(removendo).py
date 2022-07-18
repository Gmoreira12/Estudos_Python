# Para remover um item do dicionário, podemos usar o método pop().
cadastro = {
    'Nome': 'Paulo',
    'Celular': '21966048552',
    'Idade': '31',
    'Endereco': 'Rua 1'
}
cadastro['Telefone'] = '2514453365' # Acrescentei um novo dado.

cadastro.pop('Telefone', None) # removi o dado acrescentado.
print(cadastro)