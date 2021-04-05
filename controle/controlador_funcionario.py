from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()

  def l_funcionarios(self):
    return self.__funcionarios

  def incluir_funcionario(self):
    dados_funcionario = self.__tela_funcionario.dados_cadastrar()

    funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["telefone"], dados_funcionario["endereco"])

    self.__funcionarios.append(funcionario)

  def lista_funcionarios(self):
    for funcionario in self.__funcionarios:
      self.__tela_funcionario.mostrar_funcionario({"nome": funcionario.nome, "telefone": funcionario.telefone, "endereco": funcionario.endereco})



  def exclui_funcionario(self):
    pc = self.__tela_funcionario.exclui_funcionario()
    bol = False
    for funcionario in self.__funcionarios:
      if funcionario.nome == pc:
        bol = True
        self.__funcionarios.remove(funcionario)
        self.__tela_funcionario.exclui_funcionario_return(bol)
      
    if bol == False:
        self.__tela_funcionario.exclui_funcionario_return(bol)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    lista_opcoes = {1: self.incluir_funcionario, 2: self.lista_funcionarios, 3:self.exclui_funcionario, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_funcionario.tela_opcoes()]()