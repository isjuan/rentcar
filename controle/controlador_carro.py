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
    for carro in self.__carro:
      self.__tela_carro.mostra_carro({"placa": carro.placa, "modelo": carro.modelo, "cor": carro.cor})



  def exclui_carro(self):
    pc = self.__tela_carro.exclui_carro()
    bol = False
    for carro in self.__carro:
      if carro.placa == pc:
        bol = True
        self.__carro.delete(carro)
        self.__tela_carro.exclui_carro_return(bol)
      
    if bol == False:
        self.__tela_carro.exclui_carro_return(bol)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    #Atenção: código incompleto: adicionar funcões para todas as opções da tela
    lista_opcoes = {1: self.incluir_carro, 2: self.lista_carros, 3:self.exclui_carro, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_carro.tela_opcoes()]()