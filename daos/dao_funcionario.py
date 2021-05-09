from daos.dao import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):

    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (isinstance (funcionario.nome, str)) and (funcionario is not None) and isinstance (funcionario, Funcionario): 
            super().add(funcionario.nome, funcionario)

    def get (self, key: str):
        if isinstance (key, str): 
            return super().get(key)

    def remove (self, key: str):
        if isinstance (key, str): 
            return super().remove(key)