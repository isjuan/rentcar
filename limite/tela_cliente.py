import PySimpleGUI as sg

class TelaCliente():

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [[sg.Button('Incluir cliente', key='1', size=(15, 2), button_color='#008015'),
               sg.Button('Excluir cliente', key='3', size=(15, 2), button_color='#d5001d')],
              [sg.Button('Listar clientes', key='2', size=(32, 2))],
              [sg.Button('Listar alugueis do cliente', key='4', size=(32, 2))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
              ]
    self.__window = sg.Window('Clientes').Layout(layout)

  def tela_opcoes(self):
    self.init_components()
    botao, valores = self.__window.Read()
    if botao is None:
      botao = 0
    self.close()
    return int(botao)



  def dados_cadastrar(self):
    
    layout= [[sg.Text('Nome:', size=(8, 1)), sg.InputText(key= 'nome')],
             [sg.Text('Endereco:', size=(8, 1)), sg.InputText(key='endereco')],
             [sg.Text('Telefone', size=(8, 1)), sg.InputText(key='telefone')],
             [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Cadastrar', button_color='#008000')]
    ]
    self.__window = sg.Window('Cadastrar cliente').Layout(layout)

    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['nome'] == None or valores['nome'] == '':

      test_none = True
    return{"nome": valores['nome'], "telefone": valores['telefone'], "endereco": valores['endereco']}, test_none




  def incluir_cliente_return(self, verificador):
    if verificador == 1:   
      layout= [[sg.Text('Ja existe um cliente com esse nome!', justification='center')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]]
    if verificador == 0:
      layout= [[sg.Text('Cliente cadastrado!', justification='center')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
    if verificador == 2:
      layout= [[sg.Text('Operacao cancelada. Retornando a Tela Cliente.', justification='center')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
  
    self.__window = sg.Window('Incluir cliente').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()



  def close(self):
    self.__window.close()

  def retorna_cliente(self):
    layout= [[sg.Text('Qual o nome do cliente?', justification='center')],
             [sg.InputText(key='nome', size=(20,0)), sg.Submit('OK', size=(3, 0), button_color='#008000')],
             [sg.Cancel('<< Retornar <<', button_color='#500000')]
    ]

    self.__window = sg.Window('Selecionar cliente').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == 'Cancelar' or valores['nome'] == None:

      test_none = True
    return {"nome": valores['nome']}, test_none

  def exclui_cliente_return(self, verificador):
    if verificador == 0:
     layout= [[sg.Text('Nome invalido! Retornando a tela Cliente')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 1:
     layout= [[sg.Text('O cliente tem um aluguel ativo! Falha ao remover.')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 2:
     layout= [[sg.Text('Cliente removido do cadastro!')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador != 9:
      self.__window = sg.Window('Exclui cliente').Layout(layout)
      botao, valores = self.__window.Read()
      self.close()



  def lista_alugueis(self, test_none: bool, lis: list):
    if test_none == False:
      total = len(lis)
      if total == 0:
        layout= [[sg.Text('Nenhum aluguel com o nome de cliente informado!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]
                ]
      else:
        contador = 0
        layout= [[sg.Text("Os alugueis desse cliente são:")]]
        for i in lis:
          layout.append([sg.Text("Aluguel"), sg.Text(contador)])

          layout.append([sg.Text("Placa do carro:"), sg.Text(i.carro.placa), sg.Text("Funcionario:"),sg.Text(i.funcionario.nome), sg.Text("Codigo:"),sg.Text(i.data)])   

          
      self.__window = sg.Window('Listar alugueis').Layout(layout)
      botao, valores = self.__window.Read()
      self.close()

  def mostrar_cliente(self, dados_cliente):
    layout = [[sg.Text("Os clientes cadastrados são:")]]
    if len(dados_cliente) > 0:
      contador = 0
      for i in dados_cliente:
        layout.append([sg.Text("Cliente"), sg.Text(contador)])
        layout.append([sg.Text("Nome:"), sg.Text(i[0]), sg.Text("Telefone:"),sg.Text(i[1]), sg.Text("Endereco:"),sg.Text(i[2])])   
        contador = contador + 1 
    else:
      layout.append([sg.Text("Nenhum funcionario cadastrado!")])
    layout.append([sg.Button('<< Retornar <<', key= self.close(), size=(15, 1), button_color='#500000')])
    self.__window = sg.Window('Listar clientes').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()


