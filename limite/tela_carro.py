import PySimpleGUI as sg
class TelaCarro():
    

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [[sg.Button('Incluir carro', key='1', size=(15, 2)),
               sg.Button('Excluir carro', key='3', size=(15, 2))],
              [sg.Button('Listar carros', key='2', size=(30, 2))],
              [sg.Button('Listar aluguel do carro', key='4', size=(30, 2))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1))]
              ]
    self.__window = sg.Window('Carros').Layout(layout)

  def tela_opcoes(self):
    self.init_components()
    botao, valores = self.__window.Read()
    if botao is None:
      botao = 0
    self.close()
    return int(botao)

  def dados_cadastrar(self):
    
    layout= [[sg.Text('Placa:'), sg.InputText(key= 'placa')],
             [sg.Text('Modelo:'), sg.InputText(key='modelo')],
             [sg.Text('Cor'), sg.InputText(key='cor')],
             [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Cadastrar carro').Layout(layout)

    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['placa'] == None or valores['placa'] == '':

      test_none = True
    return{"placa": valores['placa'], "modelo": valores['modelo'], "cor": valores['cor']}, test_none

  def incluir_carro_return(self, verificador):
    if verificador == 0:
      layout= [[sg.Text('Carro cadastrado!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
    if verificador == 1:   
      layout= [[sg.Text('Ja existe um carro com esse placa!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]]
    if verificador == 2:
      layout= [[sg.Text('Operacao cancelada. Retornando a Tela Carro.')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
  
    self.__window = sg.Window('Incluir carro').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()



  def close(self):
    self.__window.close()

  def retorna_carro(self):
    layout= [[sg.Text('Qual o placa do carro?')],
             [sg.InputText(key='placa')],
             [sg.Submit('Enter'), sg.Cancel('Cancelar')]
    ]

    self.__window = sg.Window('Selecionar carro').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['placa'] == None:

      test_none = True
    return {"placa": valores['placa']}, test_none

  def exclui_carro_return(self, verificador):
    if verificador == 0:
     layout= [[sg.Text('Placa invalida! Retornando a tela Carro')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 1:
     layout= [[sg.Text('O carro esta alugado! Falha ao remover.')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 2:
     layout= [[sg.Text('Carro removido do cadastro!')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador != 9:
      self.__window = sg.Window('Exclui carro').Layout(layout)
      botao, valores = self.__window.Read()
      self.close()

  def aluguel_erro(self, carro_verificador):
    if carro_verificador == 0:
      layout= [[sg.Text('O placa do carro informado nao foi encontrado!')],
             [sg.Button('OK', key=self.close(), size=(5, 1))]
             ]
    if carro_verificador == 1:
        layout= [[sg.Text('O carro informado ja esta alugado!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]
                ]
    self.__window = sg.Window('Erro ao criar aluguel').Layout(layout)
    botao, valores = self.__window.Read()


  def mostrar_carro(self, dados_carro):
    layout = [[sg.Text("Os carros cadastrados são:")]]
    if len(dados_carro) > 0:
      contador = 0
      for i in dados_carro:
        layout.append([sg.Text("Carro"), sg.Text(contador)])
        layout.append([sg.Text("Placa:"), sg.Text(i[0]), sg.Text("Modelo:"),sg.Text(i[1]), sg.Text("Cor:"),sg.Text(i[2])])   
        contador = contador + 1 
      layout.append([sg.Button('<< Retornar <<', key= self.close(), size=(15, 1))])

    self.__window = sg.Window('Listar carros').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()

  def lista_alugueis(self, test_none, lista):
    if test_none == False:
      total = len(lista)
      if total == 0:
        layout= [[sg.Text('A placa informada nao pertence a nenhum carro alugado!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]
                ]
      else:        
        layout= [[sg.Text("O aluguel desse carro e:")]]          
        layout.append([sg.Text("Nome do cliente:"), sg.Text(lista[0].cliente.nome), sg.Text("Nome do funcionario:"),sg.Text(lista[0].funcionario.nome), sg.Text("Codigo do aluguel:"),sg.Text(lista[0].data)])   
    
      self.__window = sg.Window('Listar alugueis').Layout(layout)
      botao, valores = self.__window.Read()
      self.close()

'''
class TelaCarro():

  def tela_opcoes(self):
    
    print("-------- Carro ----------")
    print("Escolha a opcao")
    print("1 - Incluir carro")
    print("2 - Listar carros")
    print("3 - Excluir carro")
    print("0 - Retornar")

    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 4, 0])
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
    print("-------- INCLUIR CARRO ----------")
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")  
    return {"placa": placa, "modelo": modelo, "cor": cor}
  
  def mostrar_carro(self, dados_carro):
    print("------------------", "\n", "Modelo do carro: ", dados_carro["modelo"])
    print("Placa: ", dados_carro["placa"])
    print("Cor: ", dados_carro["cor"])
      
  def exclui_carro(self):
    placa = input("Qual a placa do carro?")
    return placa
  
  def exclui_carro_return(self, verificador):
    if verificador == 0:
      print ("Placa invalida! Retornando a tela Carro")
    if verificador == 1:
      print ("O carro está em um aluguel ativo! Falha ao remover.")
    if verificador == 2:
      print ("Carro removido do cadastro!")

  def aluguel_erro(self, carro_verificador):
    if carro_verificador == 0:
      print ("O carro informado nao foi encontrado!")
    if carro_verificador == 1:
      print ("O carro informado ja esta alugado!")

      
'''