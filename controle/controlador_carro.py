from limite.tela_carro import TelaCarro
from entidade.carro import Carro

class ControladorCarro:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__carros = []
    self.__tela_carro = TelaCarro()
    

  def incluir_carro(self):
    dados_carro = self.__tela_carro.dados_cadastrar()

    carro = Carro(dados_carro["placa"], dados_carro["modelo"], dados_carro["cor"])

    self.__carros.append(carro)

  def lista_carros(self):
    for carro in self.__carros:
      self.__tela_carro.mostrar_carro({"placa": carro.placa, "modelo": carro.modelo, "cor": carro.cor})

  def l_carros(self):
    return self.__carros

  def exclui_carro(self):
    placa = self.__tela_carro.exclui_carro()
    verificador = 0
    for carro in self.__carros:
      if carro.placa == placa:
        if carro.alugado() == False:
          verificador = 2
          self.__carros.remove(carro)
        if carro.alugado() == True:
          verificador = 1
    self.__tela_carro.exclui_carro_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()

  def aluga(self,car, aluguel, r):
    car.aluga(aluguel,r)

  def alugado(self, car):
    return car.alugado()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_carro, 2: self.lista_carros, 3:self.exclui_carro, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_carro.tela_opcoes()]()