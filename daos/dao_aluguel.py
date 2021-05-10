from daos.dao import DAO
from entidade.aluguel import Aluguel

class AluguelDAO(DAO):

    def __init__(self):
        super().__init__('alugueis.pkl')

    def add(self, aluguel: Aluguel):
        if (isinstance (aluguel.data, str)) and (aluguel is not None) and isinstance (aluguel, Aluguel):
            super().add(aluguel.data, aluguel)

    def get (self, key: str):
        if isinstance (key, str):
            return super().get(key)

    def remove (self, key: str):
        if isinstance (key, str):
            return super().remove(key)