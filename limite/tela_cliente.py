import PySimpleGUI as sg

class TelaCliente():

  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [#[sg.Listbox(values=('cliente 2', 'cliente3'), size=(30, 3))],
              [sg.Button('Incluir cliente', key='1', size=(15, 2)),
               sg.Button('Excluir cliente', key='3', size=(15, 2))],
              [sg.Button('Listar clientes', key='2', size=(30, 2))],
              [sg.Button('Listar alugueis do cliente', key='4', size=(30, 1))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1))]
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
    
    layout= [[sg.InputText('joao', key= 'nome')],
             [sg.InputText('Endereco', key='endereco')],
             [sg.InputText('Telefone', key='telefone')],
             [sg.Submit('Cadastrar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Cadastrar cliente').Layout(layout)

    botao, valores = self.__window.Read()
    #   return {"nome": nome, "telefone": telefone, "endereco": endereco}
    self.close()
    return{"nome": valores['nome'], "telefone": valores['telefone'], "endereco": valores['endereco']}

  def close(self):
    self.__window.close()

  def retorna_cliente(self):
    layout= [[sg.Text('Qual o nome do cliente?')],
             [sg.InputText('joao', key='nome')],
             [sg.Submit('Enter'), sg.Cancel('Cancelar')]
    ]

    self.__window = sg.Window('Selecionar cliente').Layout(layout)
    botao, valores = self.__window.Read()
    self.close()
    return {"nome": valores['nome']}

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

    self.__window = sg.Window('Exclui cliente').Layout(layout)
    botao, valores = self.__window.Read()

  def aluguel_erro(self):
    layout= [[sg.Text('O nome do cliente informado nao foi encontrado!')],
             [sg.Button('OK', key=self.close(), size=(5, 1))]
             ]
    self.__window = sg.Window('Erro ao criar aluguel').Layout(layout)
    botao, valores = self.__window.Read()

  def lista_alugueis(self, lis: list):
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

  def mostrar_cliente(self, dados_cliente):
    layout = [[sg.Text("Os clientes cadastrados são:")]]
    if len(dados_cliente) > 0:
      contador = 0
      for i in dados_cliente:
        layout.append([sg.Text("Cliente"), sg.Text(contador)])
        layout.append([sg.Text("Nome:"), sg.Text(i[0]), sg.Text("Telefone:"),sg.Text(i[1]), sg.Text("Endereco:"),sg.Text(i[2])])   
        contador = contador + 1 
layout.append([sg.Button('<< Retornar <<', key= self.close(), size=(15, 1))])

    self.__window = sg.Window('Listar clientes').Layout(layout)
    botao, valores = self.__window.Read()

  def incluir_cliente_return(self, verificador):
    if verificador == True:   
      layout= [[sg.Text('Ja existe um cliente com esse nome!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]]
    if verificador == False:
      layout= [[sg.Text('Cliente cadastrado!')],
               [sg.Button('OK', key=self.close(), size=(5, 1))]
               ]

    self.__window = sg.Window('Incluir cliente').Layout(layout)
    botao, valores = self.__window.Read()


