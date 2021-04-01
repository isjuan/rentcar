class TelaAluguel():

  def tela_opcoes(self):
    print("-------- Aluguel ----------")
    print("Escolha a opcao")
    print("1 - Criar aluguel")
    print("2 - Excluir aluguel")
    print("3 - Listar alugueis")
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
    carro = input("Carro: ")
    cliente = input("Cliente: ")
    funcionario = input("Funcionario: ")
    data = input("Informacoes adicionais: ")
    if carro != Carro or cliente != Cliente or data != str:
      print ("Dados invalidos! Cadastre novamente")
      self.dados_cadastrar()

  def mostra_aluguel(self, dados_aluguel):
    print("Nome do carro: ", dados_aluguel["carro"])
    print("Nome do cliente: ", dados_aluguel["cliente"])
    print("Nome do funcionario: ", dados_aluguel["funcionario"])
    print("Informacoes adicionais: ", dados_aluguel["data"])