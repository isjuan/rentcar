from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()

  def l_funcionarios(self):
    return self.__funcionarios

  def lista_alugueis(self):
    pc = self.__tela_funcionario.exclui_funcionario()
    for funcionario in self.__funcionarios:
      if funcionario.nome == pc:
        lista = funcionario.lista()
        self.__tela_funcionario.lista_alugueis(lista)

  def novo(self,funcionario, aluguel):
    funcionario.novo(aluguel)

  def remove(self,funcionario, aluguel):
    funcionario.remove(aluguel)

  def incluir_funcionario(self):
    dados_funcionario = self.__tela_funcionario.dados_cadastrar()

    funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["telefone"], dados_funcionario["endereco"])

    self.__funcionarios.append(funcionario)

  def lista_funcionarios(self):
    for funcionario in self.__funcionarios:
      self.__tela_funcionario.mostrar_funcionario({"nome": funcionario.nome, "telefone": funcionario.telefone, "endereco": funcionario.endereco})



  def exclui_funcionario(self):
    nome = self.__tela_funcionario.exclui_funcionario()
    verificador = 0
    for funcionario in self.__funcionarios:
      if funcionario.nome == nome:
        if len(funcionario.lista()) == 0:
          verificador = 2
          self.__funcionarios.remove(funcionario)
        if len(funcionario.lista()) > 0:
          verificador = 1
    self.__tela_funcionario.exclui_funcionario_return(verificador)

  def retorna_tela_principal(self):
    self.__controlador_sistema.inicializa_sistema()



  def abre_tela(self):
    lista_opcoes = {1: self.incluir_funcionario, 2: self.lista_funcionarios, 3:self.exclui_funcionario, 4: self.lista_alugueis, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_funcionario.tela_opcoes()]()