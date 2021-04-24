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
    pc = self.__tela_cliente.exclui_cliente()
    for cliente in self.__clientes:
      if cliente.nome == pc:
        lista = cliente.lista()
        self.__tela_cliente.lista_alugueis(lista)



  def incluir_cliente(self):
    dados_cliente = self.__tela_cliente.dados_cadastrar()

    cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"])

    self.__clientes.append(cliente)

  def lista_clientes(self):
    for cliente in self.__clientes:
      self.__tela_cliente.mostrar_cliente({"nome": cliente.nome, "telefone": cliente.telefone, "endereco": cliente.endereco})



  def exclui_cliente(self):
    nome = self.__tela_cliente.exclui_cliente()
    verificador = False
    for cliente in self.__clientes:
      if cliente.nome == nome:
        verificador = True
        self.__clientes.remove(cliente)
        self.__tela_cliente.exclui_cliente_return(verificador)
      
    if verificador == False:
        self.__tela_cliente.exclui_cliente_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    lista_opcoes = {1: self.incluir_cliente, 2: self.lista_clientes, 3:self.exclui_cliente, 4:self.lista_alugueis, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_cliente.tela_opcoes()]()