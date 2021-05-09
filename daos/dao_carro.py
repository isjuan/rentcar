from daos.dao import DAO
from entidade.carro import Carro

class CarroDAO(DAO):

    def __init__(self):
        super().__init__('carros.pkl')

    def add(self, carro: Carro):
        if (isinstance (carro.placa, str)) and (carro is not None) and isinstance (carro, Carro): 
            super().add(carro.placa, carro)

    def get (self, key: str):
        if isinstance (key, str): 
            return super().get(key)

    def remove (self, key: str):
        if isinstance (key, str): 
            return super().remove(key)