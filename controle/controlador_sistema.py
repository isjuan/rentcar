from controle.controlador_aluguel import ControladorAluguel
from controle.controlador_carro import ControladorCarro
from controle.controlador_cliente import ControladorCliente
from controle.controlador_funcionario import ControladorFuncionario
from limite.tela_sistema import TelaSistema

class ControladorSistema:

  def __init__(self):
    self.__controlador_carro = ControladorCarro(self)
    self.__controlador_funcionario = ControladorFuncionario(self)
    self.__controlador_cliente = ControladorCliente(self)
    self.__tela_sistema = TelaSistema()
    self.__controlador_aluguel = ControladorAluguel(self, self.__controlador_cliente, self.__controlador_funcionario, self.__controlador_carro)

  
    
  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_cliente, 2: self.cadastrar_funcionario, 3: self.cadastrar_carro, 4: self.cadastrar_aluguel, 0: self.encerra_sistema}

    while True:
      opcao_escolhida = self.__tela_sistema.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()

  def inicializa_sistema(self):
    self.abre_tela()
  
  def cadastrar_aluguel(self):
    self.__controlador_aluguel.abre_tela()

  def cadastrar_carro(self):
    self.__controlador_carro.abre_tela()
    
  def cadastrar_cliente(self):
    self.__controlador_cliente.abre_tela()

  def cadastrar_funcionario(self):
    self.__controlador_funcionario.abre_tela()

  def encerra_sistema(self):
    exit(0)