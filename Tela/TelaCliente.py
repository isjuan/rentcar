class TelaCliente():

  def tela_opcoes(self):
    print("-------- Cliente ----------")
    print("Escolha a opcao")
    print("1 - Incluir cliente")
    print("2 - Alterar cliente")
    print("3 - Listar clientes")
    print("4 - Excluir cliente")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def dados_cadastrar(self):
    print("-------- INCLUIR CLIENTE ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")

  def mostra_cliente(self, dados_cliente):
    print("Nome do cliente: ", dados_cliente["nome"])
    print("Telefone: ", dados_cliente["telefone"])
    print("Endereco: ", dados_cliente["endereco"])