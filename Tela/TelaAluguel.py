class TelaAluguel():

  def tela_opcoes(self):
    print("-------- Aluguel ----------")
    print("Escolha a opcao")
    print("1 - Criar aluguel")
    print("2 - Excluir aluguel")
    print("3 - Listar alugueis")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def dados_cadastrar(self):
    print("-------- CRIAR ALUGUEL ----------")
    Carro = input("Carro: ")
    Cliente = input("Cliente: ")
    Funcionario = input("Funcionario: ")
    data = input("Informacoes adicionais: ")

  def mostra_aluguel(self, dados_aluguel):
    print("Nome do carro: ", dados_aluguel["carro"])
    print("Nome do cliente: ", dados_aluguel["cliente"])
    print("Nome do funcionario: ", dados_aluguel["funcionario"])
    print("Informacoes adicionais: ", dados_aluguel["data"])