from entidade.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, telefone: int, endereco: str):
        super().__init__(nome, telefone, endereco)
        self.__alugueis = []

    def novo(self, aluguel):
        self.__alugueis.append(aluguel)

    def remove(self, aluguel):
        self.__alugueis.remove(aluguel)

    def lista(self):
        return self.__alugueis

    