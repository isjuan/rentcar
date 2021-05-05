import PySimpleGUI as sg

class TelaAluguel():

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [[sg.Button('Criar aluguel', key='1', size=(15, 2)),
               sg.Button('Excluir aluguel', key='3', size=(15, 2))],
              [sg.Button('Listar alugueis', key='2', size=(30, 1))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1))]
              ]
    self.__window = sg.Window('Aluguel').Layout(layout)

  def tela_opcoes(self):
    self.init_components()
    botao, valores = self.__window.Read()
    if botao is None:
      botao = 0
    self.close()
    return int(botao)

  def close(self):
    self.__window.close()

  @property
  def dados_cadastrar(self):

    layout= [[sg.Text('Placa do carro:'), sg.InputText(key= 'placa')],
             [sg.Text('Nome do cliente:'), sg.InputText(key='nome_cliente')],
             [sg.Text('Nome do funcionário:'), sg.InputText(key='nome_funcionario')],
             [sg.Text('Código de registro(único)'), sg.InputText(key='data')],
             [sg.Submit('Registrar Aluguel')]# sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Cadastrar funcionario').Layout(layout)

    botao, valores = self.__window.Read()
    self.close()

    return {"carro": valores['placa'], "cliente": valores['nome_cliente'], "funcionario": valores['nome_funcionario'], "data": valores['data']}
    #return {"carro": placa, "cliente": nome_cliente, "funcionario": nome_funcionario,  "data": data}

  def mostra_aluguel(self, dados_aluguel):
    print("------------------", "\n", "Carro: ", dados_aluguel["carro"])
    print("Cliente: ", dados_aluguel["cliente"])
    print("Funcionario: ", dados_aluguel["funcionario"])
    print("Codigo do aluguel: ", dados_aluguel["data"])

      
  def exclui_aluguel(self):
    codigo = input("Qual o codigo do aluguel?")
    return codigo
  
  def aluguel_erro(self):
    print ("O codigo do aluguel ja esta sendo utilizado!")

  def exclui_aluguel_return(self, bol):
    if bol == False:
      print ("Codigo invalido! Retornando a tela Aluguel")
    if bol == True:
      print ("Aluguel terminado!")

  def cadastro(self, verificador):
    if verificador == False:
      print ("Erro no cadastro! Retornando a tela Aluguel")
    if verificador == True:
      print ("Aluguel criado")
'''
class TelaAluguel():

  def tela_opcoes(self):
    print("-------- Aluguel ----------")
    print("Escolha a opcao")
    print("1 - Criar aluguel")   
    print("2 - Listar alugueis")
    print("3 - Excluir aluguel")
    print("0 - Retornar")

    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 0])
    return opcao

  def le_int(self, mensagem: str = " ", intervalo: [] = None):
    while True:
      lido = input(mensagem)
      try:
        inteiro = int(lido)
        if intervalo and inteiro not in intervalo:
          raise ValueError
        return inteiro
      except ValueError:
        print ("Valor incorreto: Digite um valor valido")
        if intervalo:
          print("Valores validos:", intervalo)

  def dados_cadastrar(self):
    print("-------- CRIAR ALUGUEL ----------")
    placa = input("Insira a placa do carro: ")
    nome_cliente = input("Insira o nome do cliente: ")
    nome_funcionario = input("Insira o nome do funcionario: ")
    data = input("Codigo de registro do aluguel(unico): ")
    return {"carro": placa, "cliente": nome_cliente, "funcionario": nome_funcionario,  "data": data}

  def mostra_aluguel(self, dados_aluguel):
    print("------------------", "\n", "Carro: ", dados_aluguel["carro"])
    print("Cliente: ", dados_aluguel["cliente"])
    print("Funcionario: ", dados_aluguel["funcionario"])
    print("Codigo do aluguel: ", dados_aluguel["data"])

      
  def exclui_aluguel(self):
    codigo = input("Qual o codigo do aluguel?")
    return codigo
  
  def aluguel_erro(self):
    print ("O codigo do aluguel ja esta sendo utilizado!")

  def exclui_aluguel_return(self, bol):
    if bol == False:
      print ("Codigo invalido! Retornando a tela Aluguel")
    if bol == True:
      print ("Aluguel terminado!")

  def cadastro(self, verificador):
    if verificador == False:
      print ("Erro no cadastro! Retornando a tela Aluguel")
    if verificador == True:
      print ("Aluguel criado")

'''