from limite.tela_carro import TelaCarro
from entidade.carro import Carro
from daos.dao_carro import CarroDAO


class ControladorCarro:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__dao = CarroDAO()
    self.__tela_carro = TelaCarro()
    self.__dao.add(Carro("n", "t", "e"))
  
  def l_carros(self):
    return self.__dao.get_all()

  def novo(self,carro, aluguel):
    carro.novo(aluguel)

  def remove(self,carro, aluguel):
    carro.remove(aluguel)

  def lista_alugueis(self):
    lista_placa, test_none = self.__tela_carro.retorna_carro()
    lista = []
    if test_none == False:
      placa = lista_placa["placa"]
      carro = self.__dao.get(placa)
      if type(carro) == Carro:
        lista = carro.lista()
    self.__tela_carro.lista_alugueis(test_none, lista)

  def aluguel(self, placa):
    carro_verificador  = 0
    carro = self.__dao.get(placa)
    if type(carro) == Carro:
      carro_verificador = 2
      if carro.alugado() == True:
        carro_verificador = 1
        carro_ = 0
    if carro_verificador != 2:
      carro = 0
    return carro, carro_verificador


  def incluir_carro(self):
    dados_carro, test_none = self.__tela_carro.dados_cadastrar()
    verificador = 2
    if test_none == False:
      placa = dados_carro["placa"]
      carro = self.__dao.get(placa)
      if type(carro) == Carro:
        verificador = 1
      if verificador == 2:
        verificador = 0
      if verificador == 0:
        carro = Carro(dados_carro["placa"], dados_carro["modelo"], dados_carro["cor"])
        self.__dao.add(carro)
    self.__tela_carro.incluir_carro_return(verificador)
  

  

  def lista_carros(self):
    temp = []
    chave = self.__dao.get_all()
    for carro in chave:
      a = [carro.placa, carro.modelo, carro.cor]
      temp.append(a)
    self.__tela_carro.mostrar_carro(temp)
  

  def exclui_carro(self):
    lista_placa, test_none = self.__tela_carro.retorna_carro()
    verificador = 9
    if test_none == False:
      verificador = 0
      placa = lista_placa["placa"]
      carro = self.__dao.get(placa)
      if type(carro) == Carro:
        if self.alugado(carro) == False:
          verificador = 2
          self.__dao.remove(carro)
        if self.alugado(carro) == True:
          verificador = 1
    self.__tela_carro.exclui_carro_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()
  
  
  def aluga(self,car, aluguel, r):
    car.aluga(aluguel,r)

  def alugado(self, carro):
    return carro.alugado()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_carro, 2: self.lista_carros, 3:self.exclui_carro, 4:self.lista_alugueis, 0: self.retorna_tela_principal}
    continua = True
    while continua:
      lista_opcoes[self.__tela_carro.tela_opcoes()]()


'''
class ControladorCarro:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__carros = []
    self.__tela_carro = TelaCarro()
    self.__carros.append(Carro("p","m","c"))
    

  def incluir_carro(self):
    dados_carro = self.__tela_carro.dados_cadastrar()

    carro = Carro(dados_carro["placa"], dados_carro["modelo"], dados_carro["cor"])

    self.__carros.append(carro)

  def lista_carros(self):
    for carro in self.__carros:
      self.__tela_carro.mostrar_carro({"placa": carro.placa, "modelo": carro.modelo, "cor": carro.cor})

  def l_carros(self):
    return self.__carros

  def aluguel(self, placa_certa):
    carro_verificador  = 0
    for carro in self.l_carros():
      if carro.placa == placa_certa:
        carro_certo = carro
        carro_verificador = 2
        if carro_certo.alugado() == True:
          carro_verificador = 1
          carro_certo = 0
    if carro_verificador != 2:
      carro_certo = 0
    return carro_certo, carro_verificador

  def aluguel_erro(self, carro_verificador):
    self.__tela_carro.aluguel_erro(carro_verificador)

  def exclui_carro(self):
    placa = self.__tela_carro.exclui_carro()
    verificador = 0
    for carro in self.__carros:
      if carro.placa == placa:
        if self.alugado(carro) == False:
          verificador = 2
          self.__carros.remove(carro)
        if self.alugado(carro) == True:
          verificador = 1
    self.__tela_carro.exclui_carro_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()

  def aluga(self,car, aluguel, r):
    car.aluga(aluguel,r)

  def alugado(self, carro):
    return carro.alugado()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_carro, 2: self.lista_carros, 3:self.exclui_carro, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_carro.tela_opcoes()]()
'''