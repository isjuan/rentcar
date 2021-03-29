from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone, endereco)
        self.__alugueis = []



