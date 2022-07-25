cont = 0
while(cont < 10):
    print(cont)
    cont += 1
    if cont == 6:
        print('É igual a 6')
        break  # pausa a execução do código.
else:
    print('Fim do laço')  # Quando há um break o esle não é executado.
