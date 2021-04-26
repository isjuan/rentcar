from limite.tela_aluguel import TelaAluguel
from entidade.aluguel import Aluguel


class ControladorAluguel:   

  def __init__(self, controlador_sistema, controlador_cliente, controlador_funcionario, controlador_carro):
    self.__controlador_sistema = controlador_sistema
    self.__controlador_cliente = controlador_cliente
    self.__controlador_funcionario = controlador_funcionario
    self.__controlador_carro = controlador_carro
    self.__alugueis = []
    self.__tela_aluguel = TelaAluguel()

  def incluir_aluguel(self):
    dados_aluguel = self.__tela_aluguel.dados_cadastrar()

    placa = dados_aluguel["carro"]
    carro_certo, carro_verificador = self.__controlador_carro.aluguel(placa)   

    
    nome = dados_aluguel["cliente"]
    cliente_certo, cliente_verificador = self.__controlador_cliente.aluguel(nome)   


    nome = dados_aluguel["funcionario"]
    funcionario_certo, funcionario_verificador = self.__controlador_funcionario.aluguel(nome)   
  
    count = 0
    for codigo in self.__alugueis:
      if codigo.data == dados_aluguel["data"]:
        count = count + 1
    if count == 0: 
      codigo_certo = dados_aluguel["data"]

    verificador = False

    if carro_verificador == 2:
      carro_ja_alugado = True
      if cliente_verificador and  funcionario_verificador == True and count == 0:        
          aluguel = Aluguel(carro_certo, cliente_certo, funcionario_certo, codigo_certo)

          self.__controlador_carro.aluga(carro_certo,aluguel, carro_ja_alugado)
          self.__controlador_cliente.novo(cliente_certo, aluguel)
          self.__controlador_funcionario.novo(funcionario_certo, aluguel)

          self.__alugueis.append(aluguel)
          verificador = True  



    self.__tela_aluguel.cadastro(verificador)


  def lista_alugueis(self):
    for aluguel in self.__alugueis:
      self.__tela_aluguel.mostra_aluguel({"carro": aluguel.carro, "cliente": aluguel.cliente, "funcionario": aluguel.funcionario, "data": aluguel.data})

  def exclui_aluguel(self):
    codigo = self.__tela_aluguel.exclui_aluguel()
    verificador = False
    for aluguel in self.__alugueis:
      if aluguel.data == codigo:
        verificador = True
        self.__controlador_carro.aluga(aluguel.carro,aluguel, False)
        self.__controlador_cliente.remove(aluguel.cliente, aluguel)
        self.__controlador_funcionario.remove(aluguel.funcionario, aluguel)

        self.__alugueis.remove(aluguel)
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