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

    ca_t = False
    for ca in self.__controlador_carro.l_carros():
      if ca.placa == dados_aluguel["carro"] and self.__controlador_carro.alugado(ca) == False:
        carro = ca
        ca_t = True

    
    cl_t = False
    for cl in self.__controlador_cliente.l_clientes():
      if cl.nome == dados_aluguel["cliente"]:
        cliente = cl
        cl_t = True

    fu_t = False
    for fu in self.__controlador_funcionario.l_funcionarios():
      if fu.nome == dados_aluguel["funcionario"]:
        funcionario = fu
        fu_t = True
  
    count = 0
    for i in self.__alugueis:
      if i.data == dados_aluguel["data"]:
        count = count + 1
    if count == 0: 
      da = dados_aluguel["data"]

    r = False
    if ca_t and cl_t and  fu_t == True and count == 0 :
      aluguel = Aluguel(ca, cl, fu, da)
      self.__controlador_carro.aluga(ca,aluguel, ca_t)
      self.__alugueis.append(aluguel)
      r = True  



    self.__tela_aluguel.cadastro(r)


  def lista_alugueis(self):
    for aluguel in self.__alugueis:
      self.__tela_aluguel.mostra_aluguel({"carro": aluguel.carro, "cliente": aluguel.cliente, "funcionario": aluguel.funcionario, "data": aluguel.data})

  def exclui_aluguel(self):
    dt = self.__tela_aluguel.exclui_aluguel()
    bol = False
    for aluguel in self.__alugueis:
      if aluguel.data == dt:
        bol = True
        car = aluguel.carro
        car.aluga(car, aluguel, False)

        self.__alugueis.remove(aluguel)
        self.__tela_aluguel.exclui_aluguel_return(bol)
      
    if bol == False:
        self.__tela_aluguel.exclui_aluguel_return(bol)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_aluguel, 2: self.lista_alugueis, 3:self.exclui_aluguel, 0: self.retorna_tela_principal }

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluguel.tela_opcoes()]()