from Tela.TelaSistema import TelaSistema

class ControladorSistema:

  def __init__(self):

    self.__tela_sistema = TelaSistema()

  def inicializa_sistema(self):

    self.abre_tela()
  
  def controlador_aluguel(self):
    pass
    #Instanciar ControladorAluguel

  def controlador_carro(self):
  #ou def cadastra_carro(self):
    pass
    #Instanciar ControladorCarros
    
  def controlador_cliente(self):
  #ou def cadastra_cliente(self):
    pass
    #Instanciar ControladorClientes  

  def controlador_funcionario(self):
  #ou def cadastra_funcionario(self):
    pass
    #Instanciar ControladorFuncionarios

  def abre_tela(self):
    
    opcao_escolhida = self.__tela_sistema.tela_opcoes()

    #precisa criar condicao para a opcao_escolhida