import PySimpleGUI as sg

class TelaFuncionario():

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [#[sg.Listbox(values=('funcionario 2', 'funcionario3'), size=(30, 3))],
              [sg.Button('Incluir funcionario', key='1', size=(15, 2), button_color='#008015'),
               sg.Button('Excluir funcionario', key='3', size=(15, 2), button_color='#d5001d')],
              [sg.Button('Listar funcionarios', key='2', size=(32, 2))],
              [sg.Button('Listar alugueis do funcionario', key='4', size=(32, 2))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
              ]
    self.__window = sg.Window('Funcionarios').Layout(layout)

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
    self.__window = sg.Window('Cadastrar funcionario').Layout(layout)

    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == '<< Retornar <<' or valores['nome'] == None or valores['nome'] == '':

      test_none = True
    return{"nome": valores['nome'], "telefone": valores['telefone'], "endereco": valores['endereco']}, test_none

  def incluir_funcionario_return(self, verificador):
    if verificador == 1:   
      layout= [[sg.Text('Ja existe um funcionario com esse nome!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]]
    if verificador == 0:
      layout= [[sg.Text('Funcionario cadastrado!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
    if verificador == 2:
      layout= [[sg.Text('Operacao cancelada. Retornando a Tela Funcionario.')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]
  
    self.__window = sg.Window('Incluir funcionario').Layout(layout)
    self.__window.Read()
    self.close()

  def close(self):
    self.__window.close()

  def retorna_funcionario(self):
    layout= [[sg.Text('Qual o nome do funcionario?')],
             [sg.InputText(key='nome'), sg.Submit('OK', size=(3, 0), button_color='#008000')],
             [sg.Cancel('<< Retornar <<', button_color='#500000')]
    ]

    self.__window = sg.Window('Selecionar funcionario').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()
    test_none = False
    if botao == None or botao == '<< Retornar <<' or valores['nome'] == None:

      test_none = True
    return {"nome": valores['nome']}, test_none

  def exclui_funcionario_return(self, verificador):
    if verificador == 0:
     layout= [[sg.Text('Nome invalido! Retornando a tela Funcionario')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 1:
     layout= [[sg.Text('O funcionario tem um aluguel ativo! Falha ao remover.')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]
    if verificador == 2:
     layout= [[sg.Text('Funcionario removido do cadastro!')],
              [sg.Button('OK', key=self.close(), size=(5, 1))]
              ]

    self.__window = sg.Window('Exclui funcionario').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()


    

  def lista_alugueis(self, test_none: bool, lis: list):
    if test_none == False:
      total = len(lis)
      if total == 0:
        layout= [[sg.Text('Nenhum aluguel com o nome de funcionario informado!')],
                [sg.Button('OK', key=self.close(), size=(5, 1))]
                ]
      else:
        contador = 0
        layout= [[sg.Text("Os alugueis desse funcionario são:")]]
        for i in lis:
          layout.append([sg.Text("Aluguel"), sg.Text(contador)])

          layout.append([sg.Text("Placa do carro:"), sg.Text(i.carro.placa), sg.Text("Cliente:"),sg.Text(i.cliente.nome), sg.Text("Codigo do aluguel:"),sg.Text(i.data)])   

          
      self.__window = sg.Window('Listar alugueis').Layout(layout)
      botao, valores = self.__window.Read()
      self.close()

  def mostrar_funcionario(self, dados_funcionario):
    layout = [[sg.Text("Os funcionarios cadastrados são:")]]
    if len(dados_funcionario) > 0:
      contador = 0
      for i in dados_funcionario:
        layout.append([sg.Text("Funcionario"), sg.Text(contador)])
        layout.append([sg.Text("Nome:"), sg.Text(i[0]), sg.Text("Telefone:"),sg.Text(i[1]), sg.Text("Endereco:"),sg.Text(i[2])])   
        contador = contador + 1 
    else:
      layout.append([sg.Text("Nenhum funcionario cadastrado!")])
    layout.append([sg.Button('<< Retornar <<', key= self.close(), size=(15, 1), button_color='#500000')])
    self.__window = sg.Window('Listar funcionarios').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()