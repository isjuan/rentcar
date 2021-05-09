import PySimpleGUI as sg

class TelaAluguel():

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [[sg.Button('Criar aluguel', key='1', size=(15, 2), button_color='#008015'),
               sg.Button('Excluir aluguel', key='3', size=(15, 2), button_color='#d5001d')],
              [sg.Button('Listar alugueis', key='2', size=(32, 2))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
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

  


  def dados_cadastrar(self):

    layout= [[sg.Text('Placa do carro:', size=(18, 1)), sg.InputText(key= 'placa')],
             [sg.Text('Nome do cliente:', size=(18, 1)), sg.InputText(key='nome_cliente')],
             [sg.Text('Nome do funcionário:', size=(18, 1)), sg.InputText(key='nome_funcionario')],
             [sg.Text('Código de registro(único)', size=(18, 1)), sg.InputText(key='data')],
             [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Registrar Aluguel', button_color='#008000') ]
    ]
    self.__window = sg.Window('Cadastrar funcionario').Layout(layout)

    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['data'] == None or valores['data'] == '':
      test_none = True

    return {"carro": valores['placa'], "cliente": valores['nome_cliente'], "funcionario": valores['nome_funcionario'], "data": valores['data']}, test_none
  
  
  #BUG



  def mostra_aluguel(self, dados_aluguel):

    layout = [[sg.Text("Os Alugueis são:")]]
    if len(dados_aluguel) > 0:
      contador = 0
      for i in dados_aluguel:
        layout.append([sg.Text("Codigo do aluguel:"), sg.Text(i["data"])])
        layout.append([sg.Text("Carro:"), sg.Text(i["carro"]), sg.Text("Cliente:"),sg.Text(i["cliente"]), sg.Text("Funcionario:"),sg.Text(i["funcionario"])])
        contador = contador + 1
    else:
      layout.append([sg.Text("Sem alugueis ativos!")])
    layout.append([sg.Button('<< Retornar <<', key= self.close(), size=(15, 1), button_color='#500000')])
    self.__window = sg.Window('Listar Alugueisa').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()


  def exclui_aluguel(self):
    layout = [[sg.Text('"Qual o codigo do aluguel?"')],
             [sg.InputText(key='codigo', size=(20,0)), sg.Submit('OK', size=(3, 0), button_color='#008000')],
             [sg.Button('<< Retornar <<', button_color='#500000', key=self.close())]]
    self.__window = sg.Window('Selecionar carro').Layout(layout)
    botao, valores = self.__window.Read()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['codigo'] == None or valores['codigo'] == '':
      test_none = True
    self.close()
    return valores['codigo'], test_none

  def aluguel_erro(self, cliente_verificador, funcionario_verificador, carro_verificador,  codigo_verificador):
    layout = []
    if cliente_verificador == False:
      layout.append([sg.Text('O nome do cliente informado nao foi encontrado!')])


    if funcionario_verificador == False:
      layout.append([sg.Text('O nome do funcionario informado nao foi encontrado!')])
        

    if carro_verificador < 2:
      if carro_verificador == 0:
        layout.append([sg.Text('O placa do carro informado nao foi encontrado!')])
      if carro_verificador == 1:
          layout.append([sg.Text('O carro informado ja esta alugado!')])


    if codigo_verificador != 0:
      layout.append([sg.Text('O codigo do aluguel ja esta sendo utilizado!')])

    layout.append([sg.Button('OK', key=self.close(), size=(5, 1))])
    self.__window = sg.Window('Erro ao criar aluguel').Layout(layout)
    self.__window.Read()
    self.close()

  def exclui_aluguel_return(self, bol):
    if bol == False:
      layout = [[sg.Text('Codigo invalido! Retornando a tela Aluguel')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]]
      self.__window = sg.Window('ERRO').Layout(layout)
      self.__window.Read()
      self.close()

    if bol == True:
      layout = [[sg.Text('Aluguel terminado!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]]
      self.__window = sg.Window('FINISH').Layout(layout)
      self.__window.Read()
      self.close()

  def cadastro(self, verificador):
    if verificador == False:
      layout = [[sg.Text('Erro no cadastro!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]]
      self.__window = sg.Window('ERRO').Layout(layout)
      self.__window.Read()
      self.close()

    if verificador == True:
      layout = [[sg.Text('Aluguel criado')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]]
      self.__window = sg.Window('SUCESS').Layout(layout)
      self.__window.Read()
      self.close()
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