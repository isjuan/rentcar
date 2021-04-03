from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, telefone: int, endereco: str):
        super().__init__(nome, telefone, endereco)
        self.__clientes = []