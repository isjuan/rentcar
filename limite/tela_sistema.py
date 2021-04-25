import PySimpleGUI as sg

class TelaSistema():

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Button('Cliente', key='1', size=(20, 1))],
                  [sg.Button('Funcionario', key='2', size=(20, 1))],
                  [sg.Button('Carro', key='3', size=(20, 1))],
                  [sg.Button('Aluguel', key='4', size=(20, 1))],
                  [sg.Button('Finalizar sistema', key='0', size=(20, 1))],
                  ]
        self.__window = sg.Window('HOME').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        return int(botao)

    def close(self):
        self.__window.close()

''' 

class TelaSistema:

  def tela_opcoes(self):
    print("-------- Sistema ---------")
    print("Escolha sua opcao")
    print("1 - Cliente")
    print("2 - Funcionario")
    print("3 - Carro")
    print("4 - Aluguel")
    print("0 - Finalizar sistema")
    
    opcao = self.le_int("Escolha a opcao: ", [1, 2, 3, 4, 0])
    return opcao

  def le_int(self, mensagem: str, intervalo: [] = None):
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
          
'''