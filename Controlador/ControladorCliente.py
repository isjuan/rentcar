from Tela.TelaCliente import TelaCliente
from Entidade.Cliente import Cliente

class ControladorCliente:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__clientes = []
    self.__tela_cliente = TelaCliente()


  def incluir_cliente(self):
    dados_cliente = self.__tela_cliente.dados_cadastrar()

    cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"])

    self.__clientes.append(cliente)
