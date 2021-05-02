from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionario:

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()
    self.__funcionarios.append(Funcionario("n", "t", "e"))
  
  def l_funcionarios(self):
    return self.__funcionarios

  def novo(self,funcionario, aluguel):
    funcionario.novo(aluguel)

  def remove(self,funcionario, aluguel):
    funcionario.remove(aluguel)
  
  def lista_alugueis(self):
    lista_nome, test_none = self.__tela_funcionario.retorna_funcionario()
    lista = []
    if test_none == False:
      nome = lista_nome["nome"]
      for funcionario in self.__funcionarios:
        if funcionario.nome == nome:
          lista = funcionario.lista()
    self.__tela_funcionario.lista_alugueis(test_none, lista)

  def aluguel(self, nome_certa):
    funcionario_verificador  = False
    for funcionario in self.l_funcionarios():
      if funcionario.nome == nome_certa:
        funcionario_certo = funcionario
        funcionario_verificador = True
    if funcionario_verificador == False:
      funcionario_certo = 0
    return funcionario_certo, funcionario_verificador

  def aluguel_erro(self):
    self.__tela_funcionario.aluguel_erro()

  def incluir_funcionario(self):
    dados_funcionario, test_none = self.__tela_funcionario.dados_cadastrar()
    verificador = 2
    if test_none == False:
      nome_funcionario = dados_funcionario["nome"]
      for funcionario in self.__funcionarios:
        if nome_funcionario == funcionario.nome:
          verificador = 1
      if verificador == 2:
        verificador = 0
        funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["telefone"], dados_funcionario["endereco"])
        self.__funcionarios.append(funcionario)
    self.__tela_funcionario.incluir_funcionario_return(verificador)
    

    

  def lista_funcionarios(self):
    temp = []
    for funcionario in self.__funcionarios:
      a = [funcionario.nome, funcionario.telefone, funcionario.endereco]
      temp.append(a)
    self.__tela_funcionario.mostrar_funcionario(temp)
    

  def exclui_funcionario(self):
    lista_nome, test_none = self.__tela_funcionario.retorna_funcionario()
    if test_none == False:
      nome = lista_nome["nome"]
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
    lista_opcoes = {1: self.incluir_funcionario, 2: self.lista_funcionarios, 3:self.exclui_funcionario, 4:self.lista_alugueis, 0: self.retorna_tela_principal}

    continua = True
    while continua:
      lista_opcoes[self.__tela_funcionario.tela_opcoes()]()