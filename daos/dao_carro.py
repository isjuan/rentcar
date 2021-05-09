from daos.dao import DAO
from entidade.carro import Carro

class CarroDAO(DAO):

    def __init__(self):
        super().__init__('carros.pkl')

    def add(self, carro: Carro):
        if (isinstance (carro.placa, int)) and (carro is not None) and isinstance (carro, Carro): 
            super().add(carro.placa, carro)

    def get (self, key: int):
        if isinstance (key, int): 
            return super().get(key)

    def remove (self, key: int):
        if isinstance (key, int): 
            return super().remove(key)