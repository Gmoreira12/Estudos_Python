# No python o "*" dentro do parametro ele permite que a função receba varios parametros.
def contador(* num):
    print(num)


contador(2, 5, 6)
contador(7, 6)
contador(8, 4, 1, 0)
