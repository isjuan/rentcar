from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from daos.dao_cliente import ClienteDAO


class ControladorCliente:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    #self.__clientes = []
    self.__dao = ClienteDAO()
    self.__tela_cliente = TelaCliente()
    self.__dao.add(Cliente("n", "t", "e"))

  
  def l_clientes(self):
    return self.__dao.get_all()

  def novo(self,cliente, aluguel):
    cliente.novo(aluguel)

  def remove(self,cliente, aluguel):
    cliente.remove(aluguel)
  
  def lista_alugueis(self):
    lista_nome, test_none = self.__tela_cliente.retorna_cliente()
    lista = []
    if test_none == False:
      nome = lista_nome["nome"]
      for cliente in self.__dao.get_all():
        if cliente.nome == nome:
          lista = cliente.lista()
    self.__tela_cliente.lista_alugueis(test_none, lista)

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
    dados_cliente, test_none = self.__tela_cliente.dados_cadastrar()
    verificador = 2
    if test_none == False:
      nome_cliente = dados_cliente["nome"]
      for cliente in self.__dao.get_all():
        if nome_cliente == cliente.nome:
          verificador = 1
      if verificador == 2:
        verificador = 0
        cliente = Cliente(dados_cliente["nome"], dados_cliente["telefone"], dados_cliente["endereco"])
        self.__dao.add(cliente)
    self.__tela_cliente.incluir_cliente_return(verificador)
    


    

    

  def lista_clientes(self):
    temp = []
    for cliente in self.__clientes:
      a = [cliente.nome, cliente.telefone, cliente.endereco]
      temp.append(a)
    self.__tela_cliente.mostrar_cliente(temp)
    

  def exclui_cliente(self):
    lista_nome, test_none = self.__tela_cliente.retorna_cliente()
    if test_none == False:
      nome = lista_nome["nome"]
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