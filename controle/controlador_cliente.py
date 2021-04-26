from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente

class ControladorCliente:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__clientes = []
    self.__tela_cliente = TelaCliente()
  
  def l_clientes(self):
    return self.__clientes

  def novo(self,cliente, aluguel):
    cliente.novo(aluguel)

  def remove(self,cliente, aluguel):
    cliente.remove(aluguel)
  
  def lista_alugueis(self):
    nome = self.__tela_cliente.retorna_cliente()
    for cliente in self.__clientes:
      if cliente.nome == nome:
        lista = cliente.lista()
        self.__tela_cliente.lista_alugueis(lista)

  def aluguel(self, nome_certa):
    cliente_verificador  = False
    for cliente in self.l_clientes():
      if cliente.nome == nome_certa:
        cliente_certo = cliente
        cliente_verificador = True
    if cliente_verificador == False:
      cliente_certo = 0
    return cliente_certo, cliente_verificador


  def incluir_cliente(self):
    dados_cliente = self.__tela_cliente.dados_cadastrar()

    cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"])

    self.__clientes.append(cliente)

  def lista_clientes(self):
    for cliente in self.__clientes:
      self.__tela_cliente.mostrar_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco})



  def exclui_cliente(self):
    nome = self.__tela_cliente.retorna_cliente()
    verificador = 0
    for cliente in self.__clientes:
      if cliente.nome == nome:
        if len(cliente.lista()) == 0:
          verificador = 2
          self.__clientes.remove(cliente)
        if len(cliente.lista()) > 0:
          verificador = 1

    self.__tela_cliente.exclui_cliente_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 3:self.exclui_cliente, 4:self.lista_alugueis, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_cliente.tela_opcoes()]()