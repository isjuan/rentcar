from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: int, endereco: str):
        super().__init__(nome, telefone, endereco)
        self.__alugueis = []

    def novo(self, aluguel):
        self.__alugueis.apend(aluguel)

    def remove(self, aluguel):
        self.__alugueis.remove(aluguel)



