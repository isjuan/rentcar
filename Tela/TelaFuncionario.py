class Funcionario():

  def tela_opcoes(self):
    print("-------- Funcionario ----------")
    print("Escolha a opcao")
    print("1 - Incluir funcionario")
    print("2 - Alterar funcionario")
    print("3 - Listar funcionarios")
    print("4 - Excluir funcionario")
    print("5 - Criar aluguel")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

    def dados_cadastrar(self):
    print("-------- INCLUIR FUNCIONARIO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereco: ")

