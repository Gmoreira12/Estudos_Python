class Comodo:
    __largura: float
    __profundidade: float
    __altura: float
    def __init__(self, largura, profundidade):  #Toda vez que um método está entre dois Underline é chamado de método mágico.
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9
    @property
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self,largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('O valor informado da largura é inválido.\nDigite novamente.')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try: # tratamento de erro
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor informado da profundidade é inválido.\n digite novamente.')
            exit()# tratamento de erro