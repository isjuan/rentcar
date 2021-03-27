class TelaCarro():

  def tela_opcoes(self):
    print("-------- Carro ----------")
    print("Escolha a opcao")
    print("1 - Incluir carro")
    print("2 - Alterar carro")
    print("3 - Listar carros")
    print("4 - Excluir carro")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

    def dados_cadastrar(self):
    print("-------- INCLUIR FUNCIONARIO ----------")
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")