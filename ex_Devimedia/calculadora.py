class Calculadora: # por convenção todas class é iniciada com a primeira letra maiúscula.
    __area_paredes: float
    __area_teto: float  #No python declaramos atributo privados utilizando dos underline.

    def calcular_area_parede(self, comodo):# "Self" é um parâmetro obrigatório de toda classe.
        self.__area_parede = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_parede
    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto
    def calcular_litragem_necessaria(self):
        if self.__area_parede <= 0 or self.__area_teto <= 0:
            print('Não é possível  calcular  a com os valores informados.')
            exit()
        return (self.__area_parede + self.__area_teto) / 10

6