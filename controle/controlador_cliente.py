from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente

class ControladorCliente:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__clientes = []
    self.__tela_cliente = TelaCliente()


  def incluir_cliente(self):
    dados_cliente = self.__tela_cliente.dados_cadastrar()

    cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"])

    self.__clientes.append(cliente)

  def lista_clientes(self):
    for cliente in self.__clientes:
      self.__tela_cliente.mostrar_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco})



  def exclui_cliente(self):
    pc = self.__tela_cliente.exclui_cliente()
    bol = False
    for cliente in self.__clientes:
      if cliente.nome == pc:
        bol = True
        self.__clientes.remove(cliente)
        self.__tela_cliente.exclui_cliente_return(bol)
      
    if bol == False:
        self.__tela_cliente.exclui_cliente_return(bol)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 3:self.exclui_cliente, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_cliente.tela_opcoes()]()