from limite.tela_aluguel import TelaAluguel
from entidade.aluguel import Aluguel
from daos.dao_aluguel import AluguelDAO

class ControladorAluguel:   

  def __init__(self, controlador_sistema, controlador_cliente, controlador_funcionario, controlador_carro):
    self.__controlador_sistema = controlador_sistema
    self.__controlador_cliente = controlador_cliente
    self.__controlador_funcionario = controlador_funcionario
    self.__controlador_carro = controlador_carro
    self.__dao = AluguelDAO()
    #self.__alugueis = []
    self.__tela_aluguel = TelaAluguel()


  def incluir_aluguel(self):
    dados_aluguel, test_none = self.__tela_aluguel.dados_cadastrar()

    placa = dados_aluguel["carro"]
    carro_certo, carro_verificador = self.__controlador_carro.aluguel(placa)   

    
    nome = dados_aluguel["cliente"]
    cliente_certo, cliente_verificador = self.__controlador_cliente.aluguel(nome)   


    nome = dados_aluguel["funcionario"]
    funcionario_certo, funcionario_verificador = self.__controlador_funcionario.aluguel(nome)   
  
    identificador = dados_aluguel["data"]
    codigo_certo, codigo_verificador = self.codigo_aluguel(identificador)

    aluguel_verificador = False

    if carro_verificador == 2:
      carro_ja_alugado = True #true = carro nao alugado
      if cliente_verificador and  funcionario_verificador == True and codigo_verificador == 0:        
          aluguel = Aluguel(carro_certo, cliente_certo, funcionario_certo, codigo_certo)

          self.__controlador_carro.aluga(carro_certo,aluguel, carro_ja_alugado)
          self.__controlador_cliente.novo(cliente_certo, aluguel)
          self.__controlador_funcionario.novo(funcionario_certo, aluguel)

          self.__dao.add(aluguel)
          aluguel_verificador = True
    if test_none == False: 
      self.__tela_aluguel.cadastro(aluguel_verificador)
      if aluguel_verificador == False:
        self.aluguel_verificadores(cliente_verificador, funcionario_verificador, carro_verificador,codigo_verificador)



  def aluguel_verificadores(self, cliente_verificador, funcionario_verificador, carro_verificador, codigo_verificador):
    self.__tela_aluguel.aluguel_erro(cliente_verificador, funcionario_verificador, carro_verificador, codigo_verificador)


  def codigo_aluguel(self, identificador):
    codigo_verificador = 0
    codigo_certo = 0
    for codigo in self.__dao.get_all():
      if codigo.data == identificador:
        codigo_verificador = codigo_verificador + 1
    if codigo_verificador == 0: 
      codigo_certo = identificador
    return codigo_certo, codigo_verificador


  def lista_alugueis(self):
    dados_aluguel = []
    for aluguel in self.__dao.get_all():
      dados_aluguel.append({"carro": aluguel.carro.placa, "cliente": aluguel.cliente.nome, "funcionario": aluguel.funcionario.nome, "data": aluguel.data})
    self.__tela_aluguel.mostra_aluguel(dados_aluguel)

  def exclui_aluguel(self):
    codigo, test_none = self.__tela_aluguel.exclui_aluguel()
    verificador = False
    if test_none == False:
      for aluguel in self.__dao.get_all():
        if aluguel.data == codigo:
          verificador = True
          self.__controlador_carro.aluga(aluguel.carro,aluguel, False)
          self.__controlador_cliente.remove(aluguel.cliente, aluguel)
          self.__controlador_funcionario.remove(aluguel.funcionario, aluguel)

          self.__controlador_funcionario.remove(aluguel.funcionario, aluguel)
          self.__tela_aluguel.exclui_aluguel_return(verificador)
        
      if verificador == False:
          self.__tela_aluguel.exclui_aluguel_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_aluguel, 2: self.lista_alugueis, 3:self.exclui_aluguel, 0: self.retorna_tela_principal }

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluguel.tela_opcoes()]()