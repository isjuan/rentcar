from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone, endereco)
        self.__clientes = []