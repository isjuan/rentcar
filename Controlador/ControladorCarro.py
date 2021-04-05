from Tela.TelaCarro import TelaCarro
from Entidade.Carro import Carro

class ControladorCarro:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__carros = []
    self.__tela_carro = TelaCarro()


  def incluir_carro(self):
    dados_carro = self.__tela_carro.dados_cadastrar()

    carro = Carro(dados_carro["placa"], dados_carro["modelo"], dados_carro["cor"])

    self.__carros.append(carro)
