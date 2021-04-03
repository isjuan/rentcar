from Controlador.ControladorAluguel import ControladorAluguel
from Controlador.ControladorCarro import ControladorCarro
from Controlador.ControladorCliente import ControladorCliente
from Controlador.ControladorFuncionario import ControladorFuncionario
from Tela.TelaSistema import TelaSistema

class ControladorSistema:

  def __init__(self):
    self.__controlador_carro = ControladorCarro(self)
    self.__controlador_funcionario = ControladorFuncionario(self)
    self.__controlador_cliente = ControladorCliente(self)
    self.__controlador_aluguel = ControladorAluguel(self)
    self.__tela_sistema = TelaSistema()

  def inicializa_sistema(self):
    self.abre_tela()
  
  def cadastrar_aluguel(self):
    self.__controlador_aluguel

  def cadastrar_carro(self):
    self.__controlador_carro
    
  def cadastrar_cliente(self):
    self.__controlador_cliente

  def cadastrar_funcionario(self):
    self.__controlador_funcionario

  def encerra_sistema(self):
    exit(0)
    
  def abre_tela(self):
    opcao_escolhida = self.__tela_sistema.tela_opcoes()
    lista_opcoes = {1: self.__controlador_cliente, 2: self.__controlador_funcionario, 3: self.__controlador_carro, 4: self.__controlador_aluguel, 0: self.encerra_sistema}

    while True:
      opcao_escolhida = self.__tela_sistema.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()