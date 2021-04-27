from entidade.carro import Carro
from entidade.funcionario import Funcionario
from entidade.cliente import Cliente

class Aluguel:
    def __init__(self, carro: Carro, cliente: Cliente, funcionario: Funcionario, data: str):
        self.__carro = carro
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__data = data
        
    @property
    def carro(self):
        return self.__carro

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def cliente(self):
        return self.__cliente

    @property
    def data(self):
        return self.__data