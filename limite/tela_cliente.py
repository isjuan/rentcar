class TelaCliente():

  def tela_opcoes(self):
    print("-------- Cliente ----------")
    print("Escolha a opcao")
    print("1 - Incluir cliente")
    print("2 - Alterar cliente")
    print("3 - Listar clientes")
    print("4 - Excluir cliente")
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
    print("-------- INCLUIR CLIENTE ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")
    if nome != str or telefone != int or endereco != str:
      print ("Dados invalidos! Cadastre novamente")
      self.dados_cadastrar()

  def mostra_cliente(self, dados_cliente):
    print("Nome do cliente: ", dados_cliente["nome"])
    print("Telefone: ", dados_cliente["telefone"])
    print("Endereco: ", dados_cliente["endereco"])