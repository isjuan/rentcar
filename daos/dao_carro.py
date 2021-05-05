class ClienteDAO(DAO):

    def __init__(self):
        super().__init__ ('carro.pkl')

    def add(self, cliente: Cliente):
        if (isinstance (cliente.codigo, int)) and (cliente is not None) \
                and isinstance (cliente, Cliente): 
            super().add (cliente.codigo, cliente)

    def get (self, key: int):
        if isinstance (key, int): 
            return super().get(key)

    def remove (self, key: int):
        if isinstance (key, int): 
            return super().remove(key)