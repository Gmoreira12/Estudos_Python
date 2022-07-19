# Os operadores lógicos são usados para unir duas ou mais expressões condicionais.

idade_gabriel = 18
idade_julia = 18

print('Gabriel tem', idade_gabriel, ' e Julia tem', idade_julia, 'anos')
if idade_gabriel >= 18 and idade_julia >= 18:
     print('Ambos são maiores de idade. Podem entrar')

elif idade_gabriel >= 18 or idade_julia >= 18:
    print('Há um responsável maior de 18 anos. Podem entrar')

else:
    print('Desculpe. Entrada somente com um responsável maior de 18 anos')

# Com o operador lógico AND todas as condições devem ser verdadeiras.
