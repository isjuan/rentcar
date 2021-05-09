from daos.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):

    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance (cliente.nome, str)) and (cliente is not None) and isinstance (cliente, Cliente): #checar "nome" nos outros daos_
            super().add(cliente.nome, cliente)

    def get (self, key: str):
        if isinstance (key, str): 
            return super().get(key)

    def remove (self, key: str):
        if isinstance (key, str): 
            return super().remove(key)