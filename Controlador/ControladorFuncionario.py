from Tela.TelaFuncionario import TelaFuncionario
from Entidade.Funcionario import Funcionario

class ControladorFuncionario:
  
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__funcionarios = []
    self.__tela_funcionario = TelaFuncionario()


  def incluir_cliente(self):
    dados_funcionario = self.__tela_funcionario.dados_cadastrar()

    funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["telefone"], dados_funcionario["endereco"])

    self.__funcionarios.append(funcionario)